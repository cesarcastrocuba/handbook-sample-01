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

# Full verification remains incomplete as an editorial and artifact gate.
# It runs the full descriptor/reading-order check, then fails on the remaining scope.
# Never report this target as passing.
full: check
	$(TOOLKIT) validate-book --full book.yaml
	@printf '%s\n' "FULL VERIFICATION INCOMPLETE (current scope)"
	@printf '%s\n' "- Descriptor and reading-order full check passed."
	@printf '%s\n' "- Manuscript content and profile conformance are not validated by toolkit 0.1.0."
	@printf '%s\n' "- No artifact manifest or checksums exist, so artifact validation cannot run."
	@exit 1
