
from jiant.proj.simple import runscript as run
import jiant.scripts.download_data.runscript as downloader

EXP_DIR = "./bert_results"

# Download the Data
downloader.download_data(['boolq','cb','copa','multirc','record','rte','wic','wsc','superglue_broadcoverage_diagnostics','superglue_winogender_diagnostics'], f"{EXP_DIR}/tasks")

# Set up the arguments for the Simple API
args0 = run.RunConfiguration(
   run_name="simple",
   exp_dir=EXP_DIR,
   data_dir=f"{EXP_DIR}/tasks",
   hf_pretrained_model_name_or_path="bert-base-uncased",
   tasks="boolq",
   train_batch_size=16,
   num_train_epochs=3
)

# Run!
run.run_simple(args0)

args1 = run.RunConfiguration(
   run_name="simple",
   exp_dir=EXP_DIR,
   data_dir=f"{EXP_DIR}/tasks",
   hf_pretrained_model_name_or_path="bert-base-uncased",
   tasks="cb",
   train_batch_size=16,
   num_train_epochs=3
)

# Run!
run.run_simple(args1)

args2 = run.RunConfiguration(
   run_name="simple",
   exp_dir=EXP_DIR,
   data_dir=f"{EXP_DIR}/tasks",
   hf_pretrained_model_name_or_path="bert-base-uncased",
   tasks="copa",
   train_batch_size=16,
   num_train_epochs=3
)

# Run!
run.run_simple(args2)


args3 = run.RunConfiguration(
   run_name="simple",
   exp_dir=EXP_DIR,
   data_dir=f"{EXP_DIR}/tasks",
   hf_pretrained_model_name_or_path="bert-base-uncased",
   tasks="multirc",
   train_batch_size=16,
   num_train_epochs=3
)

# Run!
run.run_simple(args3)



args5 = run.RunConfiguration(
   run_name="simple",
   exp_dir=EXP_DIR,
   data_dir=f"{EXP_DIR}/tasks",
   hf_pretrained_model_name_or_path="bert-base-uncased",
   tasks="rte",
   train_batch_size=16,
   num_train_epochs=3
)


# Run!
run.run_simple(args5)


args6 = run.RunConfiguration(
   run_name="simple",
   exp_dir=EXP_DIR,
   data_dir=f"{EXP_DIR}/tasks",
   hf_pretrained_model_name_or_path="bert-base-uncased",
   tasks="wic",
   train_batch_size=16,
   num_train_epochs=3
)

# Run!
run.run_simple(args6)

args7 = run.RunConfiguration(
   run_name="simple",
   exp_dir=EXP_DIR,
   data_dir=f"{EXP_DIR}/tasks",
   hf_pretrained_model_name_or_path="bert-base-uncased",
   tasks="wsc",
   train_batch_size=16,
   num_train_epochs=3
)

# Run!
run.run_simple(args7)


args8 = run.RunConfiguration(
   run_name="simple",
   exp_dir=EXP_DIR,
   data_dir=f"{EXP_DIR}/tasks",
   hf_pretrained_model_name_or_path="bert-base-uncased",
   tasks="superglue_broadcoverage_diagnostics",
   train_batch_size=16,
   num_train_epochs=3
)

# Run!
run.run_simple(args8)



args9 = run.RunConfiguration(
   run_name="simple",
   exp_dir=EXP_DIR,
   data_dir=f"{EXP_DIR}/tasks",
   hf_pretrained_model_name_or_path="bert-base-uncased",
   tasks="superglue_winogender_diagnostics",
   train_batch_size=16,
   num_train_epochs=3
)

# Run!
run.run_simple(args9)

# args4 = run.RunConfiguration(
#    run_name="simple",
#    exp_dir=EXP_DIR,
#    data_dir=f"{EXP_DIR}/tasks",
#    hf_pretrained_model_name_or_path="bert-base-uncased",
#    tasks="record",
#    train_batch_size=16,
#    num_train_epochs=3
# )

# # Run!
# run.run_simple(args4)
