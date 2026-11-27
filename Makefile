.PHONY: check test validate-book full build

PYTHON ?= python3
TOOLKIT ?= handbook-toolkit
COMMIT ?= $(shell git rev-parse HEAD)
OUTPUT ?= ../dist
BUILD_FLAGS ?=

# Fast checks. Requires the pinned toolkit from requirements.txt.
check: test
	$(PYTHON) -B scripts/check_repo.py
	$(TOOLKIT) validate-book book.yaml

# Book-local gate and workflow tests. PyYAML is installed by requirements.txt.
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
	dir=$$(mktemp -d "$${TMPDIR:-/tmp}/profile.XXXXXX"); \
	trap 'rm -rf "$$dir"' EXIT; \
	trap 'exit 129' HUP; \
	trap 'exit 130' INT; \
	trap 'exit 143' TERM; \
	profile="$$dir/profile.yaml"; \
	$(PYTHON) -c 'import yaml; from handbook_toolkit.profile_resources import load_profile; book = yaml.safe_load(open("book.yaml")); print(yaml.safe_dump(load_profile(book["profile"]["id"], book["profile"]["version"]), sort_keys=False))' > "$$profile"; \
	for file in manuscript/chapters/*.qmd manuscript/appendices/*.qmd; do \
		$(TOOLKIT) validate-manuscript "$$file" --mode chapter --profile "$$profile"; \
	done

# Build the seven-file release directory once. Requires Quarto 1.11.9, pdfinfo,
# qpdf 11 or later and LibreOffice Writer; the output must be outside the
# repository. This book keeps `full` as the editorial-only gate above, so an
# artifact build is always explicit.
build: check
	$(TOOLKIT) build-book --repo . --commit $(COMMIT) --output $(OUTPUT) --mode chapter $(BUILD_FLAGS)
