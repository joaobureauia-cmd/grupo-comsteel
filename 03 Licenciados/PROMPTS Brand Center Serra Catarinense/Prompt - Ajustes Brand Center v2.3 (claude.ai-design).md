# Prompt de Ajustes para Claude Design — Brand Center Serra Catarinense v2.3

> **Como usar:**
> 1. Mantenha o deck atual aberto.
> 2. Anexe **2 imagens** no chat, **nesta ordem exata**:
>    - **Anexo #1** — PNG sem fundo (transparente) da Tiny Office London com pergola, vidros amplos e plantas no canto direito. **Esta vai no Slide 2.**
>    - **Anexo #2** — Render full-color da Tiny Office London em ambiente natural, golden hour, com gramado e árvores ao redor. **Esta vai no Slide 17.**
> 3. Copie tudo entre `=== INÍCIO DO PROMPT ===` e `=== FIM DO PROMPT ===` e cole.
>
> **Observação:** este prompt corrige apenas dois erros pontuais. Não regenere o deck inteiro.

---

=== INÍCIO DO PROMPT ===

Aplique as duas correções abaixo no deck "Brand Center · Licenciados Gustavo & Guilherme · Serra Catarinense". **Não regenere o deck inteiro.** Aplique apenas as correções listadas. Tudo o que não for mencionado, mantenha exatamente como está.

---

## A. CORREÇÃO CRÍTICA — TROCA DE IMAGENS ENTRE SLIDES 2 E 17

Na versão atual do deck, as imagens dos slides 2 e 17 estão **invertidas**. Vamos corrigir.

### SLIDE 2 — CAPA OFICIAL

A imagem que está hoje no Slide 2 mostra a Tiny em ambiente natural com gramado, árvores e céu — **isso está errado**, essa imagem pertence ao Slide 17.

**Ação:**
1. **Remova a imagem atual do Slide 2** (a Tiny em ambiente natural).
2. **Coloque no Slide 2** a imagem **Anexo #1** — PNG sem fundo (transparente) da **Tiny Office London** com pergola, vidros amplos iluminados por dentro e plantas no canto direito. Essa imagem tem fundo transparente/escuro e foi feita exatamente para ser usada sobre fundo preto.
3. **Mantenha todo o layout, tipografia e elementos auxiliares do Slide 2 exatamente como estão** (BRAND CENTER · LICENCIADOS PREMIUM no topo-esquerdo, SERRA CATARINENSE · 2026 no topo-direito, GUSTAVO & GUILHERME centralizado, lockup de logos no rodapé esquerdo, DUAS MARCAS · UM PACOTE no rodapé direito). Só troque a imagem.

### SLIDE 17 — SEU ATIVO · TINY OFFICE LONDON

A imagem que está hoje no Slide 17 mostra a Tiny isolada em PNG escuro com pergola e plantas no canto — **isso está errado**, essa imagem pertence ao Slide 2.

**Ação:**
1. **Remova a imagem atual do Slide 17** (a Tiny em PNG escuro).
2. **Coloque no Slide 17** a imagem **Anexo #2** — render full-color da **Tiny Office London** em ambiente natural, golden hour, com gramado e árvores ao redor.
3. **Mantenha todo o layout, tipografia e bloco de texto à direita do Slide 17 exatamente como estão** (headline "Seu Showroom Chega Pronto", specs Office London · 23 m² · 7 × 3,20 m · 3 m de altura, três funções simultâneas, citação *"É usufruir, não construir."*). Só troque a imagem.

---

## B. CORREÇÃO CRÍTICA — INVERSÃO DE LOGOS

**Problema atual:** os logos estão sendo renderizados com a versão errada para cada fundo, ficando **invisíveis ou quase invisíveis**:
- Em slides de **fundo preto/escuro**, o logo está com o estilo **escrito em escuro/preto** — fica invisível.
- Em slides de **fundo branco/claro**, o logo está com o estilo **escrito em branco** — fica invisível.

**Está exatamente ao contrário do que deveria ser.**

### Instrução por aparência (não confie no nome do arquivo)

Esqueça o nome dos arquivos na pasta de assets. **Identifique cada versão do logo pela aparência real:**

- **Versão BRANCA do logo:** o nome "COMSTEEL" aparece em letras BRANCAS. **Esta versão SÓ pode aparecer sobre fundos pretos, tabaco ou escuros.** Sobre fundo branco, ela some.
- **Versão PRETA do logo:** o nome "COMSTEEL" aparece em letras PRETAS ou escuras. **Esta versão SÓ pode aparecer sobre fundos brancos, bege ou claros.** Sobre fundo preto, ela some.

### Regra inegociável

| Fundo do slide | Versão do logo a usar | Como verificar |
|---|---|---|
| Preto `#000000` | Versão com texto **BRANCO** | O nome "COMSTEEL" deve ler claramente sobre o preto |
| Branco `#FFFFFF` | Versão com texto **PRETO** | O nome "COMSTEEL" deve ler claramente sobre o branco |
| Tabaco `#3a240d` | Versão com texto **BRANCO** | O nome "COMSTEEL" deve ler claramente sobre o tabaco |
| Bege `#8b7050` | Versão com texto **PRETO** | O nome "COMSTEEL" deve ler claramente sobre o bege |

### Ação obrigatória

1. **Revise cada slide do deck que contém logo.** Para cada um, verifique se o nome "COMSTEEL" está legível sobre o fundo do slide.
2. Se NÃO estiver legível → **troque pela versão oposta do logo** (a outra variante disponível na pasta de assets, identificada visualmente, não pelo nome do arquivo).
3. Faça isso para **as duas marcas** (Construção & Mobilidade e Tiny House) em todos os slides onde aparecem.

### Slides a verificar (todos os que contêm logo)

- Slide 2 (capa Office London) — fundo preto → logos do lockup devem ler em BRANCO
- Slide 6 (duas marcas, um pacote) — lado preto: logo branco; lado tabaco: logo branco Tiny House
- Slide 7 (Identidade Construção) — fundo preto → logo branco
- Slide 8 (Identidade Tiny) — fundo tabaco → logo branco Tiny House
- Slide 17 (Seu ativo Tiny Office London) — fundo tabaco no bloco direito → logo branco Tiny House
- Slide 18 (Território) — fundo preto → logo branco
- Slide 21 (Encerramento) — fundo preto → logos do lockup devem ler em BRANCO

E qualquer outro slide com logo que não esteja na lista acima.

---

## C. CHECKLIST FINAL

- [ ] Slide 2 agora exibe o PNG da Tiny Office London com pergola e plantas (Anexo #1), sobre fundo preto, sem ambiente natural.
- [ ] Slide 17 agora exibe o render da Tiny em ambiente natural golden hour (Anexo #2), com gramado e árvores.
- [ ] Em **todos** os slides de fundo preto, o nome "COMSTEEL" do logo lê em **branco** e está claramente visível.
- [ ] Em **todos** os slides de fundo branco, o nome "COMSTEEL" do logo lê em **preto** e está claramente visível.
- [ ] Em **todos** os slides de fundo tabaco, o logo Tiny House lê em **branco**.
- [ ] Nenhum logo está invisível, semi-invisível ou se confundindo com o fundo.
- [ ] Todos os demais slides permanecem idênticos.

=== FIM DO PROMPT ===
