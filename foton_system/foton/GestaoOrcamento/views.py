from django.shortcuts import render, get_object_or_404
from .models import Orcamento

def index(request):
    orcamentos = Orcamento.objects.all()
    return render(request, 'GestaoOrcamento_home.html', {'orcamentos': orcamentos})
'''
def detalhes(request, orcamento_id):
    orcamento = get_object_or_404(Orcamento, id=orcamento_id)
    return render(request, 'GestaoOrcamento/index.html', {'orcamento': orcamento})

'''