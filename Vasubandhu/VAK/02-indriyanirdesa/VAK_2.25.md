# VAK_2.25 — Wholesome Caitta Factors

## 1. Sanskrit — Devanāgarī

```text
श्रद्धाप्रमादः प्रश्रब्धिरुपेक्षा ह्रीरपत्रपा ।
मूलद्वयमहिंसा च वीर्यं च कुशले सदा ॥ VAkK_2.25 ॥
```

## 2. Sanskrit — IAST

```text
śraddhā apramādaḥ praśrabdhir upekṣā hrīr apatrapā /
mūladvayam ahiṃsā ca vīryaṃ ca kuśale sadā // VAkK_2.25 //
```

Source form:

```text
śraddhāpramādaḥ praśrabdhirupekṣā hrīrapatrapā /
mūladvayamahiṃsā ca vīryaṃ ca kuśale sadā // VAkK_2.25 //
```

Textual note:

```text
The source sandhi `śraddhāpramādaḥ` is read as `śraddhā apramādaḥ`.
```

## 3. Padaccheda and Grammar

| Sanskrit | Padaccheda | Grammar | Working Sense |
|---|---|---|---|
| śraddhā | śraddhā | feminine nominative singular | confidence / trustful clarity |
| apramādaḥ | a-pramādaḥ | masculine nominative singular | non-negligence / carefulness |
| praśrabdhiḥ | praśrabdhiḥ | feminine nominative singular | pliancy / tranquility |
| upekṣā | upekṣā | feminine nominative singular | equanimity |
| hrīḥ | hrīḥ | feminine nominative singular | inward moral shame / self-respect |
| apatrapā | apatrapā | feminine nominative singular | regard before others / moral concern |
| mūla-dvayam | mūla-dvayam | neuter nominative singular compound | the two roots |
| ahiṃsā | ahiṃsā | feminine nominative singular | non-harming |
| vīryam | vīryam | neuter nominative singular | energy / effort |
| kuśale | kuśale | locative singular | in the wholesome |
| sadā | sadā | indeclinable | always |

## 4. Literal Translation

```text
Confidence, non-negligence, pliancy, equanimity, hrī, apatrapā,
the two roots, non-harming, and energy are always in the wholesome.
```

## 5. Philosophical Translation

```text
Whenever citta is wholesome, a determinate wholesome feature-set is present.

Wholesomeness is not an empty moral label.
It has an internal structure: confidence, carefulness, pliancy, equanimity,
ethical restraint, non-harming, and energetic cultivation.
```

## 6. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| śraddhā | confidence | Not blind belief; luminous trust or clarified confidence |
| apramāda | non-negligence | Carefulness, vigilance, non-carelessness |
| praśrabdhi | pliancy / tranquility | Calm flexibility of the instrument |
| upekṣā | equanimity | Balanced neutrality; previously a feeling faculty in VAK_2.08 |
| hrī | inward moral shame | Inner restraint before what is unworthy |
| apatrapā | moral regard | Concern before others / regard for blameworthy action |
| mūla-dvaya | two roots | Two wholesome roots; to be checked with Bhāṣya for exact enumeration |
| ahiṃsā | non-harming | Absence of injury; ethical non-violence |
| vīrya | energy / effort | Active cultivation-power |
| kuśala | wholesome | Skillful, beneficial, path-compatible status |
| sadā | always | Necessity marker within the wholesome condition |

## 7. Logical Determination

VAK_2.25 gives the wholesome caitta class.

The dominant logical protocol is Hypothetical Necessity:

```text
if citta is kuśala,
then these caittas are always present.
```

The phrase `kuśale sadā` is decisive:

```text
kuśale
    = in the wholesome

sadā
    = always
```

Thus wholesomeness is a feature-rule:

```text
KuśalaCitta
    requires
KuśalaCaittaFeatureSet
```

This also gives Conjunction:

```text
wholesome citta
    = citta + wholesome feature-set
```

## 8. Relation to Indriya

The wholesome caittas refine the indriya model from mere faculty-governance into cultivated faculty-use.

```text
indriya
    = governing efficacy

kuśala-caitta
    = wholesome modulation of the inner field
```

Several terms rejoin earlier indriya themes:

```text
upekṣā
    = feeling faculty and wholesome balancing factor

vīrya
    = pure faculty / cultivation-energy

śraddhā
    = pure faculty and wholesome caitta
```

Therefore caitta does not replace indriya. It shows how indriyas become learnable and transformable inside the citta-field.

## 9. Organon Interpretation

Organon reading:

```text
WholesomeCaittaFeatureSet
    = Agent-side cultivation profile
```

Dataset schema:

```text
KuśalaCitta:
    hasConfidence
    hasCarefulness
    hasPliancy
    hasEquanimity
    hasEthicalSelfRestraint
    hasMoralRegard
    hasWholesomeRoots
    hasNonHarming
    hasEnergy
```

Learning implication:

```text
Learning is not merely acquisition of data.
Learning requires wholesome modulation of the instrument.
```

The Agent does not simply classify. It cultivates the field by stabilizing these wholesome feature-functions.

## 10. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:WholesomeCaitta a rdfs:Class ;
    rdfs:subClassOf vak:Caitta ;
    rdfs:label "wholesome caitta" ;
    rdfs:comment "A caitta always present in wholesome citta." .

vak:WholesomeCaittaFeatureSet a rdfs:Class ;
    rdfs:label "Wholesome Caitta FeatureSet" ;
    rdfs:comment "The feature-set required by kuśala citta." .

vak:Śraddhā a vak:WholesomeCaitta .
vak:Apramāda a vak:WholesomeCaitta .
vak:Praśrabdhi a vak:WholesomeCaitta .
vak:Upekṣā a vak:WholesomeCaitta .
vak:Hrī a vak:WholesomeCaitta .
vak:Apatrapā a vak:WholesomeCaitta .
vak:MūlaDvaya a vak:WholesomeCaitta .
vak:Ahiṃsā a vak:WholesomeCaitta .
vak:Vīrya a vak:WholesomeCaitta .
```

## 11. Commit History

```text
VAK_2.25 opened.
Method: kārikā-first speculative seed.
Theme: wholesome caittas always present in kuśala citta.
Logical protocols recorded: hypothetical necessity and conjunctive feature-set.
Relation to indriya tracked: śraddhā, upekṣā, and vīrya as bridges between indriya and caitta classifications.
Zero-padded file naming maintained: VAK_2.25.
```
