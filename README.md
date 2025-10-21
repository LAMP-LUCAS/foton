# **Foton**  
## Controle Integrado de Informações para Construção Civil  

![License: GPLv3](https://img.shields.io/badge/License-GPLv3-blue) ![Docker](https://img.shields.io/badge/Docker-Compose-2496ED) ![Redmine](https://img.shields.io/badge/Redmine-6.0-red) ![OpenSource](https://img.shields.io/badge/Open_Source-✓-brightgreen)  

---

## **🚀 Revolucione Sua Gestão de Obras**  

O **Foton** é um ecossistema integrado que transforma como arquitetos e engenheiros gerenciam informações em projetos de construção. Combinamos:  

- **Gestão de projetos** (Redmine + Plugins)  
- **Automação inteligente** (n8n + Ferramentas e APIs)  
- **Assistência especializada** (OpenWebUI)  
- **Dados SINAPI em tempo real** (autoSINAPI)  

**Para quem é:**  
🏗️ Construtoras • 📐 Escritórios de Arquitetura • 🧮 Orçamentistas • 👷‍♂️ Gestores de Obra

**Nosso Valor Principal**:  
>> Capacitar profissionais a operarem todos os departamentos de um escritório usando ferramentas open-source integradas de maneira simples e fluída.

**Quanto tenho que pagar?**

O Foton é uma ecossistema OpenSource, utilizamos ferramentas OpenSource ou Gratuítas em um fluxo estruturado, portanto você pode utiliza-las [GRATUITAMENTE!](https://mundoaec.com/foton/)

Os planos e serviços que temos são referentes à hospedagens e serviços extras. Veja abaixo:

<div align="center" style="margin: 40px 0;">
  <a href="https://mundoaec.com/foton/">
      <img src="https://img.shields.io/badge/QUERO_SABER_MAIS:-PLANOS_E_SERVIÇOS-FF6F61?style=for-the-badge&logo=git&logoColor=white" alt="PLANOS E SERVIÇOS">
  </a>
</div>

## **👨‍💻 Para Desenvolvedores**  

### **⚙️ Arquitetura Técnica**  

```yaml
services:
  postgres:          # Banco de dados unificado
  redmine:           # Gestão de projetos (http://localhost:3000)
  n8n:               # Automações com WAHA (WhatsApp)
  searxng:           # Busca unificada
  openwebui:         # Assistentes BIM/SINAPI
  obsidian:          # Documentação colaborativa
```

### **🛠️ Comece Agora!**

```bash
git clone https://github.com/seu-usuario/foton.git
cd foton
cp .env.example .env
docker-compose up -d
```

**Acesse localmente:**

- Redmine: http://localhost:3000  
- n8n: http://localhost:5678  
- OpenWebUI: http://localhost:8080  

### **🧩 Módulos Chave**

| Módulo | Status | Link |  
|--------|--------|------|
| Redmine + Plugins | ✅ Produtivo | [RedminePlugins](https://mundoaec.com/foton) |  
| Ferramentas Web | ✅ Produtivo | [Ferramentas Web](https://mundoaec.com/tools/) |  
| Assistente Virtual | 🚧 Em desenvolvimento | [OpenWebUI](https://chat.mundoaec.com/) |  
| autoSINAPI | ✅ Produtivo | [Repositório](https://github.com/LAMP-LUCAS/AutoSINAPI) |

---

### **🌱 Participe da Comunidade**

1. Reporte bugs nas [Issues](https://github.com/LAMP-LUCAS/foton/issues)
2. Acompanhe o nosso [Fórum Técnico](https://comunidade.mundoaec.com/projects/foton/boards/2)  
3. Siga nosso [Guia de Contribuição](CONTRIBUTING.md)
4. Venha tomar um café na nossa [Comunidade](https://comunidade.mundoaec.com/projects/foton/boards/1)  

**Próximos passos técnicos:**

- [ ] Finalizar integração Redmine-OpenWebUI
- [ ] Desenvolver API para sincSINAPI  
- [ ] Implementar sistema de créditos  

---

## **📜 Licenciamento**

- **Núcleo:** [GPLv3](LICENSE)  
- **Conteúdo:** Copyright © Foton  
- **Dados SINAPI:** Licença aberta (IBGE)  

```
Este programa é software livre: você pode redistribuí-lo e/ou modificar
sob os termos da GNU General Public License conforme publicada pela
Free Software Foundation, versão 3 da Licença.
```

## **📞 Contato**

✉️ **Suporte:** lucas@arqlamp.com  
🌐 **Site:** [https://mundoaec.com](https://mundoaec.com)  
💬 **Comunidade:** [Forum Foton](https://comunidade.mundoaec.com/projects/foton/boards/1)  

---

**Tecnologias Utilizadas:**  

    [Obsidian] + [Redmine]
       [n8n]   + [OpenWebUI]
    [Maritalk] + [DeepSeek]

**Créditos:** IBGE • Redmine • Comunidade Open-Source • E logo logo à Você!
