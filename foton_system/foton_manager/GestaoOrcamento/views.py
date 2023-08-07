from django.shortcuts import render, get_object_or_404, redirect
from .models import Orcamento
from foton.forms import OrcamentoForm
from rest_framework import viewsets
from .models import ComposicaoCusto
from .serializers import ComposicaoCustoSerializer
from django.http import JsonResponse

def index(request):
    orcamentos = Orcamento.objects.all()
    return render(request, 'GestaoOrcamento/GestaoOrcamento_home.html', {'orcamentos': orcamentos})

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
    return render(request, 'GestaoOrcamento/composicao_modal.html', data)