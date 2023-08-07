# foton_system\foton_manager\integrations.py
from LocalLib.sinapiAPI import SinapiAPI as sinapi # Importe a classe SINAPI da biblioteca SINAPI que você desenvolveu

class SINAPIClient:
    def __init__(self):
        self.sinapi = sinapi() # Instancie a classe SINAPI

    def get_cost_by_code(self, codigo):
        return self.sinapi.get_cost_by_code(codigo) # Use o método da biblioteca para obter o custo pelo código
