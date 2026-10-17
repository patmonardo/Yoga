# VAK_2.01 — Governing Efficacy

## 1. Sanskrit (Devanāgarī)

> चतुर्ष्वर्थेषु पञ्चानामाधिपत्यं द्वयोः किल ।
>
> चतुर्णां पञ्चकस्याष्टानां संक्लेशव्यवदानयोः ॥ २.१ ॥

The immediate source compresses the final group (`चतुर्ण्णां पञ्चकाष्टानां`). The study follows the Bhāṣya: the four govern two, the fivefold group governs defilement, and the eight govern purification.

## 2. Sanskrit (IAST)

> caturṣv artheṣu pañcānām ādhipatyaṃ dvayoḥ kila /
>
> caturṇāṃ pañcakasyāṣṭānāṃ saṃkleśavyavadānayoḥ // 2.1 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| caturṣu artheṣu | locative plural | with respect to four meanings |
| pañcānām | genitive plural | of the five |
| ādhipatyam | nominative neuter | governing efficacy |
| dvayoḥ | locative dual | with respect to two |
| kila | particle | indeed; it is said |
| caturṇām | genitive plural | of the four |
| pañcakasya | genitive singular | of the fivefold group |
| aṣṭānām | genitive plural | of the eight |
| saṃkleśa-vyavadānayoḥ | locative dual | defilement and purification |

The verse is elliptical. Ādhipatyam governs all four groups. The Bhāṣya supplies the names.

## 4. Grammar

```text
% start S
S[TYPE=faculty] -> NP[GROUP=?g] VP[GOVERN=true, ARTHA=?a]
NP[GROUP=five] -> 'the five'
NP[GROUP=four] -> 'the four'
NP[GROUP=fivefold] -> 'the fivefold group'
NP[GROUP=eight] -> 'the eight'
VP[GOVERN=true, ARTHA=four-meanings] -> 'govern four meanings'
VP[GOVERN=true, ARTHA=two] -> 'govern two'
VP[GOVERN=true, ARTHA=defilement] -> 'govern defilement'
VP[GOVERN=true, ARTHA=purification] -> 'govern purification'
```

Feature `GOVERN=true` is the predicate. Group features discriminate membership. A successful parse is a faculty; failure is not.

## 5. Translation

### Literal Translation

Of the five, governing efficacy with respect to four meanings; of the four, indeed, with respect to two; of the fivefold and of the eight, with respect to defilement and purification.

### Bhāṣya-informed study translation

> The five govern four meanings of embodied life and disclosure; the four govern distinction and continuity; the fivefold group governs defilement and the eight govern purification. Faculty is governing efficacy, not the items themselves.

## 6. Philosophical Translation

> A faculty is a dharma that governs. The name is one because the efficacy is one, not because the items are one kind.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| indriya | faculty | faculty of Rules, in the Organon section only |
| ādhipatya | governing efficacy | the common predicate; not sovereignty |
| paramaiśvarya | supreme lordship | the root gloss; etymology only |
| artha | meaning | the commentary assigns the functions; function is not the English |
| ātmabhāva-śobhā | attractiveness of embodied existence | first matter of the five |
| ātmabhāva-parikarṣaṇa | preservation of embodied existence | second matter of the five |
| asādhāraṇa-kāraṇatva | specific cause | not a sufficient cause |
| sattva-bheda | distinction of living beings | female and male |
| sattva-vikalpa | differentiation | configuration, voice, conduct; not a separate imagining |
| jīvitendriya | life-faculty | class-series; the second member of the compound is not secure |
| manaindriya | mind-faculty | renewed existence and mastery; a production, not a thinker |
| saṃkleśa | defilement | the five feelings, on the first account |
| vyavadāna | purification | the eight; the feelings also, on the other account |
| prajñā | Discrimination | the faculty in the eight; never discernment |

## 8. Logical Determination

```text
Faculty(x, m)
    ↔ Dharma(x)
    ∧ GovernsWithRespectTo(x, m)

Indriya(x)
    ↛ Organ(x)

SensoryFaculty(x)
    → Indriya(x)
```

Four groups, one predicate:

```text
eye, ear, nose, tongue, body
    → four meanings each

female, male, life, mind
    → two each

five beginning with pleasure
    → defilement
    → purification, on the other account

eight beginning with faith
    → purification
```

The look back is not a second inventory:

```text
principle
    → locus, field, or portion

faculty
    → governing efficacy

principle
    ≠ faculty
```

Some principles are faculties. Some portions are faculties. The five external are not. A principle without governing efficacy is not yet a Rule. Governing efficacy without a principle has no bearer.

## 9. Interpretive Note

Chapter 1 closed by locating faculty: a portion of the dharma-principle, and the twelve internal. This verse changes the question. The common name is ādhipatya.

The twenty-two are not one natural kind. Eye through body, female and male, life, mind, the five feelings, faith, vigor, mindfulness, concentration, Discrimination, and the three of realization, are one class because each governs.

The four matters of the five already exceed bare sensation: attractiveness, preservation, cognition with its associates, specific cause. Feeling is not itself affliction. The eight purify. The other account keeps feeling inside purification as well: the mind of one who is happy concentrates; suffering supports faith; gladness and the rest stand on renunciation.

Kila marks the reported account. It does not by itself settle the author's distance. Principally is analysis. It is not in the verse.

Organon reading: Dhātu is the Faculty of Principles. Indriya is the faculty of Rules. The deposit stays. The wheel starts here. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_01
    a vak:Karika ;
    rdfs:label "VAK 2.01" ;
    vak:hasTopic vak:GoverningEfficacy ;
    vak:belongsTo vak:Indriyanirdesa .

vak:Indriya
    a vak:FunctionalClassification ;
    vak:definedBy vak:Adhipatya .

vak:Adhipatya
    rdfs:label "governing efficacy" ;
    vak:requires vak:Dharma, vak:Meaning .

vak:SensoryFive
    vak:partOf vak:TwentyTwoIndriyas ;
    vak:governs vak:Attractiveness,
        vak:Preservation,
        vak:CognitionWithAssociates,
        vak:SpecificCause .

vak:FemaleMaleLifeMind
    vak:governs vak:DistinctionAndContinuity .

vak:FeelingFive
    vak:governs vak:Defilement .

vak:EightBeginningWithFaith
    vak:governs vak:Purification .

organon:FacultyOfRules
    organon:spinsAfter organon:FacultyOfPrinciples ;
    organon:notIdenticalWith organon:VerseEnglish .
```
