# Organon Gītā

This is the source-based Gītā study in the four-part Organon collection:
Kośa, Gītā, Yoga, and Sāṃkhya. It is a new editorial layer; the existing
`Sankara/BG/` package remains intact as legacy research material.

## Editorial form

Work proceeds in textual order, one verse and its available Bhāṣya at a
time. Each unit has two linked reports:

- `BG_<chapter>.<verse>.md`: the mūla verse study, following the ten-stage
  verse-study sequence used in the Organon Kośa.
- `BG_<chapter>.<verse>_bhasya.md`: the paired Śaṅkara Bhāṣya study, keeping
  its continuous source, translation, argument, lexical determinations, and
  textual notes distinct.

Chapter folders use two-digit numbers under `chapters/`. The report
structure is shared with the Kośa, but Kośa-specific doctrine and technical
vocabulary are not imported into the Gītā. Interpretive claims remain
proportionate to the verse and its Bhāṣya; speculative or broader Yoga
Techne readings are not presumed.

## Text and evidence

- The Sanskrit verse and Bhāṣya are the primary witnesses. Translations and
  interpretations remain visibly distinct from them.
- Use the extracted records under
  `../sankara/derived/Gita/` and verify provenance in
  `../sankara/raw/manifest.jsonl`.
- Record source URL, page checksum, extracted passage ID, and any
  transcription or segmentation decisions in the Bhāṣya report.
- Keep chapter-leading Bhāṣya prose distinct from verse-level commentary.
  When commentary spans multiple verses, preserve its source boundary and
  make the relation explicit rather than manufacturing one commentary unit
  per verse.
- Do not supply a Bhāṣya where the source witness has none. Verse-only
  units may be studied as such and clearly marked.
- Mark studies provisional until textual and interpretive review is complete.

The initial paired study is `chapters/02/BG_2.11.md` and
`chapters/02/BG_2.11_bhasya.md`. Chapter 2, verse 11 is the first verse
record with a Bhāṣya in the extracted chapter 2 witness. This pilot tests
the paired form; it does not establish that later work should skip earlier
verse-only material.

An OWL++ section is retained in the verse-study sequence for structural
parity with the Kośa. Gītā-specific triples remain deferred until a Sankara
ontology and namespace are established; no ontology is invented for this
pilot.
