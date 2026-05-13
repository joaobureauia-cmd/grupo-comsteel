# Prompt de Ajustes para Claude Design — Brand Center Serra Catarinense v2.2

> **Como usar:**
> 1. Mantenha o deck atual aberto.
> 2. Anexe **3 novas imagens** no chat, **nesta ordem exata**:
>    - **Anexo #1** — Render da **Tiny Office London** (substitui a Office Venus do Slide 2).
>    - **Anexo #2** — Fotografia da fachada da fábrica Comsteel (para o Slide 7).
>    - **Anexo #3** — Render da Tiny Office London em natureza/golden hour (para o Slide 17).
> 3. Copie tudo entre `=== INÍCIO DO PROMPT ===` e `=== FIM DO PROMPT ===` e cole no Claude Design.
>
> **Observação:** este é um prompt de ajustes pontuais. NÃO regenere o deck inteiro. Aplique apenas as alterações listadas.

---

=== INÍCIO DO PROMPT ===

Aplique os ajustes abaixo no deck "Brand Center · Licenciados Gustavo & Guilherme · Serra Catarinense". **Não regenere o deck inteiro.** Aplique apenas as correções listadas. Tudo o que não for explicitamente alterado, mantenha exatamente como está.

---

## A. CORREÇÃO GLOBAL E CRÍTICA — LOGOS (faça antes de tudo)

Esta correção se aplica a **TODOS os slides do deck**.

**Contexto:** os logos atualmente renderizados no deck estão errados e em tamanho minúsculo. **Acabo de RESETAR a pasta de assets do projeto e substituí todos os arquivos de logo pelos corretos**, em duas pastas:

- **`Logos Comsteel Construção e Mobilidade`** — versões oficiais (branco, preto, laranja).
- **`Logos Comsteel Tiny House`** — versões oficiais (branco, tabaco, preto).

**Ação obrigatória — forçar releitura completa:**

1. **Releia os arquivos das duas pastas de assets do zero**, ignorando qualquer cache. Os arquivos foram substituídos.
2. **Substitua TODA instância de logo do deck** (em TODOS os slides onde aparece) pelos arquivos atuais dessas duas pastas.
3. **Use a versão correta de cada logo** conforme o fundo do slide:
   - Fundo preto → versão **branca**
   - Fundo branco → versão **preta**
   - Fundo tabaco → versão **branca**
   - Fundo bege → versão **preta**

**Tamanhos mínimos de exibição** (largura do logo em relação à largura do slide):

| Contexto | Largura mínima |
|---|---|
| Logo em rodapé/canto discreto | **8% da largura do slide** (~150px em 16:9 1920×1080) |
| Logo em lockup duplo (Construção + Tiny juntos) | **12% para cada logo** |
| Logo em slide de identidade (Slides 7 e 8) | **20% da largura do slide** — claramente visível e legível |
| Logo na capa (Slide 2) e encerramento (Slide 21) | **14% para cada logo do lockup** |

**Slides afetados (todos):** Slide 2, 6, 7, 8, 17, 18, 21, e qualquer outro slide que tenha logo.

> O Slide 1 NÃO precisa de logo adicional — o logo Comsteel Construção & Mobilidade já está embutido no rodapé central da imagem do mapa.

---

## B. CORREÇÃO GLOBAL — TINY OFFICE VENUS → TINY OFFICE LONDON

**Contexto:** o ativo entregue aos licenciados é a **Tiny Office LONDON**, não a Office Venus. Foi um erro do prompt original. Substitua **TODAS as ocorrências** de "Office Venus" / "Venus" / "Tiny Office Venus" no deck por **"Office London"** / **"Tiny Office London"**.

**Especificações técnicas a atualizar (substitua os números antigos pelos novos):**

| | Office Venus (antigo) | Office London (novo) |
|---|---|---|
| Área | 29 m² | **23 m²** |
| Dimensões | 9 × 3,20 m × 3 m altura | **7 × 3,20 m × 3 m altura** |
| Posicionamento | Espaço para equipes pequenas | **Home office profissional, sala de reunião** |

**Slides afetados:**
- **Slide 2** — referências a "Office Venus" no copy
- **Slide 5** — bloco "1 ativo" diz "Tiny Office Venus (29 m²)" → trocar para "Tiny Office London (23 m²)"
- **Slide 17** — slide inteiro do ativo Tiny: substituir nome e specs (ver detalhe na seção C)
- **Slide 20** — timeline 90 dias: "Produção e logística da Tiny Office Venus" e "Instalação da Office Venus" → trocar para London em ambos os marcos

Faça **find-and-replace global** de "Venus" por "London" e atualize os números 29 m² → 23 m² e 9 × 3,20 m → 7 × 3,20 m.

---

## C. AJUSTES POR SLIDE

### SLIDE 1 — CAPA DE BOAS-VINDAS (mapa Serra Catarinense)

**Problema atual:** o bloco de texto (SEJAM BEM-VINDOS, GUSTAVO & GUILHERME, tagline) está posicionado um pouco baixo demais — está **encostando no logo Comsteel embutido no rodapé do mapa**.

**Ajuste a fazer:**

