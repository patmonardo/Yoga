# VAK 5.38

## Sanskrit

### Devanāgarī

यथोक्ता एव साविद्या द्विधा दृष्टिविवेचनात् ।
उपादानानि अविद्या तु ग्राहिका नेति मिश्रिता ॥ ५.३८ ॥

### IAST

yathoktā eva sāvidyā dvidhā dṛṣṭivivecanāt /
upādānāni avidyā tu grāhikā neti miśritā // 5.38 //

## Padaccheda

- yathā-uktāḥ
- eva
- sa-avidyāḥ
- dvidhā
- dṛṣṭi-vivecanāt
- upādānāni
- avidyā
- tu
- grāhikā
- na
- iti
- miśritā

## Grammar

- **yathoktā eva** — “just those already stated”; nominative plural referring to the previously defined yokes/flood-classes.
- **sāvidyāḥ** — “together with ignorance”; *sa-avidyā*.
- **dvidhā dṛṣṭi-vivecanāt** — “twofold through the separation of views”; the view-group is divided into two appropriation-classes.
- **upādānāni** — nominative plural neuter, “appropriations,” “graspings,” or “acts of taking up.”
- **avidyā tu grāhikā na** — “ignorance, however, is not a grasper.”
- **iti miśritā** — “therefore it is mixed [with the other classes]” rather than established as an independent appropriation.

## Literal Translation

The very [classes] previously stated, together with ignorance, are the appropriations, divided into two by separating the views. Ignorance, however, is not a grasper; therefore it is included in mixture.

## Philosophical Translation

The already classified afflictive currents become **appropriations** when considered under the power of taking possession. Views must be split into two distinct grasping forms. Ignorance, however, cannot seize an object by itself; lacking the sharp determinacy of grasping, it functions only in combination with the other appropriative powers.

## Structural Analysis

VAK 5.35–5.38 presents the same afflictive field through successive functional perspectives:

1. **āsrava** — that which sustains or leaks as a current,
2. **ogha** — that which overwhelms and carries away,
3. **yoga** — that which fastens,
4. **upādāna** — that which appropriates or takes hold.

The dharmas are not replaced at each stage. Their operative relation is redescribed.

In the appropriation classification, the previous yokes are retained but ignorance is added to them. The view-yoke is divided into:

- **dṛṣṭyupādāna** — appropriation through views,
- **śīlavratopādāna** — appropriation through absolutized discipline and observance.

The other two appropriations are:

- **kāmopādāna** — appropriation of desire,
- **ātmavādopādāna** — appropriation of self-doctrine or self-assertion.

Thus one field is reorganized into four grasping powers.

## Technical Vocabulary

### upādāna

From *upa-ā-√dā*: taking up, laying hold of, appropriating, clinging.

It is stronger than mere relation to an object. It indicates that the object or determination is taken into the constitution of one’s operative standpoint.

### grāhikā

A grasping or seizing power. The term marks active determinative appropriation.

### avidyā

Ignorance is characterized by non-discernment. It conditions appropriation but lacks the sharp, object-seizing articulation required to constitute an independent appropriation-class.

### dṛṣṭivivecana

The analytical separation of views. A previously unified class is divided because distinct views exercise distinct practical powers.

## Doctrinal Determination

The verse establishes:

> Grounding a grasp is not identical with performing the grasp.

Ignorance is indispensable to appropriation, yet it is not itself an independent appropriation because it does not determinately seize.

Therefore:

```text
isConditionOfGrasping
    ≠
isGrasping
```

This continues the asymmetry established in 5.36:

```text
root of stream
    ≠
member functioning in the stream
```

Ignorance supplies the obscured field within which grasping occurs. Desire, views, observances, and self-doctrine perform the positive seizure.

## Logical Determination

The verse distinguishes three relations:

```text
conditions
seizes
isMixedWith
```

These relations must not collapse into one another.

A determination may:

- make an operation possible,
- accompany the operation,
- yet not itself perform that operation.

This gives a practical rule for causal modeling:

```text
EnablingCondition
    ≠
ExecutingPower
```

The same field may also be repartitioned according to the function being analyzed:

```text
same extension
    + different operative criterion
        → different valid classification
```

## Organon Note

For the Dialectical Copula, `upādāna` is the transition from relation to possession.

The weak form is:

```text
Agent relatesTo Determination
```

The stronger appropriative form is:

```text
Agent takesAsItsOwn Determination
```

This may generate:

```text
identifiesWith
organizesActionBy
defendsAsSelf
excludesContraryTo
```

Ignorance should not be modeled as one more explicit grasp. It is a degraded determination-field that permits grasping operations to occur without adequate discernment.

Thus:

```text
Ignorance
    = loss of discriminative articulation

Appropriation
    = positive seizure within that loss
```

This is important for practical extensions of the Copula. A system may fail not because it explicitly affirms a false predicate, but because its field of distinction is too weak to prevent another operation from seizing the object.

Under the maxim **Faith in Actuality: make the analysis actual**, the intervention must distinguish:

- restoring discernment,
- loosening identification,
- interrupting seizure,
- and revising the appropriated determination.

## OWL++ Seed

```turtle
vak:Upadana a owl:Class .
vak:GraspingPower a owl:Class .
vak:Ignorance a owl:Class .

vak:conditions a owl:ObjectProperty .
vak:seizes a owl:ObjectProperty .
vak:isMixedWith a owl:ObjectProperty .
vak:appropriatesAsOwn a owl:ObjectProperty .

vak:Ignorance rdfs:subClassOf [
  a owl:Restriction ;
  owl:onProperty vak:conditions ;
  owl:someValuesFrom vak:Upadana
] .

vak:Ignorance owl:disjointWith vak:IndependentGraspingPower .
```

Constraint:

```text
conditions(x, y)
does not entail
executes(x, y)
```

## Bhāṣya Questions

1. Does *yathoktāḥ* refer most immediately to the four yokes, the four floods, or the common afflictive set underlying both?
2. How exactly are *dṛṣṭyupādāna* and *śīlavratopādāna* separated from the view-yoke?
3. Why is *ātmavādopādāna* identified with the higher-domain existence-yoke plus ignorance?
4. Is ignorance denied grasping power absolutely, or only the sharp independent grasping required for a separate classificatory heading?
5. How should *miśritā* be rendered most precisely: mixed, included, combined, or distributed among the other appropriations?
6. How does the sūtra definition of appropriation through desire relate to the broader Abhidharma classification given here?
