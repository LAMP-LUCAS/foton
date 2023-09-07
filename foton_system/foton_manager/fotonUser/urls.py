from django.urls import path
from fotonUser import views

app_name = 'fotonUser'

urlpatterns = [
    path('', views.fotonUser_home, name='fotonUser_home'),
#    path('autorizar/', views.foton, name='fotonUser_autorizar'),
    path('excluir/', views.fotonUser_deletar, name='excluir'),
    path('editar/', views.fotonUser_editar, name='editar'),
    path('incluir/', views.fotonUser_incluir, name='incluir'),
    # outras URLs do microsserviço de contrato...
]
