from django.db import models

class Contrato(models.Model):
    titulo = models.CharField(max_length=100)
    data = models.DateField()
    numero = models.CharField(
        max_length=100,
        default=0,
        )

    def get_cliente(self):
        from gestao_cliente.models import Cliente
        return Cliente.objects.get(id=self.cliente_id)

    def get_orcamento(self):
        from gestao_orcamento.models import Orcamento
        return Orcamento.objects.get(id=self.orcamento_id)

    cliente = models.ForeignKey(
        'gestao_cliente.Cliente',
        on_delete=models.CASCADE,
        related_name='contratos',
        default=1
        )
    
    orcamento = models.OneToOneField(
        'gestao_orcamento.Orcamento',
        on_delete=models.CASCADE,
        related_name='contratado',
        default=1,
        )

    def __str__(self):
        return self.titulo
