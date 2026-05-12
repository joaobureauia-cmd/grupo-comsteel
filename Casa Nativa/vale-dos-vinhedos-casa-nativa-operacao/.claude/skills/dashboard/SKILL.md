# Skill: html-dashboard-output
## Dashboard de Acompanhamento em Tempo Real — Casa Nativa

### Quando usar esta skill
Use quando `report-generator` precisar atualizar o painel de controle do projeto ou
quando o orquestrador iniciar/concluir qualquer tarefa.

---

### Como funciona o Dashboard

O dashboard é um arquivo `dashboard/dashboard.html` que você abre no browser.
Ele lê o arquivo `dashboard/state.json` a cada 3 segundos e exibe o estado atual do projeto.

**Para atualizar o dashboard:**
1. Edite `dashboard/state.json` com o novo estado
2. O `dashboard.html` atualiza automaticamente no browser

---

### Estrutura do state.json

```json
{
  "projeto": "Vale dos Vinhedos — Casa Nativa Operação",
  "ultima_atualizacao": "AAAA-MM-DDTHH:MM:SS",
  "fase_atual": "Fase 0 — Setup",
  "fases": [
    {
      "id": 0,
      "nome": "Setup",
      "status": "concluida",
      "entregavel": "Estrutura do projeto criada"
    },
    {
      "id": 1,
      "nome": "Inteligência",
      "status": "pendente",
      "entregavel": "Relatório competitivo + Plano estratégico"
    },
    {
      "id": 2,
      "nome": "Instagram",
      "status": "pendente",
      "entregavel": "Perfil + 9 posts + calendário 30 dias"
    },
    {
      "id": 3,
      "nome": "Plataformas",
      "status": "pendente",
      "entregavel": "Landing page + Listing Airbnb"
    },
    {
      "id": 4,
      "nome": "Tráfego Pago",
      "status": "pendente",
      "entregavel": "Campanhas Meta Ads ativas"
    },
    {
      "id": 5,
      "nome": "Operação",
      "status": "pendente",
      "entregavel": "Rotina contínua"
    }
  ],
  "agentes": [
    {"nome": "brand-guardian", "status": "idle", "ultima_tarefa": "", "output": ""},
    {"nome": "research-analyst", "status": "idle", "ultima_tarefa": "", "output": ""},
    {"nome": "strategy-planner", "status": "idle", "ultima_tarefa": "", "output": ""},
    {"nome": "copywriter", "status": "idle", "ultima_tarefa": "", "output": ""},
    {"nome": "content-brief-generator", "status": "idle", "ultima_tarefa": "", "output": ""},
    {"nome": "social-media-manager", "status": "idle", "ultima_tarefa": "", "output": ""},
    {"nome": "ads-manager", "status": "idle", "ultima_tarefa": "", "output": ""},
    {"nome": "landing-page-builder", "status": "idle", "ultima_tarefa": "", "output": ""},
    {"nome": "report-generator", "status": "idle", "ultima_tarefa": "", "output": ""}
  ],
  "log": [],
  "pendencias": [
    "Preço por noite (temporada alta e baixa)",
    "Lista completa de comodidades",
    "WhatsApp do anfitrião",
    "Email do anfitrião",
    "Logo Casa Nativa (PNG/SVG)",
    "Logo Comsteel Tiny House",
    "Logo Alinea Hospedagem"
  ]
}
```

**Status possíveis para agentes:** `idle` | `running` | `completed` | `error`
**Status possíveis para fases:** `pendente` | `em_andamento` | `concluida`

---

### Como atualizar o state.json durante uma tarefa

**Ao iniciar uma tarefa:**
```json
// 1. Atualizar tarefa_atual com descrição detalhada
"tarefa_atual": {
  "fase": "Fase 1 — Inteligência",
  "numero": 1,
  "total": 3,
  "descricao": "Pesquisa competitiva Airbnb — top 10 concorrentes em Bento Gonçalves",
  "agente": "research-analyst",
  "detalhe": "Navegando airbnb.com.br via Claude in Chrome MCP"
}
// 2. Mudar status do agente para "running"
"agentes": [
  {"nome": "research-analyst", "status": "running", "ultima_tarefa": "Pesquisa competitiva Airbnb — top 10 concorrentes", "output": ""}
]
// 3. Adicionar entrada no log com timestamp real
"log": [
  {"timestamp": "2026-04-08T10:30:00", "agente": "research-analyst", "acao": "Tarefa 1/3 iniciada — Pesquisa Airbnb via Claude in Chrome"}
]
```

**Ao concluir uma tarefa:**
```json
// 1. Atualizar tarefa_atual para a próxima tarefa (ou limpar se fase concluída)
"tarefa_atual": {
  "fase": "Fase 1 — Inteligência",
  "numero": 2,
  "total": 3,
  "descricao": "Pesquisa competitiva Instagram — top 8 perfis da Serra Gaúcha",
  "agente": "research-analyst",
  "detalhe": "Navegando instagram.com via Claude in Chrome MCP"
}
// 2. Mudar status do agente para "completed" com output
"agentes": [
  {"nome": "research-analyst", "status": "completed", "ultima_tarefa": "Pesquisa Airbnb concluída", "output": "outputs/research/2026-04-08_pesquisa-airbnb.md"}
]
// 3. Adicionar entrada no log
"log": [
  {"timestamp": "2026-04-08T11:15:00", "agente": "research-analyst", "acao": "Tarefa 1/3 concluída — relatório salvo: outputs/research/2026-04-08_pesquisa-airbnb.md"}
]
```

**Regra de granularidade:**
- `tarefa_atual.descricao` → o que está fazendo AGORA (frase curta, objetiva)
- `tarefa_atual.detalhe` → contexto adicional (ferramenta usada, URL acessada, etc.)
- `tarefa_atual.numero` / `tarefa_atual.total` → posição dentro da fase (ex: 2 de 3)
- `agentes[x].ultima_tarefa` → descrição curta da tarefa do agente
- `agentes[x].output` → caminho do arquivo gerado (preencher só ao concluir)
