# VAK_2.10 — Maturation, and What Produces It

## 1. Sanskrit (Devanāgarī)

```sanskrit
विपाको जीवितं द्वेधा द्वादश अन्त्याष्टकादृते ।
दौर्मनस्याच्च तत्त्वेकं सविपाकं दश द्विधा ॥ २.१० ॥
```

## 2. Sanskrit (IAST)

```text
vipāko jīvitaṃ dvedhā dvādaśa antyāṣṭakādṛte /
daurmanasyāc ca tattv ekaṃ savipākaṃ daśa dvidhā // 2.10 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| vipākaḥ | nominative singular masculine noun | maturation; predicate of Life-Faculty |
| jīvitam | nominative singular neuter noun | Life-Faculty |
| dvedhā | indeclinable | twofold, on that axis |
| dvādaśa | cardinal numeral, nominative plural in context | twelve [Faculties] |
| antya-aṣṭakāt | ablative singular neuter compound | from the final eight; governed by ṛte |
| ṛte | indeclinable, governing ablative | apart from |
| daurmanasyāt | ablative singular neuter noun | from distress; shares the exclusion |
| ca | coordinating particle | and |
| tat | nominative singular neuter demonstrative | that; resumes distress |
| tu | restrictive particle in the Bhāṣya's construal | only; construed with the maturation-producing predicate |
| ekam | nominative singular neuter numeral | one, distress alone invariably producing maturation |
| sa-vipākam | nominative singular neuter adjective | possessing maturation as result, not being maturation |
| daśa | cardinal numeral, nominative plural in context | ten [Faculties] |
| dvidhā | indeclinable adverb | twofold on the second, result-producing axis |

Vipāka is what the present instance is. Savipāka is what it produces. The two questions are not one word.

**Grammar tokens.** External sandhi is opened, including *tat tu ekam* and *antya-aṣṭakāt ṛte*. No Bhāṣya-supplied members or life exception are inserted into the verse stream.

```text
# tokens: vipākaḥ jīvitam dvedhā dvādaśa antya-aṣṭakāt ṛte daurmanasyāt ca tat tu ekam savipākam daśa dvidhā
```

## 4. Grammar

The opening predicate states the life rule; the Bhāṣya qualifies it for concentration-projected life. The first twofold class excludes the final eight and distress, with life already treated separately. That separate placement remains even though the Bhāṣya later gives a life-instance that is not maturation. *Tat* resumes distress, not life or the twelve. The Bhāṣya construes *tu* as restrictive and displaced: distress alone is invariably maturation-producing, not the only Faculty capable of producing maturation.

```nltk-fcfg
% start S
# tokens: vipākaḥ jīvitam dvedhā dvādaśa antya-aṣṭakāt ṛte daurmanasyāt ca tat tu ekam savipākam daśa dvidhā
S[SEM=<(?life & ?twelve & ?distress & ?ten)>] -> LIFECLAUSE[SEM=?life] TWELVECLAUSE[SEM=?twelve] DISTRESSCLAUSE[SEM=?distress] TENCLAUSE[SEM=?ten]
LIFECLAUSE[SEM=<LifeMaturationRule(life_f)>] -> RESULT LIFE
RESULT -> 'vipākaḥ'
LIFE -> 'jīvitam'
TWELVECLAUSE[SEM=<EitherMaturation(twelve_group) & GroupCount(twelve_group,twelve) & Excludes(twelve_group,final_eight) & Excludes(twelve_group,distress_f)>] -> EITHER TWELVE EIGHT EXCEPT DISTRESS AND
EITHER -> 'dvedhā'
TWELVE -> 'dvādaśa'
EIGHT -> 'antya-aṣṭakāt'
EXCEPT -> 'ṛte'
DISTRESS -> 'daurmanasyāt'
AND -> 'ca'
DISTRESSCLAUSE[SEM=<SoleInvariableProducer(distress_f) & AlwaysProducesMaturation(distress_f)>] -> THAT ONLY ONE PRODUCES
THAT -> 'tat'
ONLY -> 'tu'
ONE -> 'ekam'
PRODUCES -> 'savipākam'
TENCLAUSE[SEM=<GroupCount(ten_group,ten) & EitherProduces(ten_group)>] -> TEN EITHER2
TEN -> 'daśa'
EITHER2 -> 'dvidhā'
```

```nltk-dep
'jīvitam' -> 'vipākaḥ'
'dvādaśa' -> 'dvedhā' | 'ṛte'
'ṛte' -> 'antya-aṣṭakāt' | 'daurmanasyāt' | 'ca'
'savipākam' -> 'tat' | 'tu' | 'ekam'
'daśa' -> 'dvidhā'
```

| Span | Constituent | Result |
|---|---|---|
| [0, 2) | `LIFECLAUSE` | life-maturation rule, qualified in the prose |
| [2, 8) | `TWELVECLAUSE` | twelve twofold as results, with explicit exclusions |
| [8, 12) | `DISTRESSCLAUSE` | distress alone invariably produces maturation |
| [12, 14) | `TENCLAUSE` | ten twofold as producers |
| [0, 14) | `S` | two independent maturation axes |

## 5. Translation

### Literal Translation

> Life is maturation. Twelve are twofold, apart from the final eight and distress. That one alone possesses maturation as its result. Ten are twofold.

### Bhāṣya-informed study translation

> Life is maturation. Apart from the final eight and distress, twelve Faculties can be maturation or not. That distress alone invariably produces maturation; ten Faculties can produce maturation or not.

## 6. Philosophical Translation

> Being a matured result and producing such a result are different determinations. Distress is never the former and invariably the latter; the life rule is qualified by concentration-projected life.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| vipāka | maturation | the present result of prior action |
| savipāka | possessing maturation | produces a future result |
| antya-aṣṭaka | final eight | the five and the three |
| upacayika | from development | a Form faculty that is not maturation |
| airyāpathika | deportment | indeterminate; not maturation |
| śailpasthānika | craft | indeterminate |
| nairmāṇika | magical creation | indeterminate |
| parikalpa-viśeṣa | particular conceptual construction | produces and calms distress |
| prāntakoṭika | the named fourth dhyāna | the arhat's lifespan act |
| āyuḥsaṃskāra | lifespan-formation | the digression |
| jīvitasaṃskāra | life-formation | distinguished, or not, by the alternatives |

## 8. Logical Determination

**Kārikā, derived.** LifeMaturationRule records the opening rule without silently excluding the prose's counterexample. EitherMaturation and EitherProduces concern different questions. SoleInvariableProducer does not exclude conditional production by the ten. The twelve-count is an enumerative class, not a claim that Life can never have an exceptional non-maturation instance.

```nltk-sem
received_result : EitherMaturation(twelve_group)
productive_result : EitherProduces(ten_group)
distress_reference : distress_f
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(LifeMaturationRule(life_f) & EitherMaturation(twelve_group) & GroupCount(twelve_group,twelve) & Excludes(twelve_group,final_eight) & Excludes(twelve_group,distress_f) & SoleInvariableProducer(distress_f) & AlwaysProducesMaturation(distress_f) & GroupCount(ten_group,ten) & EitherProduces(ten_group))

