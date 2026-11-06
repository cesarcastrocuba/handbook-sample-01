.PHONY: check test

check: test
	python3 -B scripts/check_repo.py

test:
	python3 -B -m unittest discover -s scripts/tests -p 'test_*.py'
