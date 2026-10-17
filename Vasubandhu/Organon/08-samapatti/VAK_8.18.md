# VAK_8.18 — Pure-Type Successors and Preparation for Skipping Levels

## 1. Sanskrit (Devanāgarī)

```sanskrit
द्वे त्रीणि त्रीणि चैकं च हानभागाद्यनन्तरम् ।
गत्वागम्य द्विधा भूमीरष्टौ श्लिष्टैकलङ्घिताः ॥ ८.१८ ॥
```

## 2. Sanskrit (IAST)

```text
dve trīṇi trīṇi caikaṃ ca hānabhāgādyanantaram |
gatvāgamya dvidhā bhūmīr aṣṭau śliṣṭaikalaṅghitāḥ || 8.18 ||
```

The Sanskrit follows the local kārikā study. The
running source separates `hāna bhāgādyanantaram`;
the study joins the expression. The second half
begins a construction continued in VAK 8.19, whose
opening the Bhāṣya quotes before explaining the preparation.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `dve` | nominative neuter numeral | two [pure types] |
| `trīṇi` | nominative neuter numeral | three [pure types] |
| `ekam` | nominative singular neuter numeral | one [pure type] |
| `ca` | conjunction | and |
| `hānabhāgādyanantaram` | adverbial compound | immediately after the decline-conducive and subsequent types |
| `gatvā` | absolutive of √gam | having gone; entered in forward order |
| `āgamya` | absolutive of ā-√gam | having returned; entered in reverse order |
| `dvidhā` | adverb | in two modes |
| `bhūmīḥ` | accusative plural feminine | levels or grounds |
| `aṣṭau` | numeral | eight |
| `śliṣṭaikalaṅghitāḥ` | accusative plural feminine, qualifying bhūmīḥ | contiguous and with one intervening level skipped |

`Ca + ekam` yields `caikam`; `gatvā + āgamya`
yields `gatvāgamya`; `bhūmīḥ + aṣṭau` yields
`bhūmīr aṣṭau`; `śliṣṭa + eka` yields `śliṣṭaika`.
The prose resolves the shortened decline designation
as hānabhāgīya.

## 4. Grammar

The first half counts immediate successors among the four pure types; the second is a preparation sequence whose absolutives continue into 8.19.

```nltk-fcfg
% start S
# tokens: dve trīṇi trīṇi caikaṃ ca hānabhāgādyanantaram ∅-utpadyante gatvā āgamya dvidhā bhūmīr aṣṭau śliṣṭaikalaṅghitāḥ ∅-prayogaḥ
S -> CL[K=successor_counts] CL[K=preparation]
CL[K=successor_counts] -> NUM[CASE=nom,NUM=du,GEN=n] NUM[CASE=nom,NUM=pl,GEN=n] NUM[CASE=nom,NUM=pl,GEN=n] NUM[CASE=nom,NUM=sg,GEN=n] CONJ PREP[REL=after] V[PERS=3,NUM=pl,TENSE=pres,VOICE=mid,SUPPLIED=prose]
CL[K=preparation] -> ABS[DIR=forward] ABS[DIR=reverse] ADV[MODES=two] N[CASE=acc,NUM=?n,GEN=?g] NUM[COUNT=eight] ADJ[CASE=acc,NUM=?n,GEN=?g,ORDER=contiguous_and_one_skipped] N[KIND=preparation,SUPPLIED=prose]
NUM[CASE=nom,NUM=du,GEN=n] -> 'dve'
NUM[CASE=nom,NUM=pl,GEN=n] -> 'trīṇi'
NUM[CASE=nom,NUM=sg,GEN=n] -> 'caikaṃ'
CONJ -> 'ca'
PREP[REL=after] -> 'hānabhāgādyanantaram'
V[PERS=3,NUM=pl,TENSE=pres,VOICE=mid,SUPPLIED=prose] -> '∅-utpadyante'
ABS[DIR=forward] -> 'gatvā'
ABS[DIR=reverse] -> 'āgamya'
ADV[MODES=two] -> 'dvidhā'
N[CASE=acc,NUM=pl,GEN=f] -> 'bhūmīr'
NUM[COUNT=eight] -> 'aṣṭau'
ADJ[CASE=acc,NUM=pl,GEN=f,ORDER=contiguous_and_one_skipped] -> 'śliṣṭaikalaṅghitāḥ'
N[KIND=preparation,SUPPLIED=prose] -> '∅-prayogaḥ'
```

```nltk-dep
'∅-utpadyante' -> 'dve' | 'trīṇi' | 'caikaṃ' | 'hānabhāgādyanantaram'
'bhūmīr' -> 'gatvā' | 'āgamya' | 'dvidhā' | 'aṣṭau' | 'śliṣṭaikalaṅghitāḥ'
'∅-prayogaḥ' -> 'gatvā' | 'āgamya' | '∅-utpadyante'
```

