# Task Plot Review

Review checklist source: `E:/Taskbeacon/skills/task-plot/references/review_checklist.md`.

## Evidence Match

- Pass: task name matches `AX-CPT Task`.
- Pass: rows match AX, AY, BX, and BY conditions.
- Pass: phase order matches `src/run_trial.py`: fixation, cue, ISI, probe, feedback, ITI.
- Pass: timing labels match config: 500 ms fixation/cue/ISI/feedback, up to 1000 ms probe, 800-1200 ms ITI.
- Pass: response mapping is correct: `f` only for AX target; `j` for AY, BX, and BY.

## Visual Quality

- Pass: fixed title and `Construct: cognitive control / context maintenance` subtitle are centered in the header.
- Pass: fixed TaskBeacon logo lockup is borderless in the top-right corner and does not overlap content.
- Pass: text is readable and no generated extra title, subtitle, logo, watermark, people, or devices are present.
- Pass: `references/task_plot_timeline_raw.png` preserves the generated timeline before header/logo post-processing.

## README Embed

- Pass: `README.md` contains `## 2. Task Flow`.
- Pass: the first image under `## 2. Task Flow` is exactly `![Task Flow](task_flow.png)`.
- Pass: final image is saved at the task root as `task_flow.png`.
