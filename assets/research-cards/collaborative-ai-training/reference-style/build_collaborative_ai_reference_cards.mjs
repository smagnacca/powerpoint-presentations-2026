import fs from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";
import { Presentation, PresentationFile } from "@oai/artifact-tool";

const ROOT = path.resolve(new URL(".", import.meta.url).pathname);
const SKILL_DIR = "/Users/scottmagnacca/.codex/plugins/cache/openai-primary-runtime/presentations/26.909.11814/skills/presentations";
const TMP_DIR = path.join(ROOT, ".build");
const OUT_DIR = ROOT;
const FINAL_CANDIDATE = path.join(TMP_DIR, "collaborative-ai-training-reference-style-draft.pptx");

await fs.mkdir(TMP_DIR, { recursive: true });
const serif = "Georgia";
const sans = "Arial";

const C = {
  paper: "#FAF9F6",
  ink: "#161A22",
  muted: "#687386",
  rule: "#242934",
  blue: "#007AFF",
  blueDark: "#0B3D78",
  gold: "#F5A623",
  white: "#FFFFFF",
};

const W = 960;
const H = 890;
const p = Presentation.create({ slideSize: { width: W, height: H } });

function shape(slide, geometry, left, top, width, height, fill, line = "none", radius = null) {
  const s = slide.shapes.add({
    geometry,
    position: { left, top, width, height },
    fill,
    line: line === "none" ? { fill: "none", width: 0 } : { style: "solid", fill: line, width: 1 },
  });
  if (radius) s.borderRadius = radius;
  return s;
}

function text(slide, value, left, top, width, height, style = {}) {
  const s = slide.shapes.add({
    geometry: "textbox",
    position: { left, top, width, height },
    fill: "none",
    line: { fill: "none", width: 0 },
  });
  s.text = value;
  s.text.style = {
    typeface: style.typeface ?? sans,
    fontSize: style.fontSize ?? 18,
    bold: style.bold ?? false,
    italic: style.italic ?? false,
    color: style.color ?? C.ink,
    align: style.align ?? "left",
    verticalAlign: style.verticalAlign ?? "top",
    autoFit: "none",
    breakLine: false,
  };
  return s;
}

function rule(slide, left, top, width, color = C.rule, height = 1) {
  return shape(slide, "rect", left, top, width, height, color);
}

function statPanel(slide, left, top, stat, label, note) {
  shape(slide, "roundRect", left, top, 158, 174, `linear(135deg, ${C.blue} 0%, ${C.blueDark} 100%)`, "none", 12);
  text(slide, stat, left + 18, top + 34, 122, 58, { typeface: sans, fontSize: 51, bold: true, color: C.white, align: "center" });
  text(slide, label, left + 8, top + 92, 142, 40, { typeface: sans, fontSize: 18, bold: true, color: C.gold, align: "center" });
  if (note) text(slide, note, left + 8, top + 142, 142, 22, { typeface: sans, fontSize: 13.5, color: C.white, align: "center" });
}

function bullet(slide, top, heading, body) {
  shape(slide, "ellipse", 66, top + 8, 12, 12, C.gold);
  text(slide, heading, 88, top, 175, 30, { typeface: sans, fontSize: 22.5, bold: true, color: C.ink });
  text(slide, body, 280, top, 614, 70, { typeface: sans, fontSize: 21, color: C.ink });
  rule(slide, 66, top + 70, 828, "#D9DDE3", 1);
}

function addHeader(slide, section, title, subtitle, stat, statLabel, statNote) {
  slide.background.fill = C.paper;
  text(slide, "RESEARCH CARD", 66, 58, 180, 22, { typeface: sans, fontSize: 13, bold: true, color: C.blue });
  text(slide, section.toUpperCase(), 650, 58, 244, 22, { typeface: sans, fontSize: 11, color: C.muted, align: "right" });
  rule(slide, 66, 84, 828, C.rule, 1);
  statPanel(slide, 66, 112, stat, statLabel, statNote);
  text(slide, title, 248, 116, 632, 80, { typeface: serif, fontSize: 29, bold: true, color: C.ink });
  text(slide, subtitle, 248, 214, 620, 56, { typeface: serif, fontSize: 18, italic: true, color: C.muted });
}

