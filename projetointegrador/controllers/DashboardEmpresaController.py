from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

class DashboardEmpresaController():

    @login_required(login_url='login-empresa')
    def index(request):
        return render(request, 'dashboard-empresa/index.html')