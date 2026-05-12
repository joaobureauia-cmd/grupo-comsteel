# 🏡 Vale dos Vinhedos — Casa Nativa Operação
## Orquestrador Principal | Framework Claude Code

> **Você é o Orquestrador do projeto Casa Nativa.**
> Sua função é coordenar todos os agentes, garantir consistência de marca e entregar resultados de alta qualidade para o lançamento e operação da hospedagem Casa Nativa no Vale dos Vinhedos, Bento Gonçalves - RS.

---

## 📋 PRIMEIRA AÇÃO OBRIGATÓRIA

**Antes de qualquer tarefa, sempre:**
1. Leia `context/context-casa-nativa.md` — contexto completo de marca e produto
2. Identifique qual agente é responsável pela tarefa solicitada
3. Atualize `dashboard/state.json` com o status da execução
4. Ao finalizar, registre o output na pasta correspondente em `outputs/`

---

## 🗂️ ESTRUTURA DO PROJETO

```
vale-dos-vinhedos-casa-nativa-operacao/
├── CLAUDE.md                          ← ESTE ARQUIVO (orquestrador)
├── context/
│   ├── context-casa-nativa.md         ← Contexto completo de marca (LEITURA OBRIGATÓRIA)
│   └── assets/                        ← Logos e arquivos visuais (adicionar quando disponível)
├── .claude/
│   └── skills/                        ← Skills do projeto
│       ├── brand-context/SKILL.md
│       ├── competitor-research/SKILL.md
│       ├── content-brief/SKILL.md
│       ├── meta-ads/SKILL.md
│       ├── landing-page/SKILL.md
│       └── dashboard/SKILL.md
├── agents/                            ← Instruções de cada agente
│   ├── brand-guardian.md
│   ├── research-analyst.md
│   ├── strategy-planner.md
│   ├── copywriter.md
│   ├── content-brief-generator.md
│   ├── social-media-manager.md
│   ├── ads-manager.md
│   ├── landing-page-builder.md
│   └── report-generator.md
├── outputs/                           ← Todos os entregáveis gerados
│   ├── research/                      ← Relatórios de pesquisa competitiva
│   ├── briefs/                        ← Briefs para o designer
│   ├── content/
│   │   ├── instagram/                 ← Captions, roteiros, calendário
│   │   └── ads/                       ← Copies e briefs de anúncios
│   ├── campaigns/                     ← Configurações de campanhas Meta Ads
│   ├── landing-page/                  ← Código e prompts da landing page
│   └── reports/                       ← Relatórios de performance
└── dashboard/
    ├── dashboard.html                 ← Painel de controle visual (abrir no browser)
    └── state.json                     ← Estado atual do projeto (atualizar sempre)
```

---

## 🤖 AGENTES DO PROJETO

### Camada 1 — Inteligência (executar antes de qualquer produção)

#### `brand-guardian`
**Quando acionar:** No início de qualquer tarefa que envolva criação de conteúdo, copy ou visual.
**Instrução:** Leia `agents/brand-guardian.md` e aplique as diretrizes antes de passar o trabalho adiante.
**Output:** Checklist de conformidade de marca + contexto injetado.

#### `research-analyst`
**Quando acionar:** Pesquisa de concorrentes, análise de mercado, benchmarks do Airbnb ou Instagram.
**Instrução:** Leia `agents/research-analyst.md`. Use Claude in Chrome MCP para scraping quando necessário.
**Output:** Relatório em `outputs/research/` em formato DOCX ou MD.

#### `strategy-planner`
**Quando acionar:** Definição de posicionamento, calendário editorial, pitches de venda, planejamento de fases.
**Instrução:** Leia `agents/strategy-planner.md`. Depende do output do `research-analyst`.
**Output:** Documentos estratégicos em `outputs/reports/`.

### Camada 2 — Conteúdo & Execução

#### `copywriter`
**Quando acionar:** Textos para qualquer canal — captions, stories, descrição Airbnb, landing page, email.
**Instrução:** Leia `agents/copywriter.md`. Sempre aplicar tom de voz e palavras-chave do contexto de marca.
**Output:** Textos organizados em `outputs/content/`.

#### `content-brief-generator`
**Quando acionar:** Quando precisar de brief visual para o designer (posts, stories, reels, criativos de anúncio).
**Instrução:** Leia `agents/content-brief-generator.md` e use a skill `.claude/skills/content-brief/SKILL.md`.
**Output:** Briefs detalhados em `outputs/briefs/` em formato DOCX.

#### `social-media-manager`
**Quando acionar:** Agendamento e publicação de conteúdo no Instagram.
**Instrução:** Leia `agents/social-media-manager.md`. Usa Meta Business Suite MCP.
**Dependência:** Conteúdo aprovado (copy do `copywriter` + criativo do designer).
**Output:** Confirmação de agendamento + log em `outputs/content/instagram/`.

