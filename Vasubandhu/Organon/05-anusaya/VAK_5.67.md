# VAK_5.67

## 1. Sanskrit (Devanāgarī)

```sanskrit
आर्यमार्गस्य सर्वाः द्वे लौकिकस्य अन्वयस्य च ।
धर्मज्ञानस्य तिस्रस्तु षट् तत्पक्षस्य पञ्च च ॥ ५.६७ ॥
```

## 2. Sanskrit (IAST)

```text
āryamārgasya sarvāḥ dve laukikasya anvayasya ca |
dharmajñānasya tisras tu ṣaṭ tatpakṣasya pañca ca || 5.67 ||
```

VAK 5.66 distributed the parijñās by meditative basis. VAK 5.67 distributes
the same completed abandonments by comprehensive Path-class, determinate
knowledge-operation, and the wider operative side to which a knowledge
belongs.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `āryamārgasya` | genitive singular masculine | of the noble path |
| `sarvāḥ` | nominative plural feminine | all nine parijñās |
| `dve` | nominative dual feminine | two parijñās |
| `laukikasya` | genitive singular masculine | of the mundane path |
| `anvayasya` | genitive singular | of `anvayajñāna`, higher-realm subsequent knowledge |
| `ca` | conjunction | and, also |
| `dharmajñānasya` | genitive singular neuter | of dharma-knowledge |
| `tisraḥ` | nominative plural feminine | three parijñās |
| `tu` | contrastive particle | but, whereas |
| `ṣaṭ` | numeral | six |
| `tat-pakṣasya` | genitive singular masculine | of its side, the dharmajñāna family |
| `pañca` | numeral | five, of the other knowledge-side |


The final `pañca` is supplied by the Bhāṣya as the count for the
`anvayajñāna-pakṣa`. The compact `tatpakṣa` clause cannot be safely expanded
from surface syntax without that prose control.

## 4. Grammar

The verse comprises a sequence of genitive fruit-relations with understood
`parijñāḥ phalam`:

```text
āryamārgasya
    sarvāḥ [nava parijñāḥ phalam]

laukikasya
    dve [parijñe phalam]

anvayajñānasya ca
    dve [parijñe phalam]

dharmajñānasya tu
    tisraḥ [parijñāḥ phalam]
```

The final pāda changes the subject-level from a knowledge alone to its side:

```text
dharmajñānapakṣasya
    ṣaṭ [parijñāḥ phalam]

anvayajñānapakṣasya
    pañca [parijñāḥ phalam]
```

The Bhāṣya defines `pakṣa` inclusively: the corresponding kṣānti-moments and
jñāna-moments are both taken. The increased count therefore comes from an
expanded operative family, not an altered intrinsic capacity of one isolated
knowledge-event.

## 5. Translation

### Literal Translation

> All [nine parijñās] are of the noble path; two are of the mundane [path] and
> also of the subsequent [knowledge]. But three are of dharma-knowledge; six
> are of its side, and five [of the other side].

### Bhāṣya-informed study translation

> All nine *parijñās* are fruits of the noble path. Two are fruits of the
> mundane path and two of anvaya-knowledge; three are fruits of
> dharma-knowledge. When the corresponding *kṣānti* and knowledge moments are
> counted together, the dharma-knowledge side has six fruits, the
> anvaya-knowledge side five.

## 6. Philosophical Translation

> A completed abandonment may be fruit of the noble Path as a whole, of a
> particular knowledge in its counteractive operation, and of the larger
> patience-and-knowledge family containing that operation. These predicates do
> not compete because they determine the result at different levels. The
> numerical asymmetry follows from operative reach: dharma-knowledge counters
> cultivation-abandonable afflictions across all three realms, while
> subsequent knowledge reaches the final two higher-realm completions.

The verse therefore measures relational efficacy, not the intrinsic dignity
of one knowledge over another.

## 7. Technical Vocabulary

**`Āryamārga` — noble path**

The comprehensive uncontaminated Path-class whose fruits include all nine
parijñās. This universal classification can coexist with more specific
knowledge-level classifications.

**`Laukikamārga` — mundane path**

Its two fruits are:

```text
avarabhāgīya-kṣaya-parijñā
rūparāga-kṣaya-parijñā
```

Its abandonment-efficacy is genuine but its parijñā range is restricted.

**`Anvayajñāna` — subsequent knowledge**

Knowledge concerning the higher-realm truths. Its fruits are the final two
parijñās:

```text
rūparāga-kṣaya-parijñā
sarva-saṃyojana-paryādāna-parijñā
```

**`Dharmajñāna` — dharma-knowledge**

Its fruits are the final three parijñās. The Bhāṣya's exact ground is
`tridhātuka-bhāvanāheya-pratipakṣatva`: it functions as counteragent to
cultivation-abandonable afflictions throughout all three realms.

**Reference range and counteractive range**

Dharmajñāna is named in relation to the Desire Realm truths, yet its
cultivation-path efficacy extends through all three realms. The truth-range after
which a knowledge is named does not by itself delimit every operation it can
perform.

**`Pakṣa` — side or operative family**

The Bhāṣya explicitly includes both corresponding `kṣāntis` and `jñānas`.
`Dharmajñāna-pakṣa` and `anvayajñāna-pakṣa` are therefore broader
classificatory subjects than dharmajñāna and anvayajñāna taken alone.

