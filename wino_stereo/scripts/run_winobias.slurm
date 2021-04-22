#!/bin/bash
#SBATCH --job-name=winobias_all
#SBATCH --open-mode=append
#SBATCH --output=/home/ks4765/crows-pairs-commit/wino_slurm_output/%j_%x.out
#SBATCH --error=/home/ks4765/crows-pairs-commit/wino_slurm_output/%j_%x.err
#SBATCH --export=ALL
#SBATCH --time=2:00:00
#SBATCH --gres=gpu:1
#SBATCH --mem=8G
#SBATCH -c 4

## TODO: Run your hyperparameter search in a singularity container. Remember to 
## activate your Conda environment in the container before running your Python script.

singularity exec --nv --overlay $SCRATCH/overlay-25GB-500K.ext3:rw /scratch/work/public/singularity/cuda10.1-cudnn7-devel-ubuntu18.04-20201207.sif /bin/bash -c 'source /ext3/env.sh \
&& conda activate \
&& python metric.py  --input_file ../data/winobias.type1.csv --metric mask-ngram --lm_model bert --output_file ../wino_res/bert_wino1_score.csv \
&& python metric.py  --input_file ../data/winobias.type1.csv --metric mask-ngram --lm_model roberta --output_file ../wino_res/roberta_wino1_score.csv \
&& python metric.py  --input_file ../data/winobias.type1.csv --metric mask-ngram --lm_model biobert --output_file ../wino_res/biobert_wino1_score.csv \
&& python metric.py  --input_file ../data/winobias.type1.csv --metric mask-ngram --lm_model biobert-large --output_file ../wino_res/biobert-large_wino1_score.csv \
&& python metric.py  --input_file ../data/winobias.type1.csv --metric mask-ngram --lm_model scibert --output_file ../wino_res/scibert_wino1_score.csv \
&& python metric.py  --input_file ../data/winobias.type2.csv --metric mask-ngram --lm_model bert --output_file ../wino_res/bert_wino2_score.csv \
&& python metric.py  --input_file ../data/winobias.type2.csv --metric mask-ngram --lm_model roberta --output_file ../wino_res/roberta_wino2_score.csv \
&& python metric.py  --input_file ../data/winobias.type2.csv --metric mask-ngram --lm_model biobert --output_file ../wino_res/biobert_wino2_score.csv \
&& python metric.py  --input_file ../data/winobias.type2.csv --metric mask-ngram --lm_model biobert-large --output_file ../wino_res/biobert-large_wino2_score.csv \
&& python metric.py  --input_file ../data/winobias.type2.csv --metric mask-ngram --lm_model scibert --output_file ../wino_res/scibert_wino2_score.csv'