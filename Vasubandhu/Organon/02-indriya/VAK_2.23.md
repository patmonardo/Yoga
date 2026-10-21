# VAK_2.23 — Consciousness and the Factors

## 1. Sanskrit (Devanāgarī)

```sanskrit
चित्तं चैत्ताः सहावश्यं सर्वसंस्कृतलक्षणैः ।
प्राप्त्या वा पञ्चधा चैत्ता महाभूम्यादिभेदतः ॥ २.२३ ॥
```

## 2. Sanskrit (IAST)

```text
cittaṃ caittāḥ sahāvaśyaṃ sarvasaṃskṛtalakṣaṇaiḥ /
prāptyā vā pañcadhā caittā mahābhūmyādibhedataḥ // 2.23 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| cittam | nominative singular neuter noun | consciousness, not Mind or Cognition |
| caittāḥ | nominative plural masculine adjective used substantivally, twice | mental factors; first co-arising, then classification |
| saha avaśyam | indeclinables | necessarily together; carried into the marks clause |
| sarvam | nominative singular neuter adjective used substantivally | everything [conditioned that arises], separately resolved in the prose |
| saṃskṛta-lakṣaṇaiḥ | instrumental plural neuter compound noun | with the marks of the conditioned |
| prāptyā | instrumental singular feminine noun | with acquisition |
| vā | particle | a distinction of cases |
| pañcadhā | adverb | fivefold |
| mahā-bhūmi-ādi-bhedataḥ | ablatival adverb in -tas | by the division beginning with the great ground |

Citta is consciousness. It is not a substance behind the event. Caitta is the factor. Manas is not this word.

The prose separates *sarvam* from *saṃskṛtalakṣaṇaiḥ*; the verse's continuous spelling is not read as “with all conditioned marks.” Sandhi is opened for parsing.

```text
# tokens: cittam caittāḥ saha avaśyam sarvam saṃskṛtalakṣaṇaiḥ prāptyā vā pañcadhā caittāḥ mahābhūmyādibhedataḥ
```

## 4. Grammar

Four units: reciprocal accompaniment, marks accompanying everything conditioned that arises, acquisition's restricted scope, and a fivefold classification. The scope restriction on acquisition and the five class-names are supplied by the Bhāṣya, not encoded as extra verse tokens. The *prāptyā* lexical SEM supplies the acquisition relation; the prose fixes its sentient-designation scope. Necessarily together is carried into the marks clause.

```nltk-fcfg
% start S
# tokens: cittam caittāḥ saha avaśyam sarvam saṃskṛtalakṣaṇaiḥ prāptyā vā pañcadhā caittāḥ mahābhūmyādibhedataḥ
S[SEM=<(?pair & ?marks & ?acquisition & ?classes)>] -> PAIR[SEM=?pair] MARKSCLAUSE[SEM=?marks] ACQUISITION[SEM=?acquisition] CLASSES[SEM=?classes]
PAIR[SEM=<all c.(Consciousness(c) -> exists f.(Factor(f) & Accompanies(f,c))) & all f.(Factor(f) -> exists c.(Consciousness(c) & Accompanies(f,c)))>] -> CONSCIOUSNESS FACTORS TOGETHER NECESSARILY
CONSCIOUSNESS -> 'cittam'
FACTORS -> 'caittāḥ'
TOGETHER -> 'saha'
NECESSARILY -> 'avaśyam'
MARKSCLAUSE[SEM=<all x.(ArisingConditioned(x) -> MarksAccompany(x))>] -> ALL MARKS
ALL -> 'sarvam'
MARKS -> 'saṃskṛtalakṣaṇaiḥ'
ACQUISITION[SEM=<all x.(ArisingConditioned(x) -> (AcquisitionAccompanies(x) <-> SentientDesignated(x)))>] -> ACQUIRED OR
ACQUIRED -> 'prāptyā'
OR -> 'vā'
CLASSES[SEM=<ClassCount(factor_classes,five) & BeginsWithGreatGround(factor_classes)>] -> FIVE FACTORS DIVISION
FIVE -> 'pañcadhā'
DIVISION -> 'mahābhūmyādibhedataḥ'
```

```nltk-dep
'cittam' -> 'caittāḥ' | 'saha' | 'avaśyam'
'sarvam' -> 'saṃskṛtalakṣaṇaiḥ' | 'prāptyā'
'prāptyā' -> 'vā'
'caittāḥ' -> 'pañcadhā' | 'mahābhūmyādibhedataḥ'
```

| Span | Constituent | Result |
|---|---|---|
| [0, 4) | `PAIR` | reciprocal accompaniment, not all-to-all pairing |
| [4, 6) | `MARKSCLAUSE` | all arising conditioned dharmas |
| [6, 8) | `ACQUISITION` | sentient designation, not optional marks |
| [8, 11) | `CLASSES` | five classes, not five accompanying factors |

## 5. Translation

### Literal Translation

> Consciousness and the mental factors, necessarily together. Everything with the marks of the conditioned. Or with acquisition. Mental factors are fivefold, by the division beginning with the great ground.

### Bhāṣya-informed study translation

> Consciousness and mental factors necessarily arise together. All conditioned dharmas arise together with the marks of the conditioned. As for acquisition, only those designated as belonging to a sentient being arise together with it. Mental factors are fivefold by divisions beginning with the great ground.

## 6. Philosophical Translation

> Co-arising is mutual necessity, not identity. Acquisition is restricted to sentient designation. The five classes name ranges of operation, not further co-arising units.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| citta | consciousness | not manas |
| caitta | mental factor | not a faculty |
| saṃskṛta-lakṣaṇa | mark of the conditioned | not enumerated |
| prāpti | acquisition | sentient designation only |
| sattvākhya | designated as belonging to a sentient being | the restriction |
| bhūmi | ground | gativiṣaya, range of operation |
| mahābhūmika | great-ground | every consciousness |
| parītta-kleśa-mahābhūmika | limited-affliction great-ground | the fifth name, kept |

Great is range. Not a meditative stage, and not a place.

## 8. Logical Determination

**Kārikā with Bhāṣya-resolved scope.** Accompaniment is a relation, not merely possession of a property called marks or acquisition. Factor-tokens accompany their own consciousness-tokens. The acquisition relation comes from *prāptyā*; the restricted scope is Bhāṣya-resolved. Distinct episodes are not forced to co-arise with one another.

```nltk-sem
marks : MarksAccompany(x)
acquisition_relation : AcquisitionAccompanies(x)
acquisition_scope : AcquisitionAccompanies(x) <-> SentientDesignated(x)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((all c.(Consciousness(c) -> exists f.(Factor(f) & Accompanies(f,c))) & all f.(Factor(f) -> exists c.(Consciousness(c) & Accompanies(f,c)))) & all x.(ArisingConditioned(x) -> MarksAccompany(x)) & all x.(ArisingConditioned(x) -> (AcquisitionAccompanies(x) <-> SentientDesignated(x))) & (ClassCount(factor_classes,five) & BeginsWithGreatGround(factor_classes)))

