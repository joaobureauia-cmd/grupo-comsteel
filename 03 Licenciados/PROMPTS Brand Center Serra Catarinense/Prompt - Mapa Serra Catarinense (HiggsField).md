# Prompt para HiggsField — Mapa Serra Catarinense (Card do Slide 0)

> **Como usar:**
> 1. No HiggsField, anexe **duas imagens** como referência:
>    - **Imagem A** — o mapa-referência de Santa Catarina dividido em 6 mesorregiões (fundo branco, regiões coloridas com seus nomes).
>    - **Imagem B** — o logo Comsteel Construção & Mobilidade na versão **preta sobre fundo branco** (PNG com fundo transparente, idealmente).
> 2. Copie tudo entre `=== INÍCIO DO PROMPT ===` e `=== FIM DO PROMPT ===`, cole no HiggsField.
> 3. Output esperado: **uma imagem 16:9, fundo branco sólido, mapa isométrico 2.5D de Santa Catarina, região Serrana destacada em laranja Comsteel, demais regiões em cinza claro, logo Comsteel discreto no canto inferior direito.**

---

=== INÍCIO DO PROMPT ===

Premium isometric 2.5D illustration of the Brazilian state of Santa Catarina, viewed from a slight 25-degree elevated angle (low-angle isometric, like a high-end corporate infographic).

The state is divided into its six official mesoregions, matching the geometry of the attached reference map (Image A). The regions are: Oeste Catarinense (west), Norte Catarinense (north), Vale do Itajaí (east-center), Grande Florianópolis (east coast, center), Sul Catarinense (south), and Serrana (central-south).

REGION TREATMENT (this is critical, follow exactly):

- The **Serrana** region is the visual hero of the composition. Fill it with a solid vibrant copper-orange, hex `#D86B28`. Lift it visually above the rest of the map with a subtle 3D extrusion of about 15–20 pixels of height — like a raised plateau or a pedestal — and cast a soft realistic drop shadow on the adjacent regions to reinforce the elevation. The orange color is uniform (no gradient, no texture).
- The **other five regions** (Oeste Catarinense, Norte Catarinense, Vale do Itajaí, Grande Florianópolis, Sul Catarinense) are completely flat, in a uniform neutral light gray `#E0E0E0`, with thin clean borders in slightly darker gray `#B5B5B5` (1–1.5 px stroke width).
- All region borders are smooth and clean, no jagged edges, no artistic distortion. Preserve the relative proportions and shapes of the regions accurately from the attached reference map.

TEXT INSIDE THE MAP:

Inside the **Serrana** region (the orange one), centered on its visual mass, render the text **"Serra Catarinense"** in two lines:
- Line 1: `Serra`
- Line 2: `Catarinense`
Use a modern geometric sans-serif typeface (similar to Inter Bold, Manrope Bold, or Neue Haas Grotesk Bold), in pure white `#FFFFFF`, all letters in Title Case (initial capital, rest lowercase — exactly "Serra Catarinense"). Slight negative letter-spacing. The text should sit comfortably inside the region with adequate padding, never touching the borders.

**No other text appears anywhere on the map.** No labels on the other regions. No legend. No compass rose. No scale bar. No website URL. No grid coordinates.

BACKGROUND:

Solid pure white `#FFFFFF`. No gradient. No texture. No noise. No drop shadows behind the map itself (only the internal shadow of the Serrana extrusion).

LOGO PLACEMENT:

In the **bottom-right corner** of the composition, place the **attached Comsteel logo (Image B)** in its original black version. The logo should be small and discrete — occupying no more than **8% of the total image width** — with comfortable clear space around it (at least the height of the logo as margin from the canvas edges). The logo must remain perfectly legible, not distorted, not rotated, not recolored. Treat it as a discrete brand mark, not as a decorative element.

COMPOSITION:

- The map of Santa Catarina is centered horizontally and vertically in the canvas.
- The map occupies approximately **80% of the canvas width**, with comfortable white margins on all sides.
- Aspect ratio: **16:9 (landscape)**.
- Resolution: high (suitable for a corporate slide deck, at least 1920×1080 px).

STYLE:

Ultra-clean modern infographic. Premium design-system aesthetic. Sharp vector-like edges. No photorealistic terrain. No clouds, no water gradients, no mountains, no decorative natural elements. Looks like a high-end branded asset from a Fortune-500 corporate report or a premium architecture firm presentation.

REFERENCE USAGE:

- **Image A** (attached SC map): use strictly as **geometric reference** for the shape and division of the six mesoregions. Do NOT copy its colors, its labels, or its decorative elements (no URL, no IBGE attribution, no compass, no scale bar) — only the geometry of the borders.
- **Image B** (attached Comsteel logo): use as the **exact logo asset** to place in the bottom-right corner. Do not redesign or recreate the logo.

NEGATIVE PROMPT:

no labels on other regions, no IBGE attribution, no compass rose, no scale bar, no coordinates, no website URL, no decorative borders or frames around the canvas, no photorealistic terrain or topography, no mountains rendered in 3D, no clouds, no shadows on the white background, no gradients inside regions, no textures inside regions, no second logo, no watermarks other than the attached Comsteel logo, no flags, no people, no buildings.

=== FIM DO PROMPT ===
