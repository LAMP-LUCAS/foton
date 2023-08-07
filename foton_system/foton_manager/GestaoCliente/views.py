from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from foton.forms import ClientePessoaFisicaForm, ClientePessoaJuridicaForm

def index(request):
    clientes = Cliente.objects.all()
    return render(request, 'GestaoCliente/GestaoCliente_home.html', {'clientes': clientes})

def incluir(request):
    if request.method == 'POST':
        if request.POST['tipo_pessoa'] == 'PF':
            form = ClientePessoaFisicaForm(request.POST)
        else:
            form = ClientePessoaJuridicaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('GestaoCliente:index')
    else:
        form = ClientePessoaFisicaForm()
    return render(request, 'GestaoCliente/incluir.html', {'form': form})

def editar(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    if request.method == 'POST':
        if request.POST['tipo_pessoa'] == 'PF':
            form = ClientePessoaFisicaForm(request.POST, instance=cliente)
        else:
            form = ClientePessoaJuridicaForm(request.POST, instance=cliente)

        if form.is_valid():
            form.save()
            return redirect('GestaoCliente:index')
    else:
        if cliente.tipo_pessoa == 'PF':
            form = ClientePessoaFisicaForm(instance=cliente)
        else:
            form = ClientePessoaJuridicaForm(instance=cliente)

    return render(request, 'GestaoCliente/editar.html', {'form': form, 'cliente': cliente})

def excluir(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('GestaoCliente:index')

    return render(request, 'GestaoCliente/excluir.html', {'cliente': cliente})

def detalhes(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'GestaoCliente/detalhes.html', {'cliente': cliente})
