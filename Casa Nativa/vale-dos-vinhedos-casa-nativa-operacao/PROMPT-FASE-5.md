# 🚀 PROMPT DE ENTRADA — FASE 5: OPERAÇÃO CONTÍNUA
## Cole este prompt no Claude Code ao iniciar a Fase 5

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

## CONTEXTO — TODAS AS FASES ANTERIORES CONCLUÍDAS (terminal reiniciado)

As Fases 0 a 4 já foram concluídas com sucesso. NÃO re-execute nenhuma delas.
Use seus outputs como insumo para a operação contínua.

### Fase 0 — Setup ✅
- Estrutura do projeto, agentes, skills e dashboard configurados

### Fase 1 — Inteligência ✅
- outputs/research/2026-04-08_pesquisa-airbnb.md
- outputs/research/2026-04-08_pesquisa-instagram.md
- outputs/reports/2026-04-08_posicionamento.md
- outputs/reports/2026-04-08_pitches-de-venda.md
- outputs/reports/2026-04-08_calendario-editorial-abril-maio.md
- outputs/reports/2026-04-08_hashtags.md

### Fase 2 — Instagram ✅
- outputs/campaigns/2026-04-08_posts-10-22-captions.md
- outputs/briefs/2026-04-08_visual-briefs-launch.md
- outputs/reports/2026-04-08_instagram-setup-master.md

### Fase 3 — Plataformas ✅
- outputs/platforms/2026-04-08_airbnb-listing.md
- outputs/platforms/2026-04-08_landing-page-wireframe.md
- outputs/platforms/vibe-coding-landing-page-prompt.json
- outputs/landing-page/index.html

### Fase 4 — Tráfego Pago ✅
- outputs/campaigns/2026-04-09_ad-copies-meta.md
- outputs/briefs/2026-04-09_ad-creative-briefs.md
- outputs/campaigns/2026-04-09_meta-ads-campaign-plan.md
- outputs/reports/2026-04-09_relatorio-fase4-trafego-pago.md

---

## EXECUÇÃO — FASE 5: OPERAÇÃO CONTÍNUA

A Fase 5 é diferente das anteriores. Não é uma fase com fim definido — é o
MODO OPERACIONAL PERMANENTE da Casa Nativa. A partir de agora, o projeto
entra em rotina de produção contínua de conteúdo, gestão de campanhas e
análise de performance.

Atualize dashboard/state.json:
- fase_atual: "Fase 5 — Operação"
- Todas as fases 0-4: status "concluida"
- Fase 5: status "em_andamento"
- tarefa_atual.numero: 1
- tarefa_atual.total: 5
- tarefa_atual.descricao: "Auditoria Geral e Inventário de Ativos"
- tarefa_atual.fase: "Fase 5 — Operação"
- tarefa_atual.agente: "report-generator"
- report-generator status: "running"
- Log: "Fase 5 — Operação Contínua iniciada. Auditoria geral de ativos."

---

TAREFA 1 — report-generator (Auditoria e Inventário de Ativos)
Leia agents/report-generator.md.
Faça uma auditoria completa de TUDO que foi produzido nas Fases 0-4.
Leia cada arquivo listado acima e compile um inventário organizado.

Produza o INVENTÁRIO MESTRE DE ATIVOS contendo:

1. CONTEÚDO PRONTO PARA USO
   - Quantas captions estão prontas (posts 1-9 do branding book + posts 10-22)
   - Status de cada uma: rascunho / aprovada / publicada
   - Briefs visuais prontos (9 de lançamento + 6 de ads)

2. PLATAFORMAS
   - Status do Airbnb listing (copy pronta, falta publicar)
   - Status da Landing Page (HTML pronto, falta domínio e hospedagem)
   - Status do Instagram (setup documentado, falta criar a conta)

3. CAMPANHAS DE TRÁFEGO
   - 3 campanhas documentadas: awareness, tráfego, conversão
   - Checklist de pré-lançamento (o que falta para ativar cada uma)

