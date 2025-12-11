# 🌌 Arquitetura do Ecossistema Foton

> **Visão Geral:** O Foton não é apenas um conjunto de plugins; é um Sistema Operacional para Construção Civil (RedmineOS) construído sobre um Kernel sólido.

Este documento define a arquitetura, os componentes e as fronteiras do ecossistema, servindo como a "Fonte da Verdade" técnica para o desenvolvimento.

---

## 1. O Conceito: Kernel e Módulos

Adotamos uma arquitetura **Híbrida Monolito-Modular** com características **Hexagonais**.

### 1.1. O Kernel (Redmine)
*   **Papel:** É o sistema operacional base. Fornece autenticação, banco de dados, roteamento e a estrutura de "Issues" e "Projetos".
*   **Diretriz de Ouro:** **Não modificamos o Kernel diretamente.** Todas as alterações de comportamento são feitas via *Patches*, *Hooks* ou *Engines* (Plugins), preservando a capacidade de atualização do Redmine upstream.

### 1.2. Módulos Comunitários (Plugins Open Source)
São as ferramentas funcionais entregues à comunidade. Devem operar de forma autônoma e agnóstica ao modelo de negócio SaaS.
*   **Exemplos:** `foton_contacts`, `foton_cash_flow`.
*   **Arquitetura:** Devem ser autocontidos. Se comunicam com outros módulos apenas via **Eventos (Pub/Sub)** ou interfaces de serviço públicas, nunca por acoplamento direto de banco de dados.

### 1.3. O Core de Sustentabilidade (SaaS Plugin)
*   **Plugin:** `foton_subscription_manager`.
*   **Papel:** É o "Orquestrador de Negócio". Ele transforma o Kernel em um SaaS Multi-tenant.
*   **Responsabilidades:**
    *   Gerenciar Assinaturas (Integração Mercado Pago).
    *   Impor Limites (Rate Limiting, Cotas de Projetos/Usuários).
    *   Gerenciar Workspaces (Tenants Lógicos).
*   **Restrição:** Este é o único componente que tem "consciência" de todos os outros, pois precisa controlá-los (habilitar/desabilitar features baseadas no plano).

### 1.4. A Interface (FotonOS)
*   **Componente:** Tema `fotonOS` + Injeções JS/CSS.
*   **Papel:** Camada de apresentação que unifica a experiência. Transforma a UI utilitária do Redmine em uma interface moderna e responsiva.
*   **Integração:** Atua como um "Decorador". O backend fornece a estrutura semântica (HTML); o FotonOS fornece a experiência visual.

---

## 2. Princípios de Engenharia

### 2.1. Arquitetura Hexagonal (Portas e Adaptadores)
Para garantir que o Kernel e os Plugins evoluam saudavelmente:
*   **Backend:** Lógica de negócio complexa reside em `Services` (Interactors), não em Controllers ou Models.
*   **Comunicação:** Plugins não chamam classes uns dos outros diretamente.
    *   *Errado:* `FotonContacts.create_invoice(...)`
    *   *Correto:* `ActiveSupport::Notifications.instrument('foton.contact.created', contact: contact)`

### 2.2. Frontend: CSS Sandbox e Design Tokens
*   **Isolamento:** Cada plugin deve "sandboxar" seus estilos para não quebrar o Kernel ou outros plugins.
    *   Uso de wrappers CSS: `.foton-contacts-app { ... }`.
*   **Coesão:** O tema `fotonOS` fornece **Design Tokens** (Variáveis CSS) que os plugins devem consumir para garantir consistência visual (cores, espaçamentos).

---

## 3. Estrutura de Diretórios (O Mapa do Território)

```
foton/
├── redmine/                  # O Kernel (Instância Dockerizada)
│   ├── plugins/
│   │   ├── foton_contacts/             # [Comunidade] CRM & Vínculos
│   │   ├── foton_cash_flow/            # [Comunidade] Financeiro
│   │   └── foton_subscription_manager/ # [SaaS Core] Gestão de Assinaturas/Tenants
│   └── themes/
│       └── fotonOS/                    # [Interface] Identidade Visual
├── docs/                     # Documentação Centralizada
│   ├── ARCHITECTURE.md       # Este arquivo
│   └── PIPELINES.md          # Fluxos de Trabalho e CI/CD
└── docker-compose.yml        # Orquestração da Infraestrutura
```

---

## 4. Decisões de Design (ADRs - Architecture Decision Records)

1.  **Workspaces como Projetos Raiz:**
    *   Decisão: Um "Tenant" no SaaS é tecnicamente um Projeto Raiz no Redmine.
    *   Motivo: Aproveita a hierarquia de permissões nativa do Kernel sem reinventar a roda.

2.  **Hotwire (Turbo + Stimulus) como Padrão de UI:**
    *   Decisão: Abandonar SPAs complexas (React/Vue) em favor do HTML-over-the-wire.
    *   Motivo: Reduz complexidade, melhora SEO e performance inicial, e alinha-se com a arquitetura Rails do Kernel.

3.  **SaaS como Plugin:**
    *   Decisão: O gerenciador de assinaturas é um plugin, não um fork do Redmine.
    *   Motivo: Permite atualizar o Kernel Redmine com segurança e facilita a distribuição dos plugins comunitários sem a lógica de cobrança.
