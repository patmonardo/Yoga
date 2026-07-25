# VAK_4.114

## 1. Sanskrit — Devanāgarī

स्वपरार्थोभयार्थाय नोभयार्थाय दीयते ।
तद्विशेषः पुनर्दातृवस्तुक्षेत्रविशेषतः ॥ ४.११४ ॥

## 2. Sanskrit — IAST

svaparārthobhayārthāya nobhayārthāya dīyate |
tadviśeṣaḥ punar dātṛvastukṣetraviśeṣataḥ || 4.114 ||

## 3. Padaccheda

sva-artha-āya |
para-artha-āya |
ubhaya-artha-āya |
na-ubhaya-artha-āya |
dīyate |

tat-viśeṣaḥ |
punaḥ |
dātṛ-viśeṣataḥ |
vastu-viśeṣataḥ |
kṣetra-viśeṣataḥ

Prose order:

svārthāya, parārthāya, ubhayārthāya,
nobhayārthāya ca dīyate.

tasya dānasya viśeṣaḥ punaḥ
dātṛ-viśeṣataḥ,
vastu-viśeṣataḥ,
kṣetra-viśeṣataś ca.

> Giving is performed for one’s own benefit, for another’s benefit, for the benefit of both, or for the benefit of neither. Its particular quality is further determined by the distinction of the giver, the object given, and the recipient-field.

## 4. Grammar

- `svārthāya`: for one’s own benefit.
- `parārthāya`: for another’s benefit.
- `ubhayārthāya`: for the benefit of both.
- `nobhayārthāya`: for the benefit of neither.
- `dīyate`: it is given.
- `tadviśeṣaḥ`: the distinction or excellence of that giving.
- `dātṛ`: giver.
- `vastu`: object or thing given.
- `kṣetra`: recipient-field.
- `viśeṣataḥ`: owing to the distinction of.

## 5. Literal translation

> Something is given for one’s own benefit, for another’s benefit, for the benefit of both, or for the benefit of neither. Its distinction, moreover, arises from the distinction of the giver, the object, and the field.

## 6. Philosophical translation

> Giving may be oriented toward the giver’s welfare, the recipient’s welfare, the welfare of both, or—in certain deficient cases—toward neither. Beyond this difference of purpose, the karmic magnitude and quality of giving are determined by three concrete factors: the ethical and spiritual character of the giver, the quality of what is given, and the excellence or need represented by the recipient-field.

## 7. Four purposes of giving

The first half gives four possibilities:

- `svārtha`: one’s own benefit;
- `parārtha`: another’s benefit;
- `ubhayārtha`: benefit of both;
- `nobhayārtha`: benefit of neither.

The same external transfer can therefore occupy different karmic structures depending on whom it genuinely benefits.

## 8. Self, other, both, neither

Giving for one’s own benefit may seek merit, favorable rebirth, wealth, reputation, or future enjoyment. Giving for another’s benefit makes the recipient’s actual good the determining end. Giving for both can materially benefit the recipient while ethically and karmically transforming the giver. An apparent gift may benefit neither when it supports harm, lacks genuine relinquishment, or fails to realize a wholesome purpose.

The exact examples and the relative roles of intention and effective result should be recovered in the Bhāṣya pass.

## 9. Three determinants of excellence

The second half identifies:

- giver;
- gift-object;
- recipient-field.

Karmic quality is therefore relational. The same material object can have different karmic significance depending on the giver’s faith and purity, the suitability and legitimacy of the gift, and the qualities or need of the recipient-field.

## 10. Giver

The giver is the subjective pole of relinquishment. Relevant determinations include faith, ethical discipline, purity of intention, detachment, respect, understanding, and spiritual attainment.

## 11. Gift-object

The object matters according to whether it is useful, pure, lawfully obtained, timely, suitable, and genuinely beneficial. Giving is not evaluated by quantity alone.

## 12. Recipient-field

The recipient is a `kṣetra`, a field in which the deed is planted and from which its result develops. Parents, teachers, the needy, the sick, the Saṃgha, trainees, arhats, and Buddhas constitute distinct fields through benefit, need, attainment, or qualities.

## 13. Giving as a complete relation

Giving requires:

- giver: agency of relinquishment;
- gift: mediating object;
- field: completed direction of transfer.

Thus:

`GivingEvent = Giver + GiftObject + RecipientField`

The karmic truth of the event is the integrated determination of the whole relation.

## 14. Relation to VAK_4.113

VAK_4.113 defined the general form of giving as recipient-oriented intention becoming effective through bodily or verbal transfer. VAK_4.114 now differentiates giving by benefit-scope and by the quality of giver, object, and field.

## 15. Doctrinal determination

The verse establishes:

1. giving may benefit self, other, both, or neither;
2. the excellence of giving depends on giver, object, and recipient-field;
3. karmic value cannot be reduced to intention alone;
4. karmic value cannot be reduced to material quantity alone;
5. giving is a complete practical relation.

## 16. Logical determination

`BenefitScope(GivingEvent) ∈ {Self, Other, Both, Neither}`

`GivingQuality(event) = f(GiverQuality, GiftObjectQuality, RecipientFieldQuality)`

## 17. Organon interpretation

The giver’s purpose becomes actual only through a determinate object and a determinate recipient-field. The gift-object is the middle through which subjective intention becomes objective benefit. If the object is unsuitable, the purpose fails; if the field is misapprehended, the relation is distorted; if the giver is corrupt, the activity is internally compromised.

Giving is therefore a practical syllogism:

`giver → gift-object → recipient-field`

Its truth lies in realized benefit through the complete relation.

## 18. OWL++ seed

```ttl
vak:VAK_4_114 a vak:Karika ;
    rdfs:label "VAK 4.114" ;
    vak:continues vak:VAK_4_113 ;
    vak:hasTopic vak:GivingBenefitScope,
                 vak:GivingQualityDeterminants .

vak:GivingEvent
    vak:hasBenefitScope vak:SelfBenefit,
                        vak:OtherBenefit,
                        vak:MutualBenefit,
                        vak:NoBenefit ;
    vak:hasGiver vak:Giver ;
    vak:hasGiftObject vak:GiftObject ;
    vak:hasRecipientField vak:RecipientField .

vak:GivingQuality
    vak:determinedBy vak:GiverQuality,
                     vak:GiftObjectQuality,
                     vak:RecipientFieldQuality .

vak:RecipientField
    rdfs:subClassOf vak:KarmicField .
```

## 19. Commit note

VAK_4.114 — classify giving by benefit and relational quality

- distinguish giving for self, other, both, or neither;
- preserve the difference between intended and effective benefit for Bhāṣya analysis;
- identify giver, gift-object, and recipient-field as the three determinants of giving’s excellence;
- reject reductions of giving to intention or material quantity alone;
- model giving as a complete practical relation whose truth lies in realized benefit.
