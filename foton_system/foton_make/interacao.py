import json
from funcoes import *

def interacao_usuario():
    caminho = 'foton_system/foton_make/objetos.json'
    # Carregar dados do arquivo JSON
    with open(caminho, 'r') as arquivo:
        objetos = json.load(arquivo)

    while True:
        print("\n1. Adicionar objeto")
        print("2. Coletar informações de um objeto")
        print("3. Deletar objeto")
        print('4. Visualizar todos os ambientes cadastrados')
        print("0. Sair\n")

        opcao = input("Escolha uma opção (1/2/3/4/0): ")
        print('\n\n')

        if opcao == '1':
            nome = input("Nome do objeto: ")
            largura = int(input("Largura em milímetros: "))
            altura = int(input("Altura em milímetros: "))
            profundidade = int(input("Profundidade em milímetros: "))
            peso = float(input("Peso em quilograma: "))
            materiais = input("Materiais (separados por vírgula): ").split(',')
            funcoes = input("Funções (separadas por vírgula): ").split(',')
            mob_armazenar = input("Mobiliários onde pode-se armazenar (separados por vírgula): ").split(',')
            mob_utilizar = input("Mobiliários onde pode-se utilizar (separados por vírgula): ").split(',')

            mostrar_barra_progresso(adicionar_objeto, "Adicionando objeto", objetos, nome, largura, altura, profundidade, peso, materiais, funcoes, mob_armazenar, mob_utilizar)

        elif opcao == '2':
            nome = input("\nNome do objeto:\n ")
            mostrar_barra_progresso(coletar_informacoes_objeto, "Coletando informações", objetos, nome)

        elif opcao == '3':
            nome = input("\nNome do objeto a ser deletado:\n ")
            mostrar_barra_progresso(deletar_objeto, "Deletando objeto", objetos, nome)

        elif opcao == '4':
            mostrar_nomes_objetos(objetos)

        elif opcao == '0':

            saida = input('\n\nDeseja salvar uma nova base de dados? (Y/N):\n')

            if saida.lower() == 'n':
                # Sair sem salvar
                print('\nPrograma foi encerrado e os dados não foram salvos no arquivo objetos.json\n')
                break
            elif saida.lower() == 'y':
                # Salvar os dados no arquivo JSON antes de sair
                salvar_em_arquivo(objetos, caminho)
                print("\n\n\n\nDados salvos com sucesso no arquivo objetos.json.\n\n\n\n")
                break
            else:
                print("\n\n\n\nOpção inválida. Escolha novamente.\n\n\n\n")

        else:
            print("\n\n\n\nOpção inválida. Escolha novamente.\n\n\n\n")

if __name__ == "__main__":
    interacao_usuario()
