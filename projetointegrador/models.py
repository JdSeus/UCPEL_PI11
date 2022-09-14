from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser


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
    observacao = models.CharField(max_length=1023)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    
class Historico(models.Model):
    empresa = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=1023)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()

class Curso(models.Model):
    instituicao = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=1023)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    
class Curriculo(models.Model):
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, blank=True, null=True)
    telefones = models.ManyToManyField(Telefone, blank=True)
    links = models.ManyToManyField(Link, blank=True)
    escolaridades = models.ManyToManyField(Escolaridade, blank=True)
    empresas = models.ManyToManyField(Historico, blank=True)
    cursos = models.ManyToManyField(Curso, blank=True)
class Usuario(AbstractBaseUser):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    curriculo = models.ForeignKey(Curriculo, on_delete=models.CASCADE, blank=True, null=True)

    USERNAME_FIELD = 'email'

    @staticmethod
    def user_is_Usuario(user):
        return user.is_authenticated and isinstance(user, Usuario)

    @property
    def is_staff(self):
        return False

    def has_perm(self, perm, obj=None):
        return False

    def has_module_perms(self, app_label):
        return False

    def __str__(self):
        return self.nome

class CategoriaVaga(models.Model):
    titulo = models.CharField(max_length=255)

class Vaga(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=1023)
    concluida = models.BooleanField()
    publicar = models.BooleanField()
    categoria = models.ManyToManyField(CategoriaVaga, blank=True)
class Empresa(AbstractBaseUser):
    cnpj = models.CharField(max_length=255, unique=True)
    nome_social = models.CharField(max_length=255)

    vagas = models.ManyToManyField(Vaga, blank=True)

    USERNAME_FIELD = 'cnpj'

    @staticmethod
    def user_is_Empresa(user):
        return user.is_authenticated and isinstance(user, Empresa)

    @property
    def is_staff(self):
        return False

    def has_perm(self, perm, obj=None):
        return False

    def has_module_perms(self, app_label):
        return False

    def __str__(self):
        return self.nome_social

class Aplicacao(models.Model):
    ACCEPTED = 'AC'
    ANALYZING = 'AN'
    REJECTED = 'RJ'

    STATUSES = [
        (ACCEPTED, 'Aprovado'),
        (ANALYZING, 'Analisando'),
        (REJECTED, 'Rejeitado'),
    ]

    curriculos = models.ManyToManyField(Curriculo, blank=True)
    vagas = models.ManyToManyField(Vaga, blank=True)
    status = models.CharField(
        max_length=2,
        choices=STATUSES,
        default=ANALYZING,
    )
    resposta = models.CharField(max_length=1023)
