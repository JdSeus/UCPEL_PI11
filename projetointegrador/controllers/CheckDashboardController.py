from django.shortcuts import redirect

from ..models import Empresa
from ..models import Usuario

class CheckDashboardController():
    # It checks if the user is logged in and if it is an instance of Empresa, if it is, it redirects to
    # the dashboard-empresa page
    def user_is_Empresa(user):
        return user.is_authenticated and isinstance(user, Empresa)

    def index(request):
        if isinstance(request.user, Usuario):
            return redirect('dashboard-usuario')
        elif isinstance(request.user, Empresa):
            return redirect('dashboard-empresa')
        else:
            return redirect('home')