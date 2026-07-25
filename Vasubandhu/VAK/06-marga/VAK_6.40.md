# VAK 6.40

## Sanskrit

### Devanāgarī

ऊर्ध्वस्रोतुरभेदेन सप्त सद्गतयो मताः ।  
सदसद्वृत्त्यवृत्तिभ्यां गताप्रत्यागतेश्च ताः ॥ ६.४० ॥

### IAST

**ūrdhva-srotur abhedena sapta sad-gatayo matāḥ |**  
**sad-asad-vṛtty-avṛttibhyāṃ gatāpratyāgateś ca tāḥ || 6.40 ||**

## Source Caution

The verse gives a sevenfold classification of the upward-streamer. Its compact compounds require Bhāṣya-level unpacking. The first pass therefore records only the explicit structure:

```text
upward-streamer
    seven good destinies

classified through:
    occurrence / non-occurrence
    good / not-good mode
    gone / not-returned
```

The detailed distribution of these alternatives is deferred.

## Padaccheda

```text
ūrdhva-srotuḥ
abhedena
sapta
sat-gatayaḥ
matāḥ

sat-asat-vṛtti-avṛttibhyām
gata-apratyāgateḥ
ca
tāḥ
```

## Grammar

- **ūrdhva-srotuḥ** — genitive singular: “of the upward-streamer.”
- **abhedena** — instrumental singular: “by distinction” or “through subdivision.”
- **sapta** — “seven.”
- **sat-gatayaḥ** — nominative plural feminine: “good destinies” or “fortunate courses.”
- **matāḥ** — nominative plural feminine: “are held” or “are considered.”
- **sat-asat-vṛtti-avṛttibhyām** — instrumental dual compound; the exact doctrinal distribution is compressed.
- **gata-apratyāgateḥ** — genitive singular compound: “of one gone and not returned,” or “through the distinction of gone / not-returned.”
- **ca** — “and.”
- **tāḥ** — nominative plural feminine: “those.”

## Literal Translation

By subdivision, seven good destinies are held for the upward-streamer. They are determined through the alternatives of occurrence and non-occurrence, good and not-good mode, and of being gone or not returned.

## Philosophical Translation

The upward-streamer is not a single undifferentiated type. The Kośa subdivides this practitioner into seven fortunate courses according to a compact set of alternatives concerning the manner in which the course occurs and the way in which the practitioner proceeds without returning.

## Technical Determination

```text
UpwardStreamer {
    subdivisions:
        SevenGoodDestinies

    distinguishingFactors:
        Occurrence
        NonOccurrence
        GoodMode
        NonGoodMode
        Gone
        NotReturned
}
```

## Logical Determination

VAK 6.37–6.39 introduced and explained the principal non-returner types. VAK 6.40 continues the schema by expanding one of those types internally:

```text
non-returner
    → upward-streamer
        → sevenfold subdivision
```

The verse is therefore classificatory rather than explanatory.

## OWL++ Seed

```text
Class: NonReturner
Class: UpwardStreamer
Class: GoodDestiny
Class: SevenfoldUpwardStreamerClassification

ObjectProperty: hasSubdivision
ObjectProperty: distinguishedBy
ObjectProperty: proceedsThrough

UpwardStreamer
    hasSubdivision SevenfoldUpwardStreamerClassification

SevenfoldUpwardStreamerClassification
    hasMember GoodDestiny
```

## Determinate Summary

```text
The upward-streamer
    is subdivided into seven good destinies.

The distinctions involve:
    occurrence / non-occurrence
    mode of course
    gone / not-returned
```

The exact allocation of the seven types is reserved for the Bhāṣya pass.