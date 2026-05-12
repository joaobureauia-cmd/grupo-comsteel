"""
==========================================================================
TEMPLATE DE PROPOSTA · COMSTEEL TINY HOUSE
==========================================================================

Engine único para gerar propostas em PDF (A4 vertical, 10 páginas) com a
identidade visual oficial da Comsteel Tiny House.

COMO USAR:
1. Edite o dicionário CONFIG abaixo com os dados da nova proposta.
2. Coloque as fotos referenciadas em ./assets/ (mesma pasta que este script).
3. Rode:  python3 build_proposta.py
4. O PDF é gerado no caminho indicado em CONFIG["output"].

Tudo o que muda entre propostas está no CONFIG. O resto é estilo.
==========================================================================
"""

# ==========================================================================
#                              CONFIG  ←  EDITE AQUI
# ==========================================================================

CONFIG = {
    # ---------- IDENTIFICAÇÃO ----------
    "cliente":          "Rodrigo",
    "modelo_titulo":    "Natura",                     # usado em "Tiny House Natura"
    "modelo_capa":      "NATURA",                     # versão maiúscula da capa
    "area":             "29 m²",
    "dimensoes":        "3,20 × 9,00 m",
    "cidade_uf":        "Novo Hamburgo · RS",
    "subtitulo_capa":   "29 m²  ·  Light Steel Frame  ·  Pronta para usufruir",

    # ---------- INVESTIMENTO (Página 9) ----------
    "preco":                 "R$ 229.900,00",
    "preco_descricao":       "29 m² · turn-key · entrega em até 7 dias após assinatura e terreno preparado",
    "prazo_entrega_curto":   "Até 7 dias",
    "prazo_entrega_longo":   "Até 7 dias após a assinatura do contrato",
    "prazo_entrega_obs":     "(considerando a preparação prévia do terreno).",
    "parcelas": [
        ("5%",  "Na assinatura do compromisso de compra e venda"),
        ("40%", "Na confirmação do pedido e início da produção"),
        ("55%", "Após o faturamento do pedido"),
    ],

    # ---------- PÁGINA 3 — HERO ----------
    "hero_titulo":    "Um refúgio que se adapta à vida.",
    "hero_subtitulo": (
        "Da fábrica em Novo Hamburgo ao seu terreno: a Tiny Natura chega "
        "<i>pronta para usufruir</i>, com o requinte do design autoral e a "
        "engenharia da construção industrializada."
    ),

    # ---------- PÁGINA 4 — A PROPOSTA / SISTEMA CONSTRUTIVO ----------
    "p4_imagem_legenda": "Tiny House Natura · 3,20 × 9,00 m  ·  Fabricação em Novo Hamburgo / RS",
    "sistema_construtivo": [
        "Projeto estrutural do LSF (Light Steel Frame);",
        "Industrialização do Steel Frame (perfis em aço engenheirado);",
        "Projeto de modulação estrutural;",
        "Fabricação dos painelizados e modulação;",
        "Responsabilidade técnica de projeto e execução estrutural;",
        "Instalação da estrutura on-site;",
        "Montagem e instalação de funilarias.",
    ],
    "materiais": (
        "Aço Galvanizado ZAR 275, Plywood, parafusos, isolante térmico em lã de PET, "
        "membrana hidrófuga, impermeabilização para bases das paredes e telhas com isolamento térmico."
    ),

    # ---------- PÁGINA 5 — REVESTIMENTOS ----------
    "p5_label_imagem":   "INTERIOR · PAINÉIS RIPADOS",
    "p5_band_quote":     "Cada espaço é mais do que uma moradia — é um refúgio.",
    "p5_band_label":     "DESIGN · LIFESTYLE · USUFRUIR",
    "revestimentos_externos": [
        "Ripado PVC Branco",
        "Placas cimentícia design pedra rústica cor concreto",
        "Esquadrias em alumínio branco com tela",
        "Perfil de LED na fachada",
        "Arandelas de LED frente e fundos",
        "Telha termo-isolante TP40",
    ],
    "revestimentos_internos": [
        "Parede e teto em MDF",
        "Instalação elétrica com luminárias dicróicas embutidas",
        "Instalação hidro-sanitária (com vaso)",
        "Sistema hidráulico com aquecimento a gás",
        "Cabeamento de rede e infraestrutura para automação",
        "Piso laminado resistente à água",
        "Banheiro revestido em porcelanato (piso e parede)",
        "Espera para ar condicionado split",
    ],

    # ---------- PÁGINA 6 — MOBILIÁRIO ----------
    "p6_big_label":          "ESTAR · INTEGRADO À COZINHA · QUIET LUXURY",
    "p6_band_titulo":        "DESIGN AUTORAL",
    "p6_band_l1":            "Marcenaria, mobiliário e iluminação executados sob medida —",
    "p6_band_l2":             "para que sua Tiny chegue pronta para o primeiro café.",
    "mobiliario_cozinha": [
        "Pedra Quartzo Branca",
        "Cuba Gourmet com torneira",
        "Armário 2 portas e aéreo",
    ],
    "mobiliario_quarto": [
        "Cama Queen sob medida",
        "Cabeceira revestida em Courino",
        "Painéis ripados nas paredes",
    ],
    "mobiliario_banheiro": [
        "Lavabo com cuba sobreposta de aço corten",
        "Pedra Quartzo Branca",
        "Espelho de LED touch",
        "Vaso sanitário",
        "Box em vidro temperado",
        "Metais — chuveiro, registros, torneiras",
    ],

    # ---------- PÁGINA 7 — GALERIA ----------
    "galeria_titulo":     "Tiny Natura · em detalhe.",
    "galeria_subtitulo":  "Fotos reais da unidade Natura — fábrica e mostra Construir·Aí.",

    # ---------- PÁGINA 8 — INFORMAÇÕES COMPLEMENTARES ----------
    "arquiteto":          "Luiz Maldaner",
    "modulo_descricao":   "Módulo Tiny House Natura",
    "gerenciamento_texto": (
        "A instalação é acompanhada pelo arquiteto responsável pelo projeto, engenheiros e gestores. "
        "Ao final, o cliente recebe um arquivo com um <i>menu</i> de imagens da instalação e dos projetos executados."
    ),
    "observacoes_gerais": [
        "Não estão inclusos paisagismo, piscina, portões, aquecedor de passagem, grades, automação, sistemas de alarme, TV, câmeras de vigilância e rede de internet.",
        "Não estão inclusas quaisquer construções em alvenaria fora deste escopo (muro de contenção, rampas de garagem, calçadas e demais áreas não computáveis).",
        "Não está inclusa a averbação do imóvel no registro de imóveis do município, custos com Habite-se, INSS, taxas e projetos.",
        "Qualquer alteração de projeto que interfira na área construtiva mensurada será considerada aditivo desta proposta inicial, assim como alterações de itens de acabamento superiores ao orçamento descrito em contrato.",
    ],
    "fora_escopo": [
        "Ensaio de SPT do terreno para fundação.",
        "Infraestrutura — sapata, fundações, terraplanagem e serviços em alvenaria.",
        "Munck para logística de movimentação de carga.",
        "Laje específica para suporte de caixas d'água, boiler e demais.",
        "Hospedagens, alimentação e alojamento da equipe (quando aplicável).",
        "Fossa séptica, sumidouro e instalações.",
    ],
    "p8_footnote": (
        "A proposta pode sofrer alterações após o projeto estrutural finalizado, "
        "caso seja necessária revisão de área e dimensionamento de cargas."
    ),

    # ---------- PÁGINA 9 — OBSERVAÇÃO INVESTIMENTO ----------
    "p9_obs_l1": "Obras com distância superior a 200 km da sede da CONTRATADA terão valor adicional, conforme",
    "p9_obs_l2": "disposições de hospedagem, temporada e condições regionais.",

    # ---------- PÁGINA 10 — CLÁUSULAS ----------
    "clausula_a": (
        "<b>A.</b> Os vencimentos dos valores desta proposta serão programados com datas de acordo com o cronograma "
        "físico-financeiro da realização das etapas da obra contratada. Os vencimentos somente sofrerão alterações no caso de "
        "ocorrências provenientes e atribuídas à parte da <b>CONTRATADA</b>, que venham a ser impeditivas à conclusão do cronograma. "
        "Não ocorrerão prorrogações nos vencimentos por motivos diversos provenientes da <b>CONTRATANTE</b>, incidindo acréscimos de mora "
        "previstos em contrato. Todas as condições especiais devem ser previamente negociadas, acordadas e formalizadas por escrito."
    ),
    "clausula_b": (
        "<b>B.</b> O atraso na entrega dos documentos definitivos impacta no <i>lead time</i> do cronograma da obra. "
        "Por isso, os períodos de pagamento vinculados às etapas não serão prorrogados e devem seguir os vencimentos previstos em contrato. "
        "Qualquer alteração de projeto realizada posteriormente — durante a execução — implica revisão de valores, "
        "previamente analisada, aprovada pelas <b>CONTRATANTES</b> e formalizada em aditivo contratual."
    ),
    "clausula_cd": (
        "<b>C.</b> Havendo necessidade de aquisição de recursos financeiros para quitação total ou parcial do valor desta "
        "proposta, fica a critério do <b>CONTRATANTE</b> realizar consultas de empréstimo em instituições de sua conveniência, "
        "ou mediante financiamento e parcelamento direto com a <b>CONTRATADA</b>. Os termos e condições serão expressos em aditivo contratual. "
        "<b>D.</b> Serão negociadas e acordadas garantias para eventuais parcelamentos diretos com a <b>CONTRATADA</b>, integrando o aditivo acima referido."
    ),
    "assinante_nome":   "Ramão Reichert Jr",
    "assinante_cargo":  "Diretor Comercial & Marketing",

    # ---------- CONTATO (rodapé página 10) ----------
    "telefone":         "+55 51 99724-2179",
    "email":            "comercial@comsteel.com.br",
    "site_instagram":   "www.comsteel.com.br  ·  @comsteel",
    "endereco_l1":      "Rua Dr. Karl Wilhelm Schinke, 69, pavilhão 09",
    "endereco_l2":      "Bairro Rondônia · Novo Hamburgo · RS",

    # ---------- IMAGENS (todas em ./assets/) ----------
    "imagens": {
        "capa":               "feira_exterior.jpg",      # foto exterior, full-bleed
        "hero_p3":             "bedroom_corredor.jpg",    # foto interior cinematográfica
        "p4":                 "exterior_front.jpg",      # foto da casa montada
        "p5_detalhe":         "wood_partition.jpg",      # detalhe interno
        "p6_thumb_cozinha":   "kitchen_cabinet.jpg",
        "p6_thumb_quarto":    "bedroom_long.jpg",
        "p6_thumb_banheiro":  "render_bathroom.jpg",
        "p6_big":             "feira_living.jpg",        # imagem grande do estar
        "p7_grid": [                                     # 6 fotos para a galeria
            "feira_exterior.jpg",
            "kitchen_full.jpg",
            "exterior_side.jpg",
            "wood_partition.jpg",
            "render_geral.jpg",
            "render_quarto.jpg",
        ],
        # Logos (não mude a não ser que existam novas versões oficiais)
        "logo_white":         "logo_white.png",
        "logo_dark":          "logo_dark.png",
    },

    # ---------- SAÍDA ----------
    "output": "Proposta_Tiny_House_Natura_Rodrigo.pdf",
    "assets_dir": "./assets",
}

