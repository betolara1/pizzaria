from django.db import models

class Pizza(models.Model):
    TAMANHOS = [
        ['Broto', '4 pedaços'],
        ['Pequena', '6 pedaços'],
        ['Média', '8 pedaços'],
        ['Grande', '12 pedaços'],
        ['Familia', '16 pedaços']
    ]

    nome = models.CharField(max_length=100)
    ingredientes = models.TextField()
    preço = models.DecimalField(max_digits=5, decimal_places=2)
    tamanho = models.CharField(max_length=10, choices=TAMANHOS)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    cliente = models.CharField(max_length=100)
    pizzas = models.ManyToManyField(Pizza)
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Pedido de {self.cliente}"
