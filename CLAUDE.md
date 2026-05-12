# CLAUDE.md — Arquivo Mestre do Grupo Comsteel

> Este arquivo é lido automaticamente pelo Claude Code ao abrir qualquer sessão neste diretório.
> Ele define comportamento, contexto, hierarquia de memória e regras de trabalho para todas as tarefas envolvendo o Grupo Comsteel.

---

## 1. QUEM É O GRUPO COMSTEEL

O **Grupo Comsteel** é uma plataforma de construção industrializada em **Light Steel Frame**, com fábrica em **Novo Hamburgo/RS**. Nasceu da reformulação completa da Encaixetec (20 anos de know-how) em outubro de 2024, lançada como Comsteel em 2025.

**Duas unidades de negócio:**
- **Comsteel Construção & Mobilidade** — construtora em Steel Frame do projeto à execução (B2C via arquitetos + B2B MCMV + projetos padronizados)
- **Comsteel Tiny House** — módulos habitacionais transportáveis plug and play, 7 a 29 m², para todo o Brasil

**Liderança:** Ramão (Dir. Comercial e Marketing) · Felipe (Dir. Engenharia) · Luis Maldaner (Arquiteto Parceiro)

**Sites:** comsteel.com.br | comsteeltinyhouse.com.br

---

## 2. ESTRUTURA DE DIRETÓRIOS

```
Grupo Comsteel /
│
├── CLAUDE.md                          ← ESTE ARQUIVO (leia sempre primeiro)
│
├── 00 Documentos Estratégicos/
│   ├── Comsteel Documento.md          ← FONTE PRIMÁRIA DE VERDADE (leia em qualquer dúvida)
│   ├── Comsteel Documento.pdf         ← versão PDF do mesmo documento
│   └── Apresentação Prefeitura Novo Hamburgo/
│       ├── Comsteel · Apresentação Prefeitura de Novo Hamburgo.pdf
│       ├── Prompt - Apresentacao Prefeito Novo Hamburgo (claude.ai-design).md
│       ├── Prompt - Ajustes Apresentacao Prefeito (claude.ai-design).md
│       └── html/                      ← apresentação em HTML interativo (deck)
│
├── 01 Comsteel Construção & Mobilidade/
│   ├── 01 - Arquivos e fotos Institucionais/
│   │   ├── Dados Cadastrais Com Steel.pdf
│   │   └── FAQ COMSTEEL .pdf
│   ├── 02 - Marketing e Comunicação/
│   │   ├── Catálogos de Projetos Prontos/   ← Casa Ibiza.pdf, Casas Standard.pdf, Catálogo Casas MCMV.pdf
│   │   └── Identidade Visual/Logos Comsteel Construção/
│   └── 03 - Portfólio de Construções/       ← fotos reais de obras (CASA VIANA, G17, G23, BOSQUE, etc.)
│
├── 02 Comsteel Tiny House/
│   ├── 02 - Marketing e Comunicação/
│   │   ├── Catálogos Comsteel tiny House/   ← catálogo completo de modelos
│   │   ├── Logos Comsteel tiny house/
│   │   └── Identidade visual.pdf
│   └── Projetos Tiny's- Renders e Plantas/  ← renders por modelo (Marrocos, Natura, London, etc.)
│
├── 03 Licenciados/                          ← materiais do modelo de licenciamento
│
├── Casa Nativa/                             ← projeto separado (vale dos vinhedos), tem CLAUDE.md próprio
│   └── vale-dos-vinhedos-casa-nativa-operacao/CLAUDE.md
│
├── Curso Comsteel/                          ← [PREENCHER: conteúdo do curso]
│
├── Hub de Arquitetos/                       ← Programa Arquiteto Sócio-Construtivo + Sociedade Construtiva
│   ├── README.md                            ← visão geral do Hub e índice
│   ├── programa/
│   │   ├── programa_socio_construtivo.md    ← os 6 blocos do programa (conceito completo)
│   │   ├── sociedade_construtiva.md         ← ecossistema da Sociedade Construtiva
│   │   └── selecao_10_modulares.md         ← critérios e processo de seleção do cluster
│   ├── remuneracao_e_visibilidade.md        ← modelo de remuneração e benefícios
│   ├── captacao/
│   │   ├── pitch_para_arquitetos.md         ← scripts de abordagem por estágio
│   │   └── cadencia_outbound.md            ← canais e cadência de prospecção
│   └── treinamento/
│       └── steel_select_arquitetos.md       ← Steel Select adaptado para arquitetos e engenheiros
│
└── context/                                 ← REPOSITÓRIO DE CONTEXTO ESTRATÉGICO
    ├── README.md                            ← índice e instruções de uso
    ├── company.md
    ├── products.md
    ├── narrative.md
    ├── competitive_positioning.md
    ├── market_context.md
    ├── sales_playbook.md
    ├── personas/
    │   ├── investidor_imobiliario.md
    │   ├── arquiteto_parceiro.md
    │   ├── cliente_final_moradia.md
    │   ├── proprietario_pousada.md
    │   └── licenciado_potencial.md
    ├── channels/
    │   ├── outbound.md
    │   ├── inbound.md
    │   └── partnerships.md
    └── assets/
        └── key_messages.md
```

