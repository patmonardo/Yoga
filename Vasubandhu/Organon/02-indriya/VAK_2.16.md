# VAK_2.16 — Fruits Through Faculties

## 1. Sanskrit (Devanāgarī)

```sanskrit
क्रममृत्यौ तु चत्वारि शुभे सर्वत्र पञ्च च ।
नवाप्तिरन्त्यफलयोः सप्ताष्टनवभिर्द्वयोः ॥ २.१६ ॥
```

## 2. Sanskrit (IAST)

```text
kramamṛtyau tu catvāri śubhe sarvatra pañca ca /
navāptir antyaphalayoḥ saptāṣṭanavabhir dvayoḥ // 2.16 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| krama-mṛtyau | locative singular masculine compound | in gradual death; continues 2.15 |
| tu | contrastive particle | however |
| catvāri | accusative plural neuter numeral | four [Faculties], under the carried cessation predicate |
| śubhe | locative singular adjective, substantival | with wholesome [consciousness], as the Bhāṣya specifies |
| sarvatra | indeclinable adverb | everywhere; in each stated death case |
| pañca | cardinal numeral, accusative plural in context | five [Faculties] |
| ca | additive particle | and; five in addition, not a replacement count |
| nava-āptiḥ | nominative singular feminine compound | attainment through nine [Faculties] |
| antya-phalayoḥ | genitive dual neuter compound | of the two extreme fruits, first and last |
| sapta-aṣṭa-navabhiḥ | instrumental plural numeral compound | through seven, eight, or nine [Faculties] |
| dvayoḥ | genitive dual numeral, substantival | of the two [middle fruits] |

Antya is the extremes of the four, stream-entry and arhatship, not the last two in time. The instrument is faculties. The fruit is not the set.

**Grammar tokens.** External sandhi is opened. Numeral compounds remain
single tokens; the semantic projection expands their counts. The death
clauses and the new fruit inquiry remain separate constituents.

```text
# tokens: kramamṛtyau tu catvāri śubhe sarvatra pañca ca nava-āptiḥ antyaphalayoḥ sapta-aṣṭa-navabhiḥ dvayoḥ
```

## 4. Grammar

The first two clauses complete the death count. The locative wholesome
is resolved by the prose as wholesome consciousness; and adds five.
The adverb `sarvatra` scopes the addition over each death context
established in 2.15; it is not an unbound truth flag.
The next nominative is attainment, with the dual extreme-fruit phrase
specifying whose attainment. The final instrumental supplies three
alternative counts for the other two fruits. The eleven-person
discussion belongs to the next verse's opening, not this token stream.

```nltk-fcfg
% start S
# tokens: kramamṛtyau tu catvāri śubhe sarvatra pañca ca nava-āptiḥ antyaphalayoḥ sapta-aṣṭa-navabhiḥ dvayoḥ
S[SEM=<(?gradual & ?wholesome & ?extreme & ?middle)>] -> GRADUAL[SEM=?gradual] WHOLESOME[SEM=?wholesome] EXTREME[SEM=?extreme] MIDDLE[SEM=?middle]
GRADUAL[SEM=<TerminalCount(?case,?count)>] -> GRADUALCASE[CASE=loc,SEM=?case] BUT FOUR[CNT=4,SEM=?count]
WHOLESOME[SEM=<?every(\c.AdditionalCount(c,?count))>] -> WHOLESOMECASE[CASE=loc,QUALITY=wholesome] EVERYWHERE[SEM=?every] FIVE[CNT=5,SEM=?count] AND[SCOPE=addition]
EXTREME[SEM=<?count(?group)>] -> NINEATTAINMENT[CASE=nom,CNT=9,SEM=?count] EXTREMES[CASE=gen,NUM=du,CNT=2,SEM=?group]
MIDDLE[SEM=<?counts(?group)>] -> COUNTS[CASE=ins,COUNTS=seven_eight_nine,SEM=?counts] TWO[CASE=gen,NUM=du,CNT=2,REF=middle,SEM=?group]
GRADUALCASE[CASE=loc,SEM=<gradual_death>] -> 'kramamṛtyau'
BUT -> 'tu'
FOUR[CNT=4,SEM=<four>] -> 'catvāri'
WHOLESOMECASE[CASE=loc,QUALITY=wholesome] -> 'śubhe'
EVERYWHERE[SEM=<\P.all c.(TerminalContext(c) -> P(c))>] -> 'sarvatra'
FIVE[CNT=5,SEM=<five>] -> 'pañca'
AND[SCOPE=addition] -> 'ca'
NINEATTAINMENT[CASE=nom,CNT=9,SEM=<\g.AttainmentCount(g,nine)>] -> 'nava-āptiḥ'
EXTREMES[CASE=gen,NUM=du,CNT=2,SEM=<extreme_fruits>] -> 'antyaphalayoḥ'
COUNTS[CASE=ins,COUNTS=seven_eight_nine,SEM=<\g.(AttainmentCount(g,seven) & AttainmentCount(g,eight) & AttainmentCount(g,nine))>] -> 'sapta-aṣṭa-navabhiḥ'
TWO[CASE=gen,NUM=du,CNT=2,REF=middle,SEM=<middle_fruits>] -> 'dvayoḥ'
```

```nltk-dep
'catvāri' -> 'kramamṛtyau' | 'tu'
'pañca' -> 'śubhe' | 'sarvatra' | 'ca'
'nava-āptiḥ' -> 'antyaphalayoḥ'
'sapta-aṣṭa-navabhiḥ' -> 'dvayoḥ'
```

| Span | Constituent | Result |
|---|---|---|
| [0, 3) | `GRADUAL` | gradual-death four |
| [3, 7) | `WHOLESOME` | five additional in every wholesome death case |
| [7, 9) | `EXTREME` | nine for the two extremes |
| [9, 11) | `MIDDLE` | seven/eight/nine for the middle two |
| [0, 11) | `S` | death completion followed by fruit inquiry |

## 5. Translation

### Literal Translation

> In gradual death, however, four. With a wholesome mind, everywhere five in
> addition. Attainment of the two extreme fruits is through nine. Of the
> two, through seven, eight, or nine.

### Bhāṣya-informed study translation

> In gradual death, however, four; with wholesome consciousness,
> everywhere five in addition. The two extreme fruits, stream-entry and
> arhatship, are attained through nine Faculties; the two middle fruits,
> once-returning and non-returning, through seven, eight, or nine.

## 6. Philosophical Translation

> Attainment is through the faculties that bring about and support disconnection. Eleven is successive possibility, not co-presence.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| śrāmaṇya-phala | fruit of the path | four |
| antya-phala | extreme fruit | stream-entry, arhatship |
| madhya | middle | once-returning, non-returning |
| ānantarya-mārga | uninterrupted Path | in stream-entry, bears “I shall know”; not a universal assignment |
| vimukti-mārga | Path of liberation | in stream-entry, bears the knowledge-faculty |
| visaṃyoga-prāpti | acquisition of disconnection | brought, then supported |
| ānupūrvika | sequential | seven or eight |
| vītarāga | already free from desire | nine |
| ekasya | of one person | the eleven |

## 8. Logical Determination

**Kārikā, derived.** The root SEM scopes the wholesome five over every
stated terminal context and preserves the two fruit groups. This
quantifier checks the addition against all six contexts modeled in 2.15.
Count alternatives are route-dependent, not three incompatible totals
for one event.

```nltk-sem
extreme_count : \g.AttainmentCount(g,nine)
middle_counts : \g.(AttainmentCount(g,seven) & AttainmentCount(g,eight) & AttainmentCount(g,nine))
wholesome_addition : all c.(TerminalContext(c) -> AdditionalCount(c,five))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(TerminalCount(gradual_death,four) & all c.(TerminalContext(c) -> AdditionalCount(c,five)) & AttainmentCount(extreme_fruits,nine) & AttainmentCount(middle_fruits,seven) & AttainmentCount(middle_fruits,eight) & AttainmentCount(middle_fruits,nine))

