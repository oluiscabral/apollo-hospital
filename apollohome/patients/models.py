from django.db import models
from professionals.models import Profissional


class Paciente(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    idade = models.IntegerField(null=True)
    estado_atendimento = models.BooleanField(default=False)
    cpf = models.CharField(max_length=14, unique=True)
    atend_desc = models.CharField(max_length=500)
    profResponsavel = models.OneToOneField(Profissional, on_delete=models.CASCADE)
