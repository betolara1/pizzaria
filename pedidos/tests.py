from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Sabores, Preco, Pedidos

class PedidosTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testpedidos', password='password123')
        self.sabor1 = Sabores.objects.create(nome='Calabresa')
        self.sabor2 = Sabores.objects.create(nome='Marguerita')
        self.preco_m = Preco.objects.create(tamanho='M', preco=40.0)
        self.cardapio_url = reverse('cardapio')
        self.pedido_url = reverse('pedido')
        self.fechar_url = reverse('fecharpedido')

    def test_cardapio_view(self):
        response = self.client.get(self.cardapio_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cardapio.html')

    def test_pedido_view_autenticado(self):
        self.client.login(username='testpedidos', password='password123')
        response = self.client.get(self.pedido_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pedido.html')

    def test_pedido_view_nao_autenticado(self):
        response = self.client.get(self.pedido_url)
        # Deve redirecionar para login (COM barra)
        self.assertRedirects(response, '/usuarios/login/')

    def test_fechar_pedido_sucesso(self):
        self.client.login(username='testpedidos', password='password123')
        response = self.client.post(self.fechar_url, {
            'tamanho': 'M',
            'sabores': [self.sabor1.id, self.sabor2.id],
            'observacao': 'Teste',
            'entregasim': 'on'
        })
        self.assertEqual(Pedidos.objects.count(), 1)
        pedido = Pedidos.objects.first()
        self.assertEqual(pedido.tamanho, 'M')
        # Preço base (40) + taxa entrega (7) = 47
        self.assertEqual(pedido.preco, 47.0)
        self.assertRedirects(response, self.pedido_url)
