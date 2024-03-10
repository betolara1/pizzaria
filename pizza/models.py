from django.db import models

class Cardapio(models.Model):
    imagem = models.ImageField(upload_to='imagens_pizzas/')
    
    def __str__(self):
        return self.imagem.name

class Pedido(models.Model):
    cliente = models.CharField(max_length=100)
    pizzas = models.ManyToManyField(Cardapio)
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Pedido de {self.cliente}"

class Tamanhos(models.Model):
    TAMANHOS = [
        ['Broto', '4 pedaços'],
        ['Pequena', '6 pedaços'],
        ['Média', '8 pedaços'],
        ['Grande', '12 pedaços'],
        ['Familia', '16 pedaços']
    ]
    preço = models.DecimalField(max_digits=5, decimal_places=2)
    tamanho = models.CharField(max_length=10, choices=TAMANHOS)

    def __str__(self):
        return self.tamanho
    
