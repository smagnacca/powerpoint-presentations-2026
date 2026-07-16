"""
Example slide: demonstrates A-Patterns #1-#5 from FIRST_RENDER_A_QUALITY_PROTOCOL.md
applied to a single research-fact slide.

  1. Real human photo, circular-cropped with accent ring   -> researcher headshot
  2. Video-textured dark card, properly scrimmed            -> neural-network poster + scrim on right panel
  3. Literal metaphor visual matched to the concept          -> brain/thought icon badge
  4. (Divider pattern -- not applicable to a single content slide, shown via
     a full-bleed scrimmed accent bar carrying the kicker/section label)
  5. Research-citation card + graphic pull-quote pairing     -> left card / right pull-quote
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml import parse_xml
import os

# ---- palette (theme.py constants) ----
WHITE   = RGBColor(0xFF, 0xFF, 0xFF)
INK     = RGBColor(0x0F, 0x17, 0x2A)
SUBTLE  = RGBColor(0x47, 0x55, 0x69)
MUTED   = RGBColor(0x64, 0x74, 0x8B)
BLUE    = RGBColor(0x25, 0x63, 0xEB)
EMERALD = RGBColor(0x05, 0x96, 0x69)
AMBER   = RGBColor(0xD9, 0x77, 0x06)
ROSE    = RGBColor(0xE1, 0x1D, 0x48)
VIOLET  = RGBColor(0x7C, 0x3A, 0xED)
FONT = "Calibri"

SW, SH = Inches(13.333), Inches(7.5)
HERE = os.path.dirname(os.path.abspath(__file__))

def new_deck():
    prs = Presentation()
    prs.slide_width = SW
    prs.slide_height = SH
    return prs

def blank_slide(prs, bg=WHITE):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    rect = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SW, SH)
    rect.fill.solid(); rect.fill.fore_color.rgb = bg
    rect.line.fill.background(); rect.shadow.inherit = False
    return slide

def set_transparency(shape, pct):
    alpha = str(int((100 - pct) * 1000))
    sp = shape.fill.fore_color._xFill
    srgb = sp.find('.//{http://schemas.openxmlformats.org/drawingml/2006/main}srgbClr')
    a = parse_xml(
        f'<a:alpha xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" val="{alpha}"/>'
    )
    srgb.append(a)

def add_text(slide, text, x, y, w, h, size=18, bold=False, italic=False,
             color=INK, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, font=FONT, line_spacing=1.0):
    box = slide.shapes.add_textbox(x, y, w, h)
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    lines = text.split("\n")
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = line_spacing
        r = p.add_run()
        r.text = line
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.italic = italic
        r.font.color.rgb = color
        r.font.name = font
    return box

def add_rich(slide, x, y, w, h, runs_text, size=18, align=PP_ALIGN.LEFT,
             anchor=MSO_ANCHOR.TOP, font=FONT, line_spacing=1.0):
    box = slide.shapes.add_textbox(x, y, w, h)
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    p = tf.paragraphs[0]
    p.alignment = align
    p.line_spacing = line_spacing
    for text, bold, color in runs_text:
        r = p.add_run()
        r.text = text
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.color.rgb = color
        r.font.name = font
    return box

def add_rounded_card(slide, x, y, w, h, fill=WHITE, line_color=None, radius=0.08):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
    card.adjustments[0] = radius
    card.fill.solid(); card.fill.fore_color.rgb = fill
    if line_color:
        card.line.color.rgb = line_color
        card.line.width = Pt(1)
    else:
        card.line.fill.background()
    card.shadow.inherit = False
    return card

def add_gradient_card(slide, x, y, w, h, c1, c2, radius=0.08, angle=45):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
    card.adjustments[0] = radius
    card.fill.gradient()
    stops = card.fill.gradient_stops
    stops[0].color.rgb = c1
    stops[0].position = 0.0
    stops[1].color.rgb = c2
    stops[1].position = 1.0
    card.fill.gradient_angle = angle
    card.line.fill.background()
    card.shadow.inherit = False
    return card

def add_citation(slide, text, x, y, w):
    return add_text(slide, text, x, y, w, Inches(0.3), size=9, italic=True, color=MUTED)

def add_page_num(slide, n):
    add_text(slide, str(n), Inches(12.6), Inches(7.15), Inches(0.6), Inches(0.3),
              size=10, color=MUTED, align=PP_ALIGN.RIGHT)

def add_badge(slide, text, x, y, w, h, fill, text_color=WHITE, size=11):
    pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
    pill.adjustments[0] = 0.5
    pill.fill.solid(); pill.fill.fore_color.rgb = fill
    pill.line.fill.background(); pill.shadow.inherit = False
    tf = pill.text_frame
    tf.word_wrap = False
    tf.margin_left = tf.margin_right = Pt(4)
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = text
    r.font.size = Pt(size); r.font.bold = True; r.font.color.rgb = text_color; r.font.name = FONT
    return pill

def add_circle_photo(slide, img_path, x, y, d, ring_color, src_w, src_h, ring_width=3.5):
    pic = slide.shapes.add_picture(img_path, x, y, width=d, height=d)
    if src_w > src_h:
        excess = (src_w - src_h) / src_w / 2
        pic.crop_left = excess; pic.crop_right = excess
    elif src_h > src_w:
        excess = (src_h - src_w) / src_h / 2
        pic.crop_top = excess; pic.crop_bottom = excess
    geom_xml = ('<a:prstGeom xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" prst="ellipse">'
                '<a:avLst/></a:prstGeom>')
    pic._element.spPr.append(parse_xml(geom_xml))
    pic.line.color.rgb = ring_color
    pic.line.width = Pt(ring_width)
    return pic

def add_bg_texture(slide, img_path, x, y, w, h, scrim_pct=35, scrim_color=INK):
    """Static poster-frame stand-in for add_bg_video() -- same scrim technique."""
    slide.shapes.add_picture(img_path, x, y, width=w, height=h)
    scrim = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    scrim.fill.solid(); scrim.fill.fore_color.rgb = scrim_color
    scrim.line.fill.background(); scrim.shadow.inherit = False
    set_transparency(scrim, scrim_pct)
    return scrim

def add_icon_badge(slide, glyph, x, y, d, c1, c2):
    """Gradient circle + centered glyph -- pattern #3 literal-metaphor icon."""
    circ = slide.shapes.add_shape(MSO_SHAPE.OVAL, x, y, d, d)
    circ.fill.gradient()
    stops = circ.fill.gradient_stops
    stops[0].color.rgb = c1; stops[0].position = 0.0
    stops[1].color.rgb = c2; stops[1].position = 1.0
    circ.line.fill.background(); circ.shadow.inherit = False
    tf = circ.text_frame
    tf.word_wrap = False
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = glyph
    r.font.size = Pt(int(d / Emu(1) / 914400 * 26)); r.font.bold = True
    r.font.color.rgb = WHITE; r.font.name = "Segoe UI Symbol"
    return circ

