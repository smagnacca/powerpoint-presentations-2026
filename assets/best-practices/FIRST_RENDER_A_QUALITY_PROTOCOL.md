# FIRST-RENDER A-QUALITY PROTOCOL — Novartis Module 3 Deck

**Date:** July 11, 2026 | **Deck:** Novartis Module 3 Part 2 (33 slides, 16:9, 226MB)

This protocol consolidates the complete knowledge from the July 11 rebuild (V1→V5) into a single operational guide. Follow these steps to generate a presentation at A-quality on the FIRST render, eliminating the 5–7 hour debug cycle.

---

## THE COMPLETE WORKFLOW (4 stages)

### STAGE 1: PRE-FLIGHT (before any build script runs)

**A. Force-materialize every input** (guards against iCloud dataless-file reads):
```bash
find module3/build_v5 -type f \( -name '*.py' -o -name '*.mp4' -o -name '*.jpg' -o -name '*.png' \) \
  -exec brctl download {} \; 2>/dev/null
find module3/build_v5 -type f -exec dd if={} of=/dev/null bs=1m \; 2>/dev/null
find module3/build_v5 -type f -exec sh -c 'test -s "$1" || echo "EMPTY (dataless): $1"' _ {} \;
```

**B. Confirm the save-path filename is the NEW version:**
```bash
grep -n "prs.save" module3/build_v5/build_v5.py   # must show V5 name, NOT V4
```

**C. Lock the prior approved deck to immutable archive:**
```bash
cp ~/Desktop/Novartis_Module3_Part2_Version4_2026-07-11.pptx assets/_locked/ 2>/dev/null
```

**D. Verify every catalogued asset path exists:**
Check `VIDEO-PRODUCTION-MASTER/memory/BROLL-LIBRARY-LOCATION.md` — never rely on a file you haven't verified on disk.

**E. Confirm FFmpeg text path (this Mac lacks freetype):**
```bash
ffmpeg -filters 2>/dev/null | grep -q drawtext || echo "No drawtext → use PIL-PNG overlay path"
```

**F. Citation + asset-provenance gate (manual):**
Every stat traced to a primary URL; every clip transcribed (never guessed from filename).

---

### STAGE 2: BUILD (authoring slides)

**Apply the 10-point A-grade checklist to EVERY slide BEFORE writing the code:**

1. ☐ Empty canvas **≤15%**? If not, add a takeaway band or supporting element.
2. ☐ **Zero visible placeholders** — every circle has a photo, icon, or frame (never empty).
3. ☐ **On-palette only** — navy/ink base, white cards, the 5 named accents. No mint, no ad-hoc colors.
4. ☐ Every **card** = gradient fill + icon badge on headline + accent bar (never flat single-fill).
5. ☐ One **focal anchor** per content slide (human photo or literal metaphor).
6. ☐ Any **background video is scrimmed** (AA contrast verified).
7. ☐ Any **reused template** is differentiated (accent color + clip + metaphor).
8. ☐ No **orphaned bold statement** — anchor it in a card or accent bar.
9. ☐ Dense text is **chunked** with dividers/badges.
10. ☐ Imagery is **thematically literal** to this slide, not generic stock.

**Scrim values (critical for readability):**
- Light content slides (texture bg): `11–14%` scrim (white)
- Dark feature cards (video over INK): `22–35%` scrim
- Dark section cards with white text: `52–58%` scrim
- Full-bleed title/divider: `52–55%` scrim

**Per-slide layering order (bottom → top):**
1. `blank_slide(prs, bg=...)` — base background.
2. Shape/gradient.
3. Media + scrim.
4. Content on top (always renders above the scrim).
5. `add_citation` and `add_page_num` last.

---

### STAGE 3: POST-BUILD QA (before presenting to Scott)

**1. Render to PDF and eyeball EVERY slide:**
```bash
soffice --headless --convert-to pdf --outdir /tmp/qa ~/Desktop/Novartis_Module3_Part2_Version5_2026-07-11.pptx
pdftoppm -png -r 90 /tmp/qa/Novartis_Module3_Part2_Version5_2026-07-11.pdf /tmp/qa/slide
```

For every slide verify:
- No text collision (baked video text vs native title)
- No ghost/old baked text on clips
- No visible placeholder
- Scrim contrast correct (dark cards 42–58%, light 11–14%)
- Card headlines carry icon/number anchor
- Repeated templates visually differentiated
- No empty bottom third

**2. Confirm slide count and prior version intact:**
```bash
python3 -c "from pptx import Presentation; print(len(Presentation('~/Desktop/Novartis_Module3_Part2_Version5_2026-07-11.pptx').slides._sldIdLst))"
ls -lh ~/Desktop/Novartis_Module3_Part2_Version4_2026-07-11.pptx   # V4 must still exist + nonzero
```

**3. File-size sanity check (guards against file-size blowup from embedding video):**
Should be ~200–250MB, NOT >500MB.

**4. Archive the approved output to assets/ immediately:**
```bash
cp ~/Desktop/Novartis_Module3_Part2_Version5_2026-07-11.pptx assets/Novartis_Module3_Part2_Version5_FINAL_$(date +%Y-%m-%d).pptx
```

---

### STAGE 4: REVIEW & HANDOFF (optional: MiniMax M3 verification)

If you've applied the checklist in Stage 2, Stage 3 QA will pass. The optional MiniMax M3 review (3 agents: salesperson, UX expert, designer) is a *confirmation* pass, not a discovery tool. Cost: ~$0.25.

---

## THE A-GRADE DESIGN RUBRIC (what passes all 3 lenses)

