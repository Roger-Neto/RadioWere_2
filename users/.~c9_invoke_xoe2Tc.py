from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

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
        us