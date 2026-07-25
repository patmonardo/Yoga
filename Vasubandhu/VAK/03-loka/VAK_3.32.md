# VAK_3b — VAkK_3.32

## Sanskrit — Devanāgarī

तज्जाः षड्वेदनाः पञ्च कायिकी चैतसी परा ।
पुनश्चाष्टादशविधा सा मनोपविचारतः ॥ VAkK_3.32 ॥

## Sanskrit — IAST

tajjāḥ ṣaḍvedanāḥ pañca kāyikī caitasī parā /
punaścāṣṭādaśavidhā sā manopavicārataḥ // VAkK_3.32 //

## Padaccheda

| Sandhi form | Padaccheda | Basic meaning |
|---|---|---|
| tajjāḥ | tat-jāḥ | born from that; born from contact |
| ṣaḍvedanāḥ | ṣaṭ-vedanāḥ | six feelings / affective experiences |
| pañca | pañca | five |
| kāyikī | kāyikī | bodily |
| caitasī | caitasī | mental |
| parā | parā | the other; the remaining one |
| punaḥ ca | punaḥ ca | and again |
| aṣṭādaśavidhā | aṣṭādaśa-vidhā | eighteenfold |
| sā | sā | she / it, i.e. vedanā |
| manopavicārataḥ | manas-upavicāra-taḥ | by mental approach / mental examination / mental ranging |

## Grammar

```text
tat-jāḥ
    nominative plural feminine
    = born from that, i.e. born from sparśa

ṣaṭ-vedanāḥ
    nominative plural feminine
    = six feelings

pañca kāyikī
    = five are bodily

caitasī parā
    = the other is mental

punaḥ ca aṣṭādaśa-vidhā sā
    = and again, that [vedanā] is eighteenfold

manas-upavicāra-taḥ
    ablative of basis / respect
    = with respect to mental approaches / examinations
```

## Literal Translation

Born from that are six feelings. Five are bodily; the other is mental. Again, that feeling is eighteenfold by way of mental approaches.

## Philosophical Translation

Feeling arises from contact and is first divided into six kinds. Five are bodily feelings, corresponding to the five bodily sense contacts; the remaining one is mental. The same feeling is further classified as eighteenfold according to the modes of mental approach or examination.

## Technical Vocabulary

| Sanskrit | Working translation | Note |
|---|---|---|
| tajjāḥ | born from that | Born from sparśa, contact |
| vedanā | feeling / affective experience | Feeling born from contact |
| ṣaṭ | six | Sixfold according to the six contacts |
| kāyikī | bodily | The first five feelings based on bodily/sense contact |
| caitasī | mental | The sixth, mental feeling |
| parā | the other / remaining one | The one beyond the five bodily feelings |
| aṣṭādaśavidhā | eighteenfold | Further classification of feeling |
| manas | mind | Here as basis of mental approach/examination |
| upavicāra | approach / examination / ranging | Technical term for mental approaches; requires Bhāṣya control |
| manopavicāra | mental approach / mental examination | Basis for the eighteenfold classification |

## Doctrinal Determination

VAkK_3.32 moves from contact to feeling.

```text
sparśa
    ↓
vedanā
```

The verse gives two classifications.

First classification:

```text
six feelings
    born from six contacts
```

Second classification:

```text
five bodily feelings
one mental feeling
```

This preserves the distinction from 3.30:

```text
five resistant / impact contacts
    → five bodily feelings

sixth designation-contact
    → one mental feeling
```

Then the verse adds a further classification:

```text
vedanā
    = eighteenfold
    by manopavicāra
```

The exact scope of `manopavicāra` should be controlled by the Bhāṣya. For now it should be kept as mental approach, mental examination, or mental ranging, not prematurely assimilated to concept.

## Logical Determination

The logical movement is:

```text
contact
    becomes feeling
```

But feeling is not a simple one-place result. It is articulated by the structure of contact.

```text
six contacts
    → six feelings

five bodily contacts
    → five bodily feelings

one mental/designative contact
    → one mental feeling
```

Then feeling becomes more finely differentiated through mental approach:

```text
feeling
    → eighteenfold classification by manopavicāra
```

So the wheel is turning more concretely:

```text
contact-event
    becomes affective registration
        becomes mentally differentiated affective field
```

## Interpretive Note

This verse confirms the doctrinal transition from `sparśa` to `vedanā`.

The important discipline is to keep the terminology initial and exact:

```text
sparśa
    = contact

vedanā
    = feeling / affective experience

kāyikī vedanā
    = bodily feeling

caitasī vedanā
    = mental feeling

manopavicāra
    = mental approach / examination / ranging
```

We should not yet overinterpret mental feeling as full concept. But this is a contact point: mental feeling arises from the sixth contact and is further articulated by mental approaches.

## Organon Interpretation

Speculatively, VAkK_3.32 shows the passage from contact to affective field.

```text
contact
    → feeling
```

And then:

```text
bodily contact
    → bodily feeling

designation-contact / mental contact
    → mental feeling
```

A light Organon contact point:

```text
mental contact
    does not merely receive impact
    it ranges through manopavicāra
```

This may later support a concept-container interpretation, but for now it should remain only a marker.

The safe formulation is:

```text
The sixth contact yields mental feeling, and mental feeling is further differentiated by modes of mental approach.
```

## OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_32
    a vak:Karika ;
    rdfs:label "VAkK 3.32" ;
    vak:continues vak:VAK_3_31 ;
    vak:hasTopic vak:Vedana ;
    vak:statesOrigin vak:VedanaFromSparsa ;
    vak:classifies vak:SixVedanas ;
    vak:classifies vak:BodilyAndMentalVedana ;
    vak:classifies vak:EighteenfoldVedana .

vak:VedanaFromSparsa
    a logic:GenerationRule ;
    rdfs:label "feeling born from contact" ;
    vak:hasSanskrit "tajjāḥ" ;
    logic:from vak:Sparsa ;
    logic:to vak:Vedana .

vak:SixVedanas
    a logic:Classification ;
    rdfs:label "six feelings" ;
    vak:hasMemberCount 6 .

vak:BodilyVedana
    a logic:FeelingType ;
    rdfs:label "kāyikī vedanā" ;
    vak:hasCanonicalTranslation "bodily feeling" ;
    vak:hasMemberCount 5 .

vak:MentalVedana
    a logic:FeelingType ;
    rdfs:label "caitasī vedanā" ;
    vak:hasCanonicalTranslation "mental feeling" ;
    vak:hasMemberCount 1 .

vak:EighteenfoldVedana
    a logic:Classification ;
    rdfs:label "eighteenfold feeling" ;
    vak:hasMemberCount 18 ;
    logic:basedOn vak:Manopavicara .

vak:Manopavicara
    a logic:MentalOperation ;
    rdfs:label "manopavicāra" ;
    vak:hasCanonicalTranslation "mental approach" .
```

## Commit Note

Committed VAK_3b / VAkK_3.32.

Established:
- vedanā is born from sparśa.
- there are six feelings corresponding to six contacts.
- five feelings are bodily and the remaining one is mental.
- vedanā is further classified as eighteenfold by manopavicāra.

Logical determination:
VAkK_3.32 turns the wheel from contact to feeling. Contact becomes affective experience, and affective experience is further differentiated into bodily and mental feeling, then into eighteen modes according to mental approach.