# THEORY prose_scope
# EXPECT prose_scope T
all x.(Unconditioned(x) -> -ArisingConditioned(x))
all x.(SentientDesignated(x) -> (MarksAccompany(x) & AcquisitionAccompanies(x)))
all x.(GreatGroundKind(x) -> all c.(Consciousness(c) -> OccursKind(x,c)))

# THEORY rejected_every_factor_with_every_consciousness
# EXPECT rejected_every_factor_with_every_consciousness F
all f c.((Factor(f) & Consciousness(c)) -> Accompanies(f,c))

# THEORY rejected_acquisition_replaces_marks
# EXPECT rejected_acquisition_replaces_marks F
all x.(AcquisitionAccompanies(x) -> -MarksAccompany(x))

# THEORY rejected_acquisition_for_all_conditioned
# EXPECT rejected_acquisition_for_all_conditioned F
all x.(ArisingConditioned(x) -> AcquisitionAccompanies(x))

# THEORY rejected_unconditioned_arises
# EXPECT rejected_unconditioned_arises F
exists x.(Unconditioned(x) & ArisingConditioned(x))
```

```nltk-valuation
factor_classes => fivefold_classification
five => count_five
Consciousness => {consciousness_a,consciousness_b}
Factor => {factor_a,factor_b}
Accompanies => {(factor_a,consciousness_a),(factor_b,consciousness_b)}
ArisingConditioned => {consciousness_a,consciousness_b,factor_a,factor_b,sentient_form,external_form,dissociated_formation}
MarksAccompany => {consciousness_a,consciousness_b,factor_a,factor_b,sentient_form,external_form,dissociated_formation}
SentientDesignated => {consciousness_a,consciousness_b,factor_a,factor_b,sentient_form,dissociated_formation}
AcquisitionAccompanies => {consciousness_a,consciousness_b,factor_a,factor_b,sentient_form,dissociated_formation}
Unconditioned => {unconditioned_example}
ClassCount => {(fivefold_classification,count_five)}
BeginsWithGreatGround => {fivefold_classification}
ClassName => {great_ground,wholesome_great_ground,affliction_great_ground,unwholesome_great_ground,limited_affliction_great_ground}
GreatGroundKind => {illustrative_universal_kind}
OccursKind => {(illustrative_universal_kind,consciousness_a),(illustrative_universal_kind,consciousness_b)}
```

The illustrative universal kind is not an enumeration of 2.24's members. Factor-tokens and factor-kinds remain separate. The model checks reciprocal accompaniment and the two scopes without asserting that all five classes occur in every consciousness or are disjoint. It illustrates the stated necessity; a finite valuation does not prove necessity over every possible episode.

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the verse translation): Consciousness and the mental factors necessarily co-arise; neither exists without the other. Everything conditioned arises with the marks. Acquisition accompanies only what is designated as belonging to a sentient being. Mental factors are fivefold by the division beginning with the great ground. The great-ground factors occur in every consciousness.

Three relations, not one together. Reciprocal for consciousness and factors. Universal for the marks. Restricted for acquisition.

Ground is range of operation. Not a place, not automatically a meditative level, not a path-stage. The five names are not yet five exclusive sets. Members and ranges wait.

Universality of the first class does not make it wholesome. The wholesome class stays available for the next verses.

In the Organon reading, Cognition joins and governs Perception and Conception without collapsing into consciousness or Mind. The present pair is consciousness and mental factors; it does not introduce a further controller. Keep that distinction active when interpreting the factors' ranges of operation.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_23
    a vak:Karika ;
    rdfs:label "VAK 2.23" ;
    vak:hasTopic vak:CittaCaittaCoarising ;
    vak:belongsTo vak:Indriyanirdesa .

vak:Citta vak:requires vak:Caitta .
vak:Prapti vak:appliesOnlyTo vak:SentientDesignation .

organon:VAK_2_23_Interpretation
    organon:distinguishes vak:ReciprocalAccompaniment,
        vak:UniversalMarks, vak:RestrictedAcquisition,
        vak:FactorClassification .
```
