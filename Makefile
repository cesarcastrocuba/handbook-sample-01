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

# Full verification is currently incomplete as a content-and-artifact gate.
# It runs the fast descriptor check, then fails with the remaining scope gaps.
# Never report this target as passing.
full: check
	@printf '%s\n' "FULL VERIFICATION INCOMPLETE (current scope)"
	@printf '%s\n' "- Fast descriptor check passed; this is not a descriptor failure."
	@printf '%s\n' "- validate-book --full is not run: no pilot or chapter .qmd exists yet; it may run once the pilot exists."
	@printf '%s\n' "- No artifact manifest or checksums exist, so artifact validation cannot run."
	@exit 1
