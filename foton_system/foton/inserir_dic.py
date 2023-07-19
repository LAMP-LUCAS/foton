import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foton.settings')
django.setup()

from GestaoCliente.models import Cliente
from GestaoContrato.models import Contrato
from GestaoOrcamento.models import Orcamento

def cad_cliente():
    data_cliente = {'nome': '','email': ''}
    print('Insira os dados para cadastrar o cliente')
    nome = input('Nome do cliente: ')
    email = input('Email do cliente: ')
    data_cliente['nome'] = nome
    data_cliente['email'] = email
    return data_cliente

def salv_cliente(data_cliente):
    # Cria e salva um novo objeto Cliente no banco de dados
    try:
        cliente = Cliente.objects.create(**data_cliente)
        print('cliente salvo')
    except:
        print('erro ao salvar')

def cad_orcamento():
    data_orcamento = {'cliente': '', 'valor': ''}
    print('Insira os dados para cadastrar o orçamento')
    cliente = input('Nome do cliente: ')
    valor = input('Valor do orçamento: ')
    data_orcamento['cliente'] = cliente
    data_orcamento['valor'] = valor
    return data_orcamento

def salv_orcamento(data_orcamento):
    # Cria e salva um novo objeto Orcamento no banco de dados
    try:
        orcamento = Orcamento.objects.create(**data_orcamento)
        print('orçamento salvo')
    except:
        print('erro ao salvar')

def cad_contrato():
    data_contrato = {'cliente': '', 'valor': '', 'data_inicio': '', 'data_fim': ''}
    print('Insira os dados para cadastrar o contrato')
    cliente = input('Nome do cliente: ')
    valor = input('Valor do contrato: ')
    data_inicio = input('Data de início do contrato (dd/mm/aaaa): ')
    data_fim = input('Data de término do contrato (dd/mm/aaaa): ')
    data_contrato['cliente'] = cliente
    data_contrato['valor'] = valor
    data_contrato['data_inicio'] = data_inicio
    data_contrato['data_fim'] = data_fim
    return data_contrato

def salv_contrato(data_contrato):
    # Cria e salva um novo objeto Contrato no banco de dados
    try:
        contrato = Contrato.objects.create(**data_contrato)
        print('contrato salvo')
    except:
        print('erro ao salvar')

def cadastros():
    pergunta1 = 'Deseja cadastrar cliente, contrato ou orçamento? Ou nada? '
    decisao = input(pergunta1)
    
    if decisao == 'cliente':
        cliente = cad_cliente()
        print(cliente)
        salvar = input('Deseja salvar no banco de dados? Sim ou não? ')
        
        if salvar == 'sim':
            salv_cliente(cliente)
        else:
            print('Não salvo')
        
        cadastros()
    
    elif decisao == 'contrato':
        contrato = cad_contrato()
        print(contrato)
        
        salvar = input('Deseja salvar no banco de dados? Sim ou não? ')
        
        if salvar == 'sim':
            salv_contrato(contrato)
        else:
            print('Não salvo')
        
        cadastros()
    
    elif decisao == 'orcamento':
        orcamento = cad_orcamento()
        print(orcamento)
        
        salvar = input('Deseja salvar no banco de dados? Sim ou não? ')
        
        if salvar == 'sim':
            salv_orcamento(orcamento)
        else:
            print('Não salvo')
        
        cadastros()
    
    elif decisao == 'nada':
        prog = 0
        print('finalizando o programa...')
        return prog
    

    else:
        decisao = input(pergunta1)
        
        if decisao not in ['cliente', 'contrato', 'orcamento', 'nada']:
            print('Erro de decisão, repita')

while cadastros() != 0:
    cadastros()