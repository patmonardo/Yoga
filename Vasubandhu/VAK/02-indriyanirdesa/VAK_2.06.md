# VAK_2.06 — Faculties of Engagement and Withdrawal

## 1. Sanskrit — Devanāgarī

```text
प्रवृत्तेराश्रयोत्पत्तिस्थितिप्रत्युपभोगतः ।
चतुर्दश तथान्यानि निवृत्तेरिन्द्रियाणि वा ॥ VAkK_2.6 ॥
```

## 2. Sanskrit — IAST

```text
pravṛtter āśrayotpattisthitipratyupabhogataḥ /
caturdaśa tathānyāni nivṛtter indriyāṇi vā // VAkK_2.6 //
```

Source form:

```text
pravṛtterāśrayotpattisthitipratyupabhogataḥ /
caturdaśa tathānyāni nivṛtterindriyāṇi vā // VAkK_2.6 //
```

## 3. Padaccheda

| Text | Padaccheda | Basic Sense |
|---|---|---|
| pravṛtteḥ | pravṛtteḥ | of engagement / forward activity |
| āśraya | āśraya | support / basis |
| utpatti | utpatti | arising / production |
| sthiti | sthiti | persistence / stability |
| pratyupabhogataḥ | praty-upabhogataḥ | because of corresponding experience / enjoyment |
| caturdaśa | caturdaśa | fourteen |
| tathā | tathā | likewise / in that way |
| anyāni | anyāni | the others |
| nivṛtteḥ | nivṛtteḥ | of withdrawal / cessation / turning back |
| indriyāṇi | indriyāṇi | faculties |
| vā | vā | alternatively / or |

## 4. Grammar

```text
pravṛtteḥ
    genitive singular
    “of pravṛtti,” of engagement or forward activity

āśraya-utpatti-sthiti-pratyupabhogataḥ
    ablative singular compound
    “because of support, arising, persistence, and corresponding experience”

caturdaśa
    numeral
    “fourteen”

anyāni
    nominative / accusative plural neuter
    “the others”

nivṛtteḥ
    genitive singular
    “of nivṛtti,” of withdrawal or cessation

indriyāṇi
    nominative / accusative plural neuter
    “faculties”
```

## 5. Literal Translation

```text
Or, because of the support, arising, persistence, and corresponding experience
of engagement, fourteen are faculties; likewise the others are faculties of withdrawal.
```

## 6. Philosophical Translation

```text
The faculties may also be divided according to the two movements of conditioned life:
fourteen faculties serve the forward engagement of the series by supporting,
producing, sustaining, and enabling experience; the remaining faculties serve withdrawal,
cessation, and release.
```

## 7. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| pravṛtti | engagement / forward activity | The outward or ongoing movement of conditioned existence |
| nivṛtti | withdrawal / cessation / turning back | The movement toward release and cessation |
| āśraya | support / basis | That on which the process depends |
| utpatti | arising / production | The coming-to-be of the process |
| sthiti | persistence / stability | Maintenance of the process |
| pratyupabhoga | corresponding experience / enjoyment | Experiential appropriation of the process |
| caturdaśa | fourteen | The fourteen faculties oriented to pravṛtti |
| anyāni | the others | The remaining faculties oriented to nivṛtti |
| indriya | faculty / governing efficacy | Sāttvic-rational governing power |

## 8. Classification Note

VAK_2.06 offers an alternative functional division of the twenty-two faculties.

```text
pravṛtti-oriented faculties
    = fourteen

nivṛtti-oriented faculties
    = the remaining eight
```

The verse does not merely count. It introduces a new axis:

```text
pravṛtti
    = engagement, continuation, forward movement of the series

nivṛtti
    = withdrawal, cessation, return, release
```

The fourteen are connected with:

```text
āśraya
    support

utpatti
    arising

sthiti
    persistence

pratyupabhoga
    corresponding experience / enjoyment
```

The remaining faculties are read as serving the movement of withdrawal and release.

## 9. Logical Determination

VAK_2.05 gave the **functional extent** of the faculties. VAK_2.06 now gives their **directional polarity**.

