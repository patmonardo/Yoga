# VAK_5.54

## 1. Sanskrit (Devanāgarī)

```sanskrit
समानसिद्धा दृग्घेया मनोविज्ञानभूमिकाः ।
उपक्लेशाः स्वतन्त्राश्च षड्विज्ञानाश्रयाः परे ॥ ५.५४ ॥
```

## 2. Sanskrit (IAST)

```text
samānasiddhā dṛg-gheyā manovijñāna-bhūmikāḥ |
upakleśāḥ svatantrāś ca ṣaḍ-vijñānāśrayāḥ pare || 5.54 ||
```

VAK 5.54 begins a new distribution of the afflictive field by cognitive
support: factors restricted to the mental-cognition plane and factors
capable of occurring with the six cognition-groups.

**Textual caution.** The working e-text reads `samānasiddhā` in the kārikā and
`saha mānasiddhābhyāṃ` in the prose. The prose securely indicates two
additional cultivation-abandoned factors that are wholly mental-plane, but
their names are not safely recoverable from this non-critical witness. No
silent normalization is introduced here.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `samāna-siddhāḥ` | nominative plural masculine, textually opaque | transmitted designation connected by the prose with two cultivation-abandoned cases |
| `dṛk-heyāḥ` | nominative plural masculine compound | to be abandoned through seeing |
| `manas-vijñāna-bhūmikāḥ` | nominative plural masculine compound | belonging to the plane of mental cognition |
| `upakleśāḥ` | nominative plural masculine | mind-defilements or secondary afflictions |
| `sva-tantrāḥ` | nominative plural masculine | independently classified |
| `ca` | conjunction | and, likewise |
| `ṣaṭ-vijñāna-āśrayāḥ` | nominative plural masculine compound | having the six cognitions as support |
| `pare` | nominative plural masculine | the others, the remaining cases |


The verse contrasts two support-ranges. `Bhūmi` locates a factor on the
mental-cognition plane; `āśraya` names the cognition-group upon which
an afflictive occurrence depends.

## 4. Grammar

**Mental-plane group**

```text
[samāna-siddhāḥ]
dṛk-heyāḥ
    manovijñāna-bhūmikāḥ

upakleśāḥ svatantrāḥ ca
    [manovijñāna-bhūmikāḥ]
```

The predicate applies first to all seeing-abandoned afflictions together with
the uncertainly transmitted additional pair, then by ellipsis to all
independent upakleśas.

**Six-cognition group**

```text
pare
    ṣaḍ-vijñāna-āśrayāḥ
```

The adjective `pare` establishes a complementary class. The Bhāṣya identifies
the principal remainder as cultivation-abandoned attachment, hostility, and
ignorance together with their associated upakleśas.

## 5. Translation

### Literal Translation

> The seeing-abandoned [afflictions], together with the cases indicated by the
> uncertain transmitted expression, belong to the plane of mental
> cognition; the independent upakleśas do so as well. The others have the
> six cognitions as support.

### Bhāṣya-informed study translation

> Those abandoned through seeing, together with two cultivation-abandoned
> factors whose names are uncertain in this witness, belong to the plane of
> mental cognition. Independent secondary afflictions do likewise; the
> remaining afflictions and secondary afflictions have the six cognitions
> as their support.

## 6. Philosophical Translation

> Realm, origin, abandonment, and cognitive support answer different
> questions. An affliction may be cultivation-abandoned yet restricted to
> mental cognition, as the independent upakleśas show. Conversely, other
> cultivation-abandoned factors can occur with sensory as well as mental
> cognition. Support specifies the cognitive field in which an afflictive
> event becomes possible; it does not identify the event's genetic root or
> dictate its Path-status. Complete determination therefore requires a matrix
> of relations rather than a single hierarchy.

This reconstruction remains deliberately agnostic about the two names obscured
by the present textual transmission.

## 7. Technical Vocabulary

**`Manovijñāna-bhūmika` — belonging to the mental-cognition plane**

A factor restricted to occurrence with mental cognition. The Bhāṣya
categorically places all seeing-abandoned afflictions in this class.

**`Dṛg-heya` / `darśana-prahātavya` — abandoned through seeing**

One Path-classification of affliction. VAK 5.54 assigns its entire extension
to mental cognition without making cognitive support identical to mode of
abandonment.

**The uncertain additional pair**

The prose indicates two factors that are cultivation-abandoned yet wholly
mental-plane. The transmitted `samānasiddhā` / `mānasiddhābhyām` does not
permit their secure lexical identification in this provisional edition.

**`Svatantra upakleśa` — independent upakleśa**

Every factor bearing this status is mental-only. From VAK 5.52 the category
includes the five remaining paryavasthānas and the six kleśa-malas; its
independence remains classificatory and relationally grounded.

**`Ṣaḍvijñāna-āśraya` — supported by the six cognitions**

Capable of occurrence with the eye-, ear-, nose-, tongue-, body-, or mental-
cognition group. The Bhāṣya also uses `ṣaḍvijñāna-bhūmika` and
`ṣaḍvijñāna-kāyika` for this range.

**The remaining kleśas**

