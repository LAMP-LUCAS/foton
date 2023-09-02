corpoDocente = ''' Efetivos: Adair Marques Filho, Adriana Aparecida Mendonça, Adriana Mara Vaz de Oliveira, Aguinaldo C. C. A. Coelho, Alice Fátima Martins, Ana Amélia de Paula Moura Ribeiro, Ana Lúcia Beck, Braulio Romeiro, Braulio Vinícius Ferreira, Breno Tenório Ramalho de Abreu, Camilo Vladimir de Lima Amaral, Carla Luzia de Abreu, Carlos Gustavo Martins Hoelzel, Christine Ramos Mahler, Claudio Aleixo Rocha, Cleomar de Sousa Rocha, Daniel de Salles Canfield, Dorivalda Santos Medeiros, Douglas Daniel Pereira, Edgar Silveira Franco, Eliane Maria Chaud, Elinaldo da Silva Meira, Eline Maria Mora Pereira Caixeta, Erika Cristine Kneib, Fábio Ferreira de Lima, Fernando Antônio Oliveira Mello, Flávia Leme de Almeida, Flávio Gomes de Oliveira, Frederico André Rabelo, Gisele Costa Ferreira da Silva, Gilson Oliveira Barreto, Glayson Arcanjo de Sampaio, Juliano Ribeiro de Moraes, Kelly Christina Mendes Arantes, Laudemiro Roriz Junior, Lavinnia Seabra Gomes, Leda Maria de Barros Guimaraes, Lilian Ucker Perotto Palazzo , Lorena Pompei Abdala , Luana Miranda Esper kallas , Lucas Jordano de Melo Barbosa , Luiz Henrique Arantes Araújo Olivieri , Manoela dos Anjos Afonso Rodrigues , Marcelina Gorni , Marcio Alves da Rocha , Marcos Antonio Soares , Maria Luiza de Ulhoa Carvalho , Maria Tereza Gomes da Silva , Maristela Abadia Fernandes Novaes , Noeli Batista dos Santos , Odinaldo da Costa Silva , Patrícia Bueno Godoy , Paulo Henrique Duarte Feitoza , Pedro Henrique Gonçalves Quefren Trindade M. Crillanovick , Ravi Figueiredo Passos , Regis de Castro Ferreira , Rita Morais de Andrade , Rogeria Eler Silva Souza , Rosa Maria Berardo , Rosana Horio Monteiro , Rosane Costa Badan Rubens Pilegi da Silva Sá Samuel José Gilbert de Jesus Thalita Pereira da Fonseca Valéria Fabiane Braga Ferreira Viviane de Sousa Cruz e Silva Wagner Bandeira da Silva.
Substitutos: Eurípedes Afonso Da Silva Neto Juan Sebastian Ospina Alvarez Matheus André Gomes Mota Nayara Araujo Assis Simone Buiate Brandão.
Voluntários: José César Clímaco Juan Carlos Guillen Salas.'''

# Split the string into three parts: Efetivos, Substitutos and Voluntários
parts = corpoDocente.split('\n')

# Initialize an empty dictionary to store the results
fav_ufg_faculty = {}

# Process each part of the string
for part in parts:
    # Split the part into two: type and names
    type_, names = part.split(':')
    
    # Remove any leading or trailing whitespace from the type
    type_ = type_.strip()
    
    # Split the names by comma
    names = names.split(',')
    
    # Process each name
    for name in names:
        # Remove any leading or trailing whitespace from the name
        name = name.strip()
        
        # Add the name and type to the dictionary
        fav_ufg_faculty[name] = type_

# Print the resulting dictionary
#print(fav_ufg_faculty)
# Define o dicionário fav_ufg_faculty

# Inicializa listas vazias para armazenar os nomes dos professores de cada tipo
efetivos = []
substitutos = []
voluntarios = []

# Itera sobre os itens do dicionário
for professor, tipo in fav_ufg_faculty.items():
    # Verifica o tipo do professor e adiciona o nome à lista correspondente
    if tipo == 'Efetivos':
        efetivos.append(professor)
    elif tipo == 'Substitutos':
        substitutos.append(professor)
    else:
        voluntarios.append(professor)

# Imprime as listas de professores de cada tipo
print(f'Professores efetivos:\n{efetivos}\n\nProfessores Substitutos:\n{substitutos}\n\nProfessores Voluntarios:\n{voluntarios}')
