from django import forms
from .models import Contrato

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['titulo', 'data','numero','cliente','orcamento']
