'''
Dados do servidor: 
Protocolo
Nome
Porta
Encryption
Incoming server (IMAP)
imap.hostinger.com 993 SSL

Incoming server (POP)
pop.hostinger.com 995 SSL

Outgoing server (SMTP)
smtp.hostinger.com 465 SSL


from myapp.models import Cliente

for index, row in df.iterrows():
    cliente = Cliente(nome=row['nome'], email=row['email'], telefone=row['telefone'])
    cliente.save()
# Lembre-se de substituir 'myapp' pelo nome do seu aplicativo Django e Cliente pelo nome do seu modelo.



'''


import imaplib
import email
from email.header import decode_header
import pandas as pd
import schedule
import time
import os
import logging
import re
from bs4 import BeautifulSoup
import html


# Configuração do log
logging.basicConfig(filename='email_extraction.log', level=logging.INFO)

def ExtractEmailData(email_body):
    # Use expressões regulares para encontrar a tabela
    table_match = re.search(r'<table.*?>.*?</table>', email_body, re.DOTALL)
    if table_match:
        print('tabela de dados encontrada no email')
        data = ExtractEmailDataTable(table_match)
        return data
    else:
        print('tabela não encontrada')
        return ExtractEmailTextBody(email_body)

def clean_value(value):
    """Removes unwanted characters from the value.

    Args:
        value: The string value to be cleaned.

    Returns:
        The cleaned string value.
    """
    # Define unwanted characters as a list
    unwanted_chars = ['= io', '= ', ' =', 'td>']

    cleaned_value = value.strip()  # Remove leading and trailing whitespace

    # Iterate through unwanted characters and replace them one by one
    for char in unwanted_chars:
        cleaned_value = cleaned_value.replace(char, '')

    # Replace the encoded character with its decoded form
    cleaned_value = cleaned_value.replace('=C3=A3', 'ã')
    cleaned_value = cleaned_value.replace('=C3=A1','á')
    #cleaned_value = cleaned_value.replace('')

    # Optionally, remove extra characters specifically from email values
    if cleaned_value.startswith('EmailCliente=') and cleaned_value.endswith('= td>'):
        cleaned_value = cleaned_value[14:-6]  # Assuming consistent format for email

    return cleaned_value

def ExtractEmailDataTable(table_match):
    print('-------------------------------\nIniciando ExtractEmailDataTable')
    table_html = table_match.group(0)
    decoded_html = html.unescape(table_html)

    # Use pandas to read the HTML table
    df = pd.read_html(decoded_html,flavor='lxml')[0]
    print(f'Data Frame criado com os dados HTML:\n{df}\n')

    # Verifique se as colunas "Name" e "Value" estão presentes
    if 'Name' in df.columns and 'Value' in df.columns:
        TableData = {}
        for name in df['Name']:
            print('Limpando valor do nome...')
            cleaned_name = clean_value(name)
            print('Valor do nome limpo:', cleaned_name)

            # Buscar valor correspondente na coluna "Value"
            value_index = df['Name'].index[df['Name'] == name]
            if not value_index.empty:
                cleaned_value = clean_value(df.loc[value_index[0], 'Value'])
                print('Limpando valor do email...')
                print('Valor do email limpo:', cleaned_value)

                TableData[cleaned_name] = cleaned_value

    print(f'Lista de dados das tabelas encontradas:\n{TableData}\n-------------------------------\n')
    return TableData

def ExtractEmailTextBody(email_body):
    # Use expressões regulares para extrair as informações
    nome = re.search(r'nome=3D(.*)', email_body)
    email_from = re.search(r'email=3D(.*)', email_body)
    telefone = re.search(r'telefone=3D(.*)', email_body)

    # Crie um dicionário com os detalhes extraídos
    details = {
        'nome': nome.group(1)[:-1] if nome else None,
        'email': email_from.group(1)[:-1] if email_from else None,
        'telefone': telefone.group(1)[:-1] if telefone else None
    }

    return details

