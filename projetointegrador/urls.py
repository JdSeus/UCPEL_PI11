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
    path('ajax/remover-telefone', views.ajax_remover_telefone, name='ajax-remover-telefone')
]