---

## 3. HIERARQUIA DE MEMÓRIA E FONTES DE VERDADE

Ao realizar qualquer tarefa, respeite esta ordem de prioridade:

```
1º  CLAUDE.md (este arquivo)               — regras de comportamento e estrutura
2º  context/README.md                      — índice do repositório estratégico
3º  00 Documentos Estratégicos/
    Comsteel Documento.md                  — fonte primária de verdade institucional
4º  context/*.md                           — documentos estratégicos elaborados
5º  01, 02, 03 (pastas de produto)         — catálogos, renders, portfólio
```

**Regra:** Em caso de conflito entre fontes, o `Comsteel Documento.md` prevalece sobre qualquer outra. O `CLAUDE.md` prevalece sobre tudo em questão de comportamento.

### Qual arquivo ler para cada tipo de tarefa:

| Tarefa | Arquivos a ler |
|---|---|
| Apresentação institucional | `Comsteel Documento.md` + `context/company.md` + `context/narrative.md` |
| Material de vendas (qualquer) | `context/sales_playbook.md` + persona relevante + `context/assets/key_messages.md` |
| Licenciamento | `Comsteel Documento.md` (seção 6) + `context/personas/licenciado_potencial.md` + `context/sales_playbook.md` |
| Conteúdo Construção & Mobilidade | `context/products.md` + `context/narrative.md` + `context/channels/` |
| Conteúdo Tiny House | `context/products.md` + `context/narrative.md` + persona relevante |
| Posicionamento / SWOT | `context/competitive_positioning.md` + `context/market_context.md` |
| Parcerias (arquitetos, imobiliárias) | `context/channels/partnerships.md` + persona relevante |
| Hub de Arquitetos / Sociedade Construtiva | `Hub de Arquitetos/README.md` → arquivos específicos do programa |
| Pitch para arquiteto parceiro | `Hub de Arquitetos/captacao/pitch_para_arquitetos.md` + `context/personas/arquiteto_parceiro.md` |
| SEO / Inbound | `context/channels/inbound.md` + `context/products.md` |
| Prospecção / Outreach | `context/channels/outbound.md` + persona alvo |
| Pitch para investidor | `Comsteel Documento.md` (seção 6) + `context/competitive_positioning.md` + `context/assets/key_messages.md` |

---

## 4. REGRAS DE IDENTIDADE VISUAL — CRÍTICO

**NUNCA misture as duas paletas em um mesmo material. Esta é a regra mais importante de design.**

### Comsteel Construção & Mobilidade

| Elemento | Valor |
|---|---|
| Fundo de destaque | Preto `#000000` |
| Cor de acento | Laranja-cobre `#D86B28` / `#F07F08` |
| Texto principal | Branco `#FFFFFF` |
| Texto secundário | Cinza `#949494` |
| Tipografia | Sans-serif geométrica, títulos em CAIXA ALTA, letter-spacing negativo |
| Estilo | Minimalista-premium, grandes blocos full-width, alternância preto/branco |

### Comsteel Tiny House

