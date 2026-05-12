# 🚀 PROMPT DE ENTRADA — FASE 4: TRÁFEGO PAGO
## Cole este prompt no Claude Code ao iniciar a Fase 4

---

## 🖥️ Dashboard — manter aberto em paralelo
Se o servidor estiver parado, reinicie:
```bash
python3 -m http.server 8081
# Acesse no navegador:
http://localhost:8081/dashboard/dashboard.html
```

---

## 💬 Prompt — cole como primeira mensagem no Claude Code

```text
Você é o Orquestrador do projeto Vale dos Vinhedos — Casa Nativa Operação.

Antes de qualquer ação, leia o arquivo CLAUDE.md na raiz do projeto e o
arquivo context/context-casa-nativa.md na íntegra.

## CONTEXTO — FASES JÁ CONCLUÍDAS (terminal reiniciado)

As seguintes fases já foram concluídas com sucesso. NÃO re-execute nenhuma delas.
Apenas use seus outputs como insumo:

### Fase 0 — Setup ✅
- Estrutura do projeto criada
- Agentes, skills, context e dashboard configurados

### Fase 1 — Inteligência ✅
- Pesquisa competitiva Airbnb: outputs/research/2026-04-08_pesquisa-airbnb.md
- Pesquisa competitiva Instagram: outputs/research/2026-04-08_pesquisa-instagram.md
- Posicionamento de marca: outputs/reports/2026-04-08_posicionamento.md
- Pitches de venda: outputs/reports/2026-04-08_pitches-de-venda.md
- Calendário editorial 30 dias: outputs/reports/2026-04-08_calendario-editorial-abril-maio.md
- Hashtags estratégicas: outputs/reports/2026-04-08_hashtags.md

### Fase 2 — Instagram ✅
- Captions posts 10-22: outputs/campaigns/2026-04-08_posts-10-22-captions.md
- Briefs visuais de lançamento: outputs/briefs/2026-04-08_visual-briefs-launch.md
- Master setup Instagram: outputs/reports/2026-04-08_instagram-setup-master.md

### Fase 3 — Plataformas ✅
- Listing oficial Airbnb: outputs/platforms/2026-04-08_airbnb-listing.md
- Wireframe da landing page: outputs/platforms/2026-04-08_landing-page-wireframe.md
- Prompt vibe-coding para LP: outputs/platforms/vibe-coding-landing-page-prompt.json

---

## EXECUÇÃO — FASE 4: TRÁFEGO PAGO (Meta Ads)

Vamos executar a FASE 4 — TRÁFEGO PAGO completa.

Primeiro, corrija e atualize dashboard/state.json de imediato:
- fase_atual: "Fase 4 — Tráfego Pago"
- Nas "fases", garanta que:
  - Fases 0, 1, 2, 3: status "concluida"
  - Fase 4: status "em_andamento"
  - Fase 5: status "pending"
- tarefa_atual.numero: 1
- tarefa_atual.total: 4
- tarefa_atual.descricao: "Copies de Anúncios — Variações por objetivo"
- tarefa_atual.fase: "Fase 4 — Tráfego Pago"
- tarefa_atual.agente: "copywriter"
- status do agente copywriter: "running"
- Log: "Fase 4 iniciada. Copywriter criando copies para campanhas Meta Ads."

---

TAREFA 1 — copywriter + brand-guardian (Copies de Anúncios)
Leia agents/copywriter.md, agents/brand-guardian.md e a skill .claude/skills/meta-ads/SKILL.md.
Consulte os templates de copy da skill e o posicionamento da Fase 1
(outputs/reports/2026-04-08_posicionamento.md).
Consulte também os pitches de venda (outputs/reports/2026-04-08_pitches-de-venda.md).

Crie variações completas de copy para 3 tipos de campanha:

A) CAMPANHA DE AWARENESS (Reconhecimento de marca)
- 3 variações de Headline (máx 40 caracteres cada)
- 3 variações de Texto Principal (máx 125 caracteres cada)
- 1 versão longa para feed (até 300 caracteres)
- CTA recomendado
- Tom: emocional, sensorial, sem preço

B) CAMPANHA DE TRÁFEGO (Cliques para a Landing Page)
- 3 variações de Headline
- 3 variações de Texto Principal
- 1 versão longa para feed
- CTA recomendado
- Tom: benefício claro + convite à descoberta

C) CAMPANHA DE CONVERSÃO (Reservas diretas)
- 3 variações de Headline
- 3 variações de Texto Principal
- 1 versão longa para feed
- CTA recomendado
- Tom: urgência sutil + exclusividade + CTA direto

Para TODAS as copies, aplique validação do brand-guardian:
✅ Tom de voz: sensorial, acolhedor, contemplativo
✅ Palavras proibidas: genérico, clichê, barato, promoção
✅ Nunca mencionar Tiny Adega como comodidade
✅ Destaques obrigatórios: sauna privativa, design premiado, Vale dos Vinhedos

Salve em: outputs/campaigns/2026-04-09_ad-copies-meta.md

Atualize state.json:
- copywriter status: "completed"
- copywriter output: "outputs/campaigns/2026-04-09_ad-copies-meta.md"
- brand-guardian status: "completed" (validação feita)
- log: entrada de conclusão da Tarefa 1
- tarefa_atual.numero: 2
- tarefa_atual.descricao: "Briefs de Criativos para Anúncios"
- tarefa_atual.agente: "content-brief-generator"
- content-brief-generator status: "running"

---

TAREFA 2 — content-brief-generator (Briefs de Criativos para Ads)
Leia agents/content-brief-generator.md.
Use as copies da Tarefa 1 como base e crie briefs visuais detalhados
para os criativos de cada campanha.

Produza briefs para no mínimo 6 peças (2 por tipo de campanha):

Para cada peça criativa, forneça:
1. Tipo de campanha (Awareness / Tráfego / Conversão)
2. Formato (Feed estático / Carrossel / Stories / Reels)
3. Conceito visual central
4. Elementos obrigatórios na imagem/vídeo
5. Paleta de cores aplicada (terra, creme, areia, marrom)
6. Referência de mood/estética
7. Prompt Text-to-Image (Midjourney/DALL-E, em inglês)
8. Copy correspondente (headline + texto da Tarefa 1)
9. Dimensões recomendadas (1080x1080, 1080x1350, 1080x1920)

Salve em: outputs/briefs/2026-04-09_ad-creative-briefs.md

Atualize state.json:
- content-brief-generator status: "completed"
- content-brief-generator output: "outputs/briefs/2026-04-09_ad-creative-briefs.md"
- log: entrada de conclusão da Tarefa 2
- tarefa_atual.numero: 3
- tarefa_atual.descricao: "Estruturação das Campanhas Meta Ads"
- tarefa_atual.agente: "ads-manager"
- ads-manager status: "running"

---

TAREFA 3 — ads-manager (Estrutura Completa das Campanhas)
Leia agents/ads-manager.md e a skill .claude/skills/meta-ads/SKILL.md.
Consulte a pesquisa de concorrência (outputs/research/2026-04-08_pesquisa-airbnb.md)
para posicionamento de preço e público.

Crie a documentação técnica completa de 3 campanhas prontas para
ativação no Meta Ads Manager:

CAMPANHA 1 — AWARENESS (Casa Nativa — Conheça o Refúgio)
- Objetivo: Reconhecimento de marca
- Público: Interesse em enoturismo, viagens de luxo, casais, Serra Gaúcha, Airbnb
- Localização: Brasil (foco SP, RS, SC, PR, RJ)
- Idade: 25-55 anos
- Orçamento sugerido: diário e total (sugestão para 15 dias)
- Posicionamentos: Instagram Feed + Stories + Reels
- Criativos: referência aos briefs da Tarefa 2
- Copies: referência à Tarefa 1 (variações A)
- Métrica de sucesso: Alcance, CPM

CAMPANHA 2 — TRÁFEGO (Descubra a Casa Nativa)
- Objetivo: Tráfego para landing page
- Público: Interesse em hospedagem boutique, turismo gastronômico, wellness
- Público de remarketing: quem interagiu com Instagram
- URL de destino: [landing page — placeholder]
- Orçamento sugerido
- Posicionamentos: Instagram Feed + Stories + Facebook Feed
- Criativos: referência aos briefs da Tarefa 2
- Copies: referência à Tarefa 1 (variações B)
- Métrica de sucesso: CTR > 1,5%, CPC

CAMPANHA 3 — CONVERSÃO (Reserve sua Experiência)
- Objetivo: Conversão (reservas)
- Público: Lookalike 1-3% de quem interagiu + remarketing visitantes LP
- URL de destino: [landing page ou Airbnb — placeholder]
- Orçamento sugerido
- Posicionamentos: todos os placements relevantes
- Criativos: referência aos briefs da Tarefa 2
- Copies: referência à Tarefa 1 (variações C)
- Pixel/evento de conversão sugerido
- Métrica de sucesso: Custo por reserva, ROAS

Para cada campanha inclua:
- Hierarquia completa (Campanha > Conjunto de Anúncios > Anúncio)
- Configuração detalhada de segmentação
- Sugestões de teste A/B (ao menos 2 variáveis por campanha)
- Cronograma de ativação sugerido (sequência das 3 campanhas)
- Checklist de pré-lançamento (pixel instalado, UTMs, criativos aprovados)

Salve em: outputs/campaigns/2026-04-09_meta-ads-campaign-plan.md

Atualize state.json:
- ads-manager status: "completed"
- ads-manager output: "outputs/campaigns/2026-04-09_meta-ads-campaign-plan.md"
- log: entrada de conclusão da Tarefa 3
- tarefa_atual.numero: 4
- tarefa_atual.descricao: "Relatório consolidado de Tráfego Pago"
- tarefa_atual.agente: "report-generator"
- report-generator status: "running"

---

TAREFA 4 — report-generator (Consolidação e Dashboard)
Leia agents/report-generator.md.
Compile um relatório executivo da Fase 4 contendo:

1. Resumo das 3 campanhas criadas (objetivo, público, orçamento)
2. Mapa completo de copies e criativos (qual copy vai com qual criativo)
3. Cronograma de ativação recomendado (ordem de lançamento das campanhas)
4. Checklist final de itens pendentes para ir ao ar:
   - [ ] Criativos finalizados pelo designer
   - [ ] Pixel do Meta instalado na landing page
   - [ ] UTMs configuradas
   - [ ] Orçamento aprovado por João
   - [ ] Conta do Meta Ads autenticada
   - [ ] Landing page no ar com domínio final
5. KPIs alvo para os primeiros 30 dias
6. Plano de otimização semanal (quando pausar, escalar ou trocar criativos)

Salve em: outputs/reports/2026-04-09_relatorio-fase4-trafego-pago.md

Atualização CRÍTICA no state.json:
- report-generator status: "completed"
- report-generator output: "outputs/reports/2026-04-09_relatorio-fase4-trafego-pago.md"
- fase_4_entregaveis (criar esta CHAVE na raiz do state.json):
  {
    "ad_copies": "outputs/campaigns/2026-04-09_ad-copies-meta.md",
    "creative_briefs": "outputs/briefs/2026-04-09_ad-creative-briefs.md",
    "campaign_plan": "outputs/campaigns/2026-04-09_meta-ads-campaign-plan.md",
    "relatorio_fase4": "outputs/reports/2026-04-09_relatorio-fase4-trafego-pago.md"
  }
- Fase 4 da lista "fases": status = "concluida"
- Fase 5 da lista "fases": status = "em_andamento"
- fase_atual: "Fase 5 — Operação"
- log: adicione as entradas de conclusão da Tarefa 4 e da Fase 4 como um todo.

---

FINALIZAÇÃO
1. Cumpra todos os updates do arquivo state.json com total precisão.
2. Apresente no chat um resumo elegante da Fase 4 com:
   - Visão geral das 3 campanhas estruturadas
   - Investimento total sugerido para os primeiros 30 dias
   - Próximos passos para ativação real
   - Lista de todos os arquivos gerados com caminhos
3. Informe que os documentos podem ser visualizados no Painel Operacional (👁️ Ler).

Pode iniciar a orquestração!
```

---

## ✅ Checklist antes de executar

- [ ] Fases 1, 2 e 3 foram concluídas com sucesso
- [ ] As pastas `outputs/campaigns/`, `outputs/briefs/`, `outputs/reports/` e `outputs/platforms/` já contêm os artefatos das fases anteriores
- [ ] O dashboard mostra os dados atualizados das Fases 1, 2 e 3
- [ ] Entende-se que as campanhas serão PLANEJADAS e DOCUMENTADAS nesta fase — a ativação real no Meta Ads depende de: criativos finais, orçamento aprovado e conta autenticada
