# Changelog — PowerPoint Presentations 2026

## [1.2] — 2026-07-18

### Added
- **Build-time checklist item #11 + QA Stage 3.4: click-to-advance animations.** Standing rule going forward — process/step/sequence slides (workflow diagrams, decision trees, staged arguments) should include click-to-advance builds where they aid comprehension; static slides stay static.
- **`add_click_fade()` helper** in `1_PPTX_TOOLKIT_REFERENCE.md` — reusable hand-authored OOXML `<p:timing>` pattern (python-pptx has no animation API). Sourced from the Novartis Module 3 "Human in the Loop" slide build (2026-07-18).
- **Mandatory two-tier animation testing protocol:** (1) structural validation (XML well-formedness, zip integrity, bldP/clickEffect/withEffect counts) — free, always do this; (2) runtime verification by actually opening the file in PowerPoint/Keynote/Google Slides and clicking through — required before claiming animations "work." A LibreOffice PDF render (the usual free QA step) flattens slides to their final state and proves nothing about animation behavior.
- **New anti-pattern (12th):** claiming animations work from a static PDF render alone.
- **Documented blocker:** uploading a real `.pptx` for browser-based runtime testing hits two dead ends — Drive/cloud API tools need inline base64 content (blows past context limits; every real pptx carries unavoidable theme/master XML overhead), and OS-native file-picker dialogs are invisible to browser-automation DOM tools. Fastest reliable path: have the user do the one-click upload/open themselves, then resume automated click-through from inside the loaded app.

### Key Learning
- A file can be structurally valid XML and still never be runtime-verified — those are different claims, and the gap matters most for animations because the standard free QA render (LibreOffice → PDF) can't exercise them at all. State explicitly which tier of verification was actually completed.

---

## [1.1] — 2026-07-16

### Added
- **A-Pattern #5: Research-citation card + graphic pull-quote pairing** — added to `FIRST_RENDER_A_QUALITY_PROTOCOL.md`'s "THE 4 A-PATTERNS" section (now 5). Every deck should include 2–3 academic sources, each as a research highlight card (source line, title, authors/year, key-finding callout, stats) paired with a large graphic pull-quote.
- Rule refined mid-session: key-finding callouts and pull-quotes must be written in **clear, plain, behavioral language** (concrete verbs: accept, offload, verify, cross-check, question) instead of academic phrasing — formal citation language stays confined to the small-type source line.
- **Worked example:** `examples/research-slide-demo/` — a single rendered slide demonstrating A-Patterns #1–#5 together (researcher photo w/ ring, scrimmed neural-network-texture card, lightning-bolt metaphor icon, dark kicker/divider bar, citation card + plain-language pull-quote). Includes `build_example.py` (self-contained python-pptx script), the rendered `.pptx`, and a `.png`/`.html` preview.

### Key Learning
- Real research content (Lee et al., CHI 2025, Microsoft Research × CMU — "The Impact of Generative AI on Critical Thinking") only lands with a business audience once translated out of academic phrasing into plain behavioral statements. This is now a standing rule for all research slides going forward, not a one-off edit.

---

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

**Framework Version:** 1.1  
**Status:** Active — ready for new presentations  
**Created:** July 12, 2026  
**Last Updated:** July 16, 2026
