from django import forms
from GestaoContrato.models import Contrato
from GestaoOrcamento.models import Orcamento

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['titulo', 'data','numero','cliente','orcamento']

class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = ['descricao', 'valor', 'contrato']