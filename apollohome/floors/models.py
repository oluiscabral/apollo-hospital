from django.db import models

# Create your models here.
class Andar(models.Model):
    numero_opc = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    )
    numero_andar = models.IntegerField(choices=numero_opc)
    leitos_totais = models.IntegerField()
    leitos_ocupados = models.IntegerField()