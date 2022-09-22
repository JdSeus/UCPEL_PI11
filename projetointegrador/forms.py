from importlib.metadata import requires
from django import forms
from django.forms import ModelForm

from projeto import settings

from .models import Curriculo
from .models import Endereco
from .models import Telefone
from .models import Link
from .models import Escolaridade
from .models import Historico
from .models import Curso
from .models import Aplicacao

from .models import Vaga

class DateInput(forms.DateInput):
    input_type = 'date'

class NameForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)

class CurriculoForm(ModelForm):
    class Meta:
        model = Curriculo
        exclude = []

class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        exclude = []

class TelefoneForm(ModelForm):
    class Meta:
        model = Telefone
        exclude = []

class LinkForm(ModelForm):
    class Meta:
        model = Link
        exclude = []

class EscolaridadeForm(ModelForm):
    class Meta:
        model = Escolaridade
        exclude = []
        widgets = {
            'inicio': DateInput(),
            'fim': DateInput(),
        }

class HistoricoForm(ModelForm):
    class Meta:
        model = Historico
        exclude = []
        widgets = {
            'inicio': DateInput(),
            'fim': DateInput(),
        }

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        exclude = []
        widgets = {
            'inicio': DateInput(),
            'fim': DateInput(),
        }

class VagaForm(ModelForm):
    class Meta:
        model = Vaga
        exclude = ['publicar', 'concluida']
        widgets = {
            'categoria': forms.CheckboxSelectMultiple(),
        }

class VagaFormEdit(ModelForm):
    class Meta:
        model = Vaga
        exclude = []
        widgets = {
            'categoria': forms.CheckboxSelectMultiple(),
        }

class AplicacaoForm(ModelForm):
    class Meta:
        model = Aplicacao
        exclude = ['curriculos', 'vagas']