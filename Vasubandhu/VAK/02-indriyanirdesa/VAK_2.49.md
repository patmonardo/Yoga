# VAK_2.49 — Sixfold Hetu System

## 1. Sanskrit — Devanāgarī

```text
कारणं सहभूश्चैव सभागः संप्रयुक्तकः ।
सर्वत्रगो विपाकाख्यः षड्विधो हेतुरिष्यते ॥ VAkK_2.49 ॥
```

## 2. Sanskrit — IAST

```text
kāraṇaṃ sahabhūś caiva sabhāgaḥ saṃprayuktakaḥ /
sarvatrago vipākākhyaḥ ṣaḍvidho hetur iṣyate // VAkK_2.49 //
```

## 3. Literal Translation

```text
Cause-as-condition, co-arisen, homogeneous, associated,
omnipresent, and that called maturation: the hetu is held to be sixfold.
```

## 4. Philosophical Translation

```text
The objective ground-system is sixfold.
Conditioned arising is not explained by one generic cause, but by distinct ground-types:
conditioning support, co-presence, similarity, association, pervasive affliction, and maturation.
```

## 5. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| hetu | cause-ground | Objective ground of arising; not yet teleological subjective ground |
| kāraṇa-hetu | conditioning cause-ground | General enabling ground |
| sahabhū-hetu | co-arisen ground | Mutual co-presence ground |
| sabhāga-hetu | homogeneous ground | Similar-class ground |
| saṃprayuktaka-hetu | associated ground | Citta-caitta association as ground |
| sarvatraga-hetu | omnipresent/pervasive ground | Pervasive afflicted ground |
| vipāka-hetu | maturation ground | Ground of maturation-result |
| ṣaḍvidha | sixfold | Feature-division marker |

## 6. Logical Determination

VAK_2.49 opens the HetuFeatureSet.

```text
HetuFeatureSet:
    kāraṇa
    sahabhū
    sabhāga
    saṃprayuktaka
    sarvatraga
    vipāka
```

This is Objective Logic:

```text
conditioned facts arise by ground-types,
not by subjective intention.
```

## 7. Organon Interpretation

```text
HetuEngine:
    groundType -> arisingProfile
```

The engine begins here: every event must be traceable to one or more ground-types.

## 8. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .

vak:HetuFeatureSet a rdfs:Class .
vak:KaranaHetu a vak:Hetu .
vak:SahabhuHetu a vak:Hetu .
vak:SabhagaHetu a vak:Hetu .
vak:SamprayuktakaHetu a vak:Hetu .
vak:SarvatragaHetu a vak:Hetu .
vak:VipakaHetu a vak:Hetu .
```

## 9. Commit History

```text
VAK_2.49 opened.
Method: kārikā-first speculative seed.
Theme: sixfold hetu system as objective ground engine.
```
