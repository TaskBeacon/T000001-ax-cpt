# Task Plot Brief

## Evidence Sources

- `README.md`
- `main.py`
- `config/config.yaml`
- `src/run_trial.py`

## Header

- Title: AX-CPT Task
- Construct: cognitive control / context maintenance

## Participant-Visible Flow

- Four randomized condition types are used: AX, AY, BX, BY.
- AX is the target condition; AY, BX, and BY are non-target conditions.
- Correct response is `f` for AX and `j` for AY, BX, and BY.
- Every trial shows fixation, cue, delay fixation, probe response, feedback, and ITI.
- Feedback is one of `Correct`, `Incorrect`, or `No response`.

## Rows

- AX target: cue `A`, probe `X`, press `f`, 40% weight.
- AY non-target: cue `A`, probe `Y`, press `j`, 10% weight.
- BX non-target: cue `B`, probe `X`, press `j`, 10% weight.
- BY non-target: cue `B`, probe `Y`, press `j`, 40% weight.

## Timings

- Fixation: 500 ms.
- Cue: 500 ms.
- Delay/ISI: 500 ms.
- Probe response window: up to 1000 ms.
- Feedback: 500 ms.
- ITI: 800-1200 ms.

## Rendering Notes

- The generated raw image must contain only timeline content below a blank header band.
- The final title, `Construct: cognitive control / context maintenance` subtitle, and TaskBeacon logo are added by post-processing.
