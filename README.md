# PowerPoint Presentations 2026 — First-Render A-Quality Framework

Generate A-quality PowerPoint presentations on the first render. No iteration cycle. No debug hours.

## Quick Links

- **Full Protocol:** `assets/best-practices/FIRST_RENDER_A_QUALITY_PROTOCOL.md`
- **One-Page Summary:** `assets/best-practices/HERMES_SUMMARY_KEY_LEARNINGS.md`
- **Toolkit API:** `assets/best-practices/1_PPTX_TOOLKIT_REFERENCE.md`
- **Reference Deck:** `assets/Novartis_Module3_Part2_Version5_2026-07-11.pptx`

## The System

### Build Protocol (4 stages, ~2 hours end-to-end)

1. **Pre-Flight** — force-materialize assets, lock prior version, verify sources
2. **Build-Time Checklist** — 10-point rubric applied during authoring
3. **Post-Build QA** — render to PDF, 3-lens review (salesperson/UX/designer)
4. **Optional Review** — MiniMax M3 panel for 2nd opinion (~$0.25)

### The 10 Failure Guardrails

| # | Pattern | Guard |
|---|---------|-------|
| 1 | Dead bottom zone | Fill bottom with content/media/gradient |
| 2 | Visible placeholder | Pre-source ALL images before render |
| 3 | Off-palette color | Use only: WHITE, INK, SUBTLE, MUTED, BLUE, EMERALD, AMBER, ROSE, VIOLET |
| 4 | Repeated template | Vary archetype per slide |
| 5 | Flat card | Every card: gradient OR icon badge OR accent bar |
| 6 | No focal anchor | ≥1 human photo OR visual metaphor per slide |
| 7 | Under-scrimmed video | Scrim: 11–14% (light) or 22–58% (dark) |
| 8 | Dense text | ≤3 chunks per card, use dividers/badges |
| 9 | Generic photo | Match image metaphorically to slide concept |
| 10 | Orphaned text | Anchor headlines to ≥1 visual element |

### The A-Grade Rubric (Must Pass All 3)

- **Busy Salesperson (3-sec skim):** Key insight visible in 3 seconds? Focal point? Finished look?
- **UX Expert (hierarchy):** Info chunked into ≤3 units? Clear hierarchy? ≥1.5x text contrast?
- **Graphic Designer (polish):** Aligned shapes? Hero element? On-palette colors?

## For the Next Presentation

```bash
cd ~/Documents/Claude/Projects/powerpoint-presentations-2026/
# Read the full protocol
cat assets/best-practices/FIRST_RENDER_A_QUALITY_PROTOCOL.md

# For a new deck, copy the toolkit from Novartis project:
# cp ~/Documents/Claude/Projects/Novartis-Emeritus-Sales-Project/module3/build_v5/{theme.py,compose_clip.py,build_v5.py} ./[your-deck-name]/

# Apply the 10-point checklist before coding
# Render once. Done.
```

## Reference

**Novartis Module 3 Part 2 V5** — A-grade example
- 33 slides, 3-agent verified
- Full video enhancement with proper scrim values
- Reusable archetypes: jensen_slide, research_slide, engagement_slide, persona_slide
- Circle-photo technique with colored rings
- Gradient cards and icon badges throughout

## The Insight

The V1→V5 rebuild (5–7 hours) taught us that the rubric for "A-quality" is fully knowable *before* rendering. Apply it as a build-time checklist, not a post-hoc quality gate. This makes the first render A-grade automatically.

---

**Status:** Framework complete and tested. Ready for next presentation.  
**Created:** July 12, 2026
