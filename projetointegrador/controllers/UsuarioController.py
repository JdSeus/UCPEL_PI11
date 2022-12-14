from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from django.core.validators import validate_email


from ..models import Usuario

class UsuarioController():

    def login_usuario(request):
        if request.user.is_authenticated:
            return redirect('check-dashboard')

        if request.method != 'POST':
            return render(request, 'login-usuario/index.html')

        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if not email or not senha:
            messages.error(request, 'Nenhum campo pode estar vazio.')
            return render(request, 'login-usuario/index.html')

        try: 
            validate_email(email)
        except:
            messages.error(request, 'Email inválido')
            return render(request, 'login-usuario/index.html')

        try:
            usuario = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            messages.error(request, 'Usuário não existe')
            return render(request, 'login-usuario/index.html')

        ispasswordcorrect = check_password(senha, usuario.password)

        if not ispasswordcorrect:
            messages.error(request, 'Senha incorreta')
            return render(request, 'login-usuario/index.html')

        auth_login(request, usuario, 'projetointegrador.backend.UsuarioBackend')
        
        return redirect('dashboard-usuario')

    def logout_usuario(request):
        auth_logout(request)
        return redirect('home')

    def register_usuario(request):
        if request.user.is_authenticated:
            return redirect('check-dashboard')

        if request.method != 'POST':
            return render(request, 'register-usuario/index.html')

        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        senha2 = request.POST.get('senha2')

        if not nome or not sobrenome or not email or not senha or not senha2:
            messages.error(request, 'Nenhum campo pode estar vazio.')
            return render(request, 'register-usuario/index.html')

        try: 
            validate_email(email)
        except:
            messages.error(request, 'Email inválido')
            return render(request, 'register-usuario/index.html')

        if len(senha) < 6:
            messages.error(request, 'Senha precisa ter 6 caracteres ou mais.')
            return render(request, 'register-usuario/index.html')

        if senha != senha2:
            messages.error(request, 'Senhas não conferem')
            return render(request, 'register-usuario/index.html')

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já existe.')
            return render(request, 'register-usuario/index.html')

        usuario = Usuario.objects.create(nome=nome, sobrenome=sobrenome, email=email, password=senha)

        hashedpassword = make_password(senha)
        usuario.password = hashedpassword
        
        usuario.save()

        auth_login(request, usuario, 'projetointegrador.backend.UsuarioBackend')
        return redirect('dashboard-usuario')
