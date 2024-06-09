# ensinosuperior/views.py
from django.shortcuts import render
from .models import *
from .models import Curso
from .models import AreaCientifica
from .models import Disciplina
from .models import Projeto
from .models import LinguagemProgramacao
# Create your views here.

def index_view(request):
    context = {
        'curso': Curso.objects.get(nome = 'Engenharia Informática'),
    }
    return render(request, "ensinosuperior/index.html", context)

def disciplina_view(request, disciplina_id):
    context = {
        'disciplina': Disciplina.objects.get(id=disciplina_id)
    }
    return render(request, "ensinosuperior/disciplina.html", context)

def projeto_view(request, projeto_id):
    context = {
        'projeto': Projeto.objects.get(id=projeto_id)
    }
    return render(request, "ensinosuperior/projeto.html", context)


