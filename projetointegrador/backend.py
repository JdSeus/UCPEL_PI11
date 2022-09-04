from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from models import Usuario

class UsuarioBackend(BaseBackend):

    def authenticate(self, request, email=None, senha=None):
        try:
            usuario = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            return None
        pwd_valid = check_password(senha, usuario.senha)
        if(pwd_valid):
            return usuario
        return None

    def get_user(self, usuario_id):
        try: 
            return Usuario.objects.get(pk=usuario_id)
        except Usuario.DoesNotExist:
            return None

    
#    def authenticate(self, request, username=None, password=None):
#        login_valid = (settings.ADMIN_LOGIN == username)
#        pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
#        if login_valid and pwd_valid:
#            try:
#                user = Usuario.objects.get(username=username)
#            except User.DoesNotExist:
#                return None
#            return user
#        return None
#
#    def get_user(self, user_id):
#        try:
#            return User.objects.get(pk=user_id)
#        except User.DoesNotExist:
#            return None