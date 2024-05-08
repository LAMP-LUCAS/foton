
from django.shortcuts import redirect, render,get_object_or_404
from foton.forms import ContratoForm
from GestaoContrato.models import Contrato
from fotonUser.models import Usuario


def lista_contratos():
    # Filtrar contratos apenas para a organização do usuário logado
    contratosOrg = Contrato.objects.filter(organizacao=Usuario.organizacao)
    return contratosOrg

def index(request):
    
    return render(request, 'GestaoContrato/GestaoContrato_home.html', {'contratos': lista_contratos()})

def detalhes(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    return render(request, 'GestaoContrato/detalhes.html', {'contrato': contrato})

def excluir(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    return render(request, 'GestaoContrato/excluir.html', {'contrato': contrato})

def editar(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    return render(request, 'GestaoContrato/editar.html', {'contrato': contrato})

def incluir(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('GestaoContrato:index')
    else:
        form = ContratoForm()
    return render(request, 'GestaoContrato/incluir.html', {'form': form})

# outras views do microsserviço de contrato...
