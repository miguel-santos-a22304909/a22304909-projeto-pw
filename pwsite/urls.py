# pwsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as funções definidas em views.py

app_name = 'pwsite'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('sobre/', views.sobre_view, name='sobre'),
    path('interesses/', views.interesses_view, name='interesses'),
]