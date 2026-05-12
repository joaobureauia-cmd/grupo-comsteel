# 🚀 PROMPT DE ENTRADA — FASE 2: INSTAGRAM
## Cole este prompt no Claude Code ao iniciar a Fase 2

---

## 🖥️ Dashboard — manter aberto em paralelo
Caso ainda não tenha feito, garanta que o seu painel de operação está rodando na pasta raiz do projeto:

```bash
# Se o servidor não estiver rodando, abra um terminal na raiz (vale-dos-vinhedos-casa-nativa-operacao)
python3 -m http.server 8081

# Acesse no navegador:
http://localhost:8081/dashboard/dashboard.html
```

---

## 💬 Prompt — cole como primeira mensagem no Claude Code

```text
Você é o Orquestrador do projeto Vale dos Vinhedos — Casa Nativa Operação.

Vamos executar a FASE 2 — INSTAGRAM completa.

Atualize dashboard/state.json:
- fase_atual: "Fase 2 — Instagram"
- Nas "fases", atualize o status da Fase 2 para "em_andamento" e confira se a Fase 1 está "concluida".
- tarefa_atual.numero: 1
- tarefa_atual.total: 3
- tarefa_atual.descricao: "Criação de Copy (Legendas) para Posts 10-30"
- tarefa_atual.fase: "Fase 2 — Instagram"
- O agente copywriter muda o status para "running"
- Log: "Fase 2 iniciada. Copywriter iniciando Tarefa 1."

---

TAREFA 1 — copywriter
Use o arquivo gerado na Fase 1 (`outputs/reports/2026-04-08_calendario-editorial-abril-maio.md`) para consultar os temas dos posts 10 a 30.
Leia também o `context/context-casa-nativa.md` para garantir o Tom de Voz (luxo descalço, sensorial, exclusivo).
Produza as 21 legendas detalhadas (referentes aos posts 10-30) incluindo as hashtags corretas geradas na Fase 1.
Formato da entrega de cada post deve ter:
1. Data / Post Num
2. Imagem sugerida
3. Legenda (Copy) focada
4. Hashtags selecionadas

Salve o resultado completo em: outputs/campaigns/2026-04-08_posts-10-30-captions.md (crie a pasta campaigns se não existir).

Atualize o state.json:
- copywriter status: "completed"
- copywriter output: "outputs/campaigns/2026-04-08_posts-10-30-captions.md"
- log: entrada de conclusão da Tarefa 1
- tarefa_atual.numero: 2
- tarefa_atual.descricao: "Criação de Briefs Visuais para Lançamento"
- content-brief-generator status: "running"

---

TAREFA 2 — content-brief-generator
A lista dos 9 primeiros posts e da identidade visual já está pronta de concepção no `context/context-casa-nativa.md`.
Sua tarefa é criar os Guias Fotográficos EXATOS ou Prompts Text-to-Image (Midjourney/DALL-E) correspondentes aos 9 posts iniciais de lançamento para manter o aspecto premium.

Formato da entrega para cada um dos 9 posts:
1. Ideia Visual central
2. Elementos da Fotografia (luz natural, cores terrosas, enquadramento detalhista)
3. Prompt Text-to-Image (escrito em inglês)
4. Recomendação de Referência Estética / Mood

Salve em: outputs/briefs/2026-04-08_visual-briefs-launch.md (crie a pasta briefs se não existir).

Atualize state.json:
- content-brief-generator status: "completed"
- content-brief-generator output: "outputs/briefs/2026-04-08_visual-briefs-launch.md"
- log: entrada de conclusão da Tarefa 2
- tarefa_atual.numero: 3
- tarefa_atual.descricao: "Compilação Estratégica do Perfil Instagram"
- social-media-manager status: "running"

---

TAREFA 3 — social-media-manager
Consolide as informações finais para a configuração e gestão da conta da Casa Nativa.
Crie um Documento Mestre de Setup do Instagram que inclua:
1. O texto EXATO da Bio, Nome, link da bio (estrutura de Linktree imaginada).
2. Títulos dos 4-5 Destaques Permanentes (Highlights) e ideias de capas.
3. Fluxo de Publicação Inicial.
4. Respostas sugeridas para os primeiros DMs e comentários baseados no Pitch criado na Fase 1.

Salve em: outputs/reports/2026-04-08_instagram-setup-master.md

Atualização CRÍTICA no state.json:
- social-media-manager status: "completed"
- social-media-manager output: "outputs/reports/2026-04-08_instagram-setup-master.md"
- fase_2_entregaveis (criar esta CHAVE na raiz do state.json, nos mesmos moldes que a fase_1_entregaveis):
  {
    "captions_posts_10_30": "outputs/campaigns/2026-04-08_posts-10-30-captions.md",
    "briefs_visuais_lancamento": "outputs/briefs/2026-04-08_visual-briefs-launch.md",
    "master_setup_instagram": "outputs/reports/2026-04-08_instagram-setup-master.md"
  }
- Fase 2 da lista "fases": status = "concluida"
- Fase 3 da lista "fases": status = "em_andamento"
- fase_atual: "Fase 3 — Plataformas"
- log: adicione as entradas de conclusão da Tarefa 3 e da Fase 2 como um todo.

FINALIZAÇÃO
1. Cumpra todos os updates do arquivo `state.json` com total precisão.
2. Apresente no chat um resumo elegante da Fase 2 e os links para os documentos gerados, prontos para que o humano clique em 👁️ Ler no Painel Operacional.

Você foi acionado. Inicie a orquestração!
```

---

## ✅ Checklist antes de executar

- [ ] A URL acessada do painel mostra `http://localhost:8081/dashboard/dashboard.html` sem erro 404
- [ ] Fase 1 consta como "Concluída" e há check marks de todas as atividades
- [ ] Você entende que as imagens ficarão apenas como briefs nesta fase (os assets finais serão finalizados depois ou repassados para um criativo humano).
