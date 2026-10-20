# VAK_2.08 — Gladness, Distress, One Neutral

## 1. Sanskrit (Devanāgarī)

```sanskrit
अन्यत्र सा सौमनस्यमशाता चैतसी पुनः ।
दौर्मनस्यमुपेक्षा तु मध्या उभयी अविकल्पनात् ॥ २.८ ॥
```

## 2. Sanskrit (IAST)

```text
anyatra sā saumanasyam aśātā caitasī punaḥ /
daurmanasyam upekṣā tu madhyā ubhayī avikalpanāt // 2.8 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| anyatra | indeclinable | elsewhere; outside the third dhyāna |
| sā | nominative singular feminine demonstrative | that agreeable mental feeling, resumed from 2.07 |
| saumanasyam | nominative singular neuter noun | gladness, used as the Faculty-name |
| aśātā | nominative singular feminine adjective | disagreeable; qualifies the supplied feeling |
| caitasī | nominative singular feminine adjective | mental; qualifies the supplied feeling |
| punaḥ | indeclinable | in turn |
| daurmanasyam | nominative singular neuter noun | distress, used as the Faculty-name |
| upekṣā | nominative singular feminine noun | neutral feeling, the Faculty being defined |
| tu | particle | but |
| madhyā | nominative singular feminine adjective | middle; neither agreeable nor disagreeable feeling |
| ubhayī | nominative singular feminine adjective | of both kinds; bodily and mental |
| avikalpanāt | ablative singular neuter action noun | because of non-differentiation; gives the reason for one Faculty |

Ubhayī is not two neutral faculties. One faculty includes bodily and mental.

**Grammar tokens.** External sandhi is opened. The anaphor resumes
agreeable mental feeling from 2.07; its resolution and the supplied
feeling in the distress clause are marked `SUPPLIED=prose`.

```text
# tokens: anyatra sā saumanasyam aśātā caitasī punaḥ daurmanasyam upekṣā tu madhyā ubhayī avikalpanāt
```

## 4. Grammar

The first clause classifies the resumed agreeable mental feeling
elsewhere than the third dhyāna. The second supplies feeling as the
subject of disagreeable and mental. The third defines neutral feeling
and gives the reason bodily and mental modes count as one Faculty.
The causal ablative gives the reason for one Faculty in the respect
of remaining neutral. `CNT=2` counts bodily and mental modes, not
Faculties; the two modes are not identical in every respect.

```nltk-fcfg
% start S
# tokens: anyatra sā saumanasyam aśātā caitasī punaḥ daurmanasyam upekṣā tu madhyā ubhayī avikalpanāt
S[SEM=<(?glad & ?distress & ?neutral)>] -> GLAD[SEM=?glad] DISTRESS[SEM=?distress] NEUTRAL[SEM=?neutral]
GLAD[SUPPLIED=prose,SEM=<all x.((?resumed(x) & ?where(x)) -> ?faculty(x))>] -> ELSEWHERE[SCOPE=outside_third,SEM=?where] THAT[CASE=nom,NUM=sg,GEN=f,REF=agreeable_mental,SEM=?resumed] GLADF[CASE=nom,NUM=sg,GEN=n,SEM=?faculty]
DISTRESS[SUPPLIED=prose,SEM=<all x.((Feeling(x) & ?tone(x) & ?mental(x)) -> ?faculty(x))>] -> DISAGREEABLE[CASE=nom,NUM=sg,GEN=f,SEM=?tone] MENTAL[CASE=nom,NUM=sg,GEN=f,SEM=?mental] AGAIN DISTRESSF[CASE=nom,NUM=sg,GEN=n,SEM=?faculty]
NEUTRAL[SEM=<(all x.((Feeling(x) & ?middle(x) & (Bodily(x) | Mental(x))) -> ?faculty(x)) & ?both(neutral_f) & ?reason(neutral_f))>] -> NEUTRALF[CASE=nom,NUM=sg,GEN=f,SEM=?faculty] BUT MIDDLE[CASE=nom,NUM=sg,GEN=f,SEM=?middle] BOTH[CASE=nom,NUM=sg,GEN=f,CNT=2,SEM=?both] REASON[CASE=abl,RESPECT=remaining_neutral,SEM=?reason]
ELSEWHERE[SCOPE=outside_third,SEM=<\x.Elsewhere(x)>] -> 'anyatra'
THAT[CASE=nom,NUM=sg,GEN=f,REF=agreeable_mental,SEM=<\x.(Feeling(x) & Agreeable(x) & Mental(x))>] -> 'sā'
GLADF[CASE=nom,NUM=sg,GEN=n,SEM=<\x.ClassifiedAs(x,gladness_f)>] -> 'saumanasyam'
DISAGREEABLE[CASE=nom,NUM=sg,GEN=f,SEM=<\x.Disagreeable(x)>] -> 'aśātā'
MENTAL[CASE=nom,NUM=sg,GEN=f,SEM=<\x.Mental(x)>] -> 'caitasī'
AGAIN -> 'punaḥ'
DISTRESSF[CASE=nom,NUM=sg,GEN=n,SEM=<\x.ClassifiedAs(x,distress_f)>] -> 'daurmanasyam'
NEUTRALF[CASE=nom,NUM=sg,GEN=f,SEM=<\x.ClassifiedAs(x,neutral_f)>] -> 'upekṣā'
BUT -> 'tu'
MIDDLE[CASE=nom,NUM=sg,GEN=f,SEM=<\x.(-Agreeable(x) & -Disagreeable(x))>] -> 'madhyā'
BOTH[CASE=nom,NUM=sg,GEN=f,CNT=2,SEM=<\f.(HasMode(f,bodily_mode) & HasMode(f,mental_mode))>] -> 'ubhayī'
REASON[CASE=abl,RESPECT=remaining_neutral,SEM=<\f.UnifiedBecause(f,non_differentiation)>] -> 'avikalpanāt'
```

```nltk-dep
'saumanasyam' -> 'anyatra' | 'sā'
'daurmanasyam' -> 'aśātā' | 'caitasī' | 'punaḥ'
'upekṣā' -> 'tu' | 'madhyā' | 'ubhayī' | 'avikalpanāt'
```

| Span | Constituent | Result |
|---|---|---|
| [0, 3) | `GLAD` | resumed agreeable mental feeling, scoped by elsewhere |
| [3, 7) | `DISTRESS` | disagreeable mental feeling classified as distress |
| [7, 12) | `NEUTRAL` | middle tone, both modes, one Faculty for the stated reason |
| [0, 12) | `S` | conjunction of the three determinations |

## 5. Translation

### Literal Translation

> Elsewhere, that is gladness. Disagreeable mental [feeling], in turn, is
> distress. Neutral feeling, however, is the middle, of both kinds, because
> of non-differentiation.

### Bhāṣya-informed study translation

> Elsewhere than the third dhyāna, that agreeable mental feeling is
> Gladness-Faculty; disagreeable mental feeling, in turn, is
> Distress-Faculty. Neutral-Feeling Faculty, however, is neither agreeable
> nor disagreeable feeling, both bodily and mental, undivided because
> there is no difference with respect to remaining neutral.

## 6. Philosophical Translation

> Bodily and mental modes do not alone decide the Faculty-count. Pleasure
> and pain are differentiated; neutral feeling remains one Faculty in
> both modes, with respect to its neutral function.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| saumanasya | gladness | agreeable mental feeling outside the third dhyāna |
| prīti | rapture | identified here with gladness; absent in the third dhyāna |
| daurmanasya | distress | disagreeable mental feeling |
| upekṣā | neutral feeling | the middle; not every equanimity |
| madhyā | middle | neither agreeable nor disagreeable |
| ubhayī | of both kinds | bodily and mental; one faculty |
| vikalpana | differentiation | how mental pleasure and pain mostly arise; not prajñā |
| avikalpana | non-differentiation | why neutral feeling is one |
| viṣaya-vaśa | force of the Condition | bodily pleasure and pain, even in an arhat; not Object |
| svarasena | in its own course | how neutral feeling arises |
| upekṣaṇa | remaining neutral | the respect in which the modes do not differ |

## 8. Logical Determination

**Kārikā, derived.** The SEM resolves the resumed feeling from 2.07,
classifies distress, and assigns both neutral modes to one Faculty for
the stated reason. The Bhāṣya specifies elsewhere as the Desire-realm
and first two dhyānas. It then gives two distinct explanations for the neutral
count: arising without differentiation and no difference in the
effect of remaining neutral. Neither the ordinal third nor that
threefold specification is an extra token in this verse.

```nltk-sem
resumed_feeling : \x.(Feeling(x) & Agreeable(x) & Mental(x))
middle_tone : \x.(-Agreeable(x) & -Disagreeable(x))
one_neutral_faculty : \f.UnifiedBecause(f,non_differentiation)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all x.((Feeling(x) & Agreeable(x) & Mental(x) & Elsewhere(x)) -> ClassifiedAs(x,gladness_f)) & all x.((Feeling(x) & Disagreeable(x) & Mental(x)) -> ClassifiedAs(x,distress_f)) & all x.((Feeling(x) & -Agreeable(x) & -Disagreeable(x) & (Bodily(x) | Mental(x))) -> ClassifiedAs(x,neutral_f)) & HasMode(neutral_f,bodily_mode) & HasMode(neutral_f,mental_mode) & UnifiedBecause(neutral_f,non_differentiation))

