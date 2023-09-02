class HonorariosArquitetura:
    def __init__(self, custo_obra, tipo_servico, complexidade):
        self.custo_obra = custo_obra
        self.tipo_servico = tipo_servico
        self.complexidade = complexidade

    def percentual_sobre_custo_obra(self):
        if self.tipo_servico == 'projeto arquitetonico':
            if self.complexidade == 'alta':
                return self.custo_obra * 0.12
            elif self.complexidade == 'media':
                return self.custo_obra * 0.09
            else:
                return self.custo_obra * 0.06
        elif self.tipo_servico == 'projeto paisagistico':
            if self.complexidade == 'alta':
                return self.custo_obra * 0.15
            elif self.complexidade == 'media':
                return self.custo_obra * 0.12
            else:
                return self.custo_obra * 0.10
        # Adicione outras condições para outros tipos de serviços aqui

    def calculo_pelo_custo_servico(self, horas_trabalhadas, valor_hora):
        return horas_trabalhadas * valor_hora

def solicitar_informacoes_usuario():
    print('Bem-vindo ao sistema de cálculo de honorários de arquitetura!')
    print('Por favor, forneça as seguintes informações:')
    custo_obra = float(input('Qual é o custo estimado da obra? '))
    tipo_servico = input('Qual é o tipo de serviço prestado? ')
    complexidade = input('Qual é a complexidade do projeto (alta, media ou baixa)? ')
    modalidade = input('Qual é a modalidade de remuneração desejada (percentual sobre o custo da obra ou cálculo pelo custo do serviço)? ')
    if modalidade == 'percentual sobre o custo da obra':
        honorarios = HonorariosArquitetura(custo_obra, tipo_servico, complexidade)
        valor_orcamento = honorarios.percentual_sobre_custo_obra()
    else:
        horas_trabalhadas = float(input('Quantas horas foram trabalhadas? '))
        valor_hora = float(input('Qual é o valor da hora trabalhada? '))
        honorarios = HonorariosArquitetura(custo_obra, tipo_servico, complexidade)
        valor_orcamento = honorarios.calculo_pelo_custo_servico(horas_trabalhadas, valor_hora)
    print(f'O valor total do orçamento é de R$ {valor_orcamento:.2f}')

# Exemplo de uso
solicitar_informacoes_usuario()
