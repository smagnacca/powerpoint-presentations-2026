# PowerPoint Presentations 2026 — A-Quality Deck Framework

**Project Type:** Reusable presentation design system  
**Status:** Active framework for high-quality slide decks  
**Created:** July 12, 2026  
**Last Updated:** July 12, 2026  

---

## Project Overview

This project consolidates the proven methodology and reusable assets from the **Novartis Module 3 Part 2 rebuild** to enable **first-render A-quality PowerPoint presentations** without the 5–7 hour iteration cycle.

### Core Innovation
The V1→V5 rebuild taught us that the rubric for "A-quality" is fully knowable *before* rendering. By applying a deterministic checklist during authoring (not after), any presentation reaches A-grade on the first render.

### What's Included
1. **FIRST_RENDER_A_QUALITY_PROTOCOL.md** — The complete build system (4 stages, 10-point checklist, 11 guardrails, 3-lens rubric)
2. **HERMES_SUMMARY_KEY_LEARNINGS.md** — One-page shareable reference for team/AI systems
3. **1_PPTX_TOOLKIT_REFERENCE.md** — Complete python-pptx API (palette, helpers, circle-photo technique, scrim values)
4. **Novartis_Module3_Part2_Version5_2026-07-11.pptx** — Reference deck (33 slides, A-grade, video-enhanced)
5. **Build scripts** (copied from Novartis project on request)

---

## Quick Start

For **any new presentation:**

1. Read `assets/best-practices/FIRST_RENDER_A_QUALITY_PROTOCOL.md`
2. Copy `theme.py` + `compose_clip.py` + `build_v5.py` from Novartis project
3. Apply the 10-point checklist before writing code
4. Render once to PDF locally
5. Done — no iteration needed

---

## The 10 Failure Patterns (Guardrails)

| # | Pattern | Guard |
|---|---------|-------|
| 1 | Dead bottom zone (15–55% empty canvas) | Fill bottom with content, media, or gradient |
| 2 | Visible placeholder ("[photo here]", empty ring) | Pre-source ALL images; never leave stubs |
| 3 | Off-palette color (e.g., mint-green stray) | Use only the 9-color palette (WHITE, INK, SUBTLE, MUTED, BLUE, EMERALD, AMBER, ROSE, VIOLET) |
| 4 | Repeated template (unchanged 2+ slides) | Vary the archetype per slide |
| 5 | Flat card (no gradient, no accent, no icon) | Every card = gradient OR icon badge OR accent bar |
| 6 | No focal anchor (no face, no metaphor) | Every slide must have ≥1 human photo OR visual metaphor |
| 7 | Under-scrimmed video (text washes out) | Scrim_pct: light 11–14%, dark card 22–58% |
| 8 | Dense text, no chunking (no dividers/badges) | Break text into ≤3 lines per section |
| 9 | Generic stock photo (not matched to concept) | Source images that metaphorically match the slide's idea |
| 10 | Orphaned bold statement (floats unmoored) | Anchor big text to ≥1 supporting element |

---

## The A-Grade Rubric (3 Independent Lenses)

✅ **Busy Salesperson (3-sec skim):** Can I find the key insight in 3 seconds?  
✅ **UX Expert (hierarchy & contrast):** Is information chunked? Is hierarchy clear?  
✅ **Graphic Designer (polish):** Are shapes aligned? Is there a hero element? Right palette?  

**All 3 must pass for A-grade.**

---

## Python-pptx Toolkit (Reusable)

**Palette:**  
`WHITE`, `INK` (#0F172A), `SUBTLE` (#475569), `MUTED` (#64748B), `BLUE` (#2563EB), `EMERALD` (#059669), `AMBER` (#D97706), `ROSE` (#E11D48), `VIOLET` (#7C3AED)

**Key Helpers:**  
`add_text()`, `add_rounded_card()`, `add_gradient_card()`, `add_icon_badge()`, `add_circle_photo()`, `add_bg_video()`, `set_transparency()`

**Per-slide layering (bottom → top):**
1. Background rect
2. Shape/gradient
3. Media + scrim
4. Content (text, icons, photos)
5. Citation + page number

---

## Build Protocol (4 Stages)

### Stage 1: Pre-Flight (Bash)
- Force-materialize iCloud files
- Verify save-path filename is NEW version
- Lock prior version to archive
- Verify catalogued assets exist on disk

### Stage 2: Build-Time Checklist (10 points)
- All images pre-sourced, verified on disk
- No palette stray colors
- ≥1 gradient or icon badge per card
- Every slide has ≥1 focal anchor
- Video scrim values correct
- Text density: ≤3 chunks per card
- No placeholder stubs or empty rings
- Archetypes vary (jensen, research, engagement, persona)
- Bottom zone filled (no dead space >55% empty)
- Every headline paired with visual anchor

### Stage 3: Post-Build QA (Local)
- Render to PDF
- 3-lens review (salesperson, UX, designer)
- Verify contrast on all backgrounds
- Check all video scrims visually

### Stage 4: Optional Review (MiniMax M3)
- Send PDF to 3-agent panel (~$0.25/session)
- Provides detailed feedback & scoring

---

## Reference Deck

**Novartis_Module3_Part2_Version5_2026-07-11.pptx**
- 33 slides at A-grade
- 3-agent MiniMax M3 verified (busysalesperson/UX/designer lenses)
- Video-enhanced with proper scrim values
- Full circle-photo technique with colored rings
- Reusable slide archetypes (jensen, research, engagement, persona)

**Use as:** Architectural reference for slide structure, gradient/icon patterns, text hierarchy, video background treatment.

---

## Asset Organization

```
powerpoint-presentations-2026/
├── CLAUDE.md                          (this file)
├── README.md                          (quick reference)
├── CHANGELOG.md                       (versions & updates)
├── assets/
│   ├── Novartis_Module3_Part2_Version5_2026-07-11.pptx  (reference deck)
│   └── best-practices/
│       ├── FIRST_RENDER_A_QUALITY_PROTOCOL.md          (full system)
│       ├── HERMES_SUMMARY_KEY_LEARNINGS.md             (1-page ref)
│       └── 1_PPTX_TOOLKIT_REFERENCE.md                 (API docs)
```

---

## Next Presentation

1. Create a new folder: `~/Documents/Claude/Projects/powerpoint-presentations-2026/[presentation-name]/`
2. Copy `theme.py`, `compose_clip.py`, `build_v5.py` from Novartis project
3. Read `assets/best-practices/FIRST_RENDER_A_QUALITY_PROTOCOL.md`
4. Apply the 10-point checklist before coding
5. Render once to PDF locally
6. Done

---

## Key Insight

**Time is spent discovering the rubric, not applying it.**

The V1→V5 rebuild was 5–7 hours climbing from 2.3/4.0 → A-grade. If this rubric had been the build spec from the start, the deck would have shipped A on first render.

**Next deck: Checklist-driven. One render. Done.**

---

## Related Projects

- **Novartis-Emeritus-Sales-Project** — Original context where this protocol was extracted
- **VIDEO-PRODUCTION-MASTER** — B-roll asset libraries (ai-tech, stock-photos, gemini-generated)

---

## Project Metadata

**Created:** July 12, 2026  
**Framework Version:** 1.0 (extracted from Novartis Module 3 rebuild)  
**Status:** Active — ready for new presentations  
**Next Review:** When creating a new presentation deck  

---

**Ready to generate A-quality decks on first render. Zero iteration needed.**
