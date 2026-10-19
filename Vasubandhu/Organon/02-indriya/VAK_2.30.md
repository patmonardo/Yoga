# VAK_2.30 — The Indeterminate Counts

## 1. Sanskrit (Devanāgarī)

```sanskrit
निवृतेऽष्टादशान्यत्र द्वादशाव्याकृते मताः ।
मिद्धं सर्वाविरोधित्वाद्यत्र स्यादधिकं हि तत् ॥ २.३० ॥
```

## 2. Sanskrit (IAST)

```text
nivṛte 'ṣṭādaśānyatra dvādaśāvyākṛte matāḥ /
middhaṃ sarvāvirodhitvād yatra syād adhikaṃ hi tat // 2.30 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| nivṛte | loc. sg. n. | in the obscured |
| aṣṭādaśa | numeral, indeclinable use | eighteen |
| anyatra | adverb | in the other |
| dvādaśa | numeral, indeclinable use | twelve |
| avyākṛte | loc. sg. n. | in the indeterminate |
| matāḥ | nom. pl. m.; past passive participle | are accepted |
| middham | nom. sg. n. | torpor |
| sarva-avirodhitvāt | abl. sg. n.; compound | because incompatible with none |
| yatra syāt | relative adverb + 3 sg. optative | wherever it may occur |
| adhikam | neuter adjective used adverbially | additional |
| hi / tat | explanatory particle / nominative singular neuter pronoun | indeed / that [torpor], the additional factor |

Indeterminate is karmic. Not the unfixed of 2.27. Torpor is not sluggishness.

Desire-Realm scope is carried from the preceding counts. External
sandhi is opened; other means the unobscured indeterminate.

```text
# tokens: nivṛte aṣṭādaśa anyatra dvādaśa avyākṛte matāḥ middham sarvāvirodhitvāt yatra syāt adhikam hi tat
```

## 4. Grammar

The two base-count clauses share the indeterminate qualification.
The conditional relative clause restricts the increment to wherever
torpor occurs. Compatibility is the reason the increment can apply
across the previously stated cases, not a claim that torpor is
present in every one.

```nltk-fcfg
% start S
# tokens: nivṛte aṣṭādaśa anyatra dvādaśa avyākṛte matāḥ middham sarvāvirodhitvāt yatra syāt adhikam hi tat
S[SEM=<(?counts & ?increment)>] -> COUNTS[SEM=?counts] TORPORCLAUSE[SEM=?increment]
COUNTS[SEM=<(BaseCount(obscured,?a) & BaseCount(unobscured,?b))>] -> OBSCURED[CASE=loc] EIGHTEEN[CNT=18,SEM=?a] OTHER[REF=unobscured] TWELVE[CNT=12,SEM=?b] INDETERMINATE[CASE=loc] ACCEPTED[CASE=nom,NUM=pl]
TORPORCLAUSE[SEM=<(CompatibleWithStatedCases(torpor) & all c.((StatedCase(c) & TorporPresent(c)) -> AddsOne(c,torpor)))>] -> TORPOR[CASE=nom] REASON[CASE=abl,READING=compatibility] WHERE[READING=conditional] MAY[MOOD=opt] ADDITION[MODE=plus_one] INDEED THAT[REF=torpor]
OBSCURED[CASE=loc] -> 'nivṛte'
EIGHTEEN[CNT=18,SEM=<eighteen>] -> 'aṣṭādaśa'
OTHER[REF=unobscured] -> 'anyatra'
TWELVE[CNT=12,SEM=<twelve>] -> 'dvādaśa'
INDETERMINATE[CASE=loc] -> 'avyākṛte'
ACCEPTED[CASE=nom,NUM=pl] -> 'matāḥ'
TORPOR[CASE=nom] -> 'middham'
REASON[CASE=abl,READING=compatibility] -> 'sarvāvirodhitvāt'
WHERE[READING=conditional] -> 'yatra'
MAY[MOOD=opt] -> 'syāt'
ADDITION[MODE=plus_one] -> 'adhikam'
INDEED -> 'hi'
THAT[REF=torpor] -> 'tat'
```

```nltk-dep
'matāḥ' -> 'nivṛte' | 'aṣṭādaśa' | 'anyatra' | 'dvādaśa' | 'avyākṛte'
'syāt' -> 'middham' | 'sarvāvirodhitvāt' | 'yatra' | 'adhikam' | 'hi' | 'tat'
```

| Span | Constituent | Result |
|---|---|---|
| [0, 6) | `COUNTS` | obscured eighteen, unobscured twelve |
| [6, 13) | `TORPORCLAUSE` | compatible torpor adds one where present |
| [0, 13) | `S` | base counts and conditional increment |

## 5. Translation

### Literal Translation

> In obscured-indeterminate consciousness, there are eighteen; in the other
> indeterminate consciousness, twelve. Torpor, being incompatible with none,
> may be additional wherever it occurs.
### Bhāṣya-informed study translation

> In the Desire Realm, eighteen mental factors are accepted in
> obscured-indeterminate consciousness, and twelve in the other,
> unobscured-indeterminate consciousness. Torpor is compatible with all
> the previously stated cases and adds one wherever it occurs.
## 6. Philosophical Translation

> Obscured and unobscured are two indeterminate classes. View specializes. Torpor increments; it does not redefine the base.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| nivṛta-avyākṛta | obscured-indeterminate | afflicted, not unwholesome |
| anivṛta-avyākṛta | unobscured-indeterminate | the other |
| satkāya-dṛṣṭi | view of a self in the Bases | named; not defined here |
| antagrāha-dṛṣṭi | extreme view | named; not defined here |
| bahirdeśaka | outer-region teachers | the attributed thirteen |
| middha | torpor | not styāna |
| avirodha | non-opposition | admissibility, not occurrence |

## 8. Logical Determination

**Kārikā, derived; local scope resolved from the Bhāṣya.**
BaseCount does not overwrite a count after an addition. AddsOne
records the increment; actual member counts are checked separately.

```nltk-sem
eighteen_count : \c.BaseCount(c,eighteen)
twelve_count : \c.BaseCount(c,twelve)
conditional_increment : \c.((StatedCase(c) & TorporPresent(c)) -> AddsOne(c,torpor))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((BaseCount(obscured,eighteen) & BaseCount(unobscured,twelve)) & (CompatibleWithStatedCases(torpor) & all c.((StatedCase(c) & TorporPresent(c)) -> AddsOne(c,torpor))))

