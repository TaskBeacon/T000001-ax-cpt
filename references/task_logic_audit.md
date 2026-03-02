# Task Logic Audit

## 1. Paradigm Intent

- Task: AX Continuous Performance Test (AX-CPT).
- Primary construct: Context maintenance and proactive control.
- Manipulated factors: Cue-probe combination (`AX`, `AY`, `BX`, `BY`) and resulting expectancy/conflict profile.
- Dependent measures: Accuracy by condition, RT by condition, omission/commission pattern.
- Key citations:
  - W2558198874
  - W2752630266
  - W2047427656
  - W2120312500

## 2. Block/Trial Workflow

### Block Structure

- Total blocks: 4 (current implementation).
- Trials per block: 40 (current implementation).
- Randomization/counterbalancing:
  - Current code path uses weighted `BlockUnit.generate_conditions(weights=...)`.
  - Condition weights are config-defined: `AX=0.4, AY=0.1, BX=0.1, BY=0.4`.
- Condition generation method:
  - Built-in `BlockUnit.generate_conditions(...)` is used.
  - Expectancy-sensitive distribution is enforced via `task.condition_weights` (no custom generator needed).
- Runtime-generated trial values:
  - Cue/probe letters are parsed from condition tokens in `run_trial.py`.
  - ITI is sampled from `[min, max]` range by `StimUnit.show`.

### Trial State Machine

1. Fixation
   - Onset trigger: `fixation_onset`
   - Stimuli shown: `fixation`
   - Valid keys: none (behaviorally ignored)
   - Timeout behavior: deterministic end after `timing.fixation_duration`
   - Next state: `context_cue`
2. Context Cue
   - Onset trigger: `cue_onset`
   - Stimuli shown: `cue_A` or `cue_B`
   - Valid keys: task keys are listed in context, but no response is collected at this stage
   - Timeout behavior: deterministic end after `timing.cue_duration`
   - Next state: `delay_fixation`
3. Delay Fixation
   - Onset trigger: none in current implementation
   - Stimuli shown: `fixation`
   - Valid keys: task keys are listed in context, but no response is collected at this stage
   - Timeout behavior: deterministic end after `timing.isi_duration`
   - Next state: `probe_response`
4. Probe Response
   - Onset trigger: `{condition}_trial_onset`
   - Stimuli shown: `probe_X` or `probe_Y`
   - Valid keys: `task.key_list`
   - Timeout behavior: ends on first response or on `timing.probe_duration` timeout
   - Next state: `feedback`
5. Feedback
   - Onset trigger: one of `feedback_correct_response`, `feedback_incorrect_response`, `feedback_no_response`
   - Stimuli shown: condition-dependent feedback text stimulus
   - Valid keys: none
   - Timeout behavior: deterministic end after `timing.feedback_duration`
   - Next state: `iti`
6. ITI
   - Onset trigger: none in current implementation
   - Stimuli shown: blank screen (`StimUnit.show` without explicit visual stimulus)
   - Valid keys: none
   - Timeout behavior: random duration in configured ITI range
   - Next state: next trial

## 3. Condition Semantics

For each condition token in `task.conditions`:

- Condition ID: `AX`
  - Participant-facing meaning: target pair.
  - Concrete stimulus realization: cue letter `A`, then probe letter `X`.
  - Outcome rules: response should match `task.target_key`.
- Condition ID: `AY`
  - Participant-facing meaning: expectancy-violation non-target.
  - Concrete stimulus realization: cue `A`, probe `Y`.
  - Outcome rules: response should match `task.nontarget_key`.
- Condition ID: `BX`
  - Participant-facing meaning: context-driven non-target with probe lure.
  - Concrete stimulus realization: cue `B`, probe `X`.
  - Outcome rules: response should match `task.nontarget_key`.
- Condition ID: `BY`
  - Participant-facing meaning: non-target baseline.
  - Concrete stimulus realization: cue `B`, probe `Y`.
  - Outcome rules: response should match `task.nontarget_key`.

Also document where participant-facing condition text/stimuli are defined:

- Participant-facing text source: `config/*.yaml` under `stimuli`.
- Why this source is appropriate for auditability: wording/layout can be versioned and localized without touching trial logic.
- Localization strategy: swap config stimulus text/font/voice fields by language profile, while keeping `run_trial.py` unchanged.

## 4. Response and Scoring Rules

- Response mapping: two-key mapping (`target_key` and `nontarget_key`) configured in task config.
- Response key source: config fields (`task.target_key`, `task.nontarget_key`, `task.key_list`).
- Missing-response policy: timeout is logged; feedback uses `no_response_feedback`.
- Correctness logic: only `AX` is treated as target; all other conditions are non-target.
- Reward/penalty updates: none (no cumulative reward model).
- Running metrics: block-level accuracy currently computed from probe hit flags.

## 5. Stimulus Layout Plan

For every screen with multiple simultaneous options/stimuli:

- Screen name: trial epochs (`fixation`, `cue`, `probe`, `feedback`)
  - Stimulus IDs shown together: one primary visual stimulus per frame.
  - Layout anchors (`pos`): centered by default PsychoPy placement.
  - Size/spacing (`height`, width, wrap): letter stimuli use shared height; instruction textbox uses explicit size/wrap.
  - Readability/overlap checks: low overlap risk due single-stimulus display design.
  - Rationale: canonical AX-CPT uses sequential cue/probe letter displays.

## 6. Trigger Plan

- `exp_onset` / `exp_end`: experiment lifecycle boundaries.
- `block_onset` / `block_end`: block boundaries.
- `fixation_onset`: fixation stage onset.
- `cue_onset`: cue display onset.
- `{AX,AY,BX,BY}_trial_onset`: probe/decision stage onset by condition.
- `key_press`: response trigger.
- `no_response`: timeout trigger.
- `feedback_correct_response` / `feedback_incorrect_response` / `feedback_no_response`: outcome coding.
- `feedback_onset`: defined in config but not currently emitted by `run_trial.py`.

## 7. Architecture Decisions (Auditability)

- `main.py` runtime flow style: single mode-aware flow (`human|qa|sim`) with consistent setup order.
- `utils.py` used: no task-specific `utils.py` currently required.
- Custom controller used: no.
- PsyFlow-native sufficiency: yes for this task structure.
- Legacy/backward-compatibility fallback logic required: no explicit fallback branches detected.

## 8. Inference Log

- Decision: Current delay (`isi_duration=0.5s`) is treated as an adapted short-delay variant.
  - Why inference was required: Selected references include multiple timing variants.
  - Citation-supported rationale: Timing parameters vary by paradigm objective and acquisition constraints; this profile should be justified explicitly in task docs.
- Decision: Explicit per-trial feedback is considered implementation-specific rather than universal AX-CPT requirement.
  - Why inference was required: Selected references are not uniform on feedback presentation.
  - Citation-supported rationale: Translational/clinical adaptations often tune feedback while preserving cue-probe decision logic.

