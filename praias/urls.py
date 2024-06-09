from django.urls import path

from . import views

app_name = 'praias'

urlpatterns = [
    path('', views.index_view, name="praias_index"),
    path('praia/<int:praia_id>/', views.praia_view, name="praia"),

]