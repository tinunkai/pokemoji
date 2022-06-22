all: upload

main:
	@.venv/bin/python main.py

yml:
	@.venv/bin/python yml.py

init:
	python3 -m venv .venv

rm:
	@.venv/bin/python rm.py

upload:
	@.venv/bin/python upload.py

install:
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt
