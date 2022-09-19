from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden

from ..helpers import dd

from pprint import pprint

from ..models import Vaga

class VagasController():

    def index(request):
        vagas = Vaga.objects.filter(publicar=True)

        dump_data = dd(request, vagas)
        return HttpResponse(dump_data)

        return render(request, 'vagas/index.html', {
            'vagas': vagas
        })