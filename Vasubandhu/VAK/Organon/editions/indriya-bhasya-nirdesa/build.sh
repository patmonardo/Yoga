#!/usr/bin/env bash
set -euo pipefail

edition_dir="$(cd "$(dirname "$0")" && pwd)"
organon_dir="$(cd "$edition_dir/../.." && pwd)"
output_file="$edition_dir/Organon-Kosa-Indriya-Bhasya-Nirdesa.pdf"

sources=()
for index in $(seq 1 73); do
  number="$(printf '%02d' "$index")"
  sources+=("$organon_dir/02-indriya/VAK_2.$number"_bhasya.md)
done

pandoc "${sources[@]}" \
  --from=markdown+pipe_tables+fenced_code_blocks+raw_tex \
  --pdf-engine=xelatex \
  --lua-filter="$edition_dir/pagebreak.lua" \
  --include-in-header="$edition_dir/book-header.tex" \
  --metadata title="The Organon Kośa: Indriyanirdeśa Bhāṣya" \
  --metadata subtitle="A Continuous Translation and Focused Study" \
  --metadata author="The Organon Project" \
  --metadata date="Complete Chapter Study Edition · VAK 2.01–2.73" \
  --variable papersize=letter \
  --variable geometry:margin=0.78in \
  --variable mainfont="FreeSerif" \
  --variable sansfont="Lato" \
  --variable monofont="FreeMono" \
  --variable fontsize=10pt \
  --variable linestretch=1.05 \
  --toc \
  --toc-depth=1 \
  --number-sections \
  --output="$output_file"

printf '%s\n' "$output_file"
