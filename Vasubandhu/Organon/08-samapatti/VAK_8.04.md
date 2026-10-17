# VAK_8.04 — Formless Names: Preparatory Practice and Attenuated Perception

## 1. Sanskrit (Devanāgarī)

```sanskrit
आकाशानन्त्यविज्ञानानन्त्याकिंचन्यसंज्ञकाः ।
तथाप्रयोगान् मान्द्यात् तु नैवसंज्ञानासंज्ञकः ॥ ८.०४ ॥
```

## 2. Sanskrit (IAST)

```text
ākāśānantya-vijñānānantyākiṃcanya-saṃjñakāḥ |
tathāprayogān māndyāt tu naivasaṃjñānāsaṃjñakaḥ || 8.04 ||
```

The IAST follows the local kārikā witness; the Devanāgarī
renders it, including the anusvāra in `ākiṃcanya` and
the sandhied `prayogān`. The local Devanāgarī witness
instead prints `ākiñcanya` and separates `prayogāt`.
The running source also has `ākiñcanya` and a different,
damaged final pāda. These differences are not silently
presented as one uniform witness.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `ākāśa-ānantya` | compound member (`ākāśānantya`) | infinity of space |
| `vijñāna-ānantya` | compound member (`vijñānānantya`) | infinity of consciousness; `vijñāna` is consciousness here, consistent with the preceding formless series |
| `ākiṃcanya` | abstract noun in compound | nothingness |
| `saṃjñakāḥ` | nominative plural masculine adjective | bearing the specified names |
| `tathā-prayogāt` | ablative singular masculine compound; final `t` assimilated before `m` in local `prayogān māndyāt` | because of application in those respective ways; not an accusative plural “those practices” |
| `māndyāt` | ablative singular neuter abstract noun | because of attenuation or weakness |
| `tu` | contrastive particle | however |
| `na-eva-saṃjñā-na-asaṃjñakaḥ` | nominative singular masculine compound adjective | designated neither-perception-nor-non-perception |

## 4. Grammar

The first three names have a distributive preparatory explanation; the fourth has a separate naming ground. The prose denies that the names imply exclusive objects and specifies attenuated—but present—perception.

```nltk-fcfg
% start S
# tokens: ∅-trayas ākāśānantya-vijñānānantyākiṃcanya-saṃjñakāḥ tathāprayogān māndyāt tu naivasaṃjñānāsaṃjñakaḥ ∅-saṃjñā
S -> CL[K=first_three] CL[K=fourth]
CL[K=first_three] -> N[CASE=nom,NUM=pl,GEN=m,SUPPLIED=prose] ADJ[CASE=nom,NUM=pl,GEN=m,COUNT=three] ABL[CASE=abl,NUM=sg,GEN=m,CAUSE=application]
CL[K=fourth] -> ABL[CASE=abl,NUM=sg,GEN=n,CAUSE=attenuation] PTCL[CONTRAST=yes] ADJ[CASE=nom,NUM=sg,GEN=m] N[CASE=nom,NUM=sg,GEN=f,SUPPLIED=prose]
N[CASE=nom,NUM=pl,GEN=m,SUPPLIED=prose] -> '∅-trayas'
ADJ[CASE=nom,NUM=pl,GEN=m,COUNT=three] -> 'ākāśānantya-vijñānānantyākiṃcanya-saṃjñakāḥ'
ABL[CASE=abl,NUM=sg,GEN=m,CAUSE=application] -> 'tathāprayogān'
ABL[CASE=abl,NUM=sg,GEN=n,CAUSE=attenuation] -> 'māndyāt'
PTCL[CONTRAST=yes] -> 'tu'
ADJ[CASE=nom,NUM=sg,GEN=m] -> 'naivasaṃjñānāsaṃjñakaḥ'
N[CASE=nom,NUM=sg,GEN=f,SUPPLIED=prose] -> '∅-saṃjñā'
```

```nltk-dep
'∅-trayas' -> 'ākāśānantya-vijñānānantyākiṃcanya-saṃjñakāḥ' | 'tathāprayogān'
'naivasaṃjñānāsaṃjñakaḥ' -> 'māndyāt' | 'tu' | '∅-saṃjñā'
```

