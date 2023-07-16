from django.db import models

class contratos(models.Model):
    numero = models.CharField(max_length=20)
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return self.numero
