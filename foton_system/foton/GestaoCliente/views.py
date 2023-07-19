from django.shortcuts import render, redirect
from .models import Cliente
from django.shortcuts import get_object_or_404

'''
def index(request):
    # lógica para recuperar os clientes e renderizar o template
    return render(request, 'gestao_cluente/index.html')
'''

def index(request):
    # Recupera todos os objetos Cliente do banco de dados
    clientes = Cliente.objects.all()
    # Renderiza o template 'GestaoCliente_home.html' com a lista de clientes
    return render(request, 'GestaoCliente_home.html', {'clientes': clientes})
'''
def incluir(request):
    if request.method == 'POST':
        # Cria um novo objeto Cliente com os dados do formulário
        cliente = Cliente.objects.create(
            nome=request.POST['nome'],
            email=request.POST['email']
        )
        return redirect('gestao_cliente:index')
    return render(request, 'gestao_cliente/criar.html')

def editar(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    if request.method == 'POST':
        # Atualiza os dados do objeto Cliente com os dados do formulário
        cliente.nome = request.POST['nome']
        cliente.email = request.POST['email']
        cliente.save()
        return redirect('gestao_cliente:index')
    return render(request, 'gestao_cliente/editar.html', {'cliente': cliente})

def excluir(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    if request.method == 'POST':
        # Exclui o objeto Cliente
        cliente.delete()
        return redirect('gestao_cliente:index')
    return render(request, 'gestao_cliente/excluir.html', {'cliente': cliente})

def detalhes(request, cliente_id):
    # Recupera o objeto Cliente com o ID especificado
    cliente = get_object_or_404(Cliente, id=cliente_id)
    # Renderiza o template 'gestao_cliente/detalhes.html' com o objeto Cliente
    return render(request, 'gestao_cliente/detalhes.html', {'cliente': cliente})
    '''