# ==========================================================================
#                       ENGINE — não precisa editar
# ==========================================================================

import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY

# ---------- Canvas shim: setCharSpace + spaced drawString variants ----------
from reportlab.pdfgen.canvas import Canvas as _Canvas
_orig_drawString         = _Canvas.drawString
_orig_drawCentredString  = _Canvas.drawCentredString
_orig_drawRightString    = _Canvas.drawRightString

def _setCharSpace(self, value):
    self._cs_val = float(value)

def _spaced_width(self, text, cs):
    return self.stringWidth(text, self._fontname, self._fontsize) + cs * max(len(text) - 1, 0)

def _reset_tc(self):
    t = self.beginText(0, 0); t.setCharSpace(0); self.drawText(t)

def _drawString(self, x, y, text, *a, **kw):
    cs = getattr(self, "_cs_val", 0)
    if not cs: return _orig_drawString(self, x, y, text, *a, **kw)
    t = self.beginText(x, y); t.setFont(self._fontname, self._fontsize); t.setCharSpace(cs); t.textOut(text); self.drawText(t); _reset_tc(self)

def _drawCentredString(self, x, y, text, *a, **kw):
    cs = getattr(self, "_cs_val", 0)
    if not cs: return _orig_drawCentredString(self, x, y, text, *a, **kw)
    w = _spaced_width(self, text, cs)
    t = self.beginText(x - w/2.0, y); t.setFont(self._fontname, self._fontsize); t.setCharSpace(cs); t.textOut(text); self.drawText(t); _reset_tc(self)

