from django.contrib import admin
from .models import Curriculo, Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'sobrenome', 'email', 'senha')
    list_display_links = ('id', 'nome', 'sobrenome')

class CurriculoAdmin(admin.ModelAdmin):
    list_display = ('id','rua', 'bairro', 'cidade', 'estado', 'telefone')

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Curriculo, CurriculoAdmin)
