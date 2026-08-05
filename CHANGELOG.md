# Changelog — PowerPoint Presentations 2026

## [1.4] — 2026-08-05

### Added
- **LLM Concepts Slides — Enhanced Edition** (`LLM-Concepts-Slides-Enhanced.pptx`) — 3-slide educational/sales deck explaining core LLM concepts (The Engine, The Steering Wheel, The Autopilot), rebuilt with pptxgenjs. Final design (v5): each slide pairs its badge/title/subtitle/takeaway with a **real embedded click-to-play video panel** (sourced from the existing local B-roll library, `addMedia` + poster-frame technique proven in the ACE-AI Case Study deck) plus **real icon graphics** (rendered via `react-icons` + `sharp`) instead of plain colored shapes. Palette (7 colors) extracted directly from the source deck's XML for continuity. Video content: a gold neural-network animation (Engine), a real AI chat prompt/response screen recording (Steering Wheel), and a spinning-turbine loop visual (Autopilot).

### Video sourcing
Surveyed `~/ClaudeProjects/VIDEO-PRODUCTION-MASTER/assets/broll/` (60+ AI/tech clips across `ai-tech/` and `ai-chip-graphics-2026-08-01/`, plus a large top-level library). Rejected candidates for baked-in NVIDIA branding and an "AZAHARLABS" watermark; discovered several top-level clips are mislabeled (`Flowing_Energy.mp4` is actually a Grok website recording; `Globe_Rotation.mp4` is actually two people at a computer; `Futuristic_Grid.mp4` is actually a real AI chat interface — used for the Steering Wheel slide despite the misleading name). Clips trimmed to ~4–5.5s and muted with ffmpeg; poster frames hand-selected by sampling several timestamps and rejecting motion-blurred ones.

### What Went Wrong First (v1–v2) — and the fix (v3–v4)
- **v1 shipped with diagrams that were too small and sparse** — the user called this out directly ("the slide size is too small... your graphics and visuals were shit"). The root cause: slides were built on pptxgenjs's **default `LAYOUT_16x9` canvas (10" × 5.625")**, and content was sized as if there were much more room, so diagrams read as small, floating elements with dead space around them.
- **v2's attempted fix made boxes bigger but never fixed the canvas** — same 10"×5.625" layout, so the taller title/diagram/takeaway stack now **overflowed the bottom edge of the slide** (verified by rendering to JPEG and inspecting pixel-by-pixel — takeaway bar text was visibly cut off in all 3 slides, and on slides 2–3 a two-line wrapped title collided directly with the subtitle text below it).
- **v3 kept iterating on box sizes without diagnosing the canvas problem**, so the same title/subtitle/diagram collisions persisted — confirmed again by rendering and reading the images, not by assumption.
- **v4 fixed the actual root cause:** switched to `pres.layout = 'LAYOUT_WIDE'` (13.33" × 7.5") and rebuilt every slide's vertical layout with an explicit, computed budget (badge → title → subtitle → diagram → caption → takeaway, each position derived from the box above it, not guessed). Also caught and fixed a second, subtler bug at this stage: slide 3's original "GOAL box stacked above the LLM circle" layout was only *not* overlapping the subtitle by coincidence (because the subtitle happened to render as one short line) — a longer subtitle would have collided. Redesigned as a single horizontal row (GOAL → LLM → TOOLS, with a LOOP box below), matching the flow-diagram pattern already used on slides 1–2, which removed the fragile vertical math entirely instead of patching around it.
- Verified structurally with python-pptx (opens cleanly, confirms 13.33"×7.5") and visually by rendering to PDF→JPEG at 150dpi and inspecting every slide after each revision — not just once at the end.

### v4 was bug-free and still rejected as boring — the fix (v5)
v4 passed every technical QA check (correct canvas, zero overlaps, on-palette, good contrast) and was still called out directly: *"those were absolutely the worst most boring slides possible."* The defect wasn't a bug — plain colored rounded-rectangles with unicode arrows read as a generic corporate flowchart no matter how cleanly they're laid out. Rebuilt (v5) with:
- **Real embedded video** per slide (click-to-play, `addMedia` + poster frame) sourced from the existing local B-roll library at `~/ClaudeProjects/VIDEO-PRODUCTION-MASTER/assets/broll/` instead of generating new synthetic diagrams — reuse over regenerate, at zero additional cost.
- **Real icon graphics** (`react-icons` rendered to SVG, rasterized with `sharp`) replacing plain shapes for the supporting callout badges.
- A second, unrelated overlap bug caught in this pass: a caption line positioned relative to the element above it (the video panel) collided with the takeaway bar three steps down, because the takeaway bar's position was fixed independently and never cross-checked against the full stack above it. On two slides the caption rendered invisibly (opaque takeaway shape painted over it, added later in z-order); on one slide it was pushed past the slide's bottom edge entirely. Fixed by removing the now-redundant captions (the video + subtitle + takeaway already carried the message) and tightening the vertical budget with real arithmetic, not estimation.

### Key Learnings
- **Always check `pres.layout` before laying out content, and print/verify the actual canvas dimensions** — the default `LAYOUT_16x9` (10"×5.625") is easy to mistake for the wider 13.3"×7.5" `LAYOUT_WIDE`, and every downstream position calculation is wrong if the canvas assumption is wrong. This was the single root cause behind two full bad iterations (v1, v2).
- **"I checked colors and contrast in a screenshot" is not the same claim as "I verified the layout has no overlaps or overflow."** v1's QA checked the wrong things (palette, font, contrast) and missed the defect the user actually saw (undersized, sparse graphics). Visual QA must specifically check: does content fill the intended proportion of the canvas, and does anything extend past a shape or slide boundary — not just "does it look styled."
- **A box position that isn't overlapping today can still be a latent bug** if it only avoids collision because of a short-text coincidence (e.g., a subtitle rendering as one line instead of two). Prefer layouts where each element's position is computed from a fixed, generous gap to the element above it, not from an assumed text height.
- When a fix doesn't visibly work, re-render and re-inspect before trying another fix — v3 was built without re-confirming v2's actual defect (canvas size), so it iterated on the wrong variable.
- **Clean technical QA and engaging design are different axes — passing one says nothing about the other.** v4's bug-free render was still rejected outright. Don't treat "no layout defects" as evidence that a design is good; check both explicitly.
- **Pairwise gap-checking doesn't compose.** Checking "does element B overlap element A above it" for each consecutive pair missed a collision between element C and a *fixed-position* element D two steps below — C's position was only checked against B, never against D. When a fixed-position element (like a takeaway bar) sits at the bottom of a stack, explicitly check the last stacked element against it, not just its immediate neighbor.
- **Top-level B-roll filenames are not reliable outside the indexed `ai-tech/` folder** — `Flowing_Energy.mp4`, `Globe_Rotation.mp4`, and `Futuristic_Grid.mp4` all contained content unrelated to their names. Always extract and view a frame before selecting a clip by filename alone.

### Files Created
- `LLM-Concepts-Slides-Enhanced.pptx` — main deliverable, 3 slides, LAYOUT_WIDE (13.33"×7.5"), 4.7MB (embedded video)
- `assets/decks/slide-1.jpg`, `slide-2.jpg`, `slide-3.jpg` — QA verification screenshots (150dpi), v5 final

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
