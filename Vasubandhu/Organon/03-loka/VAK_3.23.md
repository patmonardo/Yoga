# VAK_3.23 — From Feeling to Appropriation

## 1. Sanskrit (Devanāgarī)

> वित्तिः प्राक् मैथुनात् तृष्णा भोगमैथुनरागिणः ।
>
> उपादानं तु भोगानां प्राप्तये परिधावतः ॥ ३.२३ ॥

## 2. Sanskrit (IAST)

> vittiḥ prāk maithunāt tṛṣṇā bhogamaithunarāgiṇaḥ /
>
> upādānaṃ tu bhogānāṃ prāptaye paridhāvataḥ // 3.23 //

The Bhāṣya identifies *vittiḥ* as the stage of Feeling.

## 3. Lexical Analysis

```text
vittiḥ                  → vittiḥ
prāk                    → prāk
maithunāt               → maithunāt
tṛṣṇā                   → tṛṣṇā
bhoga-maithuna-rāgiṇaḥ  → bhogamaithunarāgiṇaḥ
upādānam                → upādānam
tu                      → tu
bhogānām                → bhogānām
prāptaye                → prāptaye
paridhāvataḥ            → paridhāvataḥ
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| vittiḥ | nominative feminine singular | Feeling; the Bhāṣya identifies it as the Feeling-stage |
| prāk | indeclinable governing the ablative | before; marks the limit of the Feeling-stage |
| maithunāt | ablative singular | before sexual coupling; the Bhāṣya specifies active sexual passion |
| tṛṣṇā | nominative feminine singular | Craving; the stage of active passion |
| bhoga-maithuna-rāgiṇaḥ | genitive masculine singular compound | of one passionately attached to sensual enjoyment and sexual coupling |
| upādānam | nominative neuter singular | Appropriation; the stage of acquisition-oriented search |
| tu | transitional or adversative particle | marks the transition to the pursuit-stage |
| bhogānām | genitive masculine plural | of enjoyments |
| prāptaye | dative singular of purpose | for attaining |
| paridhāvataḥ | genitive masculine singular present participle | of one running about in pursuit |

## 4. Grammar

The verse gives three successive designations:

```text
vittiḥ [avasthā]
    prāk maithunāt

tṛṣṇā [avasthā]
    bhoga-maithuna-rāgiṇaḥ

upādānam tu [avasthā]
    bhogānāṃ prāptaye paridhāvataḥ
```

> The Feeling-stage extends before sexual passion becomes active. Craving is
> the state of one passionately attached to sensual enjoyment and sexual
> coupling. Appropriation is the state of one running about to attain
> enjoyments.

The Bhāṣya carries forward the capacity to discriminate the causes of the
three Feelings from VAK 3.22. It defines the boundary at *maithunāt* through
the active manifestation of sexual passion, not simply the occurrence of
physical coupling.

## 5. Translation

### Close syntactic rendering

> Feeling is before sexual coupling; Craving is the state of one passionately
> attached to sensual enjoyment and sexual coupling. Appropriation, however,
> is the state of one running about to attain enjoyments.

### Bhāṣya-informed study translation

> Once the capacity to discriminate the causes of the three Feelings has
> arisen, the Feeling-stage continues while sexual passion remains
> unmanifest. Active passion for sensual enjoyments and sexual coupling is
> called Craving, until seeking that Condition begins. The stage of one who
> has entered the search and runs in all directions to attain the Condition
> is called Appropriation.

## 6. Scope Note

The Bhāṣya marks three distinct operations: Feeling before active passion,
Craving while passion is manifest but search has not begun, and Appropriation
once search is organized around attaining the Condition. This is a
functional-stage analysis, not a universal age timetable.

Here *viṣaya* is rendered **Condition**, a specific moment of the Seen and
the playground of the Faculties. Do not substitute Object—the comprehended
truth of Vastu—for this source term.

## 7. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .

vak:VAK_3_23
    a vak:Karika ;
    vak:continues vak:VAK_3_22 ;
    vak:definesStage vak:FeelingStage, vak:CravingStage,
        vak:AppropriationStage .

vak:FeelingStage
    a vak:TemporalStage ;
    vak:hasDesignation vak:Vitti ;
    vak:endsAt vak:ActiveManifestationOfPassion .

vak:CravingStage
    a vak:TemporalStage ;
    vak:hasDesignation vak:Trsna ;
    vak:orientsToward vak:SensualEnjoyment ;
    vak:endsAt vak:SearchForCondition .

vak:AppropriationStage
    a vak:TemporalStage ;
    vak:hasDesignation vak:Upadana ;
    vak:hasOperation vak:SearchForCondition ;
    vak:hasEnd vak:AttainmentOfEnjoyment ;
    organon:extendsInAllDirections true .

vak:FeelingStage
    vak:requires vak:CauseDiscriminationCapacity .
```
