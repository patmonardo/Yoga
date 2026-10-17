# VAK_8.10 — Factors Absent from Defiled Dhyānas

## 1. Sanskrit (Devanāgarī)

```sanskrit
क्लिष्टेष्वसत्प्रीतिसुखं प्रसादः सम्प्रधीः स्मृतिः ।
उपेक्षास्मृतिशुद्धिश्च केचित् प्रस्रब्ध्युपेक्षणे ॥ ८.१० ॥
```

## 2. Sanskrit (IAST)

```text
kliṣṭeṣv asat prītisukhaṃ prasādaḥ saṃpradhīḥ smṛtiḥ |
upekṣāsmṛtiśuddhiś ca kecit prasrabdhyupekṣaṇe || 8.10 ||
```

The verse follows the local kārikā witness. The running
source's `smṛṭiḥ` differs from its `smṛtiḥ`. The prose
controls the distribution across the four dhyānas and
the interpretation of the compressed `saṃpradhīḥ`.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `kliṣṭeṣu` | locative plural (`kliṣṭeṣu + asat` → `kliṣṭeṣv asat`) | in the defiled [dhyānas] |
| `asat` | neuter singular of negated `sant`, participle of √as | absent; not present |
| `prīti-sukham` | neuter singular collective expression | rapture and pleasure |
| `prasādaḥ` | nominative singular masculine | inward clarity |
| `saṃpradhīḥ` | nominative singular feminine, compressed designation | clear comprehension, resolved by the prose |
| `smṛtiḥ` | nominative singular feminine | mindfulness or recollection |
| `upekṣā-smṛti-śuddhiḥ` | nominative singular feminine compound (`śuddhiḥ + ca` → `śuddhiś ca`) | purification of equanimity and mindfulness |
| `ca` | conjunction | and |
| `kecit` | nominative plural masculine indefinite pronoun | some [authorities] |
| `prasrabdhi-upekṣaṇe` | coordinated dual expression (`prasrabdhyupekṣaṇe`) | pliancy and equanimity; `upekṣaṇa` is resolved as `upekṣā` by the prose, and the surface form is retained |

## 4. Grammar

The first absence-list is distributed over the four defiled dhyānas; a second opinion gives another pairwise distribution. Preserve both accounts: the Bhāṣya does not merge or adjudicate them.

```nltk-fcfg
% start S
# tokens: kliṣṭeṣu asat prītisukham ∅-vivekajam ∅-prathame prasādaḥ ∅-dvitīye saṃpradhīḥ smṛtiḥ ∅-tṛtīye upekṣāsmṛtiśuddhiḥ ∅-caturthe ca kecit prasrabdhyupekṣaṇe
S -> CL[K=first_account] CL[K=other_account]
CL[K=first_account] -> LOC[CASE=loc,NUM=pl,GEN=n] NEG[NEG=yes] N[CASE=nom,NUM=sg,GEN=n,ABSENCE=one] ADJ[CASE=nom,NUM=sg,GEN=n,SUPPLIED=prose,QUAL=separation_born] N[CASE=loc,NUM=sg,GEN=n,SUPPLIED=prose,LEVEL=one] N[CASE=nom,NUM=sg,GEN=m,ABSENCE=two] N[CASE=loc,NUM=sg,GEN=n,SUPPLIED=prose,LEVEL=two] N[CASE=nom,NUM=sg,GEN=f,ABSENCE=three] N[CASE=nom,NUM=sg,GEN=f,ABSENCE=three] N[CASE=loc,NUM=sg,GEN=n,SUPPLIED=prose,LEVEL=three] N[CASE=nom,NUM=sg,GEN=f,ABSENCE=four] N[CASE=loc,NUM=sg,GEN=n,SUPPLIED=prose,LEVEL=four] CONJ[COORD=yes]
CL[K=other_account] -> PRON[CASE=nom,NUM=pl,GEN=m,OPINION=yes] N[CASE=nom,NUM=du,GEN=n,ALT=yes]
LOC[CASE=loc,NUM=pl,GEN=n] -> 'kliṣṭeṣu'
NEG[NEG=yes] -> 'asat'
N[CASE=nom,NUM=sg,GEN=n,ABSENCE=one] -> 'prītisukham'
ADJ[CASE=nom,NUM=sg,GEN=n,SUPPLIED=prose,QUAL=separation_born] -> '∅-vivekajam'
N[CASE=loc,NUM=sg,GEN=n,SUPPLIED=prose,LEVEL=one] -> '∅-prathame'
N[CASE=nom,NUM=sg,GEN=m,ABSENCE=two] -> 'prasādaḥ'
N[CASE=loc,NUM=sg,GEN=n,SUPPLIED=prose,LEVEL=two] -> '∅-dvitīye'
N[CASE=nom,NUM=sg,GEN=f,ABSENCE=three] -> 'saṃpradhīḥ'
N[CASE=nom,NUM=sg,GEN=f,ABSENCE=three] -> 'smṛtiḥ'
N[CASE=loc,NUM=sg,GEN=n,SUPPLIED=prose,LEVEL=three] -> '∅-tṛtīye'
N[CASE=nom,NUM=sg,GEN=f,ABSENCE=four] -> 'upekṣāsmṛtiśuddhiḥ'
N[CASE=loc,NUM=sg,GEN=n,SUPPLIED=prose,LEVEL=four] -> '∅-caturthe'
CONJ[COORD=yes] -> 'ca'
PRON[CASE=nom,NUM=pl,GEN=m,OPINION=yes] -> 'kecit'
N[CASE=nom,NUM=du,GEN=n,ALT=yes] -> 'prasrabdhyupekṣaṇe'
```

