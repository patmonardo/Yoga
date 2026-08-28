# VAK_2.46

## 1. Sanskrit (Devanāgarī)

> जातिजात्यादयस्तेषां तेऽष्टधर्मैकवृत्तयः ।
>
> जन्यस्य जनिका जातिर्न हेतुप्रत्ययैर्विना ॥ २.४६ ॥

## 2. Sanskrit (IAST)

> jātijātyādayas teṣāṃ te 'ṣṭadharmaikavṛttayaḥ /
>
> janyasya janikā jātir na hetupratyayair vinā // 2.46 //

## 3. Padaccheda

```text
jātijātyādayas      → jāti-jāti-ādayaḥ
teṣāṃ               → teṣām
te 'ṣṭadharmaikavṛttayaḥ
                    → te aṣṭa-dharma-eka-vṛttayaḥ
janyasya            → janyasya
janikā              → janikā
jātir               → jātiḥ
na                  → na
hetupratyayair      → hetu-pratyayaiḥ
vinā                → vinā
```

| Form | Morphology | Lexical force here |
|---|---|---|
| jāti-jāti-ādayaḥ | nominative masculine plural compound | birth-of-birth and the remaining secondary marks |
| teṣām | genitive plural pronoun | of those primary marks |
| te | nominative masculine plural pronoun | those primary marks |
| aṣṭa-dharma-eka-vṛttayaḥ | nominative masculine plural compound | each operating with respect to eight dharmas |
| janyasya | genitive neuter singular gerundive used substantivally | of what is to be generated |
| janikā | nominative feminine singular agent noun | generator / producer |
| jātiḥ | nominative feminine singular | birth / arising |
| na ... vinā | negated prepositional construction | not without |
| hetu-pratyayaiḥ | instrumental masculine plural compound | causes and conditions |

`Jāti-jāti` is not a repetition for emphasis. It names the Vaibhāṣika
secondary mark “birth of birth,” paired with duration-of-duration,
aging-of-aging, and impermanence-of-impermanence.

## 4. Grammar

The first half completes the Vaibhāṣika primary/secondary-mark model:

```text
teṣāṃ jāti-jāti-ādayaḥ
    → the primary marks themselves have
      birth-of-birth and the remaining secondary marks

te aṣṭa-dharma-eka-vṛttayaḥ
    → each primary mark operates upon eight dharmas
```

The Bhāṣya reconstructs one conditioned occurrence as nine members:

```text
one focal conditioned dharma
+ four primary marks
+ four secondary marks
= nine
```

Primary birth produces the other eight, excluding itself; birth-of-birth
produces primary birth alone. Duration, aging, and impermanence are assigned
parallel distributions of operation.

The second half grants `jāti` a generating predicate and immediately limits it:

```text
janyasya janikā jātiḥ
    → birth is the generator of what is to be generated

na hetu-pratyayaiḥ vinā
    → but not without causes and conditions
```

That limitation generates the Bhāṣya's central objection: if complete causes
and conditions are necessary and sufficient, what distinct work remains for
a birth-entity?

## 5. Translation

### Close syntactic construe

> Birth-of-birth and the remaining secondary marks belong to those [primary marks]; each [primary mark] operates with respect to eight dharmas. Birth generates what is to be generated, but not without causes and conditions.

### Bhāṣya-informed translation

> The Vaibhāṣikas assign each of the four conditioned marks a corresponding secondary mark and distribute their causal operations across the resulting nine-member occurrence. They say that birth produces the dharma to be born, but only when the complete causes and conditions are assembled. Vasubandhu replies that the causal conjunction already explains the arising: “birth” designates the transition from prior nonexistence to present existence and need not name an additional producer.

## 6. Philosophical Translation

> A real transition does not require a transition-substance. When the complete causes and conditions are present, the effect arises; when they are absent, it does not. `Jāti` intelligibly names this determinate coming-to-be, but naming the transition does not add another causal agent beside the conditions that perform the work.

The critical reduction is:

```text
complete causal conjunction
    → effect arises

therefore:
    no redundant BirthOperator is required
```

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this unit |
|---|---|---|
| jāti | birth / arising | Vaibhāṣika generative substance; Vasubandhu's designation for coming to exist after prior nonexistence |
| jāti-jāti | birth of birth | secondary mark assigned to primary birth |
| anulakṣaṇa | secondary mark | meta-mark intended to ensure that each conditioned primary mark is itself marked as conditioned |
| aṣṭa-dharma-eka-vṛtti | operation upon eight dharmas | distribution rule by which a primary mark acts on the focal dharma and the remaining marks |
| janya | what is to be generated | conditioned effect whose arising is disputed |
| janikā | generator | causal role attributed to birth |
| hetu | cause | productive ground participating in the causal conjunction |
| pratyaya | condition | enabling or conditioning determination participating in arising |
| hetu-pratyaya-sāmagrī | complete conjunction of causes and conditions | sufficient causal configuration according to the critical argument |
| abhūtvā-bhāva | existing after previously not existing | Bhāṣya definition of conditioned arising without a birth-substance |
| prajñapti-mātra | conceptual designation only | status of the lifecycle term when grounded in the stream rather than reified |
| ṣaṣṭhī-vibhakti | genitive construction | grammar such as “the arising of form,” rejected as proof of separate substance |

