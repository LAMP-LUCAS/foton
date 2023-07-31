from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def get_contrato(self):
        from GestaoContrato.models import Contrato
        return Contrato.objects.get(id=self.contrato_id)

    contrato = models.ForeignKey(
                'GestaoContrato.Contrato',
                on_delete=models.SET_NULL,
                null=True,
                blank=True,
                related_name='clienteContrato')
    # outros campos do cliente

    def __str__(self):
        return self.nome
