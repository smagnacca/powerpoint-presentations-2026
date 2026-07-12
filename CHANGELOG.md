# Changelog — PowerPoint Presentations 2026

## [1.0] — 2026-07-12

### Created
- New project: PowerPoint Presentations 2026
- Framework extracted from Novartis Module 3 Part 2 rebuild (V1→V5)
- **FIRST_RENDER_A_QUALITY_PROTOCOL.md** — complete 4-stage build system with 10-point checklist, 11 guardrails, 3-lens rubric
- **HERMES_SUMMARY_KEY_LEARNINGS.md** — 1-page shareable reference
- **1_PPTX_TOOLKIT_REFERENCE.md** — python-pptx API documentation (palette, helpers, circle-photo XML technique, scrim values)
- Reference deck: Novartis_Module3_Part2_Version5_2026-07-11.pptx (33 slides, A-grade, video-enhanced)
- CLAUDE.md — project overview and quick-start guide
- README.md — framework summary and guardrail table
- CHANGELOG.md — this file

### Key Learnings
- V1→V5 rebuild (5–7 hours) revealed that the A-quality rubric is fully knowable before rendering
- Applying the rubric as a build-time checklist (not post-hoc quality gate) makes the first render A-grade automatically
- Time savings: from 5–7 hour debug cycle to 0 iteration needed
- 10 failure patterns identified and guardrailed with bash/checklist procedures
- 3-lens rubric (salesperson/UX/designer) provides deterministic quality assessment

### Design Principles
1. **Checklist-driven authoring** — apply the 10-point rubric before writing ANY code
2. **Reusable toolkit** — python-pptx helpers (palette, circle-photo, gradient cards, scrim values)
3. **Deterministic quality** — follow the protocol → first render is A-grade → zero iteration
4. **Asset sourcing hierarchy** — free stock first, paid (Gemini Omni) only for bespoke
5. **Per-slide layering** — background → shape/gradient → media+scrim → content → citations

### Files Included
- `assets/Novartis_Module3_Part2_Version5_2026-07-11.pptx` — 33-slide A-grade reference deck
- `assets/best-practices/FIRST_RENDER_A_QUALITY_PROTOCOL.md` — full system (183 lines, 4 stages)
- `assets/best-practices/HERMES_SUMMARY_KEY_LEARNINGS.md` — shareable 1-page reference
- `assets/best-practices/1_PPTX_TOOLKIT_REFERENCE.md` — python-pptx API (palette, helpers, scrim values)

### Next Steps
1. For new presentations: read FIRST_RENDER_A_QUALITY_PROTOCOL.md
2. Copy theme.py + compose_clip.py + build_v5.py from Novartis project
3. Apply the 10-point checklist before coding
4. Render once to PDF locally
5. Done — no iteration needed

---

**Framework Version:** 1.0  
**Status:** Active — ready for new presentations  
**Created:** July 12, 2026  
**Last Updated:** July 12, 2026
