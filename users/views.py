from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.descorators import login_required

def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        username = request.POST.get('username'),
        email = request.POST.get('email'),
        password = request.POST.get('password')
        
        user = User.objects.filter(username=username).first()
        
        if user:
            return HttpResponse('Já existe um usuário com esse username')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        
        return HttpResponse('Usuário cadastrado com sucesso!')
        
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            login_django(request, user)
        
            return HttpResponse('Autenticado')
        else:
            return HttpResponse('Email ou senha inválido')

@login_required(login_url="/user/login/")
def rediowere(request):   #mudar para vincular com o core/home
    return HttpResponse('Encaminhando')