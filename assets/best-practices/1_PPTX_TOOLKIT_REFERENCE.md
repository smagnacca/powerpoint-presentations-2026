# TOOLKIT REFERENCE — python-pptx A-Quality Deck System

Extracted from `module3/build_v5/{theme.py, compose_clip.py, build_v5.py}` on **2026-07-11**.

This is the exact, reusable toolkit for regenerating a 16:9 (13.333" × 7.5") presentation that renders A-quality on first pass. All coordinates use `pptx.util.Inches` / `Pt` / `Emu`.

---

## Palette Constants (theme.py)

Module-2-verified "white bg + complementary accents" palette. All are `RGBColor`.

| Name | Hex | Role |
|---|---|---|
| `WHITE` | `#FFFFFF` | Default background |
| `INK` | `#0F172A` | Headline text / dark cards (slate-900) |
| `SUBTLE` | `#475569` | Secondary body text (slate-600) |
| `MUTED` | `#64748B` | Tertiary text, captions (slate-500) |
| `BLUE` | `#2563EB` | Primary accent |
| `EMERALD` | `#059669` | Success / positive accent |
| `AMBER` | `#D97706` | Warning / attention accent |
| `ROSE` | `#E11D48` | Danger / contrast accent |
| `VIOLET` | `#7C3AED` | Secondary / "IP" accent |

**Canvas:** `SW, SH = Inches(13.333), Inches(7.5)` · `FONT = "Calibri"`.

---

## Reusable Helper Functions

### Deck + slide primitives

| Signature | Purpose |
|---|---|
| `new_deck()` | Returns a `Presentation` sized to 13.333×7.5 (16:9). |
| `blank_slide(prs, bg=WHITE)` | Adds slide on layout[6] (blank), paints full-bleed bg rect, sends to back. |

### Text primitives

| Signature | Purpose |
|---|---|
| `add_text(...)` | Multi-line textbox; splits on `\n`. The workhorse. |
| `add_rich(...)` | One paragraph of mixed-format runs; `runs_text` = list of `(text, bold, color)` tuples. |
| `add_bullets(...)` | Bulleted list; prefixes each with `"•  "`. |

### Layout / heading primitives

| Signature | Purpose |
|---|---|
| `add_kicker_title(...)` | Uppercase kicker + big title + accent rule bar. Returns y-baseline for content flow. |
| `add_rounded_card(...)` | Rounded rectangle card; optional border; shadow off. |
| `add_citation(...)` | 9pt italic muted source line at the bottom. |
| `add_page_num(slide, n)` | 10pt muted right-aligned number bottom-right. |

### Finishing devices

| Signature | Purpose |
|---|---|
| `add_badge(...)` | Pill (rounded rect radius 0.3) with centered label. |
| `add_icon_circle(...)` | Simple ringed oval (2.5pt outline). |
| `add_circle_photo(...)` | **Square-crops a photo to its center then masks to a circle with a colored ring.** See §3. |
| `add_gradient_card(...)` | Gradient rounded-rect. |
| `add_icon_badge(...)` | Gradient circle + white vector glyph on top. |
| `add_stat_ring(...)` | Native pptx doughnut chart filled to pct, with big number overlaid. |
| `set_transparency(shape, pct)` | Injects `<a:alpha>` into a solid-fill shape. `pct` = percent transparent. |

### Background helpers

Both layer a media fill **plus a semi-transparent scrim** over whatever card was already drawn. Content added *after* the call still renders on top.

```python
def add_bg_video(slide, name, x, y, w, h, scrim_pct=42, scrim_color=INK):
    slide.shapes.add_movie(CLIPS + name + ".mp4", x, y, w, h,
                           poster_frame_image=POSTERS + name + ".jpg", mime_type="video/mp4")
    scrim = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    scrim.fill.solid(); scrim.fill.fore_color.rgb = scrim_color
    scrim.line.fill.background(); scrim.shadow.inherit = False
    set_transparency(scrim, scrim_pct)
```

**Scrim value cheat-sheet (as actually used):**
- **Light content slides (texture):** `scrim_pct=11–14` (white scrim). The poster is barely visible so INK text stays crisp.
- **Dark feature cards (video over INK/gradient):** `scrim_pct=22–35`. e.g. `neural_network_card` 22, `hybrid_advisor_card` 30, `research` cards 35.
- **Dark section cards with white text:** `scrim_pct=52–58`. e.g. `authenticity_paradox_card` 58, `iteration_loop_card` 55.
- **Full-bleed title/divider:** `scrim_pct=52–55`.
- **Rule of thumb:** more white text on top → higher scrim_pct; texture-only background → ~13.

---

## The Circle-Photo Technique

Python-pptx has no crop-to-circle. The trick is (a) square-crop from source aspect, then (b) append an `ellipse` `prstGeom` element.

```python
def add_circle_photo(slide, img_path, x, y, d, ring_color, src_w, src_h, ring_width=3.5):
    """Photo cropped to a circle with a colored ring."""
    from pptx.oxml import parse_xml
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
```

**Pass `src_w`/`src_h` as true source pixel dimensions** so excess-crop math is correct.

---

## compose_clip.py — the video compositor

Turns a raw clip into a deck-ready 15-second loop. Default mode (`bake_text=False`) produces **pure ambient motion, no text** — the slide's own pptx text already plays the headline role.

**FFmpeg crop approach (fit-to-fill without distortion):**
```bash
scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},setsar=1
```

**Text in post (never baked):** Render a transparent RGBA PNG via PIL (`render_text_png` — Arial Bold, sky-blue on soft rounded box for legibility), then composite with ffmpeg `overlay` + `fade` filters. Headline window 0–4s; closing 10.5–15s.

---

## The "Deck-as-a-Program" Pattern (build_v5.py)

**Structure:** one top-to-bottom Python script — `from theme import *`, `prs = new_deck()`, then one code block per slide in order, ending in `prs.save(...)`. 

Repeated archetypes factored into closures: `jensen_slide(...)`, `research_slide(...)`, `engagement_slide(...)`, `persona_slide(...)`, `tool_spotlight(...)`.

**Per-slide layering order (bottom → top):**
1. `blank_slide(prs, bg=...)` — base background rect (sent to back).
2. Shape/gradient (`add_gradient_card` / `add_rounded_card`).
3. Media + scrim (`add_bg_video` / `add_bg_texture`).
4. Content on top — icon badges, circle photos, text, badges. (Rendered on top of the scrim untouched.)
5. `add_citation` and `add_page_num` last.

**Page-numbering pattern:**
```python
PAGE = [0]
def pg():
    PAGE[0] += 1
    return PAGE[0]
```
Every slide ends with `add_page_num(s, pg())`. Numbers stay correct regardless of how many slides each factory emits.

**Save:** the file is one `Presentation` object mutated throughout. Last line:
```python
prs.save("/Users/scottmagnacca/Desktop/Novartis_Module3_Part2_Version5_2026-07-11.pptx")
print("FINAL Built:", len(prs.slides._sldIdLst))
```

---

## For the next builder

- `theme.py` is clean and complete (all V5 deltas present).
- Assets resolved relative to CWD, so run the build from inside `build_v5/` (expects `imgs/`, `clips/`, `posters/` siblings).
- Final deck = 33 slides (1 title → 29 content → 3 appendix).
