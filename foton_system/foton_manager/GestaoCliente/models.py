from django.db import models
from django.contrib.auth.models import Group
from fotonUser.models import Organizacao

class Cliente(models.Model):
  
    organizacao = models.ForeignKey(Organizacao, on_delete=models.CASCADE, null=True)

    TIPO_PESSOA_CHOICES = [
        ('PF', 'Pessoa Física / MEI'),
        ('PJ_PRIVADO', 'Pessoa Jurídica de direito privado'),
        ('PJ_INTERNO', 'Pessoa Jurídica de direito público interno'),
        ('PJ_EXTERNO', 'Pessoa Jurídica de direito público externo'),
    ]

    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outra'),
    ]

    NATUREZA_CHOICES = [
        ('ASSOCIACAO', 'Associação'),
        ('SOCIEDADE', 'Sociedade'),
        ('FUNDACAO', 'Fundação'),
        ('RELIGIOSA', 'Organização Religiosa'),
        ('PARTIDO_POLITICO', 'Partido Político'),
        ('EIRELI', 'Empresa Individual de Responsabilidade Limitada'),
        ('OUTRA', 'Outra'),
    ]

    tipo_pessoa = models.CharField(max_length=10, choices=TIPO_PESSOA_CHOICES, default='PF')
    nome_completo = models.CharField(max_length=100, blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    rg = models.CharField(max_length=20, blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=True, null=True)
    emprego_ocupacao = models.CharField(max_length=100, blank=True, null=True)
    numero_telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    # Dados de endereço
    cep = models.CharField(max_length=10, blank=True, null=True)
    logradouro = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    ug = models.CharField(max_length=10, blank=True, null=True)

    # Dados específicos para Pessoa Jurídica
    razao_social = models.CharField(max_length=100, blank=True, null=True)
    nome_fantasia = models.CharField(max_length=100, blank=True, null=True)
    cnpj = models.CharField(max_length=18, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    natureza = models.CharField(max_length=20, choices=NATUREZA_CHOICES, blank=True, null=True)
    nome_representante = models.CharField(max_length=100, blank=True, null=True)
    cpf_representante = models.CharField(max_length=14, blank=True, null=True)
    telefone_representante = models.CharField(max_length=20, blank=True, null=True)

#RELAÇÃO COM CONTRATOS
    def get_contrato(self):
        from GestaoContrato.models import Contrato
        return Contrato.objects.get(id=self.contrato_id)

    contrato = models.ForeignKey(
                'GestaoContrato.Contrato',
                on_delete=models.SET_NULL,
                null=True,
                blank=True,
                related_name='clienteContrato')

    descricaoCliente = models.TextField(null=True)

    # GRUPO INSERIDO
    grupo = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome_completo if self.nome_completo else self.razao_social
