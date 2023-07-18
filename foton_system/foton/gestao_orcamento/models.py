from django.db import models

class Orcamento(models.Model):
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    # outros campos do orçamento

    def __str__(self):
        return self.descricao
