# VAK_8.07 — Five Factors of the First Dhyāna and Four of the Second

## 1. Sanskrit (Devanāgarī)

```sanskrit
पञ्चाद्ये तर्कचारौ च प्रीतिसौख्यसमाधयः ।
प्रीत्यादयः प्रसादश्च द्वितीयेऽङ्गचतुष्टयम् ॥ ८.०७ ॥
```

## 2. Sanskrit (IAST)

```text
pañcādye tarkacārau ca prītisaukhyasamādhayaḥ |
prītyādayaḥ prasādaś ca dvitīye 'ṅgacatuṣṭayam || 8.07 ||
```

The Sanskrit follows the local kārikā witness. The
Devanāgarī renders the same reading. The prose expands
`tarkacārau` as vitarka and vicāra, without requiring
those expanded words to be substituted into the verse.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `pañca` | numeral (`pañca + ādye` → `pañcādye`) | five [factors] |
| `ādye` | locative singular neuter adjective | in the first [dhyāna] |
| `tarka-cārau` | nominative dual coordinated compound | vitarka and vicāra |
| `ca` | conjunction | and |
| `prīti-saukhya-samādhayaḥ` | nominative plural coordinated compound | joy, ease, and concentration |
| `prīti-ādayaḥ` | nominative plural compound (`prītyādayaḥ`) | those beginning with joy, the preceding three |
| `prasādaḥ` | nominative singular masculine | clarity, expanded as inward serenity |
| `ca` | conjunction | and |
| `dvitīye` | locative singular neuter ordinal (`dvitīye 'ṅga-`) | in the second [dhyāna] |
| `aṅga-catuṣṭayam` | nominative singular neuter collective compound | a set of four factors; the dual pair and plural triad together give the first fivefold count |

## 4. Grammar

The first clause counts a dual pair plus a triad; in the second, the prose reorders but does not enlarge that triad. `Prītyādayaḥ` excludes vitarka and vicāra, and samādhi is glossed as one-pointedness; five factors are not five attainments.

```nltk-fcfg
% start S
# tokens: pañcādye tarkacārau ca prītisaukhyasamādhayaḥ prītyādayaḥ prasādaḥ ca dvitīye aṅgacatuṣṭayam
S -> CL[K=first] CL[K=second]
CL[K=first] -> LOC[CASE=loc,NUM=sg,GEN=n,COUNT=five] N[CASE=nom,NUM=du,GEN=m,COUNT=two] CONJ[COORD=yes] N[CASE=nom,NUM=pl,GEN=m,COUNT=three]
CL[K=second] -> N[CASE=nom,NUM=pl,GEN=m,COUNT=three] N[CASE=nom,NUM=sg,GEN=m,ADD=yes] CONJ[COORD=yes] LOC[CASE=loc,NUM=sg,GEN=n] N[CASE=nom,NUM=sg,GEN=n,COUNT=four]
LOC[CASE=loc,NUM=sg,GEN=n,COUNT=five] -> 'pañcādye'
N[CASE=nom,NUM=du,GEN=m,COUNT=two] -> 'tarkacārau'
CONJ[COORD=yes] -> 'ca'
N[CASE=nom,NUM=pl,GEN=m,COUNT=three] -> 'prītisaukhyasamādhayaḥ'
N[CASE=nom,NUM=pl,GEN=m,COUNT=three] -> 'prītyādayaḥ'
N[CASE=nom,NUM=sg,GEN=m,ADD=yes] -> 'prasādaḥ'
LOC[CASE=loc,NUM=sg,GEN=n] -> 'dvitīye'
N[CASE=nom,NUM=sg,GEN=n,COUNT=four] -> 'aṅgacatuṣṭayam'
```

```nltk-dep
'prītisaukhyasamādhayaḥ' -> 'tarkacārau' | 'ca' | 'pañcādye'
'aṅgacatuṣṭayam' -> 'prītyādayaḥ' | 'prasādaḥ' | 'ca' | 'dvitīye'
```

`Prītyādayaḥ` is restricted to the immediately preceding triad; it does not include vitarka/vicāra. The first-dhyāna factors remain five, not five separate attainments.


