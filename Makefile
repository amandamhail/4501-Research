.PHONY: all clean

PYTHON = python3

all: script slurm

script: script.py
	$(PYTHON) $<

slurm: jobScript.slurm
	sbatch $<

clean:
	rm -r CloudShield/attack/ai_modified/modified_attack.c
	rm -r CloudShield/attack/ai_modified/Makefile
	rm -r CloudShield/attack/ai_modified/ai_modified_attack
	rm -r CloudShield/attack/ai_modified/spectre_result.csv
	rm -r CloudShield/attack/ai_modified/spectre_time.csv
	rmdir CloudShield/attack/ai_modified