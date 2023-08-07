
def adicionar_objeto(objetos_dict, nome, largura, altura, profundidade, peso, materiais, funcoes, mob_armazenar, mob_utilizar):
    objetos_dict[nome] = {
        'largura': largura,
        'altura': altura,
        'profundidade': profundidade,
        'peso': peso,
        'material': materiais,
        'funcao': funcoes,
        'mobArmazenar': mob_armazenar,
        'mobUtilizar': mob_utilizar,
    }
    print(f"Objeto '{nome}' adicionado ao dicionário.")

def coletar_informacoes_objeto(objetos_dict, nome):
    if nome in objetos_dict:
        objeto = objetos_dict[nome]
        print(f"Características do objeto '{nome}':")
        print(f"Largura: {objeto['largura']}mm")
        print(f"Altura: {objeto['altura']}mm")
        print(f"Profundidade: {objeto['profundidade']}mm")
        print(f"Peso: {objeto['peso']}kg")
        print(f"Materiais: {', '.join(objeto['material'])}")
        print(f"Funções: {', '.join(objeto['funcao'])}")
        print(f"Mobiliários onde pode-se armazenar: {', '.join(objeto['mobArmazenar'])}")
        print(f"Mobiliários onde pode-se utilizar: {', '.join(objeto['mobUtilizar'])}")
    else:
        print(f"O objeto '{nome}' não foi encontrado no dicionário.")

#dicionário de objetos de uma casa

objetos={
    'prato': {
        'largura':200, #largura em milímetros
        'altura':20, #altura em milímetros
        'profundidade': 200, #profundidade em milímetros
        'peso':0.030, #peso em kilograma
        'material':['vidro','plastico','porcelana','pedra'], #funcoes que este objeto tem
        'funcao':['comer'], #funcoes que este objeto tem
        'mobArmazenar':['cristaleira','armario',], #mobiliários onde pode-se armazenar,expor
        'mobUtilizar':['cristaleira','armario',], #mobiliários onde pode-se utilizar este objeto
        },
#insira os objetos aqui
    
}

# dicionário de ambientes de uma casa

# Adicionando objetos ao dicionário

adicionar_objeto(objetos, 'sofa', 1500, 800, 800, 40, ['tecido', 'couro'], ['sentar', 'descansar'],
                 ['sala', 'quarto'], ['sala'])

# Coletando informações sobre um objeto específico
coletar_informacoes_objeto(objetos, 'prato')
coletar_informacoes_objeto(objetos, 'cadeira')  # Objeto inexistente para testar a mensagem de não encontrado
