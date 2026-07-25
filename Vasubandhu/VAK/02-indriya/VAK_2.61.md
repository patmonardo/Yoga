# VAK_2.61 — Fourfold Pratyaya System

## 1. Sanskrit — Devanāgarī

```text
चित्तचैताः तथान्येऽपि संप्रयुक्तकवर्जिताः ।
चत्वारः प्रत्यया उक्ताः हेत्वाख्याः पञ्च हेतवः ॥ VAkK_2.61 ॥
```

## 2. Sanskrit — IAST

```text
cittacaitāḥ tathānye 'pi saṃprayuktakavarjitāḥ /
catvāraḥ pratyayā uktāḥ hetvākhyaḥ pañca hetavaḥ // VAkK_2.61 //
```

Source form:

```text
cittacaitāḥ tathānye 'pi saṃprayuktakavarjitāḥ /
catvāraḥ pratyayā uktāḥ hetvākhyaḥ pañca hetavaḥ // VAkK_2.61 //
```

## 3. Padaccheda and Grammar

| Sanskrit | Padaccheda | Grammar | Working Sense |
|---|---|---|---|
| citta-caitāḥ | citta-caitāḥ | nominative plural compound | citta and caittas |
| tathā | tathā | indeclinable | likewise |
| anye api | anye 'pi | nominative plural phrase | others also |
| saṃprayuktaka-varjitāḥ | saṃprayuktakavarjitāḥ | nominative plural compound | excluding the associated-ground |
| catvāraḥ | catvāraḥ | masculine nominative plural | four |
| pratyayāḥ | pratyayāḥ | masculine nominative plural | conditions |
| uktāḥ | uktāḥ | past passive participle | are said |
| hetu-ākhyāḥ | hetvākhyaḥ | masculine nominative plural | called hetu |
| pañca | pañca | numeral | five |
| hetavaḥ | hetavaḥ | masculine nominative plural | causes / grounds |

## 4. Literal Translation

```text
Citta and caittas, and others also, excluding the associated-ground,
are said to be four conditions. Five grounds are called hetu.
```

## 5. Philosophical Translation

```text
The system now shifts from hetu as ground to pratyaya as condition.
Citta, caittas, and other factors are treated under a fourfold condition-system,
while five of the grounds are gathered under the name hetu.
```

## 6. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| pratyaya | condition | Condition of arising or presentation |
| hetu | cause-ground | Ground-type from VAK_2.49ff |
| citta-caitta | citta and caittas | Appearance-field and feature-functions |
| saṃprayuktaka | associated-ground | Excluded here from the five hetus named as hetu-pratyaya |
| varjita | excluding | Exclusion marker |
| catvāraḥ | four | Fourfold condition-system |
| pañca hetavaḥ | five grounds | Five hetus functioning as hetu-pratyaya |

## 7. Logical Determination

VAK_2.61 opens the PratyayaFeatureSet.

```text
PratyayaFeatureSet:
    four conditions
```

It also relates pratyaya to the previous hetu-system:

```text
five hetus
    = hetu-pratyaya
    excluding saṃprayuktaka in this formulation
```

Logical protocol:

```text
Ground-system
    becomes
Condition-system
```

This is the Kantian after-the-fact rationale becoming explicit condition logic.

## 8. Relation to the Objective Logic

The hetu-phala engine gave objective ground-result relations.
The pratyaya block gives the condition-types by which arising is intelligible.

```text
Hetu
    = ground

Phala
    = result

Pratyaya
    = condition of arising
```

## 9. Organon Interpretation

```text
ConditionEngine:
    conditionType
    applicableFactors
    relationToHetuEngine
```

The Dataset now requires condition metadata in addition to ground-result mappings.

## 10. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .

vak:PratyayaFeatureSet a rdfs:Class .
vak:HetuPratyaya a vak:Pratyaya .
vak:SamanantaraPratyaya a vak:Pratyaya .
vak:AlambanaPratyaya a vak:Pratyaya .
vak:AdhipatiPratyaya a vak:Pratyaya .
```

## 11. Commit History

```text
VAK_2.61 opened.
Method: kārikā-first speculative seed.
Theme: opening of the fourfold pratyaya system and its relation to the hetu system.
Zero-padded file naming maintained: VAK_2.61.
```