```nltk-dep
'asat' -> 'kliṣṭeṣu' | 'prītisukham' | '∅-vivekajam' | '∅-prathame' | 'prasādaḥ' | '∅-dvitīye' | 'saṃpradhīḥ' | 'smṛtiḥ' | '∅-tṛtīye' | 'upekṣāsmṛtiśuddhiḥ' | '∅-caturthe'
'kecit' -> 'ca' | 'prasrabdhyupekṣaṇe'
```

The prose supplies the level labels and qualifies first-dhyāna `prītisukham` as separation-born; `saṃpradhīḥ smṛtiḥ` is smṛtisaṃprajanya. In the second account, pliancy belongs to the first pair and equanimity to the last; these remain separately attributed opinions.


**Close construe.** In the defiled dhyānas, respectively,
separation-born rapture and pleasure, inward clarity,
clear comprehension and mindfulness, and purification
of equanimity and mindfulness are absent. Some say
that pliancy and equanimity are absent, respectively
in the first pair and the last pair.

## 5. Translation

### Literal Translation

> In the defiled [dhyānas], rapture-and-pleasure, clarity,
> clear comprehension and mindfulness, and purification
> of equanimity and mindfulness are absent. Some [say
> that] pliancy and equanimity [are absent].

### Bhāṣya-informed study translation

> In the defiled dhyānas, respectively, rapture and pleasure,
> inward clarity, clear comprehension and mindfulness, and the
> purification of equanimity and mindfulness are absent. Some say
> that pliancy and equanimity are what is absent.

## 6. Philosophical Translation

> An attainment's level does not alone determine the
> quality of its factors. Defilement makes a difference
> within the classification: separation-born joy cannot
> be asserted without separation, nor purified factors
> without their purification. A second account states
> the exclusions through the wholesome classification
> of pliancy and equanimity.

These two ways of explaining absence should remain
attributed. The passage does not adjudicate them here
or authorize a single combined subtraction from all
four factor inventories.

## 7. Technical Vocabulary

**`Kliṣṭa`.** Defiled or afflicted. This is not simply
a synonym of sāsrava, contaminated. The earlier chapter
classification distinguishes wholesome contaminated
attainment from defiled attainment; that distinction
must survive the translation.

**`Vivekaja prītisukha`.** Rapture and pleasure born of
separation. The first explanation denies this qualified
factor because separation from defilements is lacking.
The qualification is essential to the inference.

**`Adhyātmasaṃprasāda`.** Inward clarity, identified with
confidence in VAK 8.09's stated account. Here defilement's
turbidity explains its absence in the second dhyāna.

**`Smṛtisaṃprajanya`.** Mindfulness and clear comprehension.
These are the third-dhyāna factors under discussion.
Their absence as the specified factors should not be
expanded into an assertion that a defiled mind has
no capacity to retain or discriminate anything.

**`Upekṣāsmṛtipariśuddhi`.** Purification of equanimity
and mindfulness. The prose expands the verse's śuddhi
as pariśuddhi. In the first reported account it is
this purification that the fourth defiled dhyāna lacks.

**`Kuśalamahābhūmika`.** Belonging to the class of mental
factors common to wholesome states. The second account
uses this doctrinal classification to explain why
pliancy and equanimity cannot occur in defiled states.
The pairing by dhyāna follows their relevant factor roles.

## 8. Logical Determination

The Bhāṣya distributes the first absence account by level and reason, then reports a second classification-based account [verse; prose]. These are separately attributed theories, not one combined rule for all defiled dhyānas.

**Signature.** `Defiled(x)`; `AbsentA(level,factor)` (first reported account); `AbsentB(level,factor)` (other account); `ReportedTheory(t)`.

**Finite data.** A's absences are qualified and level-specific; B groups the first two and last two levels differently.