# THEORY prose_levels
# EXPECT prose_levels T
all x.((Feeling(x) & Mental(x)) -> (Elsewhere(x) <-> (AtLevel(x,desire_realm) | AtLevel(x,first_dhyana) | AtLevel(x,second_dhyana))))
all x.((Feeling(x) & Agreeable(x) & Mental(x) & AtLevel(x,third_dhyana)) -> (ClassifiedAs(x,pleasure_f) & -ClassifiedAs(x,gladness_f)))
DispassionToward(third_dhyana,rapture) & LocalIdentification(rapture,gladness_f)

# THEORY prose_arising
# EXPECT prose_arising T
ForMostPartThrough(mental_pleasure_pain,differentiation) & Through(bodily_pleasure_pain,condition_force) & PossibleFor(bodily_pleasure_pain,arhat)
ArisesWithoutDifferentiating(neutral_f) & UnifiedBecause(neutral_f,non_differentiation)

# THEORY prose_effect
# EXPECT prose_effect T
DifferentSupport(bodily_pleasure,mental_pleasure) & DifferentInjury(bodily_pain,mental_pain)
SameInRemainingNeutral(bodily_neutral,mental_neutral) & ClassifiedAs(bodily_neutral,neutral_f) & ClassifiedAs(mental_neutral,neutral_f)

