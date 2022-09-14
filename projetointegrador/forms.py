from django import forms
from django.forms import ModelForm

from projeto import settings

from .models import Curriculo
from .models import Endereco
from .models import Telefone
from .models import Link
from .models import Escolaridade
from .models import Curso

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

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        exclude = []
        widgets = {
            'inicio': DateInput(),
            'fim': DateInput(),
        }