```nltk-valuation
first => first
second => second
third => third
fourth => fourth
vivekajapriti => vivekajapriti
prasada => prasada
smrtisamprajanya => smrtisamprajanya
upeksasmrtipurification => upeksasmrtipurification
pliancy => pliancy
equanimity => equanimity
accounta => accounta
accountb => accountb
Defiled => {first, second, third, fourth}
AbsentA => {(first,vivekajapriti),(second,prasada),(third,smrtisamprajanya),(fourth,upeksasmrtipurification)}
AbsentB => {(first,pliancy),(second,pliancy),(third,equanimity),(fourth,equanimity)}
ReportedTheory => {accounta, accountb}
```

**Theories (never merged).**

```nltk-fol
# THEORY first_account — [prose] kecid āhuḥ; reasons are level-specific
ReportedTheory(accounta)
AbsentA(first,vivekajapriti)
AbsentA(second,prasada)
AbsentA(third,smrtisamprajanya)
AbsentA(fourth,upeksasmrtipurification)

# THEORY other_account — [verse] kecit; [prose] kuśala-class explanation
ReportedTheory(accountb)
AbsentB(first,pliancy)
AbsentB(second,pliancy)
AbsentB(third,equanimity)
AbsentB(fourth,equanimity)
```

**Results (NLTK).** The checker confirms each attributed theory separately against the supplied finite data. This is model satisfaction, not a proof that the accounts are equivalent or mutually contradictory.

**Scope cautions.** A denies separation-born joy/pleasure, clarity, clear comprehension with mindfulness, and the fourth's purification; it does not negate all joy or all mindfulness in defiled states. B is the `kecit` alternative. Missing purification alone does not settle whether unpurified equanimity remains; neither list warrants a universal subtraction from every factor inventory.

## 9. Interpretive Note

**Read the qualification with the noun.** “Born of
separation” and “purification” are operative conditions,
not decorative additions. Retaining them prevents the
study from claiming more than the source denies.
Likewise, wholesome contaminated and defiled attainments
must not collapse into a single category through the
English word “contaminated.”

**Witness cautions.** The running text preserves
`smṛṭiḥ`, `ccaturthe`, and `kuśalalmahābhūmikatvāt`.
The local verse supplies smṛtiḥ; the prose's context
supports “fourth” and the kuśalamahābhūmika classification.
The transmitted `saṃbrhamitatvāt` is understood through
the contextual sense of bewilderment. The official
exposition explains these readings without changing
the research files or running source.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates the relation between level,
factor, qualification, and mode of attainment. Yoga
Technē, its kriyā–karma companion, concerns their effective
exercise. Here a level label alone cannot certify
the operation of the qualified factors associated
with that level's wholesome account.

For Organon representation, record both the scope of
an absence and the authority's account. “Purification
absent,” “factor absent,” and “factor not listed” are
different assertions. Preserving their difference allows
the source's causal explanations to remain intelligible.
This is a project reconstruction, not a source claim
about Organon or a new contemplative instruction.

**Review status.** Provisional, Bhāṣya-controlled study.
The fourfold distribution, causal explanations, second
account's paired exclusions, wholesome-class rationale,
and attribution of both accounts have been checked
against the local research and running source.

## 10. OWL++ Seed

```text
Class: DhyanaLevel
Class: AttainmentMode
Class: QualifiedFactor
Class: AbsenceAssertion
Class: ReportedAccount

ObjectProperty: concernsLevel
ObjectProperty: concernsMode
ObjectProperty: specifiesAbsentFactor
ObjectProperty: specifiesAbsentQualification
ObjectProperty: attributedToAccount
ObjectProperty: explainedBy

FirstReportedAccount:
    firstDhyana: SeparationBornRaptureAndPleasureAbsent
    secondDhyana: InwardClarityAbsent
    thirdDhyana: MindfulnessAndClearComprehensionAbsent
    fourthDhyana: EquanimityAndMindfulnessPurificationAbsent
    mode: Defiled
    attribution: SomeAuthorities

SecondReportedAccount:
    firstAndSecondDhyanas: PliancyAbsent
    thirdAndFourthDhyanas: EquanimityAbsent
    reason: FactorsBelongToWholesomeClass
    mode: Defiled
    attribution: OtherAuthorities

ProjectConstraint: Preserve the level scope of every absence.
ProjectConstraint: Preserve separation-born and purification qualifications.
ProjectConstraint: Do not equate defiled with all contaminated attainment.
ProjectConstraint: Absence of purification alone does not prove factor presence.
ProjectConstraint: Do not merge reported accounts into a universal absence list.
ProjectConstraint: No final adjudication is supplied in this source unit.
```

This is a declarative project seed, not executable OWL.
VAK 8.11 next explains the fourth dhyāna's immovability
through freedom from eight disturbances.
