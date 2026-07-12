# Module 3 Best Practices — Key Learnings for Hermes

**Date:** July 11, 2026  
**Context:** Extracted from V1→V5 deck rebuild (5–7 hour optimization cycle)  
**Purpose:** Enable first-render A-quality presentations without iteration

---

## The Problem

Starting deck (V1): **2.24/4.0** score from 3-agent panel (busy salesperson, UX expert, graphic designer).  
**13 slides rated D/F.** Each failure traced to the same 10 root causes, making it predictable.

## The Solution

The rubric itself is **knowable before rendering.** Apply it as a build-time checklist, not a post-hoc quality gate.

---

## The 10 Failure Patterns (Guardrails)

| # | Pattern | Guard | Example |
|---|---------|-------|---------|
| 1 | Dead bottom zone (15–55% empty canvas) | Fill bottom with content, media, or gradient | Add shaped badge/icon in lower third |
| 2 | Visible placeholder ("[photo here]", empty ring) | Pre-source ALL images; never leave stubs | Verify every img in build script before render |
| 3 | Off-palette color (e.g., mint-green stray) | Use only: WHITE, INK, SUBTLE, MUTED, BLUE, EMERALD, AMBER, ROSE, VIOLET | Palette defined in theme.py; grep/verify |
| 4 | Repeated template (unchanged 2+ slides) | Vary the archetype per slide (jensen_slide, research_slide, engagement_slide, etc.) | Use per-slide factories, never copy-paste |
| 5 | Flat card (no gradient, no accent, no icon) | Every card = gradient OR icon badge OR accent bar | Add ≥1 visual detail per card minimum |
| 6 | No focal anchor (no face, no metaphor) | Every slide must have ≥1 human photo OR visual metaphor | Use circle-photo technique for faces |
| 7 | Under-scrimmed video (text washes out) | Scrim_pct: light 11–14%, dark card 22–58% | Verify scrim per media type; test text contrast |
| 8 | Dense text, no chunking (no dividers/badges) | Break text into ≤3 lines per section; use dividers/badges | Split into ≤3 chunks per card |
| 9 | Generic stock photo (not matched to concept) | Source images that metaphorically match the slide's idea | Asset sourcing decision tree: free stock 1st, Gemini Omni only for bespoke |
| 10 | Orphaned bold statement (floats unmoored) | Anchor big text to ≥1 supporting element (icon, accent bar, photo) | Pair every headline with a visual anchor |

---

## The A-Grade Rubric (3 Independent Lenses)

**Busy Salesperson (3-sec skim):**
- Can I find the key number/insight in 3 seconds?
- Is there a focal point (face, big number, icon)?
- Does it look "done" or templated?

**UX Expert (hierarchy & contrast):**
- Is the information chunked into ≤3 visual units?
- Is the hierarchy clear (big/bold for headline, smaller for detail)?
- Is there ≥1.5x contrast between text and background?

**Graphic Designer (polish):**
- Are shapes aligned and proportional?
- Is there one "hero" element per slide (photo, gradient, icon)?
- Does the color palette match the brand (no stray colors)?

**All 3 must pass for A-grade.** A single fail = B or lower.

---

## Python-pptx Toolkit (Reusable)

**Palette:**
```
WHITE, INK (#0F172A), SUBTLE (#475569), MUTED (#64748B),
BLUE (#2563EB), EMERALD (#059669), AMBER (#D97706),
ROSE (#E11D48), VIOLET (#7C3AED)
```

**Key Helpers:**
- `add_text(...)` — multi-line textbox (the workhorse)
- `add_rounded_card(...)` — card with optional border
- `add_gradient_card(...)` — gradient background
- `add_icon_badge(...)` — gradient circle + glyph
- `add_circle_photo(...)` — square-crop + ellipse mask (XML prstGeom)
- `add_bg_video(...)` — media + semi-transparent scrim on top
- `set_transparency(shape, pct)` — inject `<a:alpha>` into XML

**Per-slide layering (bottom → top):**
1. Background rect
2. Shape/gradient
3. Media + scrim
4. Content (text, icons, photos)
5. Citation + page number

**Scrim values (opacity):**
- Light texture: 11–14%
- Dark feature card: 22–35%
- Dark section card with white text: 52–58%

---

## Build Protocol (4 Stages)

### Stage 1: Pre-Flight (Bash)
```bash
# Force-materialize iCloud files
brctl download ~/Documents/Claude/Projects/...
# Verify save-path filename is NEW version
grep "FINAL Built" build_v5.py | head -1
# Lock prior version
mv Novartis_Module3_Part2_Version4_2026-07-11.pptx ./_archive/
# Verify assets exist
ls -la module3/build_v5/{imgs,clips,posters}/ | wc -l
```

### Stage 2: Build-Time Checklist (10 points)
- [ ] All images pre-sourced, verified to exist on disk
- [ ] No palette stray colors; grep theme.py
- [ ] ≥1 gradient or icon badge per card
- [ ] Every slide has ≥1 focal anchor (photo/metaphor)
- [ ] Video scrim values correct (11–14% or 22–58%)
- [ ] Text density: ≤3 chunks per card
- [ ] No placeholder stubs or empty rings
- [ ] Archetypes vary (jensen, research, engagement, persona)
- [ ] Bottom zone filled (no dead space >55% empty)
- [ ] Every headline paired with visual anchor

### Stage 3: Post-Build QA (Local)
- Render to PDF locally
- 3-lens review (salesperson, UX, designer)
- Verify contrast (text on all backgrounds)
- Check all video scrims visually

### Stage 4: Optional Review (MiniMax M3)
- Send PDF to 3-agent panel if you want 2nd opinion
- Cost: ~$0.25/session, provides detailed feedback

---

## Asset Sourcing Decision Tree

1. **Free stock images (Pexels)?** → Use first
2. **Metaphorically specific concept?** → Gemini Omni only
3. **No suitable free option + bespoke needed?** → $1 per 10-second Gemini Omni clip
4. **Catalog all sourced assets** with location + metadata

**B-roll libraries verified on disk:**
- `VIDEO-PRODUCTION-MASTER/assets/broll/ai-tech/` (24 verified Pexels)
- `VIDEO-PRODUCTION-MASTER/assets/broll/stock-photos-people/` (4 verified Pexels)
- `VIDEO-PRODUCTION-MASTER/assets/broll/gemini-generated/` (2 Gemini Omni clips)

---

## The Key Insight

**Time is spent discovering the rubric, not applying it.**

The V1→V5 rebuild was 5–7 hours of climbing from 2.3→A. If this rubric had been the build spec from the start, the deck would have shipped A on first render.

**Next deck:** Read this protocol → Apply the 10-point checklist before writing ANY code → Render once → Done.

---

## Files to Reference

- **Master Protocol:** `/Users/scottmagnacca/Documents/Claude/Projects/Novartis-Emeritus-Sales-Project/assets/MODULE3_BEST_PRACTICES/FIRST_RENDER_A_QUALITY_PROTOCOL.md`
- **Toolkit API:** `/Users/scottmagnacca/Documents/Claude/Projects/Novartis-Emeritus-Sales-Project/assets/MODULE3_BEST_PRACTICES/1_PPTX_TOOLKIT_REFERENCE.md`
- **Build Script:** `/Users/scottmagnacca/Documents/Claude/Projects/Novartis-Emeritus-Sales-Project/module3/build_v5/build_v5.py`
- **Theme Palette:** `/Users/scottmagnacca/Documents/Claude/Projects/Novartis-Emeritus-Sales-Project/module3/build_v5/theme.py`

---

**Ready to generate A-quality decks on first render. Zero iteration needed.**
