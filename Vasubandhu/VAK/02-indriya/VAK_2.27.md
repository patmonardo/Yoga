# VAK_2.27 — Minor Affliction Caitta Factors

## 1. Sanskrit — Devanāgarī

```text
क्रोधोपनाहशाठ्येर्ष्याप्रदासम्रक्षमत्सराः ।
मायामदविहिंसाश्च परीत्तक्लेशभूमिकाः ॥ VAkK_2.27 ॥
```

## 2. Sanskrit — IAST

```text
krodhopanāhaśāṭhyerṣyāpradāsamrakṣamatsarāḥ /
māyāmadavihiṃsāś ca parīttakleśabhūmikāḥ // VAkK_2.27 //
```

Source form:

```text
krodhopanāhaśāṭhyerṣyāpradāsamrakṣamatsarāḥ /
māyāmadavihiṃsāśca parīttakleśabhūmikāḥ // VAkK_2.27 //
```

Textual caution:

```text
The source compounds should be checked later against the Bhāṣya and printed editions.
The present file preserves the source sequence as a kārikā-first seed.
```

## 3. Padaccheda and Grammar

| Sanskrit | Padaccheda | Grammar | Working Sense |
|---|---|---|---|
| krodha | krodha | masculine noun in compound | anger |
| upanāha | upanāha | masculine noun in compound | resentment / grudge-holding |
| śāṭhya | śāṭhya | neuter noun in compound | deceitfulness / craftiness |
| īrṣyā | īrṣyā | feminine noun in compound | envy |
| pradāsa | pradāsa | masculine noun in compound | spite / hostility; to verify |
| mrakṣa | mrakṣa | masculine noun in compound | concealment / hypocrisy; to verify |
| matsaraḥ | matsaraḥ | masculine nominative plural in compound ending | selfishness / stinginess / rivalry |
| māyā | māyā | feminine noun in compound | deception / illusion-making |
| mada | mada | masculine noun in compound | intoxication / conceit |
| vihiṃsāḥ | vihiṃsāḥ | feminine nominative plural | harmfulness / injuriousness |
| ca | ca | indeclinable | and |
| parītta-kleśa-bhūmikāḥ | parītta-kleśa-bhūmikāḥ | feminine nominative plural compound | belonging to the ground of minor afflictions |

## 4. Literal Translation

```text
Anger, resentment, deceitfulness, envy, spite, concealment, selfishness,
deception, intoxication, and harmfulness belong to the ground of minor afflictions.
```

## 5. Philosophical Translation

```text
Beyond the general afflicted and unwholesome factors, there is a more particular field of minor afflictions.

These are not merely emotions. They are determinate distortions of the citta-field:
anger, resentment, deceit, envy, concealment, possessive rivalry, illusion-making,
conceit, and harmfulness.
```

## 6. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| krodha | anger | Reactive hostility |
| upanāha | resentment | Retained anger / grudge |
| śāṭhya | deceitfulness | Crookedness or craftiness |
| īrṣyā | envy | Distress at another's good |
| pradāsa | spite / hostility | Source term to verify |
| mrakṣa | concealment / hypocrisy | Source term to verify |
| matsara | stinginess / rivalry | Selfish possessiveness or rivalry |
| māyā | deception | Illusion-making or deceptive display |
| mada | intoxication / conceit | Inflated self-satisfaction |
| vihiṃsā | harmfulness | Injurious tendency |
| parītta-kleśa-bhūmikā | ground of minor afflictions | Class designation for these factors |

## 7. Logical Determination

VAK_2.27 gives a further disjunctive subclass within the afflicted field.

```text
kliṣṭa-caitta
    general afflicted factors

parītta-kleśa-bhūmika
    minor-affliction factors
```

The dominant protocol is Disjunctive Classification:

```text
Affliction
    divides into:
        general afflicted factors
        specifically unwholesome factors
        minor-affliction factors
```

It also gives Conjunction at the class level:

```text
MinorAfflictionFeatureSet
    = krodha + upanāha + śāṭhya + īrṣyā + ...
```

This is a diagnostic feature-list for subtle distortion.

## 8. Relation to Indriya

Indriyas supply governing faculty-givenness. Caittas determine how that givenness is configured within the citta-field.

The minor afflictions show fine-grained deformation of experience:

```text
same indriya-givenness
    may be configured by anger,
    resentment,
    envy,
    deceit,
    conceit,
    or harmfulness.
```

Thus caitta analysis gives the Agent a distortion taxonomy for interpreting how faculty-data has been appropriated.

## 9. Organon Interpretation

Organon reading:

```text
MinorAfflictionCaittaFeatureSet
    = fine-grained distortion taxonomy
    = Agent-side diagnostic schema
```

Dataset schema:

```text
MinorAfflictedCitta:
    hasAnger
    hasResentment
    hasDeceitfulness
    hasEnvy
    hasSpite
    hasConcealment
    hasRivalry
    hasDeception
    hasConceit
    hasHarmfulness
```

Learning implication:

```text
The Agent must not only distinguish wholesome from unwholesome.
It must detect subtle deformation modes within the field of experience.
```

This is the beginning of a fine-grained kleśa diagnostic model already inside Indriyanirdeśa.

## 10. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:MinorAfflictionCaitta a rdfs:Class ;
    rdfs:subClassOf vak:Caitta ;
    rdfs:label "minor affliction caitta" ;
    rdfs:comment "A caitta belonging to the ground of minor afflictions." .

vak:MinorAfflictionFeatureSet a rdfs:Class ;
    rdfs:label "Minor Affliction FeatureSet" ;
    rdfs:comment "Fine-grained distortion taxonomy for the citta-field." .

vak:Krodha a vak:MinorAfflictionCaitta .
vak:Upanāha a vak:MinorAfflictionCaitta .
vak:Śāṭhya a vak:MinorAfflictionCaitta .
vak:Īrṣyā a vak:MinorAfflictionCaitta .
vak:Pradāsa a vak:MinorAfflictionCaitta .
vak:Mrakṣa a vak:MinorAfflictionCaitta .
vak:Matsara a vak:MinorAfflictionCaitta .
vak:Māyā a vak:MinorAfflictionCaitta .
vak:Mada a vak:MinorAfflictionCaitta .
vak:Vihiṃsā a vak:MinorAfflictionCaitta .
```

## 11. Commit History

```text
VAK_2.27 opened.
Method: kārikā-first speculative seed.
Theme: minor affliction caittas.
Logical protocols recorded: disjunctive subclassification and conjunctive distortion feature-set.
Relation to indriya tracked: caittas as fine-grained deformation modes of faculty-givenness inside citta.
Textual caution recorded for dense source compounds.
Zero-padded file naming maintained: VAK_2.27.
```
