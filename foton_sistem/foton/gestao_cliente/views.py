from django.shortcuts import render

def index(request):
    # lógica para recuperar os cliente e renderizar o template
    return render(request, 'gestao_cliente/index.html')

# outras views do microsserviço de contrato...
