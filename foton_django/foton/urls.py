"""
URL configuration for foton project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .contratos.views import contrato_list
from .clientes.views import cliente_list
from .orcamento.views import orcamento_list



urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    path('./foton/contratos/', contrato_list, name='contrato_list'),
]

urlpatterns = [
    path('./foton/clientes/', cliente_list, name='cliente_list'),
]

urlpatterns = [
    path('./foton/orcamento/', orcamento_list, name='orcamento_list'),
]