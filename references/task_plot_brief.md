# Task Plot Brief

Task: AX-CPT Task

Goal measured: cognitive control and context maintenance.

Primary evidence:
- `README.md`: task overview, methods, timing, condition weights.
- `config/config.yaml`: condition list, response keys, timing, visible text stimuli.
- `src/run_trial.py`: participant-visible trial sequence and response scoring.

Conditions:
- AX: cue `A`, probe `X`, target trial, correct key `f`, weight 40%.
- AY: cue `A`, probe `Y`, non-target trial, correct key `j`, weight 10%.
- BX: cue `B`, probe `X`, non-target trial, correct key `j`, weight 10%.
- BY: cue `B`, probe `Y`, non-target trial, correct key `j`, weight 40%.

Trial phases:
- Fixation: `+`, 500 ms, no response.
- Cue: `A` or `B`, 500 ms. Runtime context allows keys, but scoring is at probe.
- ISI: `+`, 500 ms.
- Probe response: `X` or `Y`, up to 1000 ms, response keys `f` and `j`, terminates on response.
- Feedback: `Correct`, `Incorrect`, or `No response`, 500 ms.
- ITI: blank screen, random 800-1200 ms.

Participant-visible response rule:
- Press `f` only for AX.
- Press `j` for AY, BX, and BY.

Block context:
- 4 blocks, 40 trials per block, 160 trials total.
- Trial types are weighted randomized within blocks.

Image simplification:
- Use four timeline rows: AX, AY, BX, BY.
- Keep the same six phase snapshots in each row.
- Use short English feedback labels to avoid encoding artifacts from the source files.
