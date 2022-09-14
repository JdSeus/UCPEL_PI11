from django import forms
from django.forms import ModelForm

from .models import Curriculo
from .models import Endereco
from .models import Telefone
from .models import Link

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