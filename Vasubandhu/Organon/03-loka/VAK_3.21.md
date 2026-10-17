# VAK_3.21 — Four State-Designations of the Continuum

## 1. Sanskrit (Devanāgarī)

```sanskrit
पूर्वक्लेशा दशाविद्या संस्काराः पूर्वकर्मणः ।
संधिस्कन्धास्तु विज्ञानं नामरूपमतः परम् ॥ ३.२१ ॥
```

## 2. Sanskrit (IAST)

```text
pūrvakleśā daśāvidyā saṃskārāḥ pūrvakarmaṇaḥ /
saṃdhiskandhās tu vijñānaṃ nāmarūpam ataḥ param // 3.21 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| pūrvakleśā daśā | phrase; exact division of the first pāda remains uncertain | the state of afflictions in the former birth |
| avidyā | nominative feminine singular | Ignorance, the designation of that former afflictive state |
| saṃskārāḥ | nominative masculine plural | Formations, the designation of the former karmic state |
| pūrva-karmaṇaḥ | genitive singular | of former Karma |
| saṃdhi-skandhāḥ | nominative masculine plural compound | the Bases at the rebirth-junction |
| tu | particle | marks the transition from prior states to the junction |
| vijñānam | nominative neuter singular | Discriminative Cognition, designating the five Bases together at the junction |
| nāma-rūpam | nominative neuter singular compound | Name-and-Form, the stage following the junction |
| ataḥ | ablative singular used adverbially | from this; after this |
| param | nominative neuter singular used adverbially | later; subsequently |

The Bhāṣya explicitly reads *daśā* as “state” and carries it into the
definition of Formations. It is not the numeral *daśa*, “ten.”

## 4. Grammar

The verse gives four stage-designations:

```text
pūrvakleśā daśā
    avidyā [ucyate]

pūrva-karmaṇaḥ [daśā]
    saṃskārāḥ [ucyante]

saṃdhi-skandhāḥ tu
    vijñānam [ucyante]

ataḥ param
    nāmarūpam [ucyate]
```

The repeated word “state” is explicit in the Bhāṣya, which explains both
Ignorance and Formations as designations of temporally situated states. The
third designation is collective: the five Bases at the junction are called
Discriminative Cognition. The final pāda places Name-and-Form after that
junction but does not state its endpoint.

## 5. Translation

### Literal Translation
> The state of former afflictions is Ignorance; Formations are the state of
> former Karma. The junction Bases, however, are Discriminative Cognition;
> thereafter comes Name-and-Form.

### Bhāṣya-informed study translation

> The state of former afflictions is Ignorance; Formations are the state of
> former Karma. At the junction, the five Bases are called Discriminative
> Cognition; thereafter comes Name-and-Form.

## 6. Philosophical Translation

> Ignorance designates the former state of affliction, and Formations the
> former state of Karma. At the rebirth-junction, the five Bases are
> designated Discriminative Cognition; Name-and-Form follows that junction.

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this passage |
|---|---|---|
| `daśā` | state | Bhāṣya-confirmed reading in the first pāda; not the numeral ten |
| `avidyā` | Ignorance | designation of the former afflictive state |
| `saṃskāra` | Formations | designation of the former karmic state whose result matures here |
| `saṃdhiskandha` | junction Base | the Base configuration at rebirth-linking |
| `vijñāna` | Discriminative Cognition | designation of the five Bases together at the junction |
| `nāmarūpa` | Name-and-Form | the stage following the rebirth-junction |

## 8. Logical Determination

```text
former afflictive state
    → Ignorance

former karmic state
    → Formations

five Bases at rebirth-junction
    → Discriminative Cognition

after the junction
    → Name-and-Form
    → its boundary is specified in VAK 3.22
```

The verse orders designations across former and present births. It does not
make Formations and the junctional Cognition simultaneous, nor posit a
substance that travels between them.

## 9. Interpretive Note

**Translation note.** The Bhāṣya confirms *daśā*, “state,” rather than *daśa*, “ten”; the precise
compound division remains editorial. Here *vijñāna* designates the junctional
five-Base configuration and remains distinct from consciousness (*citta*)
and Mind (*manas*).

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .

vak:VAK_3_21
    a vak:Karika ;
    vak:continues vak:VAK_3_20 ;
    vak:definesStage vak:FormerAfflictiveState,
        vak:FormerKarmicState, vak:RebirthJunction, vak:NameAndForm .

vak:StageDesignation
    a organon:ReflectiveDesignation ;
    organon:maps vak:TemporalState ;
    organon:by vak:PredominantDetermination .

vak:FormerAfflictiveState
    a vak:TemporalState ;
    vak:hasDesignation vak:Avidya .

vak:FormerKarmicState
    a vak:TemporalState ;
    vak:hasDesignation vak:Samskara ;
    vak:maturesAs vak:PresentResult .

vak:RebirthJunction
    a vak:TemporalState ;
    vak:hasBaseCount 5 ;
    vak:hasDesignation vak:Vijnana .

vak:NameAndForm
    a vak:TemporalState ;
    vak:follows vak:RebirthJunction ;
    vak:boundarySpecifiedIn vak:VAK_3_22 .
```
