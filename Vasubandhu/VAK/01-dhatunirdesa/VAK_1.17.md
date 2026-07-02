# VAK_1.17

## 1. Sanskrit (Devanāgarī)

> षण्णामनन्तरातीतं विज्ञानं यद्धि तन्मनः ।
>
> षष्ठाश्रयप्रसिद्ध्यर्थं धातवोऽष्टादश स्मृताः ॥ १.१७ ॥

## 2. Sanskrit (IAST)

> ṣaṇṇām anantarātītaṃ vijñānaṃ yad dhi tan manaḥ /
>
> ṣaṣṭhāśrayaprasiddhyarthaṃ dhātavo 'ṣṭādaśa smṛtāḥ // VAkK_1.17 //

Source label in GRETIL: `VAkK_1.17`. Project-normalized label: `VAkK_1.17`.

## 3. Padaccheda

| Form | Padaccheda | Meaning |
|---|---|---|
| ṣaṇṇām | ṣaṇṇām | of the six |
| anantara-atītam | anantara-atītam | immediately past |
| vijñānam | vijñānam | knowledge |
| yat hi | yat hi | whatever indeed |
| tat manaḥ | tat manaḥ | that is mind |
| ṣaṣṭha-āśraya-prasiddhi-artham | ṣaṣṭhāśraya-prasiddhyartham | for establishing the sixth support |
| dhātavaḥ aṣṭādaśa | dhātavaḥ aṣṭādaśa | eighteen domains |
| smṛtāḥ | smṛtāḥ | are remembered / taught |

## 4. Grammar

The verse defines **manas** functionally:

```text
whatever knowledge among the six
has just passed away immediately
    = manas
```

This establishes the sixth support. Therefore eighteen domains are taught:

```text
six faculties
six objects
six knowledges
    = eighteen domains
```

## 5. Literal Translation

> Whatever knowledge of the six has immediately passed, that indeed is mind. For the sake of establishing the sixth support, eighteen domains are taught.

## 6. Philosophical Translation

> Manas is the immediately past sixfold knowledge functioning as the support for the next mental occurrence. The eighteen domains are taught in order to establish this sixth support alongside the other faculties.

Organon rendering:

> Mind is not an isolated substance. It is the immediate past of knowledge functioning as support. The cognitive series becomes possible because prior disclosure turns into the condition for subsequent disclosure.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| anantara | immediate | without intervening gap |
| atīta | past | just-past occurrence |
| vijñāna | knowledge | sixfold knowledge-event |
| manas | mind | immediately past knowledge as support |
| āśraya | support | condition for subsequent knowledge |
| dhātu | domain | eighteen-domain system |
| smṛta | remembered / taught | doctrinally established |

## 8. Logical Determination

```text
sixfold knowledge
    ↓ immediately past
manas
    ↓ support
next knowledge
```

The eighteen domains are required because mind must be counted as the sixth support.

## 9. Interpretive Note

This is one of the great anti-substantialist verses. Manas is not introduced as a hidden self. It is the immediately past knowledge-event functioning as support.

Organon note:

```text
mind
    = temporalized support
    = knowledge become condition
```

This is the first explicit logic of cognitive succession in the chapter. It also prepares the later account of mental knowledge being supported by the past.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_17
    a vak:Karika ;
    rdfs:label "VAK 1.17" ;
    vak:hasSourceLabel "VAkK_1.17" ;
    vak:hasProjectLabel "VAkK_1.17" ;
    vak:hasTopic vak:ManasAsImmediatelyPastKnowledge ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Manas
    vak:definedAs vak:ImmediatelyPastVijnana ;
    vak:functionsAs vak:SixthSupport .
```

## 11. Commit History

- Upgraded VAK_1.17 with expanded Organon analysis.
- Defines manas as immediately past sixfold knowledge.
- Establishes the eighteen domains as necessary for the sixth support.