def _drawRightString(self, x, y, text, *a, **kw):
    cs = getattr(self, "_cs_val", 0)
    if not cs: return _orig_drawRightString(self, x, y, text, *a, **kw)
    w = _spaced_width(self, text, cs)
    t = self.beginText(x - w, y); t.setFont(self._fontname, self._fontsize); t.setCharSpace(cs); t.textOut(text); self.drawText(t); _reset_tc(self)

_Canvas.setCharSpace      = _setCharSpace
_Canvas.drawString        = _drawString
_Canvas.drawCentredString = _drawCentredString
_Canvas.drawRightString   = _drawRightString

# ---------- Constants ----------
PAGE_W, PAGE_H = A4
CFG = CONFIG
ASSETS = CFG["assets_dir"]
OUTPUT = CFG["output"]

TABACO     = HexColor("#3A240D")
CREME      = HexColor("#8B7050")
COPPER     = HexColor("#876C4D")
SAND       = HexColor("#F5EFE6")
WHITE      = HexColor("#FFFFFF")
TEXT_DARK  = HexColor("#1D1208")
TEXT_MUTED = HexColor("#5C4A38")

# ---------- Helpers ----------
def img_path(key):
    return os.path.join(ASSETS, CFG["imagens"][key])

def draw_image_full(c, path, x, y, w, h, cover=True):
    img = ImageReader(path)
    iw, ih = img.getSize()
    if cover:
        s = max(w / iw, h / ih)
        nw, nh = iw * s, ih * s
        nx = x + (w - nw) / 2
        ny = y + (h - nh) / 2
        c.saveState()
        p = c.beginPath()
        p.rect(x, y, w, h)
        c.clipPath(p, stroke=0, fill=0)
        c.drawImage(path, nx, ny, nw, nh, mask='auto')
        c.restoreState()
    else:
        s = min(w / iw, h / ih)
        nw, nh = iw * s, ih * s
        c.drawImage(path, x + (w - nw) / 2, y + (h - nh) / 2, nw, nh, mask='auto')

def draw_logo(c, path, x, y, max_w=200, max_h=80, anchor="left"):
    img = ImageReader(path)
    iw, ih = img.getSize()
    s = min(max_w / iw, max_h / ih)
    w, h = iw * s, ih * s
    if anchor == "center": x -= w / 2
    elif anchor == "right": x -= w
    c.drawImage(path, x, y - h/2, w, h, mask='auto')

def draw_text_block(c, text, x, y, w, h, style):
    p = Paragraph(text, style)
    f = Frame(x, y, w, h, leftPadding=0, bottomPadding=0, rightPadding=0, topPadding=0, showBoundary=0)
    f.addFromList([p], c)

def draw_rule(c, x, y, w, color=COPPER, thickness=0.6):
    c.setStrokeColor(color); c.setLineWidth(thickness); c.line(x, y, x + w, y)

def draw_label(c, text, x, y, color=COPPER, size=8, char_space=2):
    c.setFont("Helvetica-Bold", size); c.setFillColor(color)
    c.setCharSpace(char_space); c.drawString(x, y, text.upper()); c.setCharSpace(0)

def draw_page_number(c, n, total):
    c.setFont("Helvetica", 7); c.setFillColor(TEXT_MUTED)
    c.setCharSpace(1); c.drawRightString(PAGE_W - 36, 24, f"{n:02d} / {total:02d}"); c.setCharSpace(0)

