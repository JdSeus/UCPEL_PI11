from .controllers.UsuarioController import UsuarioController
from .controllers.EmpresaController import EmpresaController
from .controllers.HomeController import HomeController
from .controllers.DashboardUsuarioController import DashboardUsuarioController
from .controllers.DashboardEmpresaController import DashboardEmpresaController
from .controllers.CheckDashboardController import CheckDashboardController
from .controllers.CurriculoController import CurriculoController
from .controllers.MyVagasController import MyVagasController
from .controllers.VagasController import VagasController
from .controllers.AplicacaoController import AplicacaoController

def index(request):
    if request.user.is_authenticated:
        return CheckDashboardController.index(request)
    else:
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

def ajax_editar_escolaridade(request, escolaridade_id):
    return CurriculoController.ajax_editar_escolaridade(request, escolaridade_id)

def ajax_remover_escolaridade(request, escolaridade_id):
    return CurriculoController.ajax_remover_escolaridade(request, escolaridade_id)

def ajax_adicionar_historico(request):
    return CurriculoController.ajax_adicionar_historico(request)

def ajax_editar_historico(request, historico_id):
    return CurriculoController.ajax_editar_historico(request, historico_id)

def ajax_adicionar_curso(request):
    return CurriculoController.ajax_adicionar_curso(request)

def ajax_editar_curso(request, curso_id):
    return CurriculoController.ajax_editar_curso(request, curso_id)

def ajax_remover_curso(request, curso_id):
    return CurriculoController.ajax_remover_curso(request, curso_id)

def my_vagas(request):
    return MyVagasController.index(request)

def ajax_adicionar_vaga(request):
    return MyVagasController.ajax_adicionar_vaga(request)

def ajax_editar_vaga(request, vaga_id):
    return MyVagasController.ajax_editar_vaga(request, vaga_id)

def ajax_remover_vaga(request, vaga_id):
    return MyVagasController.ajax_remover_vaga(request, vaga_id)

def vagas(request):
    return VagasController.index(request)

def vaga(request, vaga_id):
    return VagasController.vaga(request, vaga_id)

def aplicar_em_vaga(request, vaga_id):
    return VagasController.aplicar_em_vaga(request, vaga_id)

def desaplicar_em_vaga(request, vaga_id):
    return VagasController.desaplicar_em_vaga(request, vaga_id)

def aplicacao(request, vaga_id):
    return AplicacaoController.index(request, vaga_id)

def ajax_ver_curriculo(request, curriculo_id):
    return CurriculoController.ajax_ver_curriculo(request, curriculo_id)

def ajax_responder_aplicacao(request, aplicacao_id):
    return AplicacaoController.ajax_responder_aplicacao(request, aplicacao_id)