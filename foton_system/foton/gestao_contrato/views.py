from django.shortcuts import render,get_object_or_404

def index(request):
    # lógica para recuperar os contratos e renderizar o template
    return render(request, 'gestao_contrato/home_contrato.html')

def detalhes(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    return render(request, 'gestao_contrato/detalhes_contrato.html', {'contrato': contrato})

def excluir(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    return render(request, 'gestao_contrato/excluir_contrato.html', {'contrato': contrato})

def editar(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    return render(request, 'gestao_contrato/editar_contrato.html', {'contrato': contrato})

def incluir(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    return render(request, 'gestao_contrato/incluir_contrato.html', {'contrato': contrato})

# outras views do microsserviço de contrato...
