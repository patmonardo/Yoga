# VAK_8.23 — Intermediate Dhyāna and the Vitarka–Vicāra Classification

## 1. Sanskrit (Devanāgarī)

```sanskrit
त्रिधा अदुःखासुखं तच्च महाब्रह्मफलं च तत् ।
सवितर्कविचारोऽधःसमाधिः परतोऽद्वयः ॥ ८.२३ ॥
```

## 2. Sanskrit (IAST)

```text
tridhā aduḥkhāsukhaṃ tac ca mahābrahmaphalaṃ ca tat |
savitarkavicāro 'dhaḥsamādhiḥ parato 'dvayaḥ || 8.23 ||
```

The Sanskrit follows the local kārikā witness, including
the separation after tridhā. The running commentary
quotes its clauses separately. The referent of tat
is the intermediate dhyāna introduced in VAK 8.22.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `tridhā` | adverb | threefold, here in attainment mode |
| `aduḥkhāsukham` | nominative singular neuter | neither painful nor pleasant |
| `tat` | nominative singular neuter pronoun | that intermediate dhyāna |
| `ca` | conjunction | and |
| `mahābrahmaphalam` | nominative singular neuter compound adjective | having the Mahābrahmā state as its result |
| `savitarkavicāraḥ` | nominative singular masculine compound adjective | accompanied by vitarka and vicāra |
| `adhaḥsamādhiḥ` | nominative singular masculine expression | samādhi below [the intermediate dhyāna] |
| `parataḥ` | adverb | beyond it; above it |
| `advayaḥ` | nominative singular masculine adjective | without the two specified factors |

`Tat + ca` yields `tac ca`; `savitarkavicāraḥ +
adhaḥ-` yields `savitarkavicāro 'dhaḥ-`; `parataḥ +
advayaḥ` yields `parato 'dvayaḥ`. The final dvaya
refers to vitarka and vicāra, not an unspecified
metaphysical duality.

## 4. Grammar

The first predicates characterize intermediate dhyāna; masculine samādhi clauses then contrast below with above, with the latter subject carried from context.

```nltk-fcfg
% start S
# tokens: tridhā aduḥkhāsukham tat ca mahābrahmaphalam ca tat savitarkavicāraḥ adhaḥsamādhiḥ ∅-samādhiḥ parataḥ advayaḥ
S -> CL[K=intermediate_properties] CL[K=below] CL[K=above]
CL[K=intermediate_properties] -> ADV[COUNT=three] ADJ[CASE=nom,NUM=?n,GEN=?g,QUALITY=neutral] PRON[CASE=nom,NUM=?n,GEN=?g,REF=intermediate] CONJ ADJ[CASE=nom,NUM=?n,GEN=?g,RESULT=Mahabrahma] CONJ PRON[CASE=nom,NUM=?n,GEN=?g,REF=intermediate]
CL[K=below] -> ADJ[CASE=nom,NUM=?n,GEN=?g,FACTORS=both] N[CASE=nom,NUM=?n,GEN=?g,KIND=samadhi,REL=below]
CL[K=above] -> N[CASE=nom,NUM=?n,GEN=?g,KIND=samadhi,SUPPLIED=prose] ADV[REL=above] ADJ[CASE=nom,NUM=?n,GEN=?g,FACTORS=neither]
ADV[COUNT=three] -> 'tridhā'
ADJ[CASE=nom,NUM=sg,GEN=n,QUALITY=neutral] -> 'aduḥkhāsukham'
PRON[CASE=nom,NUM=sg,GEN=n,REF=intermediate] -> 'tat'
CONJ -> 'ca'
ADJ[CASE=nom,NUM=sg,GEN=n,RESULT=Mahabrahma] -> 'mahābrahmaphalam'
ADJ[CASE=nom,NUM=sg,GEN=m,FACTORS=both] -> 'savitarkavicāraḥ'
N[CASE=nom,NUM=sg,GEN=m,KIND=samadhi,REL=below] -> 'adhaḥsamādhiḥ'
N[CASE=nom,NUM=sg,GEN=m,KIND=samadhi,SUPPLIED=prose] -> '∅-samādhiḥ'
ADV[REL=above] -> 'parataḥ'
ADJ[CASE=nom,NUM=sg,GEN=m,FACTORS=neither] -> 'advayaḥ'
```

