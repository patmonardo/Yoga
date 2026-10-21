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
| duḥkhendriyam | nominative singular neuter compound | Pain-Faculty, the predicate of the relative clause |
| aśātā | nominative singular feminine adjective | disagreeable; qualifies feeling |
| yā | nominative singular feminine relative pronoun | whichever; agrees with feeling |
| kāyikī | nominative singular feminine adjective | bodily; qualifies feeling |
| vedanā | nominative singular feminine noun | feeling, the subject being classified |
| sukham | nominative singular neuter noun, used as the Faculty-name | Pleasure[-Faculty]; the Bhāṣya expands the elliptical clause |
| śātā | nominative singular feminine adjective | agreeable; resumes bodily feeling in the pleasure clause |
| dhyāne | locative singular neuter noun | in dhyāna |
| tṛtīye | locative singular neuter ordinal | third; agrees with dhyāna |
| tu | adversative particle | but; marks the qualified mental case |
| caitasī | nominative singular feminine adjective | mental; qualifies the resumed agreeable feeling |
| sā | nominative singular feminine demonstrative | that; resumes agreeable feeling |
| sukhendriyam | nominative singular neuter compound | Pleasure-Faculty, the predicate of the qualified clause |

The feminine forms agree with feeling; the neuter Faculty-names are predicates, not adjectives agreeing with it. The Bhāṣya supplies bodily feeling in the elliptical pleasure clause.

**Grammar tokens.** External sandhi is opened. No words are added to the verse stream; the second clause's resumed subject is marked as prose-supplied in the grammar.

```text
# tokens: duḥkhendriyam aśātā yā kāyikī vedanā sukham śātā dhyāne tṛtīye tu caitasī sā sukhendriyam
```

## 4. Grammar

The relative clause defines Pain-Faculty. The second clause resumes bodily feeling, as the Bhāṣya explicitly confirms. In the last clause, the locative pair constrains the mental case to the third dhyāna. The feminine anaphor resumes agreeable feeling from the preceding clause, while mental mode and third-dhyāna level delimit its new predication. The shared reference records that antecedent without identifying a bodily feeling-token with a mental one.

```nltk-fcfg
% start S
# tokens: duḥkhendriyam aśātā yā kāyikī vedanā sukham śātā dhyāne tṛtīye tu caitasī sā sukhendriyam
S[SEM=<(?pain & ?pleasure & ?third)>] -> PAIN[SEM=?pain] PLEASURE[SEM=?pleasure] THIRD[SEM=?third]
PAIN[SEM=<all x.((Feeling(x) & Bodily(x) & Disagreeable(x)) -> ClassifiedAs(x,pain_f))>] -> PAINF TONE1 REL BODY FEELING
PAINF -> 'duḥkhendriyam'
TONE1 -> 'aśātā'
REL -> 'yā'
BODY -> 'kāyikī'
FEELING -> 'vedanā'
PLEASURE[SEM=<all x.((Feeling(x) & Bodily(x) & Agreeable(x)) -> ClassifiedAs(x,pleasure_f))>] -> PLEASUREF TONE2
PLEASUREF -> 'sukham'
TONE2 -> 'śātā'
THIRD[SEM=<all x.((Feeling(x) & Agreeable(x) & Mental(x) & AtLevel(x,third_dhyana)) -> ClassifiedAs(x,pleasure_f))>] -> DHYANA THIRDLEVEL BUT MENTAL THAT PLEASUREF2
DHYANA -> 'dhyāne'
THIRDLEVEL -> 'tṛtīye'
BUT -> 'tu'
MENTAL -> 'caitasī'
THAT -> 'sā'
PLEASUREF2 -> 'sukhendriyam'
```

```nltk-dep
'duḥkhendriyam' -> 'aśātā' | 'yā' | 'kāyikī' | 'vedanā'
'sukham' -> 'śātā'
'sukhendriyam' -> 'dhyāne' | 'tṛtīye' | 'tu' | 'caitasī' | 'sā'
```

| Span | Constituent | Result |
|---|---|---|
| [0, 5) | `PAIN` | disagreeable bodily feeling classified as Pain-Faculty |
| [5, 7) | `PLEASURE` | agreeable feeling with bodily subject resumed from prose |
| [7, 13) | `THIRD` | agreeable mental feeling qualified by the third dhyāna |
| [0, 13) | `S` | three scoped classification rules with shared agreeable-feeling reference |

## 5. Translation

### Literal Translation

> Pain-Faculty is whichever bodily feeling is disagreeable; pleasure is agreeable [bodily feeling]. But in the third dhyāna, that [agreeable feeling], mental, is Pleasure-Faculty.

### Bhāṣya-informed study translation

> Pain-Faculty is whichever bodily feeling is disagreeable; Pleasure-Faculty is agreeable bodily feeling. But in the third dhyāna, that agreeable mental feeling is Pleasure-Faculty.

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
| pañca-vijñāna-kāya | five Cognition-groups | Bhāṣya: absent there; kāya is the group, not the body |

Sukha and duḥkha here are two of the five. Gladness and distress are the next verse.

## 8. Logical Determination

**Kārikā, derived.** The root SEM conjoins three scoped implications. The shared reference preserves the anaphora across the second and third clauses; it does not assert numerical identity between two feeling events. The last implication requires agreeable tone, mental mode, and third-dhyāna level together. The bodily restriction of the second clause is Bhāṣya-resolved ellipsis, not an additional Sanskrit token.

