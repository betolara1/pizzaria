from django.http import JsonResponse
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
        tamanho = Preco.TAMANHO
        preco = Preco.objects.all()

        tamanho_selecionado = request.GET.get('tamanho')
        #preco = Preco.objects.get(tamanho=tamanho_selecionado).valor

        return render(request, 'pedido.html', { 'sabores' : sabores, 'tamanho': tamanho, 'preco' : preco, })
    

    elif request.method == 'POST':
        nome = request.POST.get('nome')
        tamanho = request.POST.get('tamanho')
        observacao = request.POST.get('observacao')
        sabores_ids = request.POST.getlist('sabores')
        preco = request.POST.get('preco')

        usuario = request.user

        pedido = Pedidos(
            nome=nome,
            tamanho=tamanho,
            observacao=observacao,
            usuario=usuario,
            status='1',
            preco = preco,
        )

        pedido.save()

        for sabor_id in sabores_ids:
            sabor = Sabores.objects.get(id=int(sabor_id))
            pedido.sabores.add(sabor)

        messages.add_message(
            request, constants.SUCCESS, 'Pedido realizado com sucesso'
        )
        return redirect('/pedidos/pedido')
    

def meuspedidos(request):
    if not request.user.is_authenticated:
        return redirect('/usuarios/login')
    
    if request.method == "GET":
        pedido = Pedidos.objects.all()

        return render(request, 'meuspedidos.html', {'pedido' : pedido, })
