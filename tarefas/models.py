from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class CustomUser(AbstractUser):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)


class tarefa(models.Model):
    id_tarefa = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True)