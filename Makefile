BIN = ./venv/bin/

clean:
	rm -rf venv
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf


venv:
	python -m venv venv

install_requirements:
	$(BIN)pip install -r requirements.txt

install: clean venv install_requirements
	$(BIN)python manage.py migrate
	$(BIN)python manage.py collectstatic

test:
	$(BIN)pytest tests



