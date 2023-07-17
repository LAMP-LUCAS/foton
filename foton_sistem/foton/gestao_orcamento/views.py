from django.shortcuts import render

def index(request):
    # lógica para recuperar os orcamento e renderizar o template
    return render(request, 'gestao_orcamento/index.html')

# outras views do microsserviço de corcamento...
