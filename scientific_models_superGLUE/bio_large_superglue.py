
from jiant.proj.simple import runscript as run
import jiant.scripts.download_data.runscript as downloader
import os
import jiant.utils.python.io as py_io

EXP_DIR = "/home/ks4765/jiant-js-feature-easy_add_model/biobert_large"
HF_PRETRAINED_MODEL_NAME = "dmis-lab/biobert-large-cased-v1.1"
MODEL_NAME = HF_PRETRAINED_MODEL_NAME.split("/")[-1]
# Download the Data
downloader.download_data(['wic','wsc'], f"{EXP_DIR}/tasks")


TASK_NAME = "wic"
RUN_NAME = f"simple_{TASK_NAME}_{MODEL_NAME}"

args4 = run.RunConfiguration(
   run_name=RUN_NAME,
   exp_dir=EXP_DIR,
   data_dir=f"{EXP_DIR}/tasks",
   hf_pretrained_model_name_or_path=HF_PRETRAINED_MODEL_NAME,
   tasks=TASK_NAME,
   train_batch_size=16,
   num_train_epochs=3
)
# Run!
run.run_simple(args4)

TASK_NAME = "wsc"
RUN_NAME = f"simple_{TASK_NAME}_{MODEL_NAME}"

args5 = run.RunConfiguration(
   run_name=RUN_NAME,
   exp_dir=EXP_DIR,
   data_dir=f"{EXP_DIR}/tasks",
   hf_pretrained_model_name_or_path=HF_PRETRAINED_MODEL_NAME,
   tasks=TASK_NAME,
   train_batch_size=16,
   num_train_epochs=3
)
# Run!
run.run_simple(args5)



# TASK_NAME = "boolq"
# RUN_NAME = f"simple_{TASK_NAME}_{MODEL_NAME}"
# # Set up the arguments for the Simple API
# args0 = run.RunConfiguration(
#    run_name=RUN_NAME,
#    exp_dir=EXP_DIR,
#    data_dir=f"{EXP_DIR}/tasks",
#    hf_pretrained_model_name_or_path=HF_PRETRAINED_MODEL_NAME,
#    tasks=TASK_NAME,
#    train_batch_size=16,
#    num_train_epochs=3
# )
# # Run!
# run.run_simple(args0)


# TASK_NAME = "cb"
# RUN_NAME = f"simple_{TASK_NAME}_{MODEL_NAME}"

# args1 = run.RunConfiguration(
#    run_name=RUN_NAME,
#    exp_dir=EXP_DIR,
#    data_dir=f"{EXP_DIR}/tasks",
#    hf_pretrained_model_name_or_path=HF_PRETRAINED_MODEL_NAME,
#    tasks=TASK_NAME,
#    train_batch_size=16,
#    num_train_epochs=3
# )
# # Run!
# run.run_simple(args1)


# TASK_NAME = "copa"
# RUN_NAME = f"simple_{TASK_NAME}_{MODEL_NAME}"


# args2 = run.RunConfiguration(
#    run_name=RUN_NAME,
#    exp_dir=EXP_DIR,
#    data_dir=f"{EXP_DIR}/tasks",
#    hf_pretrained_model_name_or_path=HF_PRETRAINED_MODEL_NAME,
#    tasks=TASK_NAME,
#    train_batch_size=16,
#    num_train_epochs=3
# )
# # Run!
# run.run_simple(args2)

# TASK_NAME = "multirc"
# RUN_NAME = f"simple_{TASK_NAME}_{MODEL_NAME}"

# args3 = run.RunConfiguration(
#    run_name=RUN_NAME,
#    exp_dir=EXP_DIR,
#    data_dir=f"{EXP_DIR}/tasks",
#    hf_pretrained_model_name_or_path=HF_PRETRAINED_MODEL_NAME,
#    tasks=TASK_NAME,
#    train_batch_size=16,
#    num_train_epochs=3
# )
# # Run!
# run.run_simple(args3)

# TASK_NAME = "rte"
# RUN_NAME = f"simple_{TASK_NAME}_{MODEL_NAME}"

# args6 = run.RunConfiguration(
#    run_name=RUN_NAME,
#    exp_dir=EXP_DIR,
#    data_dir=f"{EXP_DIR}/tasks",
#    hf_pretrained_model_name_or_path=HF_PRETRAINED_MODEL_NAME,
#    tasks=TASK_NAME,
#    train_batch_size=16,
#    num_train_epochs=3
# )
# # Run!
# run.run_simple(args6)


