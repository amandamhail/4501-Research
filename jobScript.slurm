#!/bin/bash
# --- this job will be run on any available node
# and simply output the node's hostname to
# my_job.output
#SBATCH --job-name="research -- test"
#SBATCH --error="my_job.err"
#SBATCH --output="my_job.output"
#SBATCH --partition="gpu"
#SBATCH --nodelist="jaguar 01"
echo "$HOSTNAME"
python3 script.py