# THEORY prose_life_exception
# EXPECT prose_life_exception T
all x.(LifeInstance(x) -> (IsMaturation(x) <-> -ConcentrationProjected(x)))
CanBeMaturation(life_f) & CanBeNonMaturation(life_f) & -TwelveType(life_f)
(LifeInstance(ordinary_life) & IsMaturation(ordinary_life) & LifeInstance(projected_life) & -IsMaturation(projected_life))

# THEORY prose_partitions
# EXPECT prose_partitions T
all x.(TwelveType(x) <-> (CanBeMaturation(x) & CanBeNonMaturation(x) & -(x = life_f)))
all x.(NeverMaturation(x) -> (-CanBeMaturation(x) & CanBeNonMaturation(x)))
all x.(TenType(x) <-> (CanProduce(x) & CanNotProduce(x)))
all x.(NeverProduces(x) -> (-CanProduce(x) & CanNotProduce(x)))
(NeverMaturation(distress_f) & AlwaysProducesMaturation(distress_f) & CanProduce(distress_f) & -CanNotProduce(distress_f))

# THEORY rejected_life_in_twelve
# EXPECT rejected_life_in_twelve F
exists x.((x = life_f) & TwelveType(x))

# THEORY rejected_all_life_is_maturation
# EXPECT rejected_all_life_is_maturation F
all x.(LifeInstance(x) -> IsMaturation(x))

# THEORY rejected_distress_is_maturation
# EXPECT rejected_distress_is_maturation F
CanBeMaturation(distress_f) & CanProduce(distress_f)

