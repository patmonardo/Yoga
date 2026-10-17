# VAK_6.04

## 1. Sanskrit (Devanāgarī)

```sanskrit
यत्र भिन्नेन तद्बुद्धिरन्यापोहे धिया च तत् ।
घटार्थवत्संवृतिसत्परमार्थसदन्यथा ॥ ६.४ ॥
```

## 2. Sanskrit (IAST)

```text
yatra bhinnena tadbuddhir anyāpohe dhiyā ca tat |
ghaṭārthavat saṃvṛtisat paramārthasad anyathā || 6.4 ||
```

VAK 6.04 introduces the two truths after the preceding verses have established
the Four Truths and the extension of duḥkha-satya. It distinguishes
conventional and ultimate reality by testing whether the corresponding
cognition survives physical division or cognitive analysis.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `yatra` | relative adverb | where; in the case in which |
| `bhinnena` | instrumental singular past participle of `√bhid` | when divided or broken |
| `tad-buddhiḥ` | nominative singular feminine compound | cognition of that, of the named unity |
| `anya-apohe` | locative singular compound | when other dharmas are removed or excluded |
| `dhiyā` | instrumental singular feminine of `dhī` | by cognition, through analysis |
| `ca` | conjunction | and, or in the paired test |
| `tat` | nominative singular neuter correlative pronoun | that |
| `ghaṭa-artha-vat` | comparative compound | as with the meaning “pot”; the Bhāṣya gives a pot as the example |
| `saṃvṛti-sat` | nominative singular neuter | conventionally real |
| `paramārtha-sat` | nominative singular neuter | ultimately real |
| `anyathā` | adverb | otherwise |



The verse is highly compressed. The negative force—cognition of the named
object no longer occurs—is supplied by the Bhāṣya's explicit prose. `Anyathā`
reverses that result for ultimate reality: own-nature cognition continues under
the relevant division or exclusion.

## 4. Grammar

The relative-correlative construction is:

```text
yatra ... tadbuddhiḥ [na bhavati]
    tat saṃvṛtisat

where cognition of that no longer occurs ...
    that is conventionally real
```

The Bhāṣya resolves two conditions:

```text
bhinne
    when the object is divided part by part

anyadharmāpohe dhiyā
    when other dharmas are excluded by cognition
```

It assigns separate examples:

```text
ghaṭa
    pot-cognition ceases when the pot is broken into shards

ambu
    water-cognition ceases when constituent dharmas are excluded in thought
```

The conclusion is elliptical:

```text
paramārthasat anyathā
    the ultimately real is otherwise
```

The prose expands `anyathā`: cognition of the relevant own nature remains even
after atom-by-atom division or exclusion of other dharmas.

**Feature Grammar direction.** The relative `yatra` and correlative `tat`
form the classification frame. `Tad-buddhiḥ` supplies the cognition tested
under two operations; `anyathā` reverses the result for *paramārtha-sat*:

```text
REL[yatra, TEST=division-or-exclusion, RESULT=loss-of-that-cognition]
    → CORR[tat, STATUS=saṃvṛti-sat]

OTHERWISE[TEST=division-or-exclusion, RESULT=own-nature-cognition-remains]
    → STATUS[paramārtha-sat]
```

This is a feature specification for later NLTK work; the Bhāṣya supplies the
negative predicate and the positive converse.

## 5. Translation

### Literal Translation

> That in the case of which cognition of it [ceases] when it is divided, or
> when other [dharmas] are excluded by cognition, is conventionally real, as
> with the meaning “pot.” The ultimately real is otherwise.

### Bhāṣya-informed study translation

> Where, upon division or mental exclusion of other things, cognition of that
> no longer arises, that is conventionally real, as with the meaning “pot”;
> ultimately real is otherwise.

## 6. Philosophical Translation

> Reality is discriminated by asking what determination remains when an
> apparent unity is decomposed. A conventional unity is genuinely available
> for truthful discourse, yet its cognition depends upon a configuration that
> analysis can dissolve. An ultimate object is not placed beyond analysis; it
> is the determination whose own-nature cognition withstands the relevant
> analysis. The distinction therefore concerns two modes of truth, not the
> opposition of useful illusion to inaccessible reality.

