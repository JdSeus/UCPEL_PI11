from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from ..models import Empresa
# The class DashboardEmpresaController has a method index that returns a render of the template
# dashboard-empresa/index.html if the user passes the test Empresa.user_is_Empresa
class DashboardEmpresaController():

    @user_passes_test(Empresa.user_is_Empresa, login_url='login-empresa')
    def index(request):
        return render(request, 'dashboard-empresa/index.html')