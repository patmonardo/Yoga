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

```text
% start S
S[COURSE=engagement] -> Fourteen[PLACE=?p]
S[COURSE=withdrawal] -> Eight[PLACE=?p]
PLACE -> support | arising | persistence | experience
```

Same four places, two courses. `COURSE` keeps them apart.

## 5. Translation

### Literal Translation

Or, as to support, arising, persistence, and experience of engagement, fourteen; likewise the others are faculties of withdrawal.

### Bhāṣya-informed study translation

> Or the same twenty-two under another order. Fourteen govern engagement through support, arising, persistence, and experience. Eight govern withdrawal in those same four places. Withdrawal is not bare absence; it has its own support, arising, persistence, and experience.

## 6. Philosophical Translation

> Engagement and withdrawal are two courses of the same rules. The alternative does not replace the first account.

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
