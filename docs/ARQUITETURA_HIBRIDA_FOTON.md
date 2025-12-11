# Arquitetura do Ecossistema Foton: Híbrido Monolito-Modular e Hexagonal

## 1. Visão Conceitual

O objetivo deste documento é definir a arquitetura alvo para o ecossistema de plugins Foton no Redmine. O sistema deve operar sob um modelo **Híbrido**:

1.  **Monolito-Modular (O Hospedeiro):** O Redmine atua como o monolito. Os plugins (`foton_contacts`, `foton_cash_flow`, `foton_subscription_manager`) são módulos que residem dentro dele, mas devem manter fronteiras rígidas.
2.  **Arquitetura Hexagonal (Portas e Adaptadores):** Para garantir que os plugins funcionem isoladamente E em conjunto, a comunicação deve ocorrer através de contratos claros (Interfaces, Eventos, Design Tokens), e não através de acoplamento direto ou modificação global.

### Princípio da Versatilidade
> "Um plugin deve ser completo em si mesmo (funcionar isolado), mas capaz de se expandir quando em presença de aliados (Outros Plugins ou Tema FotonOS)."

---

## 2. Estratégia Frontend: "Sandbox e Design Tokens"

Para resolver o dilema de funcionar com ou sem o tema FotonOS sem quebrar o layout, adotaremos a seguinte estratégia:

### 2.1. Isolamento de CSS (CSS Sandboxing)
*   **Proibido:** Estilos globais (ex: `body { ... }`, `a { ... }`, `.btn { ... }`) dentro de plugins.
*   **Obrigatório:** Todo o HTML de um plugin deve viver dentro de um *wrapper* com ID ou Classe única (ex: `.foton-contacts-wrapper`).
*   **Implementação:** O CSS (incluindo frameworks como Bootstrap) deve ser aninhado ou compilado para atuar apenas dentro desse *wrapper*.

### 2.2. Design Tokens (Variáveis CSS)
A "cola" entre o Tema FotonOS e os Plugins não será JavaScript, mas sim Variáveis CSS.

*   **O Contrato:** Os plugins usam variáveis para cores e espaçamentos.
    *   Exemplo no Plugin: `color: var(--foton-primary-color, #0052cc);`
*   **Sem Tema:** O plugin define o valor *fallback* (ex: o azul padrão do Redmine).
*   **Com Tema FotonOS:** O tema define `:root { --foton-primary-color: #ff5722; }` e o plugin herda automaticamente a nova identidade visual.

### 2.3. FotonOS como Decorador
O tema deve abandonar a manipulação pesada de DOM via JavaScript (que causa *race conditions* com o Hotwire/Turbo). Ele deve focar em fornecer os *Design Tokens* e sobrescrever templates `.erb` específicos do Redmine quando necessário, em vez de mover `divs` após o carregamento da página.

---

## 3. Estratégia Backend: Desacoplamento

### 3.1. Comunicação via Eventos (Pub/Sub)
*   Em vez de `FotonContacts` chamar `FotonCashFlow.create_entry(...)`, ele deve publicar um evento: `ActiveSupport::Notifications.instrument('foton.issue.paid', issue: @issue)`.
*   O `FotonCashFlow` assina esse evento. Se ele não estiver instalado, o evento ocorre no vazio e nada quebra.

### 3.2. Interfaces de Serviço (Boundaries)
*   Lógica de negócio complexa deve viver em *Service Objects* isolados, não nos *Controllers* ou *Models* que herdam diretamente do Redmine.

---

## 4. Plano de Trabalho (Workplan) de Transição

### Fase 1: Isolamento Frontend (CSS Sandbox)
- [ ] **Foton Contacts:** Envolver todas as views em um container `.foton-contacts-app`.
- [ ] **Foton Contacts:** Refatorar `contacts.css` e `bootstrap.min.css` para aplicar estilos apenas dentro de `.foton-contacts-app`.
- [ ] **Foton Cash Flow:** Prefixar regras CSS (ex: `.tabular` -> `.foton-cash-flow .tabular`) para evitar quebra de layout global (Já iniciado).
- [ ] **FotonOS:** Criar arquivo `tokens.css` definindo a paleta de cores e tipografia via variáveis CSS.

### Fase 2: Adoção de Design Tokens
- [ ] **Todos os Plugins:** Substituir cores *hardcoded* (hexadecimais) por `var(--foton-token, fallback)`.
- [ ] **FotonOS:** Remover scripts JS que alteram cores via estilo inline.

### Fase 3: Refatoração do Tema FotonOS
- [ ] Eliminar dependência de `$(document).ready` para layout estrutural.
- [ ] Migrar posicionamento de Sidebar/Header para CSS Grid ou sobrescrita de template `base.html.erb`.

### Fase 4: Integração Hexagonal Backend
- [ ] Mapear pontos de integração direta entre plugins.
- [ ] Implementar camada de Eventos (`ActiveSupport::Notifications`) para substituir chamadas diretas.
- [ ] Padronizar `CONTRIBUTING.md` para exigir o cumprimento destas regras arquiteturais.

---

## 5. Checklist de Validação (DoD - Definition of Done)
1.  [ ] O plugin funciona e mantém seu estilo visual com o tema padrão do Redmine?
2.  [ ] O plugin "veste" as cores do FotonOS automaticamente quando o tema é ativado?
3.  [ ] O plugin NÃO altera a fonte, cor de fundo ou botões de páginas fora do seu escopo?
4.  [ ] O plugin não gera erros 500 se outro plugin do ecossistema for desinstalado?
