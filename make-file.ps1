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
        Write-Host "  up              → docker compose up -d"
        Write-Host "  down            → docker compose down"
        Write-Host "  restart         → Reinicia o stack"
        Write-Host "  build           → Rebuilda os containers"
        Write-Host "  logs            → Mostra logs em tempo real"
        Write-Host "  status / ps     → Mostra status dos containers"
        Write-Host "  init            → Down + limpeza + build + up"
        Write-Host "  pg-console      → Acessa psql no container"
        Write-Host "  pg-dump         → Exporta dump do PostgreSQL"
        Write-Host "  redmine-console → Bash do container Redmine"
        Write-Host "  smtp-test       → Teste de conexão SMTP (telnet)"
        Write-Host "  clean-volumes   → Remove volumes específicos"
        Write-Host "  prune           → Limpa tudo (containers, volumes, etc)"
    }
}
