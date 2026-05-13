# Prompt de Ajustes para Claude Design — Brand Center Serra Catarinense v2.1

> **Como usar:**
> 1. Mantenha o deck atual aberto (versão gerada com o prompt v2).
> 2. Anexe **4 novas imagens** no chat, **nesta ordem exata**:
>    - **Anexo #3** — fotografia para o Slide 7 (Identidade Construção & Mobilidade)
>    - **Anexo #4** — fotografia para o Slide 8 (Identidade Tiny House)
>    - **Anexo #5** — mockup de feed Instagram para o Slide 14 (Marketing)
>    - **Anexo #6** — fotografia/render de fundo para o Slide 17 (Tiny Office Venus)
> 3. Copie tudo entre `=== INÍCIO DO PROMPT ===` e `=== FIM DO PROMPT ===` e cole no Claude Design.
>
> **Observação:** este NÃO é um prompt de reconstrução completa do deck. É um prompt de ajustes pontuais. Aplique apenas as alterações listadas abaixo. Tudo o que não for explicitamente alterado, mantenha exatamente como está no deck atual.

---

=== INÍCIO DO PROMPT ===

Aplique os ajustes abaixo no deck "Brand Center · Licenciados Gustavo & Guilherme · Serra Catarinense" que já está gerado. **Não regenere o deck inteiro.** Apenas aplique as correções listadas, slide por slide. Mantenha tudo o mais idêntico ao que já existe.

---

## A. CORREÇÃO GLOBAL E CRÍTICA — LOGOS

Esta correção se aplica a **TODOS os slides do deck**.

**Contexto:** os logos atualmente em uso no deck vieram do upload original do Design System no GitHub. Eles estão em formato vetor pequeno e estão sendo renderizados em tamanho minúsculo, ilegíveis em vários slides.

**O que eu fiz:** adicionei manualmente, dentro da pasta de **assets** do Design System aqui no Claude Design, **duas novas pastas** contendo os logos corretos em PNG, em alta resolução:
- **`Logos Comsteel Construção e Mobilidade`** — contém o logo da Comsteel Construção & Mobilidade em todas as versões (branco, preto, laranja).
- **`Logos Comsteel Tiny House`** — contém o logo da Comsteel Tiny House em todas as versões (branco, tabaco, preto).

**Ação obrigatória:** **substitua TODOS os logos do deck** pelos PNGs das duas pastas novas acima. **Use a versão correta de cada logo** conforme o fundo do slide:
- Fundo preto → logo versão **branca**
- Fundo branco → logo versão **preta**
- Fundo tabaco → logo versão **branca** (Tiny House) ou versão **branca** (Construção)
- Fundo bege → logo versão **preta** (Tiny House)

**Tamanho mínimo de exibição dos logos** (largura do logo em relação à largura do slide):
- **Logo em rodapé/canto discreto** (informativo): **mínimo 8% da largura do slide** (~150px em 16:9 1920×1080)
- **Logo em lockup duplo** (Construção + Tiny juntos): **mínimo 12% da largura do slide** para cada logo
- **Logo em slide de identidade** (slide 7 e slide 8, onde a marca é o sujeito): **mínimo 20% da largura do slide** — o logo deve ser claramente visível e legível
- **Logo na capa (Slide 2) e encerramento (Slide 21)**: lockup das duas marcas com **mínimo 14% da largura do slide para cada logo**

**Slides afetados (TODOS os que contêm logo):** Slide 2 (capa Office Venus), Slide 6 (duas marcas), Slide 7 (Identidade Construção), Slide 8 (Identidade Tiny), Slide 17 (Office Venus), Slide 18 (Território), Slide 21 (Encerramento), e qualquer outro slide que tenha logo.

> **Importante:** o **Slide 1 NÃO precisa de logo adicional** — o logo Comsteel Construção & Mobilidade já está embutido no rodapé da Imagem 2 (mapa). Não adicione outro logo.

---

## B. AJUSTES POR SLIDE

### SLIDE 1 — CAPA DE BOAS-VINDAS (mapa Serra Catarinense)

