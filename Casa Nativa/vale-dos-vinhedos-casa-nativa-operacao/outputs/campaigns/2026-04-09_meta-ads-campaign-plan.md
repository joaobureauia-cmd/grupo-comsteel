---
data: 2026-04-09
tipo: meta-ads-campaign-plan
responsavel: ads-manager
versao: 1.0
---

# Plano Técnico de Campanhas — Meta Ads
## Casa Nativa | Vale dos Vinhedos, RS

> **Baseado em:** copies (2026-04-09) + briefs criativos (2026-04-09) + pesquisa Airbnb (2026-04-08) + posicionamento (2026-04-08)
> **Agente:** ads-manager
> **Data:** 09/04/2026

---

## VISÃO GERAL DO FUNIL

```
AWARENESS ──────────────────────────────────────────────────▶ TRÁFEGO ──────▶ CONVERSÃO
Campanha 1: "Conheça"    Campanha 2: "Descubra"    Campanha 3: "Reserve"
Fase: Semana 1-2         Fase: Semana 2-4           Fase: Semana 3-6
Orçamento: R$600         Orçamento: R$750            Orçamento: R$900
```

**Lógica de sequenciamento:**
1. Awareness constrói audiência qualificada (14 dias)
2. Tráfego ativa remarketing de quem interagiu com Awareness
3. Conversão ativa remarketing de visitantes da LP + lookalike

---

---

# CAMPANHA 1 — AWARENESS
## "Casa Nativa — Conheça o Refúgio"

---

### 1.1 Configuração da Campanha

| Campo | Configuração |
|-------|--------------|
| **Nome da campanha** | [CN] Awareness — Conheça o Refúgio |
| **Objetivo** | Reconhecimento — Alcance ou Reconhecimento de Marca |
| **Status** | Pausada (ativar na semana 1) |
| **Tipo de compra** | Leilão |
| **Orçamento total** | R$ 600,00 (15 dias) |
| **Orçamento diário** | R$ 40,00/dia |
| **Data início** | [Definir após aprovação de João] |
| **Data fim** | [Início + 15 dias] |
| **Pixel** | Pixel Meta instalado na landing page — obrigatório antes de ativar |

---

### 1.2 Conjunto de Anúncios — Público Frio (Interesses)

| Campo | Configuração |
|-------|--------------|
| **Nome do conjunto** | [CN-AW] Público Frio — Interesses Turismo |
| **Orçamento** | R$ 40,00/dia (nível de campanha — CBO recomendado) |
| **Localização** | Brasil |
| **Cidades priorizadas** | São Paulo (SP), Porto Alegre (RS), Curitiba (PR), Florianópolis (SC), Rio de Janeiro (RJ), Belo Horizonte (MG) |
| **Raio de exclusão** | Bento Gonçalves e municípios limítrofes (evitar mostrar para quem já conhece) |
| **Idade** | 25–55 anos |
| **Gênero** | Todos |
| **Idioma** | Português (Brasil) |

**Segmentação por interesses (camada 1 — Turismo):**
- Enoturismo
- Airbnb
- Turismo de luxo / boutique hotels
- Serra Gaúcha / Rio Grande do Sul
- Viagens de casal

**Segmentação por interesses (camada 2 — Design + Lifestyle):**
- Arquitetura e design de interiores
- Revista Architectural Digest
- Revista Casa Vogue
- Tiny house
- Design contemporâneo

**Segmentação por interesses (camada 3 — Bem-estar):**
- Sauna
- Wellness e spa
- Mindfulness / meditação
- Yoga e bem-estar

**Exclusões:**
- Pessoas que já interagiram com a página (remarketing separado)
- Interesse em "hospedagem econômica" / "hostels"

---

### 1.3 Anúncios da Campanha Awareness

| Código criativo | Formato | Copy correspondente |
|----------------|---------|---------------------|
| **AW-01** | Feed estático 1080×1080 | H2: "Design que respira com a natureza" / T2: sequência sensorial / CTA: Conheça a Casa Nativa |
| **AW-02** | Stories/Reels 1080×1920 | H3: "Onde o silêncio tem textura" / T1: design premiado + sauna + natureza / CTA: Conheça a Casa Nativa |

**Configuração de placements:**
- ✅ Instagram Feed
- ✅ Instagram Stories
- ✅ Instagram Reels
- ✅ Facebook Feed
- ❌ Audience Network (desativar — não alinhado com público premium)
- ❌ Messenger (desativar)

