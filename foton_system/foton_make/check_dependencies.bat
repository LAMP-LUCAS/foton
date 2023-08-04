@echo off

echo Verificando dependências...

python -m pip freeze > installed_packages.txt

findstr /i "tqdm" installed_packages.txt > nul
if errorlevel 1 (
    echo Instalando dependências...
    pip install -r requirements.txt
    echo Dependências instaladas com sucesso!
) else (
    echo Todas as dependências já estão instaladas.
)

del installed_packages.txt
