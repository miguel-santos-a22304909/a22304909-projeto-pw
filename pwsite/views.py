# pwsite/views.py
from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request, "pwsite/index.html")

def interesses_view(request):
    return render(request, "pwsite/interesses.html")

def sobre_view(request):
    return render(request, "pwsite/sobre.html")