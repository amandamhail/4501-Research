#!/bin/bash
#SBATCH --job-name="4501r"
#SBATCH --error="my_job.err"
#SBATCH --output="my_job.output"
#SBATCH --partition="gpu"
SBATCH --nodelist="jaguar02"

python3 script.py
