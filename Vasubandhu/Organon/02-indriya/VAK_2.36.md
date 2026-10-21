# VAK_2.36 — Acquisition

## 1. Sanskrit (Devanāgarī)

```sanskrit
नामकायादयश्चेति प्राप्तिर्लाभः समन्वयः ।
प्राप्त्यप्राप्ती स्वसंतानपतितानां निरोधयोः ॥ २.३६ ॥
```

## 2. Sanskrit (IAST)

```text
nāmakāyādayaś ceti prāptir lābhaḥ samanvayaḥ /
prāptyaprāptī svasaṃtānapatitānāṃ nirodhayoḥ // 2.36 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| nāma-kāya-ādayaḥ | nom. pl. m.; compound | groups of names and so forth |
| iti | indeclinable | thus, the list |
| ca | conjunction | and; completes the preceding enumeration |
| prāptiḥ | nom. sg. f. | acquisition |
| lābhaḥ | nom. sg. m. | obtaining |
| samanvayaḥ | nom. sg. m. | possession |
| prāpti-aprāptī | nom. dual f.; coordinated compound | acquisition and non-acquisition, the scope-pair |
| sva-saṃtāna-patitānām | gen. pl. m.; compound | of what belongs to one's own continuum |
| nirodhayoḥ | gen. dual m. | of the two cessations |

Two explanations of one word. Gender does not block that.

The opening completes 2.35; it is not part of the definition of acquisition. The two genitives distinguish the conditioned range from the unconditioned exceptions. Sandhi is opened for parsing.

```text
# tokens: nāmakāyādayaḥ ca iti prāptiḥ lābhaḥ samanvayaḥ prāptyaprāptī svasaṃtānapatitānām nirodhayoḥ
```

## 4. Grammar

The first three tokens close the prior list. The next three give acquisition's two senses, not two things that must be simultaneously manifest. The final dual takes two genitives: own-continuum items and the two cessations. The prose explicitly distinguishes conditioned from unconditioned scope and excludes space from both acquisition and non-acquisition.

```nltk-fcfg
% start S
# tokens: nāmakāyādayaḥ ca iti prāptiḥ lābhaḥ samanvayaḥ prāptyaprāptī svasaṃtānapatitānām nirodhayoḥ
S[SEM=<(?continuation & ?definition & ?scope)>] -> CONTINUATION[SEM=?continuation] DEFINITION[SEM=?definition] SCOPE[SEM=?scope]
CONTINUATION[SEM=<ContinuesPriorList(name_groups)>] -> NAMES AND CLOSE
NAMES -> 'nāmakāyādayaḥ'
AND -> 'ca'
CLOSE -> 'iti'
DEFINITION[SEM=<Sense(acquisition,obtaining) & Sense(acquisition,possession)>] -> ACQUISITION OBTAINING POSSESSION
ACQUISITION -> 'prāptiḥ'
OBTAINING -> 'lābhaḥ'
POSSESSION -> 'samanvayaḥ'
SCOPE[SEM=<PairRange(acquisition_pair,own_continuum) & PairRange(acquisition_pair,two_cessations)>] -> PAIR OWN CESSATIONS
PAIR -> 'prāptyaprāptī'
OWN -> 'svasaṃtānapatitānām'
CESSATIONS -> 'nirodhayoḥ'
```

```nltk-dep
'nāmakāyādayaḥ' -> 'ca' | 'iti'
'prāptiḥ' -> 'lābhaḥ' | 'samanvayaḥ'
'prāptyaprāptī' -> 'svasaṃtānapatitānām' | 'nirodhayoḥ'
```

| Span | Constituent | Result |
|---|---|---|
| [0, 3) | `CONTINUATION` | completes the prior enumeration |
| [3, 6) | `DEFINITION` | obtaining and possession as two senses |
| [6, 9) | `SCOPE` | own continuum and two cessations |

## 5. Translation

### Literal Translation

> And the groups of names and the rest. Acquisition is obtaining and possession. Acquisition and non-acquisition concern what belongs to one's own continuum and the two cessations.

### Bhāṣya-informed study translation

> And groups of names and so forth complete the preceding list. Acquisition is obtaining what was not obtained or had been relinquished, and possession of what has been obtained. Acquisition and non-acquisition concern conditioned dharmas belonging to one's own continuum and, among the unconditioned, the two cessations.

## 6. Philosophical Translation

> Acquisition names both obtaining and possession, not merely a present manifestation. Acquisition and non-acquisition concern one's own conditioned continuum and the two cessations; space lies outside both. Whether this determination requires a distinct real entity or is designated through seed-capacity remains disputed.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| prāpti | acquisition | obtaining and possession |
| lābha | obtaining | what was absent or relinquished |
| samanvāgama | possession | what has been obtained |
| aprāpti | non-acquisition | the reverse, inside the range |
| svasaṃtāna | one's own continuum | the conditioned range |
| pratisaṃkhyā-nirodha | cessation through Discrimination | not all beings |
| apratisaṃkhyā-nirodha | cessation not through Discrimination | all sentient beings |
| ākāśa | space | neither |
| bīja | seed | capable name-and-Form; not a second entity |
| prajñapti | designation | the critical account |
| dravya | real entity | the Vaibhāṣika account |

Anāsrava in the quotation is uncontaminated. Not unconditioned. Not every uncontaminated dharma.

## 8. Logical Determination

**Kārikā with prose-resolved scope.** Applicable differs from actual possession. Acquisition and non-acquisition share a restricted range; they are not unrestricted complements over everything. The model does not decide whether either is a distinct real entity.

```nltk-sem
two_senses : Sense(acquisition,obtaining) & Sense(acquisition,possession)
range : PairRange(acquisition_pair,own_continuum) & PairRange(acquisition_pair,two_cessations)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(ContinuesPriorList(name_groups) & (Sense(acquisition,obtaining) & Sense(acquisition,possession)) & (PairRange(acquisition_pair,own_continuum) & PairRange(acquisition_pair,two_cessations)))

