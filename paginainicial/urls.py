from django.urls import path
from . import views

app_name = 'paginainicial'

urlpatterns = [
    path('', views.paginainicial_view, name='paginainicial'),
]
