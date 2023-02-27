install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	echo "Not implemented yet"
	python -m pytest tests

format:	
	black ppt_nlp

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py 

refactor: format lint

all: install lint test