def page_footer(c, brand_color=TEXT_MUTED):
    c.setFont("Helvetica", 6.5); c.setFillColor(brand_color)
    c.setCharSpace(1.5); c.drawString(36, 24, "COMSTEEL TINY HOUSE   ·   PROPOSTA COMERCIAL"); c.setCharSpace(0)

# ---------- Paragraph styles ----------
body_style = ParagraphStyle("body", fontName="Helvetica", fontSize=9.5, leading=14, textColor=TEXT_DARK, alignment=TA_LEFT)
body_justify = ParagraphStyle("body_just", fontName="Helvetica", fontSize=9.5, leading=14, textColor=TEXT_DARK, alignment=TA_JUSTIFY)
body_white_justify = ParagraphStyle("body_w_just", fontName="Helvetica", fontSize=10, leading=15, textColor=WHITE, alignment=TA_JUSTIFY)
quote_style = ParagraphStyle("quote", fontName="Helvetica-Oblique", fontSize=20, leading=28, textColor=WHITE, alignment=TA_LEFT)
list_style = ParagraphStyle("list", fontName="Helvetica", fontSize=9.2, leading=14, textColor=TEXT_DARK, leftIndent=10, alignment=TA_LEFT)

def bullets(items):
    return "<br/>".join([f"·&nbsp;&nbsp;{i}" for i in items])

def bullets_blank(items):
    return "<br/><br/>".join([f"·&nbsp;&nbsp;{i}" for i in items])

# ==========================================================================
#                                PÁGINAS
# ==========================================================================

def page_cover(c):
    draw_image_full(c, img_path("capa"), 0, 0, PAGE_W, PAGE_H, cover=True)
    overlay = Color(0.227, 0.141, 0.05, alpha=0.55)
    c.setFillColor(overlay); c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    c.setFillColor(TABACO); c.rect(0, 0, PAGE_W, 230, fill=1, stroke=0)

    draw_logo(c, img_path("logo_white"), PAGE_W/2, PAGE_H - 100, max_w=240, max_h=70, anchor="center")

    c.setFont("Helvetica-Bold", 8); c.setFillColor(WHITE); c.setCharSpace(4)
    c.drawCentredString(PAGE_W/2, PAGE_H - 145, "PROPOSTA COMERCIAL"); c.setCharSpace(0)

    draw_label(c, "Modelo Tiny House", 40, 175, color=COPPER, size=8, char_space=3)
    c.setFont("Helvetica-Bold", 38); c.setFillColor(WHITE); c.setCharSpace(-1)
    c.drawString(40, 130, CFG["modelo_capa"]); c.setCharSpace(0)
    c.setFont("Helvetica", 11); c.setFillColor(WHITE)
    c.drawString(40, 105, CFG["subtitulo_capa"])

    c.setFont("Helvetica-Oblique", 11); c.setFillColor(WHITE)
    c.drawString(40, 70, "É usufruir, não construir.")

    draw_rule(c, 40, 55, PAGE_W - 80, color=COPPER)
    c.setFont("Helvetica", 9); c.setFillColor(WHITE)
    c.drawString(40, 35, f"Cliente: {CFG['cliente']}")
    c.drawRightString(PAGE_W - 40, 35, CFG["cidade_uf"])
    c.showPage()


def page_manifesto(c, page_num, total):
    c.setFillColor(TABACO); c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    draw_logo(c, img_path("logo_white"), 40, PAGE_H - 80, max_w=130, max_h=42)
    c.setFont("Helvetica-Bold", 7.5); c.setFillColor(CREME); c.setCharSpace(3)
    c.drawRightString(PAGE_W - 40, PAGE_H - 60, "FILOSOFIA"); c.setCharSpace(0)

    draw_label(c, "Manifesto", 40, PAGE_H - 180, color=CREME, char_space=3)
    quote = '“Trata-se de uma transformação completa no modo de construir. Você vai <i>USUFRUIR</i>, não construir.”'
    draw_text_block(c, quote, 40, PAGE_H - 360, PAGE_W - 80, 160, quote_style)

    intro = (
        "A <b>COMSTEEL Tiny House</b> alia o conhecimento de seus fundadores à inovação das construções "
        "modulares em Steel Frame, oferecendo soluções completas — do projeto à execução. "
        "Com foco em tecnologia avançada, redução de prazos, segurança e inovação, posicionamos cada Tiny House "
        "na mais alta tecnologia da construção civil."
    )
    intro2 = (
        "Fundada com base nas inúmeras vantagens dos sistemas modulares industrializados, o método construtivo "
        "<b>Light Steel Frame</b> proporciona eficiência superior em comparação aos métodos convencionais — "
        "potencializando performance e previsibilidade orçamentária de qualquer obra. "
        "Nossa unidade de negócios de casas transportáveis nasceu deste diferencial: <i>refúgios</i> compactos, "
        "sofisticados e prontos para uso."
    )
    draw_text_block(c, intro, 40, PAGE_H - 470, PAGE_W - 80, 100, body_white_justify)
    draw_text_block(c, intro2, 40, PAGE_H - 580, PAGE_W - 80, 110, body_white_justify)

    pillars = [("90 dias","ENTREGA"),("NBR 15.575","CONFORMIDADE"),("Off-site","INDUSTRIALIZADO"),("20 anos","KNOW-HOW")]
    px, pw, py = 40, (PAGE_W - 80)/4, 110
    draw_rule(c, 40, 175, PAGE_W - 80, color=CREME)
    for i,(val,label) in enumerate(pillars):
        c.setFont("Helvetica-Bold", 14); c.setFillColor(WHITE); c.drawString(px+i*pw, py+22, val)
        c.setFont("Helvetica-Bold", 6.5); c.setFillColor(CREME); c.setCharSpace(1.6)
        c.drawString(px+i*pw, py+8, label); c.setCharSpace(0)

    c.setFont("Helvetica", 6.5); c.setFillColor(CREME); c.setCharSpace(1.5)
    c.drawString(40, 24, "COMSTEEL TINY HOUSE   ·   PROPOSTA COMERCIAL"); c.setCharSpace(0)
    c.setFont("Helvetica", 7); c.setFillColor(CREME)
    c.drawRightString(PAGE_W - 40, 24, f"{page_num:02d} / {total:02d}")
    c.showPage()


