from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

from ..models import Empresa

class EmpresaController():

    def login_empresa(request):
        if request.user.is_authenticated:
            return redirect('check-dashboard')

        if request.method != 'POST':
            return render(request, 'login-empresa/index.html')

        cnpj = request.POST.get('cnpj')
        senha = request.POST.get('senha')

        if not cnpj or not senha:
            messages.error(request, 'Nenhum campo pode estar vazio.')
            return render(request, 'login-empresa/index.html')

        try:
            empresa = Empresa.objects.get(cnpj=cnpj)
        except Empresa.DoesNotExist:
            messages.error(request, 'Usuário não existe')
            return render(request, 'login-empresa/index.html')

        ispasswordcorrect = check_password(senha, empresa.password)

        if not ispasswordcorrect:
            messages.error(request, 'Senha incorreta')
            return render(request, 'login-empresa/index.html')

        auth_login(request, empresa, 'projetointegrador.backend.EmpresaBackend')
        return redirect('dashboard-empresa')

    def logout_empresa(request):
        auth_logout(request)
        return redirect('home')

    def register_empresa(request):
        if request.user.is_authenticated:
            return redirect('check-dashboard')
            
        if request.method != 'POST':
            return render(request, 'register-empresa/index.html')

        nome_social = request.POST.get('nome_social')
        cnpj = request.POST.get('cnpj')
        senha = request.POST.get('senha')
        senha2 = request.POST.get('senha2')

        if not nome_social or not cnpj or not senha or not senha2:
            messages.error(request, 'Nenhum campo pode estar vazio.')
            return render(request, 'register-empresa/index.html')

        if len(senha) < 6:
            messages.error(request, 'Senha precisa ter 6 caracteres ou mais.')
            return render(request, 'register-empresa/index.html')

        if senha != senha2:
            messages.error(request, 'Senhas não conferem')
            return render(request, 'register-empresa/index.html')

        if Empresa.objects.filter(cnpj=cnpj).exists():
            messages.error(request, 'Usuário já existe.')
            return render(request, 'register-empresa/index.html')

        empresa = Empresa.objects.create(nome_social=nome_social, cnpj=cnpj, password=senha)

        hashedpassword = make_password(senha)
        empresa.password = hashedpassword

        empresa.save()

        auth_login(request, empresa, 'projetointegrador.backend.EmpresaBackend')
        return redirect('dashboard-empresa')
