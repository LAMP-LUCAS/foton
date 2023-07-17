from django.shortcuts import render

def index(request):
    # lógica para recuperar os contratos e renderizar o template
    return render(request, 'gestao_contrato/index.html')

# outras views do microsserviço de contrato...
