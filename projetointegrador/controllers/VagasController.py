from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
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

    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
    def index(request):

        usuario = Usuario.objects.select_related('curriculo').get(id=request.user.id)

        if usuario.curriculo is None:
            curriculo = Curriculo()
            curriculo.save()
            usuario.curriculo = curriculo
            usuario.save()

        vagas = Vaga.objects.filter(publicar=True)

        aplicacoes = Aplicacao.objects.prefetch_related('vagas').filter(curriculos__id=usuario.curriculo.id)

        for idx, vaga in enumerate(vagas):
            setattr(vagas[idx], "has_vaga", False)
            setattr(vagas[idx], "result", False)
            for aplicacao in aplicacoes:
                if (aplicacao.vagas.count() > 0):
                    for vaga_em_aplicacao in aplicacao.vagas.all():
                        if (vaga_em_aplicacao.id == vaga.id):
                            setattr(vagas[idx], "has_vaga", True)
                            setattr(vagas[idx], "result", aplicacao.status)

        return render(request, 'vagas/index.html', {
            'vagas': vagas,
            'aplicacoes': aplicacoes,
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
        aplicacao = aplicacao.first()

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
        aplicacao = aplicacao.first()

        if aplicacao is None:
            aplicacao = Aplicacao()
            aplicacao.save()
            aplicacao.vagas.add(vaga)
            aplicacao.curriculos.add(usuario.curriculo)
            aplicacao.save()

        return redirect('vaga', vaga.id)

    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
    def desaplicar_em_vaga(request, vaga_id):

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
        aplicacao = aplicacao.first()

        if aplicacao is None:
            return redirect('vaga', vaga.id)

        aplicacao.delete()
        return redirect('vaga', vaga.id)