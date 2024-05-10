from cliente_library import Verificador, Gerenciador
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
import os


verificador = Verificador()
gerenciador = Gerenciador()

def enviar_feedback(email_from, senha, mensagem):
    """
    Envia um e-mail de feedback para um endereço específico usando as credenciais do usuário.

    Args:
    email_from (str): O endereço de e-mail do remetente.
    senha (str): A senha do e-mail do remetente para autenticação no servidor SMTP.
    mensagem (str): A mensagem de texto a ser enviada como feedback.

    Esta função configura uma mensagem de e-mail e a envia usando o servidor SMTP do Gmail.
    O processo inclui autenticação TLS e login com as credenciais do usuário.
    Em caso de falha, uma exceção será impressa na saída.
    """

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

def get_feedback_history():
    feedback_file = 'feedback_history.txt'
    if os.path.exists(feedback_file):
        with open(feedback_file, 'r') as file:
            history = file.read()
        print("Histórico de Feedback:")
        print(history)
    else:
        print("Não há histórico de feedback.")

def exibir_clientes_registrados():
    print("Clientes da base de dados:")
    
    Lista_base_clientes = verificador.Lista_alias_Clientes_Base()

    for i, alias in enumerate(Lista_base_clientes):
        print(f'Nome na Base - {i} : {alias}' )
    
    print("Fim da lista.")

def exibir_clientes_servidor():
    print("Pastas de Clientes do Servidor:")

    Lista_pastas_clientes = verificador.Lista_Pastas_Clientes()

    for i, pasta in enumerate(Lista_pastas_clientes):
        print(f'pasta Cliente - {i} : {pasta}' )
    
    print("Fim da lista.")

def sincronizar_Clientes():
    print("Sincronizando Clientes do Servidor com Base de dados...")
    print(" Iniciando verificação de pastas de Clientes faltantes...")

    gerenciador.atualizar_base_Clientes()

    print("Sincronização de pastas faltantes concluída.")

def Exibir_Servicos_registrados():
    print("Serviços registrados na base de dados:")

    Lista_Servicos_registrados = verificador.lista_servicos_clientes()

    for i, servico in enumerate(Lista_Servicos_registrados):
        print(f'Serviço base - {i} : {servico}' )
    
    print("Fim da lista.")

def Exibir_Servicos_Servidor():
    print("Serviços no Servidor:")

    Lista_Servicos_Servidor = verificador.lista_pastas_servicos()

    for i, servico in enumerate(Lista_Servicos_Servidor):
        print(f'Serviço no Servidor - {i} : {servico}' )
    
    print("Fim da lista.")
    return

def sincronizar_Servicos():
    print("Sincronizando Serviços com Base de dados...")
    print(" Iniciando verificação de pastas de Serv faltantes...")

    gerenciador.atualizar_base_servicos()

    print("Sincronização de pastas faltantes concluída.")

def main():
    """
    Função principal que orquestra a verificação de integridade e atualização de pastas de clientes,
    seguida pela opção de enviar feedback.

    Este método inicializa objetos de Verificador e Gerenciador, verifica a existência de base de dados e
    diretórios de clientes. Se tudo estiver correto, prossegue com a criação de pastas faltantes e atualização
    da base de dados. O usuário é então perguntado se deseja enviar um feedback, o qual, se afirmativo,
    será coletado e enviado usando a função enviar_feedback.
    """

    #verificando a existencia de arquivos
    try:
        if  verificador.base_existe() and verificador.pasta_clientes_existe():
            print("Verificação completa. Base de dados e diretório de clientes estão acessíveis.")
        else:
            print("Verificação inicial falhou: a base de dados ou o diretório de clientes não estão acessíveis.")
    except Exception as e:
        print(f"Ocorreu um erro durante a operação: {e}")
        print("Por favor, verifique as configurações e os caminhos de arquivos especificados e tente novamente.")

    menu_options = {
        '1': ['Exibir Clientes Registrados',exibir_clientes_registrados],
        '2': ['Exibir Clientes no Servidor',exibir_clientes_servidor],
        '3': ['Exibir Servicos Registrados',Exibir_Servicos_registrados],
        '4': ['Exibir Servicos no Servidor',Exibir_Servicos_Servidor],
        '5': ['Sincronizar Clientes',sincronizar_Clientes],
        '6': ['Sincronizar Serviços',sincronizar_Servicos],
        '7': ['Exibir Histórico de Feedback',get_feedback_history],
        '8': ['Enviar Feedback',lambda: enviar_feedback(input("Digite seu e-mail: "), getpass.getpass("Digite sua senha: "), input("Digite seu feedback: "))],
        '9': ['Finalizar Programa',lambda: exit("Finalizando Programa...\n")]
    }

    while True:
        print("\nEscolha uma opção:")

        for item in menu_options:
            print(f'{item} - {menu_options[item][0]}')

        escolha = input("Digite o número da opção desejada: ")
        action = menu_options.get(escolha)
        action = action[1]
        print("")
        if action:
            action()
        else:
            print("\nOpção inválida. Por favor, tente novamente.\n")

if __name__ == "__main__":
    main()
