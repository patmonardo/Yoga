# VAK_7.24 — Sharpening the Faculties and the Sixfold Cultivation

## Sanskrit

### Devanāgarī

```text
शैक्षोत्तापनमुक्तौ वा षट् सप्तज्ञानभावना ।
आनन्तर्यपथे षण्णां भवाग्रविजये तथा ॥ ७.२४ ॥
```

### IAST

```text
śaikṣottāpanamuktau vā ṣaṭ saptajñānabhāvanā /
ānantaryapathe ṣaṇṇāṃ bhavāgravijaye tathā // VAK_7.24 //
```

## Source Caution

This verse continues the path-calculus of VAK 7.22–7.23.

Its focus is not a new knowledge, but the number of knowledges cultivated during:

```text
sharpening the faculties of a trainee
    in the liberation path
    and
    in the uninterrupted path

and during
    victory over the peak of existence
```

The bhāṣya clarifies that *uttāpana* means bringing the faculties to a stronger or sharper condition.

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| śaikṣa | adjective/noun | trainee; one still under training |
| uttāpana | action noun | intensification, sharpening, perfecting |
| muktau | locative singular of *mukti* | in the liberation path |
| vā | particle | or; alternatively |
| ṣaṭ | numeral | six |
| sapta | numeral | seven |
| jñāna-bhāvanā | compound | cultivation of knowledges |
| ānantarya-pathe | locative singular compound | in the uninterrupted path |
| ṣaṇṇām | genitive plural | of six |
| bhavāgra-vijaye | locative singular compound | in the conquest of the peak of existence |
| tathā | indeclinable | likewise |

## Grammar

The first half is construed:

```text
śaikṣa-uttāpana-muktau
    in the liberation path
    belonging to the sharpening
    of a trainee's faculties

ṣaṭ sapta jñāna-bhāvanā
    cultivation of six or seven knowledges
```

The second half supplies the contrasting count:

```text
ānantarya-pathe
    in the uninterrupted path

ṣaṇṇām
    of six knowledges

bhavāgra-vijaye tathā
    likewise in the conquest
    of the peak of existence
```

## Literal Translation

In the liberation path of sharpening the faculties of a trainee, six or seven knowledges are cultivated. In the uninterrupted path, six are cultivated; likewise in the conquest of the peak of existence.

## Philosophical Translation

When a trainee strengthens the cognitive faculties, the liberation phase cultivates either six or seven knowledges according to the trainee's prior detachment. The preceding uninterrupted phase cultivates six. The same sixfold cultivation applies in the path that overcomes the highest conditioned level.

## Technical Vocabulary

### śaikṣa

```text
śaikṣa
    one under training
    one whose path is not yet complete
```

The verse concerns a practitioner whose faculties can still be intensified.

### uttāpana

```text
uttāpana
    raising to a stronger grade
    sharpening
    intensification of the faculties
```

This is not the acquisition of an entirely different path. It is the strengthening of the practitioner's capacity within the path already attained.

### mukti-mārga

```text
liberation path
    confirms and possesses
    the release produced
    by the preceding uninterrupted path
```

### ānantarya-mārga

```text
uninterrupted path
    directly opposes
    and removes
    the targeted obstruction
```

### bhavāgra

```text
bhavāgra
    peak of existence
    highest conditioned level
```

Its conquest is the final victory over the uppermost level of conditioned existence.

## Doctrinal Determination

### Liberation path: six or seven

For the trainee whose faculties are being sharpened:

```text
if desire remains
    six knowledges are cultivated

if detached from desire
    seven knowledges are cultivated
```

The seventh is knowledge of another mind.

The six are:

```text
knowledge of dharmas
inferential knowledge
knowledge of suffering
knowledge of origin
knowledge of cessation
knowledge of the path
```

### Uninterrupted path: six

In the uninterrupted path of sharpening the faculties:

```text
six knowledges are cultivated
```

Knowledge of another mind is excluded because it does not function as the direct opposition to the obstruction being removed.

### Victory over the peak of existence

The same sixfold count applies in the uninterrupted path that conquers *bhavāgra*.

Thus the verse gives a simple rule:

| Path-event | Knowledges cultivated |
|---|---:|
| liberation path of sharpening, desire remaining | 6 |
| liberation path of sharpening, detached from desire | 7 |
| uninterrupted path of sharpening | 6 |
| uninterrupted victory over bhavāgra | 6 |

## Logical Determination

The verse distinguishes two functions of the path:

```text
uninterrupted path
    removes the obstruction

liberation path
    stabilizes and possesses
    the release obtained
```

The cultivation count is therefore not arbitrary.

```text
what directly opposes the obstruction
    belongs to the uninterrupted phase

what becomes available after release
    may widen in the liberation phase
```

The six/seven distinction reflects the practitioner's attained range, not a change in the truth being realized.

## Organon Light

At the basic setting:

```text
the path does not merely move forward

it can also sharpen
its own power of knowing
```

VAK 7.24 therefore adds a readable movement to the calculus:

```text
remove
    ↓
release
    ↓
strengthen the faculty
    ↓
expand the available range of knowledge
```

The verse remains a technical count, but the living process is the intensification of an already established path-capacity.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix marga: <http://127.0.0.1:3000/marga#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_7_24
    a vak:Karika ;
    rdfs:label "VAK 7.24" ;
    vak:determines jna:FacultySharpeningCultivation,
                   jna:SixOrSevenKnowledgeCultivation,
                   marga:BhavagraConquest .

jna:FacultySharpeningCultivation
    a jna:KnowledgeDevelopment ;
    jna:occursFor marga:Trainee ;
    jna:hasPhase marga:UninterruptedPath,
                 marga:LiberationPath .

jna:SixOrSevenKnowledgeCultivation
    a jna:CultivationCount ;
    jna:dependsOn marga:PriorDetachment .

marga:BhavagraConquest
    a marga:HighestConditionedVictory ;
    jna:cultivatesCount 6 .
```

## Commit History

```text
2026-07-23 — Initial kārikā-pass analysis for VAK_7b.
```
