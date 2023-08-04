import json

def salvar_em_arquivo(dicionario, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dicionario, arquivo, indent=4, ensure_ascii=False)


# Lista de ambientes em uma casa

'''

perfeito, agora liste 10 objetos  podem estar em  um(a) 'lavanderia'. e faça o processo de inserção no dicionário objetos

'''

ambientes = [
    'sala',
    'cozinha',
    'quarto',
    'banheiro',
    'lavanderia',
    'escritorio',
    'varanda',
    'garagem',
    'jardim',
    'sótão',
    'sala de jantar',
    'sala de estar',
    'sala de TV',
    'closet',
    'área externa',
    'área de lazer',
    'sala de jogos',
    'salão de festas',
    'piscina',
    'academia',
    # Adicione outros ambientes relevantes
]

#objetos criados pela open ai:

objetos = {
    'prato': {
        'largura': 200,
        'altura': 20,
        'profundidade': 200,
        'peso': 0.030,
        'material': ['vidro', 'plastico', 'porcelana', 'pedra'],
        'funcao': ['comer'],
        'mobArmazenar': ['cristaleira', 'armario'],
        'mobUtilizar': ['cristaleira', 'armario'],
    },
    'sofa': {
        'largura': 1500,
        'altura': 800,
        'profundidade': 800,
        'peso': 40,
        'material': ['tecido', 'couro'],
        'funcao': ['sentar', 'descansar'],
        'mobArmazenar': ['sala', 'quarto'],
        'mobUtilizar': ['sala'],
    },
    'mesa de centro': {
        'largura': 800,
        'altura': 400,
        'profundidade': 800,
        'peso': 20,
        'material': ['madeira', 'vidro', 'metal'],
        'funcao': ['apoiar objetos'],
        'mobArmazenar': [],
        'mobUtilizar': ['sala'],
    },
    'estante': {
        'largura': 1000,
        'altura': 1800,
        'profundidade': 300,
        'peso': 50,
        'material': ['madeira', 'metal'],
        'funcao': ['organizar livros', 'expor objetos decorativos'],
        'mobArmazenar': ['sala'],
        'mobUtilizar': ['sala'],
    },
    'televisão': {
        'largura': 900,
        'altura': 500,
        'profundidade': 50,
        'peso': 15,
        'material': ['plastico', 'vidro'],
        'funcao': ['exibir conteúdo'],
        'mobArmazenar': ['rack', 'painel'],
        'mobUtilizar': ['sala'],
    },
    'tapete': {
        'largura': 2000,
        'altura': 1500,
        'profundidade': 10,
        'peso': 8,
        'material': ['tecido'],
        'funcao': ['forrar o chão'],
        'mobArmazenar': [],
        'mobUtilizar': ['sala'],
    },
    'poltrona': {
        'largura': 800,
        'altura': 1000,
        'profundidade': 800,
        'peso': 25,
        'material': ['tecido', 'couro'],
        'funcao': ['sentar', 'relaxar'],
        'mobArmazenar': ['sala'],
        'mobUtilizar': ['sala'],
    },
    'abajur': {
        'largura': 200,
        'altura': 400,
        'profundidade': 200,
        'peso': 2,
        'material': ['metal', 'plastico'],
        'funcao': ['iluminar'],
        'mobArmazenar': ['mesa de cabeceira', 'criado-mudo'],
        'mobUtilizar': ['sala', 'quarto'],
    },
    'prateleira': {
        'largura': 600,
        'altura': 200,
        'profundidade': 200,
        'peso': 5,
        'material': ['madeira', 'metal'],
        'funcao': ['organizar objetos'],
        'mobArmazenar': ['sala'],
        'mobUtilizar': ['sala'],
    },
    'mesa lateral': {
        'largura': 500,
        'altura': 600,
        'profundidade': 500,
        'peso': 10,
        'material': ['madeira', 'vidro', 'metal'],
        'funcao': ['apoiar objetos'],
        'mobArmazenar': ['sala', 'quarto'],
        'mobUtilizar': ['sala', 'quarto'],
    },
    'cortina': {
        'largura': 2000,
        'altura': 1500,
        'profundidade': 5,
        'peso': 1,
        'material': ['tecido'],
        'funcao': ['cobrir janelas'],
        'mobArmazenar': [],
        'mobUtilizar': ['sala'],
    },
}

# Verificando se os objetos foram inseridos corretamente
print("Objetos no dicionário:")
for objeto, detalhes in objetos.items():
    print(objeto)

# Lista de objetos que podem estar em uma 'cozinha'
objetos_cozinha = [
    'fogão',
    'geladeira',
    'pia',
    'armário',
    'mesa',
    'cadeira',
    'torradeira',
    'liquidificador',
    'microondas',
    'cafeteira',
]

# Inserindo os objetos no dicionário 'objetos'
objetos['fogão'] = {
    'largura': 600,
    'altura': 850,
    'profundidade': 600,
    'peso': 35,
    'material': ['metal', 'vidro'],
    'funcao': ['cozinhar'],
    'mobArmazenar': ['cozinha'],
    'mobUtilizar': ['cozinha'],
}

objetos['geladeira'] = {
    'largura': 700,
    'altura': 1700,
    'profundidade': 700,
    'peso': 80,
    'material': ['metal', 'plastico'],
    'funcao': ['refrigerar', 'armazenar alimentos'],
    'mobArmazenar': ['cozinha'],
    'mobUtilizar': ['cozinha'],
}

objetos['pia'] = {
    'largura': 1200,
    'altura': 850,
    'profundidade': 600,
    'peso': 40,
    'material': ['pedra', 'metal'],
    'funcao': ['lavar louças', 'preparar alimentos'],
    'mobArmazenar': ['cozinha'],
    'mobUtilizar': ['cozinha'],
}

objetos['armário'] = {
    'largura': 1000,
    'altura': 2000,
    'profundidade': 500,
    'peso': 60,
    'material': ['madeira', 'metal'],
    'funcao': ['armazenar utensílios', 'alimentos'],
    'mobArmazenar': ['cozinha'],
    'mobUtilizar': ['cozinha'],
}

objetos['mesa'] = {
    'largura': 800,
    'altura': 750,
    'profundidade': 800,
    'peso': 15,
    'material': ['madeira'],
    'funcao': ['preparar alimentos', 'apoiar objetos'],
    'mobArmazenar': ['cozinha'],
    'mobUtilizar': ['cozinha'],
}

objetos['cadeira'] = {
    'largura': 400,
    'altura': 900,
    'profundidade': 400,
    'peso': 5,
    'material': ['madeira', 'metal'],
    'funcao': ['sentar'],
    'mobArmazenar': ['cozinha'],
    'mobUtilizar': ['cozinha'],
}

objetos['torradeira'] = {
    'largura': 200,
    'altura': 200,
    'profundidade': 150,
    'peso': 2,
    'material': ['metal', 'plastico'],
    'funcao': ['tostar pães'],
    'mobArmazenar': ['cozinha'],
    'mobUtilizar': ['cozinha'],
}

objetos['liquidificador'] = {
    'largura': 150,
    'altura': 300,
    'profundidade': 150,
    'peso': 3,
    'material': ['plastico', 'vidro'],
    'funcao': ['preparar sucos', 'vitaminas'],
    'mobArmazenar': ['cozinha'],
    'mobUtilizar': ['cozinha'],
}

objetos['microondas'] = {
    'largura': 450,
    'altura': 300,
    'profundidade': 350,
    'peso': 15,
    'material': ['metal', 'plastico'],
    'funcao': ['aquecer alimentos'],
    'mobArmazenar': ['cozinha'],
    'mobUtilizar': ['cozinha'],
}

objetos['cafeteira'] = {
    'largura': 200,
    'altura': 300,
    'profundidade': 200,
    'peso': 2,
    'material': ['metal', 'plastico'],
    'funcao': ['preparar café'],
    'mobArmazenar': ['cozinha'],
    'mobUtilizar': ['cozinha'],
}

# Verificando se os objetos foram inseridos corretamente
print("Objetos no dicionário:")
for objeto, detalhes in objetos.items():
    print(objeto)

# Lista de objetos que podem estar em um 'quarto'
objetos_quarto = [
    'cama',
    'guarda-roupa',
    'criado-mudo',
    'escrivaninha',
    'cadeira de escritório',
    'espelho',
    'abajur',
    'prateleira',
    'sapateira',
    'tv',
]

# Inserindo os objetos no dicionário 'objetos'
objetos['cama'] = {
    'largura': 1600,
    'altura': 600,
    'profundidade': 2000,
    'peso': 50,
    'material': ['madeira', 'tecido'],
    'funcao': ['dormir'],
    'mobArmazenar': ['quarto'],
    'mobUtilizar': ['quarto'],
}

objetos['guarda-roupa'] = {
    'largura': 1200,
    'altura': 2000,
    'profundidade': 600,
    'peso': 80,
    'material': ['madeira', 'metal'],
    'funcao': ['armazenar roupas', 'objetos pessoais'],
    'mobArmazenar': ['quarto'],
    'mobUtilizar': ['quarto'],
}

objetos['criado-mudo'] = {
    'largura': 500,
    'altura': 600,
    'profundidade': 400,
    'peso': 10,
    'material': ['madeira', 'metal'],
    'funcao': ['apoio próximo à cama'],
    'mobArmazenar': ['quarto'],
    'mobUtilizar': ['quarto'],
}

objetos['escrivaninha'] = {
    'largura': 1000,
    'altura': 750,
    'profundidade': 500,
    'peso': 25,
    'material': ['madeira', 'metal'],
    'funcao': ['estudar', 'trabalhar'],
    'mobArmazenar': ['quarto'],
    'mobUtilizar': ['quarto'],
}

objetos['cadeira de escritório'] = {
    'largura': 600,
    'altura': 900,
    'profundidade': 600,
    'peso': 10,
    'material': ['metal', 'tecido'],
    'funcao': ['sentar'],
    'mobArmazenar': ['quarto'],
    'mobUtilizar': ['quarto'],
}

objetos['espelho'] = {
    'largura': 500,
    'altura': 1000,
    'profundidade': 50,
    'peso': 8,
    'material': ['vidro'],
    'funcao': ['refletir'],
    'mobArmazenar': ['quarto'],
    'mobUtilizar': ['quarto'],
}

objetos['abajur'] = {
    'largura': 200,
    'altura': 400,
    'profundidade': 200,
    'peso': 2,
    'material': ['metal', 'tecido'],
    'funcao': ['iluminar'],
    'mobArmazenar': ['criado-mudo', 'escrivaninha'],
    'mobUtilizar': ['quarto'],
}

objetos['prateleira'] = {
    'largura': 600,
    'altura': 200,
    'profundidade': 200,
    'peso': 5,
    'material': ['madeira', 'metal'],
    'funcao': ['organizar objetos'],
    'mobArmazenar': ['quarto'],
    'mobUtilizar': ['quarto'],
}

objetos['sapateira'] = {
    'largura': 800,
    'altura': 1200,
    'profundidade': 400,
    'peso': 30,
    'material': ['madeira'],
    'funcao': ['armazenar sapatos'],
    'mobArmazenar': ['quarto'],
    'mobUtilizar': ['quarto'],
}

objetos['tv'] = {
    'largura': 800,
    'altura': 500,
    'profundidade': 100,
    'peso': 10,
    'material': ['plastico', 'vidro'],
    'funcao': ['exibir conteúdo'],
    'mobArmazenar': ['escrivaninha'],
    'mobUtilizar': ['quarto'],
}

# Verificando se os objetos foram inseridos corretamente
print("Objetos no dicionário:")
for objeto, detalhes in objetos.items():
    print(objeto)

# Lista de objetos que podem estar em uma 'lavanderia'
objetos_lavanderia = [
    'máquina de lavar roupa',
    'secadora de roupa',
    'tábua de passar roupa',
    'varal',
    'cesto de roupas',
    'balde',
    'vassoura',
    'aspirador de pó',
    'ferro de passar roupa',
    'prateleira',
]

# Inserindo os objetos no dicionário 'objetos'
objetos['máquina de lavar roupa'] = {
    'largura': 600,
    'altura': 850,
    'profundidade': 600,
    'peso': 60,
    'material': ['metal', 'plastico'],
    'funcao': ['lavar roupas'],
    'mobArmazenar': ['lavanderia'],
    'mobUtilizar': ['lavanderia'],
}

objetos['secadora de roupa'] = {
    'largura': 600,
    'altura': 850,
    'profundidade': 600,
    'peso': 50,
    'material': ['metal', 'plastico'],
    'funcao': ['secar roupas'],
    'mobArmazenar': ['lavanderia'],
    'mobUtilizar': ['lavanderia'],
}

objetos['tábua de passar roupa'] = {
    'largura': 400,
    'altura': 800,
    'profundidade': 100,
    'peso': 5,
    'material': ['madeira', 'tecido'],
    'funcao': ['passar roupas'],
    'mobArmazenar': ['lavanderia'],
    'mobUtilizar': ['lavanderia'],
}

objetos['varal'] = {
    'largura': 1500,
    'altura': 1800,
    'profundidade': 100,
    'peso': 10,
    'material': ['metal'],
    'funcao': ['secar roupas'],
    'mobArmazenar': ['lavanderia'],
    'mobUtilizar': ['lavanderia'],
}

objetos['cesto de roupas'] = {
    'largura': 500,
    'altura': 600,
    'profundidade': 500,
    'peso': 2,
    'material': ['plastico', 'tecido'],
    'funcao': ['armazenar roupas sujas'],
    'mobArmazenar': ['lavanderia'],
    'mobUtilizar': ['lavanderia'],
}

objetos['balde'] = {
    'largura': 300,
    'altura': 250,
    'profundidade': 300,
    'peso': 1,
    'material': ['plastico'],
    'funcao': ['lavar roupas', 'armazenar água'],
    'mobArmazenar': ['lavanderia'],
    'mobUtilizar': ['lavanderia'],
}

objetos['vassoura'] = {
    'largura': 100,
    'altura': 1200,
    'profundidade': 100,
    'peso': 1,
    'material': ['madeira', 'cerdas'],
    'funcao': ['limpar o chão'],
    'mobArmazenar': ['lavanderia'],
    'mobUtilizar': ['lavanderia'],
}

objetos['aspirador de pó'] = {
    'largura': 300,
    'altura': 250,
    'profundidade': 300,
    'peso': 5,
    'material': ['plastico', 'metal'],
    'funcao': ['limpar o chão'],
    'mobArmazenar': ['lavanderia'],
    'mobUtilizar': ['lavanderia'],
}

objetos['ferro de passar roupa'] = {
    'largura': 100,
    'altura': 200,
    'profundidade': 150,
    'peso': 2,
    'material': ['metal', 'plastico'],
    'funcao': ['passar roupas'],
    'mobArmazenar': ['lavanderia'],
    'mobUtilizar': ['lavanderia'],
}

objetos['prateleira'] = {
    'largura': 600,
    'altura': 200,
    'profundidade': 200,
    'peso': 5,
    'material': ['madeira', 'metal'],
    'funcao': ['organizar objetos'],
    'mobArmazenar': ['lavanderia'],
    'mobUtilizar': ['lavanderia'],
}

# Verificando se os objetos foram inseridos corretamente
print("Objetos no dicionário:")
for objeto, detalhes in objetos.items():
    print(objeto)

# Lista de objetos que podem estar em um(a) 'escritório'
objetos_escritorio = [
    'mesa',
    'cadeira',
    'computador',
    'notebook',
    'impressora',
    'estante',
    'luminária',
    'quadro branco',
    'telefone',
    'gaveteiro',
]

# Inserindo os objetos no dicionário 'objetos'
objetos['mesa'] = {
    'largura': 1200,
    'altura': 750,
    'profundidade': 600,
    'peso': 30,
    'material': ['madeira', 'metal'],
    'funcao': ['trabalhar', 'estudar'],
    'mobArmazenar': ['escritorio'],
    'mobUtilizar': ['escritorio'],
}

objetos['cadeira'] = {
    'largura': 600,
    'altura': 900,
    'profundidade': 600,
    'peso': 10,
    'material': ['metal', 'tecido'],
    'funcao': ['sentar'],
    'mobArmazenar': ['escritorio'],
    'mobUtilizar': ['escritorio'],
}

objetos['computador'] = {
    'largura': 600,
    'altura': 500,
    'profundidade': 400,
    'peso': 10,
    'material': ['plastico', 'metal'],
    'funcao': ['computação', 'trabalho'],
    'mobArmazenar': ['escritorio'],
    'mobUtilizar': ['escritorio'],
}

objetos['notebook'] = {
    'largura': 350,
    'altura': 30,
    'profundidade': 250,
    'peso': 2,
    'material': ['plastico', 'metal'],
    'funcao': ['computação', 'trabalho'],
    'mobArmazenar': ['escritorio'],
    'mobUtilizar': ['escritorio'],
}

objetos['impressora'] = {
    'largura': 400,
    'altura': 200,
    'profundidade': 300,
    'peso': 8,
    'material': ['plastico', 'metal'],
    'funcao': ['imprimir documentos'],
    'mobArmazenar': ['estante', 'mesa'],
    'mobUtilizar': ['escritorio'],
}

objetos['estante'] = {
    'largura': 800,
    'altura': 1800,
    'profundidade': 400,
    'peso': 50,
    'material': ['madeira', 'metal'],
    'funcao': ['organizar livros', 'documentos'],
    'mobArmazenar': ['escritorio'],
    'mobUtilizar': ['escritorio'],
}

objetos['luminária'] = {
    'largura': 200,
    'altura': 400,
    'profundidade': 200,
    'peso': 2,
    'material': ['metal', 'plastico'],
    'funcao': ['iluminar'],
    'mobArmazenar': ['mesa'],
    'mobUtilizar': ['escritorio'],
}

objetos['quadro branco'] = {
    'largura': 800,
    'altura': 600,
    'profundidade': 50,
    'peso': 5,
    'material': ['plastico', 'metal'],
    'funcao': ['anotar', 'escrever'],
    'mobArmazenar': ['escritorio'],
    'mobUtilizar': ['escritorio'],
}

objetos['telefone'] = {
    'largura': 150,
    'altura': 200,
    'profundidade': 50,
    'peso': 1,
    'material': ['plastico', 'metal'],
    'funcao': ['comunicar'],
    'mobArmazenar': ['mesa'],
    'mobUtilizar': ['escritorio'],
}

objetos['gaveteiro'] = {
    'largura': 500,
    'altura': 600,
    'profundidade': 500,
    'peso': 15,
    'material': ['madeira', 'metal'],
    'funcao': ['organizar documentos', 'materiais de escritório'],
    'mobArmazenar': ['escritorio'],
    'mobUtilizar': ['escritorio'],
}

# Verificando se os objetos foram inseridos corretamente
print("Objetos no dicionário:")
for objeto, detalhes in objetos.items():
    print(objeto)

# Lista de objetos que podem estar em uma 'varanda'
objetos_varanda = [
    'mesa',
    'cadeira',
    'sofá',
    'poltrona',
    'rede',
    'vaso de planta',
    'churrasqueira',
    'espreguiçadeira',
    'guarda-sol',
    'abajur externo',
]

# Inserindo os objetos no dicionário 'objetos'
objetos['mesa'] = {
    'largura': 800,
    'altura': 750,
    'profundidade': 800,
    'peso': 20,
    'material': ['madeira', 'metal'],
    'funcao': ['apoio para refeições', 'apoio para objetos'],
    'mobArmazenar': ['varanda'],
    'mobUtilizar': ['varanda'],
}

objetos['cadeira'] = {
    'largura': 400,
    'altura': 900,
    'profundidade': 400,
    'peso': 5,
    'material': ['metal', 'tecido'],
    'funcao': ['sentar'],
    'mobArmazenar': ['varanda'],
    'mobUtilizar': ['varanda'],
}

objetos['sofá'] = {
    'largura': 1800,
    'altura': 800,
    'profundidade': 800,
    'peso': 40,
    'material': ['tecido', 'espuma'],
    'funcao': ['sentar', 'descansar'],
    'mobArmazenar': ['varanda'],
    'mobUtilizar': ['varanda'],
}

objetos['poltrona'] = {
    'largura': 800,
    'altura': 900,
    'profundidade': 800,
    'peso': 25,
    'material': ['tecido', 'espuma'],
    'funcao': ['sentar', 'relaxar'],
    'mobArmazenar': ['varanda'],
    'mobUtilizar': ['varanda'],
}

objetos['rede'] = {
    'largura': 1000,
    'altura': 1500,
    'profundidade': 0,
    'peso': 3,
    'material': ['tecido'],
    'funcao': ['descansar', 'relaxar'],
    'mobArmazenar': ['varanda'],
    'mobUtilizar': ['varanda'],
}

objetos['vaso de planta'] = {
    'largura': 300,
    'altura': 600,
    'profundidade': 300,
    'peso': 10,
    'material': ['cerâmica', 'terra'],
    'funcao': ['decorar', 'cultivar plantas'],
    'mobArmazenar': ['varanda'],
    'mobUtilizar': ['varanda'],
}

objetos['churrasqueira'] = {
    'largura': 800,
    'altura': 1500,
    'profundidade': 600,
    'peso': 60,
    'material': ['metal', 'tijolos refratários'],
    'funcao': ['preparar churrascos'],
    'mobArmazenar': ['varanda'],
    'mobUtilizar': ['varanda'],
}

objetos['espreguiçadeira'] = {
    'largura': 700,
    'altura': 800,
    'profundidade': 1800,
    'peso': 25,
    'material': ['tecido', 'metal'],
    'funcao': ['deitar', 'tomar sol'],
    'mobArmazenar': ['varanda'],
    'mobUtilizar': ['varanda'],
}

objetos['guarda-sol'] = {
    'largura': 2000,
    'altura': 2500,
    'profundidade': 2000,
    'peso': 15,
    'material': ['tecido', 'metal'],
    'funcao': ['proteger do sol'],
    'mobArmazenar': ['varanda'],
    'mobUtilizar': ['varanda'],
}

objetos['abajur externo'] = {
    'largura': 200,
    'altura': 400,
    'profundidade': 200,
    'peso': 2,
    'material': ['metal', 'tecido'],
    'funcao': ['iluminar'],
    'mobArmazenar': ['mesa'],
    'mobUtilizar': ['varanda'],
}

# Verificando se os objetos foram inseridos corretamente
print("Objetos no dicionário:")
for objeto, detalhes in objetos.items():
    print(objeto)

# Lista de objetos que podem estar em uma 'garagem'
objetos_garagem = [
    'carro',
    'bicicleta',
    'moto',
    'escada',
    'ferramentas',
    'caixa de ferramentas',
    'pneu sobressalente',
    'escova para lavar carros',
    'aspirador de pó automotivo',
    'bancada de trabalho',
]

# Inserindo os objetos no dicionário 'objetos'
objetos['carro'] = {
    'largura': 1800,
    'altura': 1500,
    'profundidade': 4500,
    'peso': 1000,
    'material': ['metal', 'vidro', 'plastico'],
    'funcao': ['transporte', 'mobilidade'],
    'mobArmazenar': ['garagem'],
    'mobUtilizar': ['garagem'],
}

objetos['bicicleta'] = {
    'largura': 600,
    'altura': 1000,
    'profundidade': 1800,
    'peso': 15,
    'material': ['metal'],
    'funcao': ['transporte', 'exercício'],
    'mobArmazenar': ['garagem'],
    'mobUtilizar': ['garagem'],
}

objetos['moto'] = {
    'largura': 800,
    'altura': 1100,
    'profundidade': 2000,
    'peso': 150,
    'material': ['metal'],
    'funcao': ['transporte', 'mobilidade'],
    'mobArmazenar': ['garagem'],
    'mobUtilizar': ['garagem'],
}

objetos['escada'] = {
    'largura': 500,
    'altura': 1800,
    'profundidade': 200,
    'peso': 10,
    'material': ['metal'],
    'funcao': ['alcançar lugares altos'],
    'mobArmazenar': ['garagem'],
    'mobUtilizar': ['garagem'],
}

objetos['ferramentas'] = {
    'largura': 500,
    'altura': 200,
    'profundidade': 300,
    'peso': 5,
    'material': ['metal'],
    'funcao': ['realizar reparos'],
    'mobArmazenar': ['garagem'],
    'mobUtilizar': ['garagem'],
}

objetos['caixa de ferramentas'] = {
    'largura': 400,
    'altura': 200,
    'profundidade': 200,
    'peso': 3,
    'material': ['metal', 'plastico'],
    'funcao': ['organizar ferramentas'],
    'mobArmazenar': ['garagem'],
    'mobUtilizar': ['garagem'],
}

objetos['pneu sobressalente'] = {
    'largura': 500,
    'altura': 500,
    'profundidade': 150,
    'peso': 15,
    'material': ['borracha', 'metal'],
    'funcao': ['substituir pneus danificados'],
    'mobArmazenar': ['garagem'],
    'mobUtilizar': ['garagem'],
}

objetos['escova para lavar carros'] = {
    'largura': 100,
    'altura': 400,
    'profundidade': 50,
    'peso': 1,
    'material': ['plastico', 'cerdas'],
    'funcao': ['limpar o carro'],
    'mobArmazenar': ['garagem'],
    'mobUtilizar': ['garagem'],
}

objetos['aspirador de pó automotivo'] = {
    'largura': 200,
    'altura': 300,
    'profundidade': 150,
    'peso': 2,
    'material': ['plastico', 'metal'],
    'funcao': ['limpar o carro'],
    'mobArmazenar': ['garagem'],
    'mobUtilizar': ['garagem'],
}

objetos['bancada de trabalho'] = {
    'largura': 1200,
    'altura': 900,
    'profundidade': 600,
    'peso': 50,
    'material': ['madeira', 'metal'],
    'funcao': ['realizar trabalhos manuais', 'reparos'],
    'mobArmazenar': ['garagem'],
    'mobUtilizar': ['garagem'],
}

# Verificando se os objetos foram inseridos corretamente
print("Objetos no dicionário:")
for objeto, detalhes in objetos.items():
    print(objeto)

# Lista de objetos que podem estar em um(a) 'jardim'
objetos_jardim = [
    'cadeira de jardim',
    'mesa de jardim',
    'guarda-sol',
    'churrasqueira portátil',
    'vaso de planta',
    'regador',
    'cortador de grama',
    'mangueira de jardim',
    'espreguiçadeira',
    'balanço de jardim',
]

# Inserindo os objetos no dicionário 'objetos'
objetos['cadeira de jardim'] = {
    'largura': 500,
    'altura': 800,
    'profundidade': 500,
    'peso': 5,
    'material': ['metal', 'tecido'],
    'funcao': ['sentar', 'relaxar'],
    'mobArmazenar': ['jardim'],
    'mobUtilizar': ['jardim'],
}

objetos['mesa de jardim'] = {
    'largura': 800,
    'altura': 750,
    'profundidade': 800,
    'peso': 15,
    'material': ['madeira', 'metal'],
    'funcao': ['apoio para refeições', 'apoio para objetos'],
    'mobArmazenar': ['jardim'],
    'mobUtilizar': ['jardim'],
}

objetos['guarda-sol'] = {
    'largura': 2000,
    'altura': 2500,
    'profundidade': 2000,
    'peso': 15,
    'material': ['tecido', 'metal'],
    'funcao': ['proteger do sol'],
    'mobArmazenar': ['jardim'],
    'mobUtilizar': ['jardim'],
}

objetos['churrasqueira portátil'] = {
    'largura': 600,
    'altura': 800,
    'profundidade': 600,
    'peso': 10,
    'material': ['metal'],
    'funcao': ['preparar churrascos'],
    'mobArmazenar': ['jardim'],
    'mobUtilizar': ['jardim'],
}

objetos['vaso de planta'] = {
    'largura': 300,
    'altura': 600,
    'profundidade': 300,
    'peso': 5,
    'material': ['cerâmica', 'terra'],
    'funcao': ['decorar', 'cultivar plantas'],
    'mobArmazenar': ['jardim'],
    'mobUtilizar': ['jardim'],
}

objetos['regador'] = {
    'largura': 200,
    'altura': 300,
    'profundidade': 100,
    'peso': 2,
    'material': ['metal', 'plastico'],
    'funcao': ['regar plantas'],
    'mobArmazenar': ['jardim'],
    'mobUtilizar': ['jardim'],
}

objetos['cortador de grama'] = {
    'largura': 400,
    'altura': 800,
    'profundidade': 400,
    'peso': 20,
    'material': ['metal', 'plastico'],
    'funcao': ['cortar a grama'],
    'mobArmazenar': ['jardim'],
    'mobUtilizar': ['jardim'],
}

objetos['mangueira de jardim'] = {
    'largura': 20,
    'altura': 1500,
    'profundidade': 20,
    'peso': 3,
    'material': ['plastico'],
    'funcao': ['regar plantas'],
    'mobArmazenar': ['jardim'],
    'mobUtilizar': ['jardim'],
}

objetos['espreguiçadeira'] = {
    'largura': 700,
    'altura': 800,
    'profundidade': 1800,
    'peso': 25,
    'material': ['tecido', 'metal'],
    'funcao': ['deitar', 'tomar sol'],
    'mobArmazenar': ['jardim'],
    'mobUtilizar': ['jardim'],
}

objetos['balanço de jardim'] = {
    'largura': 1000,
    'altura': 2000,
    'profundidade': 1000,
    'peso': 30,
    'material': ['metal', 'tecido'],
    'funcao': ['balançar', 'relaxar'],
    'mobArmazenar': ['jardim'],
    'mobUtilizar': ['jardim'],
}

# Verificando se os objetos foram inseridos corretamente
print("Objetos no dicionário:")
for objeto, detalhes in objetos.items():
    print(objeto)

# Lista de objetos que podem estar em um(a) 'sótão'
objetos_sotao = [
    'caixas de armazenamento',
    'malas de viagem',
    'prateleiras',
    'roupeiro antigo',
    'escada retrátil',
    'luminária de teto',
    'ventilador de teto',
    'cama dobrável',
    'aquecedor portátil',
    'cobertores e edredons',
]

# Inserindo os objetos no dicionário 'objetos'
objetos['caixas de armazenamento'] = {
    'largura': 300,
    'altura': 200,
    'profundidade': 400,
    'peso': 2,
    'material': ['plastico'],
    'funcao': ['armazenar objetos'],
    'mobArmazenar': ['sótão'],
    'mobUtilizar': ['sótão'],
}

objetos['malas de viagem'] = {
    'largura': 400,
    'altura': 250,
    'profundidade': 700,
    'peso': 3,
    'material': ['tecido', 'metal'],
    'funcao': ['armazenar roupas e pertences'],
    'mobArmazenar': ['sótão'],
    'mobUtilizar': ['sótão'],
}

objetos['prateleiras'] = {
    'largura': 800,
    'altura': 1800,
    'profundidade': 300,
    'peso': 10,
    'material': ['madeira', 'metal'],
    'funcao': ['organizar objetos'],
    'mobArmazenar': ['sótão'],
    'mobUtilizar': ['sótão'],
}

objetos['roupeiro antigo'] = {
    'largura': 1000,
    'altura': 1800,
    'profundidade': 500,
    'peso': 40,
    'material': ['madeira'],
    'funcao': ['armazenar roupas'],
    'mobArmazenar': ['sótão'],
    'mobUtilizar': ['sótão'],
}

objetos['escada retrátil'] = {
    'largura': 400,
    'altura': 2500,
    'profundidade': 50,
    'peso': 10,
    'material': ['metal'],
    'funcao': ['acesso ao sótão'],
    'mobArmazenar': ['sótão'],
    'mobUtilizar': ['sótão'],
}

objetos['luminária de teto'] = {
    'largura': 200,
    'altura': 300,
    'profundidade': 200,
    'peso': 2,
    'material': ['metal', 'plastico'],
    'funcao': ['iluminar'],
    'mobArmazenar': ['sótão'],
    'mobUtilizar': ['sótão'],
}

objetos['ventilador de teto'] = {
    'largura': 800,
    'altura': 500,
    'profundidade': 800,
    'peso': 5,
    'material': ['metal', 'plastico'],
    'funcao': ['ventilação'],
    'mobArmazenar': ['sótão'],
    'mobUtilizar': ['sótão'],
}

objetos['cama dobrável'] = {
    'largura': 800,
    'altura': 500,
    'profundidade': 1800,
    'peso': 15,
    'material': ['madeira', 'metal'],
    'funcao': ['dormir'],
    'mobArmazenar': ['sótão'],
    'mobUtilizar': ['sótão'],
}

objetos['aquecedor portátil'] = {
    'largura': 200,
    'altura': 300,
    'profundidade': 150,
    'peso': 3,
    'material': ['metal', 'plastico'],
    'funcao': ['aquecer o ambiente'],
    'mobArmazenar': ['sótão'],
    'mobUtilizar': ['sótão'],
}

objetos['cobertores e edredons'] = {
    'largura': 800,
    'altura': 400,
    'profundidade': 800,
    'peso': 5,
    'material': ['tecido'],
    'funcao': ['manter aquecido'],
    'mobArmazenar': ['sótão'],
    'mobUtilizar': ['sótão'],
}

# Verificando se os objetos foram inseridos corretamente
print("Objetos no dicionário:")
for objeto, detalhes in objetos.items():
    print(objeto)

# Lista de objetos que podem estar em uma 'sala de jantar'
objetos_sala_de_jantar = [
    'mesa de jantar',
    'cadeira de jantar',
    'buffet',
    'lustre',
    'tapete',
    'aparador',
    'guarda-louças',
    'pratos',
    'copos',
    'toalha de mesa',
]

# Inserindo os objetos no dicionário 'objetos'
objetos['mesa de jantar'] = {
    'largura': 1200,
    'altura': 750,
    'profundidade': 800,
    'peso': 40,
    'material': ['madeira'],
    'funcao': ['apoio para refeições'],
    'mobArmazenar': ['sala de jantar'],
    'mobUtilizar': ['sala de jantar'],
}

objetos['cadeira de jantar'] = {
    'largura': 400,
    'altura': 900,
    'profundidade': 400,
    'peso': 5,
    'material': ['madeira', 'tecido'],
    'funcao': ['sentar'],
    'mobArmazenar': ['sala de jantar'],
    'mobUtilizar': ['sala de jantar'],
}

objetos['buffet'] = {
    'largura': 1000,
    'altura': 900,
    'profundidade': 500,
    'peso': 30,
    'material': ['madeira'],
    'funcao': ['armazenar louças e talheres', 'apoio para refeições'],
    'mobArmazenar': ['sala de jantar'],
    'mobUtilizar': ['sala de jantar'],
}

objetos['lustre'] = {
    'largura': 500,
    'altura': 800,
    'profundidade': 500,
    'peso': 10,
    'material': ['metal', 'vidro'],
    'funcao': ['iluminar'],
    'mobArmazenar': ['teto'],
    'mobUtilizar': ['sala de jantar'],
}

objetos['tapete'] = {
    'largura': 1200,
    'altura': 10,
    'profundidade': 800,
    'peso': 5,
    'material': ['tecido'],
    'funcao': ['decorar o piso'],
    'mobArmazenar': ['sala de jantar'],
    'mobUtilizar': ['sala de jantar'],
}

objetos['aparador'] = {
    'largura': 1000,
    'altura': 800,
    'profundidade': 400,
    'peso': 20,
    'material': ['madeira'],
    'funcao': ['apoio para objetos', 'decoração'],
    'mobArmazenar': ['sala de jantar'],
    'mobUtilizar': ['sala de jantar'],
}

objetos['guarda-louças'] = {
    'largura': 800,
    'altura': 1800,
    'profundidade': 400,
    'peso': 40,
    'material': ['madeira'],
    'funcao': ['armazenar louças'],
    'mobArmazenar': ['sala de jantar'],
    'mobUtilizar': ['sala de jantar'],
}

objetos['pratos'] = {
    'largura': 200,
    'altura': 20,
    'profundidade': 200,
    'peso': 0.5,
    'material': ['porcelana'],
    'funcao': ['comer'],
    'mobArmazenar': ['guarda-louças', 'buffet'],
    'mobUtilizar': ['mesa de jantar'],
}

objetos['copos'] = {
    'largura': 100,
    'altura': 150,
    'profundidade': 100,
    'peso': 0.3,
    'material': ['vidro'],
    'funcao': ['beber'],
    'mobArmazenar': ['guarda-louças', 'buffet'],
    'mobUtilizar': ['mesa de jantar'],
}

objetos['toalha de mesa'] = {
    'largura': 1200,
    'altura': 10,
    'profundidade': 800,
    'peso': 0.5,
    'material': ['tecido'],
    'funcao': ['proteger e decorar a mesa'],
    'mobArmazenar': ['sala de jantar'],
    'mobUtilizar': ['mesa de jantar'],
}

# Verificando se os objetos foram inseridos corretamente
print("Objetos no dicionário:")
for objeto, detalhes in objetos.items():
    print(objeto)

# Lista de objetos que podem estar em uma 'sala de estar'
objetos_sala_de_estar = [
    'sofá',
    'poltrona',
    'mesa de centro',
    'estante',
    'televisão',
    'abajur',
    'tapete',
    'almofadas',
    'quadros decorativos',
    'cortinas',
]

# Inserindo os objetos no dicionário 'objetos'
objetos['sofá'] = {
    'largura': 2000,
    'altura': 800,
    'profundidade': 900,
    'peso': 50,
    'material': ['tecido', 'espuma', 'madeira'],
    'funcao': ['sentar', 'descansar'],
    'mobArmazenar': ['sala de estar'],
    'mobUtilizar': ['sala de estar'],
}

objetos['poltrona'] = {
    'largura': 800,
    'altura': 900,
    'profundidade': 800,
    'peso': 25,
    'material': ['tecido', 'espuma', 'madeira'],
    'funcao': ['sentar', 'relaxar'],
    'mobArmazenar': ['sala de estar'],
    'mobUtilizar': ['sala de estar'],
}

objetos['mesa de centro'] = {
    'largura': 800,
    'altura': 400,
    'profundidade': 800,
    'peso': 10,
    'material': ['madeira', 'vidro', 'metal'],
    'funcao': ['apoio para objetos'],
    'mobArmazenar': ['sala de estar'],
    'mobUtilizar': ['sala de estar'],
}

objetos['estante'] = {
    'largura': 1000,
    'altura': 1800,
    'profundidade': 400,
    'peso': 40,
    'material': ['madeira'],
    'funcao': ['armazenar livros e objetos decorativos'],
    'mobArmazenar': ['sala de estar'],
    'mobUtilizar': ['sala de estar'],
}

objetos['televisão'] = {
    'largura': 1200,
    'altura': 800,
    'profundidade': 100,
    'peso': 20,
    'material': ['plastico', 'metal'],
    'funcao': ['entretenimento'],
    'mobArmazenar': ['estante'],
    'mobUtilizar': ['sala de estar'],
}

objetos['abajur'] = {
    'largura': 200,
    'altura': 400,
    'profundidade': 200,
    'peso': 2,
    'material': ['metal', 'tecido'],
    'funcao': ['iluminar'],
    'mobArmazenar': ['mesa de centro'],
    'mobUtilizar': ['sala de estar'],
}

objetos['tapete'] = {
    'largura': 1500,
    'altura': 10,
    'profundidade': 900,
    'peso': 5,
    'material': ['tecido'],
    'funcao': ['decorar o piso'],
    'mobArmazenar': ['sala de estar'],
    'mobUtilizar': ['sala de estar'],
}

objetos['almofadas'] = {
    'largura': 400,
    'altura': 400,
    'profundidade': 100,
    'peso': 0.5,
    'material': ['tecido', 'espuma'],
    'funcao': ['apoio para sentar', 'decoração'],
    'mobArmazenar': ['sofá', 'poltrona'],
    'mobUtilizar': ['sala de estar'],
}

objetos['quadros decorativos'] = {
    'largura': 600,
    'altura': 600,
    'profundidade': 50,
    'peso': 2,
    'material': ['madeira', 'vidro'],
    'funcao': ['decorar as paredes'],
    'mobArmazenar': ['sala de estar'],
    'mobUtilizar': ['sala de estar'],
}

objetos['cortinas'] = {
    'largura': 1500,
    'altura': 2000,
    'profundidade': 0,
    'peso': 1,
    'material': ['tecido'],
    'funcao': ['proteger contra a luz externa'],
    'mobArmazenar': ['janela'],
    'mobUtilizar': ['sala de estar'],
}

# Verificando se os objetos foram inseridos corretamente
print("Objetos no dicionário:")
for objeto, detalhes in objetos.items():
    print(objeto)

# Lista de objetos que podem estar em uma 'sala de TV'
objetos_sala_de_tv = [
    'televisão',
    'sofá',
    'poltrona',
    'rack',
    'home theater',
    'tapete',
    'mesa de centro',
    'controle remoto',
    'caixas de som',
    'DVD player',
]

# Inserindo os objetos no dicionário 'objetos'
objetos['televisão'] = {
    'largura': 1200,
    'altura': 800,
    'profundidade': 100,
    'peso': 20,
    'material': ['plastico', 'metal'],
    'funcao': ['entretenimento'],
    'mobArmazenar': ['rack', 'home theater'],
    'mobUtilizar': ['sala de TV'],
}

objetos['sofá'] = {
    'largura': 2000,
    'altura': 800,
    'profundidade': 900,
    'peso': 50,
    'material': ['tecido', 'espuma', 'madeira'],
    'funcao': ['sentar', 'assistir TV'],
    'mobArmazenar': ['sala de TV'],
    'mobUtilizar': ['sala de TV'],
}

objetos['poltrona'] = {
    'largura': 800,
    'altura': 900,
    'profundidade': 800,
    'peso': 25,
    'material': ['tecido', 'espuma', 'madeira'],
    'funcao': ['sentar', 'relaxar', 'assistir TV'],
    'mobArmazenar': ['sala de TV'],
    'mobUtilizar': ['sala de TV'],
}

objetos['rack'] = {
    'largura': 1500,
    'altura': 600,
    'profundidade': 500,
    'peso': 30,
    'material': ['madeira', 'metal'],
    'funcao': ['apoio para a TV', 'armazenar equipamentos eletrônicos'],
    'mobArmazenar': ['sala de TV'],
    'mobUtilizar': ['sala de TV'],
}

objetos['home theater'] = {
    'largura': 800,
    'altura': 300,
    'profundidade': 400,
    'peso': 15,
    'material': ['plastico', 'metal'],
    'funcao': ['entretenimento', 'reprodução de áudio e vídeo'],
    'mobArmazenar': ['rack'],
    'mobUtilizar': ['sala de TV'],
}

objetos['tapete'] = {
    'largura': 2000,
    'altura': 10,
    'profundidade': 1200,
    'peso': 8,
    'material': ['tecido'],
    'funcao': ['decorar o piso', 'acústica'],
    'mobArmazenar': ['sala de TV'],
    'mobUtilizar': ['sala de TV'],
}

objetos['mesa de centro'] = {
    'largura': 800,
    'altura': 400,
    'profundidade': 800,
    'peso': 10,
    'material': ['madeira', 'vidro', 'metal'],
    'funcao': ['apoio para objetos', 'apoio para lanches'],
    'mobArmazenar': ['sala de TV'],
    'mobUtilizar': ['sala de TV'],
}

objetos['controle remoto'] = {
    'largura': 50,
    'altura': 150,
    'profundidade': 20,
    'peso': 0.1,
    'material': ['plastico'],
    'funcao': ['controlar a TV e o home theater'],
    'mobArmazenar': ['mesa de centro'],
    'mobUtilizar': ['sala de TV'],
}

objetos['caixas de som'] = {
    'largura': 150,
    'altura': 300,
    'profundidade': 150,
    'peso': 2,
    'material': ['madeira', 'metal'],
    'funcao': ['reprodução de áudio'],
    'mobArmazenar': ['rack', 'estante'],
    'mobUtilizar': ['sala de TV'],
}

objetos['DVD player'] = {
    'largura': 400,
    'altura': 50,
    'profundidade': 300,
    'peso': 1,
    'material': ['plastico', 'metal'],
    'funcao': ['reprodução de vídeos'],
    'mobArmazenar': ['rack', 'estante'],
    'mobUtilizar': ['sala de TV'],
}

# Verificando se os objetos foram inseridos corretamente
print("Objetos no dicionário:")
for objeto, detalhes in objetos.items():
    print(objeto)

# Lista de objetos que podem estar em um(a) 'closet'
objetos_closet = [
    'cabides',
    'araras',
    'gaveteiro',
    'espelho',
    'sapateira',
    'prateleiras',
    'puff',
    'caixas organizadoras',
    'cintos',
    'bolsas',
]

# Inserindo os objetos no dicionário 'objetos'
objetos['cabides'] = {
    'largura': 400,
    'altura': 200,
    'profundidade': 20,
    'peso': 0.2,
    'material': ['plastico', 'metal'],
    'funcao': ['suspender roupas'],
    'mobArmazenar': ['araras'],
    'mobUtilizar': ['closet'],
}

objetos['araras'] = {
    'largura': 800,
    'altura': 1500,
    'profundidade': 400,
    'peso': 10,
    'material': ['metal'],
    'funcao': ['pendurar roupas'],
    'mobArmazenar': ['closet'],
    'mobUtilizar': ['closet'],
}

objetos['gaveteiro'] = {
    'largura': 600,
    'altura': 800,
    'profundidade': 500,
    'peso': 15,
    'material': ['madeira'],
    'funcao': ['organizar roupas íntimas e acessórios'],
    'mobArmazenar': ['closet'],
    'mobUtilizar': ['closet'],
}

objetos['espelho'] = {
    'largura': 500,
    'altura': 1200,
    'profundidade': 20,
    'peso': 8,
    'material': ['vidro', 'madeira'],
    'funcao': ['refletir imagem'],
    'mobArmazenar': ['parede'],
    'mobUtilizar': ['closet'],
}

objetos['sapateira'] = {
    'largura': 800,
    'altura': 800,
    'profundidade': 400,
    'peso': 20,
    'material': ['madeira'],
    'funcao': ['organizar sapatos'],
    'mobArmazenar': ['closet'],
    'mobUtilizar': ['closet'],
}

objetos['prateleiras'] = {
    'largura': 600,
    'altura': 200,
    'profundidade': 300,
    'peso': 5,
    'material': ['madeira'],
    'funcao': ['organizar roupas e acessórios'],
    'mobArmazenar': ['closet'],
    'mobUtilizar': ['closet'],
}

objetos['puff'] = {
    'largura': 400,
    'altura': 400,
    'profundidade': 400,
    'peso': 5,
    'material': ['tecido', 'espuma'],
    'funcao': ['assento', 'apoio para os pés'],
    'mobArmazenar': ['closet'],
    'mobUtilizar': ['closet'],
}

objetos['caixas organizadoras'] = {
    'largura': 300,
    'altura': 200,
    'profundidade': 400,
    'peso': 1,
    'material': ['plastico', 'tecido'],
    'funcao': ['organizar acessórios e objetos menores'],
    'mobArmazenar': ['prateleiras'],
    'mobUtilizar': ['closet'],
}

objetos['cintos'] = {
    'largura': 50,
    'altura': 100,
    'profundidade': 10,
    'peso': 0.1,
    'material': ['tecido', 'metal'],
    'funcao': ['segurar calças e saias'],
    'mobArmazenar': ['cabides', 'gaveteiro'],
    'mobUtilizar': ['closet'],
}

objetos['bolsas'] = {
    'largura': 300,
    'altura': 250,
    'profundidade': 100,
    'peso': 0.5,
    'material': ['tecido', 'couro'],
    'funcao': ['armazenar objetos pessoais'],
    'mobArmazenar': ['prateleiras', 'gaveteiro'],
    'mobUtilizar': ['closet'],
}

# Verificando se os objetos foram inseridos corretamente
print("Objetos no dicionário:")
for objeto, detalhes in objetos.items():
    print(objeto)

# Lista de objetos que podem estar em uma 'área externa'
objetos_area_externa = [
    'mesa externa',
    'cadeira externa',
    'guarda-sol',
    'churrasqueira',
    'espreguiçadeira',
    'piscina',
    'jardim vertical',
    'rede',
    'balanço',
    'vaso de plantas',
]

# Inserindo os objetos no dicionário 'objetos'
objetos['mesa externa'] = {
    'largura': 800,
    'altura': 750,
    'profundidade': 800,
    'peso': 15,
    'material': ['madeira', 'metal'],
    'funcao': ['apoio para refeições'],
    'mobArmazenar': ['área externa'],
    'mobUtilizar': ['área externa'],
}

objetos['cadeira externa'] = {
    'largura': 500,
    'altura': 900,
    'profundidade': 500,
    'peso': 5,
    'material': ['plastico', 'metal'],
    'funcao': ['sentar'],
    'mobArmazenar': ['área externa'],
    'mobUtilizar': ['área externa'],
}

objetos['guarda-sol'] = {
    'largura': 2000,
    'altura': 2500,
    'profundidade': 2000,
    'peso': 8,
    'material': ['tecido', 'metal'],
    'funcao': ['proteger do sol'],
    'mobArmazenar': ['área externa'],
    'mobUtilizar': ['área externa'],
}

objetos['churrasqueira'] = {
    'largura': 1000,
    'altura': 1200,
    'profundidade': 800,
    'peso': 60,
    'material': ['metal'],
    'funcao': ['preparar alimentos'],
    'mobArmazenar': ['área externa'],
    'mobUtilizar': ['área externa'],
}

objetos['espreguiçadeira'] = {
    'largura': 600,
    'altura': 800,
    'profundidade': 1800,
    'peso': 12,
    'material': ['madeira', 'tecido'],
    'funcao': ['deitar e relaxar'],
    'mobArmazenar': ['área externa'],
    'mobUtilizar': ['área externa'],
}

objetos['piscina'] = {
    'largura': 4000,
    'altura': 1500,
    'profundidade': 2000,
    'peso': 0,  # A piscina não possui peso no dicionário.
    'material': ['fibra de vidro', 'azulejo'],
    'funcao': ['nadar', 'refrescar'],
    'mobArmazenar': ['área externa'],
    'mobUtilizar': ['área externa'],
}

objetos['jardim vertical'] = {
    'largura': 800,
    'altura': 1500,
    'profundidade': 150,
    'peso': 25,
    'material': ['metal', 'plantas'],
    'funcao': ['decorar com plantas verticais'],
    'mobArmazenar': ['parede'],
    'mobUtilizar': ['área externa'],
}

objetos['rede'] = {
    'largura': 1000,
    'altura': 200,
    'profundidade': 400,
    'peso': 1.5,
    'material': ['tecido'],
    'funcao': ['descansar'],
    'mobArmazenar': ['área externa'],
    'mobUtilizar': ['área externa'],
}

objetos['balanço'] = {
    'largura': 800,
    'altura': 2000,
    'profundidade': 800,
    'peso': 20,
    'material': ['madeira', 'corda'],
    'funcao': ['brincar'],
    'mobArmazenar': ['árvore'],
    'mobUtilizar': ['área externa'],
}

objetos['vaso de plantas'] = {
    'largura': 300,
    'altura': 400,
    'profundidade': 300,
    'peso': 2,
    'material': ['cerâmica'],
    'funcao': ['plantar e decorar com plantas'],
    'mobArmazenar': ['área externa'],
    'mobUtilizar': ['área externa'],
}

# Verificando se os objetos foram inseridos corretamente
print("Objetos no dicionário:")
for objeto, detalhes in objetos.items():
    print(objeto)

# Lista de objetos que podem estar em uma 'área de lazer'
objetos_area_de_lazer = [
    'mesa de jogos',
    'cadeira de balanço',
    'piscina',
    'churrasqueira',
    'redes',
    'mesa para refeições',
    'guarda-sol',
    'sofá externo',
    'mesa de centro',
    'caixa de som',
]

# Inserindo os objetos no dicionário 'objetos'
objetos['mesa de jogos'] = {
    'largura': 800,
    'altura': 750,
    'profundidade': 800,
    'peso': 15,
    'material': ['madeira', 'metal'],
    'funcao': ['jogos de tabuleiro', 'cartas'],
    'mobArmazenar': ['área de lazer'],
    'mobUtilizar': ['área de lazer'],
}

objetos['cadeira de balanço'] = {
    'largura': 600,
    'altura': 900,
    'profundidade': 800,
    'peso': 10,
    'material': ['madeira', 'corda'],
    'funcao': ['balançar e relaxar'],
    'mobArmazenar': ['área de lazer'],
    'mobUtilizar': ['área de lazer'],
}

objetos['piscina'] = {
    'largura': 4000,
    'altura': 1500,
    'profundidade': 2000,
    'peso': 0,
    'material': ['fibra de vidro', 'azulejo'],
    'funcao': ['nadar', 'refrescar'],
    'mobArmazenar': ['área de lazer'],
    'mobUtilizar': ['área de lazer'],
}

