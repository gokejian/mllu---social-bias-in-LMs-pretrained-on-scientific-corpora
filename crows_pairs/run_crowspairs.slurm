#!/bin/bash
#SBATCH --job-name=run_crowspairs
#SBATCH --open-mode=append
#SBATCH --output=/home/ks4765/crows_pairs/crows_slurm_output/%j_%x.out
#SBATCH --error=/home/ks4765/crows_pairs/crows_slurm_output/%j_%x.err
#SBATCH --export=ALL
#SBATCH --time=48:00:00
#SBATCH --gres=gpu:2
#SBATCH --mem=64G
#SBATCH -c 4

## TODO: Run your hyperparameter search in a singularity container. Remember to 
## activate your Conda environment in the container before running your Python script.

singularity exec --nv --overlay $SCRATCH/overlay-25GB-500K.ext3:rw /scratch/work/public/singularity/cuda10.1-cudnn7-devel-ubuntu18.04-20201207.sif /bin/bash -c 'source /ext3/env.sh && conda activate && python metric.py  --input_file data/crows_pairs_anonymized.csv --lm_model bert  --output_file bert_crows_score && python metric.py  --input_file data/crows_pairs_anonymized.csv --lm_model roberta  --output_file roberta_crows_score && python metric.py  --input_file data/crows_pairs_anonymized.csv --lm_model biobert  --output_file biobert_crows_score && python metric.py  --input_file data/crows_pairs_anonymized.csv --lm_model scibert  --output_file scibert_crows_score'


