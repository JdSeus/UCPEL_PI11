from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.http import HttpResponseForbidden

from ..models import Empresa

from ..helpers import dd

from pprint import pprint

class AplicacaoController():

    @user_passes_test(Empresa.user_is_Empresa, login_url='login-empresa')
    def index(request, vaga_id):

        empresa = Empresa.objects.get(id=request.user.id)

        vagas = empresa.vagas.all()

        userHasVaga = False
        auxvaga = None

        for vaga in vagas:
            if vaga.id == vaga_id:
                userHasVaga = True
                auxvaga = vaga
                break

        if userHasVaga == False:
            return HttpResponseForbidden()

        return render(request, 'aplicacao/index.html', {
            'vaga': auxvaga
        })