./venv:
	virtualenv venv --always-copy
	./venv/bin/pip install nose

test: ./venv/
	DJANGO_SETTINGS_MODULE=tests.settings ./venv/bin/nosetests

publish:
	- rm dist/*
	python setup.py sdist
	twine upload dist/*