4. PENDÊNCIAS CRÍTICAS
   Compile todas as pendências que dependem de ação do João:
   - Preço por noite (temporada alta e baixa)
   - Lista completa de comodidades
   - WhatsApp do anfitrião
   - Email do anfitrião
   - Logos (Casa Nativa, Comsteel, Alinea)
   - Criativos finais pelo designer
   - Pixel Meta + domínio verificado
   - Orçamento aprovado para ads
   - Conta Meta Ads com pagamento ativo

5. ROADMAP DE ATIVAÇÃO
   Priorize as pendências e monte uma sequência lógica:
   O que fazer primeiro → segundo → terceiro para que a operação comece de fato.

Salve em: outputs/reports/2026-04-09_inventario-mestre-ativos.md

Atualize state.json:
- report-generator output: "outputs/reports/2026-04-09_inventario-mestre-ativos.md"
- log: conclusão da Tarefa 1
- tarefa_atual.numero: 2
- tarefa_atual.descricao: "Calendário Editorial — Mês 2 (Maio-Junho)"
- tarefa_atual.agente: "strategy-planner"
- strategy-planner status: "running"

---

TAREFA 2 — strategy-planner + copywriter (Calendário Editorial — Mês 2)
Leia agents/strategy-planner.md e agents/copywriter.md.
Consulte o calendário do mês 1 (outputs/reports/2026-04-08_calendario-editorial-abril-maio.md)
e o posicionamento de marca (outputs/reports/2026-04-08_posicionamento.md).

Crie o CALENDÁRIO EDITORIAL DO MÊS 2 (próximos 30 dias após o mês 1).
Considere que o lançamento já foi feito e o perfil já está ativo.

Estrutura:
- 30 entradas (uma por dia útil de publicação, ~4x/semana)
- Para cada entrada: Data | Formato | Tema | Objetivo | Copy resumida | Visual sugerido
- Distribuição de conteúdo:
  - 30% Experiência/lifestyle (o que é ficar na Casa Nativa)
  - 25% Localização/enoturismo (Vale dos Vinhedos, vinícolas, gastronomia)
  - 20% Bastidores/autenticidade (dia a dia, preparação, detalhes)
  - 15% Social proof (depoimentos, avaliações, repostagens)
  - 10% Conversão direta (promoções sazonais, últimas datas, CTA forte)
- Incluir datas especiais relevantes do período
- Incluir 4 ideias de Reels com scripts curtos
- Incluir 2 ideias de carrossel educacional

Salve em: outputs/reports/2026-04-09_calendario-editorial-mes2.md

Atualize state.json:
- strategy-planner status: "completed"
- strategy-planner output: "outputs/reports/2026-04-09_calendario-editorial-mes2.md"
- log: conclusão da Tarefa 2
- tarefa_atual.numero: 3
- tarefa_atual.descricao: "Templates de Resposta e Atendimento"
- tarefa_atual.agente: "copywriter"
- copywriter status: "running"

---

TAREFA 3 — copywriter + brand-guardian (Templates de Atendimento)
Leia agents/copywriter.md e agents/brand-guardian.md.
Consulte os pitches de venda (outputs/reports/2026-04-08_pitches-de-venda.md)
e o setup do Instagram (outputs/reports/2026-04-08_instagram-setup-master.md).

Crie um MANUAL DE ATENDIMENTO DIGITAL completo para a Casa Nativa:

1. RESPOSTAS PARA INSTAGRAM (DM)
   - Saudação inicial (primeira mensagem de um interessado)
   - Resposta sobre disponibilidade de datas
   - Resposta sobre preço (com placeholder até definir o valor)
   - Resposta sobre localização e como chegar
   - Resposta sobre comodidades e diferenciais
   - Resposta sobre check-in/check-out
   - Resposta sobre política de cancelamento
   - Resposta redirecionando para Airbnb ou WhatsApp
   - Agradecimento pós-estadia + pedido de avaliação

