from django.db import models
from django.utils import timezone

class Curriculo(models.Model):
    rua = models.CharField(max_length=255, blank=True)
    bairro = models.CharField(max_length=255, blank=True)
    cidade = models.CharField(max_length=255, blank=True)
    estado = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255, blank=True)

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(default=timezone.now)
    curriculo = models.ForeignKey(Curriculo, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.nome

