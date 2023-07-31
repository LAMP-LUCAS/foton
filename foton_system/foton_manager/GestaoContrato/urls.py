from django.urls import path
from GestaoContrato import views

app_name = 'GestaoContrato'

urlpatterns = [
    path('', views.index, name='GestaoContrato_home'),

    path('detalhes/<int:contrato_id>/', views.detalhes, name='detalhes'),
    path('excluir/<int:contrato_id>/', views.excluir, name='excluir'),
    path('editar/<int:contrato_id>/', views.editar, name='editar'),
    path('incluir/', views.incluir, name='incluir'),

    # outras URLs do microsserviço de contrato...
]
