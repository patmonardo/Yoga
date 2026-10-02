# VAK_1.14

## 1. Sanskrit (Devanāgarī)

> इन्द्रियार्थास्त एवेष्टा दशायतनधातवः ।
>
> वेदनानुभवः संज्ञा निमित्तोद्ग्रहणात्मिका ॥ १.१४ ॥॥

## 2. Sanskrit (IAST)

> indriyārthās ta eveṣṭā daśāyatanadhātavaḥ /
>
> vedanānubhavaḥ saṃjñā nimittodgrahaṇātmikā // VAkK_1.14 //

Source label in GRETIL: `VAkK_1.14`. Project-normalized label: `VAkK_1.14`.

## 3. Padaccheda

| Form | Padaccheda | Meaning |
|---|---|---|
| indriya-arthāḥ | indriya-arthāḥ | faculties and objects |
| te eva | te eva | these very same |
| iṣṭāḥ | iṣṭāḥ | are accepted |
| daśa-āyatana-dhātavaḥ | daśa āyatana-dhātavaḥ | ten essences and ten principles |
| vedanā | vedanā | feeling |
| anubhavaḥ | anubhavaḥ | undergoing |
| saṃjñā | saṃjñā | mark-taking |
| nimitta-udgrahaṇa-ātmikā | nimitta-udgrahaṇa-ātmikā | consisting in taking up a mark |

## 4. Grammar

The ten faculties and objects are counted twice:

```text
five faculties
five objects
    = ten Essences
    = ten Principles
```

No new item. `te eva`.

```text
vedanā
    = anubhava

saṃjñā
    = nimitta-udgrahaṇa
```

## 5. Literal Translation

> These very faculties and objects are accepted as the ten Relations and the ten Principles. Feeling is undergoing. Saṃjñā is the taking up of a mark.

## 6. Determination

Essence is pure composite chained access to appearance. Faculty to object. Already in rūpa. Nothing added.

Principle is the logogenesis of that same factor, before Logic. Same ten, second placement. Not a hybrid.

Avijñapti is not in the ten.

Vedanā is undergoing: pleasant, painful, or neither. Not citta.

Saṃjñā is reflecting. Not Idea. Idea stays with vijñāna, and this verse does not say vijñāna.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| āyatana | Essence | pure composite chained access to appearance |
| dhātu | Principle | logogenesis before Logic |
| vedanā | feeling | undergoing |
| anubhava | undergoing | pleasant, painful, neither |
| saṃjñā | mark-taking | not Idea |
| nimitta | mark | what is taken up |
| artha | meaning | object-side of the chain |

## 8. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_14
    a vak:Karika ;
    rdfs:label "VAK 1.14" ;
    vak:hasSourceLabel "VAkK_1.14" ;
    vak:hasProjectLabel "VAkK_1.14" ;
    vak:hasTopic vak:TenRelationsAndPrinciples ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Ayatana rdfs:label "Relation" .
vak:Dhatu rdfs:label "Principle" .
vak:Vedana vak:definedAs vak:Anubhava .
vak:Samjna vak:definedAs vak:NimittaUdgrahana .
```

## 9. Commit History

- Upgraded VAK_1.14.
- Āyatana locked as Relation: pure composite chained access to appearance.
- Dhātu locked as Principle.
- Saṃjñā kept off Idea.
