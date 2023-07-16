from django.shortcuts import render

from .models import Orcamento

def orcamento_list(request):
    orcamentos = Orcamento.objects.all()
    return render(request, 'orcamentos/orcamento_list.html', {'orcamentos': orcamentos})
