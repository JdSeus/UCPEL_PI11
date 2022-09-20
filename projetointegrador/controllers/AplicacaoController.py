from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from ..models import Empresa

class AplicacaoController():

    @user_passes_test(Empresa.user_is_Empresa, login_url='login-empresa')
    def index(request, vaga_id, aplicacao_id):
        return render(request, 'aplicacao/index.html')