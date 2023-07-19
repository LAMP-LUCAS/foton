
from django.shortcuts import render,get_object_or_404

def index(request):
    # lógica para recuperar os contratos e renderizar o template
    return render(request, 'GestaoContrato_home.html')
'''
def detalhes(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    return render(request, 'gestao_contrato/detalhes_contrato.html', {'contrato': contrato})

def excluir(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    return render(request, 'gestao_contrato/excluir_contrato.html', {'contrato': contrato})

def editar(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    return render(request, 'gestao_contrato/editar_contrato.html', {'contrato': contrato})

def incluir(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestao_contrato:index')
    else:
        form = ContratoForm()
    return render(request, 'gestao_contrato/incluir.html', {'form': form})
    '''
# outras views do microsserviço de contrato...
