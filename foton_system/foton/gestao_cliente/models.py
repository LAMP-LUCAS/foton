from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    contrato = models.ForeignKey('gestao_contrato.Contrato', on_delete=models.SET_NULL, null=True, blank=True)

    # outros campos do cliente

    def __str__(self):
        return self.nome