Dvidhā means contaminated and uncontaminated modes, not forward/reverse directions;
contaminated is not synonymous with defiled. “One” after penetration-conducive counts
only the pure types. Eight contaminated but seven uncontaminated levels are available;
the skipped step is known, not blindly bypassed.

**Close construe.** After the four pure types beginning
with the decline-conducive, respectively two, three,
three, and one of those types arise. Having entered
and returned through the levels in two modes, first
contiguously and then skipping one intervening level,
[one completes the preparation described in the prose].

## 5. Translation

### Literal Translation

> Immediately after the decline-conducive and subsequent
> [types], two, three, three, and one [arise].
> Having gone and returned through the eight levels
> in two modes, contiguously and with one [level]
> skipped …

### Bhāṣya-informed study translation

> Immediately after the decline-conducive and the other pure types,
> two, three, three, and one [types] respectively arise. Having gone
> forward and returned, in two ways, through the levels, eight in
> all, contiguously and with one skipped each time …

## 6. Philosophical Translation

> A subtype's orientation does not by itself enumerate
> its immediate successors. The commentary specifies
> their membership as well as their number. It
> then turns to a different question: preparation
> for moving through the ordered attainment levels,
> where mastery of contiguous forward and reverse
> entry precedes practice in skipping a level.

These are two related analyses with different objects:
the first concerns pure subtypes, the second the
ordered dhyāna and formless levels under two modes.

## 7. Technical Vocabulary

**Source.** Pradhan 445|11–446|06, checked against the local Bhāṣya
study and running source. The ellipsis closing the translations marks the
verse-boundary continuation into VAK 8.19, not missing witness text; the
source quotes the opening of VAK 8.19 within this span. The numerals
two, three, three, one are the Bhāṣya's neighbor-sets among the four
pure types, and the eight levels are the contaminated series (the
uncontaminated series has seven). The study stops at the commentary's
conclusion identifying this procedure as preparation.

**`Hānabhāgīya / sthitibhāgīya / viśeṣabhāgīya /
nirvedhabhāgīya`.** The four pure types defined in
VAK 8.17. Here they serve as both predecessors
and the restricted set of successors being counted.

**`Anuloma / pratiloma`.** Forward / reverse order.
The prose uses these to explain going and returning
through the attainment sequence.

**`Śliṣṭa`.** Contiguous. The commentary gives anukrameṇa,
in sequence, as its explanation.

**`Ekalaṅghita`.** With one intervening level skipped.
A movement from first to third dhyāna skips the
second. It is a displacement of two level-steps,
consistent with the range clarified in VAK 8.15.

**`Sāsrava / anāsrava`.** Contaminated / uncontaminated.
Contaminated should not be replaced with defiled:
the two categories are not coextensive. The preparation
is organized by these two modes with their different
numbers of available levels.

**`Prayoga`.** Preparation or preparatory practice.
The concluding prose expressly distinguishes the work
described here from the accomplished form whose explanation
continues in VAK 8.19.

## 8. Logical Determination

The first half gives successor sets among the four pure types; the second describes preparation by traversing attainment levels in both directions and in two modes. These are distinct relations. Provenance: `[verse]`, `[prose]`.

**Signature.** `Follows/2(next,prior)`—immediate successor among pure types; `ContaminatedLevel/1(l)`, `UncontaminatedLevel/1(l)`—available level by mode; `Traversal/3(d,m,l)`—direction, mode, and level in preparation.

**Dataset (successor matrix and level inventory).** Counting the listed `Follows` pairs yields 2, 3, 3, and 1 successors. The level rows represent the eight contaminated and seven uncontaminated grounds; traversal direction and mode are separate fields.

```nltk-valuation
hanaType => hanaType
stabilityType => stabilityType
distinctionType => distinctionType
penetrationType => penetrationType
forward => forward
reverse => reverse
contaminated => contaminated
uncontaminated => uncontaminated
firstDhyana => firstDhyana
secondDhyana => secondDhyana
thirdDhyana => thirdDhyana
fourthDhyana => fourthDhyana
infiniteSpace => infiniteSpace
infiniteConsciousness => infiniteConsciousness
nothingness => nothingness
summit => summit
Follows => {(hanaType,hanaType),(stabilityType,hanaType),(hanaType,stabilityType),(stabilityType,stabilityType),(distinctionType,stabilityType),(stabilityType,distinctionType),(distinctionType,distinctionType),(penetrationType,distinctionType),(penetrationType,penetrationType)}
ContaminatedLevel => {firstDhyana,secondDhyana,thirdDhyana,fourthDhyana,infiniteSpace,infiniteConsciousness,nothingness,summit}
UncontaminatedLevel => {firstDhyana,secondDhyana,thirdDhyana,fourthDhyana,infiniteSpace,infiniteConsciousness,nothingness}
Traversal => {(forward,contaminated,firstDhyana),(reverse,contaminated,summit),(forward,uncontaminated,firstDhyana),(reverse,uncontaminated,nothingness)}
```