| Elemento | Valor |
|---|---|
| Fundo de destaque | Marrom tabaco `#3a240d` |
| Fundo principal | Bege/creme `#8b7050` |
| Cor de acento | Marrom médio/cobre `rgb(135, 108, 77)` |
| Texto principal | Branco `#FFFFFF` ou Preto `#000000` |
| Tipografia | Madefor Display Bold (títulos), Helvetica Light/Neue (corpo) |
| Estilo | Editorial, tela cheia, muito espaço em branco, fotografia cinematográfica em natureza |
| Itálico | Usar em palavras-chave: *usufruir, refúgio, lifestyle, design* |

---

## 5. DIRETRIZES DE TOM DE VOZ

### Construção & Mobilidade — Tom

- **Aspiracional e assertivo.** Protagonista da transformação do setor, não "mais uma construtora".
- **Imperativo convidativo.** Frases curtas e impactantes. Sem arrogância.
- **Técnico, mas acessível.** Equilibra Steel Frame, perfis galvanizados, NBRs com argumentos emocionais.
- **Provocativo + educativo.** Questiona o status quo da alvenaria, depois apresenta a solução.
- **Valores:** inovação, eficiência, sustentabilidade, sofisticação.
- **Exemplos de frases corretas:** "A Nova Realidade da Construção." / "Opte por Inovar." / "Construção Inteligente."
- **Evitar:** informalidade excessiva, promessas sem base em dados, linguagem genérica de construtora.

### Tiny House — Tom

- **Aspiracional e poético.** Vende sensações e estilo de vida, não produto.
- **Conceito central (repetir em todo material):** "É usufruir, não construir."
- **Direto e confiante.** Frases curtas e afirmativas.
- **Orientado a investimento** na camada B2B: "rendimento mensal de até 5%", "mercado em ascensão".
- **Inglês pontual e estratégico:** *lifestyle, design, office* — reforça premium internacional.
- **Exemplos de frases corretas:** "Refúgio que se adapta à vida." / "Descanso que você merece." / "Sua Tiny House chega até você pronta para *usufruir*."
- **Evitar:** linguagem de construção civil, jargões técnicos excessivos, mistura com paleta Construção.

---

## 6. ARGUMENTOS INSTITUCIONAIS — SEMPRE DISPONÍVEIS

Use estes argumentos como âncoras em qualquer material:

1. **20 anos de know-how construtivo** — histórico real, não promessa
2. **Conformidade NBR completa** — NBR 15.575, NBR 16.285, NBR 8.802
3. **Ganhos vs. alvenaria** — 50% mais rápido | 90% menos resíduo | custo previsível
4. **Tração B2B real** — Steel Corp (50 + 75 casas MCMV) + Espaço Smart (4 casas)
5. **Fábrica própria em Novo Hamburgo** — controle total do off-site (59% do custo)
6. **Mercado em crescimento** — Steel Frame ~2% da construção BR, crescendo 27%/ano

---

## 7. MODULARIZAÇÃO E EFICIÊNCIA

### Projeto Casa Nativa — Atenção Especial

A pasta `Casa Nativa/vale-dos-vinhedos-casa-nativa-operacao/` é um **subprojeto independente** com CLAUDE.md próprio. Ao trabalhar em tarefas da Casa Nativa:
- Abra o Claude Code **dentro** dessa pasta
- O CLAUDE.md dela prevalece sobre este para tarefas específicas da Casa Nativa
- Não misture contexto da Casa Nativa com o Grupo Comsteel principal

### Reutilização de materiais existentes

Antes de criar qualquer apresentação, verifique se já existe material reutilizável:
- Catálogos PDF prontos: `01 Comsteel Construção & Mobilidade/02 - Marketing e Comunicação/Catálogos de Projetos Prontos/`
- Renders e plantas: `01 Comsteel Construção & Mobilidade/03 - Projetos e Plantas/` e `02 Comsteel Tiny House/Projetos Tiny's- Renders e Plantas/`
- Portfólio fotográfico: `01 Comsteel Construção & Mobilidade/03 - Portfólio de Construções/`
- Apresentação HTML interativa (deck prefeitura): `00 Documentos Estratégicos/Apresentação Prefeitura Novo Hamburgo/html/`

