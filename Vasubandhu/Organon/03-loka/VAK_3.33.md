# VAK_3.33 — Mental Ranging by Realm

## 1. Sanskrit (Devanāgarī)


> कामे स्वालम्बनाः सर्वे रूपी द्वादशगोचरः ।
>
> त्रयाणामुत्तरः ध्यानद्वये द्वादश कामगाः ॥ ३.३३ ॥

## 2. Sanskrit (IAST)


> kāme svālambanāḥ sarve rūpī dvādaśagocaraḥ /
>
> trayāṇām uttaraḥ dhyānadvaye dvādaśa kāmagāḥ // 3.33 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| kāme | locative singular of `kāma` | in the desire realm |
| svālambanāḥ | nominative masculine plural; `sva` + `ālambana` | having their own realm as cognitive Condition |
| sarve | nominative masculine plural | all, namely all eighteen Mental Rangings |
| rūpī | nominative masculine singular | the Form realm, understood from the doctrinal context |
| dvādaśagocaraḥ | nominative masculine singular compound | field or range of twelve |
| trayāṇām | genitive plural numeral | of three mental rangings |
| uttaraḥ | nominative masculine singular | the higher realm, namely the Formless realm |
| dhyānadvaye | locative singular compound | in the pair of meditations; the first and second dhyānas |
| dvādaśa | nominative masculine plural numeral | twelve Mental Rangings |
| kāmagāḥ | nominative masculine plural; `kāma` + `ga` | going toward desire; taking the desire realm as cognitive Condition |

The compact verse moves between two axes which the Bhāṣya explicitly
distinguishes: realm-membership (`pratisaṃyukta`) and cognitive Condition
(`ālambana`).

## 4. Grammar


The first three clauses concern realms as cognitive Conditions:

```text
kāme sarve svālambanāḥ
    = in the desire realm, all [eighteen] have their own [realm]
      as cognitive Condition

rūpī dvādaśa-gocaraḥ
    = the form realm is the range of twelve

uttaraḥ trayāṇām [gocaraḥ]
    = the higher [formless realm] is the range of three
```

`Gocaraḥ` is carried forward into the third clause. The Bhāṣya resolves
`rūpī` as the form realm and `uttaraḥ` as the still higher, formless realm.

The final clause changes the question from possible range to the
rangings belonging to the form realm:

```text
dhyāna-dvaye dvādaśa
    = in the [first] two dhyānas there are twelve

[te] kāma-gāḥ
    = those [twelve] go toward the desire realm
```

The Bhāṣya glosses `kāmagāḥ` as taking the desire realm as cognitive
Condition.

## 5. Translation


### Close syntactic construe

> In the desire realm, all [eighteen] have their own [realm] as
> cognitive Condition. The Form realm is the range of twelve; the higher realm is
> the range of three. In the pair of dhyānas there are twelve, and [those
> twelve] go toward the desire realm.

### Bhāṣya-informed study translation

> All eighteen Mental Rangings occur in the desire realm, and the desire realm
> can serve as the cognitive Condition for all eighteen. The Form realm can serve as
> the range of twelve, because the six Rangings concerned with Smell and Taste
> are excluded there. The higher, formless realm can serve as the range of
> only the three Dharma-Rangings, because Form and the other sensory
> Conditions are absent there. In the first two dhyānas, twelve Mental
> Rangings occur—the six distress-Rangings being absent—and all twelve can
> take the desire realm as their cognitive Condition.

The identification of the omitted rangings, the reference of `rūpī` and
`uttaraḥ`, and the interpretation of `kāmagāḥ` are Bhāṣya
determinations.

## 6. Philosophical Translation

VAK 3.32 established the repeated ranging of Mind under the force of Feeling.
Here the Bhāṣya distinguishes a ranging's connection with a realm from the
realm that conditions it. All eighteen rangings are possible in the desire
realm; the Form realm conditions twelve, and the Formless realm conditions
three. The first two dhyānas connect twelve rangings with the Form realm,
while the desire realm can condition those same twelve.

## 7. Technical Vocabulary


