# **Foton**  
## Controle Integrado de Informações para Construção Civil  

![License: GPLv3](https://img.shields.io/badge/License-GPLv3-blue) ![Docker](https://img.shields.io/badge/Docker-Compose-2496ED) ![Redmine](https://img.shields.io/badge/Redmine-6.0-red) ![OpenSource](https://img.shields.io/badge/Open_Source-✓-brightgreen)  

---

## **🚀 Revolucione Sua Gestão de Obras**  

O **Foton** é um ecossistema integrado que transforma como arquitetos e engenheiros gerenciam informações em projetos de construção. Combinamos:  

- **Gestão de projetos** (Redmine)  
- **Automação inteligente** (n8n + Ferramentas e APIs)  
- **Assistência especializada** (OpenWebUI)  
- **Dados SINAPI em tempo real** (autoSINAPI)  

**Para quem é:**  
🏗️ Construtoras • 📐 Escritórios de Arquitetura • 🧮 Orçamentistas • 👷‍♂️ Gestores de Obra

**Nosso Valor Principal**:  
>> Capacitar profissionais a operarem todos os departamentos de um escritório usando ferramentas open-source integradas, com opções de suporte premium para quem precisa de mais recursos.

**Quanto tenho que pagar?**

O Foton é uma metodologia OpenSource, utilizamos ferramentas OpenSource ou Gratuítas em um fluxo estruturado, portanto você pode utiliza-las gratuítamente. Os planos e serviços que temos são referentes à hospedagens e serviços extras. Veja abaixo:

<div align="center" style="margin: 40px 0;">

  <a href="#-para-usuários-finais">
      <img src="https://img.shields.io/badge/QUERO_SABER_MAIS:-PLANOS_E_SERVIÇOS-FF6F61?style=for-the-badge&logo=git&logoColor=white" alt="Botão para Usuários Finais">
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
| [autoSINAPI](https://github.com/LAMP-LUCAS/AutoSINAPI) | ✅ Produtivo | [Repositório](https://github.com/LAMP-LUCAS/AutoSINAPI) |  
| sincSINAPI | 🚧 Em desenvolvimento | - |  
| orcSINAPI | 🚧 Em desenvolvimento | - |  
| ifcSINAPI | 🚧 Em desenvolvimento | - |  

---

### **🌱 Participe da Comunidade**  
1. Reporte bugs nas [Issues](https://github.com/LAMP-LUCAS/foton/issues)  
2. Acompanhe o nosso [Fórum Técnico](https://comunidade.mundoaec.com)  
3. Siga nosso [Guia de Contribuição](CONTRIBUTING.md)
4. Venha tomar um café na nossa [Comunidade](https://comunidade.mundoaec.com/coffee)  

**Próximos passos técnicos:**  
- [ ] Finalizar integração Redmine-OpenWebUI
- [ ] Desenvolver API para sincSINAPI  
- [ ] Implementar sistema de créditos  

---

## **👤 Para Usuários Finais**  

### **💡 Soluções Prontas para Sua Empresa**  

| Plano | Benefícios | Investimento |  
|-------|------------|--------------|  
|**✅Free**|• Acesso à Comunidade<br>•Surpresinhas mensais<br>•Grupo de estudo comunitário<br>•E muito mais!| Grátis |
| **💻 Econômico** | • Comunidade com acessos exclusívos<br>• 50 créditos/mês (IA)<br>• Wiki e fóruns | R$10 (individual)<br>R$25 (equipe) |  
| **🚀 Tipo** | • Redmine na nuvem (1GB)<br>• Cursos básicos<br>• 200 créditos IA | R$50 (individual)<br>R$150 (equipe) |  
| **🏆 Penthouse** | • Redmine premium (10GB)<br>• Todos cursos<br>• Suporte 24h | R$200 (individual)<br>R$1000 (equipe) |  

<div align="center" style="margin: 30px 0;">
  <a href="https://mundoaec.com/assinatura">
    <img src="https://img.shields.io/badge/EXPERIMENTE_GRÁTIS-30_DIAS-DD0031?style=for-the-badge&logo=openaccess&logoColor=white" alt="Teste Grátis">
  </a>
</div>

### **🎓 Conteúdo Exclusivo**  
- **Cursos Práticos:**  
  » Orçamento com SINAPI  
  » Fluxos BIM no Redmine  
  » Automação com n8n  
- **Bibliotecas Premium:**  
  » 200+ famílias RVT prontas  
  » Templates de projetos  
  » Coleção de materiais SINAPI  

### **📋 Detalhes dos Planos**  
| Recurso | Econômico | Tipo | Penthouse |  
|---------|-----------|------|----------|  
| Armazenamento | - | 1GB | 10GB |  
| Créditos OpenWebUI | 50/mês | 200/mês | Ilimitado |  
| Cursos Inclusos | 3 básicos | 10+ | Todos |  
| Suporte | Comunitário | E-mail | 24h prioritário |  
| Acesso | [Assinar](https://mundoaec.com/assinatura/#economico) | [Assinar](https://mundoaec.com/assinatura/#tipo) | [Solicitar](https://mundoaec.com/assinatura/#penthouse) |  

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
💬 **Comunidade:** [Forum Foton](https://comunidade.mundoaec.com)  

---

**Tecnologias Utilizadas:**  

    [Obsidian] + [Redmine]
       [n8n]   + [OpenWebUI]
    [Maritalk] + [DeepSeek]

**Créditos:** IBGE • Redmine • Comunidade Open-Source • E logo logo à Você!
