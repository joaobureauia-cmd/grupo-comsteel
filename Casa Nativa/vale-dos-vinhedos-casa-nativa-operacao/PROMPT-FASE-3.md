# 🚀 PROMPT DE ENTRADA — FASE 3: PLATAFORMAS DE VENDA
## Cole este prompt no Claude Code ao iniciar a Fase 3

---

## 🖥️ Dashboard — manter aberto em paralelo
Lembre-se de manter o painel de operação aberto para acompanhar a execução em tempo real.
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

Vamos executar a FASE 3 — PLATAFORMAS (Landing Page e Airbnb).

Atualize dashboard/state.json de imediato:
- fase_atual: "Fase 3 — Plataformas"
- Nas "fases", garanta que a Fase 3 esteja "em_andamento" e Fase 2 "concluida".
- tarefa_atual.numero: 1
- tarefa_atual.total: 3
- tarefa_atual.descricao: "Criação de Copy do Listing do Airbnb"
- tarefa_atual.fase: "Fase 3 — Plataformas"
- tarefa_atual.agente: "copywriter"
- status do agente copywriter: "running"
- Log: "Fase 3 iniciada. Copywriter estruturando Airbnb Listing."

---

TAREFA 1 — copywriter
Use o arquivo gerado na Fase 1 (`outputs/reports/2026-04-08_pitches-de-venda.md`) e os insights de concorrência (`outputs/research/2026-04-08_pesquisa-airbnb.md`) para criar a Estrutura Oficial Completa do Anúncio do Airbnb da Casa Nativa.
Sua entrega deve conter:
1. Título do Anúncio (Otimizado, atraente e respeitando o limite de caracteres).
2. Descrição Geral (Sensorial, focada na experiência de "luxo descalço").
3. Acomodação (Detalhes do espaço, arquitetura tiny house).
4. Acesso do Hóspede & Interação (Instruções gerais de autonomia e privacidade).
5. Seção de Diferenciais (ênfase em itens premium e na experiência regional).
6. Lista Sugerida de Comodidades e Regras da Casa.

Salve o resultado completo em: outputs/platforms/2026-04-08_airbnb-listing.md (crie a pasta platforms se não existir).

Atualize o state.json:
- copywriter status: "completed"
- copywriter output: "outputs/platforms/2026-04-08_airbnb-listing.md"
- log: entrada de conclusão da Tarefa 1
- tarefa_atual.numero: 2
- tarefa_atual.descricao: "Wireframe & Copy da Landing Page Oficial"
- tarefa_atual.agente: "landing-page-builder"
- landing-page-builder status: "running"

---

TAREFA 2 — landing-page-builder (Wireframe)
Agora é a hora de consolidar a presença própria (vendas diretas). Desenvolva o Wireframe completo de Copy e UX para a Landing Page Oficial (casa-nativa.com.br).
Sua tarefa é criar a estrutura da página de cima a baixo, ditando o que vai em cada "Dobra" (seção da página), desde o Hero/Header até o Footer.
Para cada dobra da Landing Page, forneça:
1. Objetivo da seção (ex: Conscientização, Conversão).
2. O "Copy" (título principal (H1/H2), subtítulo e botões de CTA).
3. Orientação visual (O que aparece de fundo? Vídeo? Foto em carrossel?).

Seções obrigatórias:
- Dobra 1: Hero (Primeira impressão e CTA forte).
- Dobra 2: A Experiência (O conceito, luxo no Vale dos Vinhedos).
- Dobra 3: A Casa (Fotos estruturais e tiny house living).
- Dobra 4: Depoimentos/Escassez (Agenda disputada, avaliações exclusivas).
- Dobra 5: FAQ & Rodapé.

Salve em: outputs/platforms/2026-04-08_landing-page-wireframe.md

Atualize o state.json:
- tarefa_atual.numero: 3
- tarefa_atual.descricao: "Construção do HTML funcional da Landing Page"
- tarefa_atual.agente: "landing-page-builder"
- log: entrada de conclusão da Tarefa 2

---

TAREFA 3 — landing-page-builder (HTML Funcional)
Com base no wireframe que você acabou de gerar (`outputs/platforms/2026-04-08_landing-page-wireframe.md`),
no posicionamento da marca (`outputs/reports/2026-04-08_posicionamento.md`) e no contexto
da Casa Nativa (`context/context-casa-nativa.md`), crie o código HTML+CSS+JS completo e funcional
da Landing Page da Casa Nativa.

REQUISITOS TÉCNICOS:
- Arquivo único e autossuficiente (HTML + CSS inline + JS inline).
- Design responsivo (mobile first).
- Paleta de cores da marca: terra (#80421c), creme (#f5ede0), areia (#c4a882), marrom (#5c3d22), branco (#faf8f4).
- Tipografia: Google Fonts — "Playfair Display" para títulos e "Inter" para corpo de texto.
- Animações suaves de scroll (fade-in, slide-up) usando Intersection Observer.
- Seções obrigatórias conforme o wireframe (Hero, Experiência, A Casa, Depoimentos, FAQ, Footer).
- Onde houver imagens, use placeholders elegantes com gradientes ou ícones SVG inline (não dependa de URLs externas).
- Botões de CTA com links para WhatsApp (usar placeholder https://wa.me/55XXXXXXXXXXX).
- Meta tags de SEO, Open Graph e favicon placeholder.
- Efeitos visuais premium: glassmorphism sutil, parallax no hero, hover states nos botões.

Salve em: outputs/landing-page/index.html (crie a pasta landing-page se não existir).

Atualização CRÍTICA no state.json:
- landing-page-builder status: "completed"
- landing-page-builder output: "outputs/platforms/2026-04-08_landing-page-wireframe.md, outputs/landing-page/index.html"
- fase_3_entregaveis (criar esta CHAVE na raiz do state.json, assim como ocorreu nas fases anteriores):
  {
    "listing_oficial_airbnb": "outputs/platforms/2026-04-08_airbnb-listing.md",
    "wireframe_landing_page": "outputs/platforms/2026-04-08_landing-page-wireframe.md",
    "landing_page_html": "outputs/landing-page/index.html"
  }
- Fase 3 da lista "fases": status = "concluida"
- Fase 4 da lista "fases": status = "em_andamento"
- fase_atual: "Fase 4 — Tráfego Pago"
- log: adicione as entradas de conclusão da Tarefa 3 e da Fase 3 como um todo.

FINALIZAÇÃO
1. Cumpra todos os updates do arquivo `state.json` com total precisão.
2. O dashboard atualizará sozinho mostrando os botões de 👁️ Ler nos arquivos gerados em Plataformas. Mande uma mensagem de encerramento da fase avisando o humano.
3. Informe que a Landing Page pode ser visualizada acessando http://localhost:8081/outputs/landing-page/index.html

Pode iniciar a orquestração!
```

---

## ✅ Checklist antes de executar

- [ ] Fase 2 foi finalizada com sucesso e os 3 prompts dela aprovados 
- [ ] A pasta `outputs/campaigns/` e `outputs/briefs/` já contêm os artefatos de Insta
- [ ] O dashboard já apresenta os dados atualizados das Fases 1 e 2