```nltk-fol
# THEORY shared
# [verse, prose] successor membership, restricted to the four pure types
Follows(hanaType,hanaType)
Follows(stabilityType,hanaType)
Follows(hanaType,stabilityType)
Follows(stabilityType,stabilityType)
Follows(distinctionType,stabilityType)
Follows(stabilityType,distinctionType)
Follows(distinctionType,distinctionType)
Follows(penetrationType,distinctionType)
Follows(penetrationType,penetrationType)
# [verse, prose] the counted series has eight contaminated and seven uncontaminated levels
all x.(UncontaminatedLevel(x) -> ContaminatedLevel(x))
```

**Results (NLTK).** The checker confirms the displayed successor facts and level-inclusion rule in the valuation. The 2/3/3/1 cardinalities are visible in the Dataset relation; NLTK does not derive those counts here.

**Scope cautions.** `dvidhā` means contaminated/uncontaminated modes, not forward/reverse directions. The eight levels are contaminated; the summit is absent from the uncontaminated list. Preparation is not completed skipping attainment, which is VAK 8.19.

## 9. Interpretive Note

**The verse crosses between two questions.** Its first
half completes the pure-type successor inventory. Its
second half begins the preparation question and continues
syntactically into the next verse. Preserving both
the verse and argument boundaries requires marking
that continuation rather than inventing a final clause.

**Witness cautions.** The running source separates
`hāna bhāgādyanantaram` and has the damaged
`ākṃicanyāvatanam` in the skipping example. The local
extract supplies the recognizable nothingness-sphere
reading. The research kārikā also reports a spacing
problem in śliṣṭaikalaṅghitāḥ, although the running
witness inspected here prints that compound continuously.
The official verse follows the local study; originals
remain unchanged.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates the exact successor sets, their
restricted domain, and the ordered levels available
under each mode. Yoga Technē, its kriyā–karma companion,
concerns the prescribed exercise: sequential mastery
followed by controlled skipping. The preparation's
order matters independently of the arithmetic of
the pure-type successor sets.

For Organon representation, distinguish a relation
among subtypes from a traversal of levels. Preserve
direction, self-successors, unavailable mode-level combinations,
and the difference between preparation and completion.
This is project reconstruction, not an additional
formal system attributed to the Bhāṣya.

**Review status.** Provisional, Bhāṣya-controlled study.
The four successor sets, restricted counting domain,
eight/seven distinction, forward/reverse sequence, explicit
skip example, and preparation endpoint have been
checked against the local research and running source.

## 10. OWL++ Seed

```text
Class: PureSubtypeSuccession
Class: AttainmentLevelTraversal
Class: PreparatoryPractice

ObjectProperty: mayImmediatelyFollowWithinPureTypes
ObjectProperty: traversesInMode
ObjectProperty: hasDirection
ObjectProperty: skipsInterveningLevel

PureSubtypeSuccessors:
    Hanabhagiya: Hanabhagiya, Sthitibhagiya
    Sthitibhagiya: Hanabhagiya, Sthitibhagiya, Visesabhagiya
    Visesabhagiya: Sthitibhagiya, Visesabhagiya, Nirvedhabhagiya
    Nirvedhabhagiya: Nirvedhabhagiya
    counts: 2, 3, 3, 1
    countingDomain: FourPureTypesOnly

SequentialPreparation:
    contaminatedLevelCount: 8
    uncontaminatedLevelCount: 7
    directions: Forward, Reverse

SkippingPreparation:
    prerequisite: SequentialMastery
    skippedInterveningLevelCount: 1
    directions: Forward, Reverse
    status: PreparationForCrossedAttainment

ProjectConstraint: The pure-type relation is directed, not a bidirectional chain.
ProjectConstraint: The singleton does not exclude an uncontaminated successor.
ProjectConstraint: Do not posit an uncontaminated summit attainment.
ProjectConstraint: Keep subtype succession distinct from level traversal.
ProjectConstraint: Preserve sequential mastery before skipping preparation.
ProjectConstraint: The perfected form continues in VAK 8.19.
```

This is a declarative project seed, not executable OWL.
VAK 8.19 next determines the completed skipping attainment
and who can accomplish it.
