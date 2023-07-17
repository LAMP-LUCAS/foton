from django.shortcuts import render, get_object_or_404
from .models import Orcamento

def index(request):
    orcamentos = Orcamento.objects.all()
    return render(request, 'gestao_orcamento/index.html', {'orcamentos': orcamentos})

def detalhes(request, orcamento_id):
    orcamento = get_object_or_404(Orcamento, id=orcamento_id)
    return render(request, 'gestao_orcamento/detalhes.html', {'orcamento': orcamento})

def editar(request, orcamento_id):
    orcamento = get_object_or_404(Orcamento, id=orcamento_id)
    if request.method == 'POST':
        # Lógica para salvar as alterações no orçamento
        return redirect('gestao_orcamento:detalhes', orcamento_id=orcamento_id)
    return render(request, 'gestao_orcamento/editar.html', {'orcamento': orcamento})

def excluir(request, orcamento_id):
    orcamento = get_object_or_404(Orcamento, id=orcamento_id)
    if request.method == 'POST':
        # Lógica para excluir o orçamento
        return redirect('gestao_orcamento:index')
    return render(request, 'gestao_orcamento/excluir.html', {'orcamento': orcamento})
