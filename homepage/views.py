from django.shortcuts import redirect, render

def homepage(request):
    if request.method == 'GET':
        return render(request, 'homepage.html')
    
