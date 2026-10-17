# VAK_2.32 — The Distinctions

## 1. Sanskrit (Devanāgarī)

> अह्रीरगुरुता अवद्ये भयादर्शित्वमत्रपा ।
>
> प्रेम श्रद्धा गुरुत्वं ह्रीः ते पुनः कामरूपयोः ॥ २.३२ ॥

## 2. Sanskrit (IAST)

> ahrīr agurutā avadye bhayādarśitvam atrapā /
>
> prema śraddhā gurutvaṃ hrīḥ te punaḥ kāmarūpayoḥ // 2.32 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| ahrīḥ | nominative | shamelessness |
| a-gurutā | nominative | lack of respect |
| avadye | locative | in the blameworthy |
| bhaya-adarśitvam | nominative | failure to see danger |
| atrapā | nominative | lack of moral caution |
| prema | nominative | affection |
| śraddhā | nominative | faith |
| gurutvam | nominative | respect |
| hrīḥ | nominative | moral shame |
| kāma-rūpayoḥ | locative dual | in the desire and form realms |

The verse equates. The commentary qualifies.

## 4. Grammar

```text
% start S
S[NAME=shamelessness] -> LackOfRespect
S[NAME=lack-of-caution] -> FailureToSeeDanger
S[NAME=affection] -> Faith[PERSON=true]
S[NAME=respect] -> MoralShame[PERSON=true]
S[REALM=desire|form] -> Affection Respect
```

Affection and respect are person-directed forms of faith and moral shame.  
They do not unify with the formless.

## 5. Translation

### Literal Translation

Shamelessness is lack of respect. Lack of moral caution is failure to see danger in the blameworthy. Affection is faith. Respect is moral shame. Those, further, in the desire and form realms.

### Bhāṣya-informed study translation

> Shamelessness is lack of respect. Lack of moral caution is failure to see danger in the blameworthy. Affection is the person-directed form of faith; respect is the person-directed form of moral shame. Those occur in the desire and form realms, not the formless. Identity is claimed; alternatives are recorded.

## 6. Philosophical Translation

> The formulas identify. The alternatives refuse identity. Affection and respect are the person-directed forms; they do not reach the formless.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| āhrīkya | shamelessness | lack of respect; alternatively, reference to oneself |
| anapatrāpya | lack of moral caution | failure to see danger; alternatively, reference to others |
| avadya | blameworthy | what good persons condemn |
| hrī | moral shame | the reverse |
| śraddhā | faith | esteem for qualities |
| prema | affection | craving, or fondness preceded by esteem |
| gaurava | respect | acknowledgment of authority |
| kāma-rūpa | desire and form | range of the person-directed forms |

## 8. Logical Determination

```text
seeing no danger
    = prajñā
not seeing danger
    = ignorance
lack of moral caution
    = the secondary that occasions either
    ≠ either presentation

faith and affection
    separate, overlap, both absent
respect and affection
    separate among persons

faith may precede affection
respect may precede moral shame
others
    not identical

person-directed
    desire and form
    not formless
dharma-directed
    remain
```

## 9. Interpretive Note

The counts deferred these definitions. Lack of moral caution was counted apart from Discrimination and from delusion. The reply keeps that count.

The person examples show the relations can separate. They are not judgments about every parent or teacher. Others are reported. Not a final rejection of the verse's equations.

The reversal of the negative pair is damaged. Seeing danger, rather than the negative of the preceding definition, follows the announced reversal. It wants collation. Disposition does not add a latent entity beside the named factor.

Organon reading: a compact formula is not the relation. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_32
    a vak:Karika ;
    rdfs:label "VAK 2.32" ;
    vak:hasTopic vak:FactorDistinctions ;
    vak:belongsTo vak:Indriyanirdesa .

vak:PersonDirectedForms vak:absentFrom vak:FormlessRealm .
vak:Faith vak:remainsInFormless true .

organon:EquationNotIdentity
    organon:notTheVerseEnglish true .
```