# ---------------------------------------------------------------------------
# BUILD THE ONE EXAMPLE SLIDE
# ---------------------------------------------------------------------------
prs = new_deck()
s = blank_slide(prs, bg=WHITE)

# Pattern #4 (adapted): full-bleed section kicker bar, scrimmed dark, carries
# the "divider" DNA (minimal type over a dark bar) onto a content slide.
kicker_bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SW, Inches(0.75))
kicker_bar.fill.solid(); kicker_bar.fill.fore_color.rgb = INK
kicker_bar.line.fill.background(); kicker_bar.shadow.inherit = False
add_text(s, "RESEARCH SPOTLIGHT", Inches(0.5), Inches(0.13), Inches(6), Inches(0.5),
          size=14, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
add_badge(s, "2 OF 3 SOURCES", Inches(11.0), Inches(0.15), Inches(1.9), Inches(0.45), fill=AMBER)

# ---- LEFT: Pattern #5 research-citation card ----
card_x, card_y, card_w, card_h = Inches(0.6), Inches(1.15), Inches(5.6), Inches(5.7)
add_rounded_card(s, card_x, card_y, card_w, card_h, fill=WHITE, line_color=RGBColor(0xE2, 0xE8, 0xF0), radius=0.04)

add_text(s, "Proceedings of CHI 2025 · Microsoft Research × Carnegie Mellon",
          card_x + Inches(0.35), card_y + Inches(0.3), card_w - Inches(0.7), Inches(0.4),
          size=11, italic=True, color=BLUE)
rule = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, card_x + Inches(0.35), card_y + Inches(0.72), card_w - Inches(0.7), Pt(1))
rule.fill.solid(); rule.fill.fore_color.rgb = RGBColor(0xE2, 0xE8, 0xF0); rule.line.fill.background(); rule.shadow.inherit = False