def page_projeto_hero(c, page_num, total):
    draw_image_full(c, img_path("hero_p3"), 0, 0, PAGE_W, PAGE_H, cover=True)
    c.setFillColor(TABACO); c.rect(0, 0, PAGE_W, 200, fill=1, stroke=0)
    draw_label(c, "O Projeto", 40, PAGE_H - 60, color=WHITE, char_space=3, size=8)
    draw_label(c, f"Tiny House {CFG['modelo_titulo']} · {CFG['area']}", 40, 165, color=CREME, char_space=3)
    c.setFont("Helvetica-Bold", 26); c.setFillColor(WHITE); c.setCharSpace(-0.5)
    c.drawString(40, 130, CFG["hero_titulo"]); c.setCharSpace(0)
    draw_text_block(c, CFG["hero_subtitulo"], 40, 60, PAGE_W - 80, 60, body_white_justify)

    page_footer(c, brand_color=CREME)
    c.setFont("Helvetica", 7); c.setFillColor(CREME)
    c.drawRightString(PAGE_W - 40, 24, f"{page_num:02d} / {total:02d}")
    c.showPage()


def page_proposta(c, page_num, total):
    c.setFillColor(SAND); c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    c.setFillColor(TABACO); c.rect(0, PAGE_H - 56, PAGE_W, 56, fill=1, stroke=0)
    draw_logo(c, img_path("logo_white"), 40, PAGE_H - 46, max_w=110, max_h=34)
    c.setFont("Helvetica-Bold", 7.5); c.setFillColor(CREME); c.setCharSpace(3)
    c.drawRightString(PAGE_W - 40, PAGE_H - 35, "ESPECIFICAÇÃO TÉCNICA"); c.setCharSpace(0)

    y = PAGE_H - 100
    draw_label(c, "A Proposta", 40, y, color=COPPER, size=9, char_space=3)
    y -= 35
    c.setFont("Helvetica-Bold", 28); c.setFillColor(TABACO); c.setCharSpace(-0.5)
    c.drawString(40, y, f"Tiny House {CFG['modelo_titulo']}."); c.setCharSpace(0)

    y -= 30
    intro = (
        f"Apresentamos nossa proposta para a casa modular <b>Tiny House {CFG['modelo_titulo']}</b>, "
        "utilizando o sistema modular <b>Light Steel Frame</b>. "
        "O projeto engloba as seguintes características:"
    )
    draw_text_block(c, intro, 40, y - 50, PAGE_W - 80, 50, body_justify)

    y -= 70
    draw_label(c, "Sistema Construtivo", 40, y, color=COPPER, size=8, char_space=2.5)
    draw_text_block(c, bullets(CFG["sistema_construtivo"]), 40, y - 130, (PAGE_W - 100)/2, 130, list_style)

    rx = 40 + (PAGE_W - 100)/2 + 20
    draw_label(c, "Materiais", rx, y, color=COPPER, size=8, char_space=2.5)
    draw_text_block(c, CFG["materiais"], rx, y - 130, (PAGE_W - 100)/2, 130, body_justify)

    y_img = y - 160; img_h = 200
    draw_image_full(c, img_path("p4"), 40, y_img - img_h, PAGE_W - 80, img_h, cover=True)
    c.setFillColor(TABACO); c.rect(40, y_img - img_h, PAGE_W - 80, 28, fill=1, stroke=0)
    c.setFont("Helvetica", 8); c.setFillColor(WHITE)
    c.drawString(50, y_img - img_h + 10, CFG["p4_imagem_legenda"])

    box_y, box_h = 90, 70
    c.setFillColor(TABACO); c.rect(40, box_y, PAGE_W - 80, box_h, fill=1, stroke=0)
    draw_label(c, "Prazo de Entrega", 60, box_y + box_h - 18, color=CREME, size=8, char_space=2.5)
    c.setFont("Helvetica-Bold", 16); c.setFillColor(WHITE)
    c.drawString(60, box_y + 22, CFG["prazo_entrega_longo"])
    c.setFont("Helvetica", 9); c.setFillColor(CREME)
    c.drawString(60, box_y + 8, CFG["prazo_entrega_obs"])

    page_footer(c); draw_page_number(c, page_num, total); c.showPage()


