run:
	flask run

venv:
	python3 -m venv venv && source venv/bin/activate

install:
	pip install -r requirements.txt

dev-env:
	cat .example.env > .env

first-run:
	make venv && make install && make dev-env && make run
