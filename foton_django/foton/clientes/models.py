from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14)
    # Outros campos relevantes para a aplicação

    def __str__(self):
        return self.nome
    
'''
CharField: Um campo de texto com tamanho limitado.
IntegerField: Um campo que armazena números inteiros.
ForeignKey: Um campo que estabelece uma relação de chave estrangeira com outra tabela. É usado para representar relacionamentos um-para-muitos ou muitos-para-muitos.
DateField ou DateTimeField: Campos para armazenar datas ou data e hora, respectivamente.
BooleanField: Um campo booleano que pode ter valores True ou False.
DecimalField: Um campo para armazenar números decimais com precisão fixa.
'''