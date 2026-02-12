from psyflow import BlockUnit,StimBank, StimUnit,SubInfo,TaskSettings,initialize_triggers
from psyflow import load_config, initialize_exp
import pandas as pd
from psychopy import core

from src import run_trial
from functools import partial

# Load experiment configuration from config.yaml
cfg = load_config()

# Collect subject/session info using SubInfo form
subform = SubInfo(cfg['subform_config'])
subject_data = subform.collect()

# Load task settings and merge with subject info
settings = TaskSettings.from_dict(cfg['task_config'])
settings.add_subinfo(subject_data)
settings.save_to_json() # save all settings to json file

# Initialize trigger runtime from config
settings.triggers = cfg['trigger_config']

trigger_runtime = initialize_triggers(cfg)

# 5. Set up window & input
win, kb = initialize_exp(settings)

# 6. Setup stimulus bank
stim_bank = StimBank(win, cfg['stim_config']) \
.convert_to_voice(['instruction_text'], voice=settings.voice_name) \
.preload_all()

# Save settings to file (for logging and reproducibility)
settings.save_to_json()
trigger_runtime.send(settings.triggers.get("exp_onset"))
# Show instructions
StimUnit('instruction_text', win, kb)\
    .add_stim(stim_bank.get('instruction_text'))\
    .add_stim(stim_bank.get('instruction_text_voice'))\
    .wait_and_continue()

# Run task blocks
all_data = []
for block_i in range(settings.total_blocks):
    block = BlockUnit(
        block_id=f"block_{block_i}",
        block_idx=block_i,
        settings=settings,
        window=win,
        keyboard=kb
    ) \
.generate_conditions() \
.on_start(lambda b: trigger_runtime.send(settings.triggers.get("block_onset"))) \
.on_end(lambda b: trigger_runtime.send(settings.triggers.get("block_end"))) \
.run_trial(func=partial(run_trial, stim_bank=stim_bank, trigger_runtime=trigger_runtime)) \
.to_dict(all_data)

    # Customize block-level feedback (hit rate, scores, etc.)
    block_trials = block.get_all_data()
    correct_trials = [t for t in block_trials if t.get('probe_hit', False) is True]
    accuracy = len(correct_trials) / len(block_trials) if block_trials else 0

    StimUnit('block', win, kb).add_stim(stim_bank.get_and_format('block_break',
                                                              block_num=block_i+1,
                                                             total_blocks=settings.total_blocks,
                                                             accuracy=accuracy))\
                                .wait_and_continue() 

# Final screen (e.g., goodbye or total score)
StimUnit('goodbye', win, kb).add_stim(stim_bank.get('good_bye')).wait_and_continue(terminate=True)

trigger_runtime.send(settings.triggers.get("exp_end"))
# 9. Save data
df = pd.DataFrame(all_data)
df.to_csv(settings.res_file, index=False)

# 10. Close everything
trigger_runtime.close()
core.quit()





