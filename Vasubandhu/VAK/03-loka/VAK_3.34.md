# VAK_3b — VAkK_3.34

## Sanskrit — Devanāgarī

स्वोऽष्टालम्बनमारूप्यो द्वयोर्ध्यानद्वये तु षट् ।
कामाः षण्णां चतुर्णां स्वः एकस्यालम्बनं परः ॥ VAkK_3.34 ॥

## Sanskrit — IAST

svo 'ṣṭālambanam ārūpyo dvayoḥ dhyānadvaye tu ṣaṭ /
kāmāḥ ṣaṇṇāṃ caturṇā svaḥ ekasyālambanaṃ paraḥ // VAkK_3.34 //

## Source Caution

The source reads:

```text
svo 'ṣṭālambanam ārūpyo dvayoḥ dhyānadvaye tu ṣaṭ /
kāmāḥ ṣaṇṇāṃ caturṇā svaḥ ekasyālambanaṃ paraḥ // VAkK_3.34 //
```

This continues the technical distribution of the eighteen `manopavicāras`. The exact enumeration should remain provisional until controlled by the Bhāṣya.

## Padaccheda

| Sandhi form | Padaccheda | Basic meaning |
|---|---|---|
| svaḥ / svo | svaḥ | own; pertaining to its own field |
| aṣṭālambanam | aṣṭa-ālambanam | having eight object-supports |
| ārūpyaḥ | ārūpyaḥ | belonging to the formless realm |
| dvayoḥ | dvayoḥ | of the two |
| dhyānadvaye | dhyāna-dvaye | in the pair of dhyānas |
| tu | tu | but; however |
| ṣaṭ | ṣaṭ | six |
| kāmāḥ | kāmāḥ | desire-realm ones / desire-directed ones |
| ṣaṇṇām | ṣaṇṇām | of six |
| caturṇām | caturṇām | of four |
| svaḥ | svaḥ | own |
| ekasya | ekasya | of one |
| ālambanam | ālambanam | object-support |
| paraḥ | paraḥ | another / higher / other |

## Grammar

```text
svaḥ aṣṭa-ālambanam ārūpyaḥ
    = the formless one has eight object-supports of its own / its own eight-support range

dvayoḥ dhyāna-dvaye tu ṣaṭ kāmāḥ
    = but in the pair of dhyānas, six are desire-related / desire-directed

ṣaṇṇām caturṇām svaḥ
    = of six, four are own

ekasya ālambanam paraḥ
    = for one, the object-support is other / higher
```

The syntax is compact and should be treated as mapping-language rather than ordinary prose.

## Literal Translation

The formless one has its own eight object-supports. But in the pair of dhyānas, six are desire-related. Of six, four are own; for one, the object-support is other.

## Philosophical Translation

The distribution of the mental approaches continues: in the formless context the range is restricted to eight object-supports. In the relevant pair of dhyānas, six are connected with the desire realm. Within the remaining enumeration, some have their own object-supports while one has another or higher object-support. The exact mapping is technical and must be checked against the Bhāṣya.

## Technical Vocabulary

| Sanskrit | Working translation | Note |
|---|---|---|
| sva | own | Own field / own support / own domain |
| ālambana | object-support | The support on which cognition or mental approach depends |
| aṣṭālambana | eight object-supports | Restricted range in the formless context |
| ārūpya | formless realm | Arūpya-dhātu or formless sphere |
| dhyāna | meditation-level / absorption | Here used as a field of distribution |
| dhyānadvaya | pair of dhyānas | Two dhyāna-levels under consideration |
| kāma | desire realm / desire-related | Kāma-dhātu or desire-directed support |
| para | other / higher | Other-field or higher support; requires Bhāṣya control |

## Doctrinal Determination

VAkK_3.33 began the realm-distribution of the eighteen mental approaches.

VAkK_3.34 continues that distribution, now including the formless field and further dhyāna distinctions.

The stable doctrinal point is:

```text
manopavicāra
    is distributed by field
    and by ālambana
```

The verse uses numerical restrictions:

```text
ārūpya
    → eight object-supports

dhyāna-pair
    → six desire-related supports

further distribution
    → own supports and another / higher support
```

This is not a speculative psychology. It is an Abhidharma map of which mental approaches can operate with which supports in which realm or meditative field.

## Logical Determination

The logical point continues from 3.33:

```text
mental approach
    is field-bound
    support-bound
    range-limited
```

So the wheel of human experience is not an unbounded subject moving through objects. It is a structured distribution of contact, feeling, and mental approach according to domain.

```text
realm / dhyāna-field
    determines possible ālambanas

possible ālambanas
    determine the range of manopavicāra
```

Thus the middle as concrete experience is governed by support-structure.

## Interpretive Note

This verse is one of the places where we must avoid over-speculation.

The important contact point is not yet Concept, Hypothetical, or container in a full Organon sense. The important Abhidharma point is more precise:

```text
Mental approach is limited by field and support.
```

So our initial terminology should remain:

```text
ālambana
    = object-support

gocara
    = field / range

dhyāna / dhātu
    = operating field

manopavicāra
    = mental approach / mental ranging
```

## Organon Interpretation

A light Organon contact point:

```text
A mental operation does not float freely.
It rises and falls with the field and support that make it possible.
```

But this must remain subordinate to the doctrinal mapping. The Abhidharma system is currently giving us a constrained topology of experience:

```text
field
    → support-range
        → possible mental approach
```

This belongs to the first part of Lokanirdeśa as the world of human conditioned experience.

## OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_34
    a vak:Karika ;
    rdfs:label "VAkK 3.34" ;
    vak:continues vak:VAK_3_33 ;
    vak:hasTopic vak:Manopavicara ;
    vak:distributes vak:EighteenfoldManopavicara ;
    vak:hasContext vak:ArupyaField ;
    vak:hasContext vak:DhyanaField ;
    vak:usesSupport vak:Alambana .

vak:ArupyaField
    a logic:OperatingField ;
    rdfs:label "ārūpya field" ;
    vak:hasCanonicalTranslation "formless field" .

vak:EightAlambanaRange
    a logic:SupportRange ;
    rdfs:label "eight-object-support range" ;
    vak:hasMemberCount 8 ;
    logic:inField vak:ArupyaField .

vak:DhyanaPairDistribution
    a logic:Distribution ;
    rdfs:label "dhyāna-pair distribution" ;
    vak:hasSanskrit "dhyānadvaye" .

vak:Alambana
    a logic:ObjectSupport ;
    rdfs:label "ālambana" ;
    vak:hasCanonicalTranslation "object-support" .
```

## Commit Note

Committed VAK_3b / VAkK_3.34.

Established:
- the technical distribution of manopavicāra continues from 3.33.
- the formless field is associated with an eight-object-support range.
- the dhyāna-pair distribution includes six desire-related supports.
- the exact enumeration remains provisional pending Bhāṣya control.

Logical determination:
VAkK_3.34 reinforces that mental approach is field-bound, support-bound, and range-limited. The world of human conditioned experience is structured by possible supports within specific dhātu/dhyāna fields.
