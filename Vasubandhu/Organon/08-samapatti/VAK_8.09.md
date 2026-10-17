# VAK_8.09 — Eleven Distinct Dhyāna Factors

## 1. Sanskrit (Devanāgarī)

```sanskrit
द्रव्यतो दश चैकं च प्रस्रब्धिः सुखमाद्ययोः ।
श्रद्धा प्रसादः प्रीतिस्तु सौमनस्यं द्विधागमात् ॥ ८.०९ ॥
```

## 2. Sanskrit (IAST)

```text
dravyato daśa caikaṃ ca prasrabdhiḥ sukham ādyayoḥ |
śraddhā prasādaḥ prītis tu saumanasyaṃ dvidhāgamāt || 8.09 ||
```

The verse follows the local kārikā witness. The running
Bhāṣya quotes the pleasure clause as `prasrabdhisukhamādyayoḥ`;
the local verse's explicit `prasrabdhiḥ sukham` is retained.
The prose unambiguously determines the count as eleven.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `dravyataḥ` | adverb with -tas | by substance; counting distinct dharmas |
| `daśa` | numeral (`daśa ca ekam` → `daśa caikam`) | ten |
| `ca … ca` | coordinating particles | and; joins ten and one |
| `ekam` | nominative singular neuter numeral | one [additional factor] |
| `prasrabdhiḥ` | nominative singular feminine | pliancy |
| `sukham` | nominative singular neuter | pleasure or ease, contextually determined |
| `ādyayoḥ` | locative dual of `ādya` | in the first two [dhyānas] |
| `śraddhā` | nominative singular feminine | confidence or faith |
| `prasādaḥ` | nominative singular masculine | clarity, here inward clarity |
| `prītiḥ` | nominative singular feminine (`prītiḥ tu` → `prītis tu`) | rapture or joy |
| `tu` | particle | however; marks the next determination |
| `saumanasyam` | nominative singular neuter | pleasant-mindedness; mental joy |
| `dvidhā` | adverb (`dvidhā āgamāt` → `dvidhāgamāt`) | in two ways, here through two scriptural statements |
| `āgamāt` | ablative singular masculine | because of scriptural testimony; supplies the warrant for identifying prīti with saumanasya |

## 4. Grammar

The numerals yield eleven distinct factors, while the following equations identify selected members. `Ādyayoḥ` restricts pliancy-sukha to the first two dhyānas; the Bhāṣya reports a competing bodily-pleasure account without making it the principal reading.

```nltk-fcfg
% start S
# tokens: dravyato daśa ca ekam ca prasrabdhiḥ sukham ādyayoḥ śraddhā prasādaḥ prītiḥ tu saumanasyam dvidhāgamāt
S -> CL[K=count] CL[K=first_two] CL[K=clarity] CL[K=joy]
CL[K=count] -> ADV[COUNT=by_substance] NUM[VALUE=ten] CONJ[COORD=yes] NUM[VALUE=one] CONJ[COORD=yes]
CL[K=first_two] -> N[CASE=nom,NUM=sg,GEN=f] N[CASE=nom,NUM=sg,GEN=n,IDENTITY=pliancy] LOC[CASE=loc,NUM=du,GEN=n]
CL[K=clarity] -> N[CASE=nom,NUM=sg,GEN=f] N[CASE=nom,NUM=sg,GEN=m,IDENTITY=faith]
CL[K=joy] -> N[CASE=nom,NUM=sg,GEN=f] PTCL[CONTRAST=yes] N[CASE=nom,NUM=sg,GEN=n,IDENTITY=mental_joy] ABL[CASE=abl,NUM=sg,GEN=m,SOURCE=scripture]
ADV[COUNT=by_substance] -> 'dravyato'
NUM[VALUE=ten] -> 'daśa'
CONJ[COORD=yes] -> 'ca'
NUM[VALUE=one] -> 'ekam'
N[CASE=nom,NUM=sg,GEN=f] -> 'prasrabdhiḥ'
N[CASE=nom,NUM=sg,GEN=n,IDENTITY=pliancy] -> 'sukham'
LOC[CASE=loc,NUM=du,GEN=n] -> 'ādyayoḥ'
N[CASE=nom,NUM=sg,GEN=f] -> 'śraddhā'
N[CASE=nom,NUM=sg,GEN=m,IDENTITY=faith] -> 'prasādaḥ'
N[CASE=nom,NUM=sg,GEN=f] -> 'prītiḥ'
PTCL[CONTRAST=yes] -> 'tu'
N[CASE=nom,NUM=sg,GEN=n,IDENTITY=mental_joy] -> 'saumanasyam'
ABL[CASE=abl,NUM=sg,GEN=m,SOURCE=scripture] -> 'dvidhāgamāt'
```