| Sanskrit | Controlled rendering | Determination in this unit |
|---|---|---|
| manopavicāra | Mental Ranging | Feeling-governed mental traversal classified by mode and cognitive Condition |
| kāmadhātu | desire realm | realm in which all eighteen Mental Rangings occur and which all eighteen may take as Condition |
| rūpadhātu | Form realm | range of twelve, excluding Smell- and Taste-Rangings |
| ārūpyadhātu | Formless realm | range of the three Dharma-Rangings alone |
| pratisaṃyukta | connected with / belonging to | identifies the realm to which a ranging belongs |
| ālambana | cognitive Condition / support | that on which the ranging depends |
| svālambana | own cognitive Condition | one's own realm functioning as Condition |
| gocara | field / range | admissible range of operation |
| gandha | Smell | sensory Condition absent from the Form realm |
| rasa | Taste | sensory Condition absent from the Form realm |
| dharmopavicāra | Dharma-Ranging | Mental Ranging whose Condition is Dharma |
| dhyānadvaya | pair of dhyānas | first and second meditative levels of the form realm |
| daurmanasyopavicāra | distress-Ranging | sixfold affective class absent from the first two dhyānas |
| kāmaga | desire-going / desire-directed | taking the desire realm as cognitive Condition |
| gami-prayoga | use of a verb of going | Bhāṣya's explanation of “going” as taking a cognitive Condition |

Two determinations must not be collapsed:

```text
pratisaṃyukta
    = where the mental ranging belongs

ālambana / gocara
    = what field the mental ranging can take up
```

## 8. Logical Determination


### Realm-connection differs from cognitive Condition

```text
MentalRanging {
    realmOfBelonging
    affectiveMode
    condition
    realmAsCondition
}
```

Therefore:

```text
realmOfBelonging(x) = rūpadhātu

does not entail

realmAsCondition(x) = rūpadhātu
```

The twelve rangings of the first two dhyānas belong to the form realm but may
take the desire realm as their cognitive Condition.

### Admissible range follows the constitution of the field

| realm as cognitive Condition | admissible rangings | ground of restriction |
|---|---:|---|
| desire realm | 18 | all six Conditions are available |
| Form realm | 12 | Smell and Taste are absent: `18 − (3 + 3)` |
| Formless realm | 3 | only Dharma remains available |

This is an immanent restriction:

```text
Condition lacks kind y
    → no ranging-to-y can take that realm as its Condition
```

The twelve belonging to the first two dhyānas are calculated on another axis:

```text
6 gladness-Rangings
    + 6 equanimity-Rangings
    = 12

6 distress-Rangings excluded
```

### “Going” is cognitive directedness

```text
kāmān gacchanti
    = cognitive directedness toward desire

kāmadhātum ālambante
    = they take the desire realm as cognitive Condition
```

The World System permits cross-realm cognitive range without confusing that
range with a change of station.

## 9. Interpretive Note


## 10. OWL++ Seed


```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .

vak:VAK_3_33
    a vak:Karika ;
    vak:continues vak:VAK_3_32 ;
    vak:distinguishes vak:RealmOfBelonging, vak:RealmAsCondition ;
    vak:distributes vak:EighteenMentalRangingsByRealm .

vak:DesireRealmAsCondition
    vak:admits 18 ;
    vak:admitsAffectiveMode vak:Gladness, vak:Distress, vak:Equanimity ;
    vak:admitsCondition vak:FormCondition, vak:SoundCondition,
        vak:SmellCondition, vak:TasteCondition, vak:TangibleCondition,
        vak:DharmaCondition .

vak:FormRealmAsCondition
    vak:admits 12 ;
    vak:excludesCondition vak:SmellCondition, vak:TasteCondition .

vak:FormlessRealmAsCondition
    vak:admits 3 ;
    vak:admitsCondition vak:DharmaCondition .

vak:FirstTwoDhyanas
    vak:hasRealmOfBelonging vak:FormRealm ;
    vak:hasMentalRangingCount 12 ;
    vak:excludesAffectiveMode vak:Distress ;
    vak:mayHaveRealmAsCondition vak:DesireRealm .

organon:SituatedLearningOperation
    a organon:ProjectInterpretation ;
    organon:hasCoordinate organon:RealmOfBelonging,
        organon:RealmAsCondition ;
    organon:constrainedBy organon:TargetFieldSchema ;
    organon:preserves organon:OperationProvenance,
        organon:ContentProvenance .
```
