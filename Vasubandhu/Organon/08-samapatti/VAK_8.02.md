# VAK_8.02 — Successive Dhyāna Distinctions and Four Formless Attainments

## 1. Sanskrit (Devanāgarī)

```sanskrit
विचारप्रीतिसुखवत् पूर्वपूर्वाङ्गवर्जितम् ।
तथारूप्याश् चतुःस्कन्धा अधोभूमिविवेकजाः ॥ ८.०२ ॥
```

## 2. Sanskrit (IAST)

```text
vicāraprītisukhavat pūrvapūrvāṅgavarjitam |
tathārūpyāś catuḥskandhā adhobhūmivivekajāḥ || 8.02 ||
```

The Sanskrit follows the local kārikā witness. The
Devanāgarī renders the same reading. The verse presupposes
VAK 8.01's wholesome one-pointedness and distributes
associated factors rather than defining four unrelated
kinds of cognition.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `vicāra-prīti-sukha-vat` | nominative singular neuter possessive adjective | possessing vicāra, joy, and ease |
| `pūrva-pūrva-aṅga-varjitam` | nominative singular neuter compound adjective (`pūrva + aṅga` → `pūrvāṅga`) | successively deprived of the preceding factors; repeated `pūrva` is distributive |
| `tathā` | adverb (`tathā + ārūpyāḥ` → `tathārūpyāḥ`) | likewise, in the respects specified by prose |
| `ārūpyāḥ` | nominative plural masculine | the formless attainments or states; the plural predicates apply to these, not to the four dhyānas |
| `catuḥ-skandhāḥ` | nominative plural masculine compound adjective | constituted by four Bases |
| `adho-bhūmi-viveka-jāḥ` | nominative plural masculine compound adjective | arising through separation from a lower ground |

## 4. Grammar

Feature grammar (NLTK notation). Both opening adjectives are neuter singular
and distributive over supplied heads; the formless clause agrees in the
plural masculine. Words supplied from the Bhāṣya carry `SUPPLIED=prose`.

```nltk-fcfg
% start S
# tokens: vicāraprītisukhavat ∅-prathamam-dhyānam pūrvapūrvāṅgavarjitam ∅-śeṣam-dhyānam tathā ārūpyāḥ catuḥskandhāḥ adhobhūmivivekajāḥ
S -> CL[K=possess] CL[K=lack] CL[K=likeness]

CL[K=possess]  -> ADJ[NUM=?n,GEN=?g,POSS=yes] N[NUM=?n,GEN=?g,SUPPLIED=prose,ORD=first]
CL[K=lack]     -> ADJ[NUM=?n,GEN=?g,PRIV=yes,DIST=yes] N[NUM=?n,GEN=?g,SUPPLIED=prose,ORD=rest]
CL[K=likeness] -> ADV[LIKE=restricted] N[CASE=nom,NUM=?n,GEN=?g] ADJ[NUM=?n,GEN=?g,BASES=4] ADJ[NUM=?n,GEN=?g,SRC=lower]

ADJ[NUM=sg,GEN=n,POSS=yes] -> 'vicāraprītisukhavat'
ADJ[NUM=sg,GEN=n,PRIV=yes,DIST=yes] -> 'pūrvapūrvāṅgavarjitam'
ADV[LIKE=restricted] -> 'tathā'
N[CASE=nom,NUM=pl,GEN=m] -> 'ārūpyāḥ'
ADJ[NUM=pl,GEN=m,BASES=4] -> 'catuḥskandhāḥ'
ADJ[NUM=pl,GEN=m,SRC=lower] -> 'adhobhūmivivekajāḥ'
N[NUM=sg,GEN=n,SUPPLIED=prose,ORD=first] -> '∅-prathamam-dhyānam'
N[NUM=sg,GEN=n,SUPPLIED=prose,ORD=rest]  -> '∅-śeṣam-dhyānam'
```

```nltk-dep
'∅-prathamam-dhyānam' -> 'vicāraprītisukhavat'
'∅-śeṣam-dhyānam' -> 'pūrvapūrvāṅgavarjitam'
'ārūpyāḥ' -> 'tathā' | 'catuḥskandhāḥ' | 'adhobhūmivivekajāḥ'
```

`vicāra` implies supplied `vitarka` in the first configuration only (the
smoke-and-fire concomitance), and `śubhaikāgrya` carries over from 8.01.
`tathā` is restricted by the Bhāṣya to four-ness, birth and attainment, and
one-pointedness; it does not transfer the dhyānas' full constitution.