```nltk-dep
'daśa' -> 'dravyato' | 'ca' | 'ekam' | 'ca'
'sukham' -> 'prasrabdhiḥ' | 'ādyayoḥ'
'prasādaḥ' -> 'śraddhā'
'saumanasyam' -> 'prītiḥ' | 'tu' | 'dvidhāgamāt'
```

`Prasāda` is identified with śraddhā; prīti with saumanasya on two scriptural statements, not two occurrences. Pleasure in the third dhyāna remains a distinct feeling.


**Close construe.** By distinct dharma, the factors are
ten and one. In the first two dhyānas, sukha is pliancy.
Inward clarity is confidence. Prīti is pleasant-mindedness,
on the grounds of two scriptural statements.

## 5. Translation

### Literal Translation

> By substance, [there are] ten and one. In the first
> two, pleasure is pliancy. Clarity is confidence;
> rapture, however, is pleasant-mindedness, because
> of scriptural testimony in two forms.

### Bhāṣya-informed study translation

> The eighteen factors counted by name are, by substance, ten and
> one, that is, eleven distinct dharmas. In the first two dhyānas
> the pleasure is pliancy; inward clarity is confidence; rapture,
> however, is mental joy, as scripture states it in two ways.

## 6. Philosophical Translation

> Counting a factor's named role in each attainment
> differs from counting the distinct dharmas that bear
> those roles. A recurring name can designate different
> dharmas according to its setting, while differently
> named or qualified roles can recur without adding
> a new kind to the substantial inventory.

Sukha is the decisive example: its first-two-dhyāna
and third-dhyāna determinations are not interchangeable
in the counting scheme presented here. The shift from
eighteen to eleven therefore requires interpretation,
not merely removal of repeated words.

## 7. Technical Vocabulary

**`Dravyataḥ`.** By substance or distinct dharma. Here
it answers how many distinct factors underlie the four
lists. It does not count eighteen simultaneous entities
or posit a permanent substrate of concentration.

**`Prasrabdhi`.** Pliancy, identified with the first two
dhyānas' sukha in the kārikā's account. This identification
is defended and contested in the prose; it must not
be generalized into a definition of every use of sukha.

**`Vedanāsukha`.** Pleasure as feeling, explicitly the
third dhyāna's sukha in the principal recount. It adds
a distinct factor to those already counted.

**`Adhyātmasaṃprasāda`.** Inward clarity. The prose first
describes the peaceful flow of the continuum without
the disturbance of vitarka and vicāra, like a river
without waves. The identity with śraddhā supplies its
distinct-dharma determination in the elevenfold account.

**`Śraddhā`.** Confidence or faith. This is the kārikā's
answer to what inward clarity is, rather than a new
factor added beside inward clarity in the same list.

**`Prīti / saumanasya`.** Rapture / pleasant-mindedness.
The stated identification makes prīti mental joy and
keeps it distinct from the third dhyāna's pleasure.
The prose reports other schools' different determinations.

**`Aṅga`.** A selected factor of an attainment. Being
counted as an aṅga is distinct from being every dharma
present in that attainment. Adding a factor to the
cumulative inventory does not establish its universal
absence from all earlier states.

## 8. Logical Determination

The verse converts the eighteen name-roles into eleven distinct dharma determinations and identifies selected terms [verse; prose]. The Bhāṣya distinguishes first-two-dhyāna pliancy-sukha from third-dhyāna feeling-sukha, while leaving a reported bodily-pleasure alternative for examination.

**Signature.** `Role(level,name,dharmic-kind)`; `SameDharma(x,y)`; `DifferentDharma(x,y)`; `DistinctTotal(n)`.

**Finite data.** Repeated names and equivalent names map differently: the two sukhas are distinct; inward clarity and confidence, and prīti and saumanasya, are identified in the stated account.

```nltk-valuation
first => first
second => second
third => third
fourth => fourth
firstsukha => firstsukha
thirdsukha => thirdsukha
pliancy => pliancy
feelingpleasure => feelingpleasure
prasada => prasada
faith => faith
priti => priti
saumanasya => saumanasya
eleven => eleven
Role => {(first,firstsukha,pliancy),(second,firstsukha,pliancy),(third,thirdsukha,feelingpleasure),(second,prasada,faith),(second,priti,saumanasya)}
SameDharma => {(prasada,faith),(priti,saumanasya)}
DifferentDharma => {(firstsukha,thirdsukha)}
DistinctTotal => {eleven}
```

