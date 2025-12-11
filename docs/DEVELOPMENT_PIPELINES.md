# 🚀 Pipelines de Desenvolvimento e Colaboração

Este documento define os fluxos de trabalho para contribuir com o ecossistema Foton. Como temos componentes com naturezas diferentes (Open Source vs SaaS), os pipelines variam.

---

## 1. Classificação dos Repositórios

| Componente | Tipo | Visibilidade | Pipeline Principal |
| :--- | :--- | :--- | :--- |
| **Kernel (Redmine)** | Upstream | Público (Fork) | Manutenção de infra (Docker) e configuração. |
| **Módulos Comunitários** | Plugin | **Open Source** | Fork -> Pull Request -> Review -> Merge. |
| **SaaS Core** | Plugin | **Proprietário/Restrito** | Internal Dev -> Code Review -> Deploy. |
| **FotonOS** | Tema | Híbrido | Design System -> Asset Compilation -> Publish. |

---

## 2. Fluxo de Trabalho (Git Flow Simplificado)

Adotamos um modelo de branches simplificado para todos os plugins:

*   `main`: Código estável, pronto para produção.
*   `develop`: Branch de integração. Todo PR deve apontar para cá.
*   `feature/nome-da-feature`: Desenvolvimento de novas funcionalidades.
*   `fix/nome-do-bug`: Correções de erros.

### Regras de Commit (Conventional Commits)
Obrigatório para manter o histórico legível e automatizar releases.

*   `feat: adiciona integração com WhatsApp`
*   `fix: corrige erro de cálculo no fluxo de caixa`
*   `docs: atualiza diagrama de arquitetura`
*   `chore: atualização de dependências`

---

## 3. Pipeline de Qualidade (Definition of Done)

Para um código ser aceito no Kernel (merge), ele deve passar por:

### 3.1. Validação Técnica
1.  **Testes:** O código inclui testes (RSpec/Minitest) cobrindo os cenários de sucesso e falha?
2.  **Linting:** O código segue o estilo do projeto (Rubocop para Ruby, ESLint para JS)?
3.  **Segurança:**
    *   Nenhum segredo (chaves de API) commitado.
    *   Validação de inputs (Strong Parameters).
    *   Verificação de permissões (Authorize) em todos os controllers.

### 3.2. Validação Arquitetural (O "Filtro Foton")
1.  **Isolamento:** O plugin quebra se o `foton_subscription_manager` não estiver instalado? (Não deveria, a menos que seja uma dependência explícita).
2.  **UI/UX:** O plugin funciona visualmente sem o tema `fotonOS`? (Deve ter fallback gracioso).
3.  **Performance:** Existem queries N+1? O uso de memória está controlado?

---

## 4. Pipeline de Release e Versionamento

### Versionamento Semântico (SemVer)
*   **Plugins:** `vX.Y.Z` (Ex: v1.2.0)
    *   `X` (Major): Quebra de compatibilidade (ex: requer nova versão do Redmine).
    *   `Y` (Minor): Nova funcionalidade compatível.
    *   `Z` (Patch): Correção de bug.

### Processo de Release
1.  Merge de `develop` para `main`.
2.  Tag no Git (`v1.0.0`).
3.  Geração de Changelog (automático via Conventional Commits).
4.  Build de Assets (se houver JS/CSS compilado).

---

## 5. Guia para o Colaborador

### 5.1. Quero contribuir com um Plugin Comunitário
1.  Leia o `CONTRIBUTING.md` do plugin específico.
2.  Garanta que seu ambiente Docker esteja rodando (`make setup`).
3.  Desenvolva sua feature isolada.
4.  Abra um PR descrevendo o valor gerado.

### 5.2. Quero reportar um Bug no Kernel
1.  Verifique se o bug é do Redmine original ou da camada Foton.
2.  Abra uma Issue no repositório principal com passos de reprodução.

---

## 6. Ferramentas de Apoio

*   **Docker Compose:** Orquestra todo o ambiente local.
*   **Makefiles:** Cada plugin possui um `Makefile` para facilitar instalação e testes.
    *   `make install`
    *   `make test`