```nltk-sem
pain_classification : all x.((Feeling(x) & Bodily(x) & Disagreeable(x)) -> ClassifiedAs(x,pain_f))
pleasure_classification : all x.((Feeling(x) & Bodily(x) & Agreeable(x)) -> ClassifiedAs(x,pleasure_f))
third_level : all x.((Feeling(x) & Agreeable(x) & Mental(x) & AtLevel(x,third_dhyana)) -> ClassifiedAs(x,pleasure_f))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all x.((Feeling(x) & Bodily(x) & Disagreeable(x)) -> ClassifiedAs(x,pain_f)) & all x.((Feeling(x) & Bodily(x) & Agreeable(x)) -> ClassifiedAs(x,pleasure_f)) & all x.((Feeling(x) & Agreeable(x) & Mental(x) & AtLevel(x,third_dhyana)) -> ClassifiedAs(x,pleasure_f)))

# THEORY prose
# EXPECT prose T
all x.((Feeling(x) & Disagreeable(x)) -> Injurious(x))
all x.((Feeling(x) & Agreeable(x)) -> Supportive(x))
-FiveCognitionGroupsPresent(third_dhyana)
all x.((Feeling(x) & AtLevel(x,third_dhyana)) -> -Bodily(x))
(ClassifiedAs(bodily_pain,pain_f) & ClassifiedAs(bodily_pleasure,pleasure_f) & ClassifiedAs(third_pleasure,pleasure_f))

# THEORY rejected_unqualified_mental_pleasure
# EXPECT rejected_unqualified_mental_pleasure F
all x.((Feeling(x) & Agreeable(x) & Mental(x)) -> ClassifiedAs(x,pleasure_f))

# THEORY rejected_mental_becomes_bodily
# EXPECT rejected_mental_becomes_bodily F
all x.((Feeling(x) & AtLevel(x,third_dhyana) & ClassifiedAs(x,pleasure_f)) -> Bodily(x))

# THEORY rejected_all_feeling_is_agreeable
# EXPECT rejected_all_feeling_is_agreeable F
all x.(Feeling(x) -> Agreeable(x))
```

```nltk-valuation
pain_f => pain_faculty
pleasure_f => pleasure_faculty
third_dhyana => third_level
bodily_pain => bodily_pain_event
bodily_pleasure => bodily_pleasure_event
third_pleasure => third_pleasure_event
Feeling => {bodily_pain_event,bodily_pleasure_event,third_pleasure_event,other_mental_pleasure_event}
Bodily => {bodily_pain_event,bodily_pleasure_event}
Mental => {third_pleasure_event,other_mental_pleasure_event}
Disagreeable => {bodily_pain_event}
Agreeable => {bodily_pleasure_event,third_pleasure_event,other_mental_pleasure_event}
AtLevel => {(third_pleasure_event,third_level)}
ClassifiedAs => {(bodily_pain_event,pain_faculty),(bodily_pleasure_event,pleasure_faculty),(third_pleasure_event,pleasure_faculty)}
Injurious => {bodily_pain_event}
Supportive => {bodily_pleasure_event,third_pleasure_event,other_mental_pleasure_event}
FiveCognitionGroupsPresent => {}
```

The other mental-pleasure event is a counterexample to dropping the level restriction; its Faculty-name is left to 2.08. The prose states the absence of the five Cognition-groups as the reason bodily feeling is absent. The valuation checks those absences, not a general causal law from absence alone to Pleasure-Faculty. These are finite-model checks, not proofs.

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the verse translation): Pain is disagreeable bodily feeling. Pleasure is agreeable bodily feeling. The exception is narrow: in the third dhyāna the five cognition-groups are absent, so agreeable mental feeling takes the pleasure-faculty. Mental feeling is not thereby bodily.

2.03 assigned the feelings to defilement. 2.06 assigned them to the experience of engagement. This verse begins the internal cut.

Injurious and supportive are the commentary's glosses. They are not moral wholesomeness. Pain and pleasure are faculty-names. They are not every suffering and every happiness.

Sā resumes the agreeable feeling. It is not one bodily feeling turning into a mental entity. Absence of the five cognition-groups explains why the feeling is not bodily. It does not yet say why the name is pleasure rather than gladness. That is the next unit.

Eye through male is the range already treated. It is not a count of ten Form faculties. Mind is in that range. Life is deferred because dissociated. The five beginning with faith are deferred to the mental factors.

Interpretation: Faculty-classification requires the mode and level, not agreeable tone alone. The five Cognition-groups mediate the bodily case; their absence does not turn mental feeling into bodily feeling. Cognition joins and governs Perception and Conception without becoming identical to Mind or consciousness. Here the source establishes only the local absence of the five groups; the governing synthesis belongs to the Organon reading.

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
vak:AgreeableBodilyFeeling vak:classifiedAs vak:PleasureFaculty .
vak:ThirdDhyanaAgreeableMentalFeeling
    vak:classifiedAs vak:PleasureFaculty ;
    vak:hasMode vak:Mental ;
    vak:atLevel vak:ThirdDhyana .
vak:ThirdDhyana vak:lacks vak:FiveCognitionGroups .

organon:VAK_2_07_Interpretation
    organon:distinguishes vak:FeelingMode, vak:DhyanaLevel, vak:FacultyClassification .
```
