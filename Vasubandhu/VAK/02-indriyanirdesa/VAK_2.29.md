# VAK_2.29 — Unwholesome and Affliction Caitta Count-Profiles

## 1. Sanskrit — Devanāgarī

```text
आवेणिके त्वकुशले दृष्टियुक्ते च विंशतिः ।
क्लेशैश्चतुर्भिः क्रोधाद्यैः कौकृत्येनैकविंशतिः ॥ VAkK_2.29 ॥
```

## 2. Sanskrit — IAST

```text
āveṇike tv akuśale dṛṣṭiyukte ca viṃśatiḥ /
kleśaiś caturbhiḥ krodhādyaiḥ kaukṛtyenaikaviṃśatiḥ // VAkK_2.29 //
```

Source form:

```text
āveṇike tvakuśale dṛṣṭiyukte ca viṃśatiḥ /
kleśaiścaturbhiḥ krodhādyaiḥ kaukṛtyenaikaviṃśatiḥ // VAkK_2.29 //
```

## 3. Padaccheda and Grammar

| Sanskrit | Padaccheda | Grammar | Working Sense |
|---|---|---|---|
| āveṇike | āveṇike | locative singular | in the isolated / specific case |
| tu | tu | particle | but |
| akuśale | akuśale | locative singular | in the unwholesome |
| dṛṣṭi-yukte | dṛṣṭi-yukte | locative singular compound | conjoined with view |
| ca | ca | indeclinable | and |
| viṃśatiḥ | viṃśatiḥ | feminine nominative singular | twenty |
| kleśaiḥ | kleśaiḥ | instrumental plural | with afflictions |
| caturbhiḥ | caturbhiḥ | instrumental plural | with four |
| krodha-ādyaiḥ | krodhādyaiḥ | instrumental plural compound | beginning with anger |
| kaukṛtyena | kaukṛtyena | instrumental singular | with regret / remorse |
| ekaviṃśatiḥ | eka-viṃśatiḥ | feminine nominative singular | twenty-one |

## 4. Literal Translation

```text
But in the unwholesome isolated case, and in that conjoined with view, there are twenty.
With the four afflictions, beginning with anger, or with kaukṛtya, there are twenty-one.
```

## 5. Philosophical Translation

```text
Unwholesome citta has its own discriminated count-profiles.
In the isolated unwholesome case, and in the case conjoined with view, the associated factors number twenty.
When four afflictions beginning with anger are present, or when regret is present, the profile rises to twenty-one.
```

## 6. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| āveṇika | isolated / specific | Technical case; to verify with Bhāṣya |
| akuśala | unwholesome | Ethically unskillful status |
| dṛṣṭi-yukta | conjoined with view | Citta joined with a view or view-factor |
| viṃśati | twenty | Count-profile |
| kleśa | affliction | Disturbing factor; root of distortion |
| caturbhiḥ | four | Count of afflictions in this profile |
| krodha-ādi | beginning with anger | Minor-affliction set from VAK_2.27 |
| kaukṛtya | regret / remorse | Optional/additional factor also in VAK_2.28 |
| ekaviṃśati | twenty-one | Count-profile |

## 7. Logical Determination

VAK_2.29 extends the discriminative catalog into unwholesome and afflicted profiles.

The dominant protocol is Hypothetical Count-Logic:

```text
if citta is akuśala and āveṇika,
then caittaCount = 20.

if citta is dṛṣṭi-yukta,
then caittaCount = 20.

if citta is joined with four kleśas beginning with krodha,
then caittaCount = 21.

if citta is joined with kaukṛtya,
then caittaCount = 21.
```

The verse also gives Disjunction:

```text
unwholesome isolated profile
view-conjoined profile
kleśa-conjoined profile
kaukṛtya-conjoined profile
```

## 8. Relation to Indriya

This verse mirrors the earlier indriya configuration logic, but at the level of appearance.

```text
Indriya-profile
    = what faculty array is configured

Caitta-profile
    = what mental feature array is configured
```

Here the caitta array is distorted by unwholesome status, view, affliction, or regret.

Thus:

```text
Caitta
    = appearance-level law of how indriya-givenness is mentally configured.
```

## 9. Organon Interpretation

Organon reading:

```text
UnwholesomeCittaProfile:
    ethicalStatus = akuśala
    subtype = āveṇika | dṛṣṭi-yukta | kleśa-yukta | kaukṛtya-yukta
    caittaCount = 20 | 21
```

Learning implication:

```text
The Agent requires discriminative diagnosis:
    not merely unwholesome / wholesome,
    but which unwholesome configuration,
    and with what countable feature-array.
```

This is caitta as diagnostic FeatureSet.

## 10. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .

vak:AvenikaAkusalaCittaProfile a vak:CittaCaittaProfile ;
    vak:hasEthicalStatus vak:Akusala ;
    vak:hasSubtype vak:Avenika ;
    vak:hasCaittaCount 20 .

vak:DrstiYuktaCittaProfile a vak:CittaCaittaProfile ;
    vak:hasSubtype vak:DrstiYukta ;
    vak:hasCaittaCount 20 .

vak:KlesaYuktaCittaProfile a vak:CittaCaittaProfile ;
    vak:hasSubtype vak:KlesaYukta ;
    vak:hasCaittaCount 21 .

vak:KaukṛtyaYuktaCittaProfile a vak:CittaCaittaProfile ;
    vak:hasSubtype vak:KaukṛtyaYukta ;
    vak:hasCaittaCount 21 .
```

## 11. Commit History

```text
VAK_2.29 opened.
Method: kārikā-first speculative seed.
Theme: unwholesome and affliction caitta count-profiles.
Logical protocols recorded: hypothetical count-rule and disjunctive subtype classification.
Relation to indriya tracked: caitta profile as appearance-level configuration logic.
Zero-padded file naming maintained: VAK_2.29.
```
