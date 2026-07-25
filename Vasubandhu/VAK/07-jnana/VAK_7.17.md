# VAK_7.17 — The Knowledges as Objects of Knowledge

## Sanskrit

### Devanāgarī

```text
नव मार्गान्वयधियोः दुःखहेतुधियोर्द्वयम् ।
चतुर्णां दश नैकस्य योज्या धर्माः पुनर्दश ॥ ७.१७ ॥
```

### IAST

```text
nava mārgānvayadhiyoḥ duḥkhahetudhiyor dvayam /
caturṇāṃ daśa naikasya yojyā dharmāḥ punar daśa // VAK_7.17 //
```

## Source Caution

The verse continues the table begun at the end of VAK 7.16, where the ten knowledges are considered not only as cognitions but also as possible objects of other knowledges.

The kārikā gives compressed numerical assignments. The exact one-to-one distribution of the final clauses among the remaining knowledges belongs to the bhāṣya. This first pass therefore preserves the numerical architecture without forcing an allocation beyond what the verse itself states securely.

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| nava | nominative/accusative plural neuter | nine |
| mārga-anvaya-dhiyoḥ | genitive dual | of path-knowledge and inferential knowledge |
| duḥkha-hetu-dhiyoḥ | genitive dual | of knowledge of suffering and knowledge of origin |
| dvayam | nominative/accusative singular neuter | two |
| caturṇām | genitive plural | of four |
| daśa | nominative/accusative plural neuter | ten |
| na | negation | not; none |
| ekasya | genitive singular | of one |
| yojyāḥ | gerundive, nominative plural | to be connected, assigned, combined |
| dharmāḥ | nominative plural | dharmas |
| punaḥ | indeclinable | again; in turn |
| daśa | nominative plural | ten |

## Grammar

The governing relation is inherited from VAK 7.16:

```text
X knowledges
    are objects of
Y knowledge
```

The verse then distributes numerical object-ranges:

```text
nine
    for path-knowledge and inferential knowledge

two
    for knowledge of suffering and knowledge of origin

ten
    for four knowledges

none
    for one knowledge
```

The final clause, `yojyā dharmāḥ punar daśa`, introduces a second reckoning: the object-field itself is to be articulated as ten dharmic classes. VAK 7.18 immediately specifies those classes.

## Literal Translation

Nine are the objects of path-knowledge and inferential knowledge; two are the objects of knowledge of suffering and knowledge of origin; ten are the objects of four; none are the objects of one. Again, the dharmas to be assigned are ten.

## Philosophical Translation

The ten knowledges differ not only by their own constitution, support, aspect, and sphere, but also by which other knowledges they can take as objects. Their reflexive reach is therefore numerically bounded. The total object-field is then reorganized into ten classes of dharmas.

## Technical Vocabulary

### gocara and object-range

The present verse continues the `gocara` analysis implicitly:

```text
knowledge
    has an object-range

knowledge itself
    may become an object
    within another knowledge's range
```

Thus cognition is reflexively structured, but not without limit.

### yojya

```text
yojya
    = to be connected
    = to be assigned
    = to be systematically distributed
```

The verb is important. The ten dharmas are not merely listed; they must be fitted into a determinate scheme.

## Doctrinal Determination

The verse gives four numerical relations:

| Knowledge standpoint | Number of knowledges available as objects |
|---|---:|
| path-knowledge | 9 |
| inferential knowledge | 9 |
| knowledge of suffering | 2 |
| knowledge of origin | 2 |
| four further knowledges | 10 |
| one further knowledge | 0 |

The exact identity of the four and the one is compressed here and should be distributed from the bhāṣya in a later close pass.

The doctrinal point is already secure:

> A knowledge is partly determined by the range of knowledges that can become its objects.

This means that reflexivity is itself differentiated.

```text
some knowledge
    can know nearly the whole field

some knowledge
    can know only a restricted pair

some knowledge
    can know the full ten

one knowledge
    takes none of the ten knowledges as object
```

## Logical Determination

VAK 7.17 is a table of **relative reflection**.

Each cognition is located by a relation:

```text
this knowledge
    can take these knowledges
    as its objects
```

The relation is neither universal nor symmetrical.

```text
A may know B
    without B knowing A

one standpoint may cover nine
    another only two
```

So the field of knowledge has a directed structure rather than a flat set of mutually transparent terms.

This is still Facticity:

```text
marks of conditioned cognition
    object-range
    reflexive reach
    numerical limit
    possible relation
    impossible relation
```

The verse does not yet derive why every relation must arise. It records the determinate conditions under which one cognition can become a fact for another.

## Organon Light

The immediate Organon significance is exact:

```text
Relative Reflection
    given this cognitive standpoint
    which determinations can become facts for it?

Absolute Reflection
    what makes those possibilities,
    necessities,
    and exclusions follow from the whole?
```

VAK 7.17 remains on the first side. It gives a matrix of possible object-relations.

This is already stronger than next-token prediction:

```text
not:
    what symbol follows?

but:
    given this standpoint,
    which fact can enter its object-field?
```

The final clause prepares a new move. The field of possible facts will now be reorganized into ten dharmic classes. VAK 7.18 should therefore clarify what the objects themselves are, not merely how many knowledges can know them.

No claim about Absolute Reflection or Dharma Megha is imposed in this first pass.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_7_17
    a vak:Karika ;
    rdfs:label "VAK 7.17" ;
    vak:determines jna:KnowledgeAsObjectMatrix,
                   jna:NinefoldObjectRange,
                   jna:TwofoldObjectRange,
                   jna:TenfoldObjectRange,
                   jna:ZeroObjectRange,
                   jna:TenfoldDharmaObjectField .

jna:KnowledgeAsObjectMatrix
    a jna:ReflectiveRelationStructure ;
    jna:specifies jna:PossibleCognitiveObjectRelation,
                  jna:ImpossibleCognitiveObjectRelation .
```

## Commit History

```text
2026-07-23 — Initial kārikā-pass analysis.
```
