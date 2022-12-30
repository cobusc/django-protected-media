test:
	- pip install pytest
	DJANGO_SETTINGS_MODULE=tests.settings pytest

publish:
	- rm dist/*
	python setup.py sdist
	twine upload dist/*