### Criação de novos materiais

Ao criar apresentações, decks ou documentos:
1. Verifique identidade visual correta (seção 4 deste arquivo)
2. Consulte `context/assets/key_messages.md` para taglines e mensagens prontas
3. Use portfólio fotográfico real — **nunca use stock photos ou clipart**
4. Identifique a persona-alvo antes de definir o tom (seção 5)
5. Para licenciamento: material deve ser **vendedor**, não institucional — números concretos, projeções, ROI

---

## 8. CULTURA COMERCIAL — "O CLIENTE JÁ PESQUISOU"

Todo material de vendas, script, pitch ou template produzido para o time comercial da Comsteel deve seguir estes quatro pilares:

**1. Diagnostique, não convença**
O cliente pesquisou o concorrente, comparou preço, leu review. Ele sabe. Scripts que começam apresentando o produto estão errados. Scripts corretos começam com uma pergunta que mapeia a dor real.
- Toda conversa começa com 1-3 perguntas de diagnóstico antes de qualquer apresentação
- O vendedor fala menos de 30% do tempo nos primeiros 10 minutos

**2. Venda consequência, não característica**
- ❌ "Steel Frame é 50% mais rápido." → ✅ "Cada mês de atraso numa obra convencional é retorno perdido. Com 90 dias garantidos, você sabe exatamente quando começa a receber."
- ❌ "Tiny House instalada em 1 dia." → ✅ "Sua pousada expande capacidade neste fim de semana de alta temporada — sem perder uma reserva para o concorrente."

**3. Respeito intelectual — profundidade com objetividade**
Simplificar demais gera desconfiança. Complicar demais gera desinteresse. Toda afirmação deve ter número, prazo ou caso real. Trate o interlocutor como alguém que consegue analisar planilha de ROI e ler cláusula de contrato — porque provavelmente consegue.

**4. Autoridade real — prova fecha, marketing abre**
O vendedor Comsteel deve saber de cor:
- 3 casos de obra com prazo e resultado documentados
- Steel Corp: 50 casas Muçum + 75 Bom Retiro do Sul | Espaço Smart: 4 Cruzeiro do Sul
- Dados de mercado: Steel Frame = 2% da construção BR, crescendo 27%/ano
- R$55M em orçamentos recebidos em 1 ano, 10% de conversão

**Aplicação ao gerar materiais:**
- E-mails e DMs: abrir com a dor do lead ou um dado que para a atenção — nunca com "somos a Comsteel e trabalhamos com..."
- Pitches: estrutura = dado de autoridade → diagnóstico → consequência → processo → próximo passo
- Decks: cada slide tem um dado real, não apenas uma promessa
- Objeções: sempre diagnosticar o que está por trás antes de responder

---

## 9. REGRAS AVANÇADAS DE TRABALHO

### Sobre os campos [PREENCHER]

Os arquivos em `context/` contêm campos marcados com `[PREENCHER: descrição]`. Ao encontrá-los:
- **Não invente valores.** Sinalize que o campo precisa ser preenchido.
- Se o usuário fornecer o valor, atualize o arquivo correspondente imediatamente.
- Campos prioritários para preencher: CNPJ, endereço da fábrica, faturamento, contatos comerciais, preço por m².

### Sobre dados financeiros e métricas

Só use dados financeiros que constem no `Comsteel Documento.md` ou que o usuário confirme explicitamente:
- R$55M em orçamentos enviados (1 ano), 10% de conversão ✓
- R$220k — investimento Licenciamento Master ✓
- 4% royalties + 2% fundo marketing ✓
- Meta: 15 Masters/ano → R$3,3M faturamento, R$1,5M lucro bruto ✓
- Steel Frame: ~2% da construção BR, crescendo 27%/ano ✓

**Nunca prometa números ou benefícios fiscais não documentados.**

### Sobre o modelo de licenciamento