**Close construe.** The first dhyāna possesses vicāra, joy, and ease; the
remaining dhyānas successively lack the preceding factors. Likewise [in the
specified respects] are the formless states: with accompaniment they consist
of four Bases and arise through separation from the lower ground.

## 5. Translation

### Literal Translation

> The first possesses vicāra, joy, and ease; the remaining
> dhyānas are successively deprived of preceding factors.
> Likewise are the formless attainments: four-Base
> in constitution and arising through separation from
> the lower ground.

### Bhāṣya-informed study translation

> The first dhyāna possesses vicāra, joy, and ease, with vitarka
> understood along with vicāra; the remaining dhyānas are
> successively deprived of the preceding factors. Likewise the
> formless attainments, with accompaniment, have four Bases, and
> each arises through separation from the lower ground.

## 6. Philosophical Translation

> A common defining determination persists while the
> associated factors distinguish successive attainments.
> The formless series shares that general determination
> but differs in accompanied Base constitution.
> Its order is explained through release from a lower
> ground, not merely through assigning new names to states.

“Separation” here has a stated path-function. It should
not be replaced without argument by a Yoga-specific
sense of discriminative knowledge, nor treated as an
arbitrary switch of attention.

## 7. Technical Vocabulary

**`Vicāra`.** Sustained examination or investigation.
The term is retained in the translation because its
technical distinction from vitarka should not be flattened
into a generic word such as thought.

**`Vitarka`.** Initial application or examination, supplied
by the Bhāṣya for the first dhyāna. Its inclusion is
commentarial determination of the compressed verse,
not an additional word inserted into the Sanskrit.

**`Prīti / sukha`.** Joy and ease or pleasure. Their
separate removal shows why they must not both be translated
with the same undifferentiated “happiness.” The detailed
analysis of dhyāna factors and their constitution comes
later in the chapter.

**`Aṅgavarjita`.** Deprived of factors. This passage
selects differentiating factors; it does not give a
complete inventory of every factor present in each dhyāna.
In particular, the fourth dhyāna is not a cognition
without any associated factors.

**`Ārūpya`.** Formless state or attainment. The birth
and attainment distinction remains in force. “Formless”
does not mean absent consciousness or an independently
asserted immaterial self.

**`Anuparivartirūpābhāva`.** Absence of accompanying
material form. This is the immediate explanation for
four Bases. It must not be expanded into a claim
that a human practitioner has physically lost the body
while entering an attainment.

**`Viveka`.** Separation or release. The prose defines
it as the path by which one is freed from what is
below through proceeding to dispassion. This locally
specified meaning governs the compound in the verse.

**`Adhobhūmi`.** Lower ground. In the explicitly listed
formless progression, it is the preceding ground from
which release gives rise to the next attainment.

## 8. Logical Determination

**Selected dhyāna distinctions.**

| Dhyāna | Selected qualities retained in this account | Progressive exclusions |
|---|---|---|
| First | Vicāra, joy, ease; vitarka included by prose | None of the listed qualities excluded |
| Second | Joy and ease | Vicāra; vitarka is also absent in the dhyāna scheme |
| Third | Ease | Vicāra and joy |
| Fourth | Wholesome one-pointedness remains understood | Vicāra, joy, and ease |

This is a table of the passage's differentiating qualities,
not the complete aṅga lists. The first-dhyāna inference
from vicāra to vitarka does not logically prove that
absence of vicāra entails absence of vitarka everywhere.
The fuller dhyāna-factor account will control those
technical distributions.

**The four formless attainments.**

| Ground relinquished | Attainment arising through its separation |
|---|---|
| Fourth dhyāna | Essence of infinite space, `ākāśānantyāyatana` |
| Infinite space | Essence of infinite consciousness, `vijñānānantyāyatana` |
| Infinite consciousness | Essence of nothingness, `ākiñcanyāyatana` |
| Nothingness | Essence of neither perception nor non-perception, `naivasaṃjñānāsaṃjñāyatana` |

These names are supplied by the prose. The passage
lists the progression and defines release; it does
not yet analyze each object or provide a complete
practice procedure for entering these states.

**Defining nature and accompanied constitution.**

```text
Dhyana attainment:
    general defining nature: Wholesome one-pointedness
    with accompaniment: Five Bases

Formless attainment:
    general defining nature: Wholesome one-pointedness
    with accompaniment: Four Bases
    omitted accompanying Base: Rupa
```

