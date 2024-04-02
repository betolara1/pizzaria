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

        print("IDs dos sabores do formulário:", sabores_ids)

        pedido = Pedidos(
            nome=nome,
            tamanho=tamanho,
            observacao=observacao,
        )

        pedido.save()

        for sabor_id in sabores_ids:
            sabor = Sabores.objects.get(id=int(sabor_id))  # Converta o ID para inteiro
            pedido.sabores.add(sabor)

        messages.add_message(
            request, constants.SUCCESS, 'Pedido realizado com sucesso'
        )
        return redirect('/pizza/pedido')
    

