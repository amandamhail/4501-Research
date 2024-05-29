.PHONY: all clean

PYTHON = python3

all: script

script: script.py
	$(PYTHON) $<

clean:
	rm -r code_llama_pipe cloudshield_pipe