---

### 1.4 Teste A/B — Campanha Awareness

| Variável | Variação A | Variação B |
|----------|-----------|-----------|
| **Headline** | "Design que respira com a natureza" | "Onde o silêncio tem textura" |
| **Público** | Interesses Turismo + Design (camadas 1+2) | Interesses Bem-estar + Turismo (camadas 1+3) |

**Duração do teste:** 7 dias antes de pausar a variação perdedora
**Métrica de decisão:** Menor CPM + maior frequência de 3+ (awareness acumulado)

---

### 1.5 Métricas de Sucesso — Awareness

| KPI | Meta |
|-----|------|
| Alcance | > 15.000 pessoas únicas em 15 dias |
| CPM | < R$ 25,00 |
| Frequência | 2–4x por usuário (não ultrapassar 5x) |
| CTR (sem ser objetivo principal) | > 0,5% |

---

---

# CAMPANHA 2 — TRÁFEGO
## "Descubra a Casa Nativa"

---

### 2.1 Configuração da Campanha

| Campo | Configuração |
|-------|--------------|
| **Nome da campanha** | [CN] Tráfego — Descubra a Casa Nativa |
| **Objetivo** | Tráfego — Cliques no link |
| **Status** | Pausada (ativar na semana 2, após awareness rodar 7 dias) |
| **Tipo de compra** | Leilão |
| **Orçamento total** | R$ 750,00 (25 dias) |
| **Orçamento diário** | R$ 30,00/dia |
| **URL de destino** | [URL da landing page — inserir quando disponível] |
| **UTM** | `utm_source=meta&utm_medium=paid&utm_campaign=trafego-cn&utm_content=[CÓDIGO_CRIATIVO]` |

---

### 2.2 Conjunto A — Público Frio Quente (Interesses refinados)

| Campo | Configuração |
|-------|--------------|
| **Nome do conjunto** | [CN-TR] Frio Quente — Interesses Refinados |
| **Orçamento** | R$ 15,00/dia |
| **Localização** | Brasil (mesmas cidades priorizadas) |
| **Idade** | 28–52 anos |
| **Gênero** | Todos |

**Segmentação:**
- Todos os interesses da Campanha 1 (Awareness)
- Adicionado: comportamento "Viajantes frequentes" (Meta Behavior)
- Adicionado: interesse em "hotéis boutique", "design hotel", "slow travel"
- **Advantage+ audience:** ativar para expansão automática pelo Meta

---

### 2.3 Conjunto B — Remarketing (Engajamento Awareness)

| Campo | Configuração |
|-------|--------------|
| **Nome do conjunto** | [CN-TR] Remarketing — Engajamento Instagram |
| **Orçamento** | R$ 15,00/dia |
| **Audiência personalizada** | Pessoas que interagiram com posts/perfil do Instagram nos últimos 30 dias |
| **Inclui** | Visualizou vídeo, curtiu, comentou, salvou, clicou no perfil |
| **Tamanho estimado** | Depende do crescimento do Instagram — ativar quando atingir 500+ interações |

> **Nota:** Este conjunto só se torna relevante quando o Instagram tiver tração orgânica. Pode ser ativado paralelamente às campanhas de awareness.

---

### 2.4 Anúncios da Campanha Tráfego

| Código criativo | Formato | Copy correspondente |
|----------------|---------|---------------------|
| **TR-01** | Carrossel 4 cards 1080×1080 | H1: "Descubra o Refúgio no Vale" / T1: arquitetura + sauna + localização / CTA: Saiba Mais |
| **TR-02** | Stories sequenciais 3x 1080×1920 | H2: "Sauna privativa + design premiado" / T3: do prêmio ao Vale / CTA: Ver a Experiência |

**Placements:**
- ✅ Instagram Feed
- ✅ Instagram Stories
- ✅ Facebook Feed
- ✅ Facebook Stories
- ❌ Audience Network, Messenger (desativar)

---

### 2.5 Teste A/B — Campanha Tráfego

| Variável | Variação A | Variação B |
|----------|-----------|-----------|
| **Formato de criativo** | Carrossel TR-01 | Stories TR-02 |
| **Audiência** | Público frio quente | Remarketing de engajamento |

