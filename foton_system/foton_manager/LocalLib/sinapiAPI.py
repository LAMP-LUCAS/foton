# foton_system\foton_manager\LocalLib\sinapiAPI.py
import pandas as pd

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


# Teste da funcionalidade da biblioteca
if __name__ == "__main__":
    caminho = f'C:/Users/Lucas/OneDrive/LAMP ARQUITETURA/foton/foton_system/foton_manager/bd/SINAPI/SINAPI_Custo_Ref_Composicoes_Analitico_GO_202306_NaoDesonerado.xls'
    sinapi_api = SinapiAPI(base_path=caminho)
    
    code = '97141'  # Substitua pelo código da composição que deseja consultar
    cost = sinapi_api.get_cost_by_code(code)
    cost = cost[0].replace(',', '.')
    cost = float(cost)
    if cost is not None:
        print(f"Custo da composição de código {code}: R$ {cost:.2f}")
    else:
        print(f"Composição de código {code} não encontrada.")
