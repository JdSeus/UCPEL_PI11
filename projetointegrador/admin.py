from django.contrib import admin
from .models import Endereco
from .models import Telefone
from .models import Link
from .models import Escolaridade
from .models import Historico
from .models import Curso
from .models import Curriculo
from .models import Usuario
from .models import Empresa

class UsuarioAdmin(admin.ModelAdmin):
    pass

class EmpresaAdmin(admin.ModelAdmin):
    pass

class CurriculoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Endereco)
admin.site.register(Telefone)
admin.site.register(Link)
admin.site.register(Escolaridade)
admin.site.register(Historico)
admin.site.register(Curso)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Curriculo, CurriculoAdmin)
