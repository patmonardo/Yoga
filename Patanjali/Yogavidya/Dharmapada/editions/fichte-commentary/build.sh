#!/usr/bin/env bash
set -euo pipefail

edition_dir="$(cd "$(dirname "$0")" && pwd)"
dharmapada_dir="$(cd "$edition_dir/../.." && pwd)"
output_file="$edition_dir/Organon-Dharmapada-Fichte-Commentary.pdf"

sources=()
for number in $(seq 2 34); do
  sources+=("$dharmapada_dir/ys-iv-$number-fichte-report.md")
done

pandoc "${sources[@]}" \
  --from=markdown+pipe_tables+fenced_code_blocks+raw_tex \
  --pdf-engine=xelatex \
  --lua-filter="$edition_dir/pagebreak.lua" \
  --include-in-header="$edition_dir/book-header.tex" \
  --metadata title="Dharmapāda" \
  --metadata subtitle="Fichte and Yoga Sūtra IV.2–IV.34" \
  --metadata author="The Organon Project" \
  --metadata date="Provisional Study Edition" \
  --variable papersize=letter \
  --variable geometry:margin=0.78in \
  --variable mainfont="FreeSerif" \
  --variable sansfont="Lato" \
  --variable monofont="FreeMono" \
  --variable fontsize=10pt \
  --variable linestretch=1.05 \
  --toc \
  --toc-depth=1 \
  --output="$output_file"

printf '%s\n' "$output_file"