The supplied three and `yathāsaṃkhyam` distribute name and application; `tathāprayogān` is causal, not an accusative “practices.” The opening question denies exclusive objects, and `māndyāt` concerns a weak, present saṃjñā.


**Close construe.** The first three are named infinity
of space, infinity of consciousness, and nothingness
because of corresponding application. The fourth,
however, is called neither-perception-nor-non-perception
because perception is attenuated.

## 5. Translation

### Literal Translation

> The first three are designated infinity of space,
> infinity of consciousness, and nothingness because
> of application in those ways. The fourth, however,
> is designated neither-perception-nor-non-perception
> because perception is attenuated.

### Bhāṣya-informed study translation

> The first three are designated infinity of space, infinity of
> consciousness, and nothingness, according to the way they are
> applied; the fourth, however, is designated
> neither-perception-nor-non-perception because perception in
> it is attenuated.

## 6. Philosophical Translation

> A name can record the mode of application through
> which an attainment is approached rather than exhaustively
> identify everything it can take as object. A different
> name can be explained through the condition of a
> remaining factor. The formless series therefore requires
> more than a uniform rule of naming from an object.

The fourth attainment also has a preparatory valuation.
The distinction is between the explanatory reasons
supplied for the names, not between three states with
practice and a fourth with none.

## 7. Technical Vocabulary

**`Tathāprayoga`.** Application in the corresponding
manner. The prose gives three formulations of attention
and derives the names from those formulations. It does
not offer a complete independent training protocol.

**`Manasikurvāṇa`.** Attending or bringing before the
mind, the present participial expression used of the
practitioners. The formulations are modes of attention
in this meditative context, not assertions that the
study must adopt as unrestricted metaphysical propositions.

**`Vijñāna`.** Consciousness in the second attainment's
name. The research vocabulary also uses “knowledge.”
The controlled referent remains vijñāna; it should not
be silently equated with omniscience, unlimited factual
knowledge, or every category of jñāna in Chapter 7.

**`Nāsti kiñcit`.** “There is nothing.” Here this is
the reported mode of attending associated with nothingness.
It is not a universal denial that any dharmas exist.
The four-Base constitution remains in place.

**`Māndya / mṛdutva`.** Attenuation, weakness, or mildness.
The prose specifies the condition of saṃjñā. The term
does not diagnose ordinary fatigue or intellectual
incapacity in the practitioner.

**`Paṭvī saṃjñā`.** Sharp or strongly operative perception.
The fourth attainment lacks perception of that strength,
while not lacking perception altogether.

**`Saṃjñāroga / saṃjñāgaṇḍa / saṃjñāśalya`.** Perception
regarded as disease, swelling, and thorn. These belong
to a reported preparatory valuation. They are not a
blanket command to reject every form of perception.

**`Āsaṃjñikasaṃmoha`.** The delusion associated with
non-perception in the evaluative passage. It supplies
the contrast to the negatively regarded perception;
it does not make complete non-perception the fourth
attainment's defining nature.

## 8. Logical Determination

The naming explanation is not a uniform object rule: the first three names track corresponding modes of attention, while the fourth is explained by perception's attenuated condition [verse; prose]. The Bhāṣya rejects exclusive-object entailment and keeps attenuation distinct from total absence.

**Signature.** `NamedAs(x,n)`; `AppliedAs(x,m)`; `Perception(x)`; `Attenuated(x)`; `Sharp(x)`; `PerceptionAbsent(x)`.

**Finite data.** The formulas of attention are recorded as the respective applications reported in the prose; they are not an exhaustive inventory of possible objects.

```nltk-valuation
spaceattainment => spaceattainment
consciousnessattainment => consciousnessattainment
nothingattainment => nothingattainment
fourthatta => fourthatta
space => space
consciousness => consciousness
nothing => nothing
spaceformula => spaceformula
consciousnessformula => consciousnessformula
nothingformula => nothingformula
perception => perception
NamedAs => {(spaceattainment,space),(consciousnessattainment,consciousness),(nothingattainment,nothing),(fourthatta,neither)}
AppliedAs => {(spaceattainment,spaceformula),(consciousnessattainment,consciousnessformula),(nothingattainment,nothingformula)}
Perception => {fourthatta}
Attenuated => {fourthatta}
Sharp => {}
PerceptionAbsent => {}
```

**Rules (verse and prose).**

