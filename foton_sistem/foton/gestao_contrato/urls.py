from django.urls import path
from . import views

app_name = 'gestao_contrato'

urlpatterns = [
    path('', views.index, name='index'),
    path('detalhes/<int:contrato_id>/', views.detalhes, name='detalhes'),
    path('editar/<int:contrato_id>/', views.editar, name='editar'),
    path('excluir/<int:contrato_id>/', views.excluir, name='excluir'),
    # outras rotas do microsserviço de contrato...
]
