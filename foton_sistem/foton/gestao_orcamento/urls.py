from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # outras rotas do microsserviço de contrato...
]
