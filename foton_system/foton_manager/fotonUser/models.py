from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class Usuario(AbstractUser):
    # Adicione campos personalizados para o modelo de usuário, se necessário
    # ...
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
