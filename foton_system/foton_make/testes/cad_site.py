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

# Configuração do log
logging.basicConfig(filename='email_extraction.log', level=logging.INFO)


def job():
    print('iniciando job')
    try:
        print('iniciando Try')
        logging.info('Conectando...')
        #username = os.getenv('EMAIL_USERNAME')
        #password = os.getenv('EMAIL_PASSWORD')
        # informações da conta
        username = "cadastro@arqlamp.com"
        password = "@Arqcadastro0451"   

        # crie uma instância do IMAP4 class com SSL 
        mail = imaplib.IMAP4_SSL("imap.hostinger.com")
        # autentique
        mail.login(username, password)
        print('email conectado')

        # selecione a caixa de correio que você deseja verificar
        pasta = "INBOX.cadastroSite"
        mail.select(pasta)
        print(f'pasta encontrada {mail.select(pasta)}')

        # faça uma busca com o critério ALL
        result, data = mail.uid('search', None, "ALL")
        mensagem = 'Pesquisando data'
        print(f'{mensagem}')
        # lista para armazenar os dados do e-mail
        email_data = []

        

        # percorra todos os e-mails
        mensagem = f'Percorrendo e-mails na pasta: {pasta}'
        logging.info(f'{mensagem}')
        print(f'{mensagem}') 

        # percorra todos os e-mails
        for num in data[0].split():
            result, data = mail.uid('fetch', num, '(BODY[1])')
            raw_email = data[0][1].decode("utf-8")
            email_message = email.message_from_string(raw_email)

            print(f'\n\nmensagem de email:\n{raw_email}\n')
            print(type(email_message))
            mensagem = str(email_message)
            print(mensagem)
            print(type(mensagem))


            # obtenha o corpo do e-mail
            body = email_message.get_payload()

            # use expressões regulares para extrair as informações
            nome = re.search(r'nome=3D(.*)', body)
            email_from = re.search(r'email=3D(.*)', body)
            telefone = re.search(r'telefone=3D(.*)', body)

            # adicione os detalhes à lista
            email_data.append({'nome': nome.group(1)[:-1] if nome else None,
                            'email': email_from.group(1)[:-1] if email_from else None,
                            'telefone': telefone.group(1)[:-1] if telefone else None})

        # crie um DataFrame pandas com as informações do e-mail
        df = pd.DataFrame(email_data)

        mensagem = f'Data Frame Criado com Sucesso:\n\n {df}\n\n'
        logging.info(f'{mensagem}')            
        print(f'{mensagem}')

        salvar = input('Deseja salvar o dataframe? s/n \n')

        if salvar.upper() == 'S':
            df.to_csv('email_data.csv', index=False)
            logging.info('Data Frame Salvo com Sucesso')
        else:
            mensagem = 'Processo Cancelado'
            input(mensagem)

    except Exception as e:
        logging.error(f'Erro ao extrair e-mails: {e}')

schedule.every(1).minute.do(job)

print('Iniciando Código')

while True:
    logging.info('Procurando e-mail...')
    job()
    schedule.run_pending()
    time.sleep(1)
    print('Fim do código')
