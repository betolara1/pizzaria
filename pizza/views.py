from django.shortcuts import render
from .models import Pizza

def menu(request):
    if request.method == "GET":
        pizzas = Pizza.objects.all()
        return render(request, 'menu.html', {'pizzas': pizzas})

# Outras visualizações como visualização de pedido, adição de item ao pedido, etc.
