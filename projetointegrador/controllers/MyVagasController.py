from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

from ..models import Empresa

class MyVagasController():

    @user_passes_test(Empresa.user_is_Empresa, login_url="login-empresa")
    def index(request):

        empresa = Empresa.objects.get(id=request.user.id)

        return render(request, 'minhas-vagas/index.html', {'empresa': empresa})