from django.urls import path
from . import views

app_name = 'meteo'

urlpatterns = [
    path('lisboa/', views.tempo_lisboa_view, name='tempo_lisboa'),

]