from django.db import models

class Contrato(models.Model):
    titulo = models.CharField(max_length=100)
    data = models.DateField()
    numero = models.CharField(
        max_length=100,
        default=0,
        )

    def get_cliente(self):
        from GestaoCliente.models import Cliente
        return Cliente.objects.get(id=self.cliente_id)

    def get_orcamento(self):
        from GestaoOrcamento.models import Orcamento
        return Orcamento.objects.get(id=self.orcamento_id)

    cliente = models.ForeignKey(
        'GestaoCliente.Cliente',
        on_delete=models.CASCADE,
        related_name='contratoCliente',
        default=1,
        )
    
    orcamento = models.OneToOneField(
        'GestaoOrcamento.Orcamento',
        on_delete=models.CASCADE,
        related_name='orcamentoCliente',
        default=1,
        )

    def __str__(self):
        return self.titulo
