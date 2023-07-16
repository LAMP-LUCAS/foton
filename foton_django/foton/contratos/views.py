from django.shortcuts import render

from .models import Contrato

def contrato_list(request):
    contratos = Contrato.objects.all()
    return render(request, 'contratos/contrato_list.html', {'contratos': contratos})
