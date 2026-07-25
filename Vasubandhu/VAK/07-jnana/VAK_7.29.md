# VAK_7.29 — The Remaining Buddha-Powers and Their Knowledge-Range

## Sanskrit

### Devanāgarī

```text
ध्यानाद्यक्षाधिमोक्षेषु धातौ च प्रतिपत्सु तु ।
दश वा संवृतिज्ञानं द्वयोः षट् दश वा क्षये ॥ ७.२९ ॥
```

### IAST

```text
dhyānādyakṣādhimokṣeṣu dhātau ca pratipatsu tu /
daśa vā saṃvṛtijñānaṃ dvayoḥ ṣaṭ daśa vā kṣaye // VAK_7.29 //
```

## Source Caution

VAK 7.28 began the ten powers of a Buddha. VAK 7.29 continues the enumeration.

The carried-forward `nava` from VAK 7.28 governs the powers concerning:

```text
the dhyānas and related attainments
the faculties
the aspirations or resolutions
the dispositions or domains
```

The verse then gives the remaining counts:

```text
paths
    nine or ten knowledges

the two powers of former abodes and death-rebirth
    conventional knowledge

destruction of the cankers
    six or ten knowledges
```

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| dhyāna-ādiṣu | locative plural compound | in the dhyānas and related attainments |
| akṣa | compound member from *indriya* sense | faculties |
| adhimokṣeṣu | locative plural | aspirations, resolutions, inclinations |
| dhātau | locative singular | in dispositions, domains, acquired natures |
| ca | conjunction | and |
| pratipatsu | locative plural | in paths, modes of practice |
| tu | contrastive particle | but, as for |
| daśa vā | numeral + alternative | or ten |
| saṃvṛti-jñānam | nominative/accusative singular neuter | conventional knowledge |
| dvayoḥ | genitive/locative dual | of the two |
| ṣaṭ | numeral | six |
| daśa vā | numeral + alternative | or ten |
| kṣaye | locative singular | in destruction, destruction of the cankers |

## Grammar

The first half continues the ellipsis from VAK 7.28:

```text
nava jñānāni
    nine knowledges

in the powers concerning:
    dhyānas and related attainments
    faculties
    aspirations
    dispositions
```

The second half gives three further determinations:

```text
pratipatsu
    in the paths

nava vā daśa
    nine or ten knowledges

saṃvṛtijñānam dvayoḥ
    conventional knowledge in the two

kṣaye ṣaṭ daśa vā
    in destruction, six or ten knowledges
```

## Literal Translation

There are nine knowledges in the powers concerning the dhyānas and related attainments, the faculties, the aspirations, and the dispositions; in the paths there are nine or ten. The two are conventional knowledge. In destruction there are six or ten knowledges.

## Philosophical Translation

The Buddha’s powers do not all draw upon the same cognitive range. Knowledge concerning meditative states, faculties, aspirations, and dispositions uses nine knowledges. Knowledge of paths may use nine or all ten, depending on whether the result is included with the path. Knowledge of former lives and of death and rebirth is conventional knowledge. Knowledge of the destruction of the cankers may be analyzed narrowly as six knowledges or comprehensively as all ten.

## Technical Vocabulary

### dhyānādi

```text
dhyānādi
    dhyānas
    liberations
    concentrations
    attainments
```

The power concerns the structure, purity, corruption, emergence, and range of contemplative attainments.

### akṣa / indriya

```text
faculties
    capacities of beings
    their relative strength or weakness
```

### adhimokṣa

```text
adhimokṣa
    resolution
    aspiration
    inclination
```

### dhātu

Here *dhātu* is not merely a cosmological element. It concerns the differentiated dispositions or acquired natures of beings.

### pratipad

```text
pratipad
    path
    course of practice
    route leading to a determinate result
```

### kṣaya

```text
kṣaya
    destruction
    exhaustion
    destruction of the cankers
```

## Doctrinal Determination

### Powers three through six

The powers concerning:

```text
meditative attainments
faculties
aspirations
dispositions
```

are each composed of nine knowledges, excluding knowledge of cessation.

### The power concerning paths

```text
path considered without its result
    nine knowledges

path considered together with its result
    ten knowledges
```

The difference depends on whether cessation is included as the result reached by the path.

### The two conventional powers

The powers concerning:

```text
former abodes
death and rebirth
```

are conventional knowledge. They concern extended histories and trajectories of beings rather than pure knowledge directly taking the truths as object.

### The power of destruction

```text
narrow analysis
    six knowledges

comprehensive analysis
    ten knowledges
```

Narrowly, the power is analyzed through the knowledges directly constituting the destruction of the cankers. Broadly, it is the knowledge present in a continuum in which the cankers have been destroyed, and so all ten knowledges may be included.

## Logical Determination

The same accomplished power may be analyzed under different scopes:

```text
restricted scope
    immediate cognitive constituents

extended scope
    full cognitive system in which the power operates
```

The variation in number therefore marks a variation in analytical range, not inconsistency.

## Organon Light

```text
a power is not a bare faculty

it is a determinate range
of knowledges
organized around a function
```

The path-power is especially clear:

```text
path alone
    ninefold range

path together with attained result
    tenfold range
```

The Path is known both as operation and, when taken comprehensively, through the end it realizes.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix buddha: <http://127.0.0.1:3000/buddha#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_7_29
    a vak:Karika ;
    rdfs:label "VAK 7.29" ;
    vak:determines buddha:MeditativeAttainmentPower,
                   buddha:FacultyPower,
                   buddha:AspirationPower,
                   buddha:DispositionPower,
                   buddha:PathPower,
                   buddha:FormerAbodesPower,
                   buddha:DeathRebirthPower,
                   buddha:CankerDestructionPower .

buddha:PathPower
    jna:hasKnowledgeRange jna:NineKnowledges,
                          jna:TenKnowledges .

buddha:FormerAbodesPower
    jna:constitutedBy jna:ConventionalKnowledge .

buddha:DeathRebirthPower
    jna:constitutedBy jna:ConventionalKnowledge .

buddha:CankerDestructionPower
    jna:hasKnowledgeRange jna:SixKnowledges,
                          jna:TenKnowledges .
```

## Commit History

```text
2026-07-23 — Initial kārikā-pass analysis for VAK_7b.
```
