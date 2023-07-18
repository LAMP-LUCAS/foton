from django.shortcuts import render, get_object_or_404
from .models import Contrato
from .forms import ContratoForm


def index(request):
    # lógica para recuperar os contratos e renderizar o template
    contratos = Contrato.objects.all()
    return render(request, 'gestao_contrato/index.html', {'contratos': contratos})

def detalhes(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    return render(request, 'gestao_contrato/detalhes.html', {'contrato': contrato})

def excluir(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    return render(request, 'gestao_contrato/excluir.html', {'contrato': contrato})

def editar(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    return render(request, 'gestao_contrato/editar.html', {'contrato': contrato})

def incluir(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestao_contrato:index')
    else:
        form = ContratoForm()
    return render(request, 'gestao_contrato/incluir.html', {'form': form})
# outras views do microsserviço de contrato...