```nltk-fol
# THEORY shared
# [prose] anantam ākāśam: corresponding first application
AppliedAs(spaceattainment,spaceformula)
NamedAs(spaceattainment,space)
# [prose] anantaṃ vijñānam; nāsti kiñcit: corresponding applications
AppliedAs(consciousnessattainment,consciousnessformula)
NamedAs(consciousnessattainment,consciousness)
AppliedAs(nothingattainment,nothingformula)
NamedAs(nothingattainment,nothing)
# [verse] māndyāt; [prose] perception remains, but is not sharp
Perception(fourthatta)
Attenuated(fourthatta)
- Sharp(fourthatta)
- PerceptionAbsent(fourthatta)
```

**Results (NLTK).** The checker parses the rules and finds the shared theory true against this finite valuation. This records the source's stated naming grounds; it does not infer an object restriction from a name.

**Scope cautions.** “There is nothing” reports the third mode of attention, not a universal denial that anything exists. The fourth is not cessation: perception remains, though not sharp. Preparatory valuations about perception as disease or non-perception as delusion are acknowledged in the Bhāṣya but are not its final naming ground.

## 9. Interpretive Note

**Restraint in the object claim.** The local research
analysis says the fourth cannot be defined through
a comparable new object-support. The source gives
attenuation as its naming explanation but does not
present a complete negative theory of its objects.
The official study therefore records the positive
explanation without claiming more than the passage establishes.

**Witness cautions.** The running source prints
`māndyāktu nasaṃjñanāpyasaṃjñakaḥ`, whereas the local
kārikā reads `māndyāt tu naivasaṃjñānāsaṃjñakaḥ`.
The full attainment name in prose and the contrast
between strong and non-absent perception secure the
sense, while the variant pāda remains visible here.

Other irregularities include `kimepām`, `gaṇdaḥ`, and
the compressed ending `mṛdutvātsaṃjñāmityetadevoktam`.
The local IAST `ākiṃcanya` and running `ākiñcanya`
are also distinguished. No correction is made to the
underlying research or source files.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates why a designation is warranted
and what it does not determine. Yoga Technē, its
kriyā–karma companion, concerns the application through
which an attainment is approached. The first three
names make that relation explicit; the fourth adds
the actual condition of a factor as the explanation
of its preparatory valuation.

For Organon, words such as “infinite,” “nothing,” and
“neither” require their systematic context. Here the
context supplies the relevant practice, factor, and
naming question. Their meaning is not obtained by
treating them as unbounded propositions detached from
the formless series.

A project comparison with negative judgment may be
useful, but the source's exact determination should
remain first: saṃjñā is attenuated and still present.
The passage supplies no measured perceptual threshold
or computational definition of a state boundary.

**Review status.** Provisional, Bhāṣya-controlled study.
The exclusive-object question, three preparatory formulations,
contrastive fourth naming reason, continued presence
of saṃjñā, and evaluative-practice explanation have been
checked against the local extract and running source.
Variant Sanskrit and the limits of the object inference
remain explicit.

## 10. OWL++ Seed

```text
Class: FormlessAttainment
Class: PreparatoryApplication
Class: NamingGround
Class: PerceptionCondition

ObjectProperty: receivesDesignationThrough
ObjectProperty: approachedThroughApplication
ObjectProperty: hasPerceptionCondition

InfinityOfSpace:
    namingApplication: SpaceIsInfinite

InfinityOfConsciousness:
    namingApplication: ConsciousnessIsInfinite

Nothingness:
    namingApplication: ThereIsNothing

NeitherPerceptionNorNonPerception:
    namingGround: AttenuatedPerception
    perceptionAbsent: No
    perceptionStronglyOperative: No
    preparatoryValuation: PeacefulAndExcellent

ProjectConstraint: Preparatory naming does not establish exclusive object-range.
ProjectConstraint: Fourth attainment also has preparatory application.
ProjectConstraint: Attenuation does not mean complete cessation of perception.
ProjectConstraint: Nothingness formulation is not a universal denial of dharmas.
ProjectConstraint: Vijnana designation does not imply omniscience.
ProjectConstraint: Preserve variant final-pada wording for textual review.
```

This is a declarative project seed, not executable OWL.
VAK 8.05 next classifies the eight fundamental attainments
by savoring, purity, and freedom from influxes.
