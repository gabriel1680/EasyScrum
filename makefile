run:
	flask run --host 0.0.0.0 --port 8080
venv:
	python3 -m venv venv && source venv/bin/activate
install:
	pip install -r requirements.txt
