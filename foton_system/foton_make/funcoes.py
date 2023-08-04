import json
from tqdm import tqdm
import time

def mostrar_barra_progresso(funcao, nome_funcao, *args, **kwargs):
    with tqdm(total=100, desc=nome_funcao, leave=False) as pbar:
        for _ in range(100):
            funcao(*args, **kwargs)
            pbar.update(1)

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

def deletar_objeto(objetos_dict, nome):
    if nome in objetos_dict:
        del objetos_dict[nome]
        print(f"Objeto '{nome}' deletado do dicionário.")
    else:
        print(f"O objeto '{nome}' não foi encontrado no dicionário.")

def mostrar_nomes_objetos(objetos_dict):
    print("Nomes dos objetos cadastrados:")
    for nome_objeto in objetos_dict.keys():
        print(nome_objeto)

def salvar_em_arquivo(dicionario, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dicionario, arquivo, indent=4, ensure_ascii=False)
