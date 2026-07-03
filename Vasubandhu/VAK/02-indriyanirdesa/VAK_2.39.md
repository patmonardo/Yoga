# VAK_2.39 — Aprāpti Classifications and Domain Restrictions

## 1. Sanskrit — Devanāgarī

```text
निवृतस्य च रूपस्य कामे रूपस्य नाग्रजा ।
अक्लिष्टाव्याकृताप्राप्तिः सातीताजातयोस्त्रिधा ॥ VAkK_2.39 ॥
```

## 2. Sanskrit — IAST

```text
nivṛtasya ca rūpasya kāme rūpasya nāgrajā /
akliṣṭāvyākṛtāprāptiḥ sātītājātayos tridhā // VAkK_2.39 //
```

Source form:

```text
nivṛtasya ca rūpasya kāme rūpasya nāgrajā /
akliṣṭāvyākṛtāprāptiḥ sātītājātayostridhā // VAkK_2.39 //
```

## 3. Padaccheda and Grammar

| Sanskrit | Padaccheda | Grammar | Working Sense |
|---|---|---|---|
| nivṛtasya | nivṛtasya | genitive singular | of the obscured / veiled |
| ca | ca | indeclinable | and |
| rūpasya | rūpasya | genitive singular | of form / form-realm item |
| kāme | kāme | locative singular | in the desire realm |
| rūpasya | rūpasya | genitive singular | of form |
| na | na | particle | not |
| agrajā | agra-jā | feminine nominative singular | born in the higher / foremost; to verify |
| akliṣṭa-avyākṛta-aprāptiḥ | akliṣṭāvyākṛtāprāptiḥ | feminine nominative singular compound | non-afflicted indeterminate non-acquisition |
| sa-atīta-ajātayoḥ | sātītājātayoḥ | genitive/locative dual | with past and not-yet-arisen |
| tridhā | tridhā | adverb | threefold |

## 4. Literal Translation

```text
For the obscured and for form, in the desire realm, form is not higher-born.
The non-afflicted indeterminate aprāpti, with respect to past and not-yet-arisen cases, is threefold.
```

## 5. Philosophical Translation

```text
The aprāpti relation is also classified by domain and temporal status.
Certain form-related cases are restricted in relation to the desire realm.
Non-afflicted indeterminate non-acquisition is treated as threefold with respect to past and not-yet-arisen cases.
```

## 6. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| nivṛta | obscured / veiled | Status term requiring later review |
| rūpa | form | Could indicate form-realm or material form depending context |
| kāma | desire realm | Sensuous realm |
| agrajā | higher-born / prior-born | Technical reading to verify with Bhāṣya |
| akliṣṭa | non-afflicted | Not defiled |
| avyākṛta | indeterminate / neutral | Neither wholesome nor unwholesome |
| aprāpti | non-acquisition / non-connection | Structural non-relation |
| atīta | past | Temporal status |
| ajāta | not-yet-arisen / unborn | Future/not arisen status |
| tridhā | threefold | Threefold classification |

## 7. Logical Determination

VAK_2.39 extends the relation-matrix from prāpti to aprāpti.

```text
AprāptiProfile:
    domainStatus
    afflictionStatus
    ethicalStatus
    timeStatus
```

The verse is technically dense, but its logical role is clear:

```text
aprāpti is not mere absence.
It is a classified structural relation.
```

Logical protocols:

```text
Disjunction:
    obscured / form / non-afflicted / indeterminate / past / not-yet-arisen

Hypothetical:
    if aprāpti has these status constraints,
    then its profile is threefold.
```

## 8. Relation to Indriya and Citta-Caitta

This verse confirms that non-acquisition is also a feature relation.

```text
Indriya
    = faculty configuration

Caitta
    = appearance configuration

Aprāpti
    = non-connection configuration
```

Thus absence is not nothing; it has lawful status within the conditioned system.

## 9. Organon Interpretation

Organon reading:

```text
ApraptiProfile:
    relationStatus = not-acquired
    afflictionStatus = akliṣṭa | nivṛta
    ethicalStatus = avyākṛta
    timeStatus = past | not-yet-arisen
    domainStatus = kāma | rūpa
```

Engineering implication:

```text
The Dataset must track structured absence,
not merely positive presence.
```

## 10. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .

vak:ApraptiFeatureSet a rdfs:Class .
vak:AklistaAvyakrtaApraptiProfile a vak:ApraptiFeatureSet ;
    vak:hasAfflictionStatus vak:Aklista ;
    vak:hasEthicalStatus vak:Avyakrta .
```

## 11. Commit History

```text
VAK_2.39 opened.
Method: kārikā-first speculative seed.
Theme: aprāpti classifications and domain/temporal restrictions.
Technical vocabulary marked for later Bhāṣya review.
Organon mapping: structured absence / non-connection profile in the Semantic Dataset.
Zero-padded file naming maintained: VAK_2.39.
```
