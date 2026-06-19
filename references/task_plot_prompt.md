Use case: infographic-diagram
Asset type: TaskBeacon task flow diagram
Primary request: Create a clean, publication-ready task flow diagram as a timeline collection for the behavioral task described below.

Task: AX-CPT Task
Construct: cognitive control / context maintenance
Rows/conditions:
- AX target: cue A then probe X; correct key f; weighted 40%
- AY non-target: cue A then probe Y; correct key j; weighted 10%
- BX non-target: cue B then probe X; correct key j; weighted 10%
- BY non-target: cue B then probe Y; correct key j; weighted 40%

Timeline phases:
- AX target: Fixation (+; 500 ms; no response) -> Cue A (A; 500 ms) -> ISI (+; 500 ms) -> Probe X (X; up to 1000 ms; press f) -> Feedback (Correct / Incorrect / No response; 500 ms) -> ITI (blank; 800-1200 ms)
- AY non-target: Fixation (+; 500 ms; no response) -> Cue A (A; 500 ms) -> ISI (+; 500 ms) -> Probe Y (Y; up to 1000 ms; press j) -> Feedback (Correct / Incorrect / No response; 500 ms) -> ITI (blank; 800-1200 ms)
- BX non-target: Fixation (+; 500 ms; no response) -> Cue B (B; 500 ms) -> ISI (+; 500 ms) -> Probe X (X; up to 1000 ms; press j) -> Feedback (Correct / Incorrect / No response; 500 ms) -> ITI (blank; 800-1200 ms)
- BY non-target: Fixation (+; 500 ms; no response) -> Cue B (B; 500 ms) -> ISI (+; 500 ms) -> Probe Y (Y; up to 1000 ms; press j) -> Feedback (Correct / Incorrect / No response; 500 ms) -> ITI (blank; 800-1200 ms)

Visual requirements:
- White background, landscape orientation, crisp dark text, restrained condition accent colors.
- One horizontal row per condition or representative trial type.
- Each row contains exactly 6 participant-screen snapshots connected by a subtle arrow.
- Each screen snapshot shows the visible stimulus or feedback, not internal variable names.
- Use gray participant-screen boxes, thin black arrows, consistent row spacing, and subtle row separators.
- Place timing labels under each screen in compact text.
- Place condition labels at the left of each row.
- Use short labels only; avoid paragraphs inside the image.
- Make all text legible at normal document preview size.
- Leave a clean blank header band across the top 15-18% of the image. This band is reserved for a fixed title, `Construct: ...` subtitle, and TaskBeacon logo lockup that will be added after generation.

Accuracy constraints:
- Do not invent phases, stimuli, condition names, keys, rewards, or timings.
- Do not add people, lab equipment, decorative scenes, logos, or unrelated icons.
- Do not draw the task title, construct subtitle, any logo, watermark, brand mark, or `TaskBeacon` text inside the generated image.
- Draw only the timeline content below the blank header band.
- If a detail is unknown, omit it rather than guessing.
- Preserve these exact terms where used: AX, AY, BX, BY, A, B, X, Y, f, j, 500 ms, 1000 ms, 800-1200 ms, Correct, Incorrect, No response, ITI.
- Show `f` only for AX target and `j` for AY, BX, and BY.

Style:
TaskBeacon scientific infographic style: clean vector-like raster image, organized spacing, gray screen boxes, restrained color accents, and a blank header-safe area.
