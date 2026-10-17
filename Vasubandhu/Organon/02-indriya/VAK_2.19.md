# VAK_2.19 — Realization and What It Entails

## 1. Sanskrit (Devanāgarī)

> अष्टाभिरेकादशभिस्त्वाज्ञाज्ञातेन्द्रियान्वितः ।
>
> आज्ञास्यामीन्द्रियोपेतस्त्रयोदशभिरन्वितः ॥ २.१९ ॥

## 2. Sanskrit (IAST)

> aṣṭābhir ekādaśabhis tv ājñājñātendriyānvitaḥ /
>
> ājñāsyāmīndriyopetas trayodaśabhir anvitaḥ // 2.19 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| aṣṭābhiḥ | instrumental | with eight; the prior close |
| ekādaśabhiḥ | instrumental | with eleven |
| ājñā-indriya | compound | knowledge-faculty |
| ājñāta-indriya | compound | one who has known; ājñātāvīndriya |
| anvitaḥ | nominative | accompanied by |
| ājñāsyāmi-indriya | compound | I shall know |
| upetaḥ | nominative | furnished with |
| trayodaśabhiḥ | instrumental | with thirteen |

The gloss at 51.17 is difficult. Ājñātendriya is read as one who has known. The two cases stay apart by the prose that follows.

## 4. Grammar

```text
% start S
S[POSSESS=11] -> Knowledge | HasKnown
S[POSSESS=13] -> ShallKnow[PATH=uninterrupted]
```

Thirteen unifies only on the uninterrupted path.

## 5. Translation

### Literal Translation

With eight. But one accompanied by the knowledge-faculty or the faculty of one who has known, with eleven. One furnished with the faculty “I shall know” is accompanied by thirteen.

### Bhāṣya-informed study translation

> The knowledge-faculty and the faculty of one who has known each require eleven. “I shall know” requires thirteen. The difference is not further realization. It is the presence of body and the fourth feeling on the uninterrupted path.

## 6. Philosophical Translation

> Thirteen is the uninterrupted path. Eleven is the path of liberation and beyond. The count follows the path, not a higher grade.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| ājñendriya | knowledge-faculty | eleven |
| ājñātāvīndriya | one who has known | eleven; another set |
| ājñāsyāmīndriya | I shall know | thirteen |
| śraddhādi | the five | all five, not faith alone |
| tair eva daśabhiḥ | those same ten | carries the common members |
| samanvāgata | possessing | not one path-moment |

## 8. Logical Determination

```text
common ten
    = pleasure, gladness, neutral feeling,
      life, mind, five beginning with faith

knowledge-faculty
    = ten + itself
    = 11

one who has known
    = ten + itself
    = 11
    ≠ both realization-faculties together

I shall know
    = mind, life, body,
      four feelings,
      five,
      itself
    = 13

four feelings
    = pain, pleasure, gladness, neutral feeling
    distress not in the set

same count
    ↛ same set
larger count
    ↛ more realization
omitted
    ↛ cannot be possessed
```

## 9. Interpretive Note

The eight stands in 2.18. Pratyekam still holds: female, male, distress, and each of the five are separate eights.

The damaged gloss is kept. The contrast is carried by ājñendriyeṇa and ājñātāvīndriyeṇa. The resolution is marked, not a silent repair.

Pain in the thirteen is not a constituent of the seeing-path moment. The predicate is possession. Why body and pain are necessary here and absent from the common ten is not explained. No cause is inserted.

Organon reading: the named faculty, its path-role, and the exact list. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_19
    a vak:Karika ;
    rdfs:label "VAK 2.19" ;
    vak:hasTopic vak:RealizationClosure ;
    vak:belongsTo vak:Indriyanirdesa .

vak:KnowledgeFaculty vak:closesOn 11 .
vak:OneWhoHasKnown vak:closesOn 11 .
vak:IShallKnow vak:closesOn 13 .

organon:LargerCountNotMore
    organon:notTheVerseEnglish true .
```
