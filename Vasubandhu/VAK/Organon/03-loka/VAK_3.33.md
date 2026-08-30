# VAK_3.33

## 1. Sanskrit (Devanāgarī)

> कामे स्वालम्बनाः सर्वे रूपी द्वादशगोचरः ।
>
> त्रयाणामुत्तरः ध्यानद्वये द्वादश कामगाः ॥ ३.३३ ॥

## 2. Sanskrit (IAST)

> kāme svālambanāḥ sarve rūpī dvādaśagocaraḥ /
>
> trayāṇām uttaraḥ dhyānadvaye dvādaśa kāmagāḥ // 3.33 //

## 3. Padaccheda and Lexical Analysis

```text
kāme                       → kāme
sva-ālambanāḥ              → svālambanāḥ
sarve                      → sarve
rūpī                       → rūpī
dvādaśa-gocaraḥ            → dvādaśagocaraḥ
trayāṇām                   → trayāṇām
uttaraḥ                    → uttaraḥ
dhyāna-dvaye               → dhyānadvaye
dvādaśa                    → dvādaśa
kāma-gāḥ                   → kāmagāḥ
```

| Form | Morphology | Lexical force here |
|---|---|---|
| kāme | locative singular of `kāma` | in the desire realm |
| svālambanāḥ | nominative masculine plural; `sva` + `ālambana` | having their own realm as object-support |
| sarve | nominative masculine plural | all, namely all eighteen mental rangings |
| rūpī | nominative masculine singular | the form realm, understood from the doctrinal context |
| dvādaśagocaraḥ | nominative masculine singular compound | field or range of twelve |
| trayāṇām | genitive plural numeral | of three mental rangings |
| uttaraḥ | nominative masculine singular | the higher realm, namely the formless realm |
| dhyānadvaye | locative singular compound | in the pair of meditations; the first and second dhyānas |
| dvādaśa | nominative masculine plural numeral | twelve mental rangings |
| kāmagāḥ | nominative masculine plural; `kāma` + `ga` | going toward desire; taking the desire realm as object-support |

The compact verse moves between two axes which the Bhāṣya explicitly
distinguishes: realm-membership (`pratisaṃyukta`) and object-support
(`ālambana`).

## 4. Grammar and Construe

The first three clauses concern the realms that may serve as object-supports:

```text
kāme sarve svālambanāḥ
    = in the desire realm, all [eighteen] have their own [realm]
      as object-support

rūpī dvādaśa-gocaraḥ
    = the form realm is the range of twelve

uttaraḥ trayāṇām [gocaraḥ]
    = the higher [formless realm] is the range of three
```

`Gocaraḥ` is carried forward into the third clause. The Bhāṣya resolves
`rūpī` as the form realm and `uttaraḥ` as the still higher, formless realm.

The final clause changes the question from possible object-range to the
rangings belonging to the form realm:

```text
dhyāna-dvaye dvādaśa
    = in the [first] two dhyānas there are twelve

[te] kāma-gāḥ
    = those [twelve] go toward the desire realm
```

The Bhāṣya glosses `kāmagāḥ` non-spatially: they take the desire realm as
their object-support.

## 5. Translation

### Close syntactic construe

> In the desire realm, all [eighteen] have their own [realm] as
> object-support. The form realm is the range of twelve; the higher realm is
> the range of three. In the pair of dhyānas there are twelve, and [those
> twelve] go toward the desire realm.

### Bhāṣya-informed study translation

> All eighteen mental rangings occur in the desire realm, and the desire realm
> can serve as the object-support of all eighteen. The form realm can serve as
> the range of twelve, because the six rangings concerned with odor and taste
> are excluded there. The higher, formless realm can serve as the range of
> only the three dharma-rangings, because sensory form and the other sensory
> fields are absent there. In the first two dhyānas, twelve mental rangings
> occur—the six rangings of distress being absent—and all twelve can take the
> desire realm as their object-support.

The identification of the omitted rangings, the reference of `rūpī` and
`uttaraḥ`, and the non-spatial interpretation of `kāmagāḥ` are Bhāṣya
determinations.

## 6. Philosophical Translation

> A mental ranging has both a station from which it operates and a field into
> which it ranges. These need not be the same. The desire realm supports the
> complete eighteenfold articulation; the form realm is available to twelve;
> and the formless realm to only three. Yet twelve rangings stationed in the
> first two form-realm meditations can reach back into the desire realm. The
> World System is therefore not a stack of sealed locations but a structured
> order of situated operations and permitted cross-domain reach.

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this unit |
|---|---|---|
| manopavicāra | mental ranging | feeling-governed mental traversal classified by affect and object-field |
| kāmadhātu | desire realm | realm in which all eighteen rangings occur and which all eighteen may take as support |
| rūpadhātu | form realm | object-range of twelve, excluding odor- and taste-rangings |
| ārūpyadhātu | formless realm | object-range of the three dharma-rangings alone |
| pratisaṃyukta | connected with / belonging to | identifies the realm to which a ranging belongs |
| ālambana | object-support | that upon which the ranging cognitively bears |
| svālambana | own object-support | one's own realm functioning as object-support |
| gocara | field / range | admissible domain of operation |
| gandha | odor | sensory field absent from the form realm |
| rasa | taste | sensory field absent from the form realm |
| dharmopavicāra | dharma-ranging | mental ranging whose object-field is dharma |
| dhyānadvaya | pair of dhyānas | first and second meditative levels of the form realm |
| daurmanasyopavicāra | distress-ranging | sixfold affective class absent from the first two dhyānas |
| kāmaga | desire-going / desire-directed | taking the desire realm as object-support |
| gami-prayoga | use of a verb of going | Bhāṣya's explanation of “going” as object-apprehension rather than locomotion |