**Rules (verse and prose).**

```nltk-fol
# THEORY stated_account
# [verse] daśa ca ekam; [prose] eleven distinct dharmas
DistinctTotal(eleven)
# [verse] ādyayoḥ; [prose] first-two-dhyāna sukha is pliancy
Role(first,firstsukha,pliancy)
Role(second,firstsukha,pliancy)
# [prose] third sukha is feeling-pleasure, not the same dharma
Role(third,thirdsukha,feelingpleasure)
DifferentDharma(firstsukha,thirdsukha)
# [verse] prasāda, śraddhā; prīti, saumanasya: two identifications
SameDharma(prasada,faith)
SameDharma(priti,saumanasya)
Role(second,prasada,faith)
Role(second,priti,saumanasya)
```

**Results (NLTK).** The checker parses the stated-account theory and confirms it in the finite model. It does not calculate eleven from an exhaustive census here; the roster illustrates the identifications and the sukha split.

**Scope cautions.** `dvidhāgamāt` means two scriptural warrants, not two occurrences. The bodily-pleasure account (`apare`) is reported, debated, and left for examination; it is not merged with the stated role mapping. The prose's `vicāryam` keeps that dispute open, and the count is not a claim of simultaneous presence.

## 9. Interpretive Note

**Correction of the research draft.** The local
kārikā research file initially gives ten. Its Bhāṣya
study corrects this to eleven, and both the verse's
“ten and one” and the running prose establish the
correction. This official study adopts eleven while
leaving the research witnesses unchanged.

**The prose controls more than a gloss.** Its competing
accounts prevent presenting the identifications as a
consensus across all schools. The kārikā's stated
scheme, its supporting reasoning, and the reported
objections each have a place. The source's call for
examination should not be rewritten as a decisive
refutation of every alternative.

**Witness cautions.** The running text has duplicated
lines in the report of other schools near 440|14–15
and damaged wording in the explanation of confidence
near 440|10. These are not grounds for inventing an
additional argument. The count, the śraddhā identification,
and the two scriptural warrants are explicit. The
verse/prose difference in the pliancy clause is noted
above; originals remain intact.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates which determination a term bears
within a system of relations. Yoga Technē, its kriyā–karma
companion, concerns the effective exercise of those
determinations. Here the same word sukha requires a
level-specific account before its operational role
can be represented responsibly.

For Organon, preserve the named role, its attainment,
its proposed underlying dharma, and the source position
that licenses the identification. This permits eighteen
roles and eleven distinct dharmas without flattening
qualifications or suppressing competing analyses. It
is a project reconstruction, not an attribution of
Organon architecture to Vasubandhu.

**Review status.** Provisional, Bhāṣya-controlled study.
The elevenfold count, its cumulative construction,
the three identifications, the major reported alternatives,
and both scriptural warrants have been checked against
the local research material and running source. Damaged
wording has not been silently reconstructed.

## 10. OWL++ Seed

```text
Class: DhyanaFactorRole
Class: DistinctFactorDharma
Class: SourcePosition
Class: ScripturalWarrant

ObjectProperty: belongsToDhyana
ObjectProperty: identifiedWithUnderPosition
ObjectProperty: supportedBy

PrincipalFactorAccount:
    namedRoleCount: 18
    distinctDharmaCount: 11
    cumulativeAdditions: 5, 1, 4, 1

SukhaInFirstTwoDhyanas:
    identifiedDharma: Prasrabdhi
    position: PrincipalFactorAccount

SukhaInThirdDhyana:
    identifiedDharma: PleasureFeeling
    position: PrincipalFactorAccount

InwardClarity:
    identifiedDharma: Sraddha
    position: PrincipalFactorAccount

Priti:
    identifiedDharma: Saumanasya
    position: PrincipalFactorAccount
    warrants: AviparitakaPassage, FourthDhyanaFormula

ProjectConstraint: Preserve named-role and distinct-dharma counts separately.
ProjectConstraint: Resolve sukha by attainment and source position.
ProjectConstraint: A newly counted factor need not be wholly absent earlier.
ProjectConstraint: Preserve purification without adding a distinct dharma.
ProjectConstraint: Reported alternatives are not principal-account assertions.
ProjectConstraint: Keep the source call for examination explicit.
```

This is a declarative project seed, not executable OWL.
VAK 8.10 next examines which factors are absent from
defiled dhyānas.
