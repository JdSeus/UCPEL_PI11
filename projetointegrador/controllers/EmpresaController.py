from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

from ..models import Empresa

class EmpresaController():

    def login_empresa(request):
        """
        It checks if the user is already logged in, if it's not, it checks if the request method is
        POST, if it is, it gets the cnpj and password from the request, checks if they are empty, if
        they are not, it tries to get the user from the database, if it doesn't exist, it shows an error
        message, if it does, it checks if the password is correct, if it's not, it shows an error
        message, if it is, it logs the user in and redirects to the dashboard
        
        :param request: The current request object
        :return: the render of the login-empresa/index.html page.
        """
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
        # It's logging out the user and redirecting to the home page.
        auth_logout(request)
        return redirect('home')

    def register_empresa(request):
        # It's checking if the user is already logged in, if it is, it redirects to the dashboard, if
        # it's not, it checks if the request method is POST, if it is, it gets the nome_social, cnpj,
        # senha and senha2 from the request, checks if they are empty, if they are not, it checks if
        # the senha is less than 6 characters, if it is, it shows an error message, if it's not, it
        # checks if the senha and senha2 are the same, if they are not, it shows an error message, if
        # they are, it checks if the cnpj already exists, if it does, it shows an error message, if it
        # doesn't, it creates a new user with the nome_social, cnpj and senha, it hashes the password,
        # saves the user and logs the user in.
        
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
