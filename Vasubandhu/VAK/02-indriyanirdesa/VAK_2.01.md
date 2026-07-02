# VAK_2.01 — Indriyanirdeśa Opening

## 1. Sanskrit — Devanāgarī

```text
चतुर्ष्वर्थेषु पञ्चानामाधिपत्यं द्वयोः किल ।
चतुर्ण्णां पञ्चकाष्टानां संक्लेशव्यवदानयोः ॥ VAkK_2.1 ॥
```

## 2. Sanskrit — IAST

```text
caturṣv artheṣu pañcānām ādhipatyaṃ dvayoḥ kila /
caturṇṇāṃ pañcakāṣṭānāṃ saṃkleśavyavadānayoḥ // VAkK_2.1 //
```

Source form:

```text
caturṣvartheṣu pañcānāmādhipatyaṃ dvayoḥ kila /
caturṇṇāṃ pañcakāṣṭānāṃ saṃkleśavyavadānayoḥ // VAkK_2.1 //
```

## 3. Padaccheda

| Text | Padaccheda | Basic Sense |
|---|---|---|
| caturṣvartheṣu | caturṣu artheṣu | in four functions / meanings / aims |
| pañcānām | pañcānām | of the five |
| ādhipatyam | ādhipatyam | dominance, governing power, sovereignty |
| dvayoḥ | dvayoḥ | of the two |
| kila | kila | indeed, as taught |
| caturṇṇām | caturṇām | of the four |
| pañcakāṣṭānām | pañcakānām aṣṭānām | of the fivefold and eightfold groups |
| saṃkleśavyavadānayoḥ | saṃkleśa-vyavadānayoḥ | of defilement and purification |

## 4. Grammar

```text
caturṣu artheṣu
    locative plural
    “with respect to four functions / meanings”

pañcānām
    genitive plural
    “of the five”

ādhipatyam
    nominative / accusative singular neuter
    “governing dominance,” “sovereign efficacy”

dvayoḥ
    genitive dual
    “of the two”

caturṇām
    genitive plural
    “of the four”

pañcakānām aṣṭānām
    genitive plural
    “of the groups of five and eight”

saṃkleśa-vyavadānayoḥ
    genitive dual
    “of defilement and purification”
```

The verse is elliptical. The governing syntactic idea is:

```text
ādhipatyāt indriyam
```

That is:

```text
Because of governing power, these are faculties.
```

## 5. Minimal Classification Note

This verse compresses the full doctrine of the twenty-two *indriyas*. We introduce the list only as orientation, not as a full Bhāṣya-based exposition.

```text
Twenty-two indriyas:

1–6. Six cognitive / sensory faculties:
    cakṣus
    śrotra
    ghrāṇa
    jihvā
    kāya
    manas

7–8. Two sexual faculties:
    strī-indriya
    puruṣa-indriya

9. Life faculty:
    jīvita-indriya

10–14. Five feeling faculties:
    sukha
    duḥkha
    saumanasya
    daurmanasya
    upekṣā

15–19. Five pure / constructive faculties:
    śraddhā
    vīrya
    smṛti
    samādhi
    prajñā

20–22. Three faculties of realization:
    anājñātam-ājñāsyāmīndriya
    ājñendriya
    ājñātāvīndriya
```

The important point is that **indriya** is not yet merely “sense organ.” It is a determination that has **ādhipatya**, governing efficacy.

## 6. Literal Translation

```text
Of the five, there is governing dominance with respect to four functions;
of the two, indeed; of the four, and of the fivefold and eightfold groups,
with respect to defilement and purification.
```

This literal translation intentionally preserves the elliptical compression of the kārikā.

## 7. Philosophical Translation

```text
The faculties are called faculties because they exercise governing power:
the first five govern four functional domains;
the two govern sexual differentiation;
the life faculty governs persistence of the living series;
the feeling faculties govern affective involvement;
and the pure and realization faculties govern defilement and purification.
```

This is an expanded philosophical translation, informed by VAK_2.02–VAK_2.05 but not yet by a fully cleaned Bhāṣya source.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| indriya | faculty / governing power | Not simply “sense organ” |
| ādhipatya | governing dominance / sovereignty | Key definition of *indriya* |
| artha | function / meaning | Here probably functional object-domain |
| saṃkleśa | defilement / entanglement | Impure involvement |
| vyavadāna | purification / clarification | Purifying release or clarification |
| manas | mind-faculty | Sixth among the first six |
| prajñā | principle / discriminative knowing | Already fixed in project vocabulary |
| smṛti | recollection | Already fixed in project vocabulary |

## 9. Logical Determination

```text
indriya
    =
a dharma insofar as it has ādhipatya
```

So the chapter begins not with a catalogue of organs but with a principle of **dominant functional determination**.

The movement from Chapter 1 to Chapter 2 is therefore:

```text
Dhātunirdeśa
    =
determination of domains

Indriyanirdeśa
    =
determination of governing powers within domains
```

Chapter 1 defined the field. Chapter 2 asks which determinations govern the field.

## 10. Organon Interpretation

This is a major transition.

```text
VAK_1:
    domain-structure

VAK_2:
    command-structure
```

Or:

```text
dhātu
    =
where a determination belongs

indriya
    =
where a determination rules
```

The *indriya* is therefore not primarily a substance, organ, faculty, or psychological capacity. It is a **functional sovereignty** within the dharma-field.

This is why **ādhipatya** is the hinge term. The faculty is not just present; it governs.

## 11. OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_01 a vak:Karika ;
    rdfs:label "VAK 2.01" ;
    vak:sourceVerse "VAkK_2.1" ;
    vak:chapter vak:Indriyanirdesa ;
    vak:hasTopic vak:Indriya ;
    vak:hasKeyTerm vak:Adhipatya ;
    vak:hasLiteralTranslation
        "Of the five, there is governing dominance with respect to four functions; of the two, indeed; of the four, and of the fivefold and eightfold groups, with respect to defilement and purification." ;
    vak:hasPhilosophicalTranslation
        "The faculties are called faculties because they exercise governing power: the first five govern four functional domains; the two govern sexual differentiation; the life faculty governs persistence of the living series; the feeling faculties govern affective involvement; and the pure and realization faculties govern defilement and purification." .

vak:Indriya a logic:Determination ;
    rdfs:label "indriya" ;
    vak:canonicalTranslation "faculty / governing power" ;
    vak:definedBy vak:Adhipatya .

vak:Adhipatya a logic:Determination ;
    rdfs:label "ādhipatya" ;
    vak:canonicalTranslation "governing dominance / functional sovereignty" .

vak:Indriyanirdesa a vak:Chapter ;
    rdfs:label "Indriyanirdeśa" ;
    vak:logicalFunction "Determination of governing powers within the domain-structure." .
```

## 12. Commit History

```text
VAK_2.01 opened.
Chapter: Indriyanirdeśa.
Method: kārikā-first.
Bhāṣya: acknowledged but not yet integrated as cleaned source.
Key decision: indriya = faculty / governing power, not merely sense organ.
Key term: ādhipatya = governing dominance / functional sovereignty.
Twenty-two indriyas introduced only as structural orientation.
Zero-padded file naming adopted: VAK_2.01, VAK_2.02, etc.
```
