from django.db import models
from django.utils import timezone

class Endereco(models.Model):
    rua = models.CharField(max_length=255, blank=True)
    bairro = models.CharField(max_length=255, blank=True)
    cidade = models.CharField(max_length=255, blank=True)
    estado = models.CharField(max_length=255, blank=True)

class Telefone(models.Model):
    telefone = models.CharField(max_length=255, blank=True)

class Link(models.Model):
    titulo = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

class Escolaridade(models.Model):
    instituicao = models.CharField(max_length=255)
    curso = models.CharField(max_length=255)
    observacao = models.CharField(max_length=1024)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    
class Historico(models.Model):
    empresa = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=1024)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()

class Curso(models.Model):
    instituicao = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=1024)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    
class Curriculo(models.Model):
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, blank=True, null=True)
    telefones = models.ManyToManyField(Telefone)
    links = models.ManyToManyField(Link)
    escolaridade = models.ForeignKey(Escolaridade, on_delete=models.CASCADE, blank=True, null=True)


class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(default=timezone.now)
    curriculo = models.ForeignKey(Curriculo, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nome

