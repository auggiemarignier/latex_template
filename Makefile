# Makefile — build `main.tex` with latexmk

TEX := main.tex
OUT := $(TEX:.tex=.pdf)
OUTDIR := build
LATEXMK := latexmk
LATEXMKFLAGS_COMMON := -pdf -interaction=nonstopmode -file-line-error -synctex=1
LATEXMKFLAGS := $(LATEXMKFLAGS_COMMON) -outdir=$(OUTDIR)

.DEFAULT_GOAL := pdf

.PHONY: all pdf view clean pyfigs tikzfigs

all: pdf

pdf:
	$(LATEXMK) $(LATEXMKFLAGS) $(TEX)

view: pdf
	open $(OUTDIR)/$(OUT)

clean:
	$(LATEXMK) -c $(OUTDIR)


pyfigs:
	mkdir -p figures/generated
	for f in figures/scripts/*.py; do \
		uv run "$$f"; \
	done

tikzfigs:
	mkdir -p figures/generated
	for f in figures/tikz/*.tikz; do \
		if [ -e "$$f" ]; then \
			base=$$(basename "$$f" .tikz); \
			$(LATEXMK) $(LATEXMKFLAGS_COMMON) -outdir=figures/generated "$$f"; \
		fi; \
	done
	