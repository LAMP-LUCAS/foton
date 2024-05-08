from cliente_library import Verificador, Gerenciador

def main():
    diretorio_base = 'C:\\Users\\Lucas\\OneDrive\\LAMP ARQUITETURA\\foton\\foton_system\\foton_make\\testes\\CLIENTES'
    dataBase = 'C:\\Users\\Lucas\\OneDrive\\LAMP ARQUITETURA\\foton\\foton_system\\foton_make\\testes\\base.xlsx'
    
    verificador = Verificador(diretorio_base, dataBase)
    gerenciador = Gerenciador(diretorio_base, dataBase)

    if verificador.base_existe() and verificador.pasta_clientes_existe():
        print("Base e diretório de clientes existem. Verificando e criando pastas faltantes...")
        gerenciador.criar_pastas_clientes_faltantes()
        print('Atualizando a base de dados:')
        gerenciador.atualizar_base()
    else:
        print("Erro: A base de dados ou o diretório de clientes não existem!")

if __name__ == "__main__":
    main()
