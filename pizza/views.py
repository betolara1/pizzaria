from django.shortcuts import render
from .models import *

def cardapio(request):
    if request.method == "GET":
        pizzas = Pizza.objects.all()
        return render(request, 'cardapio.html', {'pizzas': pizzas})

