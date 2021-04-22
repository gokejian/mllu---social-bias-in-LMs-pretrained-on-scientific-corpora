#!/bin/bash
#SBATCH --job-name=stereoset_all
#SBATCH --open-mode=append
#SBATCH --output=/home/ks4765/crows-pairs-commit/stereo_slurm_output/%j_%x.out
#SBATCH --error=/home/ks4765/crows-pairs-commit/stereo_slurm_output/%j_%x.err
#SBATCH --export=ALL
#SBATCH --time=2:00:00
#SBATCH --gres=gpu:1
#SBATCH --mem=16G
#SBATCH -c 4

## TODO: Run your hyperparameter search in a singularity container. Remember to 
## activate your Conda environment in the container before running your Python script.

singularity exec --nv --overlay $SCRATCH/overlay-25GB-500K.ext3:rw /scratch/work/public/singularity/cuda10.1-cudnn7-devel-ubuntu18.04-20201207.sif /bin/bash -c 'source /ext3/env.sh \
&& conda activate \
&& python metric.py  --input_file ../data/stereoset.csv --metric mask-ngram --lm_model bert          --output_file ../stereo_res/bert_stereo_score.csv \
&& python metric.py  --input_file ../data/stereoset.csv --metric mask-ngram --lm_model roberta       --output_file ../stereo_res/roberta_stereo_score.csv \
&& python metric.py  --input_file ../data/stereoset.csv --metric mask-ngram --lm_model biobert       --output_file ../stereo_res/biobert_stereo_score.csv \
&& python metric.py  --input_file ../data/stereoset.csv --metric mask-ngram --lm_model biobert-large --output_file ../stereo_res/biobert-large_stereo_score.csv \
&& python metric.py  --input_file ../data/stereoset.csv --metric mask-ngram --lm_model scibert       --output_file ../stereo_res/scibert_stereo_score.csv'