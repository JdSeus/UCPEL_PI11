from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('cadastro-usuario', views.register_usuario, name='register-usuario'),
    path('login-usuario', views.login_usuario, name='login-usuario'),
    path('logout-usuario', views.logout_usuario, name='logout-usuario'),
    path('dashboard-usuario', views.dashboard_usuario, name='dashboard-usuario'),
]