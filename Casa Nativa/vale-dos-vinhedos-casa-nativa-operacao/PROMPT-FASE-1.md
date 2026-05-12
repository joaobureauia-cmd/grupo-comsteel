# 🚀 PROMPT DE ENTRADA — FASE 1: INTELIGÊNCIA
## Cole este prompt no Claude Code ao iniciar a Fase 1

---

## ⚙️ PRÉ-REQUISITO — instalar Playwright MCP (só na primeira vez)

```bash
# 1. Verificar Node.js
node -v
# Se não tiver: brew install node

# 2. Adicionar Playwright MCP ao Claude Code
claude mcp add playwright -- npx -y @playwright/mcp@latest

# 3. Confirmar que foi adicionado
claude mcp list
# Deve aparecer: playwright

# 4. Entrar na pasta do projeto e iniciar
cd vale-dos-vinhedos-casa-nativa-operacao
claude
```

---

## 🖥️ Dashboard — abrir em paralelo

```bash
# Em outra aba do terminal:
cd vale-dos-vinhedos-casa-nativa-operacao/dashboard
python3 -m http.server 8080
# Abrir no browser: http://localhost:8080/dashboard.html
```

---

## 💬 Prompt — cole como primeira mensagem no Claude Code

```
Você é o Orquestrador do projeto Vale dos Vinhedos — Casa Nativa Operação.

Antes de qualquer ação, leia o arquivo CLAUDE.md na raiz do projeto e o
arquivo context/context-casa-nativa.md na íntegra.

Você tem acesso ao Playwright MCP para controle de browser. Use-o para
toda navegação e coleta de dados nesta fase.

Vamos executar a FASE 1 — INTELIGÊNCIA completa.

Atualize dashboard/state.json:
- fase_atual: "Fase 1 — Inteligência"
- Fase 1 status: "em_andamento"
- tarefa_atual.numero: 1, total: 3
- tarefa_atual.descricao: "Pesquisa competitiva Airbnb"
- research-analyst status: "running"

---

TAREFA 1 — research-analyst (Airbnb)
Leia agents/research-analyst.md e execute a skill
.claude/skills/competitor-research/SKILL.md para o canal Airbnb.

Use o Playwright MCP para navegar em airbnb.com.br.
Pesquise hospedagens com os seguintes termos em sequência:
- "Garibaldi RS" (2 hóspedes, qualquer tipo)
- "Vale dos Vinhedos" (2 hóspedes)
- "Serra Gaúcha sauna" (2 hóspedes)
- "Garibaldi tiny house"

Para cada hospedagem encontrada (top 10 mais relevantes) colete:
nome, preço por noite, nota média, número de avaliações, comodidades
listadas, diferenciais na descrição, estilo visual das fotos.

Relatório final com:
1. Tabela comparativa dos 10 concorrentes
2. Faixa de preço do mercado (mínimo / médio / máximo)
3. Comodidades mais comuns (benchmark para Casa Nativa)
4. Lacunas onde Casa Nativa pode se diferenciar (especialmente sauna)
5. Recomendações para o listing da Casa Nativa

Salve em: outputs/research/2026-04-08_pesquisa-airbnb.md

Atualize state.json:
- research-analyst output: "outputs/research/2026-04-08_pesquisa-airbnb.md"
- tarefa_atual.numero: 2
- tarefa_atual.descricao: "Pesquisa competitiva Instagram"
- log: entrada de conclusão da Tarefa 1

---

TAREFA 2 — research-analyst (Instagram)
Leia agents/research-analyst.md e execute a skill
.claude/skills/competitor-research/SKILL.md para o canal Instagram.

Use o Playwright MCP para navegar em instagram.com.
Pesquise por:
- Hashtags: #valedosvinhedos #garibaldirs #hospedagemserraguacha
  #casasdetemporada #tinyhouse #enoturismo #serragaucha
- Identifique perfis de hospedagens/pousadas com 500–50.000 seguidores
  na Serra Gaúcha

Para cada perfil (top 8) colete: handle (@), seguidores, frequência
de postagem, formatos predominantes, tom de voz, posts com maior
engajamento, hashtags usadas, CTA principal.

Relatório final com:
1. Tabela comparativa dos 8 perfis
2. Formatos com maior engajamento no nicho
3. Top 30 hashtags estratégicas organizadas por categoria
4. Frequência ideal de postagem
5. Oportunidades de diferenciação visual para a Casa Nativa

Salve em: outputs/research/2026-04-08_pesquisa-instagram.md

Atualize state.json:
- tarefa_atual.numero: 3
- tarefa_atual.descricao: "Strategy Planner — posicionamento e calendário"
- strategy-planner status: "running"
- log: entrada de conclusão da Tarefa 2

---

TAREFA 3 — strategy-planner
Leia agents/strategy-planner.md.

ATENÇÃO: O context/context-casa-nativa.md já contém os 9 posts de
lançamento aprovados pelo designer e a bio oficial do Instagram.
Use estes como base — não recriar, apenas incorporar no calendário.

Com base nos relatórios de pesquisa, produza:

A) PLANO DE POSICIONAMENTO
- Confirmação ou refinamento da Proposta Única de Valor
- Argumentos de diferenciação frente aos concorrentes encontrados
- 3 pilares de comunicação da Casa Nativa

B) PITCHES DE VENDA
- Pitch para DM do Instagram (resposta a consultas)
- Título do listing Airbnb (máx. 50 caracteres)
- Abertura da descrição Airbnb (primeiro parágrafo, sensorial)
- Resposta padrão para Google Meu Negócio (avaliações)

C) CALENDÁRIO EDITORIAL — PRIMEIROS 30 DIAS
Tabela com 30 entradas:
Data | Formato | Tema | Objetivo | Copy resumida | Visual sugerido
- Posts 1–9: usar as captions já aprovadas do branding book
- Posts 10–30: criar com base na pesquisa e estratégia
- Distribuição: 40% branding, 30% experiência, 20% localização, 10% conversão

D) TOP 30 HASHTAGS FINAIS
Organizadas em 3 grupos: nicho premium | localização | lifestyle/wellness

Salve:
- outputs/reports/2026-04-08_posicionamento.md
- outputs/reports/2026-04-08_pitches-de-venda.md
- outputs/reports/2026-04-08_calendario-editorial-abril-maio.md
- outputs/reports/2026-04-08_hashtags.md

---

FINALIZAÇÃO
1. Atualize dashboard/state.json:
   - Fase 1 status: "concluida"
   - Fase 2 status: "em_andamento"
   - fase_atual: "Fase 2 — Instagram"
   - Todos os agentes usados: status "completed" com output preenchido
   - tarefa_atual: próxima tarefa da Fase 2
   - Log: entradas de conclusão de cada tarefa e da fase

2. Apresente resumo com:
   - Principais insights dos concorrentes
   - Posicionamento final recomendado
   - Lista de todos os arquivos gerados com caminhos

Podemos começar.
```

---

## ✅ Checklist antes de executar

- [ ] `node -v` retorna versão instalada
- [ ] `claude mcp list` mostra `playwright`
- [ ] Está na pasta `vale-dos-vinhedos-casa-nativa-operacao`
- [ ] Dashboard aberto em `http://localhost:8080/dashboard.html`
- [ ] Modelo configurado: **MiniMax M2.7** (ou Sonnet para melhor qualidade)
