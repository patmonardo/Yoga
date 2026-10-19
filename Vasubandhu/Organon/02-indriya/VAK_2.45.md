# VAK_2.45 — Life and the Marks

## 1. Sanskrit (Devanāgarī)

```sanskrit
आयुर्जीवितमाधार ऊष्मविज्ञानयोर्हि यः ।
लक्षणानि पुनर्जातिर्जरा स्थितिरनित्यता ॥ २.४५ ॥
```

## 2. Sanskrit (IAST)

```text
āyur jīvitam ādhāra ūṣmavijñānayor hi yaḥ /
lakṣaṇāni punar jātir jarā sthitir anityatā // 2.45 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| āyuḥ | nom. sg. n. | lifespan |
| jīvitam | nom. sg. n. | life |
| ādhāraḥ | nom. sg. m. | support |
| ūṣma-vijñānayoḥ | gen. dual m.; compound | of warmth and Cognition |
| hi | particle | explanatory emphasis |
| yaḥ | nom. sg. m.; relative pronoun | that which supports them; refers back to lifespan |
| lakṣaṇāni | nom. pl. n. | marks |
| punar | adverb | in turn; changes topic |
| jātiḥ | nom. sg. f. | arising |
| jarā | nom. sg. f. | aging |
| sthitiḥ | nom. sg. f. | persistence |
| anityatā | nom. sg. f. | impermanence |

Verse order puts aging before persistence. The commentary's genetic order is arising, persistence, aging, impermanence. Both stay.

The verse's dual is corrected to *ūṣmavijñānayoḥ* from the
running witness; the inherited display omitted *na*. The support
term is *ādhāra*, not an occurrence of *āśraya*.

```text
# tokens: āyuḥ jīvitam ādhāraḥ ūṣmavijñānayoḥ hi yaḥ lakṣaṇāni punar jātiḥ jarā sthitiḥ anityatā
```
## 4. Grammar

The first clause identifies life with lifespan and explains it
as support of warmth and Cognition. It does not settle whether
this support must be a distinct real entity. The second clause
lists all four marks together, not alternative definitions.
The prose's death classifications and three-versus-four debate
are not inserted into the verse's grammatical root.

```nltk-fcfg
% start S
# tokens: āyuḥ jīvitam ādhāraḥ ūṣmavijñānayoḥ hi yaḥ lakṣaṇāni punar jātiḥ jarā sthitiḥ anityatā
S[SEM=<(?life & ?marks)>] -> LIFE[SEM=?life] MARKS[SEM=?marks]
LIFE[SEM=<(Identifies(life,lifespan) & Supports(lifespan,warmth) & Supports(lifespan,cognition))>] -> LIFESPAN[CASE=nom] LIFEWORD[CASE=nom] SUPPORT[CASE=nom] PAIR[CASE=gen,NUM=du,CNT=2] EXPLANATORY RELATIVE[CASE=nom,REF=lifespan]
MARKS[SEM=<(Mark(arising) & Mark(aging) & Mark(persistence) & Mark(impermanence))>] -> MARKWORD[CASE=nom,NUM=pl] TRANSITION ARISING[CASE=nom] AGING[CASE=nom] PERSISTENCE[CASE=nom] IMPERMANENCE[CASE=nom]
LIFESPAN[CASE=nom] -> 'āyuḥ'
LIFEWORD[CASE=nom] -> 'jīvitam'
SUPPORT[CASE=nom] -> 'ādhāraḥ'
PAIR[CASE=gen,NUM=du,CNT=2] -> 'ūṣmavijñānayoḥ'
EXPLANATORY -> 'hi'
RELATIVE[CASE=nom,REF=lifespan] -> 'yaḥ'
MARKWORD[CASE=nom,NUM=pl] -> 'lakṣaṇāni'
TRANSITION -> 'punar'
ARISING[CASE=nom] -> 'jātiḥ'
AGING[CASE=nom] -> 'jarā'
PERSISTENCE[CASE=nom] -> 'sthitiḥ'
IMPERMANENCE[CASE=nom] -> 'anityatā'
```

```nltk-dep
'jīvitam' -> 'āyuḥ' | 'ādhāraḥ'
'ādhāraḥ' -> 'ūṣmavijñānayoḥ' | 'hi' | 'yaḥ'
'lakṣaṇāni' -> 'punar' | 'jātiḥ' | 'jarā' | 'sthitiḥ' | 'anityatā'
```

The two constituent lengths are six and six. The marks remain
in verse order even though their explanatory sequence differs.

## 5. Translation

### Literal Translation

> Life is lifespan, the support of warmth and Cognition. The marks are
> arising, aging, persistence, and impermanence.
### Bhāṣya-informed study translation

> Life is lifespan, the support of warmth and Cognition. The marks, in turn,
> are arising, aging, persistence, and impermanence.
## 6. Philosophical Translation

> The support-role of lifespan is argued over: a distinct entity
> and a karma-projected duration are competing explanations.
> The four marks then introduce a second inquiry. Neither the
> duration account nor the later stream account is silently made
> the verse's settled ontology.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| jīvita | life | lifespan; disputed real |
| ādhāra | support | of warmth and Cognition |
| nikāya-sabhāga | group same-class | what karma projects a duration for |
| sthiti-kālāvedha | projected duration | the alternative life account |
| jāti | arising | beginning |
| sthiti | persistence | the continuation |
| jarā | aging | earlier and later differ |
| anityatā | impermanence | interruption |
| anulakṣaṇa | secondary mark | begins the next verse's argument, not this verse's enumeration |

## 8. Logical Determination

```nltk-sem
life : (Identifies(life,lifespan) & Supports(lifespan,warmth) & Supports(lifespan,cognition))
marks : (Mark(arising) & Mark(aging) & Mark(persistence) & Mark(impermanence))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((Identifies(life,lifespan) & Supports(lifespan,warmth) & Supports(lifespan,cognition)) & (Mark(arising) & Mark(aging) & Mark(persistence) & Mark(impermanence)))

