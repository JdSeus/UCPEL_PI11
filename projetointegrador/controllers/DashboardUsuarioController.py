from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from ..models import Usuario
class DashboardUsuarioController():

    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
    def index(request):
        return render(request, 'dashboard-usuario/index.html')