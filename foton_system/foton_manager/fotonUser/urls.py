from django.urls import path
from fotonUser import views

app_name = 'fotonUser'

urlpatterns = [
    path('', views.fotonUser_home, name='fotonUser_home'),

#    path('detalhes/<int:contrato_id>/', views.detalhes, name='detalhes'),
#    path('excluir/<int:contrato_id>/', views.excluir, name='excluir'),
#    path('editar/<int:contrato_id>/', views.editar, name='editar'),
#    path('incluir/', views.incluir, name='incluir'),

    # outras URLs do microsserviço de contrato...
]
