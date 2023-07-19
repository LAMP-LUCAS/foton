from django.urls import path
from GestaoCliente import views

app_name = 'GestaoCliente'

urlpatterns = [
    path('', views.index, name='index'),

#    path('<int:cliente_id>/detalhes/', views.detalhes, name='detalhes'),
#    path('<int:cliente_id>/incluir/', views.incluir, name='incluir'),
#    path('<int:cliente_id>/editar/', views.editar, name='editar'),
#    path('<int:cliente_id>/excluir/', views.excluir, name='excluir'),

    # outras rotas do aplicativo gestao_cliente...
]
