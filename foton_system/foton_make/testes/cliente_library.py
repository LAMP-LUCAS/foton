"""
Script para gerenciamento de pastas e bases de dados de clientes.

Este módulo automatiza a criação de pastas para clientes baseado em uma lista pré-definida
e atualiza uma base de dados Excel com novas entradas de pastas criadas. Utiliza configurações
externas definidas em um arquivo JSON e oferece uma interface de linha de comando para iniciar
as operações.

Exceções personalizadas são definidas para lidar com erros específicos de configuração,
base de dados e sistema de arquivos.

Requisitos:
    pandas: Manipulação de base de dados Excel.
    pathlib: Navegação e manipulação segura de caminhos de sistema de arquivos.
    datetime: Geração de timestamps para versionamento de arquivos.
    logging: Registro de atividades e erros.
    json: Carregamento de configurações externas.
    argparse: Interpretação de argumentos de linha de comando.
    os: Interação com o sistema operacional para obter caminhos de arquivos.

Classes:
    ConfigError: Erros de configuração.
    DatabaseError: Erros de manipulação de base de dados.
    FilesystemError: Erros de sistema de arquivos.
    Configuracoes: Carrega as configurações do arquivo JSON.
    BaseServidor: Base para classes que interagem com o sistema de arquivos e bases de dados.
    Verificador: Verifica a existência de bases de dados e pastas.
    Gerenciador: Gerencia a criação de pastas e atualização da base de dados.

Funções:
    main(): Função principal que interpreta argumentos de linha de comando e inicia os processos.

Uso:
    Execute o script com argumentos opcionais para especificar operações:
    --criar-pastas: Cria pastas para clientes que estão listados na base mas não têm pasta correspondente.
    --atualizar-base: Atualiza a base de dados com novas pastas encontradas que não estão listadas.

Configurações:
    As configurações do sistema são lidas de 'config.json', que deve estar no mesmo diretório que o script.
    Este arquivo deve especificar caminhos para a pasta de clientes e para a base de dados.

Logging:
    Todas as operações significativas e erros são registrados tanto em um arquivo de log 'log.txt' quanto no console.
"""

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
    @staticmethod
    def Carregar_config():
        """Retorna o caminho completo para o arquivo de configuração 'config.json' localizado no diretório do script."""

        ## Obtenha o diretório do script Python atualmente em execução
        diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
        ## Construa o caminho do arquivo config.json
        caminho_do_arquivo_config = os.path.join(diretorio_do_script, 'config.json')

        return caminho_do_arquivo_config
    
    @staticmethod
    def config():
        """
        Carrega o arquivo de configuração 'config.json'.
        
        Retorna:
            dict: Dicionário com configurações carregadas.

        Exceções:
            ConfigError: Erros durante o carregamento ou decodificação do arquivo de configuração.
        """
        
        caminho_configFile = Configuracoes.Carregar_config()
        print('caminho é : ',caminho_configFile)
        try:
            with open(caminho_configFile, 'r') as config_file:
                config_file = json.load(config_file)
        except FileNotFoundError:
            raise ConfigError("O arquivo de configuração 'config.json' não foi encontrado.")
        except json.JSONDecodeError:
            raise ConfigError("Erro ao decodificar o arquivo de configuração 'config.json'.")
        
        return config_file

    @staticmethod
    def basePasta(config_file):
        """Retorna o caminho para a pasta dos Clientes configurada."""
        config = config_file
        return Path(config['caminho_pastaClientes'])

    @staticmethod
    def baseUnificada(config_file):
        """Retorna o caminho para a base de dados configurada."""
        config = config_file
        return Path(config['caminho_baseDados'])

    @staticmethod
    def baseDados(config_file):
        """Retorna o caminho para a base de dados configurada."""
        config = config_file
        return Path(config['caminho_baseDados'])

    @staticmethod
    def baseClientes(config_file):
        """Retorna o caminho para a base de dados configurada."""
        config = config_file
        return Path(config['caminho_baseClientes'])

    @staticmethod
    def baseServicos(config_file):
        """Retorna o caminho para a base de dados configurada."""
        config = config_file
        return Path(config['caminho_baseServicos'])

# Carregar configurações
configFile = Configuracoes.config()
basePasta = Configuracoes.basePasta(configFile)
baseDados = Configuracoes.baseDados(configFile)
baseServicos = Configuracoes.baseServicos(configFile)
baseClientes = Configuracoes.baseUnificada(configFile)



# Configuração do Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
    logging.FileHandler("log.txt"),
    logging.StreamHandler()
    ]   
)

