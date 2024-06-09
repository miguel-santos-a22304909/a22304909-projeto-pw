# noobsite/views.py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")

def favoritegame_view(request):
    return HttpResponse("Olá n00b, o meu jogo favorito é o Destiny 2!")

def ola_view(request):
    return HttpResponse("Olá")

