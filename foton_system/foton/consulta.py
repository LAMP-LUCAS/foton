import os
print(' COMEÇANDO O CÓDIGO ')
print(os.environ.get('DJANGO_SETTINGS_MODULE'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foton.settings')
print(os.environ.get('DJANGO_SETTINGS_MODULE'))
import django
django.setup()

from gestao_cliente.models import Cliente
from gestao_contrato.models import Contrato
from gestao_orcamento.models import Orcamento


print(' COMEÇANDO O CÓDIGO ')
print(os.environ.get('DJANGO_SETTINGS_MODULE'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foton.settings')


clientes = Cliente.objects.all()
for cliente in clientes:
    print(cliente)

print('-------PROXIMA APLICAÇÃO-------')

contratos = Contrato.objects.all()
for contrato in contratos:
    print(contrato)

print('-------PROXIMA APLICAÇÃO-------')

orcamentos = Orcamento.objects.all()
for orcamento in orcamentos:
    print(orcamento)