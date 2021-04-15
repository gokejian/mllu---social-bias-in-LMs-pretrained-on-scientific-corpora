from jiant.proj.simple import runscript as run
import jiant.scripts.download_data.runscript as downloader

EXP_DIR = "./esp"

# Download the Data
downloader.download_data(['boolq','cb','copa','multirc','rte','wic','wsc'], f"{EXP_DIR}/tasks")

# Set up the arguments for the Simple API
args0 = run.RunConfiguration(
   run_name="simple",
   exp_dir=EXP_DIR,
   data_dir=f"{EXP_DIR}/tasks",
   hf_pretrained_model_name_or_path="roberta-large",
   tasks="boolq",
   train_batch_size=16,
   num_train_epochs=3
)

# Run!
run.run_simple(args0)

# Set up the arguments for the Simple API
args1 = run.RunConfiguration(
   run_name="simple",
   exp_dir=EXP_DIR,
   data_dir=f"{EXP_DIR}/tasks",
   hf_pretrained_model_name_or_path="roberta-large",
   tasks="cb",
   train_batch_size=16,
   num_train_epochs=3
)

# Run!
run.run_simple(args1)

# Set up the arguments for the Simple API
args2 = run.RunConfiguration(
   run_name="simple",
   exp_dir=EXP_DIR,
   data_dir=f"{EXP_DIR}/tasks",
   hf_pretrained_model_name_or_path="roberta-large",
   tasks="copa",
   train_batch_size=16,
   num_train_epochs=3
)

# Run!
run.run_simple(args2)

# Set up the arguments for the Simple API
args3 = run.RunConfiguration(
   run_name="simple",
   exp_dir=EXP_DIR,
   data_dir=f"{EXP_DIR}/tasks",
   hf_pretrained_model_name_or_path="roberta-large",
   tasks="multirc",
   train_batch_size=16,
   num_train_epochs=3
)

# Run!
run.run_simple(args3)

'''# Set up the arguments for the Simple API
args4 = run.RunConfiguration(
   run_name="simple",
   exp_dir=EXP_DIR,
   data_dir=f"{EXP_DIR}/tasks",
   hf_pretrained_model_name_or_path="roberta-large",
   tasks="record",
   train_batch_size=16,
   num_train_epochs=3
)

# Run!
run.run_simple(args4)'''

# Set up the arguments for the Simple API
args5 = run.RunConfiguration(
   run_name="simple",
   exp_dir=EXP_DIR,
   data_dir=f"{EXP_DIR}/tasks",
   hf_pretrained_model_name_or_path="roberta-large",
   tasks="rte",
   train_batch_size=16,
   num_train_epochs=3
)

# Run!
run.run_simple(args5)

# Set up the arguments for the Simple API
args6 = run.RunConfiguration(
   run_name="simple",
   exp_dir=EXP_DIR,
   data_dir=f"{EXP_DIR}/tasks",
   hf_pretrained_model_name_or_path="roberta-large",
   tasks="wic",
   train_batch_size=16,
   num_train_epochs=3
)

# Run!
run.run_simple(args6)

# Set up the arguments for the Simple API
args7 = run.RunConfiguration(
   run_name="simple",
   exp_dir=EXP_DIR,
   data_dir=f"{EXP_DIR}/tasks",
   hf_pretrained_model_name_or_path="roberta-large",
   tasks="wsc",
   train_batch_size=16,
   num_train_epochs=3
)

# Run!
run.run_simple(args7)