2. RESPOSTAS PARA AIRBNB
   - Mensagem automática de pré-chegada (24h antes)
   - Mensagem de boas-vindas (dia do check-in)
   - Mensagem de meio-estadia (verificação, oferecer dicas)
   - Mensagem de checkout + pedido de avaliação
   - Resposta a avaliações positivas (3 variações)
   - Resposta a avaliações com pontos de melhoria (2 variações)

3. RESPOSTAS PARA WHATSAPP
   - Saudação automática
   - Menu de opções rápidas (datas, preço, localização)
   - Confirmação de reserva
   - Instruções de chegada detalhadas

4. RESPOSTAS PARA GOOGLE MEU NEGÓCIO
   - Resposta padrão a avaliação 5 estrelas (3 variações)
   - Resposta a avaliação 4 estrelas (2 variações)
   - Resposta a avaliação ≤3 estrelas (empática + convite a resolver)

TODAS as respostas devem usar o tom de voz da Casa Nativa: acolhedor,
sensorial, sofisticado, nunca genérico. Validação do brand-guardian obrigatória.

Salve em: outputs/content/2026-04-09_manual-atendimento-digital.md

Atualize state.json:
- copywriter status: "completed"
- copywriter output: "outputs/content/2026-04-09_manual-atendimento-digital.md"
- brand-guardian status: "completed"
- log: conclusão da Tarefa 3
- tarefa_atual.numero: 4
- tarefa_atual.descricao: "SOPs — Procedimentos Operacionais Padrão"
- tarefa_atual.agente: "strategy-planner"
- strategy-planner status: "running"

---

TAREFA 4 — strategy-planner (SOPs de Operação)
Leia agents/strategy-planner.md.
Use todo o conhecimento acumulado do projeto para criar os
PROCEDIMENTOS OPERACIONAIS PADRÃO (SOPs) da Casa Nativa.

Crie um documento com os seguintes SOPs:

SOP 1 — ROTINA SEMANAL DE CONTEÚDO
- Segunda: planejamento da semana (revisar calendário, preparar copies)
- Terça/Quarta/Quinta: publicação de posts conforme calendário
- Sexta: análise rápida de performance da semana
- Sábado: story casual / bastidores (se aplicável)
- Checklist diário de engajamento (responder comentários, DMs)

SOP 2 — ROTINA DE GESTÃO DE RESERVAS
- Fluxo completo: consulta → confirmação → pré-chegada → estadia → pós-checkout
- Templates de mensagem para cada etapa (referência ao manual de atendimento)
- Quando escalar para atendimento humano personalizado

SOP 3 — GESTÃO DE META ADS (quando ativas)
- Verificação diária (2 min): orçamento e status
- Análise semanal (15 min): CPM, CTR, CPC, ROAS
- Ações de otimização: quando pausar, escalar ou trocar criativo
- Gatilhos de alerta: frequência >3, CTR <1%, CPC acima do benchmark

SOP 4 — RELATÓRIO MENSAL
- Métricas de Instagram: seguidores, alcance, engajamento, melhores posts
- Métricas de Ads: investimento, resultados, ROAS
- Métricas de reservas: ocupação, receita, avaliação média
- Ações para o próximo mês

SOP 5 — GESTÃO DE CRISES / AVALIAÇÕES NEGATIVAS
- Protocolo de resposta em até 2h
- Modelo de escalonamento
- Nunca responder quando emocional — tom sempre profissional e empático
- Follow-up após resolução

Salve em: outputs/reports/2026-04-09_sops-operacao-casa-nativa.md

Atualize state.json:
- strategy-planner status: "completed"
- strategy-planner output: "outputs/reports/2026-04-09_sops-operacao-casa-nativa.md"
- log: conclusão da Tarefa 4
- tarefa_atual.numero: 5
- tarefa_atual.descricao: "Relatório Final de Projeto + Handover"
- tarefa_atual.agente: "report-generator"
- report-generator status: "running"

---

TAREFA 5 — report-generator (Relatório Final de Projeto + Handover)
Leia agents/report-generator.md.
Compile o RELATÓRIO FINAL DO PROJETO — documento de handover que João
poderá usar como guia mestre da operação da Casa Nativa.

