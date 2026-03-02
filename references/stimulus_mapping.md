# Stimulus Mapping

## Mapping Table

| Condition | Stage/Phase | Stimulus IDs | Participant-Facing Content | Source Paper ID | Evidence (quote/figure/table) | Implementation Mode | Asset References | Notes |
|---|---|---|---|---|---|---|---|---|
| `AX` | `context_cue -> probe_response` | `cue_A`, `probe_X` | `Cue letter A followed by probe letter X` | `W2558198874` | `AX pair defines target context in AX-CPT` | `psychopy_builtin` | `n/a` | Maps to target trial. |
| `AY` | `context_cue -> probe_response` | `cue_A`, `probe_Y` | `Cue letter A followed by probe letter Y` | `W2558198874` | `AY trial probes expectancy violation after A cue` | `psychopy_builtin` | `n/a` | Non-target trial. |
| `BX` | `context_cue -> probe_response` | `cue_B`, `probe_X` | `Cue letter B followed by probe letter X` | `W2558198874` | `BX trial isolates proactive control demands` | `psychopy_builtin` | `n/a` | Non-target trial. |
| `BY` | `context_cue -> probe_response` | `cue_B`, `probe_Y` | `Cue letter B followed by probe letter Y` | `W2558198874` | `BY trial serves as low-conflict non-target baseline` | `psychopy_builtin` | `n/a` | Non-target trial. |
| `all_conditions` | `fixation` | `fixation` | `Central plus sign` | `W2047427656` | `AX-CPT sequence includes fixation/cross epochs between task letters` | `psychopy_builtin` | `n/a` | Shared timing anchor. |
| `all_conditions` | `feedback` | `correct_feedback`, `incorrect_feedback`, `no_response_feedback` | `Chinese feedback text for correct, incorrect, and no response` | `W2120312500` | `Translational tasks require interpretable performance readouts` | `psychopy_builtin` | `n/a` | Explicit trial feedback is an implementation choice and should be justified in protocol notes. |
| `all_conditions` | `instruction` | `instruction_text`, `instruction_text_voice` | `Chinese instruction text and optional synthesized voice` | `W2752630266` | `AX-CPT psychometric work depends on clear, stable task instructions` | `psychopy_builtin` | `assets/instruction_text_voice.mp3` | Text is config-defined, supporting localization portability. |

