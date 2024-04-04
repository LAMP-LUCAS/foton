from foton_system.foton_make.testes.lampastas import *


if __name__ == "__main__":
    folder_path = "."  # Pasta atual onde o arquivo será executado
    csv_path = "base.csv"  # Substitua pelo caminho correto do seu arquivo CSV

    subfolders = read_subfolders(folder_path)
    folder_names_csv = read_csv(csv_path)

    missing_folders = set(folder_names_csv) - set(subfolders)
    log = create_folders(missing_folders)
    log_filename = save_log(log)

    print(f"Pastas criadas: {', '.join(missing_folders)}")
    print(f"Arquivo de log salvo como: {log_filename}")
