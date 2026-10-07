#!/usr/bin/env bash
set -euo pipefail

edition_dir="$(cd "$(dirname "$0")" && pwd)"
organon_dir="$(cd "$edition_dir/../.." && pwd)"
output_file="$edition_dir/Organon-Kosa-Dhatu-Karika.pdf"

sources=()
for index in $(seq 1 48); do
  number="$(printf '%02d' "$index")"
  sources+=("$organon_dir/01-dhatu/VAK_1.$number.md")
done

pandoc "${sources[@]}" \
  --from=markdown+pipe_tables+fenced_code_blocks+raw_tex \
  --pdf-engine=xelatex \
  --lua-filter="$organon_dir/editions/pagebreak.lua" \
  --include-in-header="$organon_dir/editions/book-header.tex" \
  --metadata title="The Organon Kośa: Dhātunirdeśa Kārikā" \
  --metadata subtitle="A Sequential Study Edition" \
  --metadata author="The Organon Project" \
  --metadata date="Study Edition · VAK 1.01–1.48" \
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
