from psyflow import StimUnit
from functools import partial

def run_trial(win,kb,settings,condition: str,stim_bank: dict,trigger_runtime=None,):
    """
    Runs a single trial of the AX-CPT task.

    Args:
        win: The PsychoPy window object.
        kb: The keyboard handler.
        settings: The task settings object.
        condition (str): A string defining the current trial's type,
                         e.g., "AX", "AY", "BX", "BY".
        stim_bank: The stimulus bank containing all visual stimuli.
        trigger_runtime: The object responsible for sending EEG/fMRI triggers.

    Returns:
        dict: A dictionary containing all data recorded for this trial.
    """
    trial_data = {"condition": condition}
    make_unit = partial(StimUnit, win=win, kb=kb, runtime=trigger_runtime)

    # --- 1. Determine trial properties from condition string ---
    cue_letter = condition[0]
    probe_letter = condition[1]

    is_target_trial = (cue_letter == 'A' and probe_letter == 'X')
    correct_response = settings.target_key if is_target_trial else settings.nontarget_key

    trial_data.update({
        "cue_letter": cue_letter,
        "probe_letter": probe_letter,
        "is_target_trial": is_target_trial,
        "correct_response": correct_response
    })

    # --- 2. Fixation ---
    make_unit(unit_label='fixation') \
  .add_stim(stim_bank.get("fixation")) \
  .show(duration=settings.fixation_duration, onset_trigger=settings.triggers.get("fixation_onset")) \
  .to_dict(trial_data)

    # --- 3. Cue Presentation ---
    cue_stim_name = f"cue_{cue_letter}"
    make_unit(unit_label="cue").add_stim(stim_bank.get(cue_stim_name)).show(duration=settings.cue_duration, onset_trigger=settings.triggers.get("cue_onset")).to_dict(trial_data)

    # --- 4. Inter-Stimulus Interval (ISI) Fixation ---
    make_unit(unit_label='isi_fixation').add_stim(stim_bank.get("fixation")).show(duration=settings.isi_duration).to_dict(trial_data)

    # --- 5. Probe Presentation & Response ---
    probe_stim_name = f"probe_{probe_letter}"
    stim_unit = make_unit(unit_label="probe").add_stim(stim_bank.get(probe_stim_name))
    
    stim_unit.capture_response(
        keys=settings.key_list,
        correct_keys=correct_response,
        duration=settings.probe_duration,
        response_trigger=settings.triggers.get("key_press"),
        onset_trigger=settings.triggers.get(f"{condition}_trial_onset"),
        terminate_on_response=True
    )
    stim_unit.to_dict(trial_data)

    # --- 5. Determine Accuracy and Feedback ---
    response = stim_unit.get_state("response", False)
    hit = stim_unit.get_state("hit", False)

    if response and hit:
        feedback_stim = stim_bank.get("correct_feedback")
        feedback_trigger = settings.triggers.get("feedback_correct_response")
    elif response and not hit:
        feedback_stim = stim_bank.get("incorrect_feedback")
        feedback_trigger = settings.triggers.get("feedback_incorrect_response")
    else:
        feedback_stim = stim_bank.get("no_response_feedback")
        feedback_trigger = settings.triggers.get("feedback_no_response")

    # --- 6. Feedback ---
    make_unit(unit_label="feedback") \
  .add_stim(feedback_stim) \
  .show(duration=settings.feedback_duration, onset_trigger=feedback_trigger) \
  .to_dict(trial_data)

    # --- 7. Inter-Trial Interval (ITI) ---
    make_unit(unit_label='iti').show(duration=settings.iti_duration).to_dict(trial_data)

    return trial_data

