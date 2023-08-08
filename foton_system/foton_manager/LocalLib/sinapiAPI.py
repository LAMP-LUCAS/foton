# foton_system\foton_manager\LocalLib\sinapiAPI.py
import pandas as pd

class Composicao:
    def __init__(self, base_path):
        self.base_path = base_path
        self.data = pd.read_excel(self.base_path, sheet_name='Rel. Analítico')
        #Guardar o cabeçalho em uma variável para acessar depois
        cab = self.data.iloc[:5]
        # Define o índice de coluna como a quinta linha do DataFrame
        self.data.columns = self.data.iloc[4]
        # Remove a quinta linha
        self.data = self.data.iloc[5:]

    def get_Comp_resumo(self, codigo, descricao, unidade):
        self.codigo = codigo
        self.descricao = descricao
        self.unidade = unidade       


class SinapiAPI:
    def __init__(self, base_path):
        self.base_path = base_path
        self.data = pd.read_excel(self.base_path, sheet_name='Rel. Analítico')
        #Guardar o cabeçalho em uma variável para acessar depois
        cab = self.data.iloc[:5]
        # Define o índice de coluna como a quinta linha do DataFrame
        self.data.columns = self.data.iloc[4]
        # Remove a quinta linha
        self.data = self.data.iloc[5:]

    def get_cost_by_code(self, code):
        try:
            cost = self.data[self.data['CODIGO DA COMPOSICAO'] == code]['CUSTO TOTAL'].values[0]
            return cost
        except IndexError:
            return None


    def buscar_por_id(self, id_coluna, valor):
        try:
            composicoes = self.data[self.data[id_coluna] == valor]
            return composicoes
        except KeyError:
            return None
        

    def buscar_por_termo(self, termo_pesquisa):
        termo_pesquisa = termo_pesquisa.upper()

        # Define as colunas em que deseja realizar a pesquisa
        colunas_pesquisa = [
            'DESCRICAO DA CLASSE',
            'SIGLA DA CLASSE',
            'DESCRICAO DO TIPO 1',
            'SIGLA DO TIPO 1',
            'CODIGO DO AGRUPADOR',
            'DESCRICAO DO AGRUPADOR',
            'CODIGO DA COMPOSICAO',
            'DESCRICAO DA COMPOSICAO',
            'UNIDADE',
            'TIPO ITEM',
            'CODIGO ITEM',
            'DESCRIÇÃO ITEM',
            'UNIDADE ITEM'
        ]

        resultados = []

        for coluna in colunas_pesquisa:
            filtro = self.data[coluna].astype(str).str.contains(termo_pesquisa, case=False, na=False, regex=True)
            
            # Converte cada linha do DataFrame em um dicionário e adiciona à lista de resultados
            for _, row in self.data[filtro].iterrows():
                resultados.append(row.to_dict())

        if resultados:
            # Cria objetos Composicao a partir dos resultados da busca
            composicoes = []
            for resultado in resultados:
                composicao = self.get_Comp_resumo(
                    codigo=resultado['CODIGO DA COMPOSICAO'],
                    descricao=resultado['DESCRICAO DA COMPOSICAO'],
                    unidade=resultado['UNIDADE']
                )
                composicoes.append(composicao)
            
            return composicoes
        else:
            return None


    def get_Comp_resumo(self, codigo, descricao, unidade):
        self.codigo = codigo
        self.descricao = descricao
        self.unidade = unidade

        return {
        'codigo': codigo,
        'descricao': descricao,
        'unidade': unidade
        }