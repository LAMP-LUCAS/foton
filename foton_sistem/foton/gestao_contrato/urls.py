from django.urls import path
from . import views

app_name = 'gestao_contrato'

urlpatterns = [
    path('', views.index, name='index'),
    # outras rotas do microsserviço de contrato...
]
