# foton_system\foton_manager\LocalLib\sinapiAPI.py
import pandas as pd

caminho = f'C:/Users/Lucas/OneDrive/LAMP ARQUITETURA/foton/foton_system/foton_manager/bd/SINAPI/SINAPI_Custo_Ref_Composicoes_Analitico_GO_202306_NaoDesonerado.xls'
self.data = pd.read_excel(caminho, sheet_name='Rel. Analítico')
print(self.data[:5])
# Define o índice de coluna como a quinta linha do DataFrame
self.data.columns = self.data.iloc[4]
# Remove a quinta linha
self.data = self.data.iloc[5:]