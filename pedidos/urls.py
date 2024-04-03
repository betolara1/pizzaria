from django.urls import path
from . import views

urlpatterns = [
    path('cardapio/', views.cardapio, name='cardapio'),
    path('pedido/', views.pedido, name='pedido'),
    path('meuspedidos/<int:id>', views.meuspedidos, name='meuspedidos'),
]