from django.db import models
from django.contrib.auth.models import User

class Cardapio(models.Model):
    imagem = models.ImageField(upload_to='imagens_pizzas/')
    
    def __str__(self):
        return self.imagem.name


class Sabores(models.Model):
    nome = models.CharField(max_length = 50)

    def __str__(self):
        return self.nome


class Pedidos(models.Model):
    TAMANHO = (
        ('B', 'Broto'),
        ('P', 'Pequena'),
        ('M', 'Média'),
        ('G', 'Grande'),
        ('F', 'Família'),
    )

    nome = models.CharField(max_length=50, null=False)
    tamanho = models.CharField(max_length=1, choices=TAMANHO)
    sabores = models.ManyToManyField(Sabores)
    observacao = models.CharField(max_length=100, null=True)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    
    def __str__(self):
        return self.nome