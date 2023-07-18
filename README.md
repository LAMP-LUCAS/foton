# Projeto Foton

O Projeto Foton é um sistema de gestão de escritórios de arquitetura, engenharia e construção. Ele foi desenvolvido utilizando Python com o framework Django, seguindo as diretrizes de microsserviços para a gestão de contrato, cliente e orçamento.

É um sistema feito por construtores para construtores!

## Funcionalidades

O projeto possui as seguintes funcionalidades principais:

- Gestão de Contratos: Permite cadastrar, visualizar, editar e excluir contratos. 
- Gestão de Clientes: Permite cadastrar, visualizar, editar e excluir clientes.
- Gestão de Orçamentos: Permite cadastrar, visualizar, editar e excluir orçamentos.

## Instalação

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório para o seu ambiente de desenvolvimento.
3. Instale as dependências do projeto executando o comando `pip install -r requirements.txt`.
4. Execute as migrações do banco de dados utilizando o comando `python manage.py migrate`.
5. Inicie o servidor de desenvolvimento com o comando `python manage.py runserver`.

## Configuração

Para configurar o projeto, você pode ajustar as seguintes configurações no arquivo `settings.py`:

- Configurações do Banco de Dados: Você pode alterar as configurações do banco de dados no bloco `DATABASES`.
- Autenticação de Usuários: Você pode personalizar as opções de autenticação de usuários no bloco `AUTHENTICATION_BACKENDS`.

## Uso

Após configurar e iniciar o projeto, você pode acessar a página inicial em `http://localhost:8000/`, onde encontrará opções para acessar as funcionalidades de gestão de contrato, cliente e orçamento.

## Contribuição

Contribuições para o projeto são bem-vindas! Se você tiver sugestões de melhorias, correções de bugs ou novas funcionalidades, fique à vontade para abrir uma *issue* ou enviar um *pull request*.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

