#!/usr/bin/env bash
set -euo pipefail

edition_dir="$(cd "$(dirname "$0")" && pwd)"
organon_dir="$(cd "$edition_dir/.." && pwd)"

usage() {
  cat <<'EOF'
Usage: editions/build.sh --chapter 1-8 --kind karika|bhasya [options]

Options:
  --start NUMBER   First verse to include (default: 1)
  --end NUMBER     Last verse to include (default: full chapter)
  --output PATH    PDF output path (default: editions/<configured filename>)
  --dry-run        Validate inputs and show the build configuration
  -h, --help       Show this help

Configured ranges are listed by each chapter's current complete-study count.
EOF
}

chapter=
kind=
start=1
end=
output=
dry_run=0

while (($#)); do
  case "$1" in
    --chapter)
      (($# >= 2)) || { echo "Missing value for --chapter" >&2; exit 2; }
      chapter="$2"
      shift 2
      ;;
    --kind)
      (($# >= 2)) || { echo "Missing value for --kind" >&2; exit 2; }
      kind="$2"
      shift 2
      ;;
    --start)
      (($# >= 2)) || { echo "Missing value for --start" >&2; exit 2; }
      start="$2"
      shift 2
      ;;
    --end)
      (($# >= 2)) || { echo "Missing value for --end" >&2; exit 2; }
      end="$2"
      shift 2
      ;;
    --output)
      (($# >= 2)) || { echo "Missing value for --output" >&2; exit 2; }
      output="$2"
      shift 2
      ;;
    --dry-run)
      dry_run=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if [[ -z "$chapter" || -z "$kind" ]]; then
  echo "Both --chapter and --kind are required." >&2
  usage >&2
  exit 2
fi
if [[ ! "$chapter" =~ ^[1-8]$ ]]; then
  echo "Unsupported chapter: $chapter (choose 1 through 8)." >&2
  exit 2
fi
if [[ "$kind" != "karika" && "$kind" != "bhasya" ]]; then
  echo "Unsupported kind: $kind (choose karika or bhasya)." >&2
  exit 2
fi
if [[ ! "$start" =~ ^[0-9]+$ ]] || ((start < 1)); then
  echo "--start must be a positive integer." >&2
  exit 2
fi
if [[ -n "$end" && ! "$end" =~ ^[0-9]+$ ]]; then
  echo "--end must be an integer greater than or equal to --start." >&2
  exit 2
fi
if [[ -n "$end" ]] && ((end < start)); then
  echo "--end must be an integer greater than or equal to --start." >&2
  exit 2
fi

case "$chapter" in
  1)
    chapter_dir="01-dhatu"
    chapter_name="Dhātunirdeśa"
    chapter_count=48
    ;;
  2)
    chapter_dir="02-indriya"
    chapter_name="Indriyanirdeśa"
    chapter_count=73
    ;;
  3)
    chapter_dir="03-loka"
    chapter_name="Lokanirdeśa"
    chapter_count=102
    ;;
  4)
    chapter_dir="04-karma"
    chapter_name="Karmanirdeśa"
    chapter_count=127
    ;;
  5)
    chapter_dir="05-anusaya"
    chapter_name="Anuśayanirdeśa"
    chapter_count=70
    ;;
  6)
    chapter_dir="06-marga"
    chapter_name="Mārganirdeśa"
    chapter_count=79
    ;;
  7)
    chapter_dir="07-jnana"
    chapter_name="Jñānanirdeśa"
    chapter_count=56
    ;;
  8)
    chapter_dir="08-samapatti"
    chapter_name="Samāpattinirdeśa"
    chapter_count=43
    ;;
esac

if [[ -z "$end" ]]; then
  end="$chapter_count"
fi
if ((end > chapter_count)); then
  echo "Chapter $chapter $kind is configured through verse $chapter_count." >&2
  exit 2
fi

study_kind="Kārikā"
source_suffix=
if [[ "$kind" == "bhasya" ]]; then
  study_kind="Bhāṣya"
  source_suffix="_bhasya"
fi
title="The Organon Kośa: $chapter_name $study_kind"

