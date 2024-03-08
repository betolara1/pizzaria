from django.urls import path
from . import views

urlpatterns = [
    path('cardapio/', views.cardapio, name='cardapio'),
    
]
