from django.contrib import admin
from django.contrib.auth.models import User
from .models import Organizacao

class OrganizacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'razao_social', 'cnpj', 'user')

admin.site.register(Organizacao, OrganizacaoAdmin)