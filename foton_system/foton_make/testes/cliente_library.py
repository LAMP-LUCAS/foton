import pandas as pd
from pathlib import Path
from datetime import datetime
import os

class BaseServidor:
    def __init__(self, caminho_pastaClientes, caminho_baseClientes):
        self.pastaClientes = Path(caminho_pastaClientes)
        self.baseClientes = Path(caminho_baseClientes)

class Verificador(BaseServidor):
    def base_existe(self):
        try:
            return self.baseClientes.exists()
        except Exception as e:
            print(f"Erro ao verificar existência da base: {e}")
            return False

    def pasta_clientes_existe(self):
        try:
            return self.pastaClientes.exists()
        except Exception as e:
            print(f"Erro ao verificar existência da pasta de clientes: {e}")
            return False

    def obter_aliases(self):
        try:
            df = pd.read_excel(self.baseClientes)
            return df['Alias'].tolist()
        except Exception as e:
            print(f"Erro ao ler base de clientes: {e}")
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
            print(f'Pasta "{nome}" criada com sucesso.')
        except Exception as e:
            print(f'Erro ao criar pasta "{nome}": {e}')

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
            print(f"Base de dados atualizada e salva como {novo_nome_base}")