objetos['churrasqueira'] = {
    'largura': 1000,
    'altura': 1200,
    'profundidade': 800,
    'peso': 60,
    'material': ['metal'],
    'funcao': ['preparar alimentos'],
    'mobArmazenar': ['área de lazer'],
    'mobUtilizar': ['área de lazer'],
}

objetos['redes'] = {
    'largura': 1000,
    'altura': 200,
    'profundidade': 400,
    'peso': 1.5,
    'material': ['tecido'],
    'funcao': ['descansar'],
    'mobArmazenar': ['área de lazer'],
    'mobUtilizar': ['área de lazer'],
}

objetos['mesa para refeições'] = {
    'largura': 800,
    'altura': 750,
    'profundidade': 800,
    'peso': 15,
    'material': ['madeira', 'metal'],
    'funcao': ['apoio para refeições'],
    'mobArmazenar': ['área de lazer'],
    'mobUtilizar': ['área de lazer'],
}

objetos['guarda-sol'] = {
    'largura': 2000,
    'altura': 2500,
    'profundidade': 2000,
    'peso': 8,
    'material': ['tecido', 'metal'],
    'funcao': ['proteger do sol'],
    'mobArmazenar': ['área de lazer'],
    'mobUtilizar': ['área de lazer'],
}

objetos['sofá externo'] = {
    'largura': 1800,
    'altura': 800,
    'profundidade': 900,
    'peso': 40,
    'material': ['tecido', 'espuma', 'metal'],
    'funcao': ['sentar', 'relaxar'],
    'mobArmazenar': ['área de lazer'],
    'mobUtilizar': ['área de lazer'],
}

objetos['mesa de centro'] = {
    'largura': 800,
    'altura': 400,
    'profundidade': 800,
    'peso': 10,
    'material': ['madeira', 'vidro', 'metal'],
    'funcao': ['apoio para objetos'],
    'mobArmazenar': ['área de lazer'],
    'mobUtilizar': ['área de lazer'],
}

objetos['caixa de som'] = {
    'largura': 200,
    'altura': 300,
    'profundidade': 200,
    'peso': 2,
    'material': ['plastico', 'metal'],
    'funcao': ['reprodução de áudio'],
    'mobArmazenar': ['mesa de centro'],
    'mobUtilizar': ['área de lazer'],
}

# Verificando se os objetos foram inseridos corretamente
print("Objetos no dicionário:")
for objeto, detalhes in objetos.items():
    print(objeto)

# Lista de objetos que podem estar em uma 'sala de jogos'
objetos_sala_de_jogos = [
    'mesa de sinuca',
    'mesa de ping pong',
    'mesa de pebolim',
    'dardos',
    'jogos de tabuleiro',
    'videogame',
    'fliperama',
    'mesa para cartas',
    'poltrona reclinável',
    'estante para jogos',
]

# Inserindo os objetos no dicionário 'objetos'
objetos['mesa de sinuca'] = {
    'largura': 1000,
    'altura': 750,
    'profundidade': 2000,
    'peso': 100,
    'material': ['madeira', 'tecido', 'metal'],
    'funcao': ['jogo de sinuca'],
    'mobArmazenar': ['sala de jogos'],
    'mobUtilizar': ['sala de jogos'],
}

objetos['mesa de ping pong'] = {
    'largura': 1500,
    'altura': 750,
    'profundidade': 2500,
    'peso': 80,
    'material': ['madeira', 'metal'],
    'funcao': ['jogo de ping pong'],
    'mobArmazenar': ['sala de jogos'],
    'mobUtilizar': ['sala de jogos'],
}

objetos['mesa de pebolim'] = {
    'largura': 800,
    'altura': 800,
    'profundidade': 1500,
    'peso': 50,
    'material': ['madeira', 'plastico', 'metal'],
    'funcao': ['jogo de pebolim'],
    'mobArmazenar': ['sala de jogos'],
    'mobUtilizar': ['sala de jogos'],
}

objetos['dardos'] = {
    'largura': 50,
    'altura': 300,
    'profundidade': 50,
    'peso': 0.3,
    'material': ['metal', 'plumante'],
    'funcao': ['jogo de dardos'],
    'mobArmazenar': ['parede'],
    'mobUtilizar': ['sala de jogos'],
}

objetos['jogos de tabuleiro'] = {
    'largura': 400,
    'altura': 100,
    'profundidade': 400,
    'peso': 2,
    'material': ['papelão'],
    'funcao': ['jogos de tabuleiro'],
    'mobArmazenar': ['estante para jogos'],
    'mobUtilizar': ['sala de jogos'],
}

objetos['videogame'] = {
    'largura': 300,
    'altura': 80,
    'profundidade': 200,
    'peso': 2,
    'material': ['plastico', 'metal'],
    'funcao': ['jogar videogame'],
    'mobArmazenar': ['estante para jogos'],
    'mobUtilizar': ['sala de jogos'],
}

objetos['fliperama'] = {
    'largura': 600,
    'altura': 1800,
    'profundidade': 600,
    'peso': 100,
    'material': ['metal', 'vidro'],
    'funcao': ['jogar fliperama'],
    'mobArmazenar': ['sala de jogos'],
    'mobUtilizar': ['sala de jogos'],
}

objetos['mesa para cartas'] = {
    'largura': 800,
    'altura': 750,
    'profundidade': 800,
    'peso': 15,
    'material': ['madeira', 'metal'],
    'funcao': ['jogos de cartas'],
    'mobArmazenar': ['sala de jogos'],
    'mobUtilizar': ['sala de jogos'],
}

objetos['poltrona reclinável'] = {
    'largura': 800,
    'altura': 1000,
    'profundidade': 900,
    'peso': 40,
    'material': ['tecido', 'espuma', 'metal'],
    'funcao': ['sentar', 'relaxar'],
    'mobArmazenar': ['sala de jogos'],
    'mobUtilizar': ['sala de jogos'],
}

objetos['estante para jogos'] = {
    'largura': 800,
    'altura': 1800,
    'profundidade': 400,
    'peso': 30,
    'material': ['madeira', 'metal'],
    'funcao': ['organizar jogos e videogames'],
    'mobArmazenar': ['sala de jogos'],
    'mobUtilizar': ['sala de jogos'],
}

# Verificando se os objetos foram inseridos corretamente
print("Objetos no dicionário:")
for objeto, detalhes in objetos.items():
    print(objeto)

# Lista de objetos que podem estar em um(a) 'salão de festas'
objetos_salao_de_festas = [
    'mesa de buffet',
    'cadeira para eventos',
    'mesa para convidados',
    'palco',
    'iluminação cênica',
    'pista de dança',
    'sistema de som',
    'projetor',
    'telão',
    'decoração temática',
]

# Inserindo os objetos no dicionário 'objetos'
objetos['mesa de buffet'] = {
    'largura': 1000,
    'altura': 750,
    'profundidade': 800,
    'peso': 30,
    'material': ['madeira', 'metal'],
    'funcao': ['apoio para alimentos e bebidas'],
    'mobArmazenar': ['salão de festas'],
    'mobUtilizar': ['salão de festas'],
}

objetos['cadeira para eventos'] = {
    'largura': 500,
    'altura': 900,
    'profundidade': 500,
    'peso': 5,
    'material': ['plastico', 'metal'],
    'funcao': ['assento para convidados'],
    'mobArmazenar': ['salão de festas'],
    'mobUtilizar': ['salão de festas'],
}

objetos['mesa para convidados'] = {
    'largura': 800,
    'altura': 750,
    'profundidade': 800,
    'peso': 15,
    'material': ['madeira', 'metal'],
    'funcao': ['apoio para convidados'],
    'mobArmazenar': ['salão de festas'],
    'mobUtilizar': ['salão de festas'],
}

objetos['palco'] = {
    'largura': 3000,
    'altura': 600,
    'profundidade': 2000,
    'peso': 150,
    'material': ['madeira', 'tecido', 'metal'],
    'funcao': ['elevado para apresentações'],
    'mobArmazenar': ['salão de festas'],
    'mobUtilizar': ['salão de festas'],
}

objetos['iluminação cênica'] = {
    'largura': 200,
    'altura': 200,
    'profundidade': 100,
    'peso': 2,
    'material': ['metal', 'vidro'],
    'funcao': ['criar efeitos de luz'],
    'mobArmazenar': ['salão de festas'],
    'mobUtilizar': ['salão de festas'],
}

objetos['pista de dança'] = {
    'largura': 4000,
    'altura': 1,  # A pista de dança não possui altura no dicionário.
    'profundidade': 2000,
    'peso': 0,  # A pista de dança não possui peso no dicionário.
    'material': ['madeira', 'plastico'],
    'funcao': ['espaço para dançar'],
    'mobArmazenar': ['salão de festas'],
    'mobUtilizar': ['salão de festas'],
}

objetos['sistema de som'] = {
    'largura': 300,
    'altura': 400,
    'profundidade': 200,
    'peso': 10,
    'material': ['metal', 'plastico'],
    'funcao': ['reprodução de áudio'],
    'mobArmazenar': ['palco'],
    'mobUtilizar': ['salão de festas'],
}

