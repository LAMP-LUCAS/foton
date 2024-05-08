from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Organizacao(models.Model):

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

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if not self.user:
            self.user = User.objects.get(username='lucas')
        super().save(*args, **kwargs)

    def __str__(self):
        #self.nome
        str(self.id) if self.id is not None else ''
'''
        if self.nome_fantasia:
            return self.nome_fantasia
        else:
            return self.nome_completo
'''

class Usuario(AbstractUser):
    # Adicione campos personalizados para o modelo de usuário, se necessário
    organizacao = models.ForeignKey(Organizacao, on_delete=models.CASCADE, null=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('grupos'),
        blank=True,
        help_text=_(
            'Os grupos aos quais este usuário pertence. Um usuário terá todas as permissões '
            'concedidas a cada um de seus grupos.'
        ),
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('permissões de usuário'),
        blank=True,
        help_text=_('Permissões específicas para este usuário.'),
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )

    def __str__(self):
        return self.username

class Autorizacao(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    # Adicione campos para definir as autorizações do usuário, como permissões, papéis, etc.
    # ...

    def __str__(self):
        return str(self.usuario)