```nltk-dep
'tat' -> 'tridhā' | 'aduḥkhāsukham' | 'ca' | 'mahābrahmaphalam' | 'ca'
'adhaḥsamādhiḥ' -> 'savitarkavicāraḥ'
'∅-samādhiḥ' -> 'parataḥ' | 'advayaḥ'
```

Tridhā here applies to intermediate attainment modes, not the reported first-access view
of 8.22. Neutral feeling differs from difficult progress; advaya is explicitly absence
of vitarka and vicāra, not metaphysical nonduality. Vicāra alone marks the pairwise
middle, not the only mental factor.

**Close construe.** Intermediate dhyāna has three modes,
neutral feeling, and Mahābrahmā as its distinctive
result. Below it samādhi has vitarka and vicāra;
above it samādhi lacks both. Intermediate dhyāna
itself lacks vitarka while retaining vicāra.

## 5. Translation

### Literal Translation

> That [intermediate dhyāna] is threefold and neither painful nor pleasant,
> and that [dhyāna] has Mahābrahmā as its result. Samādhi
> below it is accompanied by vitarka and vicāra;
> beyond it, samādhi is without the two.

### Bhāṣya-informed study translation

> That intermediate dhyāna is threefold, neither painful nor pleasant,
> and has Mahābrahmā as its result. Samādhi below it is accompanied
> by vitarka and vicāra; beyond it, samādhi is without both.

## 6. Philosophical Translation

> Intermediate dhyāna has its own determinate constitution:
> mode, feeling, effort, result, and a specific
> position in the vitarka–vicāra classification. The
> middle position preserves one of the pair while
> excluding the other. The higher range excludes
> both without thereby excluding all mental factors.

The factor classification is not a mandatory itinerary
for every practitioner. Its ordered distinctions should
not be silently equated with the immediate-successor
rules already studied.

## 7. Technical Vocabulary

**`Dhyānāntara`.** Intermediate dhyāna. Its three modes
are distinct from the first-access disagreement of
VAK 8.22. Access and intermediate dhyāna remain
different determinations.

**`Upekṣendriya`.** Neutral-feeling faculty. This positively
specifies aduḥkhāsukha; the attainment does not lack
feeling altogether. The faculty is distinct from
the wholesome equanimity factor and from ethical neutrality.

**`Sābhisaṃskāravāhitva`.** Proceeding with effort or
active exertion. The commentary invokes this to
explain absence of prīti and the difficult mode
of progress. It does not assert absence of the
neutral feeling already specified.

**`Duḥkhā pratipat`.** Difficult mode of progress.
This classifies the manner of practice, not painful
feeling in the attainment. Neutral vedanā and difficult
pratipad answer different questions.

**`Mahābrahmaphala`.** Having Mahābrahmā as result.
The prose says that through cultivation of intermediate
dhyāna one becomes Mahābrahmā. This is a cosmological
result, not a synonym for liberation or knowledge
of destruction. Source: Pradhan 448|11–449|07. The result statement
is preserved as the source's cultivation claim, not as an assertion
that every mode or occurrence produces rebirth as Mahābrahmā.

**`Savitarka savicāra`.** With both vitarka and vicāra.
The prose includes anāgamya as well as first dhyāna
in this category.

**`Avitarka vicāramātra`.** Without vitarka, with vicāra
alone among the two. This identifies the middle
samādhi category.

**`Avitarka avicāra / advaya`.** Without vitarka and
without vicāra / without the pair. The upper range
begins with second-dhyāna access, not only with
principal second dhyāna.

## 8. Logical Determination

**The intermediate attainment's distinct classifications.**

| Question | Answer in the prose |
|---|---|
| What modes? | Savoring-associated, pure, uncontaminated |
| What feeling? | Neutral-feeling faculty |
| Is prīti present? | No |
| Why is prīti absent? | The course involves effort |
| What mode of progress? | Difficult, for the same reason |
| What distinctive result? | Mahābrahmā through cultivation |
| Which member of the factor triad? | No vitarka, vicāra retained |

Neither the difficult-progress designation nor the
savoring mode changes neutral feeling into painful
or pleasant feeling. Mode, vedanā, and manner of
progress remain separately classified.

**The sūtra's threefold factor classification.**

| Range | Vitarka | Vicāra |
|---|---|---|
| Anāgamya and first dhyāna | Present | Present |
| Intermediate dhyāna | Absent | Present |
| Second-dhyāna access through bhavāgra | Absent | Absent |

