from django.shortcuts import render, redirect
from .models import Cliente

def index(request):
    clientes = Cliente.objects.all()  # substitua "Clientes" pelo nome do seu modelo de cliente
    return render(request, 'gestao_cliente/index.html', {'clientes': clientes})

def detalhes(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)  # substitua "Clientes" pelo nome do seu modelo de cliente
    return render(request, 'gestao_cliente/detalhes.html', {'cliente': cliente})

def editar(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)  # substitua "Clientes" pelo nome do seu modelo de cliente
    if request.method == 'POST':
        # lógica para salvar as alterações do cliente
        return redirect('gestao_cliente:index')
    return render(request, 'gestao_cliente/editar.html', {'cliente': cliente})

def excluir(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)  # substitua "Clientes" pelo nome do seu modelo de cliente
    if request.method == 'POST':
        # lógica para excluir o cliente
        return redirect('gestao_cliente:index')
    return render(request, 'gestao_cliente/excluir.html', {'cliente': cliente})
