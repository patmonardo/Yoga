# VAK_2.01 — Governing Efficacy

## 1. Sanskrit (Devanāgarī)

```sanskrit
चतुर्ष्वर्थेषु पञ्चानामाधिपत्यं द्वयोः किल ।
चतुर्णां पञ्चकस्याष्टानां संक्लेशव्यवदानयोः ॥ २.१ ॥
```

The immediate source compresses the final group (`चतुर्ण्णां पञ्चकाष्टानां`). The study follows the Bhāṣya: the four govern two, the fivefold group governs defilement, and the eight govern purification.

## 2. Sanskrit (IAST)

```text
caturṣv artheṣu pañcānām ādhipatyaṃ dvayoḥ kila /
caturṇāṃ pañcakasyāṣṭānāṃ saṃkleśavyavadānayoḥ // 2.1 //
```

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

**Grammar tokens.** Sandhi is opened without altering the Sanskrit
witness. The final dual compound stays one token because its ordered
members distribute over the preceding two genitives.

```text
# tokens: caturṣu artheṣu pañcānām ādhipatyam dvayoḥ kila caturṇām pañcakasya aṣṭānām saṃkleśa-vyavadānayoḥ
```

## 4. Grammar

The genitives *pañcānām*, *caturṇām*, *pañcakasya*, and *aṣṭānām* name
four groups to which *ādhipatyam* is distributed. The locatives *caturṣv
artheṣu* and *dvayoḥ* give the respective fields of the first two
groups. The locative dual *saṃkleśavyavadānayoḥ* supplies the two fields
for the last two groups. The Bhāṣya's *yathākramam* assigns defilement
to the five feelings and purification to the eight beginning with faith.
The verse alone compresses this assignment. *Kila* marks the account as
reported; it does not resolve the later alternative about feeling.

```nltk-fcfg
% start S
# tokens: caturṣu artheṣu pañcānām ādhipatyam dvayoḥ kila caturṇām pañcakasya aṣṭānām saṃkleśa-vyavadānayoḥ
S[SEM=<(?a & (?r(?g)(?f) & ?c))>] -> FIRST[SEM=?a,REL=?r] SECOND[GROUP=?g,FIELD=?f,EVID=reported] LAST[SEM=?c]
FIRST[SEM=<?r(?g)(?f)>,REL=?r] -> NUM[CASE=loc,NUM=pl,CNT=4] FIELD[CASE=loc,NUM=pl,SEM=?f] GROUP[CASE=gen,NUM=pl,CNT=5,SEM=?g] GOVERN[SEM=?r]
SECOND[GROUP=?g,FIELD=?f,EVID=reported] -> FIELD[CASE=loc,NUM=du,SEM=?f] EVID[VALUE=reported] GROUP[CASE=gen,NUM=pl,CNT=4,SEM=?g]
LAST[SEM=<?p(?g)(?h)>] -> GROUP[CASE=gen,NUM=sg,CNT=5,SEM=?g] GROUP[CASE=gen,NUM=pl,CNT=8,SEM=?h] PAIR[CASE=loc,NUM=du,SEM=?p]
NUM[CASE=loc,NUM=pl,CNT=4] -> 'caturṣu'
FIELD[CASE=loc,NUM=pl,SEM=<four_meanings>] -> 'artheṣu'
GROUP[CASE=gen,NUM=pl,CNT=5,SEM=<sensory_five>] -> 'pañcānām'
GOVERN[SEM=<\g.\f.Governs(g,f)>] -> 'ādhipatyam'
FIELD[CASE=loc,NUM=du,SEM=<two_meanings>] -> 'dvayoḥ'
EVID[VALUE=reported] -> 'kila'
GROUP[CASE=gen,NUM=pl,CNT=4,SEM=<other_four>] -> 'caturṇām'
GROUP[CASE=gen,NUM=sg,CNT=5,SEM=<feeling_five>] -> 'pañcakasya'
GROUP[CASE=gen,NUM=pl,CNT=8,SEM=<purifying_eight>] -> 'aṣṭānām'
PAIR[CASE=loc,NUM=du,SEM=<\g.\h.(Governs(g,defilement) & Governs(h,purification))>] -> 'saṃkleśa-vyavadānayoḥ'
```

```nltk-dep
'ādhipatyam' -> 'pañcānām' | 'artheṣu' | 'caturṇām' | 'dvayoḥ' | 'pañcakasya' | 'aṣṭānām' | 'saṃkleśa-vyavadānayoḥ' | 'kila'
'artheṣu' -> 'caturṣu'
```

**Feature chart checkpoints.** The half-open spans refer to the ten
normalized tokens. The inherited `REL` applies *ādhipatyam* to the
second group without inserting a second Sanskrit word. `EVID=reported`
keeps *kila*'s voice visible, while the FOL projection records the
predications rather than a claim that the report is true.

