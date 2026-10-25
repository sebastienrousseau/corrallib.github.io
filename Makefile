# SPDX-License-Identifier: Apache-2.0 OR MIT
# Semantic Version: v0.0.1
.PHONY: all build audit test contrast validate compress prune clean help

all: build

help:
	@echo "Available Makefile targets:"
	@echo "  make build      - Compile static site using Rust static-site-generator"
	@echo "  make audit      - Run WCAG 2.2 AAA and regression tests"
	@echo "  make contrast   - Verify color tokens against WCAG 2.2 AAA math ratios"
	@echo "  make validate   - Validate Markdown frontmatter schema integrity"
	@echo "  make clean      - Remove build artifacts and temporary files"

build:
	rm -rf docs
	ssg build -f ssg.toml -q
	python3 scripts/post-build.py

audit: contrast validate
	@/usr/bin/python3 scripts/regression-test.py

contrast:
	@/usr/bin/python3 scripts/audit-contrast.py

validate:
	@/usr/bin/python3 scripts/validate-frontmatter.py

clean:
	@rm -rf public docs dist .cache coverage *.log
	@echo "Workspace cleaned."
