from django.urls import path

from . import views

app_name = 'bandas'

urlpatterns = [
    path('', views.index_view, name="bandas_index"),
    path('banda/<int:banda_id>/', views.banda_view, name="banda"),
    path('album/<int:album_id>/', views.album_view, name="album"),
    path('musica/<int:musica_id>/', views.musica_view, name="musica"),
    path('banda/nova', views.nova_banda_view, name="nova_banda"),
    path('banda/<int:banda_id>/edita', views.edita_banda_view,name="edita_banda"),
    path('banda/<int:banda_id>/apaga', views.apaga_banda_view,name="apaga_banda"),
    path('musica/nova', views.nova_musica_view,name="nova_musica"),
    path('musica/<int:musica_id>/edita', views.edita_musica_view,name="edita_musica"),
    path('musica/<int:musica_id>/apaga', views.apaga_musica_view,name="apaga_musica"),
]