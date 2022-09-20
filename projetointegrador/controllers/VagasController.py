from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404


from ..helpers import dd

from pprint import pprint

from ..models import Vaga
from ..models import Aplicacao
from ..models import Usuario
from ..models import Curriculo

class VagasController():

    def index(request):
        vagas = Vaga.objects.filter(publicar=True)

        # dump_data = dd(request, vagas)
        # return HttpResponse(dump_data)

        return render(request, 'vagas/index.html', {
            'vagas': vagas
        })

    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
    def vaga(request, vaga_id):

        usuario = Usuario.objects.select_related('curriculo').get(id=request.user.id)

        if usuario.curriculo is None:
            curriculo = Curriculo()
            curriculo.save()
            usuario.curriculo = curriculo
            usuario.save()

        vaga = get_object_or_404(Vaga, id=vaga_id)

        if vaga.publicar is False:
            return HttpResponseNotFound()     

        aplicacao = Aplicacao.objects.filter(vagas__id=vaga_id, curriculos__id=usuario.curriculo.id)

        return render(request, 'vaga/index.html', {
            'vaga': vaga,
            'aplicacao': aplicacao
        })

    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
    def aplicar_em_vaga(request, vaga_id):

        usuario = Usuario.objects.select_related('curriculo').get(id=request.user.id)

        vaga = get_object_or_404(Vaga, id=vaga_id)

        if vaga.publicar is False:
            return HttpResponseNotFound()   

        if usuario.curriculo is None:
            curriculo = Curriculo()
            curriculo.save()
            usuario.curriculo = curriculo
            usuario.save()

        aplicacao = Aplicacao.objects.filter(vagas__id=vaga_id, curriculos__id=usuario.curriculo.id)

        if aplicacao is None:
            aplicacao = Aplicacao()
            aplicacao.vagas.add(vaga)
            aplicacao.curriculos.add(usuario.curriculo)
            aplicacao.save()

        return redirect('vaga', vaga.id)