# THEORY prose_routes
# EXPECT prose_routes T
(ExtremeFruit(stream_entry) & ExtremeFruit(arhatship) & MiddleFruit(once_returning) & MiddleFruit(non_returning))
(RouteCount(sequential_mundane,seven) & RouteCount(sequential_supramundane,eight) & RouteCount(prior_dispassion,nine))
(RouteCount(sharp_mundane,eight) & RouteCount(sharp_supramundane,nine))
(OnPath(shall_know,stream_uninterrupted) & OnPath(knowledge,stream_liberation))
all x.(StreamNine(x) <-> (CommonSix(x) | x = neutral_f | x = shall_know | x = knowledge))

# THEORY cross_verse_eleven
# EXPECT cross_verse_eleven T
all x.(ArhatAttainment(x) -> (ByPerson(x,one_person) & exists y.(FeelingChoice(y) & UsesFeeling(x,y))))
all x.all y.all z.((ArhatAttainment(x) & UsesFeeling(x,y) & UsesFeeling(x,z)) -> (y = z))
(UsesFeeling(pleasure_attainment,pleasure_f) & UsesFeeling(gladness_attainment,gladness_f) & UsesFeeling(neutral_attainment,neutral_f))

# THEORY rejected_eleven_simultaneous
# EXPECT rejected_eleven_simultaneous F
exists x.(ArhatAttainment(x) & UsesFeeling(x,pleasure_f) & UsesFeeling(x,gladness_f) & UsesFeeling(x,neutral_f))

# THEORY rejected_all_mundane_middle_routes_seven
# EXPECT rejected_all_mundane_middle_routes_seven F
all x.(MundaneMiddleRoute(x) -> RouteCount(x,seven))

