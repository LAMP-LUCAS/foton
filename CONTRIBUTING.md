# Guia de Contribuição para o Projeto Foton

🎉 **Obrigado por considerar contribuir com o Foton!** 🎉  
Seguem as diretrizes para ajudar você a participar efetivamente do projeto.

---

## 🧭 Formas de Contribuir

### 1. Reportando Problemas
- Verifique se o problema já foi reportado nas [Issues](https://github.com/LAMP-LUCAS/foton/issues)
- Caso novo, crie uma issue com:
  - Título claro e descritivo
  - Descrição detalhada do problema
  - Passos para reprodução
  - Comportamento esperado vs. atual
  - Screenshots (se aplicável)

### 2. Sugerindo Melhorias
- Abra uma issue com o título **[SUGESTÃO]**
- Descreva:
  - O problema que a funcionalidade resolve
  - Como você imagina a solução
  - Alternativas consideradas

### 3. Submetendo Código
1. **Faça um fork** do repositório
2. **Crie um branch** com nome descritivo:
   ```bash
   git checkout -b feat/nome-da-feature
   # ou
   git checkout -b fix/nome-do-bug
   ```
3. **Siga os padrões**:
   - Documente seu código
   - Mantenha consistência de estilo
   - Adicione testes quando relevante
4. **Teste suas alterações**:
   ```bash
   docker-compose up --build -d
   ```
5. **Envie um Pull Request (PR)**:
   - Descreva as mudanças no template do PR
   - Referencie issues relacionadas (ex: `Resolve #123`)
   - Atualize a documentação se necessário

---

## ⚙️ Ambiente de Desenvolvimento

### Pré-requisitos
- Docker 20.10+
- Docker Compose 2.0+

### Configuração Inicial
```bash
git clone https://github.com/seu-usuario/foton.git
cd foton
cp .env.example .env  # Configure suas variáveis
docker-compose up -d
```

### Estrutura de Pastas

O respositório já está configurado como um template para ajuda-lo

```
foton/
┣ docker/           # Configurações Docker personalizadas
┣ docs/             # Documentação técnica
┣ redmine/          # Plugins e temas customizados
┣ scripts/          # Scripts de automação
┣ secrets/
┃ ┣ .secrets.example      # Template de variáveis e senhas
┗ docker-compose.yml
```

---

## 📜 Padrões de Código

### Backend (Python)
- Siga a PEP 8
- Use type hints
- Documente com docstrings
- Testes com pytest

### Commits
- Use [Conventional Commits](https://www.conventionalcommits.org):
  ```
  feat: Adiciona suporte ao SINAPI-2025
  fix: Corrige timeout na sincronização
  docs: Atualiza guia de instalação
  ```

---

## 🤝 Código de Conduta
Seguimos o [Contributor Covenant](https://www.contributor-covenant.org).  
Comportamentos inadequados podem ser reportados para lucas@arqlamp.com.

---

## 🎁 Reconhecimento
Todo contribuidor será:
- Listado na nossa [página de agradecimentos](https://mundoaec.com/contributors)
- Convidado para eventos exclusivos
- Elegível para brindes especiais

[👉 Voltar ao README](README.md)
