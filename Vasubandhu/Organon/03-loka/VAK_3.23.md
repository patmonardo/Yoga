# VAK_3.23 — From Feeling to Appropriation

## 1. Sanskrit (Devanāgarī)

```sanskrit
वित्तिः प्राक् मैथुनात् तृष्णा भोगमैथुनरागिणः ।
उपादानं तु भोगानां प्राप्तये परिधावतः ॥ ३.२३ ॥
```

## 2. Sanskrit (IAST)

```text
vittiḥ prāk maithunāt tṛṣṇā bhogamaithunarāgiṇaḥ /
upādānaṃ tu bhogānāṃ prāptaye paridhāvataḥ // 3.23 //
```

The Bhāṣya identifies *vittiḥ* as the stage of Feeling.

## 3. Lexical Analysis

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

The Bhāṣya carries forward the capacity to know the causes of the
three Feelings from VAK 3.22. It defines the boundary at *maithunāt* through
the active manifestation of sexual passion, not simply the occurrence of
physical coupling.

## 5. Translation

### Literal Translation
> The Feeling-stage is before sexual passion becomes active. Craving is the
> state of one passionately attached to sensual enjoyment and sexual
> coupling. Appropriation is the state of one running about to attain
> enjoyments.

### Bhāṣya-informed study translation

> The Feeling-stage precedes sexual coupling. Craving is the state of one
> passionate about sensual enjoyment and sexual coupling; Appropriation is
> the state of one who runs about to obtain enjoyments.

## 6. Philosophical Translation

> Feeling names the stage before active sexual passion. Craving names the
> state in which passion for sensual enjoyment and sexual coupling is
> manifest. Appropriation names the state in which one enters a search and
> ranges about to attain the sought Condition.

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this passage |
|---|---|---|
| `vitti` | Feeling | the stage before active sexual passion |
| `maithuna` | sexual coupling | the boundary named in the verse; the Bhāṣya explains it through active passion |
| `tṛṣṇā` | Craving | active passion for sensual enjoyment and sexual coupling, before search begins |
| `bhoga` | enjoyment | what the Craving-stage desires and the pursuit seeks |
| `viṣaya` | Condition | the object of pursuit in the Bhāṣya's explanation |
| `upādāna` | Appropriation | the stage in which organized search for attainment begins |
| `paridhāvati` | runs about / ranges in pursuit | the Bhāṣya's description of seeking the Condition in all directions |

## 8. Logical Determination

```text
capacity to know causes of the three Feelings
    → Feeling-stage, before passion manifests
    → Craving, when passion manifests
    → Appropriation, when the search for the Condition begins
    → pursuit ranges in all directions toward attainment
```

The distinctions are functional, not a universal age timetable or a mere
scale of increasing intensity. Appropriation begins with organized pursuit;
Craving supplies its motivational direction.

## 9. Interpretive Note

**Translation note.** The verse names the stages; the Bhāṣya specifies active passion and the
transition into search. The sought *viṣaya* is **Condition**, not Object,
the comprehended truth of Vastu.

## 10. OWL++ Seed

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
    vak:requires vak:CauseKnowledgeCapacity .
```
