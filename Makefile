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