case "$chapter:$kind" in
  1:karika)
    subtitle="A Sequential Study Edition"
    edition_status="Study Edition"
    output_name="Organon-Kosa-Dhatu-Karika.pdf"
    ;;
  1:bhasya)
    subtitle="A Continuous Translation and Focused Study"
    edition_status="Study Edition"
    output_name="Organon-Kosa-Dhatu-Bhasya.pdf"
    ;;
  2:karika)
    subtitle="A Sequential Study Edition"
    edition_status="Study Edition"
    output_name="Organon-Kosa-Indriya-Karika.pdf"
    ;;
  2:bhasya)
    subtitle="A Continuous Translation and Focused Study"
    edition_status="Study Edition"
    output_name="Organon-Kosa-Indriya-Bhasya.pdf"
    ;;
  3:karika)
    subtitle="The Systematic Analysis of the World"
    edition_status="Provisional Study Edition · Complete"
    output_name="Organon-Kosa-Loka-Karika.pdf"
    ;;
  3:bhasya)
    subtitle="A Continuous Translation and Focused Study"
    edition_status="Study Edition"
    output_name="Organon-Kosa-Loka-Bhasya.pdf"
    ;;
  4:karika)
    subtitle="The Systematic Analysis of Karma"
    edition_status="Provisional Complete-Chapter Edition"
    output_name="Organon-Kosa-Karma-Karika.pdf"
    ;;
  4:bhasya)
    subtitle="A Continuous Translation and Focused Study"
    edition_status="Complete Chapter Studies · Provisional Readings"
    output_name="Organon-Kosa-Karma-Bhasya.pdf"
    ;;
  5:karika)
    subtitle="The Systematic Analysis of the Latent Afflictions"
    edition_status="Provisional Complete-Chapter Edition"
    output_name="Organon-Kosa-Anusaya-Karika.pdf"
    ;;
  5:bhasya)
    subtitle="A Continuous Translation and Focused Study"
    edition_status="Complete Chapter Study"
    output_name="Organon-Kosa-Anusaya-Bhasya.pdf"
    ;;
  6:karika)
    subtitle="The Systematic Analysis of the Path"
    edition_status="Provisional Complete-Chapter Edition"
    output_name="Organon-Kosa-Marga-Karika.pdf"
    ;;
  6:bhasya)
    subtitle="A Continuous Translation and Focused Study"
    edition_status="Provisional Work in Progress"
    output_name="Organon-Kosa-Marga-Bhasya.pdf"
    ;;
  7:karika)
    subtitle="The Systematic Analysis of Knowledge"
    edition_status="Provisional Complete-Chapter Edition"
    output_name="Organon-Kosa-Jnana-Karika.pdf"
    ;;
  7:bhasya)
    subtitle="A Continuous Translation and Focused Study"
    edition_status="Study Edition"
    output_name="Organon-Kosa-Jnana-Bhasya.pdf"
    ;;
  8:karika)
    subtitle="The Systematic Analysis of Meditative Attainment"
    edition_status="Provisional Complete-Chapter Edition"
    output_name="Organon-Kosa-Samapatti-Karika.pdf"
    ;;
  8:bhasya)
    subtitle="A Continuous Translation and Focused Study"
    edition_status="Study Edition"
    output_name="Organon-Kosa-Samapatti-Bhasya.pdf"
    ;;
esac

first_verse="$(printf '%02d' "$start")"
last_verse="$(printf '%02d' "$end")"
date_text="$edition_status · VAK $chapter.$first_verse–$chapter.$last_verse"
if [[ "$chapter:$kind" == "5:bhasya" ]]; then
  date_text+=" · Provisional"
fi
output_file="${output:-$edition_dir/$output_name}"
filter_file="$edition_dir/pagebreak.lua"
header_file="$edition_dir/book-header.tex"

sources=()
missing_sources=()
for ((verse = start; verse <= end; verse++)); do
  number="$(printf '%02d' "$verse")"
  source="$organon_dir/$chapter_dir/VAK_$chapter.$number$source_suffix.md"
  if [[ -f "$source" ]]; then
    sources+=("$source")
  else
    missing_sources+=("$source")
  fi
done

if ((${#missing_sources[@]})); then
  printf 'Missing source files:\n' >&2
  printf '  %s\n' "${missing_sources[@]}" >&2
  exit 1
fi
for required_file in "$filter_file" "$header_file"; do
  if [[ ! -f "$required_file" ]]; then
    echo "Required shared build asset not found: $required_file" >&2
    exit 1
  fi
done

if ((dry_run)); then
  printf 'PDF: %s\n' "$output_file"
  printf 'Sources: %d (VAK %s.%s–%s.%s)\n' \
    "${#sources[@]}" "$chapter" "$first_verse" "$chapter" "$last_verse"
  printf 'Title: %s\nSubtitle: %s\nDate: %s\n' \
    "$title" "$subtitle" "$date_text"
  exit 0
fi

command -v pandoc >/dev/null || {
  echo "Pandoc is required to build the PDF." >&2
  exit 1
}
command -v xelatex >/dev/null || {
  echo "XeLaTeX is required to build the PDF." >&2
  exit 1
}

pandoc "${sources[@]}" \
  --from=markdown+pipe_tables+fenced_code_blocks+raw_tex \
  --pdf-engine=xelatex \
  --lua-filter="$filter_file" \
  --include-in-header="$header_file" \
  --metadata "title=$title" \
  --metadata "subtitle=$subtitle" \
  --metadata author="The Organon Project" \
  --metadata "date=$date_text" \
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
