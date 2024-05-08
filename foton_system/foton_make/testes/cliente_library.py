import pandas as pd
from pathlib import Path
from datetime import datetime
import logging
import json
import os


# Carregar configurações
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Configuração do Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BaseServidor:
    def __init__(self):
        self.pastaClientes = Path(config['caminho_pastaClientes'])
        self.baseClientes = Path(config['caminho_baseClientes'])

class Verificador(BaseServidor):
    def base_existe(self):
        try:
            return self.baseClientes.exists()
        except Exception as e:
            logging.error(f"Erro ao verificar existência da base: {e}")
            return False

    def pasta_clientes_existe(self):
        try:
            return self.pastaClientes.exists()
        except Exception as e:
            logging.error(f"Erro ao verificar existência da pasta de clientes: {e}")
            return False

    def obter_aliases(self):
        try:
            df = pd.read_excel(self.baseClientes)
            return df['Alias'].tolist()
        except Exception as e:
            logging.error(f"Erro ao ler base de clientes: {e}")
            return []

    def verificar_pastas_clientes(self):
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
            (self.pastaClientes / nome).mkdir()
            logging.info(f'Pasta "{nome}" criada com sucesso.')
        except Exception as e:
            logging.error(f'Erro ao criar pasta "{nome}": {e}')

    def criar_pastas_clientes_faltantes(self):
        verificador = Verificador(self.pastaClientes, self.baseClientes)
        clientes_faltantes = verificador.verificar_pastas_clientes()
        for cliente in clientes_faltantes:
            self.criar_pasta(cliente)

    def atualizar_base(self):
        verificador = Verificador(self.pastaClientes, self.baseClientes)
        pastas_nao_listadas = verificador.verificar_pastas_nao_listadas()
        if pastas_nao_listadas:
            df_atual = pd.read_excel(self.baseClientes)
            novos_dados = pd.DataFrame(list(pastas_nao_listadas), columns=['Alias'])
            df_novo = pd.concat([df_atual, novos_dados], ignore_index=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            novo_nome_base = self.baseClientes.parent / f"base_{timestamp}.xlsx"
            df_novo.to_excel(novo_nome_base, index=False)
            logging.info(f"Base de dados atualizada e salva como {novo_nome_base}")