**Three Reviewer Lenses:**
| Lens | Rewards (→ A) | Punishes (→ D/F) |
|---|---|---|
| **Busy Salesperson** (3-sec skim) | One dominant hook; message instantly clear; a human face | No visual hook; dense text; repeated template they've learned to skip |
| **UX Expert** (hierarchy, density, contrast) | Correct hierarchy; **purposeful** whitespace; AA-legible contrast; scannable chunking | Dead zones (15–55% empty); low-contrast cards; text washing out |
| **Graphic Designer** (composition, color, texture) | Looks bespoke/"finished"; on-palette; layered depth (scrim+gradient+ring); intentional composition | Off-palette color (mint); flat template; **visible placeholders**; identical back-to-back templates |

**DESIGN is the harshest grader.** To score A overall, satisfy the DESIGN lens: finished, layered, on-palette, non-repeating.

---

## THE 4 A-PATTERNS (standardize these as components)

1. **Real human photo, full-bleed or circular-cropped with accent ring** — #1 memory anchor.
2. **Video-textured dark card/background, properly scrimmed** — difference between "finished" and "wireframe."
3. **Literal metaphor visual matched to the slide's concept** — beats generic stock every time.
4. **Full-bleed scrimmed video divider with minimal 3-tier type** — the divider standard.
5. **Research-citation card + graphic pull-quote pairing** — every presentation includes 2–3 sources of academic research, each presented as a research highlight card (source line, title, authors/year, key-finding callout, supporting stats) positioned on the left of the slide, paired with a large graphic pull-quote on the right (or a following slide) that isolates the research's main message in bold, oversized editorial type. Vary the card's stat count, highlight color, and quote layout per source so no two research slides look identical.

---

## THE 11 RANKED ANTI-PATTERNS (what to avoid)

| Incident | Root Cause | Guardrail |
|---|---|---|
| Approved V4 overwritten by build_v5 | Save-path string not updated | Grep the save-path line before every run; snapshot prior deck to immutable archive FIRST. |
| Fabricated stats shipped | LLM invented plausible numbers | Audit every stat against primary URL before render. Only Confirmed stats survive. |
| Fabricated Jensen clip index | Guessed clip contents from filename | Never describe audio/video from filename. Transcribe locally first. |
| iCloud dataless read failures | Files evicted to iCloud materialize lazily | Force-materialize all inputs via `brctl download` + `dd` before build. |
| Baked video text colliding with slide title | Two independent text systems overlapped | Never bake headline text into slide-background video. Ambient motion only. |
| Mass-file trashing scare | Deliverables lived only on Desktop | Archive approved versions to `assets/`. Every deck regenerable from persisted `build_vN.py`. |
| Stale clips with old baked-in text | Cached artifact not invalidated after compositor change | Re-render ALL clips after any `compose_clip.py` change. Delete `clips/` and rebuild. |
| Stale b-roll catalog pointer | Hand-edited index never reconciled with disk | Verify every catalogued path exists before relying on it. |
| FFmpeg `drawtext` missing | Assumed standard FFmpeg feature present | This Mac has no freetype. Use PIL-PNG-overlay path in `compose_clip.py`. |
| Card-shaped video placements clipping | Forced full-HD 16:9 into mismatched aspect ratio | Render each clip at its target card's actual aspect ratio. |
| File-size blowup from video embedding | Used `add_bg_video` where motion imperceptible | Use `add_bg_video` only for heroes; use `add_bg_texture` (static poster JPG) elsewhere. |

---

## ASSET SOURCING (priority order — cheapest first)

1. **Reuse catalogued assets** ($0, see `VIDEO-PRODUCTION-MASTER/memory/BROLL-LIBRARY-LOCATION.md`):
   - `ai-tech/INDEX.md` (24 assets: Pexels AI/tech/neural stock)
   - `stock-photos-people/INDEX.md` (4 assets: Pexels faces/personas)
   - `gemini-generated/INDEX.md` (2 assets: bespoke Gemini Omni clips already rendered)

2. **Free internet stock** ($0, Pexels — commercial use, no attribution):
   - Download, verify watermark-free, **add to the correct sub-library and catalogue it**.

3. **Paid Gemini Omni** (~$1/10s clip, only for bespoke visual metaphors no stock can represent):
   - Get explicit Scott approval first. Max $2.50/session.
   - Output: 720×1280 portrait, no baked text, SynthID-watermarked (do NOT strip).
   - Deposit to `assets/broll/gemini-generated/` and catalogue.

---

## TOOLKIT API (see 1_PPTX_TOOLKIT_REFERENCE.md for full reference)

- **Palette:** `WHITE`, `INK`, `SUBTLE`, `MUTED`, `BLUE`, `EMERALD`, `AMBER`, `ROSE`, `VIOLET`
- **Primitives:** `new_deck()`, `blank_slide()`, `add_text()`, `add_rounded_card()`, `add_kicker_title()`
- **Finishing:** `add_badge()`, `add_circle_photo()`, `add_gradient_card()`, `add_icon_badge()`, `add_bg_video()`, `set_transparency()`
- **Circle-photo key:** pass true source pixel dims (`src_w`, `src_h`) so square-crop math is correct.
- **Page-numbering:** mutable counter `PAGE = [0]` + `pg()` helper. Every slide ends with `add_page_num(s, pg())`.

---

## THE ONE-LINE TAKEAWAY

**The reviewers' rubric is not a mystery to be discovered after the render — it's a checklist to build against.** Scaffold from the persisted toolkit, force-materialize and verify inputs, confirm the save path, self-apply the A-grade rubric per slide, render once to verify locally. Everything above is the difference between a deck that *starts* at A and one that spends hours climbing to it.