class BaseServidor:
    """
    Classe base para gerenciamento de operações de servidor relacionadas a arquivos e diretórios de clientes.
    
    A classe inicializa caminhos para a pasta de clientes e para a base de dados de clientes, validando
    se os caminhos são adequados e se a base de dados tem o formato correto (arquivo Excel).
    
    Exceções:
        FilesystemError: Erro se o caminho fornecido para a pasta de clientes não é um diretório.
        DatabaseError: Erro se o arquivo de base de dados não é um arquivo Excel.
        ConfigError: Erro se uma configuração esperada está ausente.
    """
    def __init__(self):
        try:
            self.basePasta = Path(basePasta)
            self.baseDados = Path(baseDados)
            if not self.basePasta.is_dir():
                raise FilesystemError(f"O caminho {self.basePasta} não é um diretório válido.")
            if not self.baseDados.suffix == '.xlsx':
                raise DatabaseError(f"A base de clientes {self.baseDados} não é um arquivo Excel válido.")
        except KeyError as e:
            raise ConfigError(f"A configuração '{e.args[0]}' está ausente no arquivo de configuração.")

class Verificador(BaseServidor):
    """
    Classe para verificar a existência e consistência de pastas e arquivos na base de dados de clientes.
    
    Métodos:
        base_existe: Verifica a existência da base de dados.
        pasta_clientes_existe: Verifica a existência da pasta de clientes.
        Lista_alias_Clientes_Base: Extrai e retorna os aliases de clientes a partir da base de dados.
        verificar_pastas_clientes: Compara os aliases da base de dados com as pastas físicas.
        verificar_pastas_nao_listadas: Identifica pastas físicas não listadas na base de dados.
    """

    def base_existe(self):
        """Verifica se o arquivo da base de dados existe."""
        if not self.baseDados.exists():
            raise DatabaseError(f"A base de dados em {self.baseDados} não existe.")
        return True

    def pasta_clientes_existe(self):
        """Verifica se a pasta de clientes existe."""
        if not self.basePasta.exists():
            raise FilesystemError(f"A pasta de clientes em {self.basePasta} não existe.")
        return True

    def Lista_alias_Clientes_Base(self):
        """Retorna uma lista de aliases de clientes a partir da base de dados."""
        try:
            df = pd.read_excel(self.baseDados)
            return df['Alias'].tolist()
        except FileNotFoundError:
            raise DatabaseError(f"O arquivo {self.baseDados} não foi encontrado.")
        except pd.errors.EmptyDataError:
            raise DatabaseError("A base de dados está vazia.")
        except Exception as e:
            raise DatabaseError(f"Erro ao processar a base de dados: {e}")

    def Lista_Pastas_Clientes(self):
        pasta_clientes = {pasta.name for pasta in self.basePasta.iterdir() if pasta.is_dir()}
        return pasta_clientes

    def verificar_pastas_clientes(self):
        """Identifica aliases que não têm uma pasta correspondente no sistema de arquivos."""
        if not self.pasta_clientes_existe():
            raise FilesystemError(f"A pasta {self.basePasta} não existe ou não pode ser acessada.")
        aliases = self.Lista_alias_Clientes_Base()
        pasta_clientes = self.Lista_Pastas_Clientes()
        return set(aliases) - pasta_clientes
    
    def verificar_pastas_nao_listadas(self):
        """Identifica pastas físicas que não estão listadas na base de dados."""
        aliases = set(self.Lista_alias_Clientes_Base())
        pastas_fisicas = {pasta.name for pasta in self.basePasta.iterdir() if pasta.is_dir()}
        return pastas_fisicas - aliases
    
    def verificar_servicos_registrados(self):
        df = pd.read_excel(self.baseDados, sheet_name='baseServicos')
        servicos_registrados = set(df['NomeServico'].tolist())
        return servicos_registrados

    def lista_pastas_servicos(self):
        for cliente_pasta in self.basePasta.iterdir():
            if cliente_pasta.is_dir():
                servicos_registrados = {servico.name for servico in cliente_pasta.iterdir() if servico.is_dir()}
            
        return servicos_registrados

    def lista_servicos_clientes(self):
        """Identifica pastas de serviços para cada cliente que não estão registradas na base de dados."""
        servicos_faltantes = {}
        servicos_registrados = self.verificar_servicos_registrados()

        for cliente_pasta in self.basePasta.iterdir():
            if cliente_pasta.is_dir():
                servicos_cliente = {servico.name for servico in cliente_pasta.iterdir() if servico.is_dir()}
                servicos_nao_listados = servicos_cliente - servicos_registrados
                if servicos_nao_listados:
                    servicos_faltantes[cliente_pasta.name] = list(servicos_nao_listados)

        return servicos_faltantes

