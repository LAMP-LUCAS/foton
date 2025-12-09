# make-file.ps1
param (
    [string]$Command = "help"
)

switch ($Command) {
    "up"         { docker compose up -d }
    "down"       { docker compose down }
    "restart"    { docker compose down; docker compose up -d }
    "build"      { docker compose build }
    "logs"       { docker compose logs -f }
    "ps"         { docker compose ps }
    "status"     { docker compose ps }
    "health"     { docker compose ps --format "table {{.Name}}\t{{.State}}\t{{.Health}}" }
    "init"       {
        docker compose down
        docker volume rm comunidadefoton_redmine_data comunidadefoton_redmine_postgres_data -f
        docker compose build
        docker compose up -d
        docker compose ps
    }
    "setup"      {
        if (-not (Test-Path ".env")) {
            Write-Host "📋 Arquivo .env não encontrado. Copiando de .env.example..."
            Copy-Item ".env.example" ".env"
            Write-Host "‼️ IMPORTANTE: Por favor, revise e edite o arquivo .env com suas configurações específicas, depois rode '.\start.bat setup' novamente."
            exit
        }
        if (Test-Path "redmine/config/master.key") {
            Write-Host "✅ Chave mestra (master.key) já existe. Nada a fazer."
        } else {
            Write-Host "🔑 Chave mestra não encontrada. Iniciando configuração de primeira vez..."
            docker compose up -d
            Write-Host "⏳ Aguardando serviços ficarem prontos..."
            Start-Sleep -Seconds 20
            Write-Host "🔐 Gerando novas credenciais (non-interactive)..."
            docker compose exec -e VISUAL= -e EDITOR= foton_redmine rails credentials:edit
            Write-Host "📂 Copiando arquivos gerados para o host..."
            docker cp comunidadefoton:/usr/src/redmine/config/master.key ./redmine/config/master.key
            docker cp comunidadefoton:/usr/src/redmine/config/credentials.yml.enc ./redmine/config/credentials.yml.enc
            Write-Host "🔄 Reiniciando serviços para carregar novas chaves..."
            docker compose down; docker compose up -d
            Write-Host "🎉 Configuração inicial concluída com sucesso!"
        }
    }
    "pg-console" {
        $envVars = Get-Content .env | ConvertFrom-StringData
        docker exec -it fotonpostgres psql -U $envVars.POSTGRES_USER -d $envVars.POSTGRES_DB
    }
    "pg-dump" {
        docker exec fotonpostgres pg_dump -U redmine -d redmine > backup.sql
    }
    "redmine-console" {
        docker exec -it comunidadefoton bash
    }
    "smtp-test" {
        Start-Process "telnet.exe" -ArgumentList "smtp.hostinger.com 587"
    }
    "clean-volumes" {
        docker volume rm comunidadefoton_redmine_data comunidadefoton_redmine_postgres_data -f
    }
    "prune" {
        docker system prune -f --volumes
    }
    default {
        Write-Host "Comandos disponíveis:"
        Write-Host "  up              → Inicia os serviços em segundo plano."
        Write-Host "  down            → Para todos os serviços."
        Write-Host "  restart         → Reinicia todos os serviços."
        Write-Host "  build           → Reconstrói as imagens dos contêineres."
        Write-Host "  setup           → (Primeira vez) Configura o projeto, incluindo chaves de segurança."
        Write-Host "  init            → (Destrutivo) Reinicia o projeto do zero, limpando volumes."
        Write-Host "  logs            → Mostra os logs dos serviços em tempo real."
        Write-Host "  status / ps     → Mostra o status dos contêineres."
        Write-Host "  pg-console      → Acessa o console psql do banco de dados."
        Write-Host "  redmine-console → Acessa o terminal bash do contêiner Redmine."
    }
}
