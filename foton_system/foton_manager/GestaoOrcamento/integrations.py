from LocalLib.sinapiAPI import SinapiAPI as sinapi  # Importe a classe SINAPI da biblioteca SINAPI que você desenvolveu

caminho_sinapi = f'C:\\Users\\Lucas\\OneDrive\\LAMP ARQUITETURA\\foton\\foton_system\\foton_manager\\bd\\SINAPI\\SINAPI_Custo_Ref_Composicoes_Analitico_GO_202306_NaoDesonerado.xls'

class SINAPIClient:

    def __init__(self):
        self.sinapi_instance = sinapi(caminho_sinapi)  # Instancie a classe SINAPI passando o caminho da base

    def get_cost_by_code(self, codigo):
        return self.sinapi_instance.get_cost_by_code(self, codigo)  # Use o método da biblioteca para obter o custo pelo código
    
    def buscar_composicoes(self, termo_pesquisa):
        composicoes = self.sinapi_instance.buscar_por_termo(termo_pesquisa)
        return composicoes
