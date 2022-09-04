from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import Usuario

class UsuarioBackend(BaseBackend):

    def authenticate(self, request, email=None, password=None):
        try:
            usuario = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            return None
        pwd_valid = check_password(password, usuario.password)
        if(pwd_valid):
            return usuario
        return None

    def get_user(self, usuario_id):
        try: 
            return Usuario.objects.get(pk=usuario_id)
        except Usuario.DoesNotExist:
            return None

