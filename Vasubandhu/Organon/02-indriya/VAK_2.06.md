# VAK_2.06 — Engagement and Withdrawal

## 1. Sanskrit (Devanāgarī)

> प्रवृत्तेराश्रयोत्पत्तिस्थितिप्रत्युपभोगतः ।
>
> चतुर्दश तथान्यानि निवृत्तेरिन्द्रियाणि वा ॥ २.६ ॥

## 2. Sanskrit (IAST)

> pravṛtter āśrayotpattisthitipratyupabhogataḥ /
>
> caturdaśa tathānyāni nivṛtter indriyāṇi vā // 2.6 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| pravṛtteḥ | genitive | of engagement |
| āśraya-utpatti-sthiti-pratyupabhogataḥ | adverbial compound | as to support, arising, persistence, experience |
| caturdaśa | nominative | fourteen |
| tathā | indeclinable | likewise |
| anyāni | nominative | the others |
| nivṛtteḥ | genitive | of withdrawal |
| indriyāṇi | nominative | faculties |
| vā | particle | or; a difference of opinion |

Pravṛtti qualifies each of the four. Tathā carries the same four to nivṛtti.

## 4. Grammar

Vā is matavikalpa. Others say:

```text
engagement
    support      the six
    arising      female and male
    persistence  life
    experience   the five feelings
    fourteen

withdrawal, likewise
    support      the five beginning with faith
    arising      I shall know
    persistence  the knowledge-faculty
    experience   one who has known
    eight
```

The same prose then refuses speech, hand, foot, anus, and genital organ. That refusal belongs to this unit.

## 5. Translation

### Literal Translation

Or, as to support, arising, persistence, and experience of engagement, fourteen; likewise the others are faculties of withdrawal.

### Bhāṣya-informed study translation

Or marks a difference of opinion. Others say: the six are the support of engagement. Female and male are its arising, because it arises from them. Life is its persistence, because it continues by that. Experience is by the feelings. These are the fourteen.

In the same manner, the others concern withdrawal. Those beginning with faith are its supports. The faculty called “I shall know” is its arising. The knowledge-faculty is its persistence. Experience is by the faculty of one who has known. For this reason there are just this many, and this is their order.

Speech is not a faculty of speaking, because speaking depends on particular training. Hand and foot are not faculties, because they are not different from taking hold and moving about, and because snakes and the like do both without them. The anus is not a faculty of excretion: heavy matter falls where there is space, and wind propels it. The genital organ is not a faculty of pleasure: that pleasure is produced by the female and male faculties. Otherwise throat, teeth, eyelids, and joints would be faculties of swallowing, chewing, opening and closing, contracting and extending — or every cause would be a faculty of its own act. Speech and the rest are not reasonably faculties.

## 6. Philosophical Translation

The same twenty-two, another order. Fourteen govern engagement: support, arising, persistence, experience. Eight govern withdrawal in those same four places. Withdrawal is not bare absence. It has a support, an arising, a persistence, and an experience. The alternative does not replace 2.05. Vā keeps them apart.

Organon rendering:

The array we subject ourselves to. Engagement is one course of the rules. Withdrawal is the other, same four places, other members. The principles still discriminate membership: speech and the acts stay outside. Adaptation is to this array, not to every cause. Not the verse English.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| pravṛtti | engagement | the fourteen; not “the world” |
| nivṛtti | withdrawal | the eight; not bare inactivity |
| āśraya | support | six; or the five beginning with faith |
| utpatti / prabhava | arising | female and male; or I shall know |
| sthiti | persistence | life; or the knowledge-faculty |
| pratyupabhoga / upabhoga | experience | the feelings; or one who has known |
| vā / matavikalpa | or | difference of opinion |
| śikṣā-viśeṣa | particular training | why speech is refused |

## 8. Logical Determination

```text
engagement
    = support 6 + arising 2 + persistence 1 + experience 5

withdrawal
    = support 5 + arising 1 + persistence 1 + experience 1

both
    = the twenty-two
    ∩ empty

withdrawal
    ≠ absence of engagement

2.05
    = six functions, the membership
2.06
    = four places, two courses, an alternative

speech, hand, foot, anus, genital organ
    ↛ faculties
```

## 9. Interpretive Note

Tathā is the point. Withdrawal has the same four places as engagement. The members differ. Feeling-experience is not the experience of one who has known. They occupy the corresponding place.

The order is explained by the functions, not only received. Arising from female and male is not a full account of generation. Life is continued standing. The five support withdrawal. The three split into arising, persistence, and experience, as 2.04 had already distinguished them.

Speech depends on training. That does not mean no cultivated faculty counts: the eight are in this same unit. Hand and foot are not different from the act, and the act occurs without them. Excretion is heavy matter and wind. Pleasure of the genital organ is already assigned to female and male. The last step is the threat: every cause would be a faculty of its own act.

Organon reading: the array is what we subject ourselves to. The principles remain the membership discriminator. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_06
    a vak:Karika ;
    rdfs:label "VAK 2.06" ;
    vak:hasTopic vak:EngagementAndWithdrawal ;
    vak:belongsTo vak:Indriyanirdesa ;
    vak:reportsPosition vak:AlternativeOpinion .

vak:Engagement vak:hasCount 14 ;
    vak:hasSupport vak:SixFaculties ;
    vak:hasArising vak:FemaleMaleFaculties ;
    vak:hasPersistence vak:LifeFaculty ;
    vak:hasExperience vak:FeelingFive .
vak:Withdrawal vak:hasCount 8 ;
    vak:hasSupport vak:FiveBeginningWithFaith ;
    vak:hasArising vak:IShallKnow ;
    vak:hasPersistence vak:KnowledgeFaculty ;
    vak:hasExperience vak:OneWhoHasKnown .

organon:IndriyaArray
    organon:subjectedTo true ;
    organon:notTheVerseEnglish true .
```
