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
    path('ajax/remover-escolaridade/<int:escolaridade_id>', views.ajax_remover_escolaridade, name='ajax-remover-escolaridade')
]