**Problema atual:**
- O bloco "SEJAM BEM-VINDOS, GUSTAVO & GUILHERME." está posicionado no terço superior-esquerdo do slide e está **sobrepondo o mapa de Santa Catarina** (em especial, "GUILHERME" cobre a região Serra Catarinense em laranja).
- A tagline "Agora vocês fazem parte da família Comsteel." está em branco com opacidade reduzida e tipografia pequena — **passa batido**, não chama atenção.

**Ajuste a fazer:**

1. **Reposicione todo o stack de texto** (linha 1 "SEJAM BEM-VINDOS,", linha 2 "GUSTAVO & GUILHERME.", linha 3 tagline) para o **canto inferior-esquerdo** do slide, em uma área onde NÃO haja sobreposição com o mapa.
2. **Reduza o tamanho da tipografia** do título principal em ~30–40% em relação ao atual. As linhas "SEJAM BEM-VINDOS, GUSTAVO & GUILHERME." devem caber confortavelmente no espaço preto disponível na parte inferior-esquerda, sem encostar no mapa nem no logo Comsteel embutido no rodapé central.
3. **Realce a tagline** "Agora vocês fazem parte da família Comsteel.":
   - Aumentar o tamanho da fonte (~30–35px de altura, próximo do tamanho usado para "BRAND CENTER · LICENCIADOS PREMIUM · 12.05.2026" no topo).
   - Cor: **branco puro `#FFFFFF`** (sem opacidade reduzida).
   - Peso: **medium ou semibold** — não pode ficar como texto secundário, é a frase que arremata a saudação.
4. **Mantenha** o pré-título "BRAND CENTER · LICENCIADOS PREMIUM · 12.05.2026" exatamente onde está (topo-esquerda, laranja, pequeno).
5. **Mantenha** o destaque em laranja `#D86B28` nos nomes "GUSTAVO & GUILHERME." — só reduza o tamanho.

**Hierarquia visual final do Slide 1:**
- Topo-esquerda: pré-título laranja pequeno (já está)
- Inferior-esquerda: SEJAM BEM-VINDOS, / GUSTAVO & GUILHERME. (reduzido) / Agora vocês fazem parte da família Comsteel. (aumentado, branco sólido)
- Centro: mapa intacto, sem sobreposição
- Rodapé central: logo Comsteel embutido na imagem (não mexer)

---

### SLIDE 2 — CAPA OFICIAL (Office Venus)

**Problema atual:**
- "GUSTAVO & GUILHERME." está dimensionado corretamente, mas a base do texto **encosta no telhado do módulo Tiny Office Venus**.
- "SERRA CATARINENSE · 2026" está posicionada à esquerda, mid-altura, e **sobrepõe a fachada esquerda do módulo**.
- Existe um "COMSTEEL · 2026" no canto superior-direito que é redundante (a marca já aparece nos logos do rodapé).

**Ajuste a fazer:**

1. **Mova "GUSTAVO & GUILHERME." para cima** em ~80–120px (cerca de 8–10% da altura do slide) — o suficiente para que a base da letra "G" de GUILHERME tenha um respiro mínimo de 60px até o telhado do módulo.
2. **Remova "COMSTEEL · 2026" do canto superior-direito.**
3. **Mova "SERRA CATARINENSE · 2026" para o canto superior-direito**, ocupando o espaço onde estava "COMSTEEL · 2026". Mesma tipografia em cinza claro, alinhamento à direita.
4. **Substitua o lockup de logos no canto inferior-esquerdo** pelos logos das pastas novas (ver seção A acima):
   - Logo Comsteel Construção & Mobilidade (versão branca) — à esquerda
   - Linha vertical fina conectora (manter)
   - Logo Comsteel Tiny House (versão branca) — à direita
   - Cada logo com mínimo 14% da largura do slide.
5. **Mantenha "DUAS MARCAS · UM PACOTE"** no canto inferior-direito (está bom).
6. **Mantenha "BRAND CENTER · LICENCIADOS PREMIUM"** no canto superior-esquerdo (está bom).

---

### SLIDE 7 — IDENTIDADE VISUAL · CONSTRUÇÃO & MOBILIDADE

**Ajuste a fazer:**

1. **Substitua a fotografia/imagem atual** desse slide pela imagem **Anexo #3** (anexada para esta sessão de ajustes).
2. Mantenha todo o resto do slide intacto: headline, paleta de cores, descrição de tipografia, descrição de layout.
3. **Aplique também a substituição do logo** se houver logo no slide (ver seção A — logo branco sobre fundo preto, mínimo 20% da largura do slide).