**Close construe.** In the first dhyāna are five factors:
vitarka, vicāra, joy, ease, and concentration. In the
second are the three beginning with joy plus inward
clarity, forming a set of four factors.

## 5. Translation

### Literal Translation

> In the first are five: vitarka and vicāra, joy, ease,
> and concentration. In the second, the three beginning
> with joy and clarity form the set of four factors.

### Bhāṣya-informed study translation

> In the first dhyāna are five factors: vitarka and vicāra, joy,
> ease, and concentration. In the second, the three beginning
> with joy, together with clarity, form the set of four factors.

## 6. Philosophical Translation

> Dhyāna is specified through a differentiated set of
> factors. Samādhi belongs to that set while also supplying
> the attainment's defining determination. The second
> dhyāna's list omits the initial pair but includes a
> positive factor not named in the first list: inward clarity.

The comparison is therefore richer than simple removal
of factors. Yet appearance in the second factor inventory
does not by itself prove that the corresponding dharma
was wholly absent from every first-dhyāna occurrence.
The present question is what is counted as an aṅga.

## 7. Technical Vocabulary

**`Aṅga`.** Factor or limb of the attainment. These
are the selected dhyāna factors, not an exhaustive
list of every associated mental dharma and not a list
of the Bases.

**`Vitarka / vicāra`.** Initial application and sustained
examination, retained as technical terms in the translation.
The Bhāṣya explicitly resolves the verse's shortened
`tarka` and `cāra`; generic reasoning and movement
would miss their doctrinal reference.

**`Prīti`.** Joy or rapture. It is counted separately
from sukha and should not be collapsed into it merely
because both may be rendered with words related to
happiness.

**`Saukhya / sukha`.** Ease or pleasure. The prose uses
`sukha` for the verse's `saukhya`. The detailed analysis
of the factor's nature is not settled merely by this
lexical correspondence.

**`Samādhi / cittaikāgratā`.** Concentration or one-pointedness
of mind. The source counts it as one factor while
also calling it dhyāna. Its role requires distinguishing
the defining nature from the accompanied factor-constitution.

**`Adhyātmasaṃprasāda`.** Inward clarity or serene confidence.
This expands the verse's `prasāda`. The present unit
names and counts it; a fuller identification should
be controlled by the subsequent factor analysis rather
than supplied from an unsupported psychological paraphrase.

**`Kila`.** “It is said,” in `samādhiḥ kilāṅgaṃ dhyānaṃ
ca`. This reportative nuance is preserved without treating
it alone as proof that Vasubandhu rejects the stated
whole-and-factor relation.

**`Caturaṅgā senā`.** Four-limbed army. The source uses
this comparison for the five-limbed dhyāna. It does
not map each army division to a particular meditative
factor or prescribe an order of operations among them.

## 8. Logical Determination

This verse gives two level-indexed factor lists: a five-member first-dhyāna list and a four-member second-dhyāna list [verse; prose]. The Bhāṣya resolves the compressed pairs and restricts “the three beginning with joy” to the preceding triad.

**Signature.** `FactorOf(level,factor)`; `Count(level,n)`; `Dhyana(level)`; `SameRole(x,y)` (synonym or interpretive equivalence stated in prose).

**Finite data.** The roster represents named factors, not every associated dharma; counts are tallied from the roster and reported by name.

```nltk-valuation
first => first
second => second
vitarka => vitarka
vicara => vicara
priti => priti
sukha => sukha
samadhi => samadhi
clarity => clarity
five => five
four => four
Dhyana => {first, second}
FactorOf => {(first,vitarka),(first,vicara),(first,priti),(first,sukha),(first,samadhi),(second,priti),(second,sukha),(second,samadhi),(second,clarity)}
Count => {(first,five),(second,four)}
SameRole => {(samadhi,onepointedness),(clarity,adhyatmasamprasad)}
onepointedness => onepointedness
adhyatmasamprasad => adhyatmasamprasad
```

**Rules (verse and prose).**

