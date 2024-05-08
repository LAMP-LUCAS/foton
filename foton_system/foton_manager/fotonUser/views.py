from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from allauth.account.views import SignupView
from .models import Autorizacao
from fotonUser.models import Organizacao


@login_required
def fotonUser_home(request):
    users = User.objects.all()
    return render(request, 'fotonUser/fotonUser_home.html', {'fotonUsers': users})

@login_required
def fotonUser_incluir(request):
    if request.method == 'POST':
        # Lógica para criar um novo usuário
        # ...
        return redirect('fotonUser_home')
    else:
        return render(request, 'fotonUser/fotonUser_incluir.html')

@login_required
def fotonUser_editar(request, fotonUser_id):
    user = User.objects.get(id=fotonUser_id)
    if request.method == 'POST':
        # Lógica para editar o usuário
        # ...
        return redirect('fotonUser_home')
    else:
        return render(request, 'fotonUser/fotonUser_editar.html', {'fotonUser': fotonUser})

@login_required
def fotonUser_deletar(request, fotonUser_id):
    user = User.objects.get(id=fotonUser_id)
    if request.method == 'POST':
        # Lógica para excluir o usuário
        # ...
        return redirect('fotonUser_home')
    else:
        return render(request, 'fotonUser/fotonUser_deletar.html', {'fotonUser': fotonUser})

@login_required
def authorization_editar(request, fotonUser_id):
    user = User.objects.get(id=fotonUser_id)
    authorization, created = Autorizacao.objects.get_or_create(usuario=user)
    if request.method == 'POST':
        # Lógica para editar as autorizações do usuário
        # ...
        return redirect('fotonUser_home')
    else:
        return render(request, 'fotonUser/authorization_editar.html', {'user': user, 'authorization': authorization})

