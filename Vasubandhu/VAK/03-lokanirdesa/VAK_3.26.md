# VAK_3b — VAkK_3.26

## Sanskrit — Devanāgarī

क्लेशास्त्रीणि द्वयं कर्म सप्त वस्तु फलं तथा ।
फलहेत्वभिसंक्षेपो द्वयोर्मध्यानुमानतः ॥ VAkK_3.26 ॥

## Sanskrit — IAST

kleśās trīṇi dvayaṃ karma sapta vastu phalaṃ tathā /
phalahetvabhisaṃkṣepo dvayor madhyānumānataḥ // VAkK_3.26 //

## Padaccheda

| Sandhi form | Padaccheda | Basic meaning |
|---|---|---|
| kleśāḥ | kleśāḥ | afflictions |
| trīṇi | trīṇi | three |
| dvayam | dvayam | pair; two |
| karma | karma | action / karma |
| sapta | sapta | seven |
| vastu | vastu | real thing / substantial basis / factual item |
| phalam | phalam | fruit / result |
| tathā | tathā | likewise; thus |
| phalahetvabhisaṃkṣepaḥ | phala-hetu-abhisaṃkṣepaḥ | compression into fruit and cause |
| dvayoḥ | dvayoḥ | of the two |
| madhyānumānataḥ | madhya-anumānataḥ | by inference from the middle |

## Grammar

```text
kleśāḥ trīṇi
    = three are afflictions

dvayam karma
    = two are karma

sapta vastu phalam tathā
    = seven are vastu and likewise fruit

phala-hetu-abhisaṃkṣepaḥ
    = compression / summary as fruit and cause

dvayoḥ
    genitive dual
    = of the two, i.e. prior and later limits

madhya-anumānataḥ
    ablative of cause / means
    = by inference from the middle
```

## Literal Translation

Three are afflictions; two are karma; seven are vastu and likewise fruit. There is a compression into fruit and cause of the two, by inference from the middle.

## Philosophical Translation

The twelve limbs are compressed into a structural grouping: three are afflictions, two are karma, and seven are vastu, or resultant factual bases. The prior and later limits are summarized as cause and fruit by inference from the middle section.

## Technical Vocabulary

| Sanskrit | Working translation | Note |
|---|---|---|
| kleśa | affliction | Defiled motivational condition |
| trīṇi | three | Three links fall under kleśa |
| karma | karma / action | Projecting action |
| dvaya | pair / two | Two links fall under karma |
| vastu | real thing / factual basis | Here the concrete resultant factors |
| phala | fruit / result | Result-side of the process |
| hetu | ground / cause | Cause-side of the process |
| abhisaṃkṣepa | compression / summary | Condensation of the twelve into larger groups |
| madhya | middle | Present-life middle section |
| anumāna | inference | The two limits are inferred from the middle |

## Doctrinal Determination

VAkK_3.26 gives a second-level grouping of the twelve limbs.

```text
kleśa:
    3 limbs

karma:
    2 limbs

vastu / phala:
    7 limbs
```

The usual assignment is:

```text
Kleśa:
    avidyā
    tṛṣṇā
    upādāna

Karma:
    saṃskāra
    bhava

Vastu / Phala:
    vijñāna
    nāmarūpa
    ṣaḍāyatana
    sparśa
    vittiḥ / vedanā-position
    jāti
    jarāmaraṇa
```

Thus the twelvefold sequence is not only a temporal chain. It can also be read functionally:

```text
affliction
    → action
        → resultant factual basis
```

## Logical Determination

The verse compresses the twelve members into a cause-result structure.

```text
kleśa
    = motive-defilement

karma
    = action-formation

vastu / phala
    = resultant factual series
```

The key phrase is:

```text
phala-hetu-abhisaṃkṣepaḥ
```

That is, the system can be summarized as:

```text
cause
    ↓
fruit
```

But the verse adds an important epistemic point:

```text
dvayor madhya-anumānataḥ
```

The two limits are inferred from the middle. We directly analyze the middle, and from it infer prior cause and later result.

```text
prior limit
    inferred from middle

later limit
    inferred from middle
```

## Interpretive Note

This confirms that the middle section is methodologically central. The prior and later limits are not treated as directly visible independent substances. They are inferred from the present structure.

This also confirms 3.25: the limbs are stage-names by predominance. Now 3.26 compresses those stages into three functional classes:

```text
kleśa
karma
vastu / phala
```

## Organon Interpretation

Speculatively, this verse is close to a modeling rule.

```text
Observed middle
    ↓
infer prior cause
    ↓
infer future result
```

In Organon terms:

```text
middle dataset
    = manifest structure

prior limit
    = inferred ground

later limit
    = projected result
```

The twelvefold wheel is therefore not merely narrated. It is reconstructed by inference from the concrete middle.

This is a powerful rule for the VAK_3b block:

```text
Do not begin from invisible past or future.
Begin from the middle.
Infer the two limits from the middle.
```

## OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_26
    a vak:Karika ;
    rdfs:label "VAkK 3.26" ;
    vak:continues vak:VAK_3_25 ;
    vak:hasTopic vak:DependentCoArising ;
    vak:statesCompression vak:KleshaKarmaVastuCompression ;
    vak:statesMethod vak:MiddleInference .

vak:KleshaKarmaVastuCompression
    a logic:CompressionRule ;
    rdfs:label "kleśa-karma-vastu compression" ;
    rdfs:comment "The twelve limbs are compressed into three afflictions, two karmic factors, and seven resultant factual bases." .

vak:KleshaGroup
    a logic:FunctionalGroup ;
    rdfs:label "kleśa group" ;
    vak:hasMemberCount 3 .

vak:KarmaGroup
    a logic:FunctionalGroup ;
    rdfs:label "karma group" ;
    vak:hasMemberCount 2 .

vak:VastuPhalaGroup
    a logic:FunctionalGroup ;
    rdfs:label "vastu / phala group" ;
    vak:hasMemberCount 7 .

vak:MiddleInference
    a logic:InferenceRule ;
    rdfs:label "inference from the middle" ;
    vak:hasSanskrit "madhyānumāna" ;
    rdfs:comment "The prior and later limits are inferred from the manifest middle section." .
```

## Commit Note

Committed VAK_3b / VAkK_3.26.

Established:
- the twelve limbs are compressed as three kleśas, two karmic factors, and seven vastu/phala factors.
- the two limits are understood through inference from the middle.
- the middle section is the methodological center for reconstructing past cause and future result.

Logical determination:
VAkK_3.26 converts the twelvefold sequence into a functional analysis: affliction, action, and resultant factual basis. It also states the epistemic rule that the prior and later limits are inferred from the middle.
