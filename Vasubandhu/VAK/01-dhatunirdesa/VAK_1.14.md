# VAK_1.14

## 1. Sanskrit (Devanāgarī)

> इन्द्रियार्थास्त एवेष्टा दशायतनधातवः ।
>
> वेदनानुभवः संज्ञा निमित्तोद्ग्रहणात्मिका ॥ १.१४ ॥

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
| daśa-āyatana-dhātavaḥ | daśa āyatana-dhātavaḥ | ten spheres and domains |
| vedanā | vedanā | feeling |
| anubhavaḥ | anubhavaḥ | experience, undergoing |
| saṃjñā | saṃjñā | recognition / sign-cognition |
| nimitta-udgrahaṇa-ātmikā | nimitta-udgrahaṇa-ātmikā | consisting in grasping marks/signs |

## 4. Grammar

The ten faculties and objects are simultaneously counted as ten **āyatanas** and ten **dhātus**:

```text
five faculties
five objects
    = ten spheres
    = ten domains
```

The second half defines two aggregates:

```text
vedanā
    = anubhava, undergoing/experience

saṃjñā
    = nimitta-udgrahaṇa, grasping of marks
```

## 5. Literal Translation

> The faculties and objects themselves are accepted as the ten spheres and domains. Feeling is experience; saṃjñā has as its nature the grasping of signs.

## 6. Philosophical Translation

> The five faculties and five objects function both as spheres and as domains. Feeling is the undergone experience of contact, while saṃjñā is the grasping of a determinate mark.

Organon rendering:

> The same structure can be read as faculty-object relation, sphere, or domain. Vedanā is the immediate undergoing of experience; saṃjñā is the taking-up of a mark, the first stabilization of what is encountered as recognizable.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| indriya | faculty | power/support of sensory knowing |
| artha | meaning / object | object-side of disclosure |
| āyatana | sphere | field of contact/relation |
| dhātu | domain | lawful domain of analysis |
| vedanā | feeling | experience/undergoing |
| anubhava | experience | felt undergoing |
| saṃjñā | recognition / sign-cognition | grasping a mark |
| nimitta | mark / sign | recognizable determination |

## 8. Logical Determination

```text
faculty + object
    = āyatana
    = dhātu
```

and:

```text
vedanā
    = undergoing

saṃjñā
    = mark-grasping
```

## 9. Interpretive Note

This verse shows that the same material structure can be re-read under different formal determinations. As āyatana, it is a sphere of relation. As dhātu, it is a domain. This is not duplication; it is logical perspective.

The definitions of vedanā and saṃjñā are also precise: feeling is not emotion in the modern sense; it is experience as undergone. Saṃjñā is not full conceptual thought; it is the grasping of a mark.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_14
    a vak:Karika ;
    rdfs:label "VAK 1.14" ;
    vak:hasSourceLabel "VAkK_1.14" ;
    vak:hasProjectLabel "VAkK_1.14" ;
    vak:hasTopic vak:TenSpheresDomainsAndTwoAggregates ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Vedana vak:definedAs vak:Anubhava .
vak:Samjna vak:definedAs vak:NimittaUdgrahana .
```

## 11. Commit History

- Added expanded Organon analysis for VAK_1.14.
- Establishes faculties and objects as ten spheres/domains.
- Defines vedanā as experience and saṃjñā as mark-grasping.
