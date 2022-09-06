from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

class DashboardUsuarioController():

    @login_required(login_url='login-usuario')
    def index(request):
        return render(request, 'dashboard-usuario/index.html')