# VAK_2.45 — Jīvita and the Marks of the Conditioned

## 1. Sanskrit — Devanāgarī

```text
आयुर्जीवितमाधार ऊष्मविज्ञायोर्हि यः ।
लक्षणानि पुनर्जातिर्जरा स्थितिरनित्यता ॥ VAkK_2.45 ॥
```

## 2. Sanskrit — IAST

```text
āyur jīvitam ādhāra ūṣmavijñāyor hi yaḥ /
lakṣaṇāni punar jātir jarā sthitir anityatā // VAkK_2.45 //
```

Source form:

```text
āyurjīvitam ādhāra ūṣmavijñāyorhi yaḥ /
lakṣaṇāni punarjātirjarā sthitiranityatā // VAkK_2.45 //
```

## 3. Padaccheda and Grammar

| Sanskrit | Padaccheda | Grammar | Working Sense |
|---|---|---|---|
| āyuḥ | āyuḥ | neuter nominative singular | lifespan / life-duration |
| jīvitam | jīvitam | neuter nominative singular | life / living continuity |
| ādhāraḥ | ādhāraḥ | masculine nominative singular | support / basis |
| ūṣma-vijñānayoḥ | ūṣmavijñānayoḥ | genitive dual | of heat and vijñāna |
| hi | hi | particle | indeed |
| yaḥ | yaḥ | relative pronoun | which / that which |
| lakṣaṇāni | lakṣaṇāni | neuter nominative plural | marks / determinations |
| punaḥ | punaḥ | indeclinable | again / further |
| jātiḥ | jātiḥ | feminine nominative singular | arising / birth |
| jarā | jarā | feminine nominative singular | aging / decay |
| sthitiḥ | sthitiḥ | feminine nominative singular | persistence / duration |
| anityatā | anityatā | feminine nominative singular | impermanence |

## 4. Literal Translation

```text
Āyuḥ is jīvita, that which is the support of heat and vijñāna.
The marks, again, are arising, aging, persistence, and impermanence.
```

## 5. Philosophical Translation

```text
Life is defined as the supporting continuity of heat and vijñāna.
The conditioned is marked by four lifecycle determinations:
arising, aging, persistence, and impermanence.
```

## 6. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| āyuḥ | lifespan | Duration of life |
| jīvita | life-continuity | Structural support of the living series |
| ādhāra | support | Basis or sustaining support |
| ūṣman | heat | Vital heat; technical relation to life |
| vijñāna | knowledge-event | Not translated as consciousness in this project |
| lakṣaṇa | mark / determination | Feature-mark of the conditioned |
| jāti | arising | Birth or coming-to-be of a conditioned item |
| jarā | aging | Transformation/decay of what has arisen |
| sthiti | persistence | Standing, duration, continuity |
| anityatā | impermanence | Perishing / non-permanence |

## 7. Logical Determination

VAK_2.45 gives the ConditionedMarkFeatureSet.

```text
ConditionedMarkFeatureSet:
    jāti
    jarā
    sthiti
    anityatā
```

This is lifecycle logic:

```text
conditioned item
    arises
    persists
    ages
    ceases / is impermanent
```

It also defines jīvita as a support-operator:

```text
jīvita
    = support of heat and vijñāna
```

## 8. Relation to the Feature Logic

This block moves from structural operators to lifecycle marks.

```text
Viprayukta-saṃskāra
    = structural operator layer

Lakṣaṇa
    = lifecycle mark layer
```

The feature-logic of conditioned experience now gains temporal determinacy.

## 9. Organon Interpretation

Organon reading:

```text
LifecycleProfile:
    arising
    persistence
    aging
    impermanence
```

Engineering implication:

```text
Every conditioned event requires lifecycle metadata.
```

A Dataset item is not simply present. It has a lifecycle profile.

## 10. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:ConditionedMarkFeatureSet a rdfs:Class ;
    rdfs:label "Conditioned Mark FeatureSet" .

vak:Jati a vak:ConditionedMark .
vak:Jara a vak:ConditionedMark .
vak:Sthiti a vak:ConditionedMark .
vak:Anityata a vak:ConditionedMark .

vak:Jivita a vak:ViprayuktaSamskara ;
    vak:hasSupportFunction vak:SupportOfHeatAndVijnana .
```

## 11. Commit History

```text
VAK_2.45 opened.
Method: kārikā-first speculative seed.
Theme: jīvita as support and the four marks of the conditioned.
Organon mapping: lifecycle metadata for conditioned events.
Zero-padded file naming maintained: VAK_2.45.
```
