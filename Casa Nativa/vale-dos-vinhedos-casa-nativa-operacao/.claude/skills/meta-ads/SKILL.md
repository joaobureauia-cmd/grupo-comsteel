# Skill: meta-ads-workflow
## Criação e Gestão de Campanhas — Meta Ads (Facebook/Instagram)

### Quando usar esta skill
Use quando `ads-manager` for acionado para criar, configurar ou otimizar campanhas no Meta Ads.

---

### Estrutura de Campanha Padrão — Casa Nativa

#### Hierarquia Meta Ads
```
CAMPANHA (objetivo)
└── CONJUNTO DE ANÚNCIOS (público + posicionamento + orçamento)
    └── ANÚNCIO (criativo + copy)
```

---

### Tipos de Campanha por Fase

#### Fase 2 — Lançamento Instagram (brand awareness)
```
Objetivo: Reconhecimento de marca / Alcance
Público: Interesses em enoturismo, viagens de luxo, casais, Serra Gaúcha
Orçamento: [a definir com João]
Duração: 15-30 dias
Posicionamento: Instagram Feed + Stories
```

#### Fase 4 — Tráfego e Conversão
```
Objetivo: Tráfego para landing page / Conversões
Público: Remarketing (quem interagiu com o Instagram) + lookalike
Orçamento: [a definir com João]
Posicionamento: Instagram Feed + Stories + Facebook Feed
```

#### Campanha de Temporada Alta
```
Objetivo: Conversão (reservas)
Público: Casais 25-50 anos, renda alta, interesse em hospedagem, turismo gastronômico
Posicionamento: todos os placements relevantes
```

---

### Definição de Público — Padrão Casa Nativa

**Público Principal (Interesse):**
- Localização: Brasil (foco em SP, RS, SC, PR, RJ)
- Idade: 25–55 anos
- Gênero: Todos
- Interesses: Enoturismo, viagens de luxo, gastronomia, wellness, design de interiores, hospedagem boutique, Serra Gaúcha, Airbnb

**Público de Remarketing:**
- Visitantes da landing page (pixel)
- Pessoas que interagiram com o perfil do Instagram
- Pessoas que assistiram 50%+ dos Reels

**Público Lookalike:**
- Similar a quem interagiu com o perfil (1%-3% Brasil)
- Similar a visitantes da landing page

---

### Protocolo de Criação de Campanha

**Passo 1 — Briefing**
Coletar antes de criar:
- Objetivo da campanha
- Orçamento total e diário
- Período da campanha
- Criativo disponível (imagem/vídeo — deve vir do designer)
- Copy aprovada (do `copywriter`)
- URL de destino (landing page ou link do Airbnb)

**Passo 2 — Configuração via Meta Ads MCP**
```
1. Criar campanha com objetivo correto
2. Criar conjunto de anúncios:
   - Definir público (usar padrões acima)
   - Definir orçamento
   - Definir período
   - Selecionar posicionamentos
3. Criar anúncio:
   - Fazer upload do criativo
   - Inserir copy (headline + texto principal + CTA)
   - Inserir URL de destino
   - Revisar preview em todos os formatos
4. Publicar ou enviar para revisão
```

**Passo 3 — Registro**
Salvar configuração completa em `outputs/campaigns/AAAA-MM-DD_campanha-[nome].md`

---

### Templates de Copy para Anúncios

**Formato Awareness (Brand Story):**
```
[Headline]: Um refúgio para desacelerar
[Texto principal]: No coração do Vale dos Vinhedos, onde o tempo desacelera e a
natureza abraça cada detalhe. Casa Nativa é design premiado, sauna privativa e
a Serra Gaúcha a poucos passos.
[CTA]: Saiba mais
```

**Formato Conversão (Reservas):**
```
[Headline]: Reserve sua experiência no Vale dos Vinhedos
[Texto principal]: Dois módulos. Um projeto premiado. Uma sauna privativa.
E o Vale dos Vinhedos inteiro como cenário. Casa Nativa — Bento Gonçalves.
[CTA]: Reservar agora
```

**Formato Engajamento (Reels):**
```
[Headline]: Isso é o que acontece quando arquitetura encontra a natureza da Serra Gaúcha
[Texto principal]: Tiny house premiada. Sauna privativa. Vale dos Vinhedos.
Casa Nativa é um refúgio onde cada detalhe foi pensado para fazer você desacelerar.
[CTA]: Ver mais
```

---

### Gestão e Otimização

**Métricas a monitorar semanalmente:**
- CPM (custo por mil impressões)
- CTR (taxa de clique) — meta: >1,5%
- CPC (custo por clique)
- Frequência — pausar se >3,0
- Custo por resultado (lead ou reserva)
- ROAS (retorno sobre investimento em ads)

**Ações de otimização:**
- CTR < 1%: trocar criativo
- Frequência > 3: renovar criativo ou expandir público
- CPC alto: testar novo público ou copy
- Campanha em aprendizado: não alterar por 7 dias

---

### Salvamento
Salvar relatórios de campanha em `outputs/campaigns/` com nomenclatura:
`AAAA-MM-DD_campanha-[objetivo]-[status].md`