function addCitations(slide, lines) {
  rule(slide, 66, 750, 828, "#D2D5DB", 1);
  text(slide, "APA CITATIONS", 66, 772, 170, 20, { typeface: sans, fontSize: 12, bold: true, color: C.muted });
  text(slide, lines, 66, 804, 828, 66, { typeface: serif, fontSize: 11, color: C.muted });
}

const s1 = p.slides.add();
addHeader(
  s1,
  "Employee perspective",
  "Collaborative AI helps employees work faster and learn while they work",
  "When people learn to direct, question, and apply AI output, the gains can improve both speed and quality.",
  "40%",
  "LESS TIME",
  "18% BETTER",
);
text(s1, "In a preregistered experiment, 453 college-educated professionals completed incentivized writing tasks with or without ChatGPT. AI-assisted participants took 40% less time, while independent raters scored their work 18% higher in quality.", 66, 302, 828, 84, { typeface: serif, fontSize: 20, color: C.ink });
bullet(s1, 424, "The result", "AI cut task time and improved assessed quality in the experiment.");
bullet(s1, 496, "The boundary", "The evidence covers writing tasks, not every job or workflow.");
bullet(s1, 568, "Employee role", "Employees still frame, inspect, and own the decision.");
text(s1, "The employee takeaway", 66, 664, 240, 22, { typeface: sans, fontSize: 12, bold: true, color: C.blue });
text(s1, "Training helps employees use AI for speed and quality without giving up review, judgment, or accountability.", 66, 692, 828, 34, { typeface: serif, fontSize: 17, bold: true, color: C.ink });
addCitations(s1, "Noy, S., & Zhang, W. (2023). Experimental evidence on the productivity effects of generative artificial intelligence. Science, 381(6654), 187–192. https://doi.org/10.1126/science.adh2586");
s1.speakerNotes.textFrame.setText("Source audit: The Science record reports a preregistered online experiment with 453 college-educated professionals. Average time decreased by 40% and output quality rose by 18%. The card preserves the study's task-level scope and does not generalize the result to all work.");

const s2 = p.slides.add();
addHeader(
  s2,
  "Manager + business",
  "Managers turn employee-level gains into team performance and business value",
  "Managers decide whether those gains stay isolated or become repeatable team capability.",
  "14%",
  "MORE / HOUR",
  "34% NOVICE",
);
text(s2, "In a field study of 5,179 customer-support agents, access to an AI conversational assistant increased issues resolved per hour by 14% on average and by 34% for novice and low-skilled workers. The authors found suggestive evidence that the system spread practices from more experienced workers.", 66, 302, 828, 92, { typeface: serif, fontSize: 20, color: C.ink });
bullet(s2, 424, "Productivity", "The average gain improved issues resolved per hour.");
bullet(s2, 496, "Performance", "Novice workers showed the largest gain, suggesting faster learning of effective patterns.");
bullet(s2, 568, "Business value", "McKinsey respondents reported cost and revenue gains in gen AI business units. This is self-reported, not causal evidence.");
text(s2, "The employer takeaway", 66, 664, 240, 22, { typeface: sans, fontSize: 12, bold: true, color: C.blue });
text(s2, "Proper training is the bridge from individual task help to repeatable productivity, stronger performance, and reported business value.", 66, 692, 828, 34, { typeface: serif, fontSize: 17, bold: true, color: C.ink });
addCitations(s2, "Brynjolfsson, E., Li, D., & Raymond, L. R. (2023). Generative AI at work. NBER Working Paper No. 31161. https://doi.org/10.3386/w31161\nSingla, A., Sukharevsky, A., Yee, L., & Chui, M. (2024). The state of AI in early 2024. McKinsey & Company. https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2024");
s2.speakerNotes.textFrame.setText("Source audit: NBER reports 5,179 customer-support agents, a 14% average productivity increase, and a 34% increase for novice and low-skilled workers on the current public summary. McKinsey's 2024 survey reports respondents seeing cost decreases and revenue increases in business units deploying gen AI. The card labels the McKinsey evidence as self-reported and avoids causal language.");

const candidate = await PresentationFile.exportPptx(p);
await candidate.save(FINAL_CANDIDATE);
for (let i = 0; i < p.slides.items.length; i += 1) {
  const png = await p.slides.items[i].export({ format: "png", scale: 2 });
  await fs.writeFile(path.join(TMP_DIR, `card-${i + 1}.png`), new Uint8Array(await png.arrayBuffer()));
}
console.log(FINAL_CANDIDATE);
