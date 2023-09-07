class HonorariosArquitetura:
    def __init__(self, custo_obra=None, tipo_servico=None, complexidade=None,allServ=None):
        self.custo_obra = custo_obra
        self.tipo_servico = tipo_servico
        self.complexidade = complexidade
        self.allServ = allServ
    def servicos(self):
        cadServ={
                "projArq":{
                    'alta':10,
                    'media':6,
                    'baixa':4,
                },
                'procMun':{
                    'alta':5,
                    'media':2,
                    'baixa':1,
                },
                'projEle':{
                    'alta':6,
                    'media':3,
                    'baixa':1,
                },
                'projHidSan':{
                    'alta':4,
                    'media':2,
                    'baixa':0.5,
                },
                'Cons':{
                    'alta':5,
                    'media':2,
                    'baixa':0.5,
                },       
            }
        
        if self.allServ is not None:
            return cadServ
        else:
            servico = self.tipo_servico
            complexidade = self.complexidade
            return cadServ[servico][complexidade]

    def percentual_sobre_custo_obra(self):
        serv = self.servicos()
        cplx = self.complexidade
        tipo = self.tipo_servico
        return serv/100*self.custo_obra
    

    def calculo_pelo_custo_servico(self, horas_trabalhadas, valor_hora):
        return horas_trabalhadas * valor_hora

def solicitar_informacoes_usuario():
    print('Bem-vindo ao sistema de cálculo de honorários de arquitetura!')
    print('Por favor, forneça as seguintes informações:')
    custo_obra = float(input('Qual é o custo estimado da obra? '))
    tipo_servico = input(f'Qual é o tipo de serviço prestado?\n [{HonorariosArquitetura(allServ=True).servicos().keys()}]\n')
    complexidade = input('Qual é a complexidade do projeto (alta, media ou baixa)? ')
    modalidade = input('Qual é a modalidade de remuneração desejada (percentual sobre o custo da obra[digite 1] ou cálculo pelo custo do serviço[digite 2])? ')
    if modalidade == '1':
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
