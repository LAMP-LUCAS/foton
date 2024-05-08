import pandas as pd
import os
from pathlib import Path
import io


class BaseServidor:
    def __init__(self, caminho_pastaClientes, caminho_baseClientes):
        self.pastaClientes = Path(caminho_pastaClientes)
        self.baseClientes = Path(caminho_baseClientes)

class Verificar(BaseServidor):

    def converter_excel_para_csv(self):
        xls = pd.ExcelFile(self.baseClientes)
        csv_dict = {sheet_name: pd.read_excel(xls, sheet_name=sheet_name).to_csv(index=False)
                    for sheet_name in xls.sheet_names}
        return csv_dict

    def imprimir_dicionario_csv(self, csv_dict):
        print('Dicionário de CSV:', csv_dict, '\n')


    def DbExcel2CSV(self):
        print('Convertendo a base excel em csv...\n')
        xls = pd.ExcelFile(self.baseClientes)
        csv_dict = {}
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet_name)
            csv_dict[sheet_name] = df.to_csv(index=False)
        print('dicionário de csv: ',csv_dict,'\n')
        return csv_dict
    
    def AliasDB(self):
        print('Definindo os nomes dos clientes... \n')
        base = self.DbExcel2CSV()
        print(base,'\n')

        df_clientes = pd.read_csv(base)

        return df_clientes['Alias'].tolist()

    def verificar_pastas(self):
        print('Iniciando a Verificação das Pastas dos Clientes...\n')

        lista_atual = [pasta.name for pasta in self.pastaClientes.iterdir() if pasta.is_dir()]
        NomeAlias = self.AliasDB()
        lista_novos = set(NomeAlias) - set(lista_atual)

        for nome_novo in lista_novos:
            try:
                (self.pastaClientes / nome_novo).mkdir()
                print(f'Pasta "{nome_novo}" criada com sucesso.')
            except Exception as e:
                print(f'Erro ao criar pasta "{nome_novo}": {e}')
        
        print('Pastas dos Clientes Verificadas...')

    def baseCSV(self,Base,nome_csv):
        # Verifique se o CSV foi encontrado
        print('verificando base...\n')
        try:
            base = Base
            print(f"CSV da planilha '{base.keys()}' encontrado!")
        except:
            print(f"Planilha '{base}' não encontrada no dicionário.")
        return base
   
    def PastasClientes(self): #Os clientes da base estão com pastas no servidor?
        print('Iniciando a Verificação das Pastas dos Clientes...')

        #Verificar a pasta e adicionar os nomes das subpastas de primeiro nível em listaAtual
        listaAtual = os.listdir(self.pastaClientes)
        print(f'Clientes atuais:\n {listaAtual}')
                
        # Ler os nomes de clientes do arquivo CSV
        conversor = self.DbExcel2CSV()
        nomeCSV = 'baseClientes'

        if nomeCSV in conversor:
            dfClientes = pd.read_csv(io.StringIO(conversor[nomeCSV]))
            nomesClientes = dfClientes['Alias'].tolist()
        else:
            print(f"CSV '{nomeCSV}' não encontrado no dicionário.")
            return

        #Verificar quais nomes de clientes não estão na listaAtual e os que não estiverem na listaAtual serão adicionados à listaNovos
        listaNovos = [cliente for cliente in nomesClientes if cliente not in listaAtual]
        print(f'Clientes Novos:\n {listaNovos}')

        #Criar novas subpastas com os nomes da listaNovos
        criar = Criar(self.pastaClientes,self.baseClientes)
        criar.NovasPastas(listaNovos)

        print('Pastas dos Clientes Verificadas...')

        return print(f'Clientes Novos:\n {listaNovos}')
    
    def PastasServicos(self): #Os Serviços dos clientes da base estão no servidor?
        r1 = ['Servico 1 - Cliente 1','Servico 1 - Cliente 2','Servico 1 - Cliente 3']
        print('Pastas de Serviços Verificadas...')
        return r1
    
    def Status(self): #Status da base igual ao Statos do Servidor?
        r1 = print('Status do Serviço verificado...')
        return r1

    def MoldeloDataBase(self):

        Database = self.baseClientes
        #Recebe o arquivo
        #Transforma a pasta com várias planilhas em csvs com os nomes das planilhas
        #printa o nome de cada planilha e cria uma variável para cada
        #
        return Database

class Criar(BaseServidor):

    def NovasPastas(self, listaNovasPastas):
        
        listaClientes = listaNovasPastas

        for i, nome_pasta in enumerate(listaClientes):
            try:
                pasta_nova = self.pastaClientes / nome_pasta.upper()
                pasta_nova.mkdir()
                print(f"Pasta '{nome_pasta}' criada com sucesso! ({i+1}/{len(listaNovasPastas)})")
            except Exception as e:
                print(f"Erro ao criar pasta '{nome_pasta}': {e}")

    def PastasServiços(Clientes):
        i1 = Clientes
        r1 = print(f'Pastas dos serviços {i1[:]} Criadas')
        return r1
    
    def AtualizaçãoStatus(self):
        Verificar.Status(self)
        r1 = print('Status do Serviço atualizado')
        return r1

print('GESTÃO DE SERVIDOR - DATABASE\n')

p1=input('Deseja Iniciar a Sincronização das pastas do servidor com a base de dados? (Y/N)\n')
diretorio_base = f'C:\\Users\\Lucas\\OneDrive\\LAMP ARQUITETURA\\foton\\foton_system\\foton_make\\testes\\CLIENTES'
dataBase = f'C:\\Users\\Lucas\\OneDrive\\LAMP ARQUITETURA\\foton\\foton_system\\foton_make\\testes\\base.xlsx'
verServidor = Verificar(caminho_pastaClientes = diretorio_base,caminho_baseClientes = dataBase)
criarServidor = Criar(caminho_pastaClientes = diretorio_base,caminho_baseClientes = dataBase)
if p1.lower() == 'Y':
    print('\nIniciando Sincronização...\n')
    v1 = verServidor.PastasClientes()
    v3 = criarServidor.AtualizaçãoStatus()
    print('\nFim da Sincronização...\n')
else:
    print('\nNão Sincronizar...\n')

print('<<<<< Fim do Programa >>>>>>')

##########################################
#Funções necessárias:#
##########################################

#Visualizar Clientes da Base
Verificar.VerClientes('base')

#Visualizar Clientes do servidor
Verificar.VerClientes('servidor')

#Visualizar Serviços da Base
Verificar.VerServicos('base')

#Visualizar Serviços do Servidor
Verificar.VerServicos('servidor')

##########################################

#Sincronizar Clientes - Servidor com Base
Criar.SincronizarClientes('servidor')

#Sincronizar Clientes - Base com Servidor
Criar.SincronizarClientes('base')

#Sincronizar Serciços - Servidor com Base
Criar.SincronizarServicos('servidor')

#Sincronizar Serviços - Base com Servidor
Criar.SincronizarServicos('base')


##########################################
