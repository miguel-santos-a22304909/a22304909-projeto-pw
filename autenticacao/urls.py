from django.urls import path

from . import views

app_name = 'autenticacao'

urlpatterns = [
    path('registo/', views.registo_view, name="registo"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]