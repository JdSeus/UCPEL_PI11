from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404

from ..forms import CurriculoForm
from ..forms import EnderecoForm

from ..models import Usuario
from ..models import Curriculo

from ..helpers import dd

from pprint import pprint

class CurriculoController():

    # dump_data = dd(request, usuario)
    # return HttpResponse(dump_data)

    # pprint(dir(usuario))


    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
    def index(request):

        usuario = Usuario.objects.get(id=request.user.id)

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
    def ajax_adicionar_endereco(request):

        usuario = Usuario.objects.select_related('curriculo').get(id=request.user.id)

        if request.method == "POST":
            form = EnderecoForm(request.POST)
            if form.is_valid():
                return HttpResponse(status=204, headers={'HX-Trigger': 'enderecoListChanged'})
        else:
            if usuario.curriculo is None:
                form = EnderecoForm()
            else:
                form = EnderecoForm()
        return render(request, 'curriculo/endereco_form.html', {
            'form': form,
        })