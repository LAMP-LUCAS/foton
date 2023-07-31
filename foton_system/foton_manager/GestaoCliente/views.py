from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from foton.forms import ClienteForm

'''
def index(request):
    # lógica para recuperar os clientes e renderizar o template
    return render(request, 'gestao_cluente/index.html')
'''

def index(request):
    clientes = Cliente.objects.all()
    return render(request, 'GestaoCliente/GestaoCliente_home.html', {'clientes': clientes})

def incluir(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('GestaoCliente:index')
    else:
        form = ClienteForm()
    return render(request, 'GestaoCliente/incluir.html', {'form': form})

def editar(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    if request.method == 'POST':
        # Atualiza os dados do objeto Cliente com os dados do formulário
        cliente.nome = request.POST['nome']
        cliente.email = request.POST['email']
        cliente.save()
        return redirect('GestaoCliente:index')
    return render(request, 'GestaoCliente/editar.html', {'cliente': cliente})

def excluir(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    if request.method == 'POST':
        # Exclui o objeto Cliente
        cliente.delete()
        return redirect('GestaoCliente:index')
    return render(request, 'GestaoCliente/excluir.html', {'cliente': cliente})

def detalhes(request, cliente_id):
    # Recupera o objeto Cliente com o ID especificado
    cliente = get_object_or_404(Cliente, id=cliente_id)
    # Renderiza o template 'GestaoCliente/detalhes.html' com o objeto Cliente
    return render(request, 'GestaoCliente/detalhes.html', {'cliente': cliente})
    