from django.shortcuts import render
from .models import *

def cardapio(request):
    if request.method == "GET":
        cardapios = Cardapio.objects.all()
        return render(request, 'cardapio.html', {'cardapios': cardapios})
    

def pedido(request):
    if request.method == 'GET':
        sabores = Sabores.objects.all()
        tamanho = Pedidos.TAMANHO

        return render(request, 'pedido.html', { 'sabores' : sabores, 'tamanho': tamanho, })
    