# THEORY rejected_only_distress_can_produce
# EXPECT rejected_only_distress_can_produce F
all x.(CanProduce(x) -> (x = distress_f))
```

```nltk-valuation
life_f => life
distress_f => distress
twelve_group => twelve_types
ten_group => ten_types
final_eight => final_eight_types
twelve => count_twelve
ten => count_ten
ordinary_life => ordinary_life_event
projected_life => concentration_life_event
LifeMaturationRule => {life}
EitherMaturation => {twelve_types}
GroupCount => {(twelve_types,count_twelve),(ten_types,count_ten)}
Excludes => {(twelve_types,final_eight_types),(twelve_types,distress)}
SoleInvariableProducer => {distress}
AlwaysProducesMaturation => {distress}
EitherProduces => {ten_types}
LifeInstance => {ordinary_life_event,concentration_life_event}
ConcentrationProjected => {concentration_life_event}
IsMaturation => {ordinary_life_event}
TwelveType => {eye,ear,nose,tongue,body,female,male,mind,pain,pleasure,gladness,neutral}
CanBeMaturation => {eye,ear,nose,tongue,body,female,male,mind,pain,pleasure,gladness,neutral,life}
CanBeNonMaturation => {eye,ear,nose,tongue,body,female,male,mind,pain,pleasure,gladness,neutral,life,distress,faith,vigor,mindfulness,concentration,comprehension,shall_know,knowledge,one_who_has_known}
FinalEightType => {faith,vigor,mindfulness,concentration,comprehension,shall_know,knowledge,one_who_has_known}
NeverMaturation => {distress,faith,vigor,mindfulness,concentration,comprehension,shall_know,knowledge,one_who_has_known}
TenType => {mind,pain,pleasure,gladness,neutral,faith,vigor,mindfulness,concentration,comprehension}
CanProduce => {distress,mind,pain,pleasure,gladness,neutral,faith,vigor,mindfulness,concentration,comprehension}
CanNotProduce => {mind,pain,pleasure,gladness,neutral,faith,vigor,mindfulness,concentration,comprehension,eye,ear,nose,tongue,body,female,male,life,shall_know,knowledge,one_who_has_known}
NeverProduces => {eye,ear,nose,tongue,body,female,male,life,shall_know,knowledge,one_who_has_known}
```

The received-result partition is 1 + 12 + 9. Life has both instance-level possibilities but remains the separately named first class; the twelve are the remaining types with both possibilities. The productive partition is 1 + 10 + 11. Finite-model tests check these counts and contrasts, not the efficacy of lifespan practices or the truth of every reported causal account. The opening Life rule does not assert that every life-instance is maturation. CanBeNonMaturation(life_f) records the prose exception without changing the verse's twelve-count.

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the verse translation): What the instance is, and what it produces, are separate. Life is received maturation, except the life concentration projects. Distress is never received. It is produced and calmed by present construction, yet always produces future maturation. Ten can either produce it or not.

The opening rule is qualified before the twelve are counted. Concentration-generated life is not maturation. Resource-maturation converted to lifespan, a remainder drawn forward, and Ghoṣaka's Great Elements are reported alternatives. The adopted explanation is the turned impetus. The digression on why, where, and the Buddha's three months is marked incidental. It is not a practical instruction.

Distress and the sūtra of three actions stay apart. Association is not maturation. The Vaibhāṣika reasons are construction, the immediate-offense counterexample, and absence in those free from attachment. Gladness still has room to be maturation. Distress does not.

Eight with life as eighth: wholesome in a favorable destiny, unwholesome in an unfavorable one. Mind is either in either. Pleasure, gladness, and neutral feeling are wholesome maturation. Pain is unwholesome. Both sexual marks in a favorable destiny: the condition is unwholesome acquisition. The faculty itself is projected by wholesome action.

Interpretation: the two predicates are the method. The received collapse is refused. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_10
    a vak:Karika ;
    rdfs:label "VAK 2.10" ;
    vak:hasTopic vak:Maturation, vak:ProducesMaturation ;
    vak:belongsTo vak:Indriyanirdesa .

vak:LifeFaculty vak:isMaturation true ;
    vak:exception vak:ConcentrationProjectedLife .
vak:DistressFaculty vak:isMaturation false ;
    vak:producesMaturation true .

organon:VAK_2_10_Interpretation
    organon:distinguishes vak:BeingMaturation, vak:ProducingMaturation .
```
