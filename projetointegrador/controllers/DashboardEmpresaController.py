from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from ..models import Empresa
class DashboardEmpresaController():

    def user_is_Empresa(user):
        return user.is_authenticated and isinstance(user, Empresa)

    @user_passes_test(user_is_Empresa, login_url='login-empresa')
    def index(request):
        return render(request, 'dashboard-empresa/index.html')