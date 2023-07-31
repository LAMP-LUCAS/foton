from django.shortcuts import render, get_object_or_404, redirect
from .models import Orcamento
from foton.forms import OrcamentoForm

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
