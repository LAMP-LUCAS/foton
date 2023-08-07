from django.db import models
from django.utils import timezone
import datetime


def get_default_termino():
    return timezone.now() + datetime.timedelta(days=30)

class ComposicaoCusto(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    descricao = models.TextField()
    custo = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.codigo} - {self.descricao}"

class Orcamento(models.Model):
    descricao = models.TextField(null=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    contrato = models.OneToOneField(
        'GestaoContrato.Contrato',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='orcamentoContrato'
    )
    composicoes_custo = models.ManyToManyField(ComposicaoCusto)
    
    inicio = models.DateField(null=False, default=timezone.now)
    termino = models.DateField(null=False, default=get_default_termino)

    clausulas = models.TextField(null=False, default='CLAUSULA')
    servicos = models.TextField(null=False, default='SERVICO')

    def __str__(self):
        return self.descricao
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    unidade_de_medida = models.CharField(max_length=50)
    base_dados = models.CharField(max_length=50, choices=[('SINAPI', 'SINAPI'), ('TCPO', 'TCPO'), ('GOINFRA', 'GOINFRA'), ('DNIT', 'DNIT'), ('FOTON', 'FOTON')])
    eficiencia = models.DecimalField(max_digits=5, decimal_places=2)
    codigo_bim = models.CharField(max_length=50)

    def __str__(self):
        return self.nome