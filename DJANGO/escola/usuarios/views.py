from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm

def unlogin(requests):
    logout(requests)
    return HttpResponseRedirect(reverse('index'))

def registrarUsuario(requests):
    if requests.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=requests.POST)
        
        if form.is_valid():
            novoUsuario = form.save()
            
            usuarioAutenticado = authenticate(username=novoUsuario,password= requests.POST['password1'])
            
            return HttpResponseRedirect(reverse('index'))
    
    contexto = {'form':form}
    
    return render(requests,'usuarios/registrarUsuario.html',contexto)
# Create your views here.


