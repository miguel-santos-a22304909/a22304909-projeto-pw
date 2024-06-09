# latintext/views.py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_view(request):
    return render(request, "latintext/index.html")

def loremipsum_view(request):
    return render(request, "latintext/loremipsum.html")

def finibus_view(request):
    return render(request, "latintext/finibus.html")