objetos['projetor'] = {
    'largura': 200,
    'altura': 300,
    'profundidade': 200,
    'peso': 5,
    'material': ['metal', 'plastico'],
    'funcao': ['projeção de imagens'],
    'mobArmazenar': ['mesa de buffet'],
    'mobUtilizar': ['salão de festas'],
}

objetos['telão'] = {
    'largura': 2000,
    'altura': 1500,
    'profundidade': 200,
    'peso': 8,
    'material': ['tecido', 'metal'],
    'funcao': ['exibição de imagens e vídeos'],
    'mobArmazenar': ['mesa de buffet'],
    'mobUtilizar': ['salão de festas'],
}

objetos['decoração temática'] = {
    'largura': 1,  # A decoração não possui largura no dicionário.
    'altura': 1,  # A decoração não possui altura no dicionário.
    'profundidade': 1,  # A decoração não possui profundidade no dicionário.
    'peso': 0,  # A decoração não possui peso no dicionário.
    'material': ['diversos'],
    'funcao': ['tematizar o ambiente'],
    'mobArmazenar': ['salão de festas'],
    'mobUtilizar': ['salão de festas'],
}

# Verificando se os objetos foram inseridos corretamente
print("Objetos no dicionário:")
for objeto, detalhes in objetos.items():
    print(objeto)

# Lista de objetos que podem estar em uma 'área de piscina'
objetos_area_de_piscina = [
    'espreguiçadeira',
    'guarda-sol',
    'toalha de praia',
    'cooler',
    'boia inflável',
    'cadeira reclinável',
    'mesa lateral',
    'chuveiro externo',
    'caixa de som resistente à água',
    'mesa para petiscos',
]

# Inserindo os objetos no dicionário 'objetos'
objetos['espreguiçadeira'] = {
    'largura': 600,
    'altura': 800,
    'profundidade': 1800,
    'peso': 12,
    'material': ['madeira', 'tecido'],
    'funcao': ['deitar e relaxar'],
    'mobArmazenar': ['área de piscina'],
    'mobUtilizar': ['área de piscina'],
}

objetos['guarda-sol'] = {
    'largura': 2000,
    'altura': 2500,
    'profundidade': 2000,
    'peso': 8,
    'material': ['tecido', 'metal'],
    'funcao': ['proteger do sol'],
    'mobArmazenar': ['área de piscina'],
    'mobUtilizar': ['área de piscina'],
}

objetos['toalha de praia'] = {
    'largura': 800,
    'altura': 1500,
    'profundidade': 10,
    'peso': 0.5,
    'material': ['algodão'],
    'funcao': ['cobrir superfícies'],
    'mobArmazenar': ['espreguiçadeira'],
    'mobUtilizar': ['área de piscina'],
}

objetos['cooler'] = {
    'largura': 400,
    'altura': 300,
    'profundidade': 300,
    'peso': 3,
    'material': ['plastico', 'metal'],
    'funcao': ['armazenar bebidas geladas'],
    'mobArmazenar': ['área de piscina'],
    'mobUtilizar': ['área de piscina'],
}

objetos['boia inflável'] = {
    'largura': 800,
    'altura': 800,
    'profundidade': 800,
    'peso': 1,
    'material': ['plastico'],
    'funcao': ['flutuar na água'],
    'mobArmazenar': ['área de piscina'],
    'mobUtilizar': ['área de piscina'],
}

objetos['cadeira reclinável'] = {
    'largura': 600,
    'altura': 800,
    'profundidade': 700,
    'peso': 10,
    'material': ['plastico', 'metal'],
    'funcao': ['sentar e relaxar'],
    'mobArmazenar': ['área de piscina'],
    'mobUtilizar': ['área de piscina'],
}

objetos['mesa lateral'] = {
    'largura': 400,
    'altura': 500,
    'profundidade': 400,
    'peso': 5,
    'material': ['plastico', 'metal'],
    'funcao': ['apoio para objetos'],
    'mobArmazenar': ['área de piscina'],
    'mobUtilizar': ['área de piscina'],
}

objetos['chuveiro externo'] = {
    'largura': 200,
    'altura': 2000,
    'profundidade': 200,
    'peso': 4,
    'material': ['metal', 'plastico'],
    'funcao': ['banho de água fria'],
    'mobArmazenar': ['parede'],
    'mobUtilizar': ['área de piscina'],
}

objetos['caixa de som resistente à água'] = {
    'largura': 200,
    'altura': 300,
    'profundidade': 200,
    'peso': 2,
    'material': ['plastico', 'metal'],
    'funcao': ['reprodução de áudio'],
    'mobArmazenar': ['mesa lateral'],
    'mobUtilizar': ['área de piscina'],
}

objetos['mesa para petiscos'] = {
    'largura': 600,
    'altura': 600,
    'profundidade': 600,
    'peso': 8,
    'material': ['madeira', 'metal'],
    'funcao': ['apoio para petiscos e bebidas'],
    'mobArmazenar': ['área de piscina'],
    'mobUtilizar': ['área de piscina'],
}

# Verificando se os objetos foram inseridos corretamente
print("Objetos no dicionário:")
for objeto, detalhes in objetos.items():
    print(objeto)

# Lista de objetos que podem estar em uma 'academia'
objetos_academia = [
    'esteira',
    'bicicleta ergométrica',
    'halteres',
    'barra de peso',
    'colchonete',
    'bola de exercícios',
    'máquina de musculação',
    'corda de pular',
    'elástico de resistência',
    'kettlebell',
]

# Inserindo os objetos no dicionário 'objetos'
objetos['esteira'] = {
    'largura': 800,
    'altura': 1200,
    'profundidade': 1800,
    'peso': 70,
    'material': ['metal', 'plastico'],
    'funcao': ['exercício cardiovascular'],
    'mobArmazenar': ['academia'],
    'mobUtilizar': ['academia'],
}

objetos['bicicleta ergométrica'] = {
    'largura': 600,
    'altura': 1200,
    'profundidade': 1000,
    'peso': 50,
    'material': ['metal', 'plastico'],
    'funcao': ['exercício cardiovascular'],
    'mobArmazenar': ['academia'],
    'mobUtilizar': ['academia'],
}

objetos['halteres'] = {
    'largura': 200,
    'altura': 300,
    'profundidade': 200,
    'peso': 2,
    'material': ['metal'],
    'funcao': ['exercício de força'],
    'mobArmazenar': ['academia'],
    'mobUtilizar': ['academia'],
}

objetos['barra de peso'] = {
    'largura': 1500,
    'altura': 200,
    'profundidade': 200,
    'peso': 15,
    'material': ['metal'],
    'funcao': ['exercício de força'],
    'mobArmazenar': ['academia'],
    'mobUtilizar': ['academia'],
}

objetos['colchonete'] = {
    'largura': 600,
    'altura': 10,
    'profundidade': 1200,
    'peso': 2,
    'material': ['espuma', 'tecido'],
    'funcao': ['apoio para exercícios'],
    'mobArmazenar': ['academia'],
    'mobUtilizar': ['academia'],
}

objetos['bola de exercícios'] = {
    'largura': 600,
    'altura': 600,
    'profundidade': 600,
    'peso': 1,
    'material': ['plastico'],
    'funcao': ['exercícios de equilíbrio'],
    'mobArmazenar': ['academia'],
    'mobUtilizar': ['academia'],
}

objetos['máquina de musculação'] = {
    'largura': 1200,
    'altura': 1800,
    'profundidade': 2000,
    'peso': 120,
    'material': ['metal', 'plastico'],
    'funcao': ['exercício de força'],
    'mobArmazenar': ['academia'],
    'mobUtilizar': ['academia'],
}

objetos['corda de pular'] = {
    'largura': 20,
    'altura': 300,
    'profundidade': 20,
    'peso': 0.5,
    'material': ['tecido', 'plastico'],
    'funcao': ['exercício cardiovascular'],
    'mobArmazenar': ['academia'],
    'mobUtilizar': ['academia'],
}

objetos['elástico de resistência'] = {
    'largura': 1000,
    'altura': 20,
    'profundidade': 20,
    'peso': 0.2,
    'material': ['borracha'],
    'funcao': ['exercício de resistência'],
    'mobArmazenar': ['academia'],
    'mobUtilizar': ['academia'],
}

objetos['kettlebell'] = {
    'largura': 200,
    'altura': 300,
    'profundidade': 200,
    'peso': 10,
    'material': ['metal'],
    'funcao': ['exercício de força'],
    'mobArmazenar': ['academia'],
    'mobUtilizar': ['academia'],
}

# Verificando se os objetos foram inseridos corretamente
print("Objetos no dicionário:")
for objeto, detalhes in objetos.items():
    print(objeto)


salvar_em_arquivo(objetos, 'foton_system/foton_make/objetos.json')

print("\n\n\nDados salvos com sucesso no arquivo objetos.json.")
