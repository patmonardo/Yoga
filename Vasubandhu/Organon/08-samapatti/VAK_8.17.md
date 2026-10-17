# VAK_8.17 — Four Orientations of Pure Attainment

## 1. Sanskrit (Devanāgarī)

```sanskrit
चतुर्धा शुद्धकं हानभागीयादि यथाक्रमम् ।
क्लेशोत्पत्तिस्वभूम्यूर्ध्वानास्रवानुगुणं हि तत् ॥ ८.१७ ॥
```

## 2. Sanskrit (IAST)

```text
caturdhā śuddhakaṃ hānabhāgīyādi yathākramam |
kleśotpattisvabhūmyūrdhvānāsravānuguṇaṃ hi tat || 8.17 ||
```

The Sanskrit follows the local kārikā witness, with
editorial hyphens in its IAST compound removed for
continuous presentation. The prose's initial enumeration
and its later functional mapping differ in order;
that difference is disclosed below.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `caturdhā` | numeral adverb | fourfold; in four ways |
| `śuddhakam` | nominative singular neuter | pure attainment |
| `hānabhāgīyādi` | nominative singular neuter compound | beginning with the decline-conducive type |
| `yathākramam` | adverbial compound | respectively; according to order |
| `kleśotpatti` | compound member | arising of defilements |
| `svabhūmi` | compound member | its own level |
| `ūrdhva` | compound member, expanded as ūrdhvabhūmi in prose | a higher level |
| `anāsrava` | compound member | uncontaminated attainment |
| `anuguṇam` | nominative singular neuter predicate | conducive or favorable to |
| `hi` | explanatory particle | for; indeed |
| `tat` | nominative singular neuter pronoun | that [pure attainment, distributed by subtype] |

`Kleśa + utpatti` yields `kleśotpatti`;
`svabhūmi + ūrdhva` yields `svabhūmyūrdhva`;
`ūrdhva + anāsrava` yields `ūrdhvānāsrava`;
`anāsrava + anuguṇa` yields `anāsravānuguṇa`.

## 4. Grammar

The verse classifies pure attainment, while the Bhāṣya supplies the three names after adi and maps each subtype to its favored outcome.

```nltk-fcfg
% start S
# tokens: caturdhā śuddhakaṃ hānabhāgīyādi yathākramam ∅-sthitibhāgīyam ∅-viśeṣabhāgīyam ∅-nirvedhabhāgīyam kleśotpattisvabhūmyūrdhvānāsravānuguṇaṃ hi tat
S -> CL[K=classification] CL[K=orientation]
CL[K=classification] -> ADV[COUNT=four] N[CASE=nom,NUM=sg,GEN=n,KIND=pure] TYPE[ORDER=first] ADV[ORDER=respectively] TYPE[ORDER=second,SUPPLIED=prose] TYPE[ORDER=third,SUPPLIED=prose] TYPE[ORDER=fourth,SUPPLIED=prose]
CL[K=orientation] -> PRED[REL=sequence,NUM=?n,GEN=?g] PTCL[EXPLAIN=yes] PRON[CASE=nom,NUM=?n,GEN=?g,REF=pure]
ADV[COUNT=four] -> 'caturdhā'
N[CASE=nom,NUM=sg,GEN=n,KIND=pure] -> 'śuddhakaṃ'
TYPE[ORDER=first] -> 'hānabhāgīyādi'
ADV[ORDER=respectively] -> 'yathākramam'
TYPE[ORDER=second,SUPPLIED=prose] -> '∅-sthitibhāgīyam'
TYPE[ORDER=third,SUPPLIED=prose] -> '∅-viśeṣabhāgīyam'
TYPE[ORDER=fourth,SUPPLIED=prose] -> '∅-nirvedhabhāgīyam'
PRED[REL=sequence,NUM=sg,GEN=n] -> 'kleśotpattisvabhūmyūrdhvānāsravānuguṇaṃ'
PTCL[EXPLAIN=yes] -> 'hi'
PRON[CASE=nom,NUM=sg,GEN=n,REF=pure] -> 'tat'
```