```nltk-fol
# THEORY shared
# [verse] pañca ādye; [prose] vitarka and vicāra resolve tarkacārau
Count(first,five)
FactorOf(first,vitarka)
FactorOf(first,vicara)
# [verse] prīti-ādi; [prose] the already named triad, plus prasāda
FactorOf(second,priti)
FactorOf(second,sukha)
FactorOf(second,samadhi)
FactorOf(second,clarity)
# [prose] samādhi = one-pointedness; prasāda = inward clarity
SameRole(samadhi,onepointedness)
SameRole(clarity,adhyatmasamprasad)
Count(second,four)
```

**Results (NLTK).** The checker confirms the roster and count facts in the finite model. It does not derive cardinalities from first-order membership; the five and four are checked as source-reported tallies.

**Scope cautions.** The second list does not count vitarka or vicāra, but omission from an aṅga list alone is not an assertion that every underlying dharma is absent. Samādhi is both a counted factor and the dhyāna's defining nature. The army comparison is not a process rule.

## 9. Interpretive Note

**The scope-setting sentence.** The running source's
`eṣāṃ ca samāpattidravyāṇāṃ dhyānānyeva bhavanti
nārupyāḥ` is compressed at the transition into factors.
Its contextual role is to restrict this aṅga analysis
to dhyānas. It must not be read as denying that the
formless states are attainments or that the first three
admit uncontaminated modes, both already explicitly established.
The exact surface wording remains a point for collation.

**A positive factor without an unsupported genesis claim.**
The local research analysis calls inward clarity a new
positive factor replacing the discursive pair. That
accurately compares the inventories if “new” means
newly selected as an aṅga. It should not become a
claim that the underlying dharma first comes into
existence only at the second dhyāna. This passage
counts factors without yet completing their ontological
analysis.

**Witness cautions.** The prose has `prathame bhāge`
where the context securely concerns the first dhyāna,
and `cittekāgratā` in the second list. The first list's
`cittaikāgratā` and the verse's `samādhi` clarify the
reference. The study retains the abbreviated verse
forms and reports their prose expansion. Originals
remain unchanged.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates the roles through which an
attainment is determined; Yoga Technē, its kriyā–karma
companion, concerns their effective exercise in cultivation.
The source provides a useful distinction between a
factor present in the explanatory inventory and the
attainment characterized through that inventory.

For Organon, the same determination can have a defining
role and a role within an articulated whole without
making those roles interchangeable. Samādhi is the
concrete example here. A representation must also
distinguish non-selection as a named factor from absence
of a dharma altogether.

This is a structural project application. The army
comparison does not supply a software component architecture,
and the five-to-four count does not measure computational
complexity. The doctrinal inventories remain the primary
determination.

**Review status.** Provisional, Bhāṣya-controlled study.
The five- and four-member lists, expansions of tarka/cāra
and prasāda, samādhi's double role, and army analogy
have been checked against the local extract and running
source. The scope-setting sentence and finer factor
identifications remain explicitly bounded.

## 10. OWL++ Seed

```text
Class: DhyanaAttainment
Class: CountedDhyanaFactor
Class: DefiningDetermination

ObjectProperty: countsAsFactor
ObjectProperty: hasDefiningDetermination

FirstDhyana:
    factors: Vitarka, Vicara, Priti, Sukha, Samadhi
    factorCount: 5

SecondDhyana:
    factors: InwardClarity, Priti, Sukha, Samadhi
    factorCount: 4

Samadhi:
    proseExpansion: OnePointednessOfMind
    role: CountedFactor
    alsoNamedAs: Dhyana

Prasada:
    proseExpansion: AdhyatmaSamprasada
    detailedIdentification: ReservedForLaterFactorAnalysis

ProjectConstraint: Counted factors are not Bases.
ProjectConstraint: Named factor inventory is not every associated dharma.
ProjectConstraint: Non-selection as a factor does not alone prove total absence.
ProjectConstraint: Preserve defining nature and accompanied constitution.
ProjectConstraint: Reportative kila alone does not prove rejection.
ProjectConstraint: These lists are not complete acquisition procedures.
```

This is a declarative project seed, not executable OWL.
VAK 8.08 next enumerates the factors of the third and
fourth dhyānas.