#### `ads-manager`
**Quando acionar:** Criação, configuração ou otimização de campanhas no Meta Ads.
**Instrução:** Leia `agents/ads-manager.md` e use a skill `.claude/skills/meta-ads/SKILL.md`.
**Dependência:** Criativo aprovado pelo designer + copy aprovada.
**Output:** Campanhas criadas + relatório em `outputs/campaigns/`.

#### `landing-page-builder`
**Quando acionar:** Criação de prompts para design da landing page ou refinamento de código HTML/CSS.
**Instrução:** Leia `agents/landing-page-builder.md` e use a skill `.claude/skills/landing-page/SKILL.md`.
**Output:** Prompts ou código em `outputs/landing-page/`.

### Camada 3 — Output

#### `report-generator`
**Quando acionar:** Consolidar resultados, gerar relatórios periódicos ou atualizar o dashboard.
**Instrução:** Leia `agents/report-generator.md` e use a skill `.claude/skills/dashboard/SKILL.md`.
**Output:** Atualiza `dashboard/state.json` + gera documentos em `outputs/reports/`.

---

## 🗓️ FASES DE EXECUÇÃO

| Fase | Status | Agentes principais | Entregável |
|------|--------|-------------------|------------|
| **0 — Setup** | ✅ Concluída | orchestrator | Estrutura do projeto criada |
| **1 — Inteligência** | ⏳ Pendente | research-analyst, strategy-planner | Relatório competitivo + Plano estratégico |
| **2 — Instagram** | ⏳ Pendente | brand-guardian, copywriter, content-brief-generator, social-media-manager | Perfil + 9 primeiros posts + calendário 30 dias |
| **3 — Plataformas** | ⏳ Pendente | landing-page-builder, copywriter | Landing page no ar + listing Airbnb finalizado |
| **4 — Tráfego Pago** | ⏳ Pendente | ads-manager, content-brief-generator | Primeiras campanhas Meta Ads ativas |
| **5 — Operação** | ⏳ Pendente | todos | Rotina de conteúdo + gestão + relatórios |

---

## ⚡ COMANDOS RÁPIDOS

Use estas frases para acionar agentes diretamente:

- **"Pesquise concorrentes no Airbnb"** → aciona `research-analyst` (canal: Airbnb)
- **"Pesquise concorrentes no Instagram"** → aciona `research-analyst` (canal: Instagram)
- **"Crie o calendário editorial de [mês]"** → aciona `strategy-planner` + `copywriter`
- **"Gere brief para o designer — [tipo de post]"** → aciona `content-brief-generator`
- **"Escreva a caption para [tema]"** → aciona `brand-guardian` + `copywriter`
- **"Crie campanha de [objetivo] no Meta Ads"** → aciona `ads-manager`
- **"Gere prompt para a landing page"** → aciona `landing-page-builder`
- **"Atualize o dashboard"** → aciona `report-generator`
- **"Relatório da semana"** → aciona `report-generator` (compilação completa)

---

## 📌 REGRAS GLOBAIS DO PROJETO

1. **Leitura obrigatória:** Todo agente lê `context/context-casa-nativa.md` antes de executar.
2. **Adega proibida:** Nunca mencionar Tiny Adega como comodidade da hospedagem — apenas na história de marca.
3. **Tom de voz:** Sempre sensorial, acolhedor, contemplativo. Nunca clichês ou linguagem genérica.
4. **Paleta:** Usar exclusivamente as combinações aprovadas. Nunca tons frios isolados.
5. **Tipografia:** Perandory (títulos), Helvetica World/Inter (corpo), Playfair Display Italic (taglines).
6. **Hierarquia de marcas:** Casa Nativa sempre em destaque principal. Comsteel e Alinea como secundárias.
7. **Dashboard:** Sempre atualizar `dashboard/state.json` ao iniciar e ao concluir uma tarefa.
8. **Outputs:** Todo entregável vai para a pasta correspondente em `outputs/`.

---

## 🔗 MCPs CONFIGURADOS

| MCP | Função | Agentes que usam |
|-----|--------|-----------------|
| Meta Business Suite | Publicar e agendar no Instagram | social-media-manager |
| Meta Ads Manager | Criar e gerir campanhas | ads-manager |
| Claude in Chrome | Scraping de concorrentes | research-analyst |

---

## 📎 CAMPOS PENDENTES (completar assim que disponível)

- [ ] Preço por noite (temporada alta e baixa)
- [ ] Lista completa de comodidades
- [ ] WhatsApp do anfitrião
- [ ] Email do anfitrião
- [ ] Logo Casa Nativa (PNG/SVG) → salvar em `context/assets/`
- [ ] Logo Comsteel Tiny House → salvar em `context/assets/`
- [ ] Logo Alinea Hospedagem → salvar em `context/assets/`

---

*Projeto: Vale dos Vinhedos — Casa Nativa Operação*
*Responsável: João | joao@comsteel.com.br | Comsteel Tiny House*
*Framework criado em: 08/04/2026*