def EmailConect():
    print('-------------------------------\nIniciando EmailConect')
    logging.info('Conectando...')
    # Informações da conta
    username = "cadastro@arqlamp.com"
    password = " "

    # Crie uma instância do IMAP4 class com SSL
    mail = imaplib.IMAP4_SSL("imap.hostinger.com")
    # Autentique
    mail.login(username, password)
    print(f'E-mail conectado!\nUsername: {username}\nPassword: {password}\nMail: {mail}\n-------------------------------\n')
    return mail

def EmailFolder(mail):
    # Selecione a caixa de correio que você deseja verificar
    print(f'-------------------------------\nIniciando EmailFolder\n')
    pasta = "INBOX.cadastroSite"
    #pasta = "INBOX"
    print(f'email puro: {mail}')
    folder = mail.select(pasta)
    print(f'pasta {pasta} no email {mail}:  {folder}\n-------------------------------\n')

    return folder

def EmailSearch(mail, Keyword):
    # Faça uma busca com o critério definido
    print('-------------------------------\niniciando EmailSearch')
    Keyword = str(Keyword)
    #print(f'Palavra de busca: {Keyword}')
    #print(f'\nnovo mail: {mail}\n')

    result, data = mail
    #print(f'\nA variável result: {result}')
    #print(f'A variável data: {data}\n\n')

    #result, data = mail.uid('search', None, Keyword)
    if result == 'OK':
        uids = data[0].split()
        #print(f'UIDs encontrados: {uids}')
    else:
        print(f'Erro ao buscar e-mails: {result}')

    print('-------------------------------\n')
    return result, data
 
def EmailFilter(result,data, mail):
        print('-------------------------------\niniciando EmailFilter')
        # Lista para armazenar os dados do e-mail
        email_data = []
        mail = mail
        # Percorra todos os e-mails
        for num in data[0].split():
            result, data = mail.uid('fetch', num, '(BODY[1])')
            raw_email = data[0][1].decode("utf-8")
            email_message = email.message_from_string(raw_email)
            #print(f'mensagem do email {num}:\n{email_message}')

            # Obtenha o corpo do e-mail
            body = email_message.get_payload()
            #print(f'Corpo do email {num}:\n{body}')


            # Extraia os detalhes do e-mail
            details = ExtractEmailData(body)
            #print(f'~~~~~~~~~~~~\nCorpo do email {num}:\n{body}\n~~~~~~~~~~~~\n')
            email_data.append(details)

        print(f'dados dos emails:\n{email_data}\n')
        print('-------------------------------\n')
        return email_data

def job():
    print('\n-------------------------------\nIniciando job\n-------------------------------\n')
    try:
        mail = EmailConect()
        mailFolder = EmailFolder(mail)
        # Faça uma busca com o critério ALL
        Keyword = 'ALL'

        print(f'Keyword de pesquisa em job: {Keyword}')

        result, data = EmailSearch(mailFolder,Keyword) #A partir daqui dá ruim
        
        print('data em job = ', data)

        result, data = mail.uid('search', None, Keyword)

        print('uids data em job = ', data)

        email_data = EmailFilter(result, data,mail)

        # Crie um DataFrame pandas com as informações do e-mail
        df = pd.DataFrame(email_data)

        print(f'Data Frame criado com sucesso:\n\n{df}\n')

        salvar = input('Deseja salvar o DataFrame? (s/n): ')

        if salvar.upper() == 'S':
            df.to_csv('email_data.csv', index=False)
            print('Data Frame salvo com sucesso')
        else:
            print('Processo cancelado')

    except KeyboardInterrupt:
        finalização()

    except Exception as e:
        print(f'Erro ao extrair e-mails: {e}')

def finalização():
    if KeyboardInterrupt:
        print('Programa interrompido pelo usuário')
        exit()
    else:
        print('fim do programa')

schedule.every(1).minute.do(job)

print('\n\n######## Iniciando Código ###########\n\n')

while True:
    try:
        logging.info('Procurando e-mail...')
        job()
        schedule.run_pending()
        time.sleep(1)
        print('\nFim do código\n')
    except KeyboardInterrupt:
        finalização()