# THEORY prose_inventory
# EXPECT prose_inventory T
all x.(ObscuredMember(x) <-> (UniversalKind(x) | AfflictionKind(x) | ExaminationKind(x)))
all x.(UnobscuredMember(x) <-> (UniversalKind(x) | ExaminationKind(x)))
all x.(RegionalRegretMember(x) <-> (UnobscuredMember(x) | x = regret))
all x.(TorporUnobscuredMember(x) <-> (UnobscuredMember(x) | x = torpor))

# THEORY rejected_compatibility_is_presence
# EXPECT rejected_compatibility_is_presence F
all c.(StatedCase(c) -> TorporPresent(c))

# THEORY rejected_equal_thirteens_equal_members
# EXPECT rejected_equal_thirteens_equal_members F
all x.(RegionalRegretMember(x) <-> TorporUnobscuredMember(x))

# THEORY rejected_obscured_has_unwholesome_pair
# EXPECT rejected_obscured_has_unwholesome_pair F
all x.(UnwholesomeKind(x) -> ObscuredMember(x))
```

```nltk-valuation
obscured => obscured_base
unobscured => unobscured_base
eighteen => count_eighteen
twelve => count_twelve
torpor => torpor_kind
regret => regret_kind
BaseCount => {(obscured_base,count_eighteen),(unobscured_base,count_twelve)}
CompatibleWithStatedCases => {torpor_kind}
StatedCase => {obscured_base,unobscured_base,obscured_with_torpor,unobscured_with_torpor,wholesome_with_torpor,wholesome_regret_with_torpor}
TorporPresent => {obscured_with_torpor,unobscured_with_torpor,wholesome_with_torpor,wholesome_regret_with_torpor}
AddsOne => {(obscured_with_torpor,torpor_kind),(unobscured_with_torpor,torpor_kind),(wholesome_with_torpor,torpor_kind),(wholesome_regret_with_torpor,torpor_kind)}
UniversalKind => {feeling,volition,reflection,wish,contact,comprehension,mindfulness,attention,resolution,concentration}
AfflictionKind => {delusion,heedlessness,laziness,faithlessness,sluggishness,agitation}
ExaminationKind => {initial_examination,sustained_examination}
UnwholesomeKind => {shamelessness,lack_caution}
ObscuredMember => {feeling,volition,reflection,wish,contact,comprehension,mindfulness,attention,resolution,concentration,delusion,heedlessness,laziness,faithlessness,sluggishness,agitation,initial_examination,sustained_examination}
UnobscuredMember => {feeling,volition,reflection,wish,contact,comprehension,mindfulness,attention,resolution,concentration,initial_examination,sustained_examination}
RegionalRegretMember => {feeling,volition,reflection,wish,contact,comprehension,mindfulness,attention,resolution,concentration,initial_examination,sustained_examination,regret_kind}
TorporUnobscuredMember => {feeling,volition,reflection,wish,contact,comprehension,mindfulness,attention,resolution,concentration,initial_examination,sustained_examination,torpor_kind}
```

RegionalRegretMember belongs to the outer-region teachers' alternative,
not the unqualified base account. The two thirteen-member inventories
share twelve but differ in the added member. Tests also check
18 → 19, 22 → 23, and 23 → 24. The latter two are the prose's
explicit examples; the former and 12 → 13 apply its general rule.
The finite inventories check accounting, not universal occurrence
or the truth of the regional position.

## 9. Interpretive Note

**Translation note.** The commentary derives eighteen from the ten universal, six affliction-great-ground factors, vitarka, and vicāra; the view adds none. The unobscured-indeterminate count is the ten universal with vitarka and vicāra. Because torpor may be wholesome, unwholesome, or indeterminate, it may add one to either count.

The Desire Realm five are now counted. Wholesome was 2.28. Unwholesome was 2.29. These two close the set. Higher levels are the next transition.

The views are named, not defined. No later account is imported. The alternative on regret is not decided. No school beyond outer-region teachers. The region is not identified.

And so forth leaves the rule open. It does not put every alternative in one consciousness.

In the Organon reading, Cognition governs Perception and Conception
without collapsing into consciousness or Mind. A view qualifies
already-counted discriminative comprehension; torpor is a distinct
addition where present. Ethical range, identity, and actual
occurrence cannot be replaced by a bare numeral.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_30
    a vak:Karika ;
    rdfs:label "VAK 2.30" ;
    vak:hasTopic vak:IndeterminateCount ;
    vak:belongsTo vak:Indriyanirdesa .

vak:ObscuredIndeterminate vak:hasCount 18 .
vak:UnobscuredIndeterminate vak:hasCount 12 .
vak:Torpor vak:countedOnlyWhenOccurrent true .

organon:VAK_2_30_Interpretation
    organon:distinguishes vak:Compatibility, vak:ActualPresence,
        vak:AttributedAlternative, vak:ConditionalIncrement .
```
