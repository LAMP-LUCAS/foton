from django.db import models
from django.utils import timezone
import datetime


def get_default_termino():
    return timezone.now() + datetime.timedelta(days=30)

class Orcamento(models.Model):
    descricao = models.TextField(null=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    contrato = models.OneToOneField(
        'GestaoContrato.Contrato',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='orcamentoContrato'
    )
    
    inicio = models.DateField(null=False, default=timezone.now)
    termino = models.DateField(null=False, default=get_default_termino)

    clausulas = models.TextField(null=False, default='CLAUSULA')
    servicos = models.TextField(null=False, default='SERVICO')

    def __str__(self):
        return self.descricao
    
 #class Proposta(models.model)
    