from django.shortcuts import render

def homepage(request):
    if request.method == 'GET':
        return render(request, 'homepage.html')
    
def contatos(request):
    if request.method == 'GET':
        return render(request, 'contatos.html')