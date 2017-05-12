test:
	python setup.py test

publish:
	- rm dist/*
	python setup.py sdist
	twine upload dist/*
