#!/bin/bash
#SBATCH --job-name="4501r"
#SBATCH --error="my_job.err"
#SBATCH --output="my_job.output"
#SBATCH --partition="gpu"
#SBATCH --nodelist="jaguar02"

# python3 script.py
python3 /u/pft3gv/security/4501-Research/CloudShield/perf/data_collection.py --core 3 --us 10000 --n_readings 12000 --bg_program mysql_same_core
