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
from ..forms import EscolaridadeForm
from ..forms import HistoricoForm
from ..forms import CursoForm

from ..models import Usuario
from ..models import Curriculo
from ..models import Endereco
from ..models import Telefone
from ..models import Link
from ..models import Escolaridade
from ..models import Historico
from ..models import Curso

from ..helpers import dd

from pprint import pprint

class CurriculoController():

    # dump_data = dd(request, usuario)
    # return HttpResponse(dump_data)

    # pprint(dir(usuario))

    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
    
    def index(request):
        """
        I'm trying to get the user's curriculum, which is related to the user's phone number and link
        
        :param request: The current request object
        :param curriculo_id: The id of the Curriculo object that I want to get
        :return: a render of the template 'curriculo/simple-curriculo.html' with the context 'usuario'
        """

        usuario = Usuario.objects.prefetch_related('curriculo', 'curriculo__telefones', 'curriculo__links').get(id=request.user.id)

        return render(request, 'curriculo/index.html', {'usuario': usuario})


    def ajax_ver_curriculo(request, curriculo_id):

        curriculo = get_object_or_404(Curriculo, id=curriculo_id)
        usuario = get_object_or_404(Usuario, curriculo_id=curriculo.id)

        return render(request, 'curriculo/simple-curriculo.html', {'usuario': usuario})

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
        return render(request, 'generic_form.html', {
            'form': form,
            'title': "Adicionar Endereço"
        })

    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
        
    def ajax_adicionar_telefone(request):
        """
        It creates a new Telefone object and adds it to the Curriculo object of the logged in user
        
        :param request: The request object
        :return: A form to add a phone number.
        """
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
        return render(request, 'generic_form.html', {
            'form': form,
            'title': "Adicionar Telefone"
        })

    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
    def ajax_editar_telefone(request, telefone_id):
        """
        If the user is logged in, and the user is a Usuario, and the user is trying to edit a Telefone
        that belongs to him, then edit the Telefone
        
        :param request: The current request object
        :param telefone_id: The id of the telefone to be edited
        :return: A HttpResponse object with a status code of 204.
        """

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

        return render(request, 'generic_form.html', {
            'title': "Editar Telefone: ",
            'form': form
        })

    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
    def ajax_remover_telefone(request, telefone_id):
        """
        If the user is logged in and is a Usuario, then it will check if the user has the telefone_id,
        if it does, then it will delete it
        
        :param request: The request object
        :param telefone_id: the id of the phone to be removed
        :return: A list of all the telefones of the user.
        """

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

        return render(request, 'generic_form.html', {
            'title': "Deseja remover este telefone?",
            'label': "Telefone: " + auxtelefone.telefone 
        })

    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
       
    def ajax_adicionar_link(request):
        """
        If the user is logged in, and the request is a POST, and the form is valid, then create a new
        link and add it to the user's curriculum
        
        :param request: The request object
        :return: A function that returns a function that returns a function that returns a function that
        returns a function that returns a function that returns a function that returns a function that
        returns a function that returns a function that returns a function that returns a function that
        returns a function that returns a function that returns a function that returns a function that
        returns a function that returns a function that returns a function that returns a function that
        returns
        """

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
        return render(request, 'generic_form.html', {
            'form': form,
            'title': "Adicionar Link"
        })

    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
    def ajax_editar_link(request, link_id):
        """
        If the user is logged in, and the user is a Usuario, and the user is requesting a POST, and the
        form is valid, then update the link
        
        :param request: The request object
        :param link_id: The id of the link to be edited
        :return: A HttpResponse object with status code 204.
        """

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
            form = LinkForm(request.POST)
            if form.is_valid():

                link = Link.objects.filter(id=auxlink.id).update(**form.cleaned_data)

                return HttpResponse(status=204, headers={'HX-Trigger': 'linkListChanged'})
        else:
            form = LinkForm(instance=auxlink)

        return render(request, 'generic_form.html', {
            'title': "Editar Link: ",
            'form': form
        })

    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
    
    def ajax_remover_link(request, link_id):
        """
        If the user is logged in and has the link, delete the link and return a 204 status code
        
        :param request: The request object
        :param link_id: the id of the link to be removed
        :return: A HttpResponseForbidden() is being returned.
        """

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

        return render(request, 'generic_form.html', {
            'title': "Deseja remover este link?",
            'label': "Link: " + auxlink.titulo 
        })

    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
        
    def ajax_adicionar_escolaridade(request):
        """
        It creates a new Escolaridade object, adds it to the user's Curriculo object, and then returns a
        204 status code with a custom header
        
        :param request: The request object
        :return: A form to add a new education.
        """

        usuario = Usuario.objects.select_related('curriculo').get(id=request.user.id)

        if request.method == "POST":
            form = EscolaridadeForm(request.POST)
            if form.is_valid():

                if usuario.curriculo is None:
                    curriculo = Curriculo()
                    curriculo.save()
                    usuario.curriculo = curriculo
                    usuario.save()
                
                escolaridade = Escolaridade.objects.create(**form.cleaned_data)

                usuario.curriculo.escolaridades.add(escolaridade)
                usuario.curriculo.save()

                return HttpResponse(status=204, headers={'HX-Trigger': 'escolaridadeListChanged'})
        else:
            form = EscolaridadeForm()
        return render(request, 'generic_form.html', {
            'form': form,
            'title': "Adicionar Escolaridade"
        })

    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
        
    def ajax_editar_escolaridade(request, escolaridade_id):
        """
        If the user is logged in, and the user is a Usuario, and the user has the escolaridade_id, and
        the form is valid, then update the escolaridade
        
        :param request: The current request object
        :param escolaridade_id: The id of the escolaridade to be edited
        :return: A list of all the escolaridades of the user.
        """

        usuario = Usuario.objects.select_related('curriculo').get(id=request.user.id)

        escolaridades = usuario.curriculo.escolaridades.all()

        userHasEscolaridade = False
        auxescolaridade = None

        for escolaridade in escolaridades:
            if escolaridade.id == escolaridade_id:
                userHasEscolaridade = True
                auxescolaridade = escolaridade
                break

        if userHasEscolaridade == False:
            return HttpResponseForbidden()

        if request.method == "POST":
            form = EscolaridadeForm(request.POST)
            if form.is_valid():

                escolaridade = Escolaridade.objects.filter(id=auxescolaridade.id).update(**form.cleaned_data)

                return HttpResponse(status=204, headers={'HX-Trigger': 'escolaridadeListChanged'})
        else:
            form = EscolaridadeForm(instance=auxescolaridade)

        return render(request, 'generic_form.html', {
            'title': "Editar Escolaridade: ",
            'form': form
        })

    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
        
    def ajax_remover_escolaridade(request, escolaridade_id):
        """
        If the user is logged in and has the escolaridade_id in his/her escolaridades, then delete it
        
        :param request: The current request object
        :param escolaridade_id: The id of the escolaridade to be removed
        :return: a render of the generic_form.html template.
        """

        usuario = Usuario.objects.select_related('curriculo').get(id=request.user.id)

        escolaridades = usuario.curriculo.escolaridades.all()

        userHasEscolaridade = False
        auxescolaridade = None

        for escolaridade in escolaridades:
            if escolaridade.id == escolaridade_id:
                userHasEscolaridade = True
                auxescolaridade = escolaridade
                break

        if userHasEscolaridade == False:
            return HttpResponseForbidden()

        if request.method == "POST":
            Escolaridade.objects.filter(id=auxescolaridade.id).delete()
            return HttpResponse(status=204, headers={'HX-Trigger': 'escolaridadeListChanged'})

        return render(request, 'generic_form.html', {
            'title': "Deseja remover esta escolaridade?",
            'label': "Curso: " + auxescolaridade.curso 
        })

    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
        
    def ajax_adicionar_historico(request):
        """
        If the request is a POST, then create a new Historico object with the data from the form, add it
        to the Curriculo object, and return a 204 status code
        
        :param request: The request object
        :return: A function that returns a function that returns a function that returns a function that
        returns a function that returns a function that returns a function that returns a function that
        returns a function that returns a function that returns a function that returns a function that
        returns a function that returns a function that returns a function that returns a function that
        returns a function that returns a function that returns a function that returns a function that
        returns
        """
        usuario = Usuario.objects.select_related('curriculo').get(id=request.user.id)

        if request.method == "POST":
            form = HistoricoForm(request.POST)
            if form.is_valid():

                if usuario.curriculo is None:
                    curriculo = Curriculo()
                    curriculo.save()
                    usuario.curriculo = curriculo
                    usuario.save()
                
                historico = Historico.objects.create(**form.cleaned_data)

                usuario.curriculo.empresas.add(historico)
                usuario.curriculo.save()

                return HttpResponse(status=204, headers={'HX-Trigger': 'historicoListChanged'})
        else:
            form = HistoricoForm()
        return render(request, 'generic_form.html', {
            'form': form,
            'title': "Adicionar Histórico Profissional"
        })

    
    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
        
    def ajax_editar_historico(request, historico_id):
        """
        If the user is logged in, and the user is a Usuario, and the user has a Historico with the given
        id, and the request is a POST, and the form is valid, then update the Historico with the given
        id with the data from the form, and return a 204 status code with a header that triggers a
        javascript function
        
        :param request: The request object
        :param historico_id: The id of the historico to be edited
        :return: A HttpResponse object with status code 204.
        """

        usuario = Usuario.objects.select_related('curriculo').get(id=request.user.id)

        empresas = usuario.curriculo.empresas.all()

        userHasHistorico = False
        auxhistorico = None

        for historico in empresas:
            if historico.id == historico_id:
                userHasHistorico = True
                auxhistorico = historico
                break

        if userHasHistorico == False:
            return HttpResponseForbidden()

        if request.method == "POST":
            form = HistoricoForm(request.POST)
            if form.is_valid():

                historico = Historico.objects.filter(id=auxhistorico.id).update(**form.cleaned_data)

                return HttpResponse(status=204, headers={'HX-Trigger': 'historicoListChanged'})
        else:
            form = HistoricoForm(instance=auxhistorico)

        return render(request, 'generic_form.html', {
            'title': "Editar Histórico Profissional: ",
            'form': form
        })

    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
        
    def ajax_remover_historico(request, historico_id):
        """
        If the user is logged in and is a Usuario, then it will check if the user has the historico_id
        in his/her list of empresas. If it does, then it will delete it
        
        :param request: The request object
        :param historico_id: The id of the historico to be removed
        :return: A list of all the objects in the database.
        """

        usuario = Usuario.objects.select_related('curriculo').get(id=request.user.id)

        empresas = usuario.curriculo.empresas.all()

        userHasHistorico = False
        auxhistorico = None

        for historico in empresas:
            if historico.id == historico_id:
                userHasHistorico = True
                auxhistorico = historico
                break

        if userHasHistorico == False:
            return HttpResponseForbidden()

        if request.method == "POST":
            Historico.objects.filter(id=auxhistorico.id).delete()
            return HttpResponse(status=204, headers={'HX-Trigger': 'historicoListChanged'})

        return render(request, 'generic_form.html', {
            'title': "Deseja remover este Histórico Profissional?",
            'label': "Cargo: " + auxhistorico.cargo 
        })

    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
        
    def ajax_adicionar_curso(request):
        """
        It creates a new Curso object and adds it to the Curriculo object of the logged in user
        
        :param request: The request object
        :return: A HttpResponse object with a status code of 204 and a header of 'HX-Trigger':
        'cursoListChanged'
        """

        usuario = Usuario.objects.select_related('curriculo').get(id=request.user.id)

        if request.method == "POST":
            form = CursoForm(request.POST)
            if form.is_valid():

                if usuario.curriculo is None:
                    curriculo = Curriculo()
                    curriculo.save()
                    usuario.curriculo = curriculo
                    usuario.save()
                
                curso = Curso.objects.create(**form.cleaned_data)

                usuario.curriculo.cursos.add(curso)
                usuario.curriculo.save()

                return HttpResponse(status=204, headers={'HX-Trigger': 'cursoListChanged'})
        else:
            form = CursoForm()
        return render(request, 'generic_form.html', {
            'form': form,
            'title': "Adicionar Curso"
        })

    
    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
        
    def ajax_editar_curso(request, curso_id):
        """
        If the user is logged in, and the user has the course, and the method is POST, and the form is
        valid, then update the course
        
        :param request: The request object
        :param curso_id: The id of the course to be edited
        :return: A HttpResponse object with status code 204.
        """

        usuario = Usuario.objects.select_related('curriculo').get(id=request.user.id)

        cursos = usuario.curriculo.cursos.all()

        userHasCurso = False
        auxcurso = None

        for curso in cursos:
            if curso.id == curso_id:
                userHasCurso = True
                auxcurso = curso
                break

        if userHasCurso == False:
            return HttpResponseForbidden()

        if request.method == "POST":
            form = CursoForm(request.POST)
            if form.is_valid():

                curso = Curso.objects.filter(id=auxcurso.id).update(**form.cleaned_data)

                return HttpResponse(status=204, headers={'HX-Trigger': 'cursoListChanged'})
        else:
            form = CursoForm(instance=auxcurso)

        return render(request, 'generic_form.html', {
            'title': "Editar Curso: ",
            'form': form
        })

    @user_passes_test(Usuario.user_is_Usuario, login_url="login-usuario")
        
    def ajax_remover_curso(request, curso_id):
        """
        If the user is logged in and has the permission to access the page, then the function will check
        if the user has the course in his curriculum, if he does, then it will delete the course from
        the database and return a 204 status code, if he doesn't, then it will return a 403 status code
        
        :param request: The request object
        :param curso_id: The id of the course to be removed
        :return: A HttpResponseForbidden object.
        """

        usuario = Usuario.objects.select_related('curriculo').get(id=request.user.id)

        cursos = usuario.curriculo.cursos.all()

        userHasCurso = False
        auxcurso = None

        for curso in cursos:
            if curso.id == curso_id:
                userHasCurso = True
                auxcurso = curso
                break

        if userHasCurso == False:
            return HttpResponseForbidden()

        if request.method == "POST":
            Curso.objects.filter(id=auxcurso.id).delete()
            return HttpResponse(status=204, headers={'HX-Trigger': 'cursoListChanged'})

        return render(request, 'generic_form.html', {
            'title': "Deseja remover este curso?",
            'label': "Curso: " + auxcurso.titulo 
        })