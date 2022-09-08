from django import forms
from django.forms import ModelForm

from .models import Curriculo

class NameForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)

class CurriculoForm(ModelForm):
    class Meta:
        model = Curriculo
        fields = ['endereco', 'telefones', 'links', 'escolaridade', 'empresas', 'cursos']
