# VAK_3.21 — From Former State to Junction

## 1. Sanskrit (Devanāgarī)

> पूर्वक्लेशा दशाविद्या संस्काराः पूर्वकर्मणः ।
>
> संधिस्कन्धास्तु विज्ञानं नामरूपमतः परम् ॥ ३.२१ ॥

## 2. Sanskrit (IAST)

> pūrvakleśā daśāvidyā saṃskārāḥ pūrvakarmaṇaḥ /
>
> saṃdhiskandhās tu vijñānaṃ nāmarūpam ataḥ param // 3.21 //

## 3. Lexical Analysis

```text
pūrvakleśā daśāvidyā  → pūrvakleśā + daśā + avidyā
saṃskārāḥ              → saṃskārāḥ
pūrva-karmaṇaḥ         → pūrvakarmaṇaḥ
saṃdhi-skandhāḥ        → saṃdhiskandhāḥ
tu                     → tu
vijñānam               → vijñānam
nāma-rūpam             → nāmarūpam
ataḥ param             → ataḥ param
```

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

### Close syntactic rendering

> The state of former afflictions is Ignorance; Formations are the state of
> former Karma. But the junction Bases are Discriminative Cognition; after
> this comes Name-and-Form.

### Bhāṣya-informed study translation

> The state of afflictions in the prior birth is called Ignorance, because
> the other afflictions accompany it and operate under its influence. The
> former birth's meritorious and other karmic state, whose result matures
> here, is called Formations. At the moment of rebirth-linking in the
> mother's womb, the five Bases together are designated Discriminative
> Cognition. Name-and-Form follows that junction; the next verse specifies
> the boundary of this stage.

## 6. Scope Note

The Bhāṣya establishes the “state” reading, the association of other
afflictions with Ignorance, the maturation of former Karma, and the five-Base
character of the junction designated Discriminative Cognition. The endpoint
of Name-and-Form belongs to VAK 3.22.

Here *vijñāna* is rendered Discriminative Cognition, not consciousness
(*citta*) or Mind (*manas*).

## 7. OWL++ Seed

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
