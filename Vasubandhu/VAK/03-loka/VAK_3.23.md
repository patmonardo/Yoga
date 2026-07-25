# VAK_3b — VAkK_3.23

## Sanskrit — Devanāgarī

वित्तिः प्राक् मैथुनात् तृष्णा भोगमैथुनरागिणः ।
उपादानं तु भोगानां प्राप्तये परिधावतः ॥ VAkK_3.23 ॥

## Sanskrit — IAST

vittiḥ prāk maithunāt tṛṣṇā bhogamaithunarāgiṇaḥ /
upādānaṃ tu bhogānāṃ prāptaye paridhāvataḥ // VAkK_3.23 //

## Working Caution

The source reads **vittiḥ**, not the more expected doctrinal label **vedanā**. For the standard twelvefold sequence, this position corresponds to feeling/affective experience, but the file preserves the Sanskrit source form as `vittiḥ`.

## Padaccheda

| Sandhi form | Padaccheda | Basic meaning |
|---|---|---|
| vittiḥ | vittiḥ | experience / feeling / affective registering |
| prāk | prāk | before; prior to |
| maithunāt | maithunāt | before sexual intercourse / coupling |
| tṛṣṇā | tṛṣṇā | thirst; craving |
| bhogamaithunarāgiṇaḥ | bhoga-maithuna-rāgiṇaḥ | of one attached to enjoyment and sexual intercourse |
| upādānam | upādānam | appropriation; grasping; clinging |
| tu | tu | but; now |
| bhogānām | bhogānām | of enjoyments |
| prāptaye | prāptaye | for obtaining; for acquisition |
| paridhāvataḥ | paridhāvataḥ | of one running about; pursuing |

## Grammar

```text
vittiḥ
    nominative singular feminine
    = affective experiencing / feeling-position

prāk maithunāt
    prāk + ablative
    = before sexual intercourse

tṛṣṇā
    nominative singular feminine
    = craving / thirst

bhoga-maithuna-rāgiṇaḥ
    genitive singular
    = of one attached to enjoyment and intercourse

upādānam
    nominative singular neuter
    = appropriation / grasping

bhogānām prāptaye
    genitive plural + dative singular
    = for the acquisition of enjoyments

paridhāvataḥ
    genitive singular participial form
    = of one running after / pursuing
```

## Literal Translation

Affective experience is before sexual intercourse. Craving belongs to one attached to enjoyment and intercourse. Appropriation, however, belongs to one running after the acquisition of enjoyments.

## Philosophical Translation

Feeling or affective experience occupies the stage before sexual coupling. Craving appears in the one who is attached to enjoyment and intercourse. Appropriation is the intensified pursuit in which one runs after the acquisition of enjoyments.

## Technical Vocabulary

| Sanskrit | Working translation | Note |
|---|---|---|
| vittiḥ | affective experience / feeling | Preserved as source form; doctrinally corresponds to vedanā-position |
| maithuna | sexual intercourse / coupling | Marks a developmental threshold |
| tṛṣṇā | craving / thirst | The affective movement of desire |
| bhoga | enjoyment | Object of pursuit and consumption |
| rāga | attachment / passion | Affective fixation |
| upādāna | appropriation / grasping | Craving intensified into taking-up |
| prāpti | acquisition / obtaining | The aim of pursuit |
| paridhāvataḥ | running after / pursuing | Active pursuit of enjoyment |

## Doctrinal Determination

VAkK_3.23 continues the middle section of dependent co-arising.

It gives the next two limbs explicitly:

```text
7. vittiḥ / vedanā-position
8. tṛṣṇā
9. upādāna
```

The verse presents them developmentally rather than abstractly:

```text
vittiḥ
    before sexual coupling

tṛṣṇā
    of one attached to enjoyment and coupling

upādāna
    of one running after the acquisition of enjoyments
```

So the movement is:

```text
contact
    ↓
affective experience
    ↓
craving
    ↓
appropriative pursuit
```

## Logical Determination

The verse shows the transition from passive affectivity to active pursuit.

```text
vittiḥ
    = affective registration

tṛṣṇā
    = desire awakened by attachment

upādāna
    = desire hardened into appropriation
```

The logical movement is:

```text
being affected
    becomes craving
        becomes grasping pursuit
```

This is the intensification of the middle section. Contact does not remain neutral. It becomes affectively marked, then desirous, then appropriative.

## Interpretive Note

This verse should be kept close to the Sanskrit. It is not yet a metaphysical theory of subjectivity. It is a developmental account of how affect becomes craving and how craving becomes pursuit.

The key danger is translating too quickly into a modern psychological vocabulary. The verse is more precise: it names stages by their thresholds and dominant functions.

## Organon Interpretation

Speculatively, this gives the transition from interface-contact to motivated action.

```text
sparśa
    = contact event

vittiḥ
    = affective registration

tṛṣṇā
    = desire-vector

upādāna
    = appropriative capture / pursuit
```

In Organon terms, the system begins to move from reception to drive:

```text
interface contact
    ↓
affective mark
    ↓
desire-orientation
    ↓
acquisitive pursuit
```

This remains a hypothesis until checked against the Bhāṣya.

## OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_23
    a vak:Karika ;
    rdfs:label "VAkK 3.23" ;
    vak:continues vak:VAK_3_22 ;
    vak:hasTopic vak:DependentCoArising ;
    vak:explicatesLimb vak:Vitti ;
    vak:explicatesLimb vak:Trsna ;
    vak:explicatesLimb vak:Upadana .

vak:Vitti
    a vak:DependentCoArisingLimb ;
    rdfs:label "vittiḥ" ;
    vak:hasCanonicalTranslation "affective experience" ;
    vak:belongsToSection vak:MadhyaSection ;
    logic:follows vak:Sparsa ;
    logic:precedes vak:Trsna .

vak:Trsna
    a vak:DependentCoArisingLimb ;
    rdfs:label "tṛṣṇā" ;
    vak:hasCanonicalTranslation "craving" ;
    vak:belongsToSection vak:MadhyaSection ;
    logic:follows vak:Vitti ;
    logic:precedes vak:Upadana .

vak:Upadana
    a vak:DependentCoArisingLimb ;
    rdfs:label "upādāna" ;
    vak:hasCanonicalTranslation "appropriation" ;
    vak:belongsToSection vak:MadhyaSection ;
    logic:follows vak:Trsna .
```

## Commit Note

Committed VAK_3b / VAkK_3.23.

Established:
- vittiḥ is preserved as the source reading.
- vittiḥ marks the affective/feeling position before sexual coupling.
- tṛṣṇā belongs to one attached to enjoyment and coupling.
- upādāna belongs to one pursuing acquisition of enjoyments.

Logical determination:
VAkK_3.23 shows the transition from affective registration to craving, and from craving to appropriative pursuit.
