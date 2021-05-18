#!/bin/bash
#SBATCH --job-name=biobase-superglue
#SBATCH --open-mode=append
#SBATCH --output=/home/ks4765/biobert_base_out/%j_%x.out
#SBATCH --error=/home/ks4765/biobert_base_out/%j_%x.err
#SBATCH --export=ALL
#SBATCH --time=00:50:00
#SBATCH --gres=gpu:1
#SBATCH --mem=16G
#SBATCH -c 4

## TODO: Run your hyperparameter search in a singularity container. Remember to
## activate your Conda environment in the container before running your Python script.
singularity exec --nv --overlay $SCRATCH/overlay-25GB-500K.ext3:rw /scratch/work/public/singularity/cuda10.1-cudnn7-devel-ubuntu18.04-20201207.sif /bin/bash -c "
source /ext3/env.sh
conda activate
python bio_base_superglue.py
"