1. **Suba o bloco de texto inteiro** em ~40–60px (cerca de 4–5% da altura do slide). Mantenha o alinhamento à esquerda.
2. Garanta que **a tagline "Agora vocês fazem parte da família Comsteel." tenha pelo menos 60px de respiro entre a base da última linha e o topo do logo Comsteel embutido no mapa**.
3. **Não altere o tamanho da tipografia, nem as cores, nem a hierarquia** — apenas reposicionamento vertical.

---

### SLIDE 2 — CAPA OFICIAL (Office)

**Problema atual:** o slide ainda mostra a Tiny **Office Venus**. O ativo correto é a Tiny **Office London**.

**Ajuste a fazer:**

1. **Substitua a imagem PNG da Office Venus** pela imagem **Anexo #1** (render da Tiny Office London).
2. **Atualize qualquer referência textual no slide** de "Venus" para "London" (se houver).
3. **Mantenha o layout, a tipografia, o posicionamento dos textos e os elementos auxiliares** (BRAND CENTER · LICENCIADOS PREMIUM no topo-esquerdo, SERRA CATARINENSE · 2026 no topo-direito, GUSTAVO & GUILHERME centralizado, lockup de logos no rodapé esquerdo, DUAS MARCAS · UM PACOTE no rodapé direito) **exatamente como estão**.
4. Aplique a substituição de logos da seção A.

---

### SLIDE 7 — IDENTIDADE VISUAL · CONSTRUÇÃO & MOBILIDADE

**Ajuste a fazer:**

1. **Substitua a fotografia atual** pela imagem **Anexo #2** (fotografia real da fachada da fábrica Comsteel com letreiro 3D metálico em laranja e cinza).
2. **Mantenha todo o resto do slide intacto:** headline, paleta de cores, descrição de tipografia, descrição de layout.
3. Aplique a substituição de logos da seção A — o logo do slide deve ter **mínimo 20% da largura do slide**, claramente visível.

---

### SLIDE 17 — SEU ATIVO · TINY OFFICE LONDON

> Este slide era originalmente "SEU ATIVO · TINY OFFICE VENUS" — agora vira "SEU ATIVO · TINY OFFICE LONDON".

**Ajuste a fazer:**

1. **Substitua a imagem de fundo do lado esquerdo** pela imagem **Anexo #3** (render da Tiny Office London em ambiente natural, golden hour, com grama, pedras e árvores ao redor).
2. **Remova qualquer PNG/recorte da Tiny** que esteja sobreposto ao fundo — o Anexo #3 já é a composição completa, não sobreponha outro render.
3. **Atualize o nome e specs** no bloco de texto à direita:
   - "Office Venus · 29 m²" → **"Office London · 23 m²"**
   - "9 × 3,20 m × 3 m de altura" → **"7 × 3,20 m × 3 m de altura"**
   - "Espaço para equipes pequenas, sala de reunião, área de demonstração" → **"Home office profissional, sala de reunião, área de demonstração"**
4. **Atualize "Três funções simultâneas":**
   - Escritório oficial dos licenciados na Serra Catarinense (mantém)
   - Showroom para o cliente final tocar o produto antes de comprar (mantém)
   - *Ponto físico da marca* — coloca a Comsteel na rua do seu território (mantém)
5. **Mantenha** a identidade Tiny House (fundo tabaco, texto branco, acento cobre, Madefor Display Bold) e a citação *"É usufruir, não construir."*
6. Aplique a substituição de logos da seção A — versão Tiny House branca sobre fundo tabaco.

---

## D. CHECKLIST DE VERIFICAÇÃO FINAL

Antes de devolver o arquivo, confirme:

- [ ] **Logos:** TODOS os logos do deck foram relidos das duas pastas de assets resetadas e estão nos tamanhos mínimos especificados na seção A.
- [ ] **"Venus" não aparece em lugar nenhum do deck.** Toda referência ao ativo do licenciado é "Office London" / "Tiny Office London".
- [ ] **Specs corretas em todos os slides que mencionam o módulo:** 23 m² · 7 × 3,20 m · 3 m de altura.
- [ ] **Slide 1:** texto subiu o suficiente para não encostar no logo Comsteel embutido no mapa (mínimo 60px de respiro).
- [ ] **Slide 2:** PNG da Venus foi trocado pela imagem do Anexo #1 (London). Layout e tipografia inalterados.
- [ ] **Slide 5:** "1 ativo" agora diz "Tiny Office London (23 m²)".
- [ ] **Slide 7:** fotografia substituída pelo Anexo #2 (fachada da fábrica Comsteel).
- [ ] **Slide 17:** background do lado esquerdo substituído pelo Anexo #3, sem PNG da Tiny sobreposto. Título do slide vira "SEU ATIVO · TINY OFFICE LONDON". Specs atualizadas no bloco de texto à direita.
- [ ] **Slide 20:** timeline menciona "Tiny Office London" nas semanas 5-8 e 9-13.
- [ ] Todos os demais slides do deck (3, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 21) **permanecem idênticos** ao que estava antes, exceto pelos logos substituídos.

=== FIM DO PROMPT ===
