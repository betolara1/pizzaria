from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.messages import constants
from .models import *

def cardapio(request):
    if request.method == "GET":
        cardapios = Cardapio.objects.all()
        return render(request, 'cardapio.html', {'cardapios': cardapios})
    

def pedido(request):
    if not request.user.is_authenticated:
        return redirect('/usuarios/login')
    
    if request.method == 'GET':
        sabores = Sabores.objects.all()
        tamanho = Pedidos.TAMANHO

        return render(request, 'pedido.html', { 'sabores' : sabores, 'tamanho': tamanho, })
    

    elif request.method == 'POST':
        nome = request.POST.get('nome')
        tamanho = request.POST.get('tamanho')
        observacao = request.POST.get('observacao')
        sabores_ids = request.POST.getlist('sabores')

        usuario = request.user

        pedido = Pedidos(
            nome=nome,
            tamanho=tamanho,
            observacao=observacao,
            usuario=usuario,
        )

        pedido.save()

        for sabor_id in sabores_ids:
            sabor = Sabores.objects.get(id=int(sabor_id))
            pedido.sabores.add(sabor)

        messages.add_message(
            request, constants.SUCCESS, 'Pedido realizado com sucesso'
        )
        return redirect('/pedidos/pedido')
    

def meuspedidos(request, id):
    if not request.user.is_authenticated:
        return redirect('/usuarios/login')
    
    if request.method == "GET":
        return render(request, 'meuspedidos.html')
    
    elif request.method == 'POST':
        pass