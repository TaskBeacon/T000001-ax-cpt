# Parameter Mapping

## Mapping Table

| Parameter ID | Config Path | Implemented Value | Source Paper ID | Evidence (quote/figure/table) | Decision Type | Notes |
|---|---|---|---|---|---|---|
| `conditions` | `task.conditions` | `[AX, AY, BX, BY]` | `W2558198874` | `AX-CPT condition family and proactive-control interpretation` | `direct` | Core condition schema is aligned. |
| `target_rule` | `task.target_key` + `task.nontarget_key` | `AX -> f; non-AX -> j` | `W2558198874` | `AX target vs non-target response rule described in AX-CPT task methods` | `direct` | Response mapping structure is aligned; key letters are localized choices. |
| `total_blocks` | `task.total_blocks` | `4` | `W2752630266` | `AX-CPT often run in multi-block designs for stable estimates` | `adapted` | Reasonable for reliability; verify against exact study objective. |
| `total_trials` | `task.total_trials` | `160` | `W2752630266` | `Psychometric analyses rely on sufficient trial counts` | `adapted` | Trial count is plausible but should be justified explicitly in task docs. |
| `trial_per_block` | `task.trial_per_block` | `40` | `W2752630266` | `Block-wise analysis and reliability discussion in AX-CPT context` | `adapted` | Keep if fatigue is acceptable in target population. |
| `condition_distribution` | `task.condition_weights` + `BlockUnit.generate_conditions(weights=...)` | `AX=0.4, AY=0.1, BX=0.1, BY=0.4` | `W2558198874` | `Inducing Proactive Control Shifts in the AX-CPT reports AX-CPT variants with AX and BY at high frequency and AY/BX low frequency.` | `adapted` | Weighted generation now enforces expectancy-sensitive sampling instead of uniform randomization. |
| `fixation_duration` | `timing.fixation_duration` | `0.5 s` | `W2047427656` | `Cue/probe epochs separated by brief fixation epochs in AX-CPT implementations` | `adapted` | Acceptable as an adapted timing profile. |
| `cue_duration` | `timing.cue_duration` | `0.5 s` | `W2047427656` | `Letter cue presentation stage in AX-CPT procedures` | `adapted` | Keep only if justified for EEG design constraints. |
| `isi_duration` | `timing.isi_duration` | `0.5 s` | `W2558198874` | `Cue-probe separation is a core AX-CPT control element` | `inferred` | Delay appears shorter than common AX-CPT variants; verify against intended construct emphasis. |
| `probe_duration` | `timing.probe_duration` | `1.0 s` | `W2558198874` | `Probe response window defines target/non-target decision epoch` | `adapted` | Reasonable if accuracy/RT tradeoff is acceptable. |
| `feedback_duration` | `timing.feedback_duration` | `0.5 s` | `W2120312500` | `Clinical translation guidance emphasizes interpretable performance feedback/metrics` | `inferred` | Trial-level explicit feedback is optional in AX-CPT literature; consider protocol consistency. |
| `iti_duration` | `timing.iti_duration` | `[0.8, 1.2] s` | `W2047427656` | `Use of temporal jitter in neurocognitive paradigms` | `adapted` | Jitter is methodologically sensible for EEG timing decorrelation. |
| `trigger_schema` | `triggers.map.*` | `Event-coded cue/probe/response/feedback` | `W2120312500` | `CNTRICS translational framing supports task event observability` | `inferred` | Trigger taxonomy is acquisition-driven, not uniquely prescribed by a single AX-CPT paper. |

