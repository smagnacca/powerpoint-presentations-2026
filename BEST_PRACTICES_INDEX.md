# Best Practices Index — PowerPoint Presentations 2026

**Last Updated:** July 18, 2026

This file serves as a master index and quick-reference for all best practices, protocols, and supporting documents.

**2026-07-18 addition:** Click-to-advance animations are now a standing part of the build checklist (#11) and QA stage (Stage 3.4) — include on process/step/sequence slides where they aid comprehension, and test with the mandatory two-tier protocol (structural validation + runtime verification in PowerPoint/Keynote/Google Slides). See `1_PPTX_TOOLKIT_REFERENCE.md` § Click-to-Advance Animations for the reusable `add_click_fade()` helper, sourced from the Novartis Module 3 "Human in the Loop" slide build.

---

## 🎯 START HERE

**Read in this order for first-time setup:**

1. [README.md](README.md) — 2-minute overview
2. [HERMES_SUMMARY_KEY_LEARNINGS.md](assets/best-practices/HERMES_SUMMARY_KEY_LEARNINGS.md) — 5-minute essentials
3. [FIRST_RENDER_A_QUALITY_PROTOCOL.md](assets/best-practices/FIRST_RENDER_A_QUALITY_PROTOCOL.md) — complete system (20 minutes)

---

## 📋 Core Documents

### Full Protocol
**File:** `assets/best-practices/FIRST_RENDER_A_QUALITY_PROTOCOL.md`  
**Purpose:** Complete build system with all stages, checklists, and anti-patterns  
**Length:** ~183 lines  
**Read Time:** 20 min  
**Use When:** Authoring any new presentation deck; reference for edge cases  
**Sections:**
- PRE-FLIGHT bash checklist (force-materialize, verify save-path, lock prior version)
- BUILD-TIME checklist (10-point A-grade rubric)
- POST-BUILD QA procedures (PDF review, 3-lens verification)
- A-GRADE rubric with 3 independent lenses
- 11 ranked anti-patterns with root causes and guardrails
- Asset sourcing decision tree
- 4-stage protocol execution

### One-Page Reference
**File:** `assets/best-practices/HERMES_SUMMARY_KEY_LEARNINGS.md`  
**Purpose:** Shareable summary for team, AI systems, quick lookups  
**Length:** ~1 page  
**Read Time:** 5 min  
**Use When:** Need a quick reference; sharing with Hermes or other systems; onboarding new team member  
**Sections:**
- The 10 failure patterns + guardrails (table format)
- The 3-lens A-grade rubric
- Python-pptx toolkit essentials (palette, helpers, scrim values)
- Build protocol overview (4 stages)
- Asset sourcing decision tree
- Key insight summary

### Toolkit API Reference
**File:** `assets/best-practices/1_PPTX_TOOLKIT_REFERENCE.md`  
**Purpose:** Complete python-pptx API documentation with examples  
**Length:** ~165 lines  
**Read Time:** 10 min  
**Use When:** Implementing slides in code; reference for specific helpers; understanding circle-photo technique  
**Sections:**
- Palette constants (9 colors with hex codes)
- Deck + slide primitives (new_deck, blank_slide)
- Text primitives (add_text, add_rich, add_bullets)
- Layout / heading primitives (add_kicker_title, add_rounded_card, add_citation)
- Finishing devices (add_badge, add_circle_photo, add_gradient_card, add_icon_badge, add_stat_ring, set_transparency)
- Background helpers (add_bg_video with scrim values)
- Scrim value cheat-sheet (11–14% light, 22–58% dark)
- Circle-photo technique with XML prstGeom ellipse masking
- compose_clip.py video compositor (FFmpeg fit-to-fill crop, PIL text overlay, fade)
- Deck-as-a-program pattern (top-to-bottom build_v5.py)
- Per-slide layering order (bottom → top)
- Page-numbering pattern

---

## 📊 Reference Materials

### Reference Deck
**File:** `assets/Novartis_Module3_Part2_Version5_2026-07-11.pptx`  
**Purpose:** A-grade example presentation (33 slides)  
**Use When:** 
- Need to see the protocol in action
- Want to understand slide structure, gradients, video treatment
- Studying slide archetypes (jensen, research, engagement, persona)
- Reference for circle-photo technique with rings

**Key Features:**
- 33 slides at A-grade quality
- 3-agent MiniMax M3 verified
- Video-enhanced backgrounds with proper scrim values
- Circle photos with colored rings
- Gradient cards and icon badges throughout
- Full text hierarchy and contrast verification
- Reusable slide archetypes

---

## 🔗 Related Projects

### Source Project (Reference Only)
**Project:** Novartis-Emeritus-Sales-Project  
**Location:** `~/Documents/Claude/Projects/Novartis-Emeritus-Sales-Project/`  
**Contains:**
- Build scripts: `module3/build_v5/{theme.py, compose_clip.py, build_v5.py}`
- Extended asset libraries: `assets/MODULE3_BEST_PRACTICES/`
- B-roll libraries: `VIDEO-PRODUCTION-MASTER/assets/broll/`

**Use When:** Need to copy build scripts for new presentations

### Video Production Resources
**Project:** VIDEO-PRODUCTION-MASTER  
**Location:** `~/Documents/Claude/Projects/VIDEO-PRODUCTION-MASTER/`  
**Contains:**
- B-roll asset libraries (157 videos, 131 stills)
- Free Pexels clips: `assets/broll/ai-tech/` (24 verified)
- Stock photos: `assets/broll/stock-photos-people/` (4 verified)
- Gemini Omni clips: `assets/broll/gemini-generated/` (2 verified)

---

## 📁 File Organization

```
powerpoint-presentations-2026/
├── README.md                                    ← START: 2-min overview
├── CLAUDE.md                                    ← Project details
├── CHANGELOG.md                                 ← Version history
├── BEST_PRACTICES_INDEX.md                      ← THIS FILE
└── assets/
    ├── Novartis_Module3_Part2_Version5_2026-07-11.pptx  ← Reference deck (33 slides)
    └── best-practices/
        ├── FIRST_RENDER_A_QUALITY_PROTOCOL.md          ← FULL SYSTEM (read 2nd)
        ├── HERMES_SUMMARY_KEY_LEARNINGS.md             ← 1-PAGE SUMMARY (read 1st)
        └── 1_PPTX_TOOLKIT_REFERENCE.md                 ← API DOCS (reference)
```

---

## 🚀 Quick Start for New Presentations

1. **Read the protocol**
   ```bash
   cat assets/best-practices/FIRST_RENDER_A_QUALITY_PROTOCOL.md
   ```

2. **Copy the toolkit** (from Novartis project)
   ```bash
   cp ~/Documents/Claude/Projects/Novartis-Emeritus-Sales-Project/module3/build_v5/{theme.py,compose_clip.py,build_v5.py} ./[your-deck-name]/
   ```

3. **Apply the 10-point checklist** before writing ANY code

4. **Render once to PDF** and QA locally with the 3-lens rubric

5. **Done** — no iteration needed

---

## 💡 Key Insights

**The Problem:** Traditional presentation builds take 5–7 hours to reach A-quality because the rubric is discovered *after* the render.

**The Solution:** The rubric is fully knowable *before* rendering. Apply it as a build-time checklist and the first render is A-grade automatically.

**The Result:** Zero iteration. One render. Done.

---

## 📞 Support

- **For protocol questions:** See FIRST_RENDER_A_QUALITY_PROTOCOL.md (full system details)
- **For API questions:** See 1_PPTX_TOOLKIT_REFERENCE.md (helper functions, examples)
- **For quick reference:** See HERMES_SUMMARY_KEY_LEARNINGS.md (1-page summary)
- **For examples:** Open Novartis_Module3_Part2_Version5_2026-07-11.pptx (33-slide reference)

---

**Last Updated:** July 12, 2026  
**Framework Version:** 1.0  
**Status:** Ready for next presentation
