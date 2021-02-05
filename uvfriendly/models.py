from django.db import models
from django.urls import reverse

# Create your models here.

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    objetos = models.Manager()



class Componentes(models.Model):
    nome = models.CharField(
        max_length=50, null=False, blank=False)
    descricao = models.CharField(
        max_length=150, null=False, blank=False)
    fullsize = models.CharField(
        max_length=255, null=False, blank=False)
    thumbnails = models.CharField(
        max_length=255, null=False, blank=False)
    status = models.IntegerField(
        null=False, blank=False, default=0)

    objetos = models.Manager()


class Projetos(models.Model):
    nome = models.CharField(
        max_length=20, null=False, blank=False)
    descricao = models.CharField(
        max_length=255, null=False, blank=False)
    classe = models.CharField(
        max_length=255, null=False, blank=False, default='')
    status = models.IntegerField(
        null=False, blank=False, default=0)

    objetos = models.Manager()


class Tecnologias(models.Model):
    classe = models.CharField(
        max_length=150, null=False, blank=False)
    alt = models.CharField(
        max_length=50, null=False, blank=False)
    nome = models.CharField(
        max_length=50, null=False, blank=False)
    status = models.IntegerField(
        null=False, blank=False, default=0)

    objetos = models.Manager()


class Usuarios(models.Model):
    cpf = models.CharField(
        max_length=14, null=False, blank=False)
    nome = models.CharField(
        max_length=255, null=False, blank=False)
    sobrenome = models.CharField(
        max_length=255, null=False, blank=False)
    email = models.EmailField(
        max_length=255, null=False, blank=False)
    senha1 = models.CharField(
        max_length=255, null=False, blank=False)
    senha2 = models.CharField(
        max_length=255, null=False, blank=False)
    status = models.IntegerField(
        default=0, null=False, blank=False)
    level = models.IntegerField(
        default=0, null=False, blank=False)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('form_users', kwargs={'pk':self.pk})

    objetos = models.Manager()


class Canais(models.Model):
    nome = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    nomecanal = models.CharField(
        max_length=50, null=False, blank=False)
    descricao = models.CharField(
        max_length=150, null=False, blank=False)
    campo_01 = models.CharField(
        max_length=50, null=True, blank=True)
    campo_02 = models.CharField(
        max_length=50, null=True, blank=True)
    campo_03 = models.CharField(
        max_length=50, null=True, blank=True)
    campo_04 = models.CharField(
        max_length=50, null=True, blank=True)
    campo_05 = models.CharField(
        max_length=50, null=True, blank=True)
    campo_06 = models.CharField(
        max_length=50, null=True, blank=True)
    campo_07 = models.CharField(
        max_length=50, null=True, blank=True)
    campo_08 = models.CharField(
        max_length=50, null=True, blank=True)
    metadata = models.CharField(
        max_length=255, null=False, blank=False)
    tags = models.CharField(
        max_length=255, null=False, blank=False)
    latitude = models.IntegerField(
        null=True, blank=True, default=0)
    longitude = models.IntegerField(
        null=True, blank=True, default=0)
    elevation = models.IntegerField(
        null=True, blank=True, default=0)
    status = models.IntegerField(
        null=True, blank=True, default=0)

    objetos = models.Manager()

