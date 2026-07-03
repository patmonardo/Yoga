# VAK_2.33 — Functional Caitta Definitions

## 1. Sanskrit — Devanāgarī

```text
वितर्कचारावौदार्यसूक्ष्मते मान उन्नतिः ।
मदः स्वधर्मे रक्तस्य पर्यादानं तु चेतसः ॥ VAkK_2.33 ॥
```

## 2. Sanskrit — IAST

```text
vitarkacārāv audāryasūkṣmate māna unnatiḥ /
madaḥ svadharme raktasya paryādānaṃ tu cetasaḥ // VAkK_2.33 //
```

Source form:

```text
vitarkacārā vaudāryasūkṣmate māna unnatiḥ /
madaḥ svadharme raktasya paryādānaṃ tu cetasaḥ // VAkK_2.33 //
```

## 3. Textual Caution

The local source marks this verse as the second consecutive `VAkK_2.33`.

For working repo continuity:

```text
Source numbering:
    second duplicated VAkK_2.33

Working numbering:
    VAK_2.33
```

The segmentation of `vitarkacārāv audāryasūkṣmate` should be checked against the Bhāṣya and printed editions.

## 4. Padaccheda and Grammar

| Sanskrit | Padaccheda | Grammar | Working Sense |
|---|---|---|---|
| vitarka-cārau | vitarka-cārau | masculine nominative dual | vitarka and vicāra/cāra; source form to verify |
| audārya-sūkṣmate | audārya-sūkṣmate | feminine nominative dual | coarseness and subtlety |
| mānaḥ | mānaḥ | masculine nominative singular | conceit / measure of self-elevation |
| unnatiḥ | unnatiḥ | feminine nominative singular | elevation / lifting up |
| madaḥ | madaḥ | masculine nominative singular | intoxication / prideful elation |
| svadharme | sva-dharme | locative singular | in one's own dharma / own condition |
| raktasya | raktasya | genitive singular | of one attached / colored by attachment |
| paryādānam | paryādānam | neuter nominative singular | saturation / taking-over / overwhelming |
| tu | tu | particle | but / and as for |
| cetasaḥ | cetasaḥ | genitive singular | of citta / of the mental field |

## 5. Literal Translation

```text
Vitarka and cāra/vicāra are coarseness and subtlety.
Māna is elevation.
Mada is the taking-over of the citta of one attached to one's own condition.
```

## 6. Philosophical Translation

```text
The catalog now defines selected caitta-functions by their operation.

Vitarka and vicāra are distinguished as coarse and subtle modes.
Māna is the elevation of the self-measure.
Mada is the saturation of citta when it is attached to its own condition.
```

## 7. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| vitarka | vitarka | Left untranslated; coarse application or initial placing |
| cāra / vicāra | cāra / vicāra | Source reads cāra; likely linked to vicāra; to verify |
| audārya | coarseness | Grossness or coarser mode |
| sūkṣmatā | subtlety | Finer mode |
| māna | conceit / self-measure | Defined here as unnati, elevation |
| unnati | elevation | Raising or inflation |
| mada | intoxication / prideful elation | Attached satisfaction in one's own condition |
| svadharma | own dharma / own condition | One's own basis, quality, or state |
| rakta | attached / colored | Affected by attachment |
| paryādāna | saturation / taking-over | Full occupation or overwhelming of citta |
| citta | mental field | Appearance-side field of mental operation |

## 8. Logical Determination

VAK_2.33 gives functional definitions rather than merely listing classes.

```text
vitarka / vicāra
    = coarse / subtle modes

māna
    = elevation

mada
    = saturation of attached citta
```

The dominant protocol is Determinate Specification:

```text
term
    = functional definition
```

This is discriminative knowledge in a stricter sense:

```text
not only:
    which caittas belong to which profile

but:
    what specific operation each caitta performs
```

## 9. Relation to Indriya

The indriya-system gives governing faculty-functions.

This verse shows caittas as fine internal functions of appearance:

```text
vitarka / vicāra
    configure the mode of mental approach

māna
    configures self-elevation

mada
    configures attached saturation of citta
```

So caitta is to citta what feature-operation is to a field:

```text
Citta
    = appearance-field

Caitta
    = determinate function of that field
```

## 10. Organon Interpretation

Organon reading:

```text
CaittaFunctionDefinition:
    caittaName
    functionalMode
    cittaEffect
```

Dataset schema:

```text
VitarkaVicaraPair:
    coarseMode = vitarka
    subtleMode = vicāra

Mana:
    operation = elevation

Mada:
    condition = attachment to own condition
    effect = citta-saturation
```

Learning implication:

```text
The Agent must not only classify feature-sets.
It must know the functional meaning of each feature.
```

This is FeatureSet semantics, not merely FeatureSet enumeration.

## 11. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:CaittaFunctionDefinition a rdfs:Class ;
    rdfs:label "Caitta Function Definition" ;
    rdfs:comment "A functional specification of a caitta." .

vak:Vitarka vak:hasFunctionalMode vak:CoarseMode .
vak:Vicara vak:hasFunctionalMode vak:SubtleMode .
vak:Mana vak:hasOperation vak:Elevation .
vak:Mada vak:hasCondition vak:AttachmentToOwnCondition ;
    vak:hasEffect vak:CittaSaturation .
```

## 12. Commit History

```text
VAK_2.33 opened.
Method: kārikā-first speculative seed.
Theme: functional definitions of selected caittas.
Source numbering caution recorded: second duplicated VAkK_2.33 retained as VAK_2.33.
Logical protocol recorded: determinate specification of caitta-functions.
Relation to indriya tracked: caitta as appearance-level functional operation.
Zero-padded file naming maintained: VAK_2.33.
```
