from django import forms
from GestaoContrato.models import Contrato
from GestaoOrcamento.models import Orcamento
from GestaoCliente.models import Cliente
from allauth.account.forms import LoginForm


class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['titulo', 'data','numero','cliente','orcamento']

class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = ['descricao', 'valor', 'contrato']

#class ClienteForm(forms.ModelForm):
 #   class Meta:
  #      model = Cliente
   #     fields = ['nome', 'email']

class ClientePessoaFisicaForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'tipo_pessoa',
            'nome_completo',
            'cpf',
            'rg',
            'sexo',
            'emprego_ocupacao',
            'numero_telefone',
            'email',
            'cep',
            'logradouro',
            'numero',
            'complemento',
            'cidade',
            'ug',
        ]

class ClientePessoaJuridicaForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'tipo_pessoa',
            'razao_social',
            'nome_fantasia',
            'cnpj',
            'telefone',
            'email',
            'natureza',
            'nome_representante',
            'cpf_representante',
            'telefone_representante',
        ]

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['remember'].label = 'Permanecer conectado'
        self.fields['remember'].initial = True