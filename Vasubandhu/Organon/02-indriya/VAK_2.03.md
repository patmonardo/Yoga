# VAK_2.03 — Class, Defilement, Purification

## 1. Sanskrit (Devanāgarī)

> निकायस्थितिसंक्लेशव्यवदानाधिपत्यतः ।
>
> जीवितं वेदनाः पञ्च श्रद्धाद्याश्चेन्द्रियं मताः ॥ २.३ ॥

## 2. Sanskrit (IAST)

> nikāyasthitisaṃkleśavyavadānādhipatyataḥ /
>
> jīvitaṃ vedanāḥ pañca śraddhādyāś cendriyaṃ matāḥ // 2.3 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| nikāya-sthiti | compound member | persistence of the living class |
| saṃkleśa | compound member | defilement |
| vyavadāna | compound member | purification |
| ādhipatyataḥ | ablative | because of governing efficacy |
| jīvitam | nominative | life |
| vedanāḥ pañca | nominative | the five feelings |
| śraddhā-ādyāḥ | nominative | those beginning with faith |
| ca | conjunction | and |
| indriyam | predicative | faculty, read distributively |
| matāḥ | nominative participle | are held |

The compound gives three fields. The second line gives three groups, in that order.

## 4. Grammar

```text
nikāya-sthiti-ādhipatyataḥ
    jīvitam indriyam matam

saṃkleśa-ādhipatyataḥ
    vedanāḥ pañca indriyam matāḥ

vyavadāna-ādhipatyataḥ
    śraddhā-ādyāḥ indriyam matāḥ
```

The Bhāṣya specifies nikāya-sthiti as nikāyasabhāga-sthiti, persistence of the homogeneous class. Śraddhādyāḥ here are five, each a faculty: faith, vigor, mindfulness, concentration, Discrimination. The eight of 2.01 are not closed in this verse.

## 5. Translation

### Literal Translation

Because of governing efficacy over class-persistence, defilement, and purification, life, the five feelings, and those beginning with faith are held to be faculty.

### Bhāṣya-informed study translation

The life-faculty governs persistence of the homogeneous class of living beings. The feelings govern defilement. The sūtra says: attachment lies latent in pleasant feeling, aversion in painful feeling, ignorance in neither-painful-nor-pleasant feeling. The five beginning with faith govern purification: through them the afflictions are checked, and the path is brought forward. Each of these is individually accepted as a faculty.

## 6. Philosophical Translation

Life governs standing, not origination. The five feelings govern the tones on which affliction lies. They are not the afflictions. Faith, vigor, mindfulness, concentration, and Discrimination govern purification, by checking the afflictions and drawing the path forward. Faculty is not only apprehension. It is also persistence, defilement, and purification.

Organon rendering:

Applied Indriya. Defilement and purification are the Kośa Path. The five feelings and the five beginning with faith are its controllers. Life controls the standing of the class, and is not one of those two. Checking is not final abandonment. The principles remain deposited. Not the verse English.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| nikāyasthiti | class-persistence | Bhāṣya: nikāyasabhāga-sthiti |
| jīvita | life-faculty | standing, not creation |
| vedanā | feeling | not the affliction |
| saṃkleśa | defilement | the Kośa Path, one side |
| vyavadāna | purification | the Kośa Path, the other side |
| anuśete | lies latent | relation of affliction to feeling; not identity |
| śraddhā | faith | first of the five |
| vīrya | vigor | |
| smṛti | mindfulness | |
| samādhi | concentration | |
| prajñā | Discrimination | never discernment |
| viṣkambha | checking | not final abandonment |
| āvāhana | drawing forward | the path brought on |

## 8. Logical Determination

```text
life
    → persistence of the homogeneous class
    ↛ creates the aggregates

pleasant feeling
    → attachment lies latent
painful feeling
    → aversion lies latent
neither
    → ignorance lies latent

feeling
    ≠ affliction

five beginning with faith
    → each governs purification
    → afflictions checked
    → path drawn forward

purification
    ≠ mere absence
```

The five of the verse are not the eight of 2.01. The remaining three are not this unit.

## 9. Interpretive Note

2.01 named defilement and purification as the last distribution. 2.02 revised the six and the body-portion. This verse gives the predicate of the rest that are in view: life, the five feelings, and five of the eight.

The sūtra uses three tones. The verse counts five faculties. Pleasure and gladness are pleasant. Pain and distress are painful. Equanimity is neither. The tones are not a second list of faculties.

Pleasant feeling is not attachment. Painful feeling is not aversion. Neutral feeling is not ignorance. The citation does not say every feeling produces its affliction, and it does not tell a story about neutrality hiding ignorance.

The five check and draw. The two operations are coordinated. The text does not say checking must finish before the path begins, and it does not assign a separate operation to each of the five.

Organon reading: Defilement and purification are the Kośa Path. The faculties that govern them are its controllers. Life governs the standing of the class beside that path. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_03
    a vak:Karika ;
    rdfs:label "VAK 2.03" ;
    vak:hasTopic vak:ClassDefilementPurification ;
    vak:belongsTo vak:Indriyanirdesa .

vak:LifeFaculty vak:governs vak:ClassPersistence .
vak:FeelingFive vak:governs vak:Defilement .
vak:FiveBeginningWithFaith vak:governs vak:Purification .
vak:Feeling vak:notIdenticalWith vak:Affliction .
vak:Purification vak:checks vak:Affliction ;
    vak:drawsForward vak:Path .

organon:KosaPath
    organon:namedBy vak:Defilement, vak:Purification ;
    organon:controlledBy vak:FeelingFive, vak:FiveBeginningWithFaith ;
    organon:notTheVerseEnglish true .
```
