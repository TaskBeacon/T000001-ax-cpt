# Task Plot Audit

- generated_at: 2026-03-09T23:57:47
- mode: existing
- task_path: E:\Taskbeacon\T000001-ax-cpt

## 1. Inputs and provenance

- E:\Taskbeacon\T000001-ax-cpt\README.md
- E:\Taskbeacon\T000001-ax-cpt\config\config.yaml
- E:\Taskbeacon\T000001-ax-cpt\src\run_trial.py

## 2. Evidence extracted from README

- | Step | Description |
- |---|---|
- | 1. Fixation | A central fixation cross `(+)` is displayed. |
- | 2. Cue Presentation | The cue letter (A or B) is presented. |
- | 3. Inter-Stimulus Interval (ISI) Fixation | A central fixation cross `(+)` is displayed for a short duration. |
- | 4. Probe Presentation & Response | The probe letter (X or Y) is presented, and the participant responds. |
- | 4. Feedback | Feedback (`Correct`, `Incorrect`, or `Too Slow`) is displayed. |
- | 5. Inter-Trial Interval (ITI) | A blank screen is shown before the next trial. |

## 3. Evidence extracted from config/source

- AX: phase=context cue, deadline_expr=settings.cue_duration, response_expr=n/a, stim_expr=cue_stim_name
- AX: phase=delay fixation, deadline_expr=settings.isi_duration, response_expr=n/a, stim_expr='fixation'
- AX: phase=probe response, deadline_expr=settings.probe_duration, response_expr=settings.probe_duration, stim_expr=probe_stim_name
- AY: phase=context cue, deadline_expr=settings.cue_duration, response_expr=n/a, stim_expr=cue_stim_name
- AY: phase=delay fixation, deadline_expr=settings.isi_duration, response_expr=n/a, stim_expr='fixation'
- AY: phase=probe response, deadline_expr=settings.probe_duration, response_expr=settings.probe_duration, stim_expr=probe_stim_name
- BX: phase=context cue, deadline_expr=settings.cue_duration, response_expr=n/a, stim_expr=cue_stim_name
- BX: phase=delay fixation, deadline_expr=settings.isi_duration, response_expr=n/a, stim_expr='fixation'
- BX: phase=probe response, deadline_expr=settings.probe_duration, response_expr=settings.probe_duration, stim_expr=probe_stim_name
- BY: phase=context cue, deadline_expr=settings.cue_duration, response_expr=n/a, stim_expr=cue_stim_name
- BY: phase=delay fixation, deadline_expr=settings.isi_duration, response_expr=n/a, stim_expr='fixation'
- BY: phase=probe response, deadline_expr=settings.probe_duration, response_expr=settings.probe_duration, stim_expr=probe_stim_name

## 4. Mapping to task_plot_spec

- timeline collection: one representative timeline per unique trial logic
- phase flow inferred from run_trial set_trial_context order and branch predicates
- participant-visible show() phases without set_trial_context are inferred where possible and warned
- duration/response inferred from deadline/capture expressions
- stimulus examples inferred from stim_id + config stimuli
- conditions with equivalent phase/timing logic collapsed and annotated as variants
- root_key: task_plot_spec
- spec_version: 0.2

## 5. Style decision and rationale

- Single timeline-collection view selected by policy: one representative condition per unique timeline logic.

## 6. Rendering parameters and constraints

- output_file: task_flow.png
- dpi: 300
- max_conditions: 4
- screens_per_timeline: 6
- screen_overlap_ratio: 0.1
- screen_slope: 0.08
- screen_slope_deg: 25.0
- screen_aspect_ratio: 1.4545454545454546
- qa_mode: local
- auto_layout_feedback:
  - layout pass 1: crop-only; left=0.039, right=0.041, blank=0.151
- auto_layout_feedback_records:
  - pass: 1
    metrics: {'left_ratio': 0.0392, 'right_ratio': 0.0406, 'blank_ratio': 0.1513}

## 7. Output files and checksums

- E:\Taskbeacon\T000001-ax-cpt\references\task_plot_spec.yaml: sha256=a2744547248df0a0afbfd15111dd45042035f91703bdc8a69dcd07bab0df31b0
- E:\Taskbeacon\T000001-ax-cpt\references\task_plot_spec.json: sha256=1484462b3273cc3a6a6e93d26cf8aacb9d4bc3984d996685b05a692d91b76f68
- E:\Taskbeacon\T000001-ax-cpt\references\task_plot_source_excerpt.md: sha256=57c700dba9c18f3787acf8213d7f58657293a1c596ca7cd921977d3ea552011c
- E:\Taskbeacon\T000001-ax-cpt\task_flow.png: sha256=361fabc0404242c49b9dfc039fe2f716d786011525e13399a20322127cd5a09e

## 8. Inferred/uncertain items

- collapsed equivalent condition logic into representative timeline: AX, AY, BX, BY
- unparsed if-tests defaulted to condition-agnostic applicability: response; hit; response; not hit
