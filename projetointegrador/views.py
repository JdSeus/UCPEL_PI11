from .controllers.UsuarioController import UsuarioController
from .controllers.EmpresaController import EmpresaController
from .controllers.HomeController import HomeController
from .controllers.DashboardUsuarioController import DashboardUsuarioController
from .controllers.DashboardEmpresaController import DashboardEmpresaController
from .controllers.CheckDashboardController import CheckDashboardController


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

def login_empresa(request):
    return EmpresaController.login_empresa(request)

def logout_empresa(request):
    return EmpresaController.logout_empresa(request)

def register_empresa(request):
    return EmpresaController.register_empresa(request)

def dashboard_empresa(request):
    return DashboardEmpresaController.index(request)

def check_dashboard(request):
    return CheckDashboardController.index(request)