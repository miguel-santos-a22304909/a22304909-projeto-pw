from django.urls import path

from . import views

app_name = 'ensinosuperior'

urlpatterns = [
    path('', views.index_view, name="ensinosuperior_index"),
    path('disciplina/<int:disciplina_id>/', views.disciplina_view, name="disciplina"),
    path('projeto/<int:projeto_id>/', views.projeto_view, name="projeto"),

]