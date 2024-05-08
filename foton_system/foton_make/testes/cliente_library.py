import pandas as pd
from pathlib import Path
from datetime import datetime
import logging
import json
import argparse
import os

# Exceções Personalizadas
class ConfigError(Exception):
    """Exceção lançada por erros de configuração."""
    pass

class DatabaseError(Exception):
    """Exceção lançada por falhas na base de dados."""
    pass

class FilesystemError(Exception):
    """Exceção lançada por erros no sistema de arquivos."""
    pass


class Configuracoes:
    def Carregar_config():
        ## Obtenha o diretório do script Python atualmente em execução
        diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
        ## Construa o caminho do arquivo config.json
        caminho_do_arquivo_config = os.path.join(diretorio_do_script, 'config.json')

        return caminho_do_arquivo_config

    def config():
        caminho_configFile = Configuracoes.Carregar_config()
        print('caminho é : ',caminho_configFile)
        try:
            with open('config.json', 'r') as config_file:
                config_file = json.load(config_file)
        except FileNotFoundError:
            raise ConfigError("O arquivo de configuração 'config.json' não foi encontrado.")
        except json.JSONDecodeError:
            raise ConfigError("Erro ao decodificar o arquivo de configuração 'config.json'.")
        
        return config_file
    
    def pastaClientes():
        diretorio = Path(config['caminho_pastaClientes'])
        return diretorio

    def baseClientes():
        base = Path(config['caminho_baseClientes'])
        return base

# Carregar configurações
try:
    caminho_config = Configuracoes.Carregar_config()
    with open(caminho_config, 'r') as config_file:
        config = json.load(config_file)
except FileNotFoundError:
    raise ConfigError("O arquivo de configuração 'config.json' não foi encontrado.")
except json.JSONDecodeError:
    raise ConfigError("Erro ao decodificar o arquivo de configuração 'config.json'.")

# Configuração do Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#base
class BaseServidor:
    def __init__(self):
        try:
            self.pastaClientes = Path(config['caminho_pastaClientes'])
            self.baseClientes = Path(config['caminho_baseClientes'])
            if not self.pastaClientes.is_dir():
                raise FilesystemError(f"O caminho {self.pastaClientes} não é um diretório válido.")
            if not self.baseClientes.suffix == '.xlsx':
                raise DatabaseError(f"A base de clientes {self.baseClientes} não é um arquivo Excel válido.")
        except KeyError as e:
            raise ConfigError(f"A configuração '{e.args[0]}' está ausente no arquivo de configuração.")

class Verificador(BaseServidor):
    def base_existe(self):
        if not self.baseClientes.exists():
            raise DatabaseError(f"A base de dados em {self.baseClientes} não existe.")
        return True

    def pasta_clientes_existe(self):
        if not self.pastaClientes.exists():
            raise FilesystemError(f"A pasta de clientes em {self.pastaClientes} não existe.")
        return True

    def obter_aliases(self):
        try:
            df = pd.read_excel(self.baseClientes)
            return df['Alias'].tolist()
        except FileNotFoundError:
            raise DatabaseError(f"O arquivo {self.baseClientes} não foi encontrado.")
        except pd.errors.EmptyDataError:
            raise DatabaseError("A base de dados está vazia.")
        except Exception as e:
            raise DatabaseError(f"Erro ao processar a base de dados: {e}")

    def verificar_pastas_clientes(self):
        if not self.pasta_clientes_existe():
            raise FilesystemError(f"A pasta {self.pastaClientes} não existe ou não pode ser acessada.")
        aliases = self.obter_aliases()
        pasta_clientes = {pasta.name for pasta in self.pastaClientes.iterdir() if pasta.is_dir()}
        return set(aliases) - pasta_clientes
    
    def verificar_pastas_nao_listadas(self):
        aliases = set(self.obter_aliases())
        pastas_fisicas = {pasta.name for pasta in self.pastaClientes.iterdir() if pasta.is_dir()}
        return pastas_fisicas - aliases

class Gerenciador(BaseServidor):
    def criar_pasta(self, nome):
        try:
            pasta = self.pastaClientes / nome
            pasta.mkdir(exist_ok=True)
            logging.info(f'Pasta "{nome}" criada com sucesso.')
        except PermissionError:
            raise FilesystemError(f"Permissão negada ao tentar criar a pasta {nome}.")
        except Exception as e:
            raise FilesystemError(f'Erro inesperado ao criar pasta "{nome}": {e}')

    def criar_pastas_clientes_faltantes(self):
        verificador = Verificador()
        clientes_faltantes = verificador.verificar_pastas_clientes()
        if not clientes_faltantes:
            logging.info("Não há pastas de clientes faltantes para criar.")
        for cliente in clientes_faltantes:
            self.criar_pasta(cliente)

    def atualizar_base(self):
        verificador = Verificador()
        pastas_nao_listadas = verificador.verificar_pastas_nao_listadas()
        if not pastas_nao_listadas:
            logging.info("Nenhuma atualização necessária na base de dados.")
        else:
            try:
                df_atual = pd.read_excel(self.baseClientes)
                novos_dados = pd.DataFrame(list(pastas_nao_listadas), columns=['Alias'])
                df_novo = pd.concat([df_atual, novos_dados], ignore_index=True)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                novo_nome_base = self.baseClientes.parent / f"base_{timestamp}.xlsx"
                df_novo.to_excel(novo_nome_base, index=False)
                logging.info(f"Base de dados atualizada e salva como {novo_nome_base}")
            except Exception as e:
                raise DatabaseError(f"Erro ao atualizar a base de dados: {e}")

def main():
    parser = argparse.ArgumentParser(description="Gerenciador de pastas e bases de clientes")
    parser.add_argument('--criar-pastas', action='store_true', help='Cria pastas para clientes faltantes')
    parser.add_argument('--atualizar-base', action='store_true', help='Atualiza a base de dados com novas pastas encontradas')
    args = parser.parse_args()

    gerenciador = Gerenciador()

    if args.criar_pastas:
        gerenciador.criar_pastas_clientes_faltantes()
    
    if args.atualizar_base:
        gerenciador.atualizar_base()


if __name__ == "__main__":
    main()