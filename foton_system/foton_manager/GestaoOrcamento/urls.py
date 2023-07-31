from django.urls import path
from . import views

app_name = 'GestaoOrcamento'

urlpatterns = [
    path('', views.index, name='GestaoOrcamento_home'),
    path('incluir/', views.incluir, name='incluir'),
    path('<int:orcamento_id>/detalhes/', views.detalhes, name='detalhes'),
    path('<int:orcamento_id>/editar/', views.editar, name='editar'),
    path('<int:orcamento_id>/excluir/', views.excluir, name='excluir'),
]