| Span | Constituent | Result |
|---|---|---|
| [0, 4) | `FIRST` | five sensory faculties govern four meanings |
| [4, 7) | `SECOND` | reported four govern two meanings; relation inherited |
| [7, 10) | `LAST` | ordered pairing of five feelings and eight purifiers |
| [0, 10) | `S` | four governing relations conjoined |

## 5. Translation

### Literal Translation

> Of the five, governing efficacy with respect to four meanings; of the
> four, indeed, with respect to two; of the fivefold and of the eight, with
> respect to defilement and purification.

### Bhāṣya-informed study translation

> The five sensory Faculties have governing efficacy with respect to four
> meanings each; the four—female, male, life, and mind—it is said, with
> respect to two each. The five feeling Faculties govern defilement; the
> eight beginning with faith govern purification.

## 6. Philosophical Translation

> These distinct dharmas bear one Faculty designation through governing
> efficacy, though their bearers and the meanings they govern differ.

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
| prajñā | discriminative comprehension | the faculty in the eight; not discernment |

## 8. Logical Determination

The section 4 parse composes the verse's four assignments. Its lexical
*ādhipatyam* is a curried relation; the first clause applies it, and the
second clause inherits it across the ellipsis. The final locative dual
applies its ordered fields to the two preceding groups. These are group
level projections; the Bhāṣya distributes each count over individual
faculties. The model checks the projection and its source specified
members, without treating four or two as an arithmetic operation.

```nltk-sem
governing : \g.\f.Governs(g,f)
paired_fields : \g.\h.(Governs(g,defilement) & Governs(h,purification))
```

**Root `SEM`, after beta reduction.**

```nltk-fol
# THEORY verse
# EXPECT verse T
(Governs(sensory_five,four_meanings) & Governs(other_four,two_meanings) & Governs(feeling_five,defilement) & Governs(purifying_eight,purification))

# THEORY prose
# EXPECT prose T
all x.(SensoryMember(x) -> (Faculty(x) & Governs(x,four_meanings)))
all x.(OtherFourMember(x) -> (Faculty(x) & Governs(x,two_meanings)))
all x.(FeelingMember(x) -> (Faculty(x) & Governs(x,defilement)))
all x.(PurifyingMember(x) -> (Faculty(x) & Governs(x,purification)))
exists x.(FeelingMember(x) & Governs(x,purification))

# THEORY rejected_all_conditions_are_faculties
# EXPECT rejected_all_conditions_are_faculties F
all x.(Condition(x) -> Faculty(x))
```

The `prose` theory represents the Bhāṣya's distribution and its
alternative that feeling also governs purification. The verse formula
retains the first account's *yathākramam*. The negative theory guards the
question that 2.02 raises: causal participation alone is not governing
efficacy. It is a countermodel to that inference, not a claim that the
word *Condition* occurs in this verse.

```nltk-valuation
sensory_five => sf
other_four => of
feeling_five => ff
purifying_eight => pe
four_meanings => fm
two_meanings => tm
defilement => def
purification => pur
Governs => {(sf,fm), (of,tm), (ff,def), (pe,pur), (eye,fm), (female,tm), (pleasure,def), (pleasure,pur), (faith,pur)}
SensoryMember => {eye}
OtherFourMember => {female}
FeelingMember => {pleasure}
PurifyingMember => {faith}
Faculty => {eye,female,pleasure,faith}
Condition => {visible_form}
```

The finite witness represents one member of each group. It does not
certify the total membership counts or prove the historical account.
The distinction between conditioned genesis and governing efficacy needs
the later causal analysis; it is not silently derived from this verse.

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the
verse translation): The five govern four meanings of embodied life and
disclosure; the four govern distinction and continuity; the fivefold group
governs defilement and the eight govern purification. Faculty is governing
efficacy, not the items themselves.

Chapter 1 closed by locating faculty: a portion of the dharma-principle, and the twelve internal. This verse changes the question. The common name is ādhipatya.

The twenty-two are not one natural kind. Eye through body, female and male, life, mind, the five feelings, faith, vigor, mindfulness, concentration, discriminative comprehension, and the three of realization, are one class because each governs.

The four matters of the five already exceed bare sensation: attractiveness, preservation, cognition with its associates, specific cause. Feeling is not itself affliction. The eight purify. The other account keeps feeling inside purification as well: the mind of one who is happy concentrates; suffering supports faith; gladness and the rest stand on renunciation.

Kila marks the reported account. It does not by itself settle the author's distance. Principally is analysis. It is not in the verse.

Interpretation: Dhātu is the Faculty of Principles. Indriya is the faculty of Rules. The deposit stays. The wheel starts here. Not the verse English.

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
