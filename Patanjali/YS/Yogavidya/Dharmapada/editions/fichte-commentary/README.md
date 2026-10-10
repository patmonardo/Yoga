# Dharmapāda: Fichte Commentary Edition

This directory contains the print-oriented PDF edition generated from the
thirty-three Fichte reports in `Docs/Dharmapada`, covering the project's Yoga
Sūtra IV.2–IV.34 sequence.

The Markdown reports remain the canonical editable sources. The PDF is a
derived reading artifact. Each sūtra report begins on a new page, while a
report may continue across as many pages as required.

Yoga Sūtra IV.1 is intentionally outside this project's Dharmapāda sequence.
The separate `ys-iv-8-10-synthesis.md` is not included in this sequential
commentary edition.

Copyright notice in this edition:

> © 2026 The Organon Project. All rights reserved.

This notice records the present reserved-rights status and may be replaced by
an explicit distribution license in a later edition.

Build requirements:

- Pandoc
- XeLaTeX
- FreeSerif, Lato, and FreeMono fonts

Run `./build.sh` from this directory to rebuild the PDF.
