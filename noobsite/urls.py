# noobsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

urlpatterns = [
    path('index/', views.index_view),
    path('jogofavorito/', views.favoritegame_view),
    path('ola/', views.ola_view),

]