def page_revestimentos(c, page_num, total):
    c.setFillColor(SAND); c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    draw_label(c, "Acabamentos", 40, PAGE_H - 60, color=COPPER, char_space=3)
    c.setFont("Helvetica-Bold", 28); c.setFillColor(TABACO); c.setCharSpace(-0.5)
    c.drawString(40, PAGE_H - 95, "Revestimentos."); c.setCharSpace(0)

    img_h, img_w = 320, 230
    img_x, img_y = PAGE_W - img_w - 40, PAGE_H - 130 - img_h
    draw_image_full(c, img_path("p5_detalhe"), img_x, img_y, img_w, img_h, cover=True)
    c.setFillColor(TABACO); c.rect(img_x, img_y + img_h - 26, img_w, 26, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 7); c.setFillColor(CREME); c.setCharSpace(2.5)
    c.drawString(img_x + 12, img_y + img_h - 16, CFG["p5_label_imagem"]); c.setCharSpace(0)

    lx, ly = 40, PAGE_H - 145
    col_w = (PAGE_W - 80 - img_w - 30)
    draw_label(c, "Revestimentos Externos", lx, ly, color=COPPER, size=8.5, char_space=2.5)
    draw_text_block(c, bullets(CFG["revestimentos_externos"]), lx, ly - 130, col_w, 130, list_style)

    ly2 = ly - 160
    draw_label(c, "Revestimentos Internos", lx, ly2, color=COPPER, size=8.5, char_space=2.5)
    draw_text_block(c, bullets(CFG["revestimentos_internos"]), lx, ly2 - 175, PAGE_W - 80, 175, list_style)

    c.setFillColor(TABACO); c.rect(0, 90, PAGE_W, 50, fill=1, stroke=0)
    c.setFont("Helvetica-Oblique", 11); c.setFillColor(WHITE)
    c.drawString(40, 113, CFG["p5_band_quote"])
    c.setFont("Helvetica", 7.5); c.setFillColor(CREME); c.setCharSpace(2)
    c.drawString(40, 98, CFG["p5_band_label"]); c.setCharSpace(0)

    page_footer(c); draw_page_number(c, page_num, total); c.showPage()


def page_mobiliario(c, page_num, total):
    c.setFillColor(SAND); c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    draw_label(c, "Sob medida", 40, PAGE_H - 60, color=COPPER, char_space=3)
    c.setFont("Helvetica-Bold", 28); c.setFillColor(TABACO); c.setCharSpace(-0.5)
    c.drawString(40, PAGE_H - 95, "Mobiliário sob medida."); c.setCharSpace(0)

    col_w = (PAGE_W - 80 - 30) / 3
    cy, img_h = PAGE_H - 150, 130

    cols = [
        ("p6_thumb_cozinha",  "Cozinha Completa",  CFG["mobiliario_cozinha"], 75),
        ("p6_thumb_quarto",   "Quarto",             CFG["mobiliario_quarto"], 75),
        ("p6_thumb_banheiro", "Banheiro",           CFG["mobiliario_banheiro"], 100),
    ]
    for i,(img_key,label,items,h) in enumerate(cols):
        cx = 40 + i*(col_w + 15)
        draw_image_full(c, img_path(img_key), cx, cy - img_h, col_w, img_h, cover=True)
        draw_label(c, label, cx, cy - img_h - 25, color=COPPER, size=8.5, char_space=2.5)
        block_h = 100 if i == 2 else 75
        draw_text_block(c, bullets(items), cx, cy - img_h - (block_h+25), col_w, block_h, list_style)

    big_y, big_h = 170, 230
    draw_image_full(c, img_path("p6_big"), 40, big_y, PAGE_W - 80, big_h, cover=True)
    c.setFillColor(TABACO); c.rect(40, big_y, PAGE_W - 80, 28, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 7.5); c.setFillColor(CREME); c.setCharSpace(2.5)
    c.drawString(50, big_y + 10, CFG["p6_big_label"]); c.setCharSpace(0)

    c.setFillColor(TABACO); c.rect(0, 75, PAGE_W, 70, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 8); c.setFillColor(CREME); c.setCharSpace(3)
    c.drawString(40, 120, CFG["p6_band_titulo"]); c.setCharSpace(0)
    c.setFont("Helvetica", 9.5); c.setFillColor(WHITE)
    c.drawString(40, 100, CFG["p6_band_l1"])
    c.drawString(40, 87, CFG["p6_band_l2"])

    page_footer(c, brand_color=CREME)
    c.setFont("Helvetica", 7); c.setFillColor(CREME)
    c.drawRightString(PAGE_W - 40, 24, f"{page_num:02d} / {total:02d}")
    c.showPage()


def page_galeria(c, page_num, total):
    c.setFillColor(SAND); c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    draw_label(c, "Galeria", 40, PAGE_H - 60, color=COPPER, char_space=3)
    c.setFont("Helvetica-Bold", 28); c.setFillColor(TABACO); c.setCharSpace(-0.5)
    c.drawString(40, PAGE_H - 95, CFG["galeria_titulo"]); c.setCharSpace(0)
    c.setFont("Helvetica", 9.5); c.setFillColor(TEXT_MUTED)
    c.drawString(40, PAGE_H - 113, CFG["galeria_subtitulo"])

    margin, gap = 40, 12
    grid_top = PAGE_H - 140
    grid_h = grid_top - 80
    rows, cols = 3, 2
    cell_w = (PAGE_W - 2*margin - (cols-1)*gap) / cols
    cell_h = (grid_h - (rows-1)*gap) / rows
    photos = CFG["imagens"]["p7_grid"]
    for i, p in enumerate(photos[:6]):
        r, col = i // cols, i % cols
        x = margin + col*(cell_w+gap)
        y = grid_top - cell_h - r*(cell_h+gap)
        draw_image_full(c, os.path.join(ASSETS, p), x, y, cell_w, cell_h, cover=True)

    page_footer(c); draw_page_number(c, page_num, total); c.showPage()


