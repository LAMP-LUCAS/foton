from django import forms
from GestaoContrato.models import Contrato
from GestaoOrcamento.models import Orcamento
from GestaoCliente.models import Cliente


class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['titulo', 'data','numero','cliente','orcamento']

class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = ['descricao', 'valor', 'contrato']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email']