---

### SLIDE 8 — IDENTIDADE VISUAL · TINY HOUSE

**Ajuste a fazer:**

1. **Substitua a fotografia/imagem atual** desse slide pela imagem **Anexo #4** (anexada para esta sessão de ajustes).
2. Mantenha o resto intacto: headline em Title Case, paleta tabaco/bege/cobre, descrição de tipografia Madefor Display, descrição de layout editorial.
3. **Aplique também a substituição do logo** se houver logo no slide (ver seção A — logo Tiny House versão branca sobre fundo tabaco, mínimo 20% da largura do slide).

---

### SLIDE 14 — MARKETING

**Ajuste a fazer:**

1. **Substitua o mockup de feed Instagram** que está à direita do slide pela imagem **Anexo #5** (anexada para esta sessão de ajustes).
2. Mantenha o resto do slide intacto: headline "MARKETING.", lista de bullets à esquerda, identidade Construção & Mobilidade (fundo preto, acento laranja).

---

### SLIDE 17 — SEU ATIVO · TINY OFFICE VENUS

**Ajuste a fazer:**

1. **Substitua a imagem de fundo do lado esquerdo** do slide pela imagem **Anexo #6** (anexada para esta sessão de ajustes).
2. **Remova qualquer PNG/recorte da Tiny House** que esteja sobreposto ao fundo — o Anexo #6 já contém a composição completa (Tiny + ambiente natural). Não sobreponha um segundo render.
3. Mantenha o resto do slide intacto: identidade Tiny House (fundo tabaco no bloco direito de texto), headline em Title Case "Seu Showroom Chega Pronto.", bloco de texto à direita com especificações + 3 funções simultâneas, citação em itálico *"É usufruir, não construir."*
4. **Aplique também a substituição do logo Comsteel Tiny House** se houver logo no slide (ver seção A — versão branca sobre fundo tabaco).

---

### SLIDE 18 — SEU TERRITÓRIO · SERRA CATARINENSE

**Problema atual:**
- O logo Comsteel posicionado na parte inferior do slide está **sobrepondo conteúdo** (rodapé ou bloco textual).

**Ajuste a fazer:**

1. **Reposicione o logo Comsteel** que está na parte inferior do slide para que **não sobreponha nenhum elemento** (rodapé em cinza, blocos de texto, números #1/#2/#3, mapa estilizado).
2. Se necessário, **reduza ligeiramente o logo** ou **mova-o para o canto inferior-direito** com margem confortável (mínimo 40px da borda).
3. **Use o logo da nova pasta** (versão branca, fundo preto — ver seção A).
4. Mantenha o resto do slide intacto.

---

## C. CHECKLIST DE VERIFICAÇÃO FINAL

Antes de devolver o arquivo, confirme:

- [ ] **Logos:** TODOS os logos do deck foram substituídos pelos PNGs das duas pastas novas em assets, com versão correta para cada fundo e tamanhos mínimos respeitados.
- [ ] **Slide 1:** texto reposicionado para canto inferior-esquerdo, reduzido, sem sobreposição com o mapa. Tagline em branco sólido, maior, em peso medium — não passa batido.
- [ ] **Slide 2:** "GUSTAVO & GUILHERME." subiu o suficiente para não encostar no telhado da Office. "SERRA CATARINENSE · 2026" foi pro canto superior-direito. "COMSTEEL · 2026" foi removido. Lockup de logos no rodapé com logos novos em tamanho adequado.
- [ ] **Slide 7:** fotografia substituída pelo Anexo #3.
- [ ] **Slide 8:** fotografia substituída pelo Anexo #4.
- [ ] **Slide 14:** mockup do feed substituído pelo Anexo #5.
- [ ] **Slide 17:** background do lado esquerdo substituído pelo Anexo #6, sem PNG da Tiny sobreposto.
- [ ] **Slide 18:** logo Comsteel no rodapé não sobrepõe mais nenhum elemento.
- [ ] Todos os demais slides do deck (3, 4, 5, 6, 9, 10, 11, 12, 13, 15, 16, 19, 20, 21) **permanecem idênticos** ao que estava antes, exceto pelos logos substituídos.

=== FIM DO PROMPT ===
