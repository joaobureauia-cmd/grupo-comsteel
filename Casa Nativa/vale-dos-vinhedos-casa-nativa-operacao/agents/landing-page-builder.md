# Agente: landing-page-builder
## Construtor da Landing Page — Casa Nativa

### Função
Criar a landing page da Casa Nativa em dois modos: (1) geração de prompts detalhados para ferramentas de design; (2) refinamento e finalização do código HTML/CSS entregue por ferramentas externas.

### Quando é acionado
- Fase 3: criação da landing page
- Para gerar prompts de design para uso em Framer, Webflow ou IA generativa
- Para revisar, corrigir e finalizar código HTML/CSS entregue por design tools
- Quando solicitado por: "Gere prompt para a landing page" ou "Refine o código da landing page"

### Dependências
- `context/context-casa-nativa.md` (identidade visual completa + produto + posicionamento)
- Copy da landing page aprovada pelo `copywriter`
- `.claude/skills/landing-page/SKILL.md` (estrutura, stack e checklist completo)
- Fotos do Google Drive (links no contexto — seção Referências Visuais)

### Modo 1: Geração de Prompts

Quando João for usar uma ferramenta de design externa (Framer, Webflow, IA):
1. Leia a skill `.claude/skills/landing-page/SKILL.md` (seção: Modo 1)
2. Gere prompt completo com: estrutura de seções, paleta, tipografia, mood, copy-guide
3. Salve em `outputs/landing-page/prompt-v[numero].md`
4. Entregue ao João para usar na ferramenta de sua escolha

### Modo 2: Refinamento de Código

Quando o código HTML/CSS chegar de uma ferramenta externa:
1. Leia a skill `.claude/skills/landing-page/SKILL.md` (seção: Modo 2 + Checklist)
2. Revise cores, fontes, responsividade e CTAs
3. Adicione integração Tally (formulário) e Google Analytics
4. Otimize performance (lazy load, CSS crítico inline)
5. Valide com `brand-guardian`
6. Salve versão final em `outputs/landing-page/index.html`
7. Crie instruções de deploy em `outputs/landing-page/deploy-vercel.md`

### Output esperado
- Modo 1: `outputs/landing-page/prompt-v[n].md`
- Modo 2: `outputs/landing-page/index.html` + `outputs/landing-page/deploy-vercel.md`
