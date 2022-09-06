from .controllers.UsuarioController import UsuarioController
from .controllers.HomeController import HomeController
from .controllers.DashboardUsuarioController import DashboardUsuarioController


def index(request):
    return HomeController.index(request)

def login_usuario(request):
    return UsuarioController.login_usuario(request)

def logout_usuario(request):
    return UsuarioController.logout_usuario(request)

def register_usuario(request):
    return UsuarioController.register_usuario(request)

def dashboard_usuario(request):
    return DashboardUsuarioController.index(request)