class Gerenciador(BaseServidor):
    """
    Classe responsável por gerenciar as operações de criação de pastas e atualização da base de dados.
    
    Métodos:
        criar_pasta: Cria uma pasta no diretório de clientes.
        criar_pastas_clientes_faltantes: Cria pastas para todos os clientes que não têm uma.
        atualizar_base: Atualiza a base de dados com informações de novas pastas encontradas.
    """

    def criar_pasta(self, nome):
        """Cria uma pasta individual para um cliente, dado o nome da pasta."""
        try:
            pasta = self.basePasta / nome
            pasta.mkdir(exist_ok=True)
            logging.info(f'Pasta "{nome}" criada com sucesso.')
        except PermissionError:
            raise FilesystemError(f"Permissão negada ao tentar criar a pasta {nome}.")
        except Exception as e:
            raise FilesystemError(f'Erro inesperado ao criar pasta "{nome}": {e}')

    def criar_pastas_clientes_faltantes(self):
        """Cria pastas para todos os clientes listados na base de dados que ainda não possuem pasta."""
        verificador = Verificador()
        clientes_faltantes = verificador.verificar_pastas_clientes()
        if not clientes_faltantes:
            logging.info("Não há pastas de clientes faltantes para criar.")
        for cliente in clientes_faltantes:
            self.criar_pasta(cliente)

    def atualizar_base_Clientes(self):
        """Atualiza a base de dados com novas pastas encontradas que ainda não estão listadas na base."""
        verificador = Verificador()
        pastas_nao_listadas = verificador.verificar_pastas_nao_listadas()
        if not pastas_nao_listadas:
            logging.info("Nenhuma atualização necessária na base de dados.")
        else:
            try:
                df_atual = pd.read_excel(self.baseDados, sheet_name='baseClientes')
                novos_dados = pd.DataFrame(list(pastas_nao_listadas), columns=['Alias'])
                df_novo = pd.concat([df_atual, novos_dados], ignore_index=True)

                df_novo.to_excel(self.baseDados, sheet_name='baseClientes' , index=False)

                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                novo_nome_base = self.baseDados.parent / f"BKP-baseClientes_{timestamp}.xlsx"
                df_novo.to_excel(novo_nome_base, sheet_name='baseClientes' , index=False)

                logging.info(f"Base de dados atualizada e salva como {novo_nome_base}")
            except Exception as e:
                raise DatabaseError(f"Erro ao atualizar a base de dados: {e}")
            
    def atualizar_base_servicos(self):
        """Atualiza a base de dados 'baseServicos' com novos serviços encontrados."""
        verificador = Verificador()
        servicos_faltantes = verificador.lista_servicos_clientes()

        if not servicos_faltantes:
            logging.info("Todos os serviços já estão registrados na base de dados.")
            return

        try:
            df_atual = pd.read_excel(self.baseDados, sheet_name='baseServicos')
            novos_servicos = []
            for cliente, servicos in servicos_faltantes.items():
                for servico in servicos:
                    novos_servicos.append({'AliasCliente': cliente, 'Alias': servico})
            
            df_novos_servicos = pd.DataFrame(novos_servicos)
            df_novo = pd.concat([df_atual, df_novos_servicos], ignore_index=True)

            df_novo.to_excel(self.baseDados, sheet_name='baseServicos', index=False)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            novo_nome_base = self.baseDados.parent / f"BKP-baseServicos_{timestamp}.xlsx"
            df_novo.to_excel(novo_nome_base, sheet_name='baseServicos' , index=False)

            logging.info(f"Base de dados de serviços atualizada.")
        except Exception as e:
            raise DatabaseError(f"Erro ao atualizar a base de dados de serviços: {e}")

    def atualizar_baseDados(self):

        return

def main():
    parser = argparse.ArgumentParser(description="Gerenciador de pastas e bases de clientes")
    parser.add_argument('--criar-pastas', action='store_true', help='Cria pastas para clientes faltantes')
    parser.add_argument('--atualizar-base', action='store_true', help='Atualiza a base de dados com novas pastas encontradas')
    parser.add_argument('--verificar-servicos', action='store_true', help='Verifica e registra novos serviços nas pastas de clientes')
    parser.add_argument('--atualizar-servicos', action='store_true', help='Atualiza a base de dados com novos serviços encontrados')

    args = parser.parse_args()

    gerenciador = Gerenciador()
    verificador = Verificador()

    if args.criar_pastas:
        gerenciador.criar_pastas_clientes_faltantes()
    
    if args.atualizar_base:
        gerenciador.atualizar_baseDados()

    if args.verificar_servicos:
        verificador.lista_servicos_clientes()

    if args.atualizar_servicos:
        gerenciador.atualizar_base_servicos()

if __name__ == "__main__":
    main()
