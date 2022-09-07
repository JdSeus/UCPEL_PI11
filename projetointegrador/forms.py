from django import forms
from django.forms import ModelForm

from .models import Curriculo

class CurriculoForm(ModelForm):
    class Meta:
        model = Curriculo
        fields = ['endereco', 'telefones', 'links', 'escolaridade', 'empresas', 'cursos']
