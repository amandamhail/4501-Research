#!/bin/bash
# filename = jobScript
#SBATCH --job-name="4501r"
#SBATCH --error="my_job.err"
#SBATCH --output="my_job.output"
#SBATCH --partition="gpu"
#SBATCH --nodelist="jaguar02"
echo 'Cores per node:'
echo $SLURM_TASKS_PER_NODE
echo "$HOSTNAME"

python3 script.py
