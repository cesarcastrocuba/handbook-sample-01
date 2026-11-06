.PHONY: check test validate-book full

PYTHON ?= python3
TOOLKIT ?= handbook-toolkit

# Fast checks. Requires the pinned toolkit from requirements.txt.
check: test
	$(PYTHON) -B scripts/check_repo.py
	$(TOOLKIT) validate-book book.yaml

# Local gate-policy tests only; no toolkit or network required.
test:
	$(PYTHON) -B -m unittest discover -s scripts/tests -p 'test_*.py'

# Fast descriptor check from the pinned toolkit. No chapter validation.
validate-book:
	$(TOOLKIT) validate-book book.yaml

# Full editorial checks: descriptor, reading order, cross-references and every
# chapter against the packaged approved profile. No artifact build is run.
full: check
	$(TOOLKIT) validate-book --full book.yaml
	$(TOOLKIT) validate-references book.yaml
	@set -e; \
	profile=$$(mktemp --suffix=.yaml); \
	trap 'rm -f "$$profile"' EXIT; \
	$(PYTHON) -c 'import yaml; from handbook_toolkit.profile_resources import load_profile; book = yaml.safe_load(open("book.yaml")); print(yaml.safe_dump(load_profile(book["profile"]["id"], book["profile"]["version"]), sort_keys=False))' > "$$profile"; \
	for file in manuscript/chapters/*.qmd manuscript/appendices/*.qmd; do \
		$(TOOLKIT) validate-manuscript "$$file" --mode chapter --profile "$$profile"; \
	done
