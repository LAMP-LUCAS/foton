# Variáveis
COMPOSE=docker compose
PROJECT_NAME=comunidadefoton

# Rotinas principais
up:
    $(COMPOSE) up -d

down:
    $(COMPOSE) down

restart:
    $(COMPOSE) down && $(COMPOSE) up -d

build:
    $(COMPOSE) build

logs:
    $(COMPOSE) logs -f

ps:
    $(COMPOSE) ps

# Inicialização completa (rebuilda e sobe do zero)
init: down clean-volumes build up status

# Novo: Setup de primeira inicialização para credenciais
setup:
	@if [ ! -f ".env" ]; then \
		echo "📋 Arquivo .env não encontrado. Copiando de .env.example..."; \
		cp .env.example .env; \
		echo "‼️ IMPORTANTE: Por favor, revise e edite o arquivo .env com suas configurações específicas, depois rode 'make setup' novamente."; \
		exit 0; \
	fi; \
	@if [ -f "redmine/config/master.key" ]; then \
		echo "✅ Chave mestra (master.key) já existe. Nada a fazer."; \
	else \
		echo "🔑 Chave mestra não encontrada. Iniciando configuração de primeira vez..."; \
		sudo $(COMPOSE) up -d; \
		echo "⏳ Aguardando serviços ficarem prontos..."; \
		sleep 20; \
		echo "🔐 Gerando novas credenciais (non-interactive)..."; \
		sudo $(COMPOSE) exec -e VISUAL= -e EDITOR= foton_redmine rails credentials:edit; \
		echo "📂 Copiando arquivos gerados para o host..."; \
		sudo docker cp comunidadefoton:/usr/src/redmine/config/master.key ./redmine/config/master.key; \
		sudo docker cp comunidadefoton:/usr/src/redmine/config/credentials.yml.enc ./redmine/config/credentials.yml.enc; \
		echo "🔒 Corrigindo permissões dos arquivos..."; \
		sudo chown $(shell id -u):$(shell id -g) ./redmine/config/master.key ./redmine/config/credentials.yml.enc; \
		echo "🔄 Reiniciando serviços para carregar novas chaves..."; \
		sudo $(COMPOSE) down && sudo $(COMPOSE) up -d; \
		echo "🎉 Configuração inicial concluída com sucesso!"; \
	fi

# Status e inspeção
status:
	$(COMPOSE) ps
health:
    @echo "\n📋 Verificando healthchecks:\n"
    $(COMPOSE) ps --format "table {{.Name}}\t{{.State}}\t{{.Health}}"

# Banco de Dados
pg-console:
    docker exec -it fotonpostgres psql -U $(shell grep POSTGRES_USER .env | cut -d '=' -f2) -d $(shell grep POSTGRES_DB .env | cut -d '=' -f2)

pg-dump:
    docker exec fotonpostgres pg_dump -U redmine -d redmine > backup.sql

# Redmine
redmine-console:
    docker exec -it comunidadefoton bash

# Volumes e limpeza
clean-volumes:
    docker volume rm comunidadefoton_redmine_data comunidadefoton_redmine_postgres_data || true

prune:
    docker system prune -f --volumes

# SMTP Teste (via telnet)
smtp-test:
    telnet smtp.hostinger.com 587
