from django.shortcuts import render
from .models import Contato

def homepage(request):
    if request.method == 'GET':
        return render(request, 'homepage.html')
    
def contatos(request):
    if request.method == 'GET':
        contatos = Contato.objects.all()
        return render(request, 'contatos.html', {'contatos' : contatos, }, )
    
def sobre(request):
    if request.method == 'GET':
        return render(request, 'sobre.html')