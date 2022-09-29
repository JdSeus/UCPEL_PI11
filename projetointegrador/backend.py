from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password

from .models import Usuario
from .models import Empresa

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


class EmpresaBackend(BaseBackend):

    def authenticate(self, request, cnpj=None, password=None):
        """
        If the password is valid, return the user object, otherwise return None
        
        :param request: The request object
        :param cnpj: The username of the user trying to authenticate
        :param password: The password to check
        :return: The user object
        """
        try:
            empresa = Empresa.objects.get(cnpj=cnpj)
        except Empresa.DoesNotExist:
            return None
        pwd_valid = check_password(password, empresa.password)
        if(pwd_valid):
            return empresa
        return None

    def get_user(self, empresa_id):
        """
        If the user exists, return the user. If the user doesn't exist, return None
        
        :param empresa_id: The primary key of the user you want to get
        :return: The user object if it exists, or None if it doesn't.
        """
        try: 
            return Empresa.objects.get(pk=empresa_id)
        except Empresa.DoesNotExist:
            return None

