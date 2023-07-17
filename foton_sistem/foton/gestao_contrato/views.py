from django.shortcuts import render

def index(request):
    # lógica para recuperar os contratos e renderizar o template
    return render(request, 'gestao_contrato/index.html')

def detalhes(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    return render(request, 'gestao_contrato/detalhes.html', {'contrato': contrato})

def excluir(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    return render(request, 'gestao_contrato/excluir.html', {'contrato': contrato})

def editar(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    return render(request, 'gestao_contrato/editar.html', {'contrato': contrato})

# outras views do microsserviço de contrato...
