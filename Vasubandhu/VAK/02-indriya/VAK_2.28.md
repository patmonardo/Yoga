# VAK_2.28 — Wholesome Desire-Realm Caitta Count-Profile

## 1. Sanskrit — Devanāgarī

```text
सवितर्कविचारत्वात् कुशले कामचेतसि ।
द्वाविंशतिश्चैतसिकाः कौकृत्यमधिकं क्वचित् ॥ VAkK_2.28 ॥
```

## 2. Sanskrit — IAST

```text
savitarkavicāratvāt kuśale kāmacetasi /
dvāviṃśatiś caitasikāḥ kaukṛtyam adhikaṃ kvacit // VAkK_2.28 //
```

Source form:

```text
savitarkavicāratvāt kuśale kāmacetasi /
dvāṃviṃśatiścaitasikāḥ kaukṛtyamadhikaṃ kvacit // VAkK_2.28 //
```

Textual caution:

```text
The source gives `dvāṃviṃśatiḥ`; normalized here as `dvāviṃśatiḥ`.
```

## 3. Padaccheda and Grammar

| Sanskrit | Padaccheda | Grammar | Working Sense |
|---|---|---|---|
| savitarka-vicāratvāt | sa-vitarka-vicāratvāt | ablative singular abstract compound | because of being with vitarka and vicāra |
| kuśale | kuśale | locative singular | in the wholesome |
| kāma-cetasi | kāma-cetasi | locative singular compound | in a desire-realm citta |
| dvāviṃśatiḥ | dvā-viṃśatiḥ | feminine nominative singular | twenty-two |
| caitasikāḥ | caitasikāḥ | masculine nominative plural | caittas / mental factors |
| kaukṛtyam | kaukṛtyam | neuter nominative singular | regret / remorse / worry over action |
| adhikam | adhikam | neuter nominative singular | additional |
| kvacit | kvacit | indeclinable | sometimes, in some cases |

## 4. Literal Translation

```text
Because it is with vitarka and vicāra, in a wholesome desire-realm citta
there are twenty-two caittas; in some cases, kaukṛtya is additional.
```

## 5. Philosophical Translation

```text
A wholesome citta in the desire realm has a determinate count-profile.
Because it operates with vitarka and vicāra, it includes twenty-two associated mental factors.
In some cases, regret or reflective unease over action is added.
```

## 6. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| savitarka | with vitarka | Leave vitarka untranslated initially; coarse initial application or discursive placement |
| savicāra | with vicāra | Leave vicāra untranslated initially; finer examination or sustained consideration |
| kuśala | wholesome | Skillful, beneficial, path-compatible status |
| kāma-citta | desire-realm citta | Citta operating in the desire realm |
| caitasika | caitta / mental factor | Associated function of citta |
| dvāviṃśati | twenty-two | Count-profile |
| kaukṛtya | regret / remorse | Additional factor in some cases |
| kvacit | sometimes | Conditional variability marker |

## 7. Logical Determination

VAK_2.28 begins the discriminative catalog of citta-caitta configurations.

The dominant protocol is Hypothetical Count-Logic:

```text
if citta is kuśala
and if it is kāma-realm
and because it is savitarka-savicāra,
then caittaCount = 22.
```

It also includes a conditional extension:

```text
kvacit
    = in some cases

if kaukṛtya is present,
then add one further factor.
```

Thus the citta-caitta relation becomes a feature-count model.

## 8. Relation to Indriya

The previous indriya verses counted faculty configurations. This verse now counts associated caitta configurations.

```text
Indriya count-profile
    = faculty-array of governing givenness

Caitta count-profile
    = feature-array of appearing citta-operation
```

So the same logical protocol reappears at the appearance level:

```text
Dhātu-Indriya principle
    appears as
Citta-Caitta feature-count discrimination
```

## 9. Organon Interpretation

Organon reading:

```text
KuśalaKāmaCittaProfile:
    realm = kāma
    ethicalStatus = kuśala
    vitarkaStatus = present
    vicāraStatus = present
    caittaCount = 22
    optionalAdditionalFactor = kaukṛtya
```

Learning implication:

```text
A learning-state is not merely wholesome or unwholesome.
It has a realm, a mode of discursive operation, and a countable feature-array.
```

This is discriminative knowledge of the citta-caitta catalog.

## 10. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:KusalaKamaCittaProfile a vak:CittaCaittaProfile ;
    rdfs:label "Wholesome desire-realm citta profile" ;
    vak:hasRealmStatus vak:KamaRealm ;
    vak:hasEthicalStatus vak:Kusala ;
    vak:hasVitarkaStatus vak:VitarkaPresent ;
    vak:hasVicaraStatus vak:VicaraPresent ;
    vak:hasCaittaCount 22 ;
    vak:hasOptionalFactor vak:Kaukṛtya .
```

## 11. Commit History

```text
VAK_2.28 opened.
Method: kārikā-first speculative seed.
Theme: wholesome desire-realm citta count-profile.
Logical protocols recorded: hypothetical count-rule and optional extension.
Relation to indriya tracked: caitta count-profile as appearance-level repetition of indriya configuration logic.
Zero-padded file naming maintained: VAK_2.28.
```
