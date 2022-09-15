from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

from ..models import Empresa
from ..models import Vaga

from ..forms import VagaForm

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