# THEORY rejected_same_count_same_composition
# EXPECT rejected_same_count_same_composition F
all x.(SequentialSupraEight(x) <-> SharpMundaneEight(x))
```

```nltk-valuation
gradual_death => gradual_case
extreme_fruits => extremes
middle_fruits => middles
four => count_four
five => count_five
seven => count_seven
eight => count_eight
nine => count_nine
stream_entry => stream_entry_fruit
arhatship => arhatship_fruit
once_returning => once_returning_fruit
non_returning => non_returning_fruit
sequential_mundane => sequential_mundane_route
sequential_supramundane => sequential_supra_route
prior_dispassion => prior_dispassion_route
sharp_mundane => sharp_mundane_route
sharp_supramundane => sharp_supra_route
shall_know => shall_know_faculty
knowledge => knowledge_faculty
neutral_f => neutral
pleasure_f => pleasure
gladness_f => gladness
stream_uninterrupted => stream_uninterrupted_path
stream_liberation => stream_liberation_path
one_person => person
pleasure_attainment => attainment_pleasure
gladness_attainment => attainment_gladness
neutral_attainment => attainment_neutral
TerminalContext => {formless_case,form_case,desire_none_case,desire_one_case,desire_both_case,gradual_case}
TerminalCount => {(gradual_case,count_four)}
AdditionalCount => {(formless_case,count_five),(form_case,count_five),(desire_none_case,count_five),(desire_one_case,count_five),(desire_both_case,count_five),(gradual_case,count_five)}
AttainmentCount => {(extremes,count_nine),(middles,count_seven),(middles,count_eight),(middles,count_nine)}
ExtremeFruit => {stream_entry_fruit,arhatship_fruit}
MiddleFruit => {once_returning_fruit,non_returning_fruit}
RouteCount => {(sequential_mundane_route,count_seven),(sequential_supra_route,count_eight),(prior_dispassion_route,count_nine),(sharp_mundane_route,count_eight),(sharp_supra_route,count_nine)}
MundaneMiddleRoute => {sequential_mundane_route,sharp_mundane_route}
OnPath => {(shall_know_faculty,stream_uninterrupted_path),(knowledge_faculty,stream_liberation_path)}
CommonSix => {faith,vigor,mindfulness,concentration,comprehension,mind}
StreamNine => {faith,vigor,mindfulness,concentration,comprehension,mind,neutral,shall_know_faculty,knowledge_faculty}
ArhatFixedEight => {faith,vigor,mindfulness,concentration,comprehension,mind,knowledge_faculty,one_who_has_known}
FeelingChoice => {pleasure,gladness,neutral}
SequentialMundaneSeven => {faith,vigor,mindfulness,concentration,comprehension,mind,neutral}
SequentialSupraEight => {faith,vigor,mindfulness,concentration,comprehension,mind,neutral,knowledge_faculty}
SharpMundaneEight => {faith,vigor,mindfulness,concentration,comprehension,mind,neutral,gladness}
SharpSupraNine => {faith,vigor,mindfulness,concentration,comprehension,mind,neutral,gladness,knowledge_faculty}
ArhatAttainment => {attainment_pleasure,attainment_gladness,attainment_neutral}
ByPerson => {(attainment_pleasure,person),(attainment_gladness,person),(attainment_neutral,person)}
UsesFeeling => {(attainment_pleasure,pleasure),(attainment_gladness,gladness),(attainment_neutral,neutral)}
```

Each arhatship set is the fixed eight plus one feeling, hence nine.
Their union for the represented person is eleven across repeated
attainments, not eleven at once. Even a nine-count may combine two
Path-stages. The sharp-route sets likewise count neutral feeling and
gladness across stages; they do not assert simultaneous feelings.
Cardinality tests check these unions separately from the finite-model
formulas. The model does not establish the possibility of relapse;
it represents the Bhāṣya's reported answer.

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the
verse translation): The extreme fruits are attained through nine.
Stream-entry takes the five beginning with faith, excluding one who has
known, with mind and neutral feeling. Arhatship takes the five, excluding
“I shall know,” with mind and any one feeling. The middle fruits take
seven, eight, or nine according to route. Eleven is not a simultaneous
count. It is one person attaining again across different feelings.

The death clauses are numbered in this verse and studied with the
continuous death unit at 2.15. Four do not cease separately in that
terminal context. Five are added with wholesome consciousness.

Extreme is first and last, not the last two. The stream-entry nine includes two path-names. They are not nine factors in one moment. Arhatship says any one feeling, not three together. That prepares the eleven.

Eight may be the knowledge-faculty added, or gladness added across the path-moments. The number does not identify the route.

Eleven gathers a history. The reply denies the three feelings at one time. A fallen non-returner does not regain the fruit with pleasure. Prior dispassion, attained through both paths, does not fall away. No general theory of relapse is added.

Interpretation: the result is invariant. The mediating membership is not. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_16
    a vak:Karika ;
    rdfs:label "VAK 2.16" ;
    vak:hasTopic vak:FruitAttainment ;
    vak:belongsTo vak:Indriyanirdesa .

vak:StreamEntry vak:throughCount 9 .
vak:Arhatship vak:throughCount 9 ;
    vak:acrossPerson 11 .
vak:MiddleFruit vak:throughCount 7, 8, 9 .

organon:VAK_2_16_Interpretation
    organon:distinguishes vak:Fruit, vak:Route, vak:FacultyComposition,
        vak:TemporalScope .
```
