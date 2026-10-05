# VAK_1.17 — Mind Is One of the Six, Just Ceased

## 1. Sanskrit (Devanāgarī)

> षण्णामनन्तरातीतं विज्ञानं यद्धि तन्मनः ।
>
> षष्ठाश्रयप्रसिद्ध्यर्थं धातवोऽष्टादश स्मृताः ॥ १.१७ ॥॥

## 2. Sanskrit (IAST)

> ṣaṇṇām anantarātītaṃ vijñānaṃ yad dhi tan manaḥ /
>
> ṣaṣṭhāśrayaprasiddhyarthaṃ dhātavo 'ṣṭādaśa smṛtāḥ // 1.17 //

## 3. Lexical Analysis

```text
ṣaṇṇām anantarātītam       → of the six, immediately past
yad dhi                    → whichever, indeed
tan manaḥ                  → that is mind
ṣaṣṭha-āśraya-prasiddhi-artham → in order to establish the sixth support
dhātavaḥ aṣṭādaśa         → eighteen principles
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| ṣaṇṇām | genitive plural | of the six |
| anantara-atītam | nominative neuter | immediately past; just ceased |
| vijñānam | nominative neuter | a principle, one of the six |
| yat / tat | nominative neuter | whichever, that |
| hi | particle | the reason |
| manaḥ | nominative neuter | mind |
| ṣaṣṭha-āśraya-prasiddhi-artham | accusative of purpose | so that the sixth support be established |
| dhātavaḥ | nominative plural | principles |
| aṣṭādaśa smṛtāḥ | numeral and participle | eighteen are taught |

The commentary tightens *anantarātīta* to *samanantara-niruddha*: ceased
immediately before, nothing between.

## 4. Grammar

```text
ṣaṇṇām vijñānam yat anantara-atītam
    = tat manaḥ

ṣaṣṭha-āśraya-prasiddhi-artham
    dhātavaḥ aṣṭādaśa smṛtāḥ
```

*Yat* and *tat* are the same neuter. The genitive draws the principle from the
six already named. The identity is relational. The verse does not add a
seventh principle. The purpose compound qualifies the second clause. It does
not say that the eighteen are eighteen substances.

## 5. Translation

### Literal Translation

Whichever principle among the six is immediately past, that indeed is mind.
The eighteen principles are taught in order to establish the sixth support.

### Bhāṣya-informed study translation

Mind is not a seventh principle beside the six. Whichever of those six has
just ceased is called mind, and called the mind-principle, in its office as
support. The five have supports of their own. The mind-group principle has no
further support of that kind. Eighteen are taught so that this sixth support
be established.

The support does not require a successor. An arhat's final consciousness
remains mind. Another cause is wanting, and no next principle arises.

## 6. Philosophical Translation

Again, two lines. The first answers 1.16. The second says why the count is
eighteen.

The seventh name is not a seventh thing. Whichever of the six has just ceased,
that is mind. Present, it is one of the six principles. Just ceased, it is the
support of the next. Same principle, two offices. The commentary's pictures
are exact: the same person is son to one and father to another; the same fruit
is seed to another.

The five have a support each. The sixth, the mind-group principle, has none of
that kind. Mind is taught so that the sixth support stand in the open. That is
why eighteen, and not a reduced substance-count.

Eighteen here is six supports, six supported, and six that are borne. Mind is
the sixth support. It is not a sixth eye.

The last test is quiet. If mind meant whatever produces the next, an arhat's
final consciousness would fail the name. It does not fail. The office remains.
The next does not arise, because another cause is wanting.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| vijñāna | principle | one of the six; not consciousness |
| manas | mind | the same principle, just ceased |
| manodhātu | mind-principle | the office, not a seventh substance |
| manovijñāna-dhātu | mind-group principle | the sixth of the six; the supported |
| anantarātīta | immediately past | ceased immediately before |
| āśraya | support | the office mind fills |
| āśrita | the supported | the six principles |
| ālambana | the borne | not the support |
| citta | consciousness | the arhat's final consciousness; not mind |
| dravyataḥ | by substance | the objection's count |
| prasiddhi | establishment | so that the sixth support be known |

## 8. Logical Determination

```text
1.16   seven names: six principles + mind-principle
       relation not yet said

1.17   of those six, whichever has just ceased
           → mind
           → mind-principle, as support

       present office     one of the six
       just-ceased office mind, the sixth support

       five supports      eye and the rest
       sixth support      mind
       supported          six principles
       borne              six
       6 + 6 + 6 = 18

       objection          17, or 12, by substance
       reply              eighteen, for the sixth support

       arhat's last consciousness
           remains mind
           no successor, another cause wanting
           support ≠ production

1.18 not opened
```

The objection's twelve is a substance-count. It is not the twelve essences.

## 9. Interpretive Note

The hinge is *yat ... tat*: whichever, that. Interpretation of the office, and
of the arhat's limit, is in the Bhāṣya.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_17 a vak:Karika ;
    vak:hasTopic vak:MindAsSixthSupport ;
    vak:belongsTo vak:Dhatunirdesa ;
    vak:answers vak:VAK_1_16 .

vak:Mind vak:isOneOf vak:SixPrinciples ;
    vak:when vak:ImmediatelyPast ;
    vak:functionsAs vak:SixthSupport ;
    vak:distinctFrom vak:SeventhSubstance .

vak:EighteenPrinciples vak:supports 6 ;
    vak:supported 6 ;
    vak:borne 6 .

vak:FinalArhatConsciousness vak:remains vak:Mind ;
    vak:hasSuccessor false ;
    vak:reason vak:AnotherCauseWanting .
```
