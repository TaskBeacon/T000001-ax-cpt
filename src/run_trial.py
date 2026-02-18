from functools import partial

from psyflow import StimUnit, set_trial_context

# trial stages use task-specific phase labels via set_trial_context(...)
_TRIAL_COUNTER = 0


def _next_trial_id() -> int:
    global _TRIAL_COUNTER
    _TRIAL_COUNTER += 1
    return _TRIAL_COUNTER


def _deadline_s(value) -> float | None:
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, (list, tuple)) and value:
        try:
            return float(max(value))
        except Exception:
            return None
    return None


def run_trial(
    win,
    kb,
    settings,
    condition: str,
    stim_bank: dict,
    trigger_runtime=None,
    block_id=None,
    block_idx=None,
):
    """Run one AX-CPT trial."""
    trial_id = _next_trial_id()
    trial_data = {"condition": condition}
    make_unit = partial(StimUnit, win=win, kb=kb, runtime=trigger_runtime)

    cue_letter = condition[0]
    probe_letter = condition[1]

    is_target_trial = cue_letter == "A" and probe_letter == "X"
    correct_response = settings.target_key if is_target_trial else settings.nontarget_key

    trial_data.update(
        {
            "cue_letter": cue_letter,
            "probe_letter": probe_letter,
            "is_target_trial": is_target_trial,
            "correct_response": correct_response,
        }
    )

    # phase: context_cue
    make_unit(unit_label="fixation").add_stim(stim_bank.get("fixation")).show(
        duration=settings.fixation_duration,
        onset_trigger=settings.triggers.get("fixation_onset"),
    ).to_dict(trial_data)

    cue_stim_name = f"cue_{cue_letter}"
    cue_unit = make_unit(unit_label="cue").add_stim(stim_bank.get(cue_stim_name))
    set_trial_context(
        cue_unit,
        trial_id=trial_id,
        phase="context_cue",
        deadline_s=_deadline_s(settings.cue_duration),
        valid_keys=list(settings.key_list),
        block_id=block_id,
        condition_id=str(condition),
        task_factors={
            "condition": str(condition),
            "stage": "context_cue",
            "cue_letter": cue_letter,
            "probe_letter": probe_letter,
            "block_idx": block_idx,
        },
        stim_id=cue_stim_name,
    )
    cue_unit.show(duration=settings.cue_duration, onset_trigger=settings.triggers.get("cue_onset")).to_dict(trial_data)

    # phase: delay_fixation
    isi_unit = make_unit(unit_label="isi_fixation").add_stim(stim_bank.get("fixation"))
    set_trial_context(
        isi_unit,
        trial_id=trial_id,
        phase="delay_fixation",
        deadline_s=_deadline_s(settings.isi_duration),
        valid_keys=list(settings.key_list),
        block_id=block_id,
        condition_id=str(condition),
        task_factors={
            "condition": str(condition),
            "stage": "delay_fixation",
            "cue_letter": cue_letter,
            "probe_letter": probe_letter,
            "block_idx": block_idx,
        },
        stim_id="fixation",
    )
    isi_unit.show(duration=settings.isi_duration).to_dict(trial_data)

    # phase: probe_response
    probe_stim_name = f"probe_{probe_letter}"
    probe_unit = make_unit(unit_label="probe").add_stim(stim_bank.get(probe_stim_name))
    set_trial_context(
        probe_unit,
        trial_id=trial_id,
        phase="probe_response",
        deadline_s=_deadline_s(settings.probe_duration),
        valid_keys=list(settings.key_list),
        block_id=block_id,
        condition_id=str(condition),
        task_factors={
            "condition": str(condition),
            "stage": "probe_response",
            "cue_letter": cue_letter,
            "probe_letter": probe_letter,
            "correct_key": str(correct_response),
            "block_idx": block_idx,
        },
        stim_id=probe_stim_name,
    )
    probe_unit.capture_response(
        keys=settings.key_list,
        correct_keys=correct_response,
        duration=settings.probe_duration,
        response_trigger=settings.triggers.get("key_press"),
        onset_trigger=settings.triggers.get(f"{condition}_trial_onset"),
        terminate_on_response=True,
    )
    probe_unit.to_dict(trial_data)

    # outcome display
    response = probe_unit.get_state("response", False)
    hit = probe_unit.get_state("hit", False)

    if response and hit:
        feedback_stim = stim_bank.get("correct_feedback")
        feedback_trigger = settings.triggers.get("feedback_correct_response")
    elif response and not hit:
        feedback_stim = stim_bank.get("incorrect_feedback")
        feedback_trigger = settings.triggers.get("feedback_incorrect_response")
    else:
        feedback_stim = stim_bank.get("no_response_feedback")
        feedback_trigger = settings.triggers.get("feedback_no_response")

    make_unit(unit_label="feedback").add_stim(feedback_stim).show(
        duration=settings.feedback_duration,
        onset_trigger=feedback_trigger,
    ).to_dict(trial_data)

    make_unit(unit_label="iti").show(duration=settings.iti_duration).to_dict(trial_data)

    return trial_data