**The two knowledge-sides**

```text
dharmajñāna-pakṣa   → six parijñās
anvayajñāna-pakṣa   → five parijñās
```

The additional fruits belong to patience-moments included by the expanded
family scope.

## 8. Logical Determination

The fruit relation is many-to-many:

```text
YieldsFruit(PathOrKnowledgeSubject, Parijñā)
```

Its cardinalities are:

```text
Count(FruitSet(Āryamārga))          = 9
Count(FruitSet(Laukikamārga))       = 2
Count(FruitSet(Anvayajñāna))        = 2
Count(FruitSet(Dharmajñāna))        = 3
Count(FruitSet(DharmajñānaPakṣa))   = 6
Count(FruitSet(AnvayajñānaPakṣa))   = 5
```

The subject-levels remain distinct:

```text
PathClass
    ≠ KnowledgeOperation
    ≠ KnowledgeSide
```

Thus one parijñā may satisfy several predicates:

```text
FruitOf(p, Āryamārga)
AND FruitOf(p, Dharmajñāna)
AND FruitOf(p, DharmajñānaPakṣa)
```

without causal contradiction. The inclusion rule is:

```text
DharmajñānaPakṣa
    includes {DharmajñānaKṣāntiMoments, DharmajñānaMoments}

AnvayajñānaPakṣa
    includes {AnvayajñānaKṣāntiMoments, AnvayajñānaMoments}
```

And the asymmetry follows from counteractive range:

```text
Counteracts(Dharmajñāna, CultivationAbandonables(AllThreeRealms))
    → Count(DirectParijñāFruits) = 3
```

## 9. Interpretive Note

**Classification by productive operation.** The verse no longer asks from
which meditative state a Path proceeds, but under which Path or knowledge-
operation a completed abandonment counts as fruit.

**Mundane efficacy without universal range.** The mundane path yields two
real parijñā completions. The passage does not reduce them to mere temporary
appearance, yet it reserves the complete ninefold range for the noble Path.

**Reference does not exhaust efficacy.** Dharmajñāna's name is Desire Realm
indexed, but its counteractive function on the cultivation path spans all
three realms. Its truth-reference and operational range must be modeled
separately.

**Knowledge versus knowledge-family.** Moving from `jñāna` to `pakṣa` changes
the classificatory subject. The extra fruits do not belong to an isolated
knowledge considered more powerful; they belong to the patience-and-knowledge
sequence taken as a whole.

**Organon interpretation.** A later Dataset should type both the producer and
its level of abstraction:

```text
ParijñāFruitAssertion
    hasResult Parijñā
    hasProductiveSubject
    hasSubjectLevel {PathClass, Knowledge, KnowledgeSide}
    hasCounteractiveRange
    supportedBy SourceSpan
```

This is a project-level representation of the source distinctions, not
formal vocabulary attributed to the Bhāṣya.

## 10. OWL++ Seed

```text
Class: Parijna
Class: ProductiveSubject
Class: PathClass
    SubClassOf: ProductiveSubject
Class: KnowledgeOperation
    SubClassOf: ProductiveSubject
Class: KnowledgeSide
    SubClassOf: ProductiveSubject
Class: ParijnaFruitAssertion
Class: CounteractiveRange

Individual: NoblePath
    Types: PathClass
Individual: MundanePath
    Types: PathClass
Individual: Dharmajnana
    Types: KnowledgeOperation
Individual: Anvayajnana
    Types: KnowledgeOperation
Individual: DharmajnanaSide
    Types: KnowledgeSide
Individual: AnvayajnanaSide
    Types: KnowledgeSide

ObjectProperty: hasProductiveSubject
    Domain: ParijnaFruitAssertion
    Range: ProductiveSubject

ObjectProperty: hasResult
    Domain: ParijnaFruitAssertion
    Range: Parijna

ObjectProperty: includesPathMoment
    Domain: KnowledgeSide
    Range: PathMoment

ObjectProperty: hasCounteractiveRange
    Domain: KnowledgeOperation
    Range: CounteractiveRange

Assertion: NoblePath hasParijnaFruitCount 9
Assertion: MundanePath hasParijnaFruitCount 2
Assertion: Anvayajnana hasParijnaFruitCount 2
Assertion: Dharmajnana hasParijnaFruitCount 3
Assertion: DharmajnanaSide hasParijnaFruitCount 6
Assertion: AnvayajnanaSide hasParijnaFruitCount 5

Assertion: Dharmajnana hasCounteractiveRange AllThreeRealmCultivationAbandonables

Rule: KnowledgeSide(?side)
      AND includesPathMoment(?side, ?moment)
      AND ProducesParijna(?moment, ?p)
    -> HasParijnaFruit(?side, ?p)

Constraint: FruitOf(?p, ?specificSubject)
    doesNotEntail NotFruitOf(?p, ?comprehensiveSubject)

View: ParijnaProductiveOperationMap
    Preserves: ParijnaIdentity, ProductiveSubject, SubjectLevel,
               KnowledgeFamilyMembership, CounteractiveRange,
               FruitCardinality, SourceProvenance
```

The seed preserves the central structure: one completed abandonment can be a
fruit under several nested but non-identical productive descriptions.
