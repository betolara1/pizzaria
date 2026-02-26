from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class UsuariosTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.cadastro_url = reverse('cadastro')
        self.login_url = reverse('login')
        self.username = 'testuser'
        self.password = 'testpassword123'
        self.email = 'test@example.com'

    def test_cadastro_view_get(self):
        response = self.client.get(self.cadastro_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cadastro.html')

    def test_cadastro_usuario_sucesso(self):
        response = self.client.post(self.cadastro_url, {
            'username': self.username,
            'senha': self.password,
            'confirmar_senha': self.password,
            'email': self.email
        })
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, self.username)
        # Redireciona para login após sucesso
        self.assertRedirects(response, self.login_url)

    def test_cadastro_senhas_diferentes(self):
        response = self.client.post(self.cadastro_url, {
            'username': self.username,
            'senha': self.password,
            'confirmar_senha': 'wrongpassword',
            'email': self.email
        })
        self.assertEqual(User.objects.count(), 0)
        self.assertRedirects(response, self.cadastro_url)

    def test_login_usuario_sucesso(self):
        User.objects.create_user(username=self.username, password=self.password)
        response = self.client.post(self.login_url, {
            'username': self.username,
            'senha': self.password
        })
        self.assertRedirects(response, '/')
        # Verifica se o usuário está logado
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_login_usuario_falha(self):
        response = self.client.post(self.login_url, {
            'username': 'wronguser',
            'senha': 'wrongpassword'
        })
        # Verifique se redireciona para a URL COM barra
        self.assertRedirects(response, self.login_url)
        self.assertFalse('_auth_user_id' in self.client.session)
