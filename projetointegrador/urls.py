from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('cadastro', views.register, name='register'),
    path('logar', views.login, name='login'),
    path('dashboard-usuario', views.dashboard_usuario, name='dashboard-usuario'),
]