Two determinations must not be collapsed:

```text
pratisaṃyukta
    = where the mental ranging belongs

ālambana / gocara
    = what field the mental ranging can take up
```

## 8. Logical Determination

### Realm-membership is not object-range

```text
MentalRanging {
    realmOfBelonging
    affectiveMode
    objectField
    objectRealm
}
```

Therefore:

```text
realmOfBelonging(x) = rūpadhātu

does not entail

objectRealm(x) = rūpadhātu
```

The twelve rangings of the first two dhyānas belong to the form realm but may
take the desire realm as their object-support.

### Admissible range follows the constitution of the field

| realm as object-support | admissible rangings | ground of restriction |
|---|---:|---|
| desire realm | 18 | all six object-fields are available |
| form realm | 12 | odor and taste are absent: `18 − (3 + 3)` |
| formless realm | 3 | only the dharma-field remains available |

This is an immanent restriction:

```text
field lacks object-kind y
    → no ranging-to-y has that field as object-support
```

The twelve belonging to the first two dhyānas are calculated on another axis:

```text
6 gladness-rangings
    + 6 equanimity-rangings
    = 12

6 distress-rangings excluded
```

### “Going” is cognitive directedness

```text
kāmān gacchanti
    ≠ spatial flight into the desire realm

kāmadhātum ālambante
    = they take the desire realm as object-support
```

The World System permits cross-domain cognitive range without confusing that
range with a change of station.

## 9. Interpretive Note

VAK 3.32 established Learning as feeling-conditioned repeated ranging. VAK
3.33 now gives that ranging an address space. Every Learning operation has at
least two coordinates:

```text
where the Agent is stationed
    ≠
what field the Agent ranges over
```

That distinction is indispensable. A form-realm operation may learn from the
desire realm without becoming a desire-realm operation. The determining state
and the determined field remain related but non-identical.

This also refines the Oculus Client SDK. The 3.32 record requires two further
fields:

```ts
interface SituatedMentalRanging extends MentalRanging {
  realmOfBelonging: Realm;
  objectRealm: Realm;
}
```

This is still an interpretive projection, not Vasubandhu's software model.
Its value is logical: it prevents the platform from confusing the location of
an operation with the provenance or domain of its content.

Nor are all cross-domain queries valid. The admissible range follows from the
constitution of the target field. The form realm cannot support odor- or
taste-rangings because it does not contain those fields; the formless realm
can support only dharma-rangings. A View cannot request a column the field
does not possess.

That is the deeper Learning principle here:

```text
Learning capacity
    = situated operation
      constrained by the schema of the field ranged over
```

The World is not an Earth-container populated by traveling mental Things. It
is the law that determines which operations can arise at a station and which
domains can become their object-support. `Kāmaga` is especially revealing:
“going” means cognitive reach. The architecture of the World System is an
architecture of possible directedness.

The verse therefore gives us a clean distinction between Agent state and
Dataset range. The same Agent-side state may ocularize content from a lower
domain while retaining its own station. Learning crosses a boundary without
erasing the provenance of either the learner or the learned field.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .

vak:VAK_3_33
    a vak:Karika ;
    vak:continues vak:VAK_3_32 ;
    vak:distinguishes vak:RealmOfBelonging, vak:ObjectRealm ;
    vak:distributes vak:EighteenMentalRangingsByRealm .

vak:DesireRealmAsObjectSupport
    vak:admits 18 ;
    vak:admitsAffectiveMode vak:Gladness, vak:Distress, vak:Equanimity ;
    vak:admitsObjectField vak:FormField, vak:SoundField,
        vak:SmellField, vak:TasteField, vak:TangibleField,
        vak:DharmaField .

vak:FormRealmAsObjectSupport
    vak:admits 12 ;
    vak:excludesObjectField vak:SmellField, vak:TasteField .

vak:FormlessRealmAsObjectSupport
    vak:admits 3 ;
    vak:admitsObjectField vak:DharmaField .

vak:FirstTwoDhyanas
    vak:hasRealmOfBelonging vak:FormRealm ;
    vak:hasMentalRangingCount 12 ;
    vak:excludesAffectiveMode vak:Distress ;
    vak:mayHaveObjectRealm vak:DesireRealm .

organon:SituatedLearningOperation
    a organon:ProjectInterpretation ;
    organon:hasCoordinate organon:RealmOfBelonging,
        organon:ObjectRealm ;
    organon:constrainedBy organon:TargetFieldSchema ;
    organon:preserves organon:OperationProvenance,
        organon:ContentProvenance .
```