The four are feeling, perception, formations, and
consciousness. Their enumeration explains the fourfold
constitution without turning formless attainment into
one isolated consciousness lacking mental factors.

The transition is not characterized solely by subtraction.
The source retains wholesome one-pointedness and supplies
a path of dispassion from the lower ground. “Higher”
therefore does not mean simply “fewer properties” in
an unrestricted philosophical sense.

## 9. Interpretive Note

**Source boundary.** The local Bhāṣya file extends to
435|21 and summarizes an extended argument against
subtle form in the formless domain. The running source
has already opened VAK 8.03 with the naming of the
formless states and their access stages at 434|11.
That later argument is not silently treated as entirely
belonging to 8.02. Here the four-Base claim is
established with its immediate reason; its ensuing
challenge and defense remain the next study's work.

**Correcting a logical shortcut.** The local analysis
says the second dhyāna lacks vicāra “and therefore”
vitarka. The first-dhyāna concomitance statement alone
does not license that converse inference. The standard
dhyāna distribution must be kept distinct from what
that particular smoke-and-fire argument proves.

**Witness cautions.** The running source contains
`kuśalamaikāgyraṃ`, `punrdhyānatrayaṃ`, and
`naivasaṃjñānāsamjñāyatanam`. The local verse and prose
context secure wholesome one-pointedness, the remaining
three dhyānas, and the final formless attainment, while
the transcription defects remain in the source files.
No underlying witness has been changed.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates the common determination and
the distinctions among associated factors and Base
constitution. Yoga Technē, its kriyā–karma companion,
concerns the path of release through which the succeeding
attainment arises. The passage keeps both structural
classification and operative transition explicit.

For Organon, a shared cognitive determination does not
require identical associated conditions in every state.
Conversely, removing a named factor is not a sufficient
model of the entire transition: the path and the retained
determination also matter. This supports a relational
representation without reducing the account to deletion
of fields from a data structure.

Comparisons with Judgment, Yoga viveka, or a wider
architecture of reason remain project developments.
The source here gives the controlled basis: wholesome
one-pointedness, differentiated accompaniment, and release
from the lower ground through dispassion.

**Review status.** Provisional, Bhāṣya-controlled study.
The inherited wholesome one-pointedness, first-dhyāna
vitarka inclusion, selected factor progression, specified
analogy with formless states, four Bases, fourfold
sequence, and local definition of viveka have been
checked against the local extract and running source.
The extended form-absence debate remains for VAK 8.03.

## 10. OWL++ Seed

```text
Class: DhyanaAttainment
Class: FormlessAttainment
Class: AssociatedFactor
Class: LowerGroundRelease

ObjectProperty: hasGeneralDefiningNature
ObjectProperty: hasSelectedAssociatedFactor
ObjectProperty: hasAccompaniedConstitution
ObjectProperty: arisesThroughReleaseFrom

AllAttainmentsInPresentGeneralDefinition:
    definingNature: WholesomeOnePointedness

FirstDhyana:
    selectedFactors: Vitarka, Vicara, Priti, Sukha
SecondDhyana:
    selectedFactorsHere: Priti, Sukha
ThirdDhyana:
    selectedFactorHere: Sukha
FourthDhyana:
    excludedSelectedFactors: Vicara, Priti, Sukha

FormlessAttainments:
    aspects: Birth, Attainment
    accompaniedConstitution: FourBases
    absentAccompanyingBase: Rupa

InfiniteSpace:
    releasedGround: FourthDhyana
InfiniteConsciousness:
    releasedGround: InfiniteSpace
Nothingness:
    releasedGround: InfiniteConsciousness
NeitherPerceptionNorNonPerception:
    releasedGround: Nothingness

VivekaHere:
    explanation: PathOfReleaseFromLowerGroundThroughDispassion

ProjectConstraint: Selected factors are not complete dhyana factor inventories.
ProjectConstraint: First-dhyana concomitance does not prove its converse universally.
ProjectConstraint: Four Bases concern accompanied attainment constitution.
ProjectConstraint: Tatha preserves specified analogies, not complete identity.
ProjectConstraint: Extended form-absence debate continues in VAK 8.03.
```

This is a declarative project seed, not executable OWL.
VAK 8.03 next examines formless naming, the absence of
form, and the subsequent arising of form.
