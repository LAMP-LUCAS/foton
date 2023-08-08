from .integrations import SINAPIClient
from .models import ComposicaoCusto

class OrcamentacaoSINAPI:
    def __init__(self, orcamento):
        self.orcamento = orcamento
        self.sinapi_client = SINAPIClient()

    def criar_composicao_custo(self, codigo, quantidade):
        custo_sinapi = self.sinapi_client.get_cost_by_code(codigo)
        valor_total = custo_sinapi * quantidade

        composicao = ComposicaoCusto.objects.create(
            orcamento=self.orcamento,
            codigo=codigo,
            descricao=custo_sinapi.descricao,
            quantidade=quantidade,
            valor_unitario=custo_sinapi,
            valor_total=valor_total
        )
        return composicao

    def criar_orcamento_com_sinapi(self, composicoes):
        for codigo, quantidade in composicoes.items():
            self.criar_composicao_custo(codigo, quantidade)