O licenciamento é o maior vetor de crescimento estratégico da Comsteel. Ao trabalhar em materiais de licenciamento:
- Tom deve ser **vendedor e orientado a ROI** — não institucional
- Perfil do licenciado ideal: ex-executivo/CEO/funcionário público com reserva financeira e rede local
- Programa de treinamento: **Steel Select**
- Destacar: não precisa de experiência em construção, fábrica própria ou capital antecipado
- A Tiny House inclusa no Master serve como **showroom + ativo de renda + ponto físico da marca**

### Sobre o MCMV

O MCMV é argumento de credibilidade B2B, não apenas assistencial. Use-o para:
- Provar capacidade de execução em escala
- Demonstrar conformidade normativa para contratos públicos
- Mostrar ao poder público que a Comsteel gera empregos locais e reduz déficit habitacional com qualidade

### Atualização do repositório

Quando novas informações relevantes surgirem (novos contratos, novos licenciados, novos produtos, dados de mercado), atualize os arquivos correspondentes em `context/`. O repositório deve refletir sempre o estado atual da empresa.

---

## 9. HUB DE ARQUITETOS — REFERÊNCIA RÁPIDA

O **Hub de Arquitetos** é o programa estratégico de captação e desenvolvimento de arquitetos parceiros. Documentação completa em `Hub de Arquitetos/`.

**Conceito-chave:** Arquiteto Sócio-Construtivo — o arquiteto não é só uma fonte de leads, é um parceiro de ecossistema (Sociedade Construtiva).

**Os dois eixos:**
1. **Geração de negócio** — arquitetos trazem projetos; Comsteel executa; arquiteto recebe comissão (2-4%)
2. **Cluster de Arquitetos Modulares** — 10-20 selecionados com visibilidade, Steel Select, indicações mútuas e potencial de se tornar referência no segmento

**Os 6 Blocos do programa:**
1. Consciência — trazer a tendência para o radar do arquiteto
2. Oportunidade — Steel Frame como novo segmento de mercado (não substituto)
3. Desmistificação — Steel Select resolve o gap técnico
4. Sociedade Construtiva — ecossistema, não comissão
5. Tendência — quem vai dominar o mercado habitacional
6. Seleção — os 10 Arquitetos Modulares

**Case de referência:** Felipe Sagace — arquiteto que virou referência nacional em construção industrializada; contratado pelo grupo Steel Corps.

**Comissionamento:**
- Indicação simples: **2%** sobre valor do contrato
- Parceria construtiva: **4%** sobre valor do contrato

---

## 10. PERSONAS RÁPIDAS — REFERÊNCIA

| Persona | Arquivo | Gatilho principal | Canal preferido |
|---|---|---|---|
| Investidor imobiliário | `context/personas/investidor_imobiliario.md` | ROI, renda passiva, escassez de terrenos | WhatsApp + reunião presencial |
| Arquiteto parceiro | `context/personas/arquiteto_parceiro.md` | Construtora confiável, prazo, qualidade técnica | LinkedIn + e-mail técnico |
| Cliente final (moradia) | `context/personas/cliente_final_moradia.md` | Prazo, preço previsível, visual moderno | Instagram + WhatsApp |
| Proprietário de pousada | `context/personas/proprietario_pousada.md` | Expansão sem obra longa, renda por módulo | WhatsApp + visita |
| Licenciado potencial | `context/personas/licenciado_potencial.md` | Negócio próprio, renda passiva, modelo estruturado | LinkedIn + evento |

---

## 11. CHECKLIST DE INÍCIO DE SESSÃO

Ao iniciar uma nova sessão com tarefa específica, verifique:

- [ ] Qual unidade de negócio está sendo trabalhada? (Construção / Tiny House / Licenciamento / ambas)
- [ ] Qual persona ou interlocutor é o alvo?
- [ ] Qual paleta de cores e tom de voz se aplica?
- [ ] Existe material já pronto que pode ser reutilizado ou adaptado?
- [ ] Algum dado financeiro ou técnico precisa ser confirmado antes de usar?
- [ ] O resultado final mistura paletas? (Se sim: **corrigir**)

---

*CLAUDE.md — Grupo Comsteel. Última atualização: 2026-04-29. Mantenha atualizado a cada mudança estrutural no projeto.*
