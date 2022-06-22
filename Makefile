all: yml

main:
	@.venv/bin/python main.py

yml:
	@.venv/bin/python yml.py

init:
	python3 -m venv .venv

install:
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt
