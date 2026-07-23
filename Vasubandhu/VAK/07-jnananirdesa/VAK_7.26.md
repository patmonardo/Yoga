# VAK_7.26 — The Range of Future Cultivation

## Sanskrit

### Devanāgarī

```text
यद्वैराग्याय यल्लाभस्तत्र चाधश्च भाव्यते ।
सास्रवाश्च क्षयज्ञाने लब्धपूर्वं न भाव्यते ॥ ७.२६ ॥
```

### IAST

```text
yadvairāgyāya yallābhas tatra cādhaś ca bhāvyate /
sāsravāś ca kṣayajñāne labdhapūrvaṃ na bhāvyate // VAK_7.26 //
```

## Source Caution

This verse does not introduce a new list of knowledges. It limits the **range** within which future cultivation occurs.

The received explanation is:

```text
future cultivation belongs to
    the level from which detachment is being gained
    the level newly acquired
    or a lower level

at knowledge of destruction
    impure knowledges of the relevant levels are also cultivated

what was already acquired before
    is not counted as newly cultivated
```

The phrase concerning *sāsrava* is compressed and should be read with the bhāṣya. The main point is that cultivation is ordered by the practitioner's actual transition between levels, not by an indiscriminate activation of all possible knowledges.

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| yat | relative pronoun | whichever; whatever |
| vairāgyāya | dative singular | for detachment; toward freedom from attachment |
| yat | relative pronoun | whichever |
| lābhaḥ | nominative singular | acquisition, attainment |
| tatra | adverb | there; at that level |
| ca | conjunction | and |
| adhaḥ | adverb | below; at lower levels |
| ca | conjunction | and |
| bhāvyate | passive present | is cultivated |
| sāsravāḥ | nominative plural | impure, contaminated knowledges |
| ca | conjunction | also |
| kṣaya-jñāne | locative singular | at knowledge of destruction |
| labdha-pūrvam | adverbial compound | previously acquired |
| na | negation | not |
| bhāvyate | passive present | is cultivated |

## Grammar

The first half uses a relative-correlative structure:

```text
yat ... yat ... tatra
    whatever acquisition is made
    for detachment from a given level
    there and below cultivation occurs
```

The second half adds two qualifications:

```text
at knowledge of destruction
    impure knowledges are also cultivated

but
    what has already been acquired
    is not cultivated anew
```

## Literal Translation

Whatever attainment is made for the sake of detachment, cultivation takes place there and below. At knowledge of destruction, impure knowledges are also cultivated; what has previously been acquired is not cultivated.

## Philosophical Translation

Cultivation follows the actual path-transition. When detachment from a level is attained, future cognitive capacities are established at that level and at levels beneath it. At the moment of knowledge of destruction, the cultivation-range also includes the relevant impure knowledges. Yet a capacity already secured earlier is not counted as a fresh acquisition.

## Technical Vocabulary

### vairāgya

```text
vairāgya
    detachment
    freedom from attachment to a level
    the condition enabling transition beyond it
```

Here *vairāgya* is path-functional. It marks the release that permits movement from one meditative level to another.

### lābha

```text
lābha
    acquisition
    attainment
    incorporation into the practitioner's continuum
```

The verse concerns which capacities are acquired in relation to that attainment.

### adhaḥ

```text
adhaḥ
    below
    lower levels already included within the practitioner's mastery
```

Cultivation extends downward because the newly attained higher position does not exclude capacities belonging to levels beneath it.

### labdhapūrvam

```text
labdhapūrvam
    previously acquired
```

This prevents double counting. Path calculus distinguishes:

```text
capacity already possessed
    from
capacity newly cultivated now
```

## Doctrinal Determination

### Cultivation follows the path-transition

The verse establishes a directional rule:

```text
detachment from a level
    ↓
acquisition connected with that level
    ↓
cultivation there and below
```

The path does not cultivate every possible cognition at every moment. Its range is determined by the level currently being relinquished and the level being entered.

### Downward inclusion

A higher attainment includes cultivation at lower relevant levels:

```text
newly reached level
    +
levels beneath it
```

This does not mean regression. It means that lower capacities remain available within a more advanced attainment.

### No double counting

The closing rule is simple:

```text
previously acquired
    ≠
newly cultivated
```

The path-register therefore tracks genuine additions and present activations rather than merely listing everything the practitioner possesses.

## Logical Determination

VAK 7.26 introduces three distinct coordinates:

```text
level from which detachment occurs
level newly acquired
lower levels included beneath it
```

Cultivation is thus **range-sensitive**.

It also distinguishes two temporal statuses:

```text
already acquired
newly cultivated
```

That distinction is indispensable for readable Path Calculus. Without it, possession, activation, and new acquisition would collapse into one undifferentiated count.

## Organon Light

The basic determination is:

```text
an advance of the Path
    reorganizes a definite range of capacities

it does not recreate
    every capacity already possessed
```

The higher state includes lower powers while adding only what is genuinely new.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix marga: <http://127.0.0.1:3000/marga#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_7_26
    a vak:Karika ;
    rdfs:label "VAK 7.26" ;
    vak:determines jna:CultivationRange,
                   jna:PreviouslyAcquiredExclusion .

jna:CultivationRange
    a jna:PathCultivationRule ;
    jna:conditionedBy marga:DetachmentTransition ;
    jna:includes jna:CurrentLevel,
                 jna:LowerLevels .

jna:PreviouslyAcquiredExclusion
    a jna:CountingRule ;
    jna:excludes jna:AlreadyAcquiredCapacity .
```

## Commit History

```text
2026-07-23 — Initial kārikā-pass analysis for VAK_7b.
```
