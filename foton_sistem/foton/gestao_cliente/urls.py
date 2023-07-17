from django.urls import path
from gestao_cliente import views

app_name = 'gestao_cliente'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:cliente_id>/', views.detalhes, name='detalhes'),
    path('<int:cliente_id>/editar/', views.editar, name='editar'),
    path('<int:cliente_id>/excluir/', views.excluir, name='excluir'),
    # outras rotas do aplicativo gestao_cliente...
]
