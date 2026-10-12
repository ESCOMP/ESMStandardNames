# Makefile for building the ESM Standard Names Sphinx documentation locally.

SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = html

.PHONY: help html clean

help:
	@echo "Targets:"
	@echo "  html   - build the HTML docs into $(BUILDDIR)/"
	@echo "  clean  - remove the built docs"

html:
	$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/."

clean:
	rm -rf "$(BUILDDIR)"
