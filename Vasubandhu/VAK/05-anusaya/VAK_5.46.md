# VAK 5.46

## Sanskrit

येऽप्यन्ये चैतसाः क्लिष्टाः संस्कारस्कन्धसंज्ञिताः ।
क्लेशेभ्यस्तेऽप्युपक्लेशास्ते तु न क्लेशसंज्ञिताः ॥ ५.४६ ॥

## IAST

ye 'py anye caitasāḥ kliṣṭāḥ saṃskāraskandha-saṃjñitāḥ /
kleśebhyas te 'py upakleśās te tu na kleśa-saṃjñitāḥ // 5.46 //

## Padaccheda

ye | api | anye | caitasāḥ | kliṣṭāḥ | saṃskāra-skandha-saṃjñitāḥ | kleśebhyaḥ | te | api | upakleśāḥ | te | tu | na | kleśa-saṃjñitāḥ

## Grammar

- **ye** — nominative plural masculine relative pronoun, “those which.”
- **api** — “also,” “even.”
- **anye** — nominative plural masculine, “other,” distinguishing these factors from the principal kleśas already enumerated.
- **caitasāḥ** — nominative plural masculine, “mental factors,” dharmas associated with citta.
- **kliṣṭāḥ** — nominative plural masculine, “afflicted,” “defiled.”
- **saṃskāra-skandha-saṃjñitāḥ** — nominative plural masculine compound, “designated as belonging to the aggregate of formations.”
- **kleśebhyaḥ** — ablative plural, “from the afflictions,” “in dependence upon the kleśas.”
- **te api** — “they also.”
- **upakleśāḥ** — nominative plural masculine, “secondary afflictions,” “derivative afflictions.”
- **te tu** — “but they.”
- **na kleśa-saṃjñitāḥ** — “are not designated as kleśas.”

## Literal Translation

Those other afflicted mental factors that are designated as belonging to the aggregate of formations are also secondary afflictions arising from the afflictions; but they are not designated as afflictions proper.

## Philosophical Translation

Beyond the root afflictions there are other afflicted mental determinations within the aggregate of formations. Because they arise in dependence upon the kleśas, they are called derivative afflictions; nevertheless, they do not possess the defining status of root afflictions themselves.

## Structural Analysis

VAK 5.41–5.45 completed the classification of fetters. VAK 5.46 now changes the level of analysis:

```text
root afflictions
    ↓
derivative afflicted mental factors
```

The distinction is not between affliction and non-affliction. Both are afflicted. The distinction is between:

```text
kleśa
    primary afflictive determination

upakleśa
    derivative or dependent afflictive determination
```

The verse therefore introduces a relation of dependence inside the afflicted field itself.

## Technical Vocabulary

### Caitasa

A mental factor associated with citta. The term does not mean an independent mind-substance; it names a determinate mental function occurring within a cognitive event.

### Saṃskāraskandha

The aggregate of formations contains constructed and conditioning determinations not included under form, feeling, representation, or knowledge. Here the relevant factors are afflicted mental formations.

### Kleśa

A root affliction possessing the status required to generate and sustain the afflicted field directly.

### Upakleśa

A secondary affliction. The prefix **upa-** marks proximity, dependence, or derivation. An upakleśa is genuinely afflictive but does not independently occupy the status of a root kleśa.

## Doctrinal Determination

The verse establishes that the afflicted field has internal depth:

```text
root condition
    ≠
manifest derivative
```

A derivative affliction is not merely another name for a kleśa. Its identity depends upon its relation to a root affliction.

Therefore:

```text
isAfflicted(x)
    does not entail
isRootAffliction(x)
```

and:

```text
isSecondaryAffliction(x)
    entails
arisesInDependenceOn(x, some Kleśa)
```

The distinction allows the Kośa to explain how a limited set of roots can generate a much broader field of concrete afflicted behavior.

## Logical Determination

VAK 5.46 introduces the logical form of derivation:

```text
Ground
    ↓
Derivative Determination
```

The upakleśa is not externally attached to the kleśa. It is the kleśa's further determination under concrete conditions.

This yields three levels:

```text
root power
    ↓
derivative formation
    ↓
manifest conduct or obstruction
```

The verse therefore guards against two reductions:

```text
all afflicted factors are identical
```

and:

```text
derivative factors are merely accidental
```

They are neither identical with nor independent of their grounds.

## Organon Note

This distinction is central for the coming Speculative Reason work. The afflicted field should be modeled as a generative dependency graph rather than a flat taxonomy.

```text
Kleśa
    generates / conditions
Upakleśa
    modifies
Cognitive and practical activity
```

A root discriminator must be able to distinguish:

```text
primary contradiction
secondary deformation
concrete symptom
```

without collapsing one into another.

The present verse also gives a useful mediation between dharma and karma:

```text
kleśa
    afflictive determination

upakleśa
    derived formation of that determination

karma
    activity in which the formation becomes effective
```

This remains a light first-pass Organon hypothesis and should be tested against the Bhāṣya.

## OWL++ Seed

```ttl
vak:Klesa a owl:Class ;
  rdfs:subClassOf vak:AfflictiveMentalFactor .

vak:Upaklesa a owl:Class ;
  rdfs:subClassOf vak:AfflictiveMentalFactor ,
    vak:SamskaraSkandhaMember ;
  owl:disjointWith vak:Klesa .

vak:arisesFromKlesa a owl:ObjectProperty ;
  rdfs:domain vak:Upaklesa ;
  rdfs:range vak:Klesa .
```

Possible SHACL constraint:

```ttl
vak:UpaklesaShape a sh:NodeShape ;
  sh:targetClass vak:Upaklesa ;
  sh:property [
    sh:path vak:arisesFromKlesa ;
    sh:minCount 1 ;
    sh:class vak:Klesa
  ] .
```

## Bhāṣya Questions

1. Does **kleśebhyaḥ** indicate efficient derivation, causal dependence, classificatory subordination, or all three?
2. Which precise criterion prevents an upakleśa from being called a kleśa?
3. Are all upakleśas necessarily members of the saṃskāra-skandha?
4. Does the Bhāṣya define the root kleśas by universality, independence, persistence, or capacity to generate further afflictions?
5. How tightly are specific upakleśas assigned to specific kleśa-roots in the verses that follow?
