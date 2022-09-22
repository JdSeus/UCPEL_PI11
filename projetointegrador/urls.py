from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('cadastro-usuario', views.register_usuario, name='register-usuario'),
    path('login-usuario', views.login_usuario, name='login-usuario'),
    path('logout-usuario', views.logout_usuario, name='logout-usuario'),
    path('dashboard-usuario', views.dashboard_usuario, name='dashboard-usuario'),
    path('cadastro-empresa', views.register_empresa, name='register-empresa'),
    path('login-empresa', views.login_empresa, name='login-empresa'),
    path('logout-empresa', views.logout_empresa, name='logout-empresa'),
    path('dashboard-empresa', views.dashboard_empresa, name='dashboard-empresa'),
    path('check-dashboard', views.check_dashboard, name='check-dashboard'),
    path('curriculo', views.curriculo, name='curriculo'),
    path('ajax/editar-endereco', views.ajax_editar_endereco, name='ajax-editar-endereco'),
    path('ajax/adicionar-telefone', views.ajax_adicionar_telefone, name='ajax-adicionar-telefone'),
    path('ajax/editar-telefone/<int:telefone_id>', views.ajax_editar_telefone, name='ajax-editar-telefone'),
    path('ajax/remover-telefone/<int:telefone_id>', views.ajax_remover_telefone, name='ajax-remover-telefone'),
    path('ajax/adicionar-link', views.ajax_adicionar_link, name='ajax-adicionar-link'),
    path('ajax/editar-link/<int:link_id>', views.ajax_editar_link, name='ajax-editar-link'),
    path('ajax/remover-link/<int:link_id>', views.ajax_remover_link, name='ajax-remover-link'),
    path('ajax/adicionar-escolaridade', views.ajax_adicionar_escolaridade, name='ajax-adicionar-escolaridade'),
    path('ajax/editar-escolaridade/<int:escolaridade_id>', views.ajax_editar_escolaridade, name='ajax-editar-escolaridade'),
    path('ajax/remover-escolaridade/<int:escolaridade_id>', views.ajax_remover_escolaridade, name='ajax-remover-escolaridade'),
    path('ajax/adicionar-historico', views.ajax_adicionar_historico, name='ajax-adicionar-historico'),
    path('ajax/editar-historico/<int:historico_id>', views.ajax_editar_historico, name='ajax-editar-historico'),
    path('ajax/adicionar-curso', views.ajax_adicionar_curso, name='ajax-adicionar-curso'),
    path('ajax/editar-curso/<int:curso_id>', views.ajax_editar_curso, name='ajax-editar-curso'),
    path('ajax/remover-curso/<int:curso_id>', views.ajax_remover_curso, name='ajax-remover-curso'),
    path('minhas-vagas', views.my_vagas, name='minhas-vagas'),
    path('ajax/adicionar-vaga', views.ajax_adicionar_vaga, name='ajax-adicionar-vaga'),
    path('ajax/editar-vaga/<int:vaga_id>', views.ajax_editar_vaga, name='ajax-editar-vaga'),
    path('ajax/remover-vaga/<int:vaga_id>', views.ajax_remover_vaga, name='ajax-remover-vaga'),
    path('vagas', views.vagas, name='vagas'),
    path('vaga/<int:vaga_id>', views.vaga, name='vaga'),
    path('aplicar-em-vaga/<int:vaga_id>', views.aplicar_em_vaga, name='aplicar-em-vaga'),
    path('desaplicar-em-vaga/<int:vaga_id>', views.desaplicar_em_vaga, name='desaplicar-em-vaga'),
    path('aplicacao/<int:vaga_id>', views.aplicacao, name='aplicacao'),
    path('ajax/curriculo/<int:curriculo_id>', views.ajax_ver_curriculo, name='ajax-ver-curriculo'),
    path('ajax/aplicacao/<int:aplicacao_id>', views.ajax_responder_aplicacao, name='ajax-responder-aplicacao'),
]