```text
bhāvanā-prahātavya rāga
bhāvanā-prahātavya pratigha
bhāvanā-prahātavya avidyā
```

These cultivation-abandoned forms are six-cognition based.

**Associated upakleśas in the remainder**

The Bhāṣya names shamelessness, lack of moral concern, torpor, excitation, and
factors previously classified among the `kleśa-mahābhūmikas`.

**`Kleśa-mahābhūmika` — factor universally associated with afflicted mind**

An earlier Chapter 2 classification invoked here to complete the
six-cognition-supported remainder. The present verse does not re-enumerate
or redefine that class.

**`Āśraya` — support or basis**

The cognitive support of an occurrence. It must not be confused with
`niḥṣyanda` source, object-support (`ālambana`), realm-range, or mode of
abandonment.

## 8. Logical Determination

The secure mental-only rules are:

```text
AbandonedBySeeing(x)
    → SupportedOnlyBy(x, MentalCognition)

IndependentUpakleśa(x)
    → SupportedOnlyBy(x, MentalCognition)
```

The second rule blocks an invalid inference:

```text
AbandonedByCultivation(x)
    ⇏ SupportedByAllSixCognitions(x)
```

The remainder is:

```text
For x in {CultivationAbandonedRāga,
          CultivationAbandonedPratigha,
          CultivationAbandonedAvidyā,
          TheirSpecifiedAssociatedUpakleśas}:
    HasCognitiveSupportRange(x, SixCognitionGroups)
```

Support remains independent of other relations:

```text
HasCognitiveSupport(x, vijñāna)
    ≠ HasGeneticGround(x, kleśa)
    ≠ HasObjectSupport(x, ālambana)
    ≠ HasAbandonmentMode(x, pathOperation)
```

The unresolved pair must remain formally open:

```text
Cardinality(UncertainMentalOnlyPair) = 2
LexicalIdentity(UncertainMentalOnlyPair) = Unresolved
```

## 9. Interpretive Note

**Source determination.** After closing the upakleśa block by realm, the
Bhāṣya asks how many anuśayas belong to the mental plane and how many to the
six cognition-groups. The answer divides the field by cognitive support.

**Textual restraint.** The two extra cultivation-abandoned cases are real
members of the argument, but their names are not secure in the available
e-text. A durable provisional edition preserves both determinate cardinality
and indeterminate identity rather than filling the gap from conjecture.

**Support is not origin.** A visible object may occur in an eye-cognition
event supporting attachment, but neither the visible object nor eye-
cognition thereby becomes the affliction's `niḥṣyanda` source. The chapter
has supplied separate vocabulary for each relation.

**Support is not abandonment.** Some cultivation-abandoned factors are
mental-only, while others are six-cognition based. The same Path-status
therefore does not determine one cognitive range.

**Organon interpretation.** The Dataset should model a support assertion with
its own provenance:

```text
CognitiveSupportAssertion
    concernsFactor
    hasSupportRange
    hasAbandonmentContext
    hasTextualCertainty
    supportedBy SourceSpan
```

The unresolved pair also requires uncertainty about identity without loss of
its other known predicates. This is project architecture designed to preserve
the Bhāṣya's actual evidential state.

## 10. OWL++ Seed

```text
Class: AfflictiveFactor
Class: Klesa
Class: Upaklesa
Class: CognitionGroup
Class: MentalCognition
    SubClassOf: CognitionGroup
Class: SensoryCognition
    SubClassOf: CognitionGroup
Class: CognitiveSupportAssertion
Class: TextualCertainty
Class: UnresolvedIdentity

ObjectProperty: concernsFactor
    Domain: CognitiveSupportAssertion
    Range: AfflictiveFactor

ObjectProperty: hasCognitiveSupport
    Domain: CognitiveSupportAssertion
    Range: CognitionGroup

ObjectProperty: hasTextualCertainty
    Domain: CognitiveSupportAssertion
    Range: TextualCertainty

DataProperty: isMentalOnly
    Domain: AfflictiveFactor
    Range: Boolean

Rule: SeeingAbandonedAffliction(?x)
    -> isMentalOnly(?x, true)

Rule: IndependentUpaklesa(?x)
    -> isMentalOnly(?x, true)

Rule: RemainingSixfoldAffliction(?x)
    -> MayBeSupportedBy(?x, EyeCognition)
    AND MayBeSupportedBy(?x, EarCognition)
    AND MayBeSupportedBy(?x, NoseCognition)
    AND MayBeSupportedBy(?x, TongueCognition)
    AND MayBeSupportedBy(?x, BodyCognition)
    AND MayBeSupportedBy(?x, MentalCognition)

Constraint: CultivationAbandoned(?x)
    doesNotEntail isMentalOnly(?x, false)

Constraint: UncertainMentalOnlyPair(?group)
    hasMemberCount 2
    AND hasMemberIdentity UnresolvedIdentity

View: AfflictionCognitiveSupportMatrix
    Preserves: FactorIdentity, CognitionRange, AbandonmentMode,
               IndependenceStatus, TextualUncertainty, SourceProvenance
```

The seed treats cognitive support as an independent classificatory axis and
preserves the unresolved pair without conjectural normalization.
