from .controllers.UsuarioController import UsuarioController
from .controllers.EmpresaController import EmpresaController
from .controllers.HomeController import HomeController
from .controllers.DashboardUsuarioController import DashboardUsuarioController
from .controllers.DashboardEmpresaController import DashboardEmpresaController
from .controllers.CheckDashboardController import CheckDashboardController
from .controllers.CurriculoController import CurriculoController

from .forms import NameForm

from django.shortcuts import render
from django.http import HttpResponse

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

def curriculo(request):
    return CurriculoController.index(request)

def ajax_editar_endereco(request):
    return CurriculoController.ajax_editar_endereco(request)

def ajax_adicionar_telefone(request):
    return CurriculoController.ajax_adicionar_telefone(request)

def ajax_editar_telefone(request, telefone_id):
    return CurriculoController.ajax_editar_telefone(request, telefone_id)

def ajax_remover_telefone(request, telefone_id):
    return CurriculoController.ajax_remover_telefone(request, telefone_id)

def ajax_adicionar_link(request):
    return CurriculoController.ajax_adicionar_link(request)

def ajax_editar_link(request, link_id):
    return CurriculoController.ajax_editar_link(request, link_id)

def ajax_remover_link(request, link_id):
    return CurriculoController.ajax_remover_link(request, link_id)

def ajax_adicionar_escolaridade(request):
    return CurriculoController.ajax_adicionar_escolaridade(request)