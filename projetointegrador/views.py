from django.shortcuts import render
from django.contrib import messages
from django.core.validators import validate_email

def index(request):
    return render(request, 'home/index.html')

def register(request):
    if request.method != 'POST':
        return render(request, 'register/index.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not email or not senha or not senha2:
        messages.error(request, 'Nenhum campo pode estar vazio.')

    try: 
        validate_email(email)
    except:
        messages.error(request, 'Email inválido')
        return render(request, 'register/index.html')

    return render(request, 'register/index.html')