O relatório deve conter:

1. RESUMO EXECUTIVO
   - O que foi construído nas Fases 0 a 5
   - Visão geral do ecossistema de marketing montado
   - Quantidade total de entregáveis gerados

2. MAPA DE ENTREGÁVEIS
   Tabela completa com todos os arquivos gerados, organizados por fase:
   | Fase | Arquivo | Descrição | Status |
   Para cada arquivo, indicar se está pronto para uso ou depende de ação.

3. GUIA DE ATIVAÇÃO — PASSO A PASSO
   Ordem exata do que João precisa fazer para colocar tudo no ar:
   Passo 1: Criar conta Instagram (@casanativa.vale)
   Passo 2: Configurar bio e destaques (usar setup master)
   Passo 3: Publicar os 9 posts de lançamento (usar captions + briefs)
   Passo 4: Publicar listing no Airbnb (usar copy pronta)
   Passo 5: Contratar hospedagem e domínio para landing page
   Passo 6: Configurar Pixel do Meta na landing page
   Passo 7: Ativar campanhas Meta Ads (seguir plano técnico)
   Passo 8: Iniciar rotina semanal de conteúdo (seguir SOPs)
   (expandir conforme necessário)

4. PENDÊNCIAS FINAIS
   Lista definitiva de tudo que ainda precisa de ação humana,
   priorizada por urgência.

5. COMO USAR ESTE FRAMEWORK NO DIA A DIA
   - Como acionar o Orquestrador para tarefas pontuais
   - Comandos rápidos disponíveis (listar do CLAUDE.md)
   - Como solicitar novos conteúdos, briefs ou relatórios
   - Como atualizar o dashboard

Salve em: outputs/reports/2026-04-09_relatorio-final-projeto.md

Atualização CRÍTICA no state.json:
- report-generator status: "completed"
- report-generator output: "outputs/reports/2026-04-09_relatorio-final-projeto.md"
- fase_5_entregaveis (criar esta CHAVE na raiz do state.json):
  {
    "inventario_ativos": "outputs/reports/2026-04-09_inventario-mestre-ativos.md",
    "calendario_mes2": "outputs/reports/2026-04-09_calendario-editorial-mes2.md",
    "manual_atendimento": "outputs/content/2026-04-09_manual-atendimento-digital.md",
    "sops_operacao": "outputs/reports/2026-04-09_sops-operacao-casa-nativa.md",
    "relatorio_final": "outputs/reports/2026-04-09_relatorio-final-projeto.md"
  }
- Fase 5 na lista "fases": manter como "em_andamento" (fase contínua, nunca "concluida")
- fase_atual: "Fase 5 — Operação (ativa)"
- tarefa_atual: { "fase": "Fase 5 — Operação", "numero": null, "total": null, "descricao": "Modo operacional — aguardando próxima instrução de João", "agente": "orchestrator" }
- Remova da lista de pendências os itens que foram resolvidos (se houver)
- Log: adicione as entradas de conclusão de cada tarefa e da Fase 5 (setup operacional concluído)

---

FINALIZAÇÃO
1. Cumpra todos os updates do arquivo state.json com total precisão.
2. Apresente no chat um RESUMO FINAL ELEGANTE contendo:
   - Recapitulação do projeto completo (Fases 0-5)
   - Total de arquivos gerados com caminhos
   - As 5 primeiras ações que João deve tomar HOJE
   - O que o Orquestrador pode fazer a qualquer momento (comandos rápidos)
3. Encerre celebrando: "🏡 Casa Nativa — pronta para operar."

Pode iniciar a orquestração!
```

---

## ✅ Checklist antes de executar

- [ ] Fases 0 a 4 constam como "concluída" no dashboard
- [ ] A pasta `outputs/` contém os 16 arquivos das fases anteriores
- [ ] O dashboard está acessível em `http://localhost:8081/dashboard/dashboard.html`
- [ ] Entende-se que a Fase 5 gera os documentos operacionais — a rotina real começa quando João tomar as ações do Guia de Ativação
