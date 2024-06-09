# pwsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as funções definidas em views.py

app_name = 'latintext'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('loremipsum/', views.loremipsum_view, name='loremipsum'),
    path('finibus/', views.finibus_view, name='finibus'),
]