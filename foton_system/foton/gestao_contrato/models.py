from django.db import models

class Contrato(models.Model):
    titulo = models.CharField(max_length=100)
    data = models.DateField()
    numero = models.IntegerField()
    cliente = models.CharField(max_length=100)

    # outros campos do contrato

    def __str__(self):
        return self.titulo
