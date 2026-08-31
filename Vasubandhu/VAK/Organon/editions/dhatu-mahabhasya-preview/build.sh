#!/usr/bin/env bash
set -euo pipefail

edition_dir="$(cd "$(dirname "$0")" && pwd)"
vak_dir="$(cd "$edition_dir/../../.." && pwd)"
source_dir="$vak_dir/01-dhatu"
output_file="$edition_dir/Organon-Kosa-Dhatu-Mahabhasya-Preview.pdf"

sources=()
for number in $(seq -w 1 48); do
  sources+=("$source_dir/VAK_1.${number}_bhasya.md")
done

pandoc "${sources[@]}" \
  --from=markdown+pipe_tables+fenced_code_blocks+raw_tex \
  --pdf-engine=xelatex \
  --lua-filter="$edition_dir/pagebreak.lua" \
  --include-in-header="$edition_dir/book-header.tex" \
  --metadata title="The Organon Kośa: Dhātu Mahābhāṣya Preview" \
  --metadata subtitle="Initial Bhāṣya Analysis · Forty-Eight Units" \
  --metadata author="The Organon Project" \
  --metadata date="Working Preview Edition" \
  --variable papersize=letter \
  --variable geometry:margin=0.78in \
  --variable mainfont="FreeSerif" \
  --variable sansfont="Lato" \
  --variable monofont="FreeMono" \
  --variable fontsize=10pt \
  --variable linestretch=1.08 \
  --toc \
  --toc-depth=1 \
  --output="$output_file"

printf '%s\n' "$output_file"