def page_complementares(c, page_num, total):
    c.setFillColor(SAND); c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    draw_label(c, "Informações", 40, PAGE_H - 60, color=COPPER, char_space=3)
    c.setFont("Helvetica-Bold", 26); c.setFillColor(TABACO); c.setCharSpace(-0.5)
    c.drawString(40, PAGE_H - 95, "Informações complementares do projeto."); c.setCharSpace(0)

    y = PAGE_H - 140
    lx, rx = 40, PAGE_W/2 + 10
    col_w = (PAGE_W - 80 - 20) / 2

    draw_label(c, "Arquiteto do Projeto", lx, y, color=COPPER, size=8.5, char_space=2.5)
    c.setFont("Helvetica-Bold", 12); c.setFillColor(TABACO); c.drawString(lx, y - 18, CFG["arquiteto"])

    draw_label(c, "Medidas do Projeto", lx, y - 50, color=COPPER, size=8.5, char_space=2.5)
    c.setFont("Helvetica-Bold", 12); c.setFillColor(TABACO); c.drawString(lx, y - 68, CFG["modulo_descricao"])
    c.setFont("Helvetica", 11); c.setFillColor(TEXT_DARK)
    c.drawString(lx, y - 84, f"{CFG['area']}  ·  {CFG['dimensoes']}")

    draw_label(c, "Gerenciamento da Instalação", lx, y - 115, color=COPPER, size=8.5, char_space=2.5)
    draw_text_block(c, CFG["gerenciamento_texto"], lx, y - 250, col_w, 130, body_justify)

    draw_label(c, "Observações Gerais", rx, y, color=COPPER, size=8.5, char_space=2.5)
    draw_text_block(c, bullets_blank(CFG["observacoes_gerais"]), rx, y - 250, col_w, 250, list_style)

    sy = 260
    c.setFillColor(TABACO); c.rect(0, 100, PAGE_W, sy - 100 + 30, fill=1, stroke=0)
    draw_label(c, "Serviços fora do escopo orçamentário", 40, sy + 10, color=CREME, size=8.5, char_space=2.5)
    fora = CFG["fora_escopo"]
    fora_l, fora_r = fora[:len(fora)//2 + len(fora)%2], fora[len(fora)//2 + len(fora)%2:]
    list_white = ParagraphStyle("lswl", fontName="Helvetica", fontSize=8.5, leading=12, textColor=WHITE, leftIndent=10, alignment=TA_LEFT)
    draw_text_block(c, bullets(fora_l), 40, 110, (PAGE_W - 100)/2, 100, list_white)
    draw_text_block(c, bullets(fora_r), 40 + (PAGE_W - 100)/2 + 20, 110, (PAGE_W - 100)/2, 100, list_white)

    c.setFont("Helvetica-Oblique", 7.5); c.setFillColor(TEXT_MUTED)
    c.drawString(40, 78, CFG["p8_footnote"])

    page_footer(c); draw_page_number(c, page_num, total); c.showPage()


def page_investimento(c, page_num, total):
    c.setFillColor(TABACO); c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    draw_logo(c, img_path("logo_white"), 40, PAGE_H - 70, max_w=120, max_h=36)
    c.setFont("Helvetica-Bold", 7.5); c.setFillColor(CREME); c.setCharSpace(3)
    c.drawRightString(PAGE_W - 40, PAGE_H - 50, "VISÃO GERAL · TOTAL GERAL"); c.setCharSpace(0)

    y = PAGE_H - 140
    draw_label(c, "Investimento", 40, y, color=CREME, size=10, char_space=3.5)
    y -= 35
    c.setFont("Helvetica-Bold", 32); c.setFillColor(WHITE); c.setCharSpace(-0.5)
    c.drawString(40, y, "Visão geral da proposta."); c.setCharSpace(0)

    card_y, card_h = y - 270, 240
    c.setStrokeColor(CREME); c.setLineWidth(0.5)
    c.rect(40, card_y, PAGE_W - 80, card_h, fill=0, stroke=1)

    in_y = card_y + card_h - 40
    c.setFont("Helvetica-Bold", 9); c.setFillColor(CREME); c.setCharSpace(3)
    c.drawString(60, in_y, f"TINY HOUSE {CFG['modelo_capa']}  ·  OPÇÃO COMPLETA"); c.setCharSpace(0)

    c.setFont("Helvetica-Bold", 64); c.setFillColor(WHITE); c.setCharSpace(-1.5)
    c.drawString(60, in_y - 80, CFG["preco"]); c.setCharSpace(0)

    c.setFont("Helvetica", 11); c.setFillColor(CREME)
    c.drawString(60, in_y - 105, CFG["preco_descricao"])

    row_y = in_y - 165
    cells = [("Área total", CFG["area"]), ("Dimensões", CFG["dimensoes"]), ("Prazo de entrega", CFG["prazo_entrega_curto"])]
    cw = (PAGE_W - 120) / 3
    for i,(label,val) in enumerate(cells):
        cx = 60 + i * cw
        c.setFont("Helvetica-Bold", 7); c.setFillColor(CREME); c.setCharSpace(2.5)
        c.drawString(cx, row_y + 22, label.upper()); c.setCharSpace(0)
        c.setFont("Helvetica-Bold", 16); c.setFillColor(WHITE); c.drawString(cx, row_y, val)

    pay_y = card_y - 30
    draw_label(c, "Prazo de Pagamento", 40, pay_y, color=CREME, char_space=3, size=9)
    pay_y -= 20
    rule_w = PAGE_W - 80
    draw_rule(c, 40, pay_y - 4, rule_w, color=CREME)
    pw = rule_w / len(CFG["parcelas"])
    for i,(pct,desc) in enumerate(CFG["parcelas"]):
        sx = 40 + i * pw
        c.setFont("Helvetica-Bold", 28); c.setFillColor(WHITE); c.setCharSpace(-1)
        c.drawString(sx, pay_y - 50, pct); c.setCharSpace(0)
        c.setFont("Helvetica", 8.5); c.setFillColor(CREME)
        words = desc.split()
        line1, line2 = [], []
        cur = line1
        for w in words:
            cur.append(w)
            if len(" ".join(cur)) > 24 and cur is line1: cur = line2
        c.drawString(sx, pay_y - 70, " ".join(line1))
        c.drawString(sx, pay_y - 82, " ".join(line2))

    obs_y = 70
    c.setFont("Helvetica-Oblique", 7.5); c.setFillColor(CREME)
    c.drawString(40, obs_y + 12, CFG["p9_obs_l1"])
    c.drawString(40, obs_y, CFG["p9_obs_l2"])

    page_footer(c, brand_color=CREME)
    c.setFont("Helvetica", 7); c.setFillColor(CREME)
    c.drawRightString(PAGE_W - 40, 24, f"{page_num:02d} / {total:02d}")
    c.showPage()


def page_contato(c, page_num, total):
    c.setFillColor(SAND); c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    draw_label(c, "Condições", 40, PAGE_H - 60, color=COPPER, char_space=3)
    c.setFont("Helvetica-Bold", 26); c.setFillColor(TABACO); c.setCharSpace(-0.5)
    c.drawString(40, PAGE_H - 95, "Dos valores desta proposta."); c.setCharSpace(0)

    y = PAGE_H - 130
    draw_text_block(c, CFG["clausula_a"], 40, y - 110, PAGE_W - 80, 110, body_justify)
    draw_text_block(c, CFG["clausula_b"], 40, y - 220, PAGE_W - 80, 100, body_justify)
    draw_text_block(c, CFG["clausula_cd"], 40, y - 340, PAGE_W - 80, 110, body_justify)

    sig_y = 230
    draw_rule(c, PAGE_W/2 - 100, sig_y + 20, 200, color=TABACO, thickness=0.7)
    c.setFont("Helvetica-Bold", 10); c.setFillColor(TABACO)
    c.drawCentredString(PAGE_W/2, sig_y, CFG["assinante_nome"])
    c.setFont("Helvetica", 8.5); c.setFillColor(TEXT_MUTED)
    c.drawCentredString(PAGE_W/2, sig_y - 12, CFG["assinante_cargo"])

    band_y, band_h = 0, 165
    c.setFillColor(TABACO); c.rect(0, band_y, PAGE_W, band_h, fill=1, stroke=0)
    draw_logo(c, img_path("logo_white"), 40, band_y + band_h - 70, max_w=180, max_h=55)

    cx, cy = PAGE_W - 40, band_y + band_h - 50
    c.setFont("Helvetica-Bold", 7.5); c.setFillColor(CREME); c.setCharSpace(3)
    c.drawRightString(cx, cy, "CONTATO"); c.setCharSpace(0)
    c.setFont("Helvetica", 9); c.setFillColor(WHITE)
    c.drawRightString(cx, cy - 16, CFG["telefone"])
    c.drawRightString(cx, cy - 30, CFG["email"])
    c.drawRightString(cx, cy - 44, CFG["site_instagram"])

    c.setFont("Helvetica", 8); c.setFillColor(CREME)
    c.drawString(40, band_y + 50, CFG["endereco_l1"])
    c.drawString(40, band_y + 38, CFG["endereco_l2"])

    c.setFont("Helvetica-Oblique", 9); c.setFillColor(CREME)
    c.drawRightString(PAGE_W - 40, band_y + 38, "É usufruir, não construir.")

    c.setFont("Helvetica", 7); c.setFillColor(CREME)
    c.drawCentredString(PAGE_W/2, band_y + 20,
                        f"Cliente: {CFG['cliente']} · Tiny House {CFG['modelo_titulo']} · {page_num:02d} / {total:02d}")

    c.showPage()


# ==========================================================================
def build():
    c = canvas.Canvas(OUTPUT, pagesize=A4)
    c.setTitle(f"Proposta · Tiny House {CFG['modelo_titulo']}")
    c.setAuthor("COMSTEEL Tiny House")
    c.setSubject(f"Proposta Comercial - Tiny House {CFG['modelo_titulo']}")
    c.setCreator("COMSTEEL")
    TOTAL = 10
    page_cover(c)
    page_manifesto(c, 2, TOTAL)
    page_projeto_hero(c, 3, TOTAL)
    page_proposta(c, 4, TOTAL)
    page_revestimentos(c, 5, TOTAL)
    page_mobiliario(c, 6, TOTAL)
    page_galeria(c, 7, TOTAL)
    page_complementares(c, 8, TOTAL)
    page_investimento(c, 9, TOTAL)
    page_contato(c, 10, TOTAL)
    c.save()
    print(f"Proposta gerada: {OUTPUT}")


if __name__ == "__main__":
    build()
