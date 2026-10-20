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

The verse distributes one predicate, *ādhipatyam*, across four groups. The
first locative gives four meanings to each of the five sensory Faculties;
the second gives two meanings to each of the four named in the Bhāṣya.
The final locative dual is ordered: the five feelings govern defilement,
and the eight beginning with faith govern purification. *Kila* marks the
second assignment as reported. The grammar makes the ellipsis explicit
in each clause without adding Sanskrit tokens or a higher-order relation.

```nltk-fcfg
% start S
# tokens: caturṣu artheṣu pañcānām ādhipatyam dvayoḥ kila caturṇām pañcakasya aṣṭānām saṃkleśa-vyavadānayoḥ
S[SEM=<(?first & ?second & ?last)>] -> FIRST[SEM=?first] SECOND[SEM=?second] LAST[SEM=?last]
FIRST[SEM=<Governs(sensory_five,four_meanings)>] -> FOUR[CASE=loc,NUM=pl,CNT=4] MEANINGS[CASE=loc,NUM=pl] FIVE[CASE=gen,NUM=pl,CNT=5] GOVERN
FOUR[CASE=loc,NUM=pl,CNT=4] -> 'caturṣu'
MEANINGS[CASE=loc,NUM=pl] -> 'artheṣu'
FIVE[CASE=gen,NUM=pl,CNT=5] -> 'pañcānām'
GOVERN -> 'ādhipatyam'
SECOND[SEM=<Governs(other_four,two_meanings)>] -> TWO[CASE=loc,NUM=du,CNT=2] REPORT[VOICE=reported] OTHER_FOUR[CASE=gen,NUM=pl,CNT=4]
TWO[CASE=loc,NUM=du,CNT=2] -> 'dvayoḥ'
REPORT[VOICE=reported] -> 'kila'
OTHER_FOUR[CASE=gen,NUM=pl,CNT=4] -> 'caturṇām'
LAST[SEM=<(Governs(feeling_five,defilement) & Governs(purifying_eight,purification))>] -> FEELINGS[CASE=gen,NUM=sg,CNT=5] PURIFIERS[CASE=gen,NUM=pl,CNT=8] FIELDS[CASE=loc,NUM=du,ORDER=defilement_purification]
FEELINGS[CASE=gen,NUM=sg,CNT=5] -> 'pañcakasya'
PURIFIERS[CASE=gen,NUM=pl,CNT=8] -> 'aṣṭānām'
FIELDS[CASE=loc,NUM=du,ORDER=defilement_purification] -> 'saṃkleśa-vyavadānayoḥ'
```

```nltk-dep
'ādhipatyam' -> 'pañcānām' | 'artheṣu' | 'caturṇām' | 'dvayoḥ' | 'pañcakasya' | 'aṣṭānām' | 'saṃkleśa-vyavadānayoḥ' | 'kila'
'artheṣu' -> 'caturṣu'
```

**Feature chart checkpoints.** The ten normalized tokens give `FIRST`
[0, 4), `SECOND` [4, 7), `LAST` [7, 10), and one root [0, 10).
Changing a count, the second locative dual, or the final ordered dual
blocks the relevant clause. `VOICE=reported` records *kila* in the chart;
the finite FOL projection tests the content of that reported assignment.

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

**Kārikā, derived.** The root `SEM` gives four governing relations. The
Bhāṣya supplies the group members and says *yathākramam* for the final
pair. Its later claim that feelings also govern purification is introduced
by *apare* (“others”); the finite model records that report separately
from the verse's ordered assignment. Counts remain grammatical constraints
on the groups, not arithmetic claims about the model's sample individuals.

```nltk-sem
first : Governs(sensory_five,four_meanings)
second : Governs(other_four,two_meanings)
last : Governs(feeling_five,defilement) & Governs(purifying_eight,purification)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
Governs(sensory_five,four_meanings) & Governs(other_four,two_meanings) & (Governs(feeling_five,defilement) & Governs(purifying_eight,purification))

# THEORY prose_member_distribution
# EXPECT prose_member_distribution T
all x.(SensoryMember(x) -> Governs(x,four_meanings))
all x.(OtherFourMember(x) -> Governs(x,two_meanings))
all x.(FeelingMember(x) -> Governs(x,defilement))
all x.(PurifyingMember(x) -> Governs(x,purification))

# THEORY reported_feeling_alternative
# EXPECT reported_feeling_alternative T
Reports(others,feelings_also_purify) & Governs(feeling_five,defilement)

# THEORY rejected_sensory_five_two_meanings
# EXPECT rejected_sensory_five_two_meanings F
Governs(sensory_five,two_meanings) & Governs(sensory_five,four_meanings)

# THEORY rejected_four_four_meanings
# EXPECT rejected_four_four_meanings F
Governs(other_four,four_meanings) & Governs(other_four,two_meanings)

# THEORY rejected_final_fields_reversed
# EXPECT rejected_final_fields_reversed F
Governs(feeling_five,purification) & Governs(purifying_eight,defilement)
```

```nltk-valuation
sensory_five => sf
other_four => of
feeling_five => ff
purifying_eight => pe
four_meanings => fm
two_meanings => tm
defilement => def
purification => pur
eye => eye_d
female => female_d
pleasure => pleasure_d
faith => faith_d
others => others_d
feelings_also_purify => alternative_d
Governs => {(sf,fm),(of,tm),(ff,def),(pe,pur),(eye_d,fm),(female_d,tm),(pleasure_d,def),(faith_d,pur)}
SensoryMember => {eye_d}
OtherFourMember => {female_d}
FeelingMember => {pleasure_d}
PurifyingMember => {faith_d}
Reports => {(others_d,alternative_d)}
```

The model witnesses the four verse assignments and one member of each
group. Its false theories catch swapped fields; the reported alternative
is present as an attributed claim, not silently installed as the first
account's fact. Neither a finite valuation nor this group-level projection
proves all twenty-two memberships or resolves the Bhāṣya's later objection
in 2.02.

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