```nltk-dep
'śuddhakaṃ' -> 'caturdhā' | 'hānabhāgīyādi' | '∅-sthitibhāgīyam' | '∅-viśeṣabhāgīyam' | '∅-nirvedhabhāgīyam'
'tat' -> 'kleśotpattisvabhūmyūrdhvānāsravānuguṇaṃ' | 'hi' | 'yathākramam'
```

The functional mapping governs: stability favors its own level and distinction favors a
higher one, despite their reversed order in the Bhāṣya's initial list. Hānabhāgīya
remains pure, not already defiled; conducive does not mean inevitable next.

**Close construe.** Pure attainment is fourfold, beginning
with the decline-conducive type; for the types are
respectively conducive to the arising of defilements,
to their own level, to a higher level, and to
uncontaminated attainment.

## 5. Translation

### Literal Translation

> Pure attainment is fourfold, beginning with that
> conducive to decline. For it is respectively
> conducive to the arising of defilements, to its
> own level, to a higher level, and to the uncontaminated.

### Bhāṣya-informed study translation

> Pure attainment is of four kinds, beginning with the decline-conducive
> and followed in order by the stability-conducive, the
> distinction-conducive, and the penetration-conducive; for, in that
> order, it is conducive to the arising of defilements, to its own
> level, to a higher level, and to the uncontaminated.

## 6. Philosophical Translation

> Present purity does not exhaust the determination
> of an attainment. Within the pure class, the
> commentary distinguishes what favors renewed defilement,
> what favors the existing level, what favors a
> higher level, and what favors the uncontaminated.
> These orientations refine the earlier general rule
> concerning successors of pure attainment.

Conduciveness is not a prediction that the named
result must occur next in every instance. The following
verse separately enumerates immediate successors among
the four pure types themselves.

## 7. Technical Vocabulary

**Source.** Pradhan 445|02–445|10, checked against the local Bhāṣya
study and running source. The Bhāṣya's opening qualification (not every
pure attainment is followed by an uncontaminated one) ties the verse to
VAK 8.15; at the summit of existence only three types occur, the
distinction-conducive being absent. The verse's `ādi` is filled by the
three further names in the commentary's order, while the mapping to
functions follows `yathākramam`.

**`Śuddhaka`.** Pure attainment: wholesome but contaminated,
kept distinct from anāsrava. Each of the four types
belongs to this class, including the decline-conducive type.

**`Hānabhāgīya`.** Conducive to decline. Its explicit
mark is favoring kleśotpatti, the arising of defilements.
The present pure attainment must not be relabeled
defiled merely because its orientation is toward decline.

**`Sthitibhāgīya`.** Conducive to stability. Its explicit
relation is to svabhūmi, its own level. The designation
does not assert permanent possession or impossibility
of any later change.

**`Viśeṣabhāgīya`.** Conducive to distinction or advancement.
The prose specifies a higher bhūmi. Here viśeṣa
is therefore more determinate than a generic improvement
unrelated to level.

**`Nirvedhabhāgīya`.** Conducive to penetration. Its
mark here is favoring uncontaminated attainment.
The pure precursor and the uncontaminated successor
remain distinct; this local classification does not
by itself import every subdivision of the earlier
Path discussion bearing the same term.

**`Anuguṇa`.** Conducive or favorable to. This is
the defining relation, rather than mere similarity
of labels. The concluding `tasmād anāsravam utpadyate`
adds an explicit arising statement for the penetration-conducive type.

**`Bhavāgra`.** Summit of existence. Its pure attainment
lacks the higher-level-oriented subtype. The source
retains the other three; this does not supply an
uncontaminated attainment native to the summit.

## 8. Logical Determination

The verse classifies pure attainment by four orientations; the Bhāṣya supplies all four names and maps each to what it favors. “Conducive” is not an assertion that the outcome must occur. Provenance: `[verse]`, `[prose]`.

**Signature.** `PureType/1(t)`—pure subtype; `Orientation/1(o)`—favorable outcome category; `Favors/2(t,o)`—subtype t is conducive to o; `PresentAtSummit/1(t)`—subtype occurs at bhavāgra.

**Composition.** No compositional paraphrase is needed: the verse asserts a four-member classification and an ordered correspondence, represented as a finite relation.

