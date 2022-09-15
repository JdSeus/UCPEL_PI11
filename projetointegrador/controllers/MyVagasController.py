from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.http import HttpResponseForbidden

from ..models import Empresa
from ..models import Vaga

from ..forms import VagaForm
from ..forms import VagaFormEdit

from ..helpers import dd

from pprint import pprint

class MyVagasController():

    @user_passes_test(Empresa.user_is_Empresa, login_url="login-empresa")
    def index(request):

        empresa = Empresa.objects.get(id=request.user.id)

        return render(request, 'minhas-vagas/index.html', {'empresa': empresa})


    @user_passes_test(Empresa.user_is_Empresa, login_url="login-empresa")
    def ajax_adicionar_vaga(request):

        empresa = Empresa.objects.get(id=request.user.id)

        if request.method == "POST":
            form = VagaForm(request.POST)
            if form.is_valid():

                titulo = form.cleaned_data.get("titulo")
                descricao = form.cleaned_data.get("descricao")
                
                categorias = form.cleaned_data.get("categoria")

                vaga = Vaga.objects.create(titulo=titulo, descricao=descricao, concluida=0, publicar=1)

                for categoria in categorias:
                    vaga.categoria.add(categoria)

                vaga.save()

                empresa.vagas.add(vaga)
                empresa.save()

                return HttpResponse(status=204, headers={'HX-Trigger': 'vagaListChanged'})
        else:
            form = VagaForm()
        return render(request, 'generic_form.html', {
            'form': form,
            'title': "Adicionar Vaga"
        })

    @user_passes_test(Empresa.user_is_Empresa, login_url="login-empresa")
    def ajax_editar_vaga(request, vaga_id):

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

        if request.method == "POST":
            form = VagaFormEdit(request.POST)
            if form.is_valid():

                titulo = form.cleaned_data.get("titulo")
                descricao = form.cleaned_data.get("descricao")
                publicar = form.cleaned_data.get("publicar")
                concluida = form.cleaned_data.get("concluida")
                
                categorias = form.cleaned_data.get("categoria")

                Vaga.objects.filter(id=auxvaga.id).update(titulo=titulo, descricao=descricao, concluida=concluida, publicar=publicar)

                vaga = Vaga.objects.get(id=auxvaga.id)

                vaga.categoria.clear()

                for categoria in categorias:
                    vaga.categoria.add(categoria)

                vaga.save()

                return HttpResponse(status=204, headers={'HX-Trigger': 'vagaListChanged'})
        else:
            form = VagaFormEdit(instance=auxvaga)

        return render(request, 'generic_form.html', {
            'title': "Editar Vaga: ",
            'form': form
        })