import os
import csv
from datetime import datetime
import re

log = []

def get_folder_structure(root_dir):
    folder_structure = {}
    for root, dirs, files in os.walk(root_dir):
        rel_path = os.path.relpath(root, root_dir)
        if rel_path == ".":
            rel_path = root_dir
        depth = rel_path.count(os.sep)
        # Atualiza o dicionário de estrutura de pastas
        folder_structure[rel_path] = {"depth": depth, "subfolders": dirs, "files": files}
        # Registra a pasta atual no log
        log.append(f"Encontrada pasta: {rel_path} com profundidade {depth}")

        #print(folder_structure)
    return folder_structure
    '''
        # Extrai o nome do cliente e serviço
        match = re.match(r"(.+?)/(.+?)/?", rel_path)
        if match:
            cliente, servico = match.groups()
        else:
            continue
        
        folder_structure[rel_path] = {"depth": depth, "subfolders": dirs, "files": files}
        log.append(f"Encontrada pasta: {rel_path} com profundidade {depth}")
    print(folder_structure)
    return folder_structure
    '''

'''
def write_to_csv(folder_structure, csv_file_name):
    with open(csv_file_name, mode='w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["NOME-CLIENTE", "SERVICO", "NIVEL3", "NIVEL4"])
        for path, info in folder_structure.items():
            cliente, servico = path.split(os.sep, 1)
            if info["depth"] == 2:
                nivel3 = info["subfolders"][0]
                nivel4 = ""
            elif info["depth"] == 3:
                nivel3 = info["subfolders"][0]
                nivel4 = info["files"][0]
            else:
                continue
            row = [cliente, servico, nivel3, nivel4]
            csv_writer.writerow(row)
'''

def write_to_csv(folder_structure, csv_file_name):
    """
    Escreve a estrutura de pastas em um arquivo CSV, representando o nível de profundidade dos arquivos e pastas.
    """
    with open(csv_file_name, mode='w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')
        # Escreve o cabeçalho
        csv_writer.writerow(["PASTA-CLIENTE", "PASTA-SERVICO","NIVEL-3",])
        # Escreve a estrutura de pastas
        for depth, info in folder_structure.items():
            row = [path, info["depth"]]
            csv_writer.writerow(row)

def write_log(log, log_file_name):
    """
    Escreve o log em um arquivo de texto.
    """
    with open(log_file_name, 'w') as log_file:
        for entry in log:
            log_file.write(entry + "\n")

def save_log(log):
    """
    Salva um arquivo de log com o que foi feito.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = f"log_{timestamp}.txt"
    with open(log_filename, 'w') as f:
        f.write("\n".join(log))
    return log_filename

def read_subfolders(folder_path):
    """
    Lê o nome de todas as subpastas de uma determinada pasta.
    """
    subfolders = []
    for root, dirs, files in os.walk(folder_path):
        for dir_name in dirs:
            subfolders.append(dir_name)
    return subfolders

def read_csv(csv_path):
    """
    Lê os nomes da coluna "nome da pasta" em um arquivo CSV.
    """
    folder_names = []
    with open(csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            folder_names.append(row['nome da pasta'])
    return folder_names

def create_folders(folder_names):
    """
    Cria a estrutura de subpastas conforme as regras especificadas.
    """
    log = []
    for folder_name in folder_names:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            log.append(f"Criada a pasta: {folder_name}")
            os.makedirs(os.path.join(folder_name, 'DOC'))
            os.makedirs(os.path.join(folder_name, 'COMERCIAL'))
            with open(os.path.join(folder_name, 'COMERCIAL', 'codigo.txt'), 'w') as f:
                f.write(f"Código do serviço: {folder_name}")
    return log

print(read_subfolders('CLIENTES'))

print(get_folder_structure('CLIENTES'))