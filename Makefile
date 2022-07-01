.PHONY: init install
all: upload

%: %.py
	@.venv/bin/python $<

init:
	python3 -m venv .venv

install:
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt
