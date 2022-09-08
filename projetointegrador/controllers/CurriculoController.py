from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

from ..forms import CurriculoForm

from ..forms import NameForm
class CurriculoController():

    def index(request):
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = CurriculoForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = CurriculoForm()

        return render(request, 'curriculo/index.html', {'form': form})

    def ajax_adicionar_endereco(request):
        if request.method == "POST":
            form = NameForm(request.POST)
            if form.is_valid():
                return HttpResponse(status=204, headers={'HX-Trigger': 'enderecoListChanged'})
        else:
            form = NameForm()
        return render(request, 'curriculo/endereco_form.html', {
            'form': form,
        })