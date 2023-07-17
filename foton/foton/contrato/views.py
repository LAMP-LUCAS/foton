from django.shortcuts import render

from .models import contrato

def contrato_list(request):
    contratos = contrato.objects.all()
    return render(request, 'contrato/contrato_list.html', {'contratos': contratos})