```nltk-valuation
hanaType => hanaType
stabilityType => stabilityType
distinctionType => distinctionType
penetrationType => penetrationType
defilementRise => defilementRise
ownLevel => ownLevel
higherLevel => higherLevel
uncontaminated => uncontaminated
summit => summit
PureType => {hanaType,stabilityType,distinctionType,penetrationType}
Orientation => {defilementRise,ownLevel,higherLevel,uncontaminated}
Favors => {(hanaType,defilementRise),(stabilityType,ownLevel),(distinctionType,higherLevel),(penetrationType,uncontaminated)}
PresentAtSummit => {}
```

```nltk-fol
# THEORY shared
# [verse] fourfold pure classification and the ordered favorable outcomes [prose]
all t.(PureType(t) -> exists o.(Orientation(o) & Favors(t,o)))
all t.all o.((PureType(t) & Favors(t,o)) -> Orientation(o))
# [prose] bhavāgra lacks the higher-level-oriented subtype
-PresentAtSummit(distinctionType)
```

**Results (NLTK).** `Model.satisfy` checks the two relational rules against the four listed type–orientation pairs. The last line records the Bhāṣya's summit restriction, not an inference that the type is already defiled.

**Scope cautions.** The opening enumeration order in the Bhāṣya differs from its functional mapping; the latter controls this relation. The verse does not assert that an orientation inevitably produces its favored outcome, nor that the summit has an uncontaminated attainment of its own. Actual successor membership is treated separately in VAK 8.18.

## 9. Interpretive Note

**The source-order difference matters.** At 445|05
the transmitted list is hānabhāgīya, viśeṣabhāgīya,
sthitibhāgīya, nirvedhabhāgīya. At 445|09–10 each
name receives an explicit function, producing the
order used in the study table. The witness is
preserved; no silent transposition is made in the
research or running source.

**Keep developmental language proportional.** The research
speaks of internal tendencies and transition potential.
The source warrants classification by anuguṇa and
an explicit uncontaminated arising from the last type.
It does not require an additional hidden entity,
a deterministic forecast, or a complete causal theory
of every possible later development.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates the pure mode together with
its particular orientation. Yoga Technē, its kriyā–karma
companion, concerns the effective exercise for which
that orientation matters. A shared present classification
does not erase the difference between maintaining a
level, advancing to another, and favoring uncontaminated attainment.

For Organon representation, record the anuguṇa relation
separately from actual succession and preserve the
summit's three-type restriction. This permits the next
verse's successor counts to add information without
replacing the present definitions. This is a project
reconstruction, not an additional doctrine attributed
to Vasubandhu.

**Review status.** Provisional, Bhāṣya-controlled study.
The introductory restriction, four explicit functional
mappings, source-order discrepancy, summit exception,
and final arising statement have been checked against
the local research and running source.

## 10. OWL++ Seed

```text
Class: PureAttainment
Class: PureAttainmentSubtype
Class: ConducivenessRelation

ObjectProperty: hasPureSubtype
ObjectProperty: isConduciveTo
ObjectProperty: occursAtLevel

Hanabhagiya:
    parentMode: Pure
    conduciveTo: ArisingOfDefilements

Sthitibhagiya:
    parentMode: Pure
    conduciveTo: OwnLevel

Visesabhagiya:
    parentMode: Pure
    conduciveTo: HigherLevel

Nirvedhabhagiya:
    parentMode: Pure
    conduciveTo: UncontaminatedAttainment
    proseResult: UncontaminatedAttainmentArisesFromThisType

BhavagraPureAttainment:
    availableTypes: Hanabhagiya, Sthitibhagiya, Nirvedhabhagiya
    excludedType: Visesabhagiya

ProjectConstraint: Pure precursor is distinct from its favored result.
ProjectConstraint: Conduciveness is not an inevitable next occurrence.
ProjectConstraint: Not every pure attainment yields an uncontaminated successor.
ProjectConstraint: Retain the explicit mappings despite the initial list order.
ProjectConstraint: Do not infer an uncontaminated attainment native to bhavagra.
ProjectConstraint: Fourfold mapping is not a mandatory four-stage itinerary.
ProjectConstraint: Immediate pure-subtype successor counts continue in VAK 8.18.
```

This is a declarative project seed, not executable OWL.
VAK 8.18 next gives the immediate-successor counts
among the pure types and begins the account of
practice that skips attainment levels.