**Métrica de decisão:** Menor CPC + maior CTR após 5 dias
**Ação:** Pausar variação perdedora, concentrar orçamento na vencedora

---

### 2.6 Configuração de UTMs por Criativo

| Criativo | UTM Content |
|----------|-------------|
| TR-01 Carrossel | `tr-carrossel-01` |
| TR-02 Stories | `tr-stories-02` |

**UTM completa (TR-01):**
```
https://[URL-landing-page]?utm_source=meta&utm_medium=paid&utm_campaign=trafego-cn&utm_content=tr-carrossel-01
```

---

### 2.7 Métricas de Sucesso — Tráfego

| KPI | Meta |
|-----|------|
| CPC | < R$ 2,50 |
| CTR | > 1,5% |
| Sessões geradas | > 500 em 25 dias |
| Taxa de rejeição LP | < 60% |
| Tempo médio na LP | > 45 segundos |

---

---

# CAMPANHA 3 — CONVERSÃO
## "Reserve sua Experiência"

---

### 3.1 Configuração da Campanha

| Campo | Configuração |
|-------|--------------|
| **Nome da campanha** | [CN] Conversão — Reserve sua Experiência |
| **Objetivo** | Conversão — Evento de conversão (Lead ou Purchase conforme pixel) |
| **Status** | Pausada (ativar na semana 3, após LP ter tráfego e pixel com dados) |
| **Tipo de compra** | Leilão |
| **Orçamento total** | R$ 900,00 (30 dias) |
| **Orçamento diário** | R$ 30,00/dia |
| **URL de destino** | [Landing page ou Airbnb — conforme definição de João] |
| **Evento de pixel** | `Lead` (pré-reserva via formulário LP) ou `Purchase` (Airbnb) |
| **UTM** | `utm_source=meta&utm_medium=paid&utm_campaign=conversao-cn&utm_content=[CÓDIGO]` |

---

### 3.2 Conjunto A — Lookalike 1-3%

| Campo | Configuração |
|-------|--------------|
| **Nome do conjunto** | [CN-CV] Lookalike 1-3% — Base de Engajamento |
| **Orçamento** | R$ 15,00/dia |
| **Audiência personalizada de origem** | Público que interagiu com o perfil do Instagram (mínimo 1.000 pessoas) |
| **Lookalike** | 1–3% (Brasil) |
| **Sobreposição excluída** | Audiências de remarketing (conjuntos B e C) |

> **Nota:** O lookalike só funciona bem com uma base de qualidade. Recomenda-se ativar este conjunto quando o perfil tiver pelo menos 1.000 interações acumuladas (curtidas, seguidores, comentários, saves).

---

### 3.3 Conjunto B — Remarketing Visitantes LP

| Campo | Configuração |
|-------|--------------|
| **Nome do conjunto** | [CN-CV] Remarketing — Visitantes LP (30 dias) |
| **Orçamento** | R$ 10,00/dia |
| **Audiência personalizada** | Visitantes da landing page nos últimos 30 dias (via pixel) |
| **Exclusão** | Quem já converteu (preencheu formulário ou clicou no CTA de reserva Airbnb) |
| **Frequência recomendada** | Máx. 3x por semana por usuário |

---

### 3.4 Conjunto C — Remarketing Visitantes LP (Quentes — 7 dias)

| Campo | Configuração |
|-------|--------------|
| **Nome do conjunto** | [CN-CV] Remarketing Quente — LP 7 dias |
| **Orçamento** | R$ 5,00/dia |
| **Audiência personalizada** | Visitantes da landing page nos últimos 7 dias |
| **Objetivo** | Fechar quem visitou recentemente mas não converteu |
| **Copy recomendada** | Usar variação C com urgência mais direta (C2 — "Datas preenchem rápido") |

---

### 3.5 Anúncios da Campanha Conversão

| Código criativo | Formato | Copy correspondente |
|----------------|---------|---------------------|
| **CV-01** | Feed retrato 1080×1350 | H1: "Reserve sua Experiência no Vale" / T1: design + sauna + momento especial / CTA: Reservar Agora |
| **CV-02** | Stories urgência 1080×1920 | H3: "Duas pessoas. Um refúgio. Sua data." / T2: exclusividade + urgência / CTA: Ver Disponibilidade |

