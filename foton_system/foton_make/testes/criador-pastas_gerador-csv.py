from foton_system.foton_make.testes.lampastas import *

# Define o diretório raiz
root_dir = "CLIENTES"

# Define o nome do arquivo CSV
csv_file_name = "base.csv"

# Define o nome do arquivo de log com o timestamp atual
log_file_name = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

# Obtém a estrutura de pastas
folder_structure = get_folder_structure(root_dir)

# Escreve a estrutura de pastas no arquivo CSV
write_to_csv(folder_structure, csv_file_name)

# Escreve o log no arquivo de log
write_log(log, log_file_name)

print(f"Arquivo de log salvo como: {log_file_name}")
