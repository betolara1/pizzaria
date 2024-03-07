from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contatos/', views.contatos, name='contatos'),
    path('sobre/', views.sobre, name='sobre'),
]
