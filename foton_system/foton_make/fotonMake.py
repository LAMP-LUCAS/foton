import json
import tkinter as tk
from tkinter import messagebox
from funcoes import *

def mostrar_barra_progresso(funcao, nome_funcao, *args, **kwargs):
    with tqdm(total=100, desc=nome_funcao, leave=False) as pbar:
        for _ in range(100):
            funcao(*args, **kwargs)
            pbar.update(1)

def mostrar_nomes_objetos(objetos_dict):
    nomes_objetos = list(objetos_dict.keys())
    return nomes_objetos

def adicionar_objeto_interface():
    nome = entry_nome.get()
    largura = int(entry_largura.get())
    altura = int(entry_altura.get())
    profundidade = int(entry_profundidade.get())
    peso = float(entry_peso.get())
    materiais = entry_materiais.get().split(',')
    funcoes = entry_funcoes.get().split(',')
    mob_armazenar = entry_mob_armazenar.get().split(',')
    mob_utilizar = entry_mob_utilizar.get().split(',')

    mostrar_barra_progresso(adicionar_objeto, "Adicionando objeto", objetos, nome, largura, altura, profundidade, peso, materiais, funcoes, mob_armazenar, mob_utilizar)
    messagebox.showinfo("Sucesso", f"Objeto '{nome}' adicionado ao dicionário.")

def coletar_informacoes_objeto_interface():
    nome = entry_nome_obj.get()
    coletar_informacoes_objeto(objetos, nome)

def deletar_objeto_interface():
    nome = entry_nome_del.get()
    mostrar_barra_progresso(deletar_objeto, "Deletando objeto", objetos, nome)
    messagebox.showinfo("Sucesso", f"Objeto '{nome}' deletado do dicionário.")

# Carregar dados do arquivo JSON
with open('foton_system/foton_make/objetos.json', 'r') as arquivo:
    objetos = json.load(arquivo)

root = tk.Tk()
root.title("Cadastro de Objetos - Foton System")

# Frame para adicionar objetos
frame_adicionar = tk.Frame(root)
frame_adicionar.pack(pady=10)

label_nome = tk.Label(frame_adicionar, text="Nome:")
label_nome.grid(row=0, column=0, padx=10)
entry_nome = tk.Entry(frame_adicionar)
entry_nome.grid(row=0, column=1)

label_largura = tk.Label(frame_adicionar, text="Largura:")
label_largura.grid(row=1, column=0, padx=10)
entry_largura = tk.Entry(frame_adicionar)
entry_largura.grid(row=1, column=1)

label_altura = tk.Label(frame_adicionar, text="Altura:")
label_altura.grid(row=2, column=0, padx=10)
entry_altura = tk.Entry(frame_adicionar)
entry_altura.grid(row=2, column=1)

label_profundidade = tk.Label(frame_adicionar, text="Profundidade:")
label_profundidade.grid(row=3, column=0, padx=10)
entry_profundidade = tk.Entry(frame_adicionar)
entry_profundidade.grid(row=3, column=1)

label_peso = tk.Label(frame_adicionar, text="Peso:")
label_peso.grid(row=4, column=0, padx=10)
entry_peso = tk.Entry(frame_adicionar)
entry_peso.grid(row=4, column=1)

label_materiais = tk.Label(frame_adicionar, text="Materiais (separados por vírgula):")
label_materiais.grid(row=5, column=0, padx=10)
entry_materiais = tk.Entry(frame_adicionar)
entry_materiais.grid(row=5, column=1)

label_funcoes = tk.Label(frame_adicionar, text="Funções (separadas por vírgula):")
label_funcoes.grid(row=6, column=0, padx=10)
entry_funcoes = tk.Entry(frame_adicionar)
entry_funcoes.grid(row=6, column=1)

label_mob_armazenar = tk.Label(frame_adicionar, text="Mobiliários onde pode-se armazenar (separados por vírgula):")
label_mob_armazenar.grid(row=7, column=0, padx=10)
entry_mob_armazenar = tk.Entry(frame_adicionar)
entry_mob_armazenar.grid(row=7, column=1)

label_mob_utilizar = tk.Label(frame_adicionar, text="Mobiliários onde pode-se utilizar (separados por vírgula):")
label_mob_utilizar.grid(row=8, column=0, padx=10)
entry_mob_utilizar = tk.Entry(frame_adicionar)
entry_mob_utilizar.grid(row=8, column=1)

button_adicionar = tk.Button(frame_adicionar, text="Adicionar Objeto", command=adicionar_objeto_interface)
button_adicionar.grid(row=9, column=0, columnspan=2, pady=10)

# Frame para coletar informações de um objeto
frame_coletar = tk.Frame(root)
frame_coletar.pack(pady=10)

label_nome_obj = tk.Label(frame_coletar, text="Nome do objeto:")
label_nome_obj.grid(row=0, column=0, padx=10)
entry_nome_obj = tk.Entry(frame_coletar)
entry_nome_obj.grid(row=0, column=1)

button_coletar = tk.Button(frame_coletar, text="Coletar Informações", command=coletar_informacoes_objeto_interface)
button_coletar.grid(row=1, column=0, columnspan=2, pady=10)

# Frame para deletar um objeto
frame_deletar = tk.Frame(root)
frame_deletar.pack(pady=10)

label_nome_del = tk.Label(frame_deletar, text="Nome do objeto:")
label_nome_del.grid(row=0, column=0, padx=10)
entry_nome_del = tk.Entry(frame_deletar)
entry_nome_del.grid(row=0, column=1)

button_deletar = tk.Button(frame_deletar, text="Deletar Objeto", command=deletar_objeto_interface)
button_deletar.grid(row=1, column=0, columnspan=2, pady=10)

# Frame para visualizar todos os objetos cadastrados
frame_visualizar = tk.Frame(root)
frame_visualizar.pack(pady=10)

button_visualizar = tk.Button(frame_visualizar, text="Visualizar Todos os Objetos", command=lambda: messagebox.showinfo("Objetos Cadastrados", ", ".join(mostrar_nomes_objetos(objetos))))
button_visualizar.pack()

root.mainloop()
