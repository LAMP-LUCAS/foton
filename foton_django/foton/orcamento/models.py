from django.db import models

class Orcamento(models.Model):
    projeto = models.ForeignKey('projetos.Projeto', on_delete=models.CASCADE)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Orçamento #{self.id}"
