# Skill: landing-page-prompt-engineer
## Criação da Landing Page — Casa Nativa

### Quando usar esta skill
Use quando `landing-page-builder` for acionado para gerar prompts de design ou refinar código da landing page.

---

### Stack Técnica Adotada
- **Hospedagem:** Vercel (gratuito, deploy via Git)
- **Código:** HTML + CSS + JavaScript (arquivo único ou estrutura simples)
- **Formulário de contato:** Tally.so (gratuito, sem backend)
- **Domínio:** Configurar domínio próprio no Vercel (ex: casanativa.com.br)
- **Analytics:** Google Analytics 4 (gratuito)

---

### Estrutura da Landing Page — Casa Nativa

#### Seções obrigatórias (em ordem):

```
1. HERO
   - Logo Casa Nativa
   - Foto de destaque (módulo principal ou deck com natureza)
   - Headline: "Um refúgio para desacelerar"
   - Subheadline: curta descrição sensorial (2 linhas)
   - CTA primário: "Reserve sua estadia" (link Airbnb ou formulário)

2. EXPERIÊNCIA
   - Título: "Mais do que hospedagem — uma vivência"
   - Descrição sensorial do produto (copy do copywriter)
   - Galeria de fotos (3-4 imagens)

3. ESPAÇOS
   - Tiny Hospedagem: foto + descrição dos ambientes
   - Tiny Sauna: foto + descrição do diferencial
   - (NÃO mencionar Tiny Adega como comodidade)

4. DIFERENCIAIS
   - Ícones + texto para: Sauna Privativa | Design Premiado | Vale dos Vinhedos | Intimidade para 2
   - Prêmio Anuário de Arquitetura (badge/selo)

5. LOCALIZAÇÃO
   - "No coração do Vale dos Vinhedos"
   - Mapa ou texto sobre proximidade às vinícolas
   - Texto sobre enoturismo como experiência da região

6. GALERIA
   - Grid de fotos profissionais (usar links do Google Drive)

7. RESERVAS
   - Preço por noite [a definir]
   - Capacidade: 2 hóspedes
   - Política básica
   - CTA: "Reservar no Airbnb" + formulário de contato direto (Tally)

8. SOBRE
   - História resumida da Casa Nativa (Mostra Glass + premiação)
   - Logos: Casa Nativa | by Comsteel Tiny House | Alinea Hospedagem

9. FOOTER
   - Links: Instagram | Airbnb | WhatsApp [a definir]
   - Tagline: "Um refúgio para desacelerar"
```

---

### Modo 1: Geração de Prompts para Ferramentas de Design

Use este template ao gerar prompts para Framer, Webflow, Figma ou IA generativa de UI:

```
PROMPT BASE PARA GERAÇÃO DE LANDING PAGE:

Crie uma landing page premium para uma hospedagem chamada "Casa Nativa",
localizada em Bento Gonçalves, RS, Brasil (Vale dos Vinhedos).

Estilo visual:
- Paleta: fundo creme (#f5ede0), texto terra escuro (#80421c),
  destaque terra média (#945128), branco sujo (#faf8f4)
- Tipografia: títulos em Perandory (serif elegante), corpo em Inter,
  taglines em Playfair Display Italic
- Mood: refúgio de natureza, minimalismo orgânico, premium sem ser frio,
  acolhedor e contemporâneo

Elementos visuais:
- Foto hero: luz quente e dourada, natureza integrada à arquitetura
- Ripados/brises como textura decorativa
- Vegetação nativa em imagens e elementos gráficos
- Ícones minimalistas em linha, cor terra escura

Estrutura de seções: [listar as seções acima]

Tom do conteúdo: sensorial, contemplativo, poético mas direto.
Nunca genérico. Tagline: "Um refúgio para desacelerar"

CTA principal: "Reserve sua estadia" — cor terra escura (#80421c)
```

---

### Modo 2: Refinamento de Código

Quando o designer entrega o HTML/CSS gerado por ferramenta, o `landing-page-builder` deve:

1. **Revisar** o código gerado para consistência com a identidade visual
2. **Corrigir** cores, fontes e espaçamentos que desviaram do padrão
3. **Otimizar** para performance (imagens lazy load, CSS inline crítico)
4. **Adicionar** integração com Tally (formulário) e Google Analytics
5. **Preparar** para deploy no Vercel (garantir que funciona como arquivo estático)

**Checklist de revisão de código:**
- [ ] Cores corretas (hexadecimais conforme paleta)
- [ ] Fontes carregando do Google Fonts (Perandory, Inter, Playfair Display)
- [ ] Hero com foto de alta qualidade e overlay correto
- [ ] CTA com cor #80421c e hover em #945128
- [ ] Formulário Tally integrado
- [ ] Meta tags SEO: title, description, og:image
- [ ] Mobile responsivo (testar em 375px, 768px, 1440px)
- [ ] Logo Casa Nativa no header e footer
- [ ] Hierarquia de marcas correta (Comsteel e Alinea no footer)

---

### Salvamento
- Prompts: `outputs/landing-page/prompt-[versao].md`
- Código: `outputs/landing-page/index.html` (+ assets/)
- Deploy: instruções em `outputs/landing-page/deploy-vercel.md`
