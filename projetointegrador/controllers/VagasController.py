from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from django.core.validators import validate_email


from ..models import Usuario

class VagasController():

    def index(request):
        return render(request, 'vagas/index.html')