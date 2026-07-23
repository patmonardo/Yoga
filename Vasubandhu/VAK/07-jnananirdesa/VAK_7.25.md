# VAK_7.25 — Nine, Ten, or Eight Knowledges Cultivated

## Sanskrit

### Devanāgarī

```text
नवानां तु क्षयज्ञाने अकोप्यस्य दश भावना ।
तत्संचरेऽन्त्यमुक्तौ च प्रोक्तशेषेऽष्टभावना ॥ ७.२५ ॥
```

### IAST

```text
navānāṃ tu kṣayajñāne akopyasya daśa bhāvanā /
tatsaṃcare 'ntyamuktau ca proktaśeṣe 'ṣṭabhāvanā // VAK_7.25 //
```

## Source Caution

The verse continues the numerical path-calculus of VAK 7.22–7.24. Its concern is not the definition of new knowledges, but the number cultivated at decisive terminal or transitional moments.

The working reading is:

```text
at knowledge of destruction
    nine knowledges are cultivated

for the immovable one
    ten are cultivated

at the final liberation path
    in the transition to immovability
        ten are cultivated

in the remaining cases already discussed
    eight are cultivated
```

The phrase *tatsaṃcare 'ntyamuktau* is compressed. The bhāṣya-supported sense is the final liberation path in the passage to the state of immovability.

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| navānām | genitive plural of *nava* | of nine |
| tu | particle | but; now |
| kṣaya-jñāne | locative singular compound | at knowledge of destruction |
| akopyasya | genitive singular | of the immovable one |
| daśa | numeral | ten |
| bhāvanā | nominative singular | cultivation |
| tat-saṃcare | locative singular | in the transition to that state |
| antya-muktau | locative singular compound | at the final liberation path |
| ca | conjunction | and |
| prokta-śeṣe | locative singular compound | in the remainder of the cases stated |
| aṣṭa-bhāvanā | nominative singular compound | cultivation of eight |

## Grammar

The first half is elliptical:

```text
kṣayajñāne
    at the moment of knowledge of destruction

navānāṃ bhāvanā
    there is cultivation of nine

akopyasya
    for the immovable one

daśa bhāvanā
    there is cultivation of ten
```

The second half continues:

```text
tat-saṃcare
    in the transition to that immovable state

antya-muktau ca
    and at the final liberation path

[daśa bhāvanā]
    ten are cultivated

prokta-śeṣe
    in the remaining cases already stated

aṣṭa-bhāvanā
    eight are cultivated
```

## Literal Translation

At the moment of knowledge of destruction, nine knowledges are cultivated; for the immovable one, ten. Ten are also cultivated at the final liberation path in the transition to that state. In the remaining cases already stated, eight are cultivated.

## Philosophical Translation

As the path reaches its terminal liberating knowledge, its cultivated range expands. Ordinary knowledge of destruction activates nine knowledges. When realization is stabilized as immovable, the full tenfold field is cultivated. The final transition into that immovable condition likewise carries the complete tenfold cultivation. Other advanced cases in this sequence cultivate eight.

## Technical Vocabulary

### kṣaya-jñāna

```text
kṣaya-jñāna
    knowledge of destruction
    knowledge that the defilements to be abandoned
    have been destroyed
```

This is a terminal knowledge of the path. It does not merely oppose an obstruction; it knows that the required destruction has been accomplished.

### akopya

```text
akopya
    immovable
    no longer liable to regression
    stable in liberation
```

The immovable practitioner cultivates all ten knowledges.

### saṃcara

```text
saṃcara
    passage
    transition
    movement into another established state
```

Here it is the transition into immovability.

### antya-mukti

```text
antya-mukti
    final liberation path
```

This is the culminating liberation moment in that transition.

## Doctrinal Determination

### The count at knowledge of destruction

```text
knowledge of destruction
    → cultivation of nine knowledges
```

The exclusion of one knowledge reflects the practitioner's still not fully immovable status.

### The count for the immovable one

```text
immovable liberation
    → cultivation of all ten knowledges
```

The complete count signals that no knowledge-type relevant to the liberated cognitive system remains excluded.

### The transition to immovability

```text
final liberation path
    in transition to immovability
        → cultivation of ten
```

The transition is counted by the state it actualizes. At its culminating liberation moment, the full range is cultivated.

### The remaining cases

```text
other advanced cases already enumerated
    → cultivation of eight
```

The verse closes the local counting scheme by supplying the default number for cases not separately assigned six, seven, nine, or ten.

## Path Calculus

VAK 7.25 gives a compact terminal scale:

| Path condition | Knowledges cultivated |
|---|---:|
| Knowledge of destruction | 9 |
| Immovable practitioner | 10 |
| Final liberation path in transition to immovability | 10 |
| Remaining stated cases | 8 |

The counts express differences in attained stability and path-function, not merely arithmetic variation.

```text
advanced path-operation
    + degree of stability
    + terminal or transitional status
        → cultivation count
```

This is the sort of material that will later belong to a dedicated Path Analytics treatment.

## Organon Light

The basic determination is:

```text
as liberation becomes more stable
    the active range of knowledge becomes more complete
```

The path does not merely remove obstacles one by one. At decisive terminal moments, it reorganizes the whole available field of knowing.

No stronger identification is imposed in this first pass.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix marga: <http://127.0.0.1:3000/marga#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_7_25
    a vak:Karika ;
    rdfs:label "VAK 7.25" ;
    vak:determines jna:NinefoldCultivationAtDestructionKnowledge,
                   jna:TenfoldCultivationOfImmovable,
                   jna:EightfoldCultivationInRemainingCases .

jna:NinefoldCultivationAtDestructionKnowledge
    a jna:CultivationCount ;
    jna:occursAt jna:DestructionKnowledge ;
    jna:count 9 .

jna:TenfoldCultivationOfImmovable
    a jna:CultivationCount ;
    jna:belongsTo marga:ImmovableLiberation ;
    jna:count 10 .

jna:EightfoldCultivationInRemainingCases
    a jna:CultivationCount ;
    jna:count 8 .
```

## Commit History

```text
2026-07-23 — Initial kārikā-pass analysis for VAK_7b.
```
