import os
import subprocess

# Lê o arquivo .gitignore e armazena os padrões em uma lista
with open('.gitignore', 'r') as f:
    patterns = f.read().splitlines()

# Itera sobre os padrões e exclui os arquivos e pastas correspondentes
for pattern in patterns:
    # Usa o comando dir para encontrar os arquivos e pastas correspondentes
    result = subprocess.run(['cmd', '/c', f'dir /b /s {pattern}'], stdout=subprocess.PIPE)
    files = result.stdout.decode('utf-8').splitlines()

    # Remove os arquivos e pastas encontrados
    for file in files:
        subprocess.run(['git', 'rm', '-r', '--cached', file])
