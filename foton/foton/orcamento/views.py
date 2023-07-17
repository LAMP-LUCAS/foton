from django.shortcuts import render

from .models import Orcamento

def orcamento_list(request):
    orcamento = Orcamento.objects.all()
    return render(request, 'orcamento/orcamento_list.html', {'orcamento': orcamento})
