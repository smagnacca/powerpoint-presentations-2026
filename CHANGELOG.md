# Changelog — PowerPoint Presentations 2026

## [1.4] — 2026-08-05

### Added
- **LLM Concepts Slides — Enhanced Edition** (`LLM-Concepts-Slides-Enhanced.pptx`) — 3-slide educational/sales deck explaining core LLM concepts (The Engine, The Steering Wheel, The Autopilot) rebuilt with pptxgenjs using the A-quality framework. Each slide features:
  - **Concept 1 (THE ENGINE):** Token-by-token prediction visualization with attention layers diagram
  - **Concept 2 (THE STEERING WHEEL):** Prompt→LLM→Output flow showing cause-effect of instructions
  - **Concept 3 (THE AUTOPILOT):** Agent loop diagram (LLM + Goal + Tools + Loop) with "repeats until done" concept
- **Hybrid visual design:** Kinetic typography badges, flow diagrams with gold directional elements, structured content boxes with shadows, and takeaway bars. All using the extracted color palette (dark forest green, teal accents, warm gold, cream/white).
- **QA verification:** All 3 slides converted to JPEG (150dpi) and passed visual QA on contrast, hierarchy, readability, and color consistency.

### Process Notes
- Completed task intake (2c protocol) with 5 scoping questions → routing plan → approval gate
- Routing: Local-first approach (Bash analysis, Ollama reasoning, pptxgenjs slide builders)
- Attempted ffmpeg/Playwright animation pipeline for video overlays; pivoted to simpler pptxgenjs-native approach when tool dependencies unavailable
- Framework ensures first-render A-quality without iteration (no post-hoc refinement needed)
- Asset sourcing: Reused existing color palette from source .pptx; generated diagrams natively in pptxgenjs

### Key Learnings
- pptxgenjs with simple geometric diagrams (boxes, circles, text, arrows) is faster and more reliable than trying to compose frame sequences with external tools (Playwright, ffmpeg filters) when dependencies aren't pre-installed
- Three-box "flow" diagram (Prompt → LLM → Output) is the clearest way to show steering-wheel metaphor; reinforced with explicit text: "Different Prompt = Different Output"
- Loop diagram (center LLM with 3 surrounding boxes: Goal, Tools, Loop) clarifies agent concept better than sequential arrows; adds ↻ symbol to reinforce cycling
- Extracted palette consistency check (all 3 slides share 7 colors) ensures visual cohesion without custom theming

### Files Created
- `LLM-Concepts-Slides-Enhanced.pptx` — main deliverable, 3 slides
- `assets/decks/slide-1.jpg`, `slide-2.jpg`, `slide-3.jpg` — QA verification screenshots (150dpi)

---

## [1.3] — 2026-08-04

### Added
- **New deck: "ACE-AI Case Study"** (`ACE-Score-Full-Deck.pptx` / saved as `assets/decks/ACE-AI-Case-Study.pptx` + `.pdf`) — 6-slide deck on the AI-Cirrhosis-ECG (ACE) score study (Ma et al.), built with pptxgenjs rather than python-pptx. Structure: (1) medical/cost burden, (2) why early detection matters, (3) ACE score intro with AUC explainer answering "so what?", (4) validation evidence across 890 patients, (5) crisis-vs-prevention cost impact, (6) AI+clinical-judgment synthesis with full APA reference list.
- **Video-embedded animated charts** — new capability for this framework. Built a small Playwright + ffmpeg pipeline (`anim-build/templates.js`, `anim-build/record.js`) that renders HTML/CSS/JS count-up numbers, growing bar charts, and SVG line-draw (ROC curve) animations, records them via `context.recordVideo`, and encodes to h264 mp4 for embedding as click-to-play video via pptxgenjs `addMedia`. Real vs. estimated data visually distinguished with a diagonal hatch pattern + dashed border + gold "ILLUSTRATIVE"/"EST." badge, not text alone.
- **Real Pexels photography** used for hero background and 3 closing "pillar" photos (quality of life, longevity, cost savings) instead of icons/clip art, each color-graded to match the deck palette — extracted a 4K frame from an existing licensed B-roll clip (`ai-16-plexus-abstract-geometric-lines.mp4`) for the hero.
- **Distributed to 3 other project folders** for reuse as a case-study reference: Novartis-Emeritus-Sales-Project, VIDEO-PRODUCTION-MASTER, Babson Summer Course (each under `assets/ACE-AI-Case-Study/`).

### Key Learnings
- Playwright's `recordVideo` flattens CSS `background: transparent` to opaque **white** in the output video, not true alpha — any HTML animation template destined for video recording needs an explicit opaque background color, or light text/elements meant for a dark card become invisible.
- pptxgenjs `addMedia`'s `cover` (poster image) option requires a base64 data URI, not a file path — extracting a real near-final animation frame via ffmpeg and passing it as `cover` looks far better than the library's default gray play-button box.
- Hand-authoring OOXML `<p:timing>` for embedded-video autoplay/loop was investigated and deliberately rejected for this deck: real corruption risk from hand-authored XML, and no way to verify actual playback behavior without real PowerPoint (LibreOffice can't render video timing). Shipped standard click-to-play instead — a communicated trade-off, not an oversight.
- Two rounds of independent red-team subagent review (fresh context, no build knowledge) caught real defects a self-review missed: two unsourced "problem" stats that had crept in as generic framing text, inconsistent red/green color semantics across slides, and illustrative-vs-real data that wasn't visually distinct enough at a skim. All fixed before delivery.

---

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
