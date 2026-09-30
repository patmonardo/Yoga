#!/usr/bin/env bash
set -euo pipefail

edition_dir="$(cd "$(dirname "$0")" && pwd)"
organon_dir="$(cd "$edition_dir/../.." && pwd)"
output_file="$edition_dir/Organon-Kosa-Loka-Nirdesa.pdf"

sources=()
for number in $(seq -w 1 99); do
  sources+=("$organon_dir/03-loka/VAK_3.$number.md")
done
sources+=("$organon_dir/03-loka/VAK_3.100.md")
sources+=("$organon_dir/03-loka/VAK_3.101.md")
sources+=("$organon_dir/03-loka/VAK_3.102.md")

pandoc "${sources[@]}" \
  --from=markdown+pipe_tables+fenced_code_blocks+raw_tex \
  --pdf-engine=xelatex \
  --lua-filter="$edition_dir/pagebreak.lua" \
  --include-in-header="$edition_dir/book-header.tex" \
  --metadata title="The Organon Kośa: Lokanirdeśa" \
  --metadata subtitle="The Systematic Analysis of the World" \
  --metadata author="The Organon Project" \
  --metadata date="Provisional Study Edition · Complete VAK 3.01–3.102" \
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
