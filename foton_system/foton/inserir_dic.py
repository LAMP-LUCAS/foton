import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foton.settings')
django.setup()

from gestao_cliente.models import Cliente
from gestao_contrato.models import Contrato
from gestao_orcamento.models import Orcamento

# Dicionário com os dados do cliente
data_cliente = {
    'nome': 'João Silva',
    'email': 'joao.silva@example.com'
}

# Cria e salva um novo objeto Cliente no banco de dados
cliente = Cliente.objects.create(**data_cliente)

# Dicionário com os dados do contrato
data_contrato = {
    'titulo': 'João Silva',
    'data': '2023-05-20'
}

# Cria e salva um novo objeto contrato no banco de dados
contrato = Contrato.objects.create(**data_contrato)

# Dicionário com os dados do contrato
data_orcamento = {
    'descricao': 'João Silva',
    'valor': '100'
}

# Cria e salva um novo objeto orcamento no banco de dados
orcamento = Orcamento.objects.create(**data_orcamento)
