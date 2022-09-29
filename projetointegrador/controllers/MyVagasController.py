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
        """
        If the user is not logged in, redirect to the login page. If the user is logged in, but is not an
        Empresa, redirect to the login page. If the user is logged in and is an Empresa, render the index
        page
        
        :param request: The request object
        :return: The index view is returning a render of the index.html template.
        """

        empresa = Empresa.objects.get(id=request.user.id)

        return render(request, 'minhas-vagas/index.html', {'empresa': empresa})


    @user_passes_test(Empresa.user_is_Empresa, login_url="login-empresa")
        
    def ajax_adicionar_vaga(request):
        """
        It creates a new Vaga object, adds it to the Empresa object, and then returns a 204 status code with
        a custom header
        
        :param request: The request object
        :return: A form to add a new job vacancy.
        """

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
        """
        It checks if the user is an empresa, if it is, it checks if the user has the vaga, if it does, it
        checks if the request is a POST, if it is, it checks if the form is valid, if it is, it updates the
        vaga and returns a 204 status code, if it isn't, it returns the form, if the request isn't a POST,
        it returns the form
        
        :param request: The request object
        :param vaga_id: The id of the vaga that will be edited
        :return: A HttpResponse object with a status code of 204.
        """

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

    @user_passes_test(Empresa.user_is_Empresa, login_url="login-empresa")
        
    def ajax_remover_vaga(request, vaga_id):
        """
        If the user is logged in as an Empresa, and the request is a POST, then delete the Vaga with the
        given id
        
        :param request: The request object
        :param vaga_id: The id of the vacancy to be removed
        :return: A HttpResponseForbidden() is being returned.
        """
        empresa = Empresa.objects.get(id=request.user.id)

        vagas = empresa.vagas.all()

        userHasVagas = False
        auxvaga = None

        for vaga in vagas:
            if vaga.id == vaga_id:
                userHasVagas = True
                auxvaga = vaga
                break

        if userHasVagas == False:
            return HttpResponseForbidden()

        if request.method == "POST":
            Vaga.objects.filter(id=auxvaga.id).delete()
            return HttpResponse(status=204, headers={'HX-Trigger': 'vagaListChanged'})

        return render(request, 'generic_form.html', {
            'title': "Deseja remover esta vaga?",
            'label': "Vaga: " + auxvaga.titulo 
        })