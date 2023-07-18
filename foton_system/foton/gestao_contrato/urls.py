from django.urls import path
from . import views

app_name = 'gestao_contrato'

urlpatterns = [
    path('', views.index, name='home_contrato'),
    path('detalhes/<int:contrato_id>/', views.detalhes, name='detalhes'),
    path('excluir/<int:contrato_id>/', views.excluir, name='excluir'),
<<<<<<< HEAD
    path('incluir/<int:contrato_id>/', views.incluir, name='incluir'),
    # outras rotas do microsserviço de contrato...
=======
    path('editar/<int:contrato_id>/', views.editar, name='editar'),
    path('incluir/', views.incluir, name='incluir'),
    # outras URLs do microsserviço de contrato...
>>>>>>> master
]
