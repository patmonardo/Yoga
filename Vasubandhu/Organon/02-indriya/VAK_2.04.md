# VAK_2.04 — The Three That Complete the Eight

## 1. Sanskrit (Devanāgarī)

> आज्ञास्याम्याख्यमाज्ञाख्यमाज्ञातावीन्द्रियं तथा ।
>
> उत्तरोत्तरसंप्राप्तिनिर्वाणाद्याधिपत्यतः ॥ २.४ ॥

## 2. Sanskrit (IAST)

> ājñāsyāmyākhyam ājñākhyam ājñātāvīndriyaṃ tathā /
>
> uttarottarasaṃprāptinirvāṇādyādhipatyataḥ // 2.4 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| ājñāsyāmi-ākhyam | nominative | the one called “I shall know” |
| ājñā-ākhyam | nominative | the one called knowledge |
| ājñātāvi-indriyam | nominative | the faculty of one who has known |
| tathā | indeclinable | likewise; each a faculty |
| uttarottara-saṃprāpti | compound member | successive attainment |
| nirvāṇa | compound member | nirvāṇa |
| ādi | compound member | and the rest; a second account |
| ādhipatyataḥ | ablative | because of governing efficacy |

The short name is anājñātam ājñāsyāmi, I shall know what is not known.

## 4. Grammar

```text
ājñāsyāmi-ākhyam
ājñā-ākhyam
ājñātāvi-indriyam
    tathā indriyam
    uttarottara-saṃprāpti-nirvāṇa-ādi-ādhipatyataḥ
```

Tathā continues pratyekam from 2.03. Each is a faculty. Ādi opens the second distribution: abandonment by seeing, abandonment by cultivation, pleasant abiding in this life.

## 5. Translation

### Literal Translation

Likewise, the one called “I shall know,” the one called knowledge, and the faculty of one who has known, because of governing efficacy over successive attainment, nirvāṇa, and the rest.

### Bhāṣya-informed study translation

Likewise means each is individually a faculty. The faculty called “I shall know” governs attainment of the knowledge-faculty. The knowledge-faculty governs attainment of the faculty of one who has known. The faculty of one who has known governs parinirvāṇa. There is no parinirvāṇa for one whose mind is not liberated.

And the rest is another account. The first governs abandonment of the afflictions abandoned by seeing. The second governs abandonment of the afflictions abandoned by cultivation. The third governs pleasant abiding in this life, because one experiences the joy and happiness of liberation.

## 6. Philosophical Translation

The three complete the eight. They are not tenses of one act. The first governs the next faculty, and abandonment by seeing. The second governs the last faculty, and abandonment by cultivation. The third governs parinirvāṇa, and pleasant abiding now. The sequence stops. There is no fourth faculty.

Organon rendering:

Applied Indriya. These three complete the controllers of purification. Checking in 2.03 is not this abandonment. The principles remain deposited. Knowledge here is the faculty-name, not the Idea. Not the verse English.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| anājñātam-ājñāsyāmi | I shall know what is not known | first of the three |
| ājñā | knowledge | the faculty-name; not the Idea |
| ājñātāvin | one who has known | completed in this sequence |
| uttarottara-saṃprāpti | successive attainment | next faculty, then parinirvāṇa |
| parinirvāṇa | parinirvāṇa | prose; the verse says nirvāṇa |
| avimukta-citta | mind not liberated | no parinirvāṇa |
| darśana-heya | abandoned by seeing | class of affliction |
| bhāvanā-heya | abandoned by cultivation | class of affliction |
| prahāṇa | abandonment | not the checking of 2.03 |
| dṛṣṭa-dharma-sukha-vihāra | pleasant abiding in this life | not parinirvāṇa |

## 8. Logical Determination

```text
I shall know
    → attainment of the knowledge-faculty
    → abandonment by seeing

knowledge-faculty
    → attainment of one who has known
    → abandonment by cultivation

one who has known
    → parinirvāṇa
    → pleasant abiding in this life
    ↛ a fourth faculty

mind not liberated
    → no parinirvāṇa

successive attainment
    ≠ the abandonment account
    both kept
```

The names are not future, present, and past.

## 9. Interpretive Note

2.03 took five of the eight. This verse takes the three that remain, and the twenty-two are named. Their constitution is not yet analyzed.

The first account is attainment of the next, and then parinirvāṇa. The reason is narrow: no parinirvāṇa while mind is not liberated. It does not say liberated mind is already parinirvāṇa.

The second account is the work. Seeing and cultivation abandon specified classes. The text does not list the classes. Pleasant abiding is present experience of the joy and happiness of liberation. It is not ordinary pleasure, and it is not identified with parinirvāṇa.

Prahāṇa is abandonment. It is not the checking of 2.03, and it is not a generic improvement.

Organon reading: the three complete the controllers of purification on the Kośa Path. The principles remain deposited. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_04
    a vak:Karika ;
    rdfs:label "VAK 2.04" ;
    vak:hasTopic vak:ThreeThatCompleteTheEight ;
    vak:belongsTo vak:Indriyanirdesa .

vak:IShallKnow vak:governsAttainmentOf vak:KnowledgeFaculty ;
    vak:governs vak:AbandonmentBySeeing .
vak:KnowledgeFaculty vak:governsAttainmentOf vak:OneWhoHasKnown ;
    vak:governs vak:AbandonmentByCultivation .
vak:OneWhoHasKnown vak:governs vak:Parinirvana, vak:PleasantAbiding ;
    vak:requires vak:LiberatedMind .

organon:PurificationControllers
    organon:completedBy vak:VAK_2_04 ;
    organon:notTheVerseEnglish true .
```
