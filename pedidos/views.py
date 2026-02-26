from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from .models import *

def cardapio(request):
    if request.method == "GET":
        cardapios = Cardapio.objects.all()
        return render(request, 'cardapio.html', {'cardapios': cardapios})
    
def pedido(request):
    if not request.user.is_authenticated:
        return redirect('/usuarios/login/')
    
    sabores = Sabores.objects.all()
    tamanho = Preco.TAMANHO

    if request.method == 'GET':
        return render(request, 'pedido.html', { 'sabores' : sabores, 'tamanho': tamanho,})

    
@login_required  
def fecharpedido(request):
    if request.method == 'POST':
        tamanho = request.POST.get('tamanho')
        observacao = request.POST.get('observacao')
        sabores_ids = request.POST.getlist('sabores')
        entrega = request.POST.get('entregasim')

        solicitacao_preco = Preco.objects.all()
        for p in solicitacao_preco:
            if tamanho in p.tamanho:
                preco = p.preco

        if entrega:
            preco = preco + 7

        usuario = request.user

        pedido = Pedidos(
            nome=usuario,
            tamanho=tamanho,
            observacao=observacao,
            usuario=usuario,
            status='1',
            preco = preco,
            entrega='S',
        )

        pedido.save()

        for sabor_id in sabores_ids:
            sabor = Sabores.objects.get(id=int(sabor_id))
            pedido.sabores.add(sabor)

        messages.add_message(
            request, constants.SUCCESS, 'Pedido realizado com sucesso'
        )

        return redirect('/pedidos/pedido/')


@login_required
def meuspedidos(request):
    if not request.user.is_authenticated:
        return redirect('/usuarios/login/')
    
    if request.method == "GET":
        pedido = Pedidos.objects.all()

        return render(request, 'meuspedidos.html', {'pedido' : pedido, })


@login_required
def excluirpedido(request, pedido_id):
    pedido = Pedidos.objects.get(id=pedido_id)

    if not pedido.usuario == request.user:
        messages.add_message(request, constants.ERROR, 'Esse pedido não é seu')
        return redirect('/pedidos/meuspedidos/')

    pedido.delete()
    messages.add_message(request, constants.SUCCESS, 'Pedido excluido com sucesso')
    return redirect('/pedidos/meuspedidos/')
    