`Prajñapti` does not make arising imaginary or functionless. It says that
the name is grounded in an intelligible causal transition without requiring
an additional entity numerically distinct from the arising dharma and its
conditions.

## 8. Logical Determination

The Vaibhāṣika mark structure is:

```text
Occurrence = {
    focalDharma,
    primaryBirth,
    primaryDuration,
    primaryAging,
    primaryImpermanence,
    birthOfBirth,
    durationOfDuration,
    agingOfAging,
    impermanenceOfImpermanence
}
```

Its distribution rule is:

```text
PrimaryMark(M)
    → OperatesOn(M, eight members excluding M)

SecondaryMark(M2, M)
    → OperatesOn(M2, M only)
```

The verse's causal restriction is:

```text
Generates(Jati, D)
    → Complete(Causes(D) + Conditions(D))
```

The critical argument eliminates the redundant term:

```text
Complete(Causes(D) + Conditions(D))
    → Arises(D)

NOT Complete(Causes(D) + Conditions(D))
    → NOT Arises(D)

No independently observable difference is contributed by JatiEntity
    → JatiEntity is explanatorily redundant
```

The designation remains exact:

```text
Jati(D, t)
    := NOT Exists(D, before t)
       AND Exists(D, at t)
```

The unconditioned does not satisfy this transition:

```text
Unconditioned(U)
    → NOT Jati(U)
```

Grammar supplies no ontological entailment:

```text
DistinctExpression("arising of form")
    ⇏ SeparateSubstance(Arising, Form)
```

## 9. Interpretive Note

VAK 2.46 completes the critique of substantialized lifecycle marks. The
Vaibhāṣika model tries to prevent regress by adding exactly one secondary
mark for each primary mark and distributing their operations asymmetrically.
The construction is ingenious, but the Bhāṣya asks the prior question:
does any mark-entity perform work not already performed by causes and
conditions?

The answer is negative. Complete causal conditions explain both why this
dharma arises and why all future dharmas do not arise simultaneously. Adding
`jāti` after that explanation duplicates the transition.

The grammatical defense fails for the same reason. From the fact that one
can say “the arising of form” it does not follow that form and arising are two
substances. Otherwise every numerical, spatial, relational, and grammatical
distinction would require a matching entity:

```text
one, two, large, small,
separate, conjoined,
prior, posterior, existent ...
```

The Kośa's own critical labor therefore gives us a precise ontology rule:

```text
semantic distinction
    requires an intelligible ground

semantic distinction
    does not automatically require a separate substance
```

For the Kośa Technē, `jāti` should be a derived transition with causal
provenance:

```text
deriveArising(effect)
    from priorNonexistence
       + completeCauses
       + completeConditions
       + presentOccurrence
```

This is not merely an optimization that removes unnecessary objects. It
preserves the Concept of arising: the effect is known through the complete
genesis by which it becomes present.

The Vaibhāṣika closes by retaining the substantial marks as established
doctrine despite the objections. That conclusion must remain attributed; the
Bhāṣya's argumentative weight, however, strongly favors Vasubandhu's
immanent causal analysis.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_46
    a vak:Karika ;
    rdfs:label "VAK 2.46" ;
    vak:hasTopic vak:PrimarySecondaryMarks,
        vak:JatiCausalRestriction ;
    vak:belongsTo vak:Indriyanirdesa .

vak:VaibhasikaMarkModel
    a vak:AttributedDoctrinalPosition ;
    vak:asserts vak:FourPrimaryMarks,
        vak:FourSecondaryMarks ;
    vak:assignsOperation vak:EightDharmaDistribution .

vak:VasubandhuJatiCritique
    a vak:AttributedDoctrinalPosition ;
    vak:grounds vak:Arising ;
    vak:in vak:CompleteCauseConditionConjunction,
        vak:PriorNonexistence,
        vak:PresentExistence ;
    vak:denies vak:SeparateBirthSubstance .

organon:DerivedArisingTransition
    a organon:InterpretiveReconstruction ;
    organon:isDerivedFrom organon:PriorNonexistence,
        organon:CompleteCauses,
        organon:CompleteConditions,
        organon:PresentOccurrence ;
    organon:isNot organon:IndependentBirthOperator .
```
