# VAK_2.30 — Indeterminate Caitta Count-Profiles and Middha

## 1. Sanskrit — Devanāgarī

```text
निवृतेऽष्टादश अन्यत्र द्वादशाव्याकृते मताः ।
मिद्धं सर्वाविरोधित्वाद्यत्र स्यादधिकं हि तत् ॥ VAkK_2.30 ॥
```

## 2. Sanskrit — IAST

```text
nivṛte 'ṣṭādaśa anyatra dvādaśāvyākṛte matāḥ /
middhaṃ sarvāvirodhitvād yatra syād adhikaṃ hi tat // VAkK_2.30 //
```

Source form:

```text
nivṛte 'ṣṭādaśa anyatra dvādaśāvyākṛte matāḥ /
middhaṃ sarvāvirodhitvādyatra syādadhikaṃ hi tat // VAkK_2.30 //
```

## 3. Padaccheda and Grammar

| Sanskrit | Padaccheda | Grammar | Working Sense |
|---|---|---|---|
| nivṛte | nivṛte | locative singular | in the obscured / veiled |
| aṣṭādaśa | aṣṭādaśa | numeral | eighteen |
| anyatra | anyatra | indeclinable | elsewhere / in another case |
| dvādaśa | dvādaśa | numeral | twelve |
| avyākṛte | avyākṛte | locative singular | in the indeterminate / ethically neutral |
| matāḥ | matāḥ | masculine nominative plural | considered / held |
| middham | middham | neuter nominative singular | sleepiness / torpor |
| sarva-avirodhitvāt | sarva-avirodhitvāt | ablative singular compound | because of non-opposition to all |
| yatra | yatra | adverb | where |
| syāt | syāt | optative, 3rd singular | it may be |
| adhikam | adhikam | neuter nominative singular | additional |
| hi | hi | particle | indeed |
| tat | tat | pronoun | that |

## 4. Literal Translation

```text
In the obscured there are eighteen; elsewhere, in the indeterminate, twelve are held.
Middha, because it is opposed to none, is additional wherever it may occur.
```

## 5. Philosophical Translation

```text
The catalog further distinguishes obscured and indeterminate citta-profiles.
An obscured citta has eighteen associated factors.
Another indeterminate citta has twelve.
Sleepiness or torpor may be added wherever it occurs, because it is not incompatible with any of the profiles.
```

## 6. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| nivṛta | obscured / veiled | Covered or obstructed status; to verify context with Bhāṣya |
| aṣṭādaśa | eighteen | Count-profile |
| anyatra | elsewhere | Alternative case marker |
| avyākṛta | indeterminate / neutral | Neither wholesome nor unwholesome in ethical determination |
| dvādaśa | twelve | Count-profile |
| middha | sleepiness / torpor | Mental heaviness; mobile/additional factor |
| avirodhitva | non-opposition | Compatibility condition |
| yatra syāt | wherever it may be | Explicit conditional location |
| adhika | additional | Added factor beyond base count |

## 7. Logical Determination

VAK_2.30 continues the citta-caitta catalog through indeterminate profiles.

The dominant protocol is Hypothetical Count-Logic:

```text
if citta is nivṛta,
then caittaCount = 18.

if citta is another avyākṛta case,
then caittaCount = 12.
```

The verse also gives a compatibility rule:

```text
if middha occurs,
then add middha,
because middha is not opposed to any profile.
```

This is important as formal logic:

```text
avirodha
    = compatibility condition
```

So VAK_2.30 introduces a rule for optional feature-addition based on non-contradiction.

## 8. Relation to Indriya

Earlier indriya profiles determined faculty configurations by realm, purity, acquisition, and exclusion.

Here caitta profiles determine appearance-configurations by ethical indeterminacy and compatibility.

```text
Indriya
    = givenness-profile

Caitta
    = appearance-profile

Middha
    = optional compatible feature
```

So the citta-caitta catalog adds a new logic:

```text
feature may be added
where it does not contradict the profile.
```

## 9. Organon Interpretation

Organon reading:

```text
CittaCaittaProfile:
    ethicalStatus = nivṛta | avyākṛta
    caittaCount = 18 | 12
    optionalCompatibleFeature = middha
```

Learning implication:

```text
The Agent requires compatibility logic.
A feature is not merely present or absent;
it may be admissible wherever it does not oppose the profile.
```

This begins a protocol of lawful feature-extension.

## 10. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .

vak:NivrtaCittaProfile a vak:CittaCaittaProfile ;
    vak:hasStatus vak:Nivrta ;
    vak:hasCaittaCount 18 .

vak:AvyakrtaCittaProfile a vak:CittaCaittaProfile ;
    vak:hasStatus vak:Avyakrta ;
    vak:hasCaittaCount 12 .

vak:Middha a vak:Caitta ;
    vak:hasCompatibilityStatus vak:NonOpposedToAll .

vak:allowsAdditionalFactor a rdf:Property .
```

## 11. Commit History

```text
VAK_2.30 opened.
Method: kārikā-first speculative seed.
Theme: obscured and indeterminate citta count-profiles with middha compatibility rule.
Logical protocols recorded: hypothetical count-rule and non-contradiction-based optional addition.
Relation to indriya tracked: caitta catalog as appearance-level feature compatibility model.
Zero-padded file naming maintained: VAK_2.30.
```
