from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden

from ..forms import AplicacaoForm

from ..models import Aplicacao
from ..models import Empresa
from ..models import Usuario

from ..helpers import dd

from pprint import pprint

# The index method of the AplicacaoController class is a view that returns a list of applications for
# a specific job
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

        aplicacoes = Aplicacao.objects.prefetch_related('vagas', 'curriculos').filter(vagas__id=auxvaga.id)
        
        usuarios_e_aplicacao = []
        for aplicacao in aplicacoes:
            for curriculo in aplicacao.curriculos.all():
                usuario = Usuario.objects.get(curriculo_id=curriculo.id)
                if usuario is not None:
                    usuarios_e_aplicacao.append([usuario, aplicacao])  


        return render(request, 'aplicacao/index.html', {
            'vaga': auxvaga,
            'usuarios_e_aplicacao': usuarios_e_aplicacao,
        })

    @user_passes_test(Empresa.user_is_Empresa, login_url='login-empresa')

    def ajax_responder_aplicacao(request, aplicacao_id):
        """
        It checks if the user is an Empresa, if it is, it checks if the user has the vaga that the
        aplicacao is applying to, if it does, it renders the form
        
        :param request: The current request object
        :param aplicacao_id: The id of the aplicacao that is being responded to
        :return: A form with the title "Responder Aplicacao: " and the form.
        """

        empresa = Empresa.objects.get(id=request.user.id)

        aplicacao = get_object_or_404(Aplicacao, id=aplicacao_id)

        aplicacao_vagas = aplicacao.vagas.all()

        vagas = empresa.vagas.all()

        user_has_vaga = False

        for aplicacao_vaga in aplicacao_vagas:
            for vaga in vagas:
                if vaga.id == aplicacao_vaga.id:
                    user_has_vaga = True
                    break

        if user_has_vaga == False:
            return HttpResponseForbidden()

        if request.method == "POST":
            form = AplicacaoForm(request.POST)
            if form.is_valid():

                status = form.cleaned_data.get("status")
                resposta = form.cleaned_data.get("resposta")

                aplicacao = Aplicacao.objects.filter(id=aplicacao.id).update(status=status, resposta=resposta)

                return HttpResponse(status=204, headers={'HX-Trigger': 'aplicacaoListChanged'})
        else:
            form = AplicacaoForm(instance=aplicacao)

        return render(request, 'generic_form.html', {
            'title': "Responder Aplicacao: ",
            'form': form
        })