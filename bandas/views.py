# bandas/views.py
from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from .models import Musica
from .models import Banda
from .models import Album
from .forms import BandaForm
from .forms import MusicaForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index_view(request):
    context = {
        'bandas': Banda.objects.all().order_by('nome'),
    }
    return render(request, "bandas/index.html", context)

def banda_view(request, banda_id):
    context = {
        'banda': Banda.objects.get(id=banda_id)
    }
    return render(request, "bandas/banda.html", context)

def album_view(request, album_id):
    context = {
        'album': Album.objects.get(id=album_id)
    }
    return render(request, "bandas/album.html", context)

def musica_view(request, musica_id):
    context = {
        'musica': Musica.objects.get(id=musica_id)
    }
    return render(request, "bandas/musica.html", context)



@login_required
def nova_banda_view(request):

    form = BandaForm(request.POST or None, request.FILES)      # form é uma instancia de BandaForm, request.FILES deve ser incluido se forem enviados ficheiros ou imagens


    if form.is_valid():
        form.save()
        return redirect('bandas:bandas_index')

    context = {'form': form}
    return render(request, 'bandas/nova_banda.html', context)

@login_required
def edita_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)

    if request.POST:
        form = BandaForm(request.POST or None, request.FILES, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('bandas:bandas_index')
    else:
        form = BandaForm(instance=banda)  # cria formulário com dados da instância

    context = {'form': form, 'banda':banda}
    return render(request, 'bandas/edita_banda.html', context)

@login_required
def apaga_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    banda.delete()
    return redirect('bandas:bandas_index')



@login_required
def nova_musica_view(request):

    form = MusicaForm(request.POST or None)      # form é uma instancia de MusicaForm


    if form.is_valid():
        form.save()
        return redirect('bandas:bandas_index')

    context = {'form': form}
    return render(request, 'bandas/nova_musica.html', context)

@login_required
def edita_musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    album_id = musica.album.id

    if request.POST:
        form = MusicaForm(request.POST or None, instance = musica) # Passa a instância da música existente
        if form.is_valid():
            form.save()
            return redirect('bandas:album',album_id=album_id)
    else:
        form = MusicaForm(instance=musica)  # cria formulário com dados da instância

    context = {'form': form, 'musica': musica}
    return render(request, 'bandas/edita_musica.html', context)

@login_required
def apaga_musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    album_id = musica.album.id
    musica.delete()
    return redirect('bandas:album',album_id=album_id)


