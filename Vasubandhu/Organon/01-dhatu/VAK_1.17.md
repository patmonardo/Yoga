# VAK_1.17 — Mind Is the Sixth Support

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
ṣaṇṇām anantarātītam       → ṣaṇṇām + anantara-atītam
yad dhi                    → yat + hi
tan manaḥ                  → tat + manaḥ
ṣaṣṭhāśrayaprasiddhyartham → ṣaṣṭha-āśraya-prasiddhi-artham
dhātavo 'ṣṭādaśa          → dhātavaḥ + aṣṭādaśa
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| ṣaṇṇām | genitive plural of *ṣaṣ* | of the six |
| anantara-atītam | nominative neuter singular | immediately past; just ceased |
| vijñānam | nominative neuter singular | cognition, one of the six |
| yat | nominative neuter singular | whichever |
| hi | particle | for; the reason |
| tat | nominative neuter singular | that same one |
| manaḥ | nominative neuter singular | mind |
| ṣaṣṭha-āśraya-prasiddhi-artham | accusative of purpose | in order to establish the sixth support |
| dhātavaḥ | nominative masculine plural | principles |
| aṣṭādaśa | numeral | eighteen |
| smṛtāḥ | nominative masculine plural | taught; held in the teaching |

The Bhāṣya tightens *anantarātīta* to *samanantara-niruddha*: ceased
immediately before, nothing between. That gloss belongs to the commentary.

## 4. Grammar

```text
ṣaṇṇām vijñānam yat anantara-atītam
    = tat manaḥ

ṣaṣṭha-āśraya-prasiddhi-artham
    dhātavaḥ aṣṭādaśa smṛtāḥ
```

*Yat* and *tat* are the same neuter. The genitive *ṣaṇṇām* draws the
cognition from the six already named. The identity is relational. The
verse does not add a seventh Principle.

The purpose compound qualifies the second clause. Eighteen principles
are taught for the sake of establishing the sixth support. The compound
does not say that the eighteen are eighteen substances.

## 5. Translation

### Literal Translation

Whichever Cognition among the six is immediately past, that indeed is
mind. The eighteen principles are taught in order to establish the sixth
support.

### Bhāṣya-informed study translation

Mind is not a seventh Principle beside the six. Whichever of those six
has just ceased is called Mind, and called the Mind Principle, in its
office as support. The five have supports of their own. The
Mind-Cognition Principle has no further support of that kind. Eighteen
are taught so that this sixth support be established.

The support does not require a successor. An arhat's final consciousness
remains mind. Another cause is wanting, and no next principle arises.

## 6. Systematic Placement

The Bhāṣya resolves the eighteen Principles as six supports, six
supported Cognition Principles, and six Objects. Mind is the sixth support:
the immediately ceased Cognition among the six, not a seventh Cognition.
Support is a distinct relation, not a synonym for production.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| vijñāna | Cognition | one of the six; not *citta* |
| manas | Mind | the same Cognition, just ceased |
| manodhātu | Mind Principle | the office, not an additional substance |
| manovijñāna-dhātu | Mind-Cognition Principle | the sixth of the six; the supported |
| anantarātīta | immediately past | Bhāṣya: *samanantara-niruddha* |
| āśraya | support | the office mind fills |
| āśrita | the supported | the six Cognition Principles |
| ālambana | Object | distinct from support and from *viṣaya* |
| citta | consciousness | the arhat's final consciousness; distinct from *manas* |
| dravyataḥ | by substance | the objection's count, not the eighteen Principles |
| prasiddhi | establishment | so that the sixth support be established |

## 8. Logical Determination

```text
1.16   seven names: six Cognitions + Mind Principle
       relation not yet said

1.17   of those six, whichever has just ceased
           → Mind
           → Mind Principle, as support

       present office     one of the six
       just-ceased office mind, the sixth support

       five supports      eye and the rest
       sixth support      mind
       supported          six Cognition Principles
       objects            six
       6 + 6 + 6 = 18

       objection          17, or 12, by substance
       reply              eighteen, for the sixth support

       arhat's last consciousness
           remains Mind
           no successor, another cause wanting
           support ≠ production
```

The objection's twelve is a substance-count. It is not the twelve
essences.

## 9. Interpretive Note

The hinge is *yat ... tat*: whichever, that. Interpretation of the
office, and of the arhat's limit, is in the Bhāṣya.

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
    vak:objects 6 .

vak:MindCognitionPrinciple vak:hasSupport vak:Mind ;
    vak:hasNoFurtherSenseSupport true .

vak:FinalArhatConsciousness vak:remains vak:Mind ;
    vak:hasSuccessor false ;
    vak:reason vak:AnotherCauseWanting .
```
