.PHONY: all clean

PYTHON = python3

all: script slurm

script: script.py
	$(PYTHON) $<

slurm: jobScript.slurm
	sbatch $<

clean:
	rm -r code_llama_pipe cloudshield_pipe