from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import matplotlib.pyplot as plt


def homepage(request):
    return render(request, 'home.html')

'''
@login_required
def user_dashboard(request):
    # Lógica para recuperar dados (por exemplo, número de contratos, orçamentos, clientes)
    
    # Crie um gráfico de barras simples
    data = {'Contratos': 50, 'Orçamentos': 30, 'Clientes': 80}
    labels = data.keys()
    values = data.values()

    plt.figure(figsize=(8, 6))
    plt.bar(labels, values)
    plt.xlabel('Tipos de Dados')
    plt.ylabel('Quantidade')
    plt.title('Dados do Sistema')
    plt.savefig('fotonUser/static/fotonUser/graph.png')  # Salve o gráfico como uma imagem

    return render(request, 'fotonUser/fotonUser_home.html')'''