**Placements:**
- ✅ Instagram Feed
- ✅ Instagram Stories
- ✅ Facebook Feed
- ✅ Facebook Stories
- ✅ Instagram Explore (testar — público ativo em descoberta)
- ❌ Audience Network, Messenger (desativar)

---

### 3.6 Configuração de Evento de Conversão

**Opção A (Landing Page com formulário de pré-reserva):**
```
Evento: Lead
Disparar: quando o usuário preencher e enviar o formulário de contato
```

**Opção B (Airbnb como destino direto):**
```
Evento: Clique no link (View Content)
Criar evento personalizado: "Clique CTA Airbnb" na landing page
```

> **Recomendação:** Priorizar Opção A. O formulário de pré-reserva na landing page permite:
> a) Captura do lead mesmo sem reserva imediata
> b) Follow-up via WhatsApp/email pelo João
> c) Pixel com dados de conversão mais claros

---

### 3.7 Teste A/B — Campanha Conversão

| Variável | Variação A | Variação B |
|----------|-----------|-----------|
| **CTA** | "Reservar Agora" | "Ver Disponibilidade" |
| **Criativo** | CV-01 Feed retrato | CV-02 Stories urgência |

**Métrica de decisão:** Menor custo por lead após 7 dias
**Orçamento mínimo para decisão estatística:** R$ 150,00 em teste antes de desativar variação perdedora

---

### 3.8 Métricas de Sucesso — Conversão

| KPI | Meta |
|-----|------|
| CPL (Custo por Lead) | < R$ 35,00 |
| Taxa de conversão LP → Lead | > 3% |
| ROAS | > 3x (referência: diária R$500 → gasto de ads < R$165) |
| Leads gerados em 30 dias | > 25 leads qualificados |
| Taxa de fechamento (leads → reservas) | > 20% (meta João) |

---

---

## CRONOGRAMA DE ATIVAÇÃO

```
SEMANA 1 (Dias 1-7)
├── Ativar Campanha 1 — AWARENESS
├── Objetivo: construir audiência + dados para remarketing
└── Budget: R$40/dia

SEMANA 2 (Dias 8-14)
├── Continuar Campanha 1 — AWARENESS
├── Ativar Campanha 2 — TRÁFEGO (público frio quente)
├── Análise A/B de Awareness (pausar variação perdedora)
└── Budget total: R$70/dia

SEMANA 3 (Dias 15-21)
├── Otimizar Campanha 1 — AWARENESS (se necessário)
├── Continuar Campanha 2 — TRÁFEGO
├── Ativar Campanha 2 — Conjunto B (remarketing de engajamento)
├── Ativar Campanha 3 — CONVERSÃO (lookalike + remarketing LP)
└── Budget total: R$100/dia

SEMANA 4-6 (Dias 22-45)
├── Pausar ou reduzir Campanha 1 (awareness construída)
├── Manter Campanha 2 — TRÁFEGO (maior volume de audiência qualificada)
├── Escalar Campanha 3 — CONVERSÃO (onde custo por lead for menor)
└── Budget total: R$85-120/dia (ajustar conforme ROAS)
```

**Investimento total estimado — primeiros 45 dias:**

| Campanha | Orçamento | Dias ativos |
|----------|-----------|-------------|
| Awareness | R$ 600,00 | 15 dias |
| Tráfego | R$ 750,00 | 25 dias |
| Conversão | R$ 900,00 | 30 dias |
| **TOTAL** | **R$ 2.250,00** | **45 dias** |

---

## HIERARQUIA COMPLETA DE CAMPANHAS

```
CONTA META ADS
│
├── CAMPANHA 1: [CN] Awareness — Conheça o Refúgio
│   └── Conjunto: [CN-AW] Público Frio — Interesses Turismo
│       ├── Anúncio AW-01 (Feed estático)
│       └── Anúncio AW-02 (Stories/Reels)
│
├── CAMPANHA 2: [CN] Tráfego — Descubra a Casa Nativa
│   ├── Conjunto A: [CN-TR] Frio Quente — Interesses Refinados
│   │   ├── Anúncio TR-01 (Carrossel)
│   │   └── Anúncio TR-02 (Stories)
│   └── Conjunto B: [CN-TR] Remarketing — Engajamento Instagram
│       ├── Anúncio TR-01 (Carrossel)
│       └── Anúncio TR-02 (Stories)
│
└── CAMPANHA 3: [CN] Conversão — Reserve sua Experiência
    ├── Conjunto A: [CN-CV] Lookalike 1-3%
    │   ├── Anúncio CV-01 (Feed retrato)
    │   └── Anúncio CV-02 (Stories urgência)
    ├── Conjunto B: [CN-CV] Remarketing — Visitantes LP 30 dias
    │   ├── Anúncio CV-01 (Feed retrato)
    │   └── Anúncio CV-02 (Stories urgência)
    └── Conjunto C: [CN-CV] Remarketing Quente — LP 7 dias
        └── Anúncio CV-02 (Stories urgência — urgência máxima)
```

---

## CHECKLIST PRÉ-LANÇAMENTO

### Infraestrutura (responsabilidade: João)

- [ ] **Pixel Meta instalado** na landing page e verificado via Meta Pixel Helper
- [ ] **Eventos de pixel configurados:** PageView, Lead (formulário), ViewContent (botão Airbnb)
- [ ] **Conta Meta Ads autenticada** e com método de pagamento ativo
- [ ] **Página do Facebook** criada e conectada à conta de anúncios
- [ ] **Perfil Instagram** conectado à conta de anúncios
- [ ] **Domínio verificado** no Meta Business Suite (necessário para pixel de conversão)

### Criativos (responsabilidade: Designer + João)

- [ ] **AW-01** — Feed estático 1080×1080 aprovado
- [ ] **AW-02** — Stories/Reels 1080×1920 aprovado
- [ ] **TR-01** — Carrossel 4 cards 1080×1080 aprovado
- [ ] **TR-02** — Stories sequenciais (3x) 1080×1920 aprovados
- [ ] **CV-01** — Feed retrato 1080×1350 aprovado
- [ ] **CV-02** — Stories urgência 1080×1920 aprovado
- [ ] Todos os arquivos em **formato correto** (JPG/PNG para estático, MP4 para vídeo)
- [ ] Arquivos abaixo do **limite de texto sobre imagem** (Meta recomenda < 20% de texto)

### Copies e URLs

- [ ] **Copies aprovadas** por João conforme documento `2026-04-09_ad-copies-meta.md`
- [ ] **URL da landing page** finalizada e no ar
- [ ] **UTMs configuradas** para todos os criativos (conforme tabela acima)
- [ ] **Orçamento aprovado** por João (R$ 2.250,00 para 45 dias)

### Landing Page

- [ ] **LP no ar** com domínio final (não localhost)
- [ ] **Formulário de pré-reserva** funcionando e enviando notificação para João
- [ ] **Velocidade de carregamento** < 3 segundos (verificar via PageSpeed Insights)
- [ ] **Versão mobile** testada e aprovada

---

## PLANO DE OTIMIZAÇÃO SEMANAL

### Semana 1 — Baseline
- Monitorar: CPM, frequência, alcance
- Não mexer em nada — deixar o algoritmo aprender
- Revisar: se CPM > R$40, avaliar reduzir segmentação ou pausar placement mais caro

### Semana 2 — Primeiros Ajustes
- Pausar variação de Awareness perdedora no A/B
- Ativar Campanha de Tráfego
- Verificar: se CTR < 0,8%, trocar criativo principal

### Semana 3 — Escalonamento Inicial
- Se CPC < R$2,00: aumentar budget de Tráfego em +30%
- Ativar Campanha de Conversão
- Criar audiência de remarketing de visitantes LP (min. 100 visitantes)

### Semana 4+ — Otimização Contínua
- Pausar criativos com CTR < 0,5% (abaixo da média)
- Testar novos criativos se os originais esgotarem (frequência > 5x)
- Avaliar se escalar Conversão ou manter Tráfego como principal alimentador
- Reunião semanal de performance com João (15min — sexta-feira)

### Sinais para Escalar (aumentar budget)
- CPL < R$20,00 → aumentar budget de Conversão em +50%
- ROAS > 5x → dobrar budget de Conversão
- CTR > 2,5% → duplicar conjunto de anúncios ganhador

### Sinais para Pausar (reduzir ou pausar)
- CPL > R$60,00 após 7 dias → pausar conjunto e revisar criativo/público
- Frequência > 6x → pausar para evitar saturação
- CTR < 0,5% → pausar criativo e substituir

---

*Documento gerado em: 09/04/2026*
*ads-manager — Casa Nativa Operation*
