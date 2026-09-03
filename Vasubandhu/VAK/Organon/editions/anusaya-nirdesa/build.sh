#!/usr/bin/env bash
set -euo pipefail

edition_dir="$(cd "$(dirname "$0")" && pwd)"
organon_dir="$(cd "$edition_dir/../.." && pwd)"
output_file="$edition_dir/Organon-Kosa-Anusaya-Nirdesa.pdf"

sources=()
for number in $(seq -w 1 70); do
  sources+=("$organon_dir/05-anusaya/VAK_5.$number.md")
done

pandoc "${sources[@]}" \
  --from=markdown+pipe_tables+fenced_code_blocks+raw_tex \
  --pdf-engine=xelatex \
  --lua-filter="$edition_dir/pagebreak.lua" \
  --include-in-header="$edition_dir/book-header.tex" \
  --metadata title="The Organon Kośa: Anuśayanirdeśa" \
  --metadata subtitle="The Systematic Analysis of the Latent Afflictions" \
  --metadata author="The Organon Project" \
  --metadata date="Provisional Complete-Chapter Edition · VAK 5.01–5.70" \
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