The commentary attributes the threefold grouping to
a sūtra and explicitly locates its members. The
last range includes access stages; the first includes
anāgamya. A table limited to principal dhyānas would
omit part of its scope.

**The middle does not contain only one factor.**
Vicāramātra contrasts with the two-factor pair under
discussion. The same passage assigns neutral feeling
and speaks of samādhi. Reading “vicāra alone” as
an exhaustive inventory of all dharmas would contradict
that context.

**Three combinations do not establish a fourth.**
The text gives both present, vicāra without vitarka,
and neither. It does not posit a fourth samādhi
with vitarka but no vicāra merely to complete a
formal two-by-two matrix. The source's classifications
govern the representation.

**Result must not be distributed indiscriminately across modes.**
The prose states both the three modes and the
Mahābrahmā result. It does not specify here a
separate result rule for each mode. The study
therefore records the cultivation result without asserting
that uncontaminated attainment generates cosmological rebirth.

**The next triad asks another question.** After
completing this classification, the prose introduces
emptiness, wishlessness, and signlessness samādhis.
Those are not new names for the three vitarka–vicāra
configurations. Their determinations begin with VAK 8.24.

## 9. Interpretive Note

**Neutral feeling and difficult practice are compatible.**
A translation that renders duḥkhā pratipat simply
as a painful feeling would make the commentary
appear inconsistent. The source expressly gives neutral
feeling and then classifies progress as difficult
through its effortful course. Both should remain explicit.

**Avoid an unsupported metaphysical reading of advaya.**
The prose identifies the missing pair as vitarka
and vicāra. No general subject–object nonduality is
asserted by this local adjective. The positive factor
classification supplies its meaning.

**Witness cautions.** The running source prints
`samādhhir` in its explanation of the middle member.
The surrounding statements and repeated samādhi forms
secure the reading. The local verse separates the
first two predicates, while the running commentary
quotes them independently. Originals remain untouched;
no critical reconstruction is claimed.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates the pair's three source-attested
configurations alongside mode, feeling, and result.
Yoga Technē, its kriyā–karma companion, concerns the
cultivation and effort described in the passage.
Neither classification should erase the other: neutral
feeling does not settle how practice proceeds, and
factor absence does not settle ethical mode.

For Organon representation, distinguish a classified
configuration from an asserted transition between configurations.
Keep the neutral-feeling and difficult-progress predicates
separate, and do not add an unattested fourth
combination for formal symmetry. This is project
reconstruction, not a further theory attributed to
the Bhāṣya.

**Review status.** Provisional, Bhāṣya-controlled study.
The three modes, neutral feeling, absence of prīti,
effort explanation, difficult progress, Mahābrahmā result,
and exact ranges of the three samādhi categories
have been checked against the local research and
running source.

## 10. OWL++ Seed

```text
Class: IntermediateDhyana
Class: FactorConfiguration
Class: FeelingClassification
Class: ProgressClassification

ObjectProperty: hasAvailableMode
ObjectProperty: hasFeelingFaculty
ObjectProperty: hasFactorConfiguration
ObjectProperty: hasProgressClassification
ObjectProperty: hasStatedCultivationResult

IntermediateDhyana:
    modes: SavoringAssociated, Pure, Uncontaminated
    feelingFaculty: NeutralFeeling
    priti: absent
    course: WithEffort
    progress: Difficult
    statedCultivationResult: Mahabrahma
    factorPair: VitarkaAbsent, VicaraPresent

AnagamyaAndFirstDhyana:
    factorPair: VitarkaPresent, VicaraPresent

SecondDhyanaAccessThroughBhavagra:
    factorPair: VitarkaAbsent, VicaraAbsent

ProjectConstraint: Difficult progress is not painful feeling.
ProjectConstraint: Vicara alone is relative to the specified pair.
ProjectConstraint: Advaya here means without vitarka and vicara.
ProjectConstraint: Do not invent a vitarka-only fourth category.
ProjectConstraint: Do not infer mandatory succession from classification order.
ProjectConstraint: Do not distribute the rebirth result across all modes blindly.
ProjectConstraint: The next samadhi triad is a separate classification.
```

This is a declarative project seed, not executable OWL.
VAK 8.24 next begins the analysis of signlessness,
emptiness, and wishlessness samādhis.
