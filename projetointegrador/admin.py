from django.contrib import admin
from .models import Endereco
from .models import Telefone
from .models import Link
from .models import Escolaridade
from .models import Historico
from .models import Curso
from .models import Curriculo
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'sobrenome', 'email', 'senha')
    list_display_links = ('id', 'nome', 'sobrenome')

class CurriculoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Endereco)
admin.site.register(Telefone)
admin.site.register(Link)
admin.site.register(Escolaridade)
admin.site.register(Historico)
admin.site.register(Curso)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Curriculo, CurriculoAdmin)