The movement is:

```text
configured unity
    → decomposition
    → loss of that-object cognition
    → conventional reality

own-nature determination
    → decomposition or exclusion
    → persistence of cognition
    → ultimate reality
```

## 7. Technical Vocabulary

**`Saṃvṛti-satya` — conventional truth**

Truthful discourse under the force of convention. The Bhāṣya explicitly says
that one who says “the pot exists” or “water exists” speaks truth, not
falsehood, because conventional designation is established upon the relevant
dharmas.

**`Saṃvṛti-sat` — conventionally real**

A named and functioning unity whose corresponding cognition does not survive
the decomposition of its basis. This is dependent reality, not sheer
nonexistence.

**`Paramārtha-satya` — ultimate truth**

Truth concerning what exists ultimately. In the Vaibhāṣika analysis presented
here, cognition of the dharma's own nature persists after the relevant
division and cognitive exclusion.

**`Paramārtha-sat` — ultimately real**

The analytically final determination exemplified by `rūpa`, visible Form, and
extended by the Bhāṣya to feeling and other dharmas. The plural examples block
identification with a single all-encompassing substance.

**`Tad-buddhi` — cognition of that**

The classification test concerns persistence of a determinate cognition. When
the pot is reduced to shards, cognitions of shards and qualities may remain,
but the cognition “pot” does not.

**`Avayavaśo bhinna` — divided part by part**

The Bhāṣya's expansion of physical division. The pot is broken into shards;
the ultimate example is considered under division atom by atom.

**`Anya-apoha` — removal or exclusion of others**

Here an operation of cognitive analysis: other supporting or associated
dharmas are excluded in thought to test whether cognition of the proposed
object remains. This local use should not be silently equated with every later
Buddhist theory bearing the name `apoha`.

**`Ghaṭārtha` — the meaning “pot”**

The named meaning depends on a composite pot whose cognition fails the
persistence test when the pot is broken. `Artha` remains Meaning; the
Bhāṣya's concrete example is the pot, not a new technical use of Object.

**`Ambu` — water**

The Bhāṣya's example for cognitive exclusion. Water-cognition ceases when the
dharmas supporting that configured object are removed in analysis.

**`Rūpa` — visible Form or material Form**

The primary ultimate example. Its own-nature cognition is said to remain after
atomization and after other associated dharmas are excluded. This is a
school-specific Abhidharma determination, not an unqualified cross-Buddhist
definition of ultimate reality.

**`Svabhāva-buddhi` — cognition of own nature**

The cognition that persists in the ultimate case. The criterion is not mere
survival of a word but continued cognition of the dharma's specific nature.

**`Pūrvācārya` — former teacher**

The Bhāṣya attributes a further criterion to former teachers: what is grasped
in the same way by supramundane knowledge or its subsequently acquired mundane
cognition is ultimate truth; what is grasped otherwise is conventional. This
is reported attribution, not kārikā wording.

## 8. Logical Determination

The conventional-reality tests are:

```text
PhysicalDivision(x)
AND Ceases(CognitionOf(x))
    → ConventionalReal(x)

CognitiveExclusionOfSupportingDharmas(x)
AND Ceases(CognitionOf(x))
    → ConventionalReal(x)
```

The ultimate-reality test is:

```text
RelevantDecomposition(x)
AND Persists(CognitionOfOwnNature(x))
    → UltimateReal(x)
```

The truth-preservation rule is:

```text
ConventionalDesignation(name, ConfigurationOfDharmas)
AND ConventionallyReal(x)
    → CanBeTrue(AssertionExists(x))
```

Therefore:

```text
ConventionalReal(x)
    ↛ False(x)

NotUltimateReal(x)
    ↛ Nonexistent(x)
```

The former teachers' attributed criterion is distinct:

```text
SameModeOfApprehension(
    SupramundaneKnowledge,
    SubsequentlyAcquiredMundaneKnowledge,
    x
)
    → UltimateTruthObject(x)
```

## 9. Interpretive Note