```text
pravṛtti
    =
the series as engaged, arising, sustained, and experienced

nivṛtti
    =
the series as turning back, ceasing, and being released
```

The indriyas therefore govern not only isolated functions, but the two great movements of conditioned experience:

```text
engagement
    -> pravṛtti

withdrawal
    -> nivṛtti
```

This is the first explicit transition from the static enumeration of faculties to their dynamic soteriological orientation.

## 10. Transcendental Placement

The verse is a Logic of Experience distinction.

```text
pravṛtti
    =
the forward deployment of experience

nivṛtti
    =
the reversal or cessation of that deployment
```

The fourteen pravṛtti-faculties make conditioned experience possible as support, arising, persistence, and enjoyment.

The remaining faculties make release possible as withdrawal, cessation, and realization.

Thus:

```text
indriya
    =
governing efficacy either for engagement or for withdrawal
```

This is not a crude opposition between world and salvation. It is the lawful polarity of the same field of experience.

## 11. Organon Interpretation

VAK_2.06 introduces the major polarity of the Indriya chapter:

```text
pravṛtti
    =
forward execution of the experience-system

nivṛtti
    =
release / shutdown / reversal of the experience-system
```

Organon reading:

```text
pravṛtti-indriyas
    =
drivers of support, arising, persistence, and experiential appropriation

nivṛtti-indriyas
    =
drivers of withdrawal, purification, and realization
```

This belongs directly to the Logic of Experience:

```text
Experience is generated.
Experience is sustained.
Experience is enjoyed.
Experience is reversed.
Experience is released.
```

## 12. Compact Formula

```text
VAK_2.06 divides the faculties according to direction:
fourteen serve pravṛtti, the forward activity of conditioned experience;
the others serve nivṛtti, the movement of withdrawal and release.
```

## 13. OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_06 a vak:Karika ;
    rdfs:label "VAK 2.06" ;
    vak:sourceVerse "VAkK_2.6" ;
    vak:chapter vak:Indriyanirdesa ;
    vak:hasTopic vak:PravrttiIndriyas, vak:NivrttiIndriyas ;
    vak:hasKeyTerm vak:Pravrtti, vak:Nivrtti, vak:Asraya, vak:Utpatti, vak:Sthiti, vak:Pratyupabhoga ;
    vak:hasLiteralTranslation
        "Or, because of the support, arising, persistence, and corresponding experience of engagement, fourteen are faculties; likewise the others are faculties of withdrawal." ;
    vak:hasPhilosophicalTranslation
        "The faculties may also be divided according to the two movements of conditioned life: fourteen faculties serve the forward engagement of the series by supporting, producing, sustaining, and enabling experience; the remaining faculties serve withdrawal, cessation, and release." .

vak:Pravrtti a logic:Determination ;
    rdfs:label "pravṛtti" ;
    vak:canonicalTranslation "engagement / forward activity" ;
    organon:logicalFunction "Forward deployment of conditioned experience." .

vak:Nivrtti a logic:Determination ;
    rdfs:label "nivṛtti" ;
    vak:canonicalTranslation "withdrawal / cessation / turning back" ;
    organon:logicalFunction "Reversal and release of conditioned experience." .

vak:PravrttiIndriyas a logic:DeterminationGroup ;
    rdfs:label "pravṛtti-oriented faculties" ;
    vak:count "14" ;
    organon:logicalFunction "Faculties governing support, arising, persistence, and experience." .

vak:NivrttiIndriyas a logic:DeterminationGroup ;
    rdfs:label "nivṛtti-oriented faculties" ;
    organon:logicalFunction "Faculties governing withdrawal, cessation, and release." .
```

## 14. Commit History

```text
VAK_2.06 opened.
Chapter: Indriyanirdeśa.
Method: kārikā-first.
Key continuation from VAK_2.05: the faculties are justified by functional extent.
New axis introduced: pravṛtti and nivṛtti.
Fourteen faculties interpreted as serving engagement / forward activity.
Remaining faculties interpreted as serving withdrawal / cessation / release.
Organon note added: experience-system as generated, sustained, enjoyed, reversed, and released.
Zero-padded file naming maintained: VAK_2.06.
```
