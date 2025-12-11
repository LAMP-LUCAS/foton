# 🤝 Guia de Contribuição - Ecossistema Foton

Bem-vindo ao Foton! Somos um ecossistema de soluções para a construção civil construído sobre o kernel do **Redmine**.

Este repositório é um "monorepo" que abriga o Kernel (configurações do Redmine) e os Módulos (Plugins). Sua contribuição é valiosa, seja no código livre ou reportando problemas.

---

## 🧭 Por onde começar?

Antes de codar, entenda onde sua contribuição se encaixa:

| Se você quer... | Você deve ir para... |
| :--- | :--- |
| Criar/Melhorar funcionalidades de CRM ou Fluxo de Caixa | **Plugins Comunitários** (`redmine/plugins/foton_contacts`, etc.) |
| Melhorar a Interface ou Tema | **FotonOS** (`redmine/themes/fotonOS`) |
| Corrigir configurações do Docker ou Redmine base | **Kernel** (Raiz deste repositório) |
| Entender a Arquitetura | [📖 Arquitetura do Ecossistema](docs/FOTON_ECOSYSTEM_ARCHITECTURE.md) |

---

## 🛠️ Ambiente de Desenvolvimento

1.  **Pré-requisitos:** Docker e Docker Compose.
2.  **Setup Rápido:**
    ```bash
    make setup
    # ou
    ./start.bat setup
    ```
    Isso subirá o Redmine, Banco de Dados e todos os plugins configurados.

---

## 📜 Regras do Jogo (Pipelines)

Para garantir a estabilidade do ecossistema, seguimos regras estritas. Por favor, leia nosso **[Pipeline de Desenvolvimento](docs/DEVELOPMENT_PIPELINES.md)** antes de abrir um Pull Request.

### Resumo Rápido:
1.  **Não toque no Core:** Evite alterar arquivos do Redmine fora da pasta `plugins/` ou `themes/`. Use *hooks* e *patches*.
2.  **Branches:** Crie branches a partir de `develop` (ex: `feat/nova-tela`).
3.  **Commits:** Use [Conventional Commits](https://www.conventionalcommits.org) (ex: `feat: adiciona botão de exportar`).
4.  **Testes:** Se quebrou, conserte. Se é novo, teste.

---

## 🐛 Reportando Problemas

Encontrou um bug? Ótimo (quer dizer, que pena, mas obrigado por avisar)!
Abra uma Issue detalhando:
1.  Qual plugin/módulo falhou?
2.  Passos para reproduzir.
3.  O que você esperava vs O que aconteceu.

---

## 📄 Licença e Legal

*   **Kernel e Plugins Comunitários:** GPLv3 (Software Livre).
*   **SaaS Core (foton_subscription_manager):** Proprietário/Comercial.

Ao contribuir, você concorda que seu código será compatível com estas licenças.