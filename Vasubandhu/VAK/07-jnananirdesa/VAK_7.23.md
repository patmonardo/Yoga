# VAK_7.23 — Occasions for the Cultivation of Seven Knowledges

## Sanskrit

### Devanāgarī

```text
सप्तभूमिजयाभिज्ञाकोप्याप्त्याकीर्णभाविते ।
आनन्तर्यपथेषूर्ध्वं मुक्तिमार्गाष्टकेऽपि च ॥ ७.२३ ॥
```

### IAST

```text
saptabhūmijayābhijñākopyāptyākīrṇabhāvite /
ānantaryapatheṣūrdhvaṃ muktimārgāṣṭake 'pi ca // VAK_7.23 //
```

## Source Caution

This verse continues the cultivation count from VAK 7.22.

Its syntax is highly compressed. It enumerates further occasions on which seven knowledges are cultivated. The detailed distribution is controlled by the bhāṣya, but the kārikā-level structure is clear:

```text
seven knowledges are cultivated
    at the conquest of seven stages
    at the acquisition of the superknowledges
    at the acquisition of immovability
    in mixed cultivation
    in higher uninterrupted paths
    and in eight liberation paths
```

The verse is therefore primarily classificatory. It lists path-events rather than introducing a new type of knowledge.

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| sapta-bhūmi-jaya | compound | conquest of seven stages |
| abhijñā | feminine noun, compound member | superknowledge, direct higher knowledge |
| akopya-āpti | compound | acquisition of the immovable state |
| ākīrṇa-bhāvite | locative singular compound | in mixed cultivation; when mixed cultivation is developed |
| ānantarya-patheṣu | locative plural | in uninterrupted paths |
| ūrdhvam | indeclinable | above; in the higher stages |
| mukti-mārga-aṣṭake | locative singular compound | in the group of eight liberation paths |
| api | indeclinable | also |
| ca | conjunction | and |

## Grammar

The verse supplies a series of locative occasions governed by the cultivation count inherited from VAK 7.22:

```text
seven knowledges are cultivated
    sapta-bhūmi-jaye
    abhijñā-āptau
    akopya-āptau
    ākīrṇa-bhāvite
    ūrdhvam ānantarya-patheṣu
    mukti-mārga-aṣṭake api
```

Several case endings are compressed through compounding. The meaning is distributive: the same sevenfold cultivation applies at each listed occasion.

## Literal Translation

At the conquest of the seven stages, at the acquisition of the superknowledges, at the acquisition of immovability, in mixed cultivation, in the higher uninterrupted paths, and also in the group of eight liberation paths, seven knowledges are cultivated.

## Philosophical Translation

Seven knowledges are cultivated at a determinate series of advanced path-events: the overcoming of seven stages, the acquisition of higher knowledges, the attainment of immovability, mixed cultivation, the higher uninterrupted paths, and eight liberation paths.

## Technical Vocabulary

### sapta-bhūmi-jaya

```text
sapta-bhūmi-jaya
    conquest of seven stages
```

This refers to the overcoming or mastery of seven meditative levels through the path. The verse is concerned with the cultivation count accompanying that conquest.

### abhijñā

```text
abhijñā
    superknowledge
    direct higher knowledge
```

The acquisition of such knowledge is treated as a specific path-event at which seven knowledges are cultivated.

### akopya-āpti

```text
akopya
    immovable
    no longer subject to falling away

āpti
    acquisition
    attainment
```

The phrase marks attainment of the immovable type of arhatship.

### ākīrṇa-bhāvanā

```text
ākīrṇa-bhāvanā
    mixed cultivation
```

At this level of the first pass, the term should be retained as a technical designation. Its detailed procedure belongs to the bhāṣya pass.

### ānantarya-mārga

```text
ānantarya-mārga
    uninterrupted path
```

This is the path-moment directly removing an obstruction. VAK 7.23 specifies the higher uninterrupted paths.

### mukti-mārga

```text
mukti-mārga
    path of liberation
```

This is the path-moment immediately following the uninterrupted path, in which the removal is possessed as accomplished.

## Doctrinal Determination

### The common count

The verse preserves the number established in the preceding discussion:

```text
seven knowledges cultivated
```

It then extends that count across several advanced occasions.

### Enumerated occasions

| Occasion | Immediate determination |
|---|---|
| conquest of seven stages | seven knowledges cultivated |
| acquisition of superknowledges | seven knowledges cultivated |
| acquisition of immovability | seven knowledges cultivated |
| mixed cultivation | seven knowledges cultivated |
| higher uninterrupted paths | seven knowledges cultivated |
| eight liberation paths | seven knowledges cultivated |

### No new knowledge-class

VAK 7.23 does not add an eleventh knowledge or revise the tenfold classification.

It answers a narrower question:

```text
At which advanced path-events
is the sevenfold cultivation found?
```

The answer is supplied by enumeration.

### Uninterrupted and liberation paths

The verse again preserves the functional pair:

```text
uninterrupted path
    direct removal of an obstruction

liberation path
    possession of the accomplished removal
```

The cultivation count is attached to both, though VAK 7.24 will refine the exceptional cases.

## Logical Determination

The verse organizes advanced practice through a stable rule:

```text
one cultivation count
    applied across
multiple determinate path-events
```

The important structural feature is not speculation about the experiences themselves, but the repeatable classification:

```text
path-event
    +
practitioner's attainment
    →
number of knowledges cultivated
```

VAK 7.23 therefore expands the cultivation map without changing its basic categories.

## Organon Light

Basic setting:

```text
The same cognitive equipment
can be cultivated
at several different operations
of the path.
```

The verse classifies the operations; it does not yet explain their deeper unity.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix marga: <http://127.0.0.1:3000/marga#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_7_23
    a vak:Karika ;
    rdfs:label "VAK 7.23" ;
    vak:determines jna:SevenKnowledgeCultivation,
                   marga:AdvancedCultivationOccasions .

jna:SevenKnowledgeCultivation
    a jna:CultivationCount ;
    jna:count 7 .

marga:AdvancedCultivationOccasions
    a marga:PathEventSet ;
    marga:includes marga:SevenStageConquest,
                   marga:SuperknowledgeAcquisition,
                   marga:ImmovabilityAcquisition,
                   marga:MixedCultivation,
                   marga:HigherUninterruptedPath,
                   marga:EightLiberationPaths .
```

## Commit History

```text
2026-07-23 — Initial kārikā-pass analysis for VAK_7b.
```