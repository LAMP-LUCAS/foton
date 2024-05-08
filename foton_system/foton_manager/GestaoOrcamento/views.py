from django.shortcuts import render, get_object_or_404, redirect
from .models import Orcamento, ComposicaoCusto
from foton.forms import OrcamentoForm
from rest_framework import viewsets
from .serializers import ComposicaoCustoSerializer
from django.http import JsonResponse
from GestaoOrcamento.integrations import SINAPIClient, sinapi
from fotonUser.models import Usuario

def lista_orcamentos():
    # Filtrar orcamentos apenas para a organização do usuário logado
    orcamentosOrg = Orcamento.objects.filter(organizacao=Usuario.organizacao)
    return orcamentosOrg

def index(request):
    orcamentos = Orcamento.objects.all()
    return render(request, 'GestaoOrcamento/GestaoOrcamento_home.html', {'orcamentos': lista_orcamentos()})

def detalhes(request, orcamento_id):
    orcamento = get_object_or_404(Orcamento, id=orcamento_id)
    return render(request, 'GestaoOrcamento/detalhes.html', {'orcamento': orcamento})

def incluir(request):
    if request.method == 'POST':
        form = OrcamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('GestaoOrcamento:GestaoOrcamento_home')
    else:
        form = OrcamentoForm()
    return render(request, 'GestaoOrcamento/incluir.html', {'form': form})

def editar(request, orcamento_id):
    orcamento = get_object_or_404(Orcamento, id=orcamento_id)
    if request.method == 'POST':
        form = OrcamentoForm(request.POST, instance=orcamento)
        if form.is_valid():
            form.save()
            return redirect('GestaoOrcamento:detalhes', orcamento_id=orcamento_id)
    else:
        form = OrcamentoForm(instance=orcamento)
    return render(request, 'GestaoOrcamento/editar.html', {'form': form, 'orcamento': orcamento})

def excluir(request, orcamento_id):
    orcamento = get_object_or_404(Orcamento, id=orcamento_id)
    if request.method == 'POST':
        orcamento.delete()
        return redirect('GestaoOrcamento:GestaoOrcamento_home')
    return render(request, 'GestaoOrcamento/excluir.html', {'orcamento': orcamento})

class ComposicaoCustoViewSet(viewsets.ModelViewSet):
    queryset = ComposicaoCusto.objects.all()
    serializer_class = ComposicaoCustoSerializer


def composicao_modal(request, composicao_id=None):
    # Lógica para buscar os dados da composição de custo com o ID fornecido (se houver)
    # Renderiza a tela em modal com os dados da composição
    data = {
        'composicao_id': composicao_id,
        # Outros dados da composição, se necessário
    }
    print('-------------- funcao composicao_modal() ----------------')
    print(data,'\n\n\n\n')
    print('------------------------------------')
    return render(request, 'GestaoOrcamento/composicao_modal.html', data)


def buscar_composicoes(request):
    print('\niniciando buscar_composicoes')
    base_dados = request.GET.get('base_dados',)# 'base_dados')
    termo_pesquisa = request.GET.get('termo_pesquisa',)# 'termo_pesquisa')
    if not termo_pesquisa:
        termo_pesquisa = 'ASSENTAMENTO'
    composicoes = []  # atribui um valor inicial à variável composicoes

    if base_dados == 'SINAPI':
        print('\nacessando o sinapi')
        sinapi_client = SINAPIClient()  # Instancie o SINAPIClient
        print('\nsinapi acessado com sucesso, Iniciando pesquisa do termo ', termo_pesquisa)
        composicoes = sinapi_client.buscar_composicoes(termo_pesquisa)  # Use o método do SINAPIClient
        
        # Exibe informações sobre o processo de busca
        '''
        print('-------------- funcao buscar_composicoes() -----------------')
        print(f'sinapi_client: {sinapi_client}')
        print('------------------------------------')
        print(f'Base de dados: {base_dados}')
        
        print('------------------------------------')
        print(f'Termo de pesquisa: {termo_pesquisa}')
        print('------------------------------------')
        
        print(f'Resultados da busca: {composicoes}')
        print('------------------------------------')
        '''
    print('\nA solicitação foi do tipo: ', type(request),'\n')
    if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        # A solicitação é uma solicitação AJAX
        # Retorne os dados em formato JSON
        print('\nenviando resposta json')
        #return JsonResponse(composicoes, safe=False)
        return render(request, 'GestaoOrcamento/buscar_composicoes.html', {'composicoes': composicoes})

    else:
        # A solicitação não é uma solicitação AJAX
        # Renderize o template normalmente
        print('\nenviando resposta html\n')
        return render(request, 'GestaoOrcamento/buscar_composicoes.html', {'composicoes': composicoes})


'''
def buscar_composicoes(request):
    base_dados = request.GET.get('base_dados')
    termo_pesquisa = request.GET.get('termo_pesquisa')
    if not termo_pesquisa:
        termo_pesquisa = 'ASSENTAMENTO'
    composicoes = []

    if base_dados == 'SINAPI':
        sinapi_client = SINAPIClient()
        composicoes = sinapi_client.buscar_composicoes(termo_pesquisa)

    if request.is_ajax():
        # A solicitação é uma solicitação AJAX
        # Retorne os dados em formato JSON
        return JsonResponse(composicoes, safe=False)
    else:
        # A solicitação não é uma solicitação AJAX
        # Renderize o template normalmente
        return render(request, 'GestaoOrcamento/buscar_composicoes.html', {'composicoes': composicoes})

'''
    
def get_cost_by_code(request, codigo):
    sinapi_client = SINAPIClient()  # Instancie o SINAPIClient
    custo = sinapi_client.get_cost_by_code(codigo)  # Use o método do SINAPIClient

    return render(request, 'GestaoOrcamento/custo_composicao.html', {'custo': custo})