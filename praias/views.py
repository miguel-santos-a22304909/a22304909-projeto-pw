# praias/views.py
from django.shortcuts import render
from .models import Praia
from .models import Regiao
from .models import Servico
# Create your views here.

def index_view(request):
    context = {
        'praiasLisboa' : Praia.objects.filter(regiao__nome = 'Lisboa'),
        'praiasAlgarve': Praia.objects.filter(regiao__nome = 'Algarve'),

    }

    return render(request, "praias/index.html", context)

def praia_view(request, praia_id):
    context = {
        'praia': Praia.objects.get(id=praia_id)
    }
    return render(request, "praias/praia.html", context)