**Translation note.** The Bhāṣya illustrates conventional designation with a pot broken into shards and removal of other properties with water; visible Form and feeling retain cognition of their own nature.

**The two truths do not replace the Four Truths.** VAK 6.02 names the fourfold
field of realization; 6.04 now discriminates the mode of reality of what is
spoken and known within that field.

**Convention remains truth.** The strongest anti-nihilist control comes from
the Bhāṣya itself: claims that a pot and water exist are true, not false, under
convention. Analytical non-finality is not non-being.

**The two conventional tests must remain distinct.** Physical breakage is
illustrated by the pot; cognitive exclusion is illustrated by water. Combining
both into a single pot example loses the Bhāṣya's articulation.

**Ultimate reality is analytically disclosed.** It is not an indeterminate
beyond inaccessible to cognition. `Rūpa`, `vedanā`, and other dharmas are the
examples, and the criterion is persistence of own-nature cognition.

**The account is school-specific.** This is the Vaibhāṣika analytic realism
presented in the Kośa context. It should not be projected without qualification
onto Madhyamaka, Yogācāra, Vedānta, or a generic notion of “absolute truth.”

**Organon interpretation.** VAK 6.04 gives a rigorous textual threshold for
our search for paramārthika Meaning. The following is project synthesis, not
source doctrine:

```text
configured meaning
    valid within a functioning relational whole
    yet lost when that configuration is decomposed

paramārthika determination
    not a grander verbal unity
    but what remains determinately cognizable through analysis
```

The Ideal Copula cannot merely declare a conventional whole ultimate. It must
preserve conventional truth while exposing which determinations depend upon
composition and which survive disciplined discrimination. Yet 6.04 does not
itself equate paramārtha with Path. Rather, it supplies the truth-test that the
Path of Knowing must enact. The Path remains the practical mediation; the
ultimate is what adequate discrimination discloses.

## 10. OWL++ Seed

```text
Class: Truth
Class: ConventionalTruth
    SubClassOf: Truth
Class: UltimateTruth
    SubClassOf: Truth
Class: Real
Class: ConventionalReal
    SubClassOf: Real
Class: UltimateReal
    SubClassOf: Real
Class: CompositeConfiguration
Class: Dharma
Class: Cognition
Class: OwnNatureCognition
    SubClassOf: Cognition
Class: DecompositionOperation
Class: PhysicalDivision
    SubClassOf: DecompositionOperation
Class: CognitiveExclusion
    SubClassOf: DecompositionOperation

ObjectProperty: testsObject
    Domain: DecompositionOperation
    Range: Real

ObjectProperty: hasCognitionBefore
    Domain: DecompositionOperation
    Range: Cognition

ObjectProperty: hasCognitionAfter
    Domain: DecompositionOperation
    Range: Cognition

ObjectProperty: designatedOnBasisOf
    Domain: ConventionalReal
    Range: Dharma

ObjectProperty: apprehendedBy
    Domain: Real
    Range: Cognition

Rule: PhysicalDivision(?operation)
      AND testsObject(?operation, ?object)
      AND cognitionOfObjectCeases(?operation, ?object)
    -> ConventionalReal(?object)

Rule: CognitiveExclusion(?operation)
      AND testsObject(?operation, ?object)
      AND cognitionOfObjectCeases(?operation, ?object)
    -> ConventionalReal(?object)

Rule: DecompositionOperation(?operation)
      AND testsObject(?operation, ?object)
      AND ownNatureCognitionPersists(?operation, ?object)
    -> UltimateReal(?object)

Assertion: Pot instanceOf ConventionalReal
Assertion: Water instanceOf ConventionalReal
Assertion: Rupa instanceOf UltimateReal
Assertion: Vedana instanceOf UltimateReal

Constraint: ConventionalReal
    doesNotEntail False
    doesNotEntail Nonexistent

View: TwoTruthAnalyticTest
    Preserves: ObjectIdentity, ConfigurationBasis, DecompositionType,
               CognitionBefore, CognitionAfter, RealityStatus,
               Attribution, SourceProvenance
```

The seed represents the two tests and preserves conventional truth as truth.
It records the former teachers' account separately rather than flattening it
into the kārikā's analytic definition.