# THEORY rejected_gladness_without_level_restriction
# EXPECT rejected_gladness_without_level_restriction F
all x.((Feeling(x) & Agreeable(x) & Mental(x)) -> ClassifiedAs(x,gladness_f))

# THEORY rejected_neutral_is_mental_only
# EXPECT rejected_neutral_is_mental_only F
all x.(ClassifiedAs(x,neutral_f) -> Mental(x))

# THEORY rejected_every_mental_feeling_neutral
# EXPECT rejected_every_mental_feeling_neutral F
all x.((Feeling(x) & Mental(x)) -> ClassifiedAs(x,neutral_f))
```

```nltk-valuation
gladness_f => gladness_faculty
distress_f => distress_faculty
neutral_f => neutral_faculty
pleasure_f => pleasure_faculty
bodily_mode => bodily
mental_mode => mental
non_differentiation => non_difference_in_remaining_neutral
desire_realm => desire_level
first_dhyana => first_level
second_dhyana => second_level
third_dhyana => third_level
rapture => rapture_kind
mental_pleasure_pain => mental_pleasure_pain_class
bodily_pleasure_pain => bodily_pleasure_pain_class
bodily_pleasure => bodily_pleasure_case
mental_pleasure => mental_pleasure_case
bodily_pain => bodily_pain_case
mental_pain => mental_pain_case
bodily_neutral => bodily_neutral
mental_neutral => mental_neutral
differentiation => differentiation_process
condition_force => force_of_condition
arhat => arhat_person
Feeling => {desire_gladness,first_gladness,second_gladness,third_pleasure,mental_distress,bodily_neutral,mental_neutral}
Agreeable => {desire_gladness,first_gladness,second_gladness,third_pleasure}
Disagreeable => {mental_distress}
Mental => {desire_gladness,first_gladness,second_gladness,third_pleasure,mental_distress,mental_neutral}
Bodily => {bodily_neutral}
Elsewhere => {desire_gladness,first_gladness,second_gladness}
AtLevel => {(desire_gladness,desire_level),(first_gladness,first_level),(second_gladness,second_level),(third_pleasure,third_level)}
ClassifiedAs => {(desire_gladness,gladness_faculty),(first_gladness,gladness_faculty),(second_gladness,gladness_faculty),(third_pleasure,pleasure_faculty),(mental_distress,distress_faculty),(bodily_neutral,neutral_faculty),(mental_neutral,neutral_faculty)}
HasMode => {(neutral_faculty,bodily),(neutral_faculty,mental)}
UnifiedBecause => {(neutral_faculty,non_difference_in_remaining_neutral)}
DispassionToward => {(third_level,rapture_kind)}
LocalIdentification => {(rapture_kind,gladness_faculty)}
ForMostPartThrough => {(mental_pleasure_pain_class,differentiation_process)}
Through => {(bodily_pleasure_pain_class,force_of_condition)}
PossibleFor => {(bodily_pleasure_pain_class,arhat_person)}
ArisesWithoutDifferentiating => {neutral_faculty}
DifferentSupport => {(bodily_pleasure_case,mental_pleasure_case)}
DifferentInjury => {(bodily_pain_case,mental_pain_case)}
SameInRemainingNeutral => {(bodily_neutral,mental_neutral)}
```

`ForMostPartThrough` records the prose's qualified claim; it does not
derive a universal causal rule or test a statistical proportion.
`DifferentSupport` and `DifferentInjury` keep the two effects apart;
`SameInRemainingNeutral` is restricted to the neutral function, not
identity of bodily and mental modes. `LocalIdentification` records the
stated identification of rapture with gladness without equating their
predicates across the corpus. The finite model tests these claims, not
the causal sufficiency of the stated reasons.

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the
verse translation): Elsewhere, outside the third dhyāna, that agreeable
mental feeling is gladness. Disagreeable mental feeling, in turn, is
distress. Neutral feeling, neither agreeable nor disagreeable, is the
middle; it is of both kinds, bodily and mental, yet one faculty, because
in remaining neutral there is no difference between them.

2.07 left the name. This verse gives it. Elsewhere is specified: desire realm, first dhyāna, second dhyāna. Absence of the five cognition-groups explained why the third-dhyāna feeling is mental. Dispassion toward rapture explains why it is not gladness. Rapture is gladness is the local statement. It is not a rule for every text.

For the most part stays. Differentiation is not every mental pleasure or pain, and it is not affliction. The arhat may still have bodily pleasure and pain. The sentence does not say the arhat has no thought.

Neutral feeling arises in its own course. That is not the unconditioned, and it is not an advanced attainment by this sentence alone. Ubhayī keeps the modes. One faculty is the count, not the erasure of bodily and mental.

Interpretation: the rule of classification is sensitive to both level
and operation. Neutral feeling's one-Faculty status preserves its two
modes rather than eliminating their distinction. Cognition governs
Perception and Conception without collapsing into Mind or consciousness;
the distinction between bodily and mental feeling is not a division
between having and lacking Cognition.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_08
    a vak:Karika ;
    rdfs:label "VAK 2.08" ;
    vak:hasTopic vak:Gladness, vak:Distress, vak:NeutralFeeling ;
    vak:belongsTo vak:Indriyanirdesa .

vak:Gladness vak:isAgreeableMentalFeeling true ;
    vak:atLevel vak:DesireRealm, vak:FirstDhyana, vak:SecondDhyana .
vak:VAK_2_08 vak:locallyIdentifiesRaptureWith vak:Gladness .
vak:Distress vak:isDisagreeableMentalFeeling true .
vak:NeutralFeeling vak:includes vak:Bodily, vak:Mental ;
    vak:oneFacultyBecause vak:NonDifferenceInRemainingNeutral .

organon:VAK_2_08_Interpretation
    organon:distinguishes vak:FeelingMode, vak:DhyanaLevel, vak:FacultyCount .
```
