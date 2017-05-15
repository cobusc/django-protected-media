test:
	- pip install nose
	DJANGO_SETTINGS_MODULE=tests.settings nosetests

publish:
	- rm dist/*
	python setup.py sdist
	twine upload dist/*