# THEORY prose_applicability
# EXPECT prose_applicability T
all x.(AcquisitionApplicable(x) <-> (OwnConditioned(x) | Cessation(x)))
all x.(NonAcquisitionApplicable(x) <-> AcquisitionApplicable(x))
all x.(Possessed(x) -> AcquisitionApplicable(x))
all x.(NonPossessed(x) -> NonAcquisitionApplicable(x))
all x.(OutsideRange(x) -> (-AcquisitionApplicable(x) & -NonAcquisitionApplicable(x)))

# THEORY rejected_nonpossession_means_inapplicability
# EXPECT rejected_nonpossession_means_inapplicability F
all x.(NonPossessed(x) -> -NonAcquisitionApplicable(x))

# THEORY rejected_every_unconditioned_is_in_range
# EXPECT rejected_every_unconditioned_is_in_range F
all x.(Unconditioned(x) -> AcquisitionApplicable(x))

# THEORY rejected_another_continuum_is_own
# EXPECT rejected_another_continuum_is_own F
all x.(OtherContinuum(x) -> AcquisitionApplicable(x))
```

```nltk-valuation
name_groups => name_groups_continuation
acquisition => acquisition_term
obtaining => obtaining_sense
possession => possession_sense
acquisition_pair => acquisition_nonacquisition_pair
own_continuum => own_conditioned_range
two_cessations => two_cessation_range
ContinuesPriorList => {name_groups_continuation}
Sense => {(acquisition_term,obtaining_sense),(acquisition_term,possession_sense)}
PairRange => {(acquisition_nonacquisition_pair,own_conditioned_range),(acquisition_nonacquisition_pair,two_cessation_range)}
OwnConditioned => {possessed_own_dharma,unpossessed_own_dharma}
Cessation => {discriminative_cessation,nondiscriminative_cessation}
Unconditioned => {discriminative_cessation,nondiscriminative_cessation,space}
OtherContinuum => {another_person_dharma}
OutsideRange => {another_person_dharma,nonsentient_item,space}
AcquisitionApplicable => {possessed_own_dharma,unpossessed_own_dharma,discriminative_cessation,nondiscriminative_cessation}
NonAcquisitionApplicable => {possessed_own_dharma,unpossessed_own_dharma,discriminative_cessation,nondiscriminative_cessation}
Possessed => {possessed_own_dharma,nondiscriminative_cessation}
NonPossessed => {unpossessed_own_dharma}
```

These examples have an implicit fixed subject: possession of the discriminative cessation is deliberately not assigned, because the prose distinguishes persons. The two cessation constants label the range, not literal substitutions for every technical occurrence. The entity/designation dispute stays in its attributed argument, not in a valuation silently declaring one position true.

## 9. Interpretive Note

**Translation note.** The commentary distinguishes obtaining what was not obtained or had been relinquished from possessing what has been obtained. It excludes what belongs to another continuum, the non-sentient, and space. It tests scriptural wording, causal production, noble status, and possible regress; the contested initial-moment exception and local sense of tolerating remain unsettled.

The list is completed and left. The inquiry is acquisition. Scriptural wording, causal work, and noble status are tested in that order. Production is disowned. Status remains the problem, because worldly consciousness does not display the path.

The initial-moment exception is contextual. Fully bound, at the first moment of the noble path. Not a restored collation. The greed sentence is a local use. Tolerating, or not expelling. Not the king's mastery, and not the seed, forced into one gloss.

In the Organon reading, Cognition governs Perception and Conception, remaining distinct from consciousness and Mind. Possession cannot be reduced to what is presently manifest in consciousness. The competing accounts must explain status and abandonment without silently changing applicability into actual possession.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_36
    a vak:Karika ;
    rdfs:label "VAK 2.36" ;
    vak:hasTopic vak:Acquisition ;
    vak:belongsTo vak:Indriyanirdesa .

vak:Acquisition vak:includes vak:Obtaining, vak:Possession .
vak:Acquisition vak:range vak:OwnContinuum, vak:TwoCessations .
vak:Space vak:acquisitionApplicable false ;
    vak:nonAcquisitionApplicable false .

organon:VAK_2_36_Interpretation
    organon:distinguishes vak:Applicability, vak:ActualPossession,
        vak:SeedCapacity, vak:RealEntityClaim .
```
