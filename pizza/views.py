from django.shortcuts import render
from .models import *

def cardapio(request):
    if request.method == "GET":
        cardapios = Cardapio.objects.all()
        return render(request, 'cardapio.html', {'cardapios': cardapios})

