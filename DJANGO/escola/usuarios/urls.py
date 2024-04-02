from django.urls import path
from . import views
from django.contrib.auth import views as autViews

urlpatterns = [
    path('login', autViews.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('unlogin',views.unlogin, name='unlogin'),
    path('registrarUsuario',views.registrarUsuario, name='registrarUsuario'),
]