# THEORY death_four_alternatives
# EXPECT death_four_alternatives T
LifespanExhausted(lifespan_only) & -MeritExhausted(lifespan_only)
-LifespanExhausted(merit_only) & MeritExhausted(merit_only)
LifespanExhausted(both_exhausted) & MeritExhausted(both_exhausted)
-LifespanExhausted(neither_exhausted) & -MeritExhausted(neither_exhausted) & FailureToAvoidHarm(neither_exhausted)

# THEORY reported_life_accounts
# EXPECT reported_life_accounts T
DistinctLifeEntity(real_entity_account) & -DistinctLifeEntity(projected_duration_account)
ProjectedDuration(projected_duration_account) & AllowsUntimelyDeath(kashmir_explanation)

# THEORY rejected_marks_are_one_alternative_only
# EXPECT rejected_marks_are_one_alternative_only F
all x y.((Mark(x) & Mark(y)) -> (x = y))

# THEORY rejected_all_death_exhausts_lifespan
# EXPECT rejected_all_death_exhausts_lifespan F
all x.(DeathCase(x) -> LifespanExhausted(x))
```

```nltk-valuation
life => life_term
lifespan => lifespan_term
warmth => warmth_term
cognition => cognition_term
arising => arising_mark
aging => aging_mark
persistence => persistence_mark
impermanence => impermanence_mark
lifespan_only => lifespan_only_case
merit_only => merit_only_case
both_exhausted => both_exhausted_case
neither_exhausted => neither_exhausted_case
real_entity_account => real_entity_position
projected_duration_account => projected_duration_position
kashmir_explanation => kashmir_explanation_position
Identifies => {(life_term,lifespan_term)}
Supports => {(lifespan_term,warmth_term),(lifespan_term,cognition_term)}
Mark => {arising_mark,aging_mark,persistence_mark,impermanence_mark}
DeathCase => {lifespan_only_case,merit_only_case,both_exhausted_case,neither_exhausted_case}
LifespanExhausted => {lifespan_only_case,both_exhausted_case}
MeritExhausted => {merit_only_case,both_exhausted_case}
FailureToAvoidHarm => {neither_exhausted_case}
DistinctLifeEntity => {real_entity_position}
ProjectedDuration => {projected_duration_position}
AllowsUntimelyDeath => {kashmir_explanation_position}
```

The four death cases are class-level alternatives, not medical
diagnoses or causes inferred for actual individuals. The two
exhaustion axes distinguish the cases; relinquishing lifespan
is assigned by the prose to the first rather than a fifth case.
The model indexes the life accounts without settling their
ontology. Three scriptural marks and the competing explanations
for persistence are kept in the Bhāṣya argument, not reduced
to “three equals four.”

## 9. Interpretive Note

**Translation note.** The commentary says lifespan, warmth, and Cognition leave the body, which lies cast aside like senseless wood. It rejects mutual support as the explanation of lifespan and considers karma as projecting duration; the relation of karma and Cognition remains part of the discussion, not the verse translation.

The life discussion continues through 75.18, not merely the opening
support explanation. The marks discussion follows through 76.09;
secondary marks begin the next verse's argument. The damaged list
of protected lives is retained without speculative restoration.

In the Organon reading, Cognition joins and governs Perception and
Conception and guides the Dharma Base, remaining distinct from
consciousness and Mind. A support-role does not by itself establish
an extra substance. Duration, interruption, and the marks of a
conditioned course must be distinguished before competing accounts
of their reality can be assessed.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_45 a vak:Karika ; vak:hasTopic vak:Life, vak:Marks .
vak:LifeEntity vak:settled false .
```
