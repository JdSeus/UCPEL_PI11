from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden

from ..forms import CurriculoForm
from ..forms import EnderecoForm
from ..forms import TelefoneForm
from ..forms import LinkForm

from ..models import Usuario
from ..models import Curriculo
from ..models import Endereco
from ..models import Telefone
from ..models import Link

from ..helpers import dd

from pprint import pprint

class CurriculoController():

    # dump_data = dd(request, usuario)
    # return HttpResponse(dump_data)

    # pprint(dir(usuario))

    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
    def index(request):

        usuario = Usuario.objects.prefetch_related('curriculo', 'curriculo__telefones', 'curriculo__links').get(id=request.user.id)

        if request.method == 'POST':
            form = CurriculoForm(request.POST)
            if form.is_valid():
                return HttpResponseRedirect('/thanks/')
        else:
            if usuario.curriculo is None:
                form = CurriculoForm()
            else:
                form = CurriculoForm(instance=usuario.curriculo)

        return render(request, 'curriculo/index.html', {'form': form, 'usuario': usuario})

    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
    def ajax_editar_endereco(request):

        usuario = Usuario.objects.select_related('curriculo').get(id=request.user.id)

        if request.method == "POST":
            form = EnderecoForm(request.POST)
            if form.is_valid():

                if usuario.curriculo is None:
                    curriculo = Curriculo()
                    curriculo.save()
                    usuario.curriculo = curriculo
                    usuario.save()
                
                if usuario.curriculo.endereco is None:
                    endereco = Endereco.objects.create(**form.cleaned_data)
                    usuario.curriculo.endereco = endereco
                    usuario.curriculo.save()
                else:
                    endereco = Endereco.objects.filter(id=usuario.curriculo.endereco.id).update(**form.cleaned_data)

                return HttpResponse(status=204, headers={'HX-Trigger': 'enderecoListChanged'})
        else:
            if usuario.curriculo is None:
                form = EnderecoForm()
            else:
                if usuario.curriculo.endereco is None:
                    form = EnderecoForm()
                else:
                    form = EnderecoForm(instance=usuario.curriculo.endereco)
        return render(request, 'curriculo/generic_form.html', {
            'form': form,
            'title': "Adicionar Endereço"
        })

    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
    def ajax_adicionar_telefone(request):

        usuario = Usuario.objects.select_related('curriculo').get(id=request.user.id)

        if request.method == "POST":
            form = TelefoneForm(request.POST)
            if form.is_valid():

                if usuario.curriculo is None:
                    curriculo = Curriculo()
                    curriculo.save()
                    usuario.curriculo = curriculo
                    usuario.save()
                
                telefone = Telefone.objects.create(**form.cleaned_data)
                usuario.curriculo.telefones.add(telefone)
                usuario.curriculo.save()

                return HttpResponse(status=204, headers={'HX-Trigger': 'telefoneListChanged'})
        else:
            form = TelefoneForm()
        return render(request, 'curriculo/generic_form.html', {
            'form': form,
            'title': "Adicionar Telefone"
        })

    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
    def ajax_remover_telefone(request, telefone_id):

        usuario = Usuario.objects.select_related('curriculo').get(id=request.user.id)

        telefones = usuario.curriculo.telefones.all()

        userHasTelefone = False
        auxtelefone = None

        for telefone in telefones:
            if telefone.id == telefone_id:
                userHasTelefone = True
                auxtelefone = telefone
                break

        if userHasTelefone == False:
            return HttpResponseForbidden()

        if request.method == "POST":
            Telefone.objects.filter(id=auxtelefone.id).delete()
            return HttpResponse(status=204, headers={'HX-Trigger': 'telefoneListChanged'})

        return render(request, 'curriculo/generic_form.html', {
            'title': "Deseja remover este telefone?",
            'label': "Telefone: " + auxtelefone.telefone 
        })

    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
    def ajax_editar_telefone(request, telefone_id):

        usuario = Usuario.objects.select_related('curriculo').get(id=request.user.id)

        telefones = usuario.curriculo.telefones.all()

        userHasTelefone = False
        auxtelefone = None

        for telefone in telefones:
            if telefone.id == telefone_id:
                userHasTelefone = True
                auxtelefone = telefone
                break

        if userHasTelefone == False:
            return HttpResponseForbidden()

        if request.method == "POST":
            form = TelefoneForm(request.POST)
            if form.is_valid():

                telefone = Telefone.objects.filter(id=auxtelefone.id).update(**form.cleaned_data)

                return HttpResponse(status=204, headers={'HX-Trigger': 'telefoneListChanged'})
        else:
            form = TelefoneForm(instance=auxtelefone)

        return render(request, 'curriculo/generic_form.html', {
            'title': "Editar Telefone: ",
            'form': form
        })

    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
    def ajax_adicionar_link(request):

        usuario = Usuario.objects.select_related('curriculo').get(id=request.user.id)

        if request.method == "POST":
            form = LinkForm(request.POST)
            if form.is_valid():

                if usuario.curriculo is None:
                    curriculo = Curriculo()
                    curriculo.save()
                    usuario.curriculo = curriculo
                    usuario.save()
                
                link = Link.objects.create(**form.cleaned_data)
                usuario.curriculo.links.add(link)
                usuario.curriculo.save()

                return HttpResponse(status=204, headers={'HX-Trigger': 'linkListChanged'})
        else:
            form = LinkForm()
        return render(request, 'curriculo/generic_form.html', {
            'form': form,
            'title': "Adicionar Link"
        })

    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
    def ajax_remover_link(request, link_id):

        usuario = Usuario.objects.select_related('curriculo').get(id=request.user.id)

        links = usuario.curriculo.links.all()

        userHasLink = False
        auxlink = None

        for link in links:
            if link.id == link_id:
                userHasLink = True
                auxlink = link
                break

        if userHasLink == False:
            return HttpResponseForbidden()

        if request.method == "POST":
            Link.objects.filter(id=auxlink.id).delete()
            return HttpResponse(status=204, headers={'HX-Trigger': 'linkListChanged'})

        return render(request, 'curriculo/generic_form.html', {
            'title': "Deseja remover este link?",
            'label': "Link: " + auxlink.titulo 
        })