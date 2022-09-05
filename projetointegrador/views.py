from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required
from .models import Usuario


def index(request):
    return render(request, 'home/index.html')

def login(request):
    if request.method != 'POST':
        return render(request, 'login/index.html')

    email = request.POST.get('email')
    senha = request.POST.get('senha')

    if not email or not senha:
        messages.error(request, 'Nenhum campo pode estar vazio.')

    try: 
        validate_email(email)
    except:
        messages.error(request, 'Email inválido')
        return render(request, 'login/index.html')

    try:
        usuario = Usuario.objects.get(email=email)
    except Usuario.DoesNotExist:
        messages.error(request, 'Usuário não existe')
        return render(request, 'login/index.html')

    messages.success(request, 'Login Realizado com sucesso.')
    auth_login(request, usuario, 'projetointegrador.backend.UsuarioBackend')
    return redirect('dashboard-usuario')

def logout(request):
    auth_logout(request)
    return redirect('index')

def register(request):
    if request.method != 'POST':
        return render(request, 'register/index.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not email or not senha or not senha2:
        messages.error(request, 'Nenhum campo pode estar vazio.')

    try: 
        validate_email(email)
    except:
        messages.error(request, 'Email inválido')
        return render(request, 'register/index.html')

    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter 6 caracteres ou mais.')
        return render(request, 'register/index.html')

    if senha != senha2:
        messages.error(request, 'Senhas não conferem')
        return render(request, 'register/index.html')

    if Usuario.objects.filter(email=email).exists():
        messages.error(request, 'Usuário já existe.')
        return render(request, 'register/index.html')

    usuario = Usuario.objects.create(nome=nome, sobrenome=sobrenome, email=email, senha=senha)

    usuario.save()

    messages.success(request, 'Registrado com sucesso! Agora faça login.')

    return redirect('home')

@login_required(login_url='login')
def dashboard_usuario(request):
    return render(request, 'dashboard-usuario/index.html')