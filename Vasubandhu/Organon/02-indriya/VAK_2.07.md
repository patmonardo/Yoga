# VAK_2.07 — Pain, and Pleasure in the Third Dhyāna

## 1. Sanskrit (Devanāgarī)

```sanskrit
दुःखेन्द्रियमशाता या कायिकी वेदना सुखम् ।
शाता ध्याने तृतीये तु चैतसी सा सुखेन्द्रियम् ॥ २.७ ॥
```

## 2. Sanskrit (IAST)

```text
duḥkhendriyam aśātā yā kāyikī vedanā sukham /
śātā dhyāne tṛtīye tu caitasī sā sukhendriyam // 2.7 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| duḥkha-indriyam | nominative | the pain-faculty |
| aśātā yā | nominative | whichever is disagreeable |
| kāyikī vedanā | nominative | bodily feeling |
| sukham śātā | nominative | pleasure is agreeable |
| dhyāne tṛtīye | locative | in the third dhyāna |
| tu | particle | but |
| caitasī sā | nominative | that, mental |
| sukha-indriyam | nominative | the pleasure-faculty |

The feminine agrees with vedanā. The neuter compounds are the faculty-names. Same referent.

## 4. Grammar

```text
% start S
S[FACULTY=pain] -> Feeling[MODE=bodily, TONE=disagreeable]
S[FACULTY=pleasure] -> Feeling[MODE=bodily, TONE=agreeable]
S[FACULTY=pleasure, LEVEL=third] -> Feeling[MODE=mental, TONE=agreeable]
```

Default is bodily. The third-dhyāna feature overrides `MODE`.

## 5. Translation

### Literal Translation

> The pain-faculty is whichever bodily feeling is disagreeable. Pleasure is
> agreeable. But in the third dhyāna, that, mental, is the pleasure-faculty.

### Bhāṣya-informed study translation

> Pain-Faculty is whichever bodily feeling is disagreeable; pleasure is
> agreeable feeling. But in the third dhyāna, the agreeable mental feeling
> is Pleasure-Faculty.

## 6. Philosophical Translation

> The third dhyāna projects agreeable mental feeling into the pleasure-place. It does not create a new faculty.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| duḥkhendriya | pain-faculty | disagreeable bodily feeling |
| sukhendriya | pleasure-faculty | agreeable bodily feeling; mental in the third dhyāna |
| aśātā | disagreeable | Bhāṣya: injurious, upaghātikā |
| śātā | agreeable | Bhāṣya: supportive, anugrāhikā |
| kāyikī | bodily | not a material organ |
| caitasī | mental | mode of feeling; not the faith-group |
| tṛtīya-dhyāna | third dhyāna | the exception |
| pañca-vijñāna-kāya | five cognition-groups | absent there; kāya is the group |

Sukha and duḥkha here are two of the five. Gladness and distress are the next verse.

## 8. Logical Determination

```text
bodily + disagreeable
    → pain-faculty

bodily + agreeable
    → pleasure-faculty

third dhyāna
    → five cognition-groups absent
    → bodily feeling absent
    → agreeable mental feeling is the pleasure-faculty

mental
    ↛ pleasure-faculty
agreeable + mental + third dhyāna
    → pleasure-faculty
```

The exception does not make every agreeable mental feeling the pleasure-faculty.

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the
verse translation): Pain is disagreeable bodily feeling. Pleasure is
agreeable bodily feeling. The exception is narrow: in the third dhyāna the
five cognition-groups are absent, so agreeable mental feeling takes the
pleasure-faculty. Mental feeling is not thereby bodily.

2.03 assigned the feelings to defilement. 2.06 assigned them to the experience of engagement. This verse begins the internal cut.

Injurious and supportive are the commentary's glosses. They are not moral wholesomeness. Pain and pleasure are faculty-names. They are not every suffering and every happiness.

Sā resumes the agreeable feeling. It is not one bodily feeling turning into a mental entity. Absence of the five cognition-groups explains why the feeling is not bodily. It does not yet say why the name is pleasure rather than gladness. That is the next unit.

Eye through male is the range already treated. It is not a count of ten Form faculties. Mind is in that range. Life is deferred because dissociated. The five beginning with faith are deferred to the mental factors.

Organon reading: the network projects the same place under another mode when the level changes. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_07
    a vak:Karika ;
    rdfs:label "VAK 2.07" ;
    vak:hasTopic vak:PainFaculty, vak:PleasureFaculty ;
    vak:belongsTo vak:Indriyanirdesa .

vak:PainFaculty vak:isDisagreeableBodilyFeeling true .
vak:PleasureFaculty vak:defaultMode vak:Bodily ;
    vak:inThirdDhyana vak:AgreeableMentalFeeling .
vak:ThirdDhyana vak:lacks vak:FiveCognitionGroups .

organon:ProjectedNode
    organon:samePlace true ;
    organon:notTheVerseEnglish true .
```
