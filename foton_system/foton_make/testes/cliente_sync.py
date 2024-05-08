from cliente_library import Verificador, Gerenciador
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass

def enviar_feedback(email_from, senha, mensagem):
    email_to = 'contato@arqlamp.com'  # Email de suporte técnico da empresa ou desenvolvedor

    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = email_to
    msg['Subject'] = '[FEEDBACK INTERNO - GER CLIENTES]'

    body = MIMEText(mensagem, 'plain')
    msg.attach(body)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Configuração para Gmail, alterar se necessário
        server.starttls()
        server.login(email_from, senha)
        text = msg.as_string()
        server.sendmail(email_from, email_to, text)
        server.quit()
        print("Feedback enviado com sucesso!")
    except Exception as e:
        print(f"Falha ao enviar feedback: {e}")

def main():
    '''
    diretorio_base = configuracoes['diretorio_base']  # Carrega configuração do arquivo config.json
    dataBase = configuracoes['dataBase']             # Carrega configuração do arquivo config.json
    '''    
    #verificador = Verificador(diretorio_base, dataBase)
    #gerenciador = Gerenciador(diretorio_base, dataBase)

    verificador = Verificador()
    gerenciador = Gerenciador()

    try:
        if  verificador.base_existe() and verificador.pasta_clientes_existe():
            print("Verificação completa. Base de dados e diretório de clientes estão acessíveis.")
            print("Iniciando verificação de pastas faltantes...")
            gerenciador.criar_pastas_clientes_faltantes()
            print("Verificação de pastas faltantes concluída.")
            print('Iniciando atualização da base de dados...')
            gerenciador.atualizar_base()
            print('Atualização da base de dados concluída com sucesso.')
            
            # Solicitar feedback
            print("\nGostaria de enviar um feedback sobre o sistema? (s/n)")
            if input().lower() == 's':
                email_from = input("Digite seu e-mail: ")
                senha = getpass.getpass("Digite sua senha: ")
                mensagem = input("Digite seu feedback: ")
                enviar_feedback(email_from, senha, mensagem)

        else:
            print("Verificação inicial falhou: a base de dados ou o diretório de clientes não estão acessíveis.")
    except Exception as e:
        print(f"Ocorreu um erro durante a operação: {e}")
        print("Por favor, verifique as configurações e os caminhos de arquivos especificados e tente novamente.")

if __name__ == "__main__":
    main()
