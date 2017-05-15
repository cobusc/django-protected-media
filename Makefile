test:
	make -C example test

publish:
	- rm dist/*
	python setup.py sdist
	twine upload dist/*