add_text(s, "The Impact of Generative AI\non Critical Thinking",
          card_x + Inches(0.35), card_y + Inches(0.85), card_w - Inches(0.7), Inches(1.0),
          size=24, bold=True, color=INK, line_spacing=1.05)

add_text(s, "Lee, H., et al. (2025)\nSurvey of 319 knowledge workers",
          card_x + Inches(0.35), card_y + Inches(1.75), card_w - Inches(0.7), Inches(0.6),
          size=11, color=MUTED, line_spacing=1.2)

add_badge(s, "KEY FINDING", card_x + Inches(0.35), card_y + Inches(2.4), Inches(1.5), Inches(0.32), fill=BLUE, size=10)

add_rich(s, card_x + Inches(0.35), card_y + Inches(2.85), card_w - Inches(0.7), Inches(1.3),
          [("When people trust the AI more, they ", False, INK),
           ("accept its answer at face value", True, ROSE),
           (" — less checking, less scrutiny. When people trust ", False, INK),
           ("themselves", False, INK),
           (" more, they ", False, INK),
           ("verify and question", True, EMERALD),
           (" what the AI gives them.", False, INK)],
          size=14, line_spacing=1.25)

# stats row
add_text(s, "319", card_x + Inches(0.35), card_y + Inches(4.35), Inches(1.4), Inches(0.5), size=28, bold=True, color=BLUE)
add_text(s, "professionals\nsurveyed", card_x + Inches(0.35), card_y + Inches(4.9), Inches(1.4), Inches(0.5), size=10, color=MUTED, line_spacing=1.1)
add_text(s, "936", card_x + Inches(1.9), card_y + Inches(4.35), Inches(1.4), Inches(0.5), size=28, bold=True, color=BLUE)
add_text(s, "real AI\nuse cases", card_x + Inches(1.9), card_y + Inches(4.9), Inches(1.4), Inches(0.5), size=10, color=MUTED, line_spacing=1.1)

# Pattern #1: real human photo, circular-cropped with accent ring (the researcher)
add_circle_photo(s, os.path.join(HERE, "researcher.jpg"),
                  card_x + card_w - Inches(1.55), card_y + card_h - Inches(1.55),
                  Inches(1.15), ring_color=BLUE, src_w=1200, src_h=1800, ring_width=3.5)
add_text(s, "Dr. H. Lee, lead author", card_x + card_w - Inches(2.85), card_y + card_h - Inches(0.42),
          Inches(1.3), Inches(0.3), size=8, color=MUTED, align=PP_ALIGN.RIGHT)

# Pattern #3: literal metaphor icon badge (brain/thought glyph) pinned on the card
add_icon_badge(s, "⚡", card_x + card_w - Inches(0.45), card_y - Inches(0.35), Inches(0.8), AMBER, ROSE)

# ---- RIGHT: Pattern #2 video-textured dark card (scrimmed) + Pattern #5 pull-quote ----
pq_x, pq_y, pq_w, pq_h = Inches(6.55), Inches(1.15), Inches(6.2), Inches(5.7)
add_bg_texture(s, os.path.join(HERE, "neural_poster.jpg"), pq_x, pq_y, pq_w, pq_h, scrim_pct=35, scrim_color=INK)

add_text(s, "“", pq_x + Inches(0.5), pq_y + Inches(0.5), Inches(1.2), Inches(1.2),
          size=80, bold=True, color=AMBER)

add_text(s,
          "“Trust the AI more, and\nyou stop checking its work.\nTrust YOURSELF more, and\nyou start questioning it.”",
          pq_x + Inches(0.6), pq_y + Inches(1.75), pq_w - Inches(1.2), Inches(3.1),
          size=26, italic=True, bold=True, color=WHITE, line_spacing=1.15)

add_text(s, "— it's the confidence balance, not the AI, that drives the outcome",
          pq_x + Inches(0.6), pq_y + Inches(5.05), pq_w - Inches(1.2), Inches(0.5),
          size=13, color=RGBColor(0xCB, 0xD5, 0xE1))

add_citation(s, "Source: Lee et al., “The Impact of Generative AI on Critical Thinking,” CHI 2025.",
              Inches(0.6), Inches(7.05), Inches(9))
add_page_num(s, 1)

out_path = os.path.join(HERE, "research_slide_example.pptx")
prs.save(out_path)
print("Saved:", out_path)
