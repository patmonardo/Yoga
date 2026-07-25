# VAK_8.04 — The Four Formless Attainments

## Sanskrit

### Devanāgarī

```text
आकाशानन्त्यविज्ञानानन्त्याकिञ्चन्यसंज्ञकाः ।
तथाप्रयोगात् मान्द्यात्तु नैवसंज्ञानासंज्ञकः ॥ ८.४ ॥
```

### IAST

```text
ākāśānantya-vijñānānantyākiṃcanya-saṃjñakāḥ /
tathāprayogān māndyāt tu naivasaṃjñānāsaṃjñakaḥ // VAK_8.04 //
```

## Source Caution

The verse compresses the names of the four formless attainments into one compound sequence. The normalized doctrinal forms are:

```text
ākāśānantyāyatana
vijñānānantyāyatana
ākiṃcanyāyatana
naivasaṃjñānāsaṃjñāyatana
```

The kārikā omits `āyatana` in the first three names and gives only the naming determinants. This first pass preserves the compressed syntax while identifying the standard fourfold series.

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| ākāśa-ānantya | compound | infinity of space |
| vijñāna-ānantya | compound | infinity of knowledge |
| ākiṃcanya | abstract noun | nothingness; absence of anything |
| saṃjñakāḥ | nominative plural | designated; named |
| tathā-prayogāt | ablative singular | from practice in that manner |
| māndyāt | ablative singular | from weakness; attenuation; subtle diminution |
| tu | indeclinable | but; however |
| na-eva-saṃjñā | compound | neither exactly perception |
| na-asaṃjñā | compound | nor non-perception |
| saṃjñakaḥ | nominative singular | designated; named |

## Grammar

The first half names three attainments directly:

```text
ākāśa-ānantya
    infinity of space

vijñāna-ānantya
    infinity of knowledge

ākiṃcanya
    nothingness
```

All three are governed by:

```text
saṃjñakāḥ
    they are designated as
```

The final attainment receives a different explanation:

```text
tathā-prayogāt
    because of practice carried out in that manner

māndyāt tu
    but because of the extreme attenuation

naiva-saṃjñā-na-asaṃjñakaḥ
    it is called neither-perception-nor-non-perception
```

The causal ablatives explain the designation rather than merely listing another object-field.

## Literal Translation

They are designated as the infinity of space, the infinity of knowledge, and nothingness. Because of practice in that manner, but owing to attenuation, the last is called neither-perception-nor-non-perception.

## Philosophical Translation

The first three formless attainments are determined by the boundlessness of space, the boundlessness of knowledge, and the absence of anything. The fourth is not named by a positive object of contemplation. Through the progressive refinement of practice, perception becomes so attenuated that the state can be described neither simply as perception nor as its absence.

## Technical Vocabulary

### ākāśānantya

```text
ākāśa
    space

ānantya
    infinity
    boundlessness
```

The first formless attainment takes boundless space as its determinate field.

### vijñānānantya

```text
vijñāna
    knowledge

ānantya
    infinity
```

The canonical project translation remains `knowledge`, not consciousness.

```text
vijñānānantya
    infinity of knowledge
```

The attainment shifts from the boundlessness of spatial extension to the boundlessness of the knowing field.

### ākiṃcanya

```text
ā-kiṃ-canya
    not-anything-ness
    nothingness
```

The name determines the field through the absence of any thing:

```text
na kiṃcit
    there is nothing
```

It should not yet be inflated into an absolute metaphysical Nothing. It is the determinate object-support of a specific conditioned attainment.

### naivasaṃjñānāsaṃjñā

```text
na eva saṃjñā
    not exactly perception

na asaṃjñā
    not non-perception
```

The double negation marks an extreme limit-state.

```text
perception remains
    but is exceedingly subtle

therefore
    it cannot simply be called perception

because it is not wholly absent
    it cannot be called non-perception
```

### māndya

```text
māndya
    weakness
    diminution
    attenuation
```

Here it describes the reduced force or clarity of perception, not mere dullness in the ordinary pejorative sense.

## Doctrinal Determination

VAK 8.04 completes the fourfold ārūpya series.

| Order | Formless attainment | Naming determination |
|---:|---|---|
| 1 | infinity of space | boundless spatial field |
| 2 | infinity of knowledge | boundless knowing field |
| 3 | nothingness | absence of anything |
| 4 | neither-perception-nor-non-perception | extreme attenuation of perception |

The sequence moves through progressively subtler object-supports:

```text
boundless space
    ↓
boundless knowledge
    ↓
nothingness
    ↓
perception at its limit
```

The fourth attainment differs structurally from the first three. It is not named by a new positive object but by the indeterminate status of perception itself.

## Logical Determination

The first three attainments are determinate through their object-support:

```text
this field is boundless space
this field is boundless knowledge
this field is nothingness
```

The fourth is determinate through a limit judgment:

```text
not perception
not non-perception
```

This is not sheer indeterminacy. The double negation fixes a precise middle condition:

```text
saṃjñā
    remains minimally operative

asaṃjñā
    is therefore false

ordinary saṃjñā
    is also false
```

Thus the final formless attainment is known through the exclusion of both ordinary alternatives.

## Organon Light

The immediate kārikā-pass point is a fourfold taxonomy of conditioned attainments. The broader reconstruction is held in reserve.

The verse nevertheless reveals two modes of determination:

```text
positive field-determination
    space
    knowledge
    nothingness

limit-determination
    neither perception nor non-perception
```

In platform language:

```text
three states
    are indexed by object-support type

one terminal state
    is indexed by a constraint
    on the degree of perception
```

This is still Samāpatti as the determinate Idea-field of Samādhi, not yet Supreme Samādhi comprehending the whole field.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix sam: <http://127.0.0.1:3000/samapatti#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_8_04
    a vak:Karika ;
    rdfs:label "VAK 8.04" ;
    vak:determines sam:FourFormlessAttainments .

sam:FourFormlessAttainments
    a sam:AttainmentSeries ;
    sam:hasMember sam:InfinityOfSpace,
                  sam:InfinityOfKnowledge,
                  sam:Nothingness,
                  sam:NeitherPerceptionNorNonPerception .

sam:InfinityOfSpace
    sam:hasObjectSupport sam:BoundlessSpace .

sam:InfinityOfKnowledge
    sam:hasObjectSupport jna:BoundlessKnowledge .

sam:Nothingness
    sam:hasObjectSupport sam:AbsenceOfAnything .

sam:NeitherPerceptionNorNonPerception
    a sam:LimitAttainment ;
    sam:constrains sam:PerceptionDegree ;
    sam:excludes sam:OrdinaryPerception,
                 sam:TotalNonPerception .
```

## Commit History

```text
2026-07-25 — Initial kārikā-pass analysis.
```
