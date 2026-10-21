# VAK_2.13 — To Be Abandoned, and Not

## 1. Sanskrit (Devanāgarī)

```sanskrit
मनोवित्तित्रयं त्रेधा द्विहेया दुर्मनस्कता ।
नव भावनया पञ्च त्वहेयान्यपि न त्रयम् ॥ २.१३ ॥
```

## 2. Sanskrit (IAST)

```text
manovittitrayaṃ tredhā dviheyā durmanaskatā /
nava bhāvanayā pañca tv aheyāny api na trayam // 2.13 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| mano-vitti-trayam | nominative singular neuter compound, collective | Mind and a triad of feelings; four Faculties, not three |
| tredhā | indeclinable | in three ways |
| dvi-heyā | nominative singular feminine gerundive compound | to be abandoned in two ways; qualifies distress |
| durmanaskatā | nominative singular feminine noun | distress |
| nava | cardinal numeral, nominative plural in context | nine [Faculties] |
| bhāvanayā | instrumental singular feminine noun | by cultivation; the abandonment predicate continues |
| pañca | cardinal numeral, nominative plural in context | the five beginning with faith |
| tu | contrastive particle | however |
| aheyāni | nominative plural neuter gerundive adjective with privative prefix | not to be abandoned |
| api | additive particle | also; adds non-abandonment to cultivation-abandonment |
| na | negative particle | not; negates the supplied abandonment predicate |
| trayam | nominative singular neuter collective noun | the three realization Faculties |

Manovittitrayam is four faculties. The three feelings are pleasure, gladness, and neutral feeling. Pain is not in that triad.

**Grammar tokens.** External sandhi is opened, including *tu aheyāni api*. The opening compound remains one token. The question supplies the three statuses, and the prose resolves the carried cultivation predicate.

```text
# tokens: manovittitrayam tredhā dviheyā durmanaskatā nava bhāvanayā pañca tu aheyāni api na trayam
```

## 4. Grammar

Threefold answers the opening question: abandonable by seeing, by cultivation, or not abandonable. The feminine gerundive agrees with distress; the instrumental cultivation specifies the means for the nine. For the five, *api* adds non-abandonment to the carried cultivation predicate. A shared feature requires that carry to agree with the nine's instrumental clause. The final negation excludes abandonment of the triad. These are ranges across qualified instances, not completed acts.

```nltk-fcfg
% start S
# tokens: manovittitrayam tredhā dviheyā durmanaskatā nava bhāvanayā pañca tu aheyāni api na trayam
S[SEM=<(?four & ?distress & ?nine & ?five & ?triad)>] -> FOUR[SEM=?four] DISTRESSCLAUSE[SEM=?distress] NINECLAUSE[SEM=?nine] FIVECLAUSE[SEM=?five] TRIADCLAUSE[SEM=?triad]
FOUR[SEM=<ThreeAbandonmentStatuses(mind_three_feelings)>] -> FOURGROUP THREEFOLD
FOURGROUP -> 'manovittitrayam'
THREEFOLD -> 'tredhā'
DISTRESSCLAUSE[SEM=<SeeingOrCultivation(distress_f)>] -> TWOHEYA DISTRESS
TWOHEYA -> 'dviheyā'
DISTRESS -> 'durmanaskatā'
NINECLAUSE[SEM=<GroupCount(nine_group,nine) & CultivationOnly(nine_group)>] -> NINE CULTIVATION
NINE -> 'nava'
CULTIVATION -> 'bhāvanayā'
FIVECLAUSE[SEM=<GroupCount(faith_group,five) & CultivationOrNot(faith_group) & CanBeNotAbandoned(faith_group)>] -> FIVE BUT NOTHEYA ALSO
FIVE -> 'pañca'
BUT -> 'tu'
NOTHEYA -> 'aheyāni'
ALSO -> 'api'
TRIADCLAUSE[SEM=<GroupCount(realization_group,three) & NotAbandonedOnly(realization_group)>] -> NOT TRIAD
NOT -> 'na'
TRIAD -> 'trayam'
```

```nltk-dep
'manovittitrayam' -> 'tredhā'
'durmanaskatā' -> 'dviheyā'
'nava' -> 'bhāvanayā'
'pañca' -> 'tu' | 'aheyāni' | 'api'
'trayam' -> 'na'
```

| Span | Constituent | Result |
|---|---|---|
| [0, 2) | `FOUR` | Mind and three feelings, three statuses |
| [2, 4) | `DISTRESSCLAUSE` | distress, seeing or cultivation |
| [4, 6) | `NINECLAUSE` | nine, cultivation only |
| [6, 10) | `FIVECLAUSE` | five, cultivation or not abandonable |
| [10, 12) | `TRIADCLAUSE` | triad, not abandonable |
| [0, 12) | `S` | five ranges with cultivation carried into the five |

## 5. Translation

### Literal Translation

> Mind and the triad of feelings are threefold. Distress is to be abandoned in two ways. Nine by cultivation. The five, however, also not to be abandoned. Not the triad.

### Bhāṣya-informed study translation

> Mind and the three feelings are to be abandoned by seeing, by cultivation, or not at all. Distress is to be abandoned by seeing or cultivation; nine Faculties by cultivation alone. The five, however, are either to be abandoned by cultivation or not to be abandoned; the triad is not to be abandoned.

## 6. Philosophical Translation

> Abandonment classifies qualified instances, not the rejection of a Faculty-type. The five differ according to outflow-status; the faultless triad is not fit to be abandoned.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| darśana-prahātavya | to be abandoned by seeing | one status of Mind, the three feelings, and distress |
| bhāvanā-prahātavya | to be abandoned by cultivation | exclusive for the nine; possible for the mixed groups |
| aheya | not to be abandoned | not inert, not permanent |
| vitti-traya | three feelings | pleasure, gladness, neutral feeling |
| durmanaskatā | distress | both ways; never kept |
| jīvitāṣṭama | life as eighth | with pain, the nine |
| nirdoṣa | faultless | the reason the triad is not fit |
| prakāra-bheda | distinctions of kind | closed here |

## 8. Logical Determination

**Kārikā, derived.** The root SEM records five ranges. The Bhāṣya supplies their members and maps the five's two statuses to with-outflows and without-outflows instances. Can be not abandoned describes the classification, not actual retention or permanence. The inherited status link records the ellipsis resolved by the Bhāṣya; the five's two alternatives apply across qualified instances.

```nltk-sem
three_statuses : ThreeAbandonmentStatuses(mind_three_feelings)
cultivation_only : CultivationOnly(nine_group)
triad_status : NotAbandonedOnly(realization_group)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(ThreeAbandonmentStatuses(mind_three_feelings) & SeeingOrCultivation(distress_f) & GroupCount(nine_group,nine) & CultivationOnly(nine_group) & GroupCount(faith_group,five) & CultivationOrNot(faith_group) & CanBeNotAbandoned(faith_group) & GroupCount(realization_group,three) & NotAbandonedOnly(realization_group))

# THEORY prose_type_ranges
# EXPECT prose_type_ranges T
all x.(FourType(x) -> (CanSeeing(x) & CanCultivation(x) & CanNotAbandon(x)))
CanSeeing(distress_f) & CanCultivation(distress_f) & -CanNotAbandon(distress_f)
all x.(NineType(x) -> (-CanSeeing(x) & CanCultivation(x) & -CanNotAbandon(x)))
all x.(FaithType(x) -> (-CanSeeing(x) & CanCultivation(x) & CanNotAbandon(x)))
all x.(RealizationType(x) -> (-CanSeeing(x) & -CanCultivation(x) & CanNotAbandon(x)))

# THEORY prose_faith_instances
# EXPECT prose_faith_instances T
all x.(FaithInstance(x) -> (WithOutflows(x) | WithoutOutflows(x)))
all x.(FaithInstance(x) -> -(WithOutflows(x) & WithoutOutflows(x)))
all x.(FaithInstance(x) -> (ByCultivation(x) <-> WithOutflows(x)))
all x.(FaithInstance(x) -> (NotToAbandon(x) <-> WithoutOutflows(x)))

# THEORY prose_faultless
# EXPECT prose_faultless T
all x.(Faultless(x) -> -FitToAbandon(x))

# THEORY rejected_both_faith_statuses
# EXPECT rejected_both_faith_statuses F
exists x.(FaithInstance(x) & ByCultivation(x) & NotToAbandon(x))

# THEORY rejected_pain_in_threefold_group
# EXPECT rejected_pain_in_threefold_group F
FourType(pain_f) & CanNotAbandon(pain_f)

# THEORY rejected_faith_by_seeing
# EXPECT rejected_faith_by_seeing F
exists x.(FaithType(x) & CanSeeing(x))

# THEORY rejected_distress_not_abandonable
# EXPECT rejected_distress_not_abandonable F
CanNotAbandon(distress_f) & CanCultivation(distress_f)

# THEORY rejected_all_faith_instances_abandonable
# EXPECT rejected_all_faith_instances_abandonable F
all x.(FaithInstance(x) -> ByCultivation(x))
```

```nltk-valuation
mind_three_feelings => four_types
distress_f => distress
pain_f => pain
nine_group => nine_types
faith_group => five_types
realization_group => three_types
nine => count_nine
five => count_five
three => count_three
ThreeAbandonmentStatuses => {four_types}
SeeingOrCultivation => {distress}
GroupCount => {(nine_types,count_nine),(five_types,count_five),(three_types,count_three)}
CultivationOnly => {nine_types}
CultivationOrNot => {five_types}
CanBeNotAbandoned => {five_types}
NotAbandonedOnly => {three_types}
FourType => {mind,pleasure,gladness,neutral}
NineType => {eye,ear,nose,tongue,body,female,male,life,pain}
FaithType => {faith,vigor,mindfulness,concentration,comprehension}
RealizationType => {shall_know,knowledge,one_who_has_known}
CanSeeing => {mind,pleasure,gladness,neutral,distress}
CanCultivation => {mind,pleasure,gladness,neutral,distress,eye,ear,nose,tongue,body,female,male,life,pain,faith,vigor,mindfulness,concentration,comprehension}
CanNotAbandon => {mind,pleasure,gladness,neutral,faith,vigor,mindfulness,concentration,comprehension,shall_know,knowledge,one_who_has_known}
FaithInstance => {faith_with_outflows,faith_without_outflows}
WithOutflows => {faith_with_outflows}
WithoutOutflows => {faith_without_outflows}
ByCultivation => {faith_with_outflows}
NotToAbandon => {faith_without_outflows}
Faultless => {shall_know,knowledge,one_who_has_known,faith_without_outflows}
FitToAbandon => {faith_with_outflows}
```

The Faculty partition contains 4 + 1 + 9 + 5 + 3 = 22 types. The two faith instances illustrate the prose's exclusive alternatives, not extra Faculties or an exhaustive ontology. The model checks permitted ranges and their distinction; it does not supply a mechanism of abandonment.

Threefold here is not the ethical threefold of 2.11. Pain has moved.

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the verse translation): Mind and the three feelings, pleasure, gladness, and neutral feeling, are threefold: to be abandoned by seeing, by cultivation, or not at all. Distress is to be abandoned in two ways, by seeing and by cultivation. Nine, the eye and the rest with life as the eighth, together with pain, are to be abandoned by cultivation alone. The five beginning with faith are both to be abandoned by cultivation and not to be abandoned, according as they are with or without outflows. The triad is not to be abandoned at all, for what is faultless is not fit to be abandoned.

This closes the distinctions of kind opened at 2.09: outflow, maturation, ethical quality, realm-connection, abandonment. Acquisition is the next question. It is not another name for this.

Both ways, for distress, distributes instances. One instance is not abandoned twice. Cultivation-abandonable is not unwholesome. The nine include indeterminate faculties. The five are wholesome and still abandonable when with outflows.

The paragraph does not say how the nine are abandoned. It is not an instruction to destroy the body or end life. Ordinary cessation is not this category. Not to be abandoned is not permanence, and not uninterrupted operation.

Interpretation: the path-rule is typed. Keep the faculty. Inspect the instance. Abandon only what is fit. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_13
    a vak:Karika ;
    rdfs:label "VAK 2.13" ;
    vak:hasTopic vak:Abandonment ;
    vak:belongsTo vak:Indriyanirdesa .

vak:DistressFaculty vak:notAbandoned false .
vak:Triad vak:notAbandoned true ;
    vak:because vak:Faultless .
vak:Five vak:splitsBy vak:Outflow .

organon:VAK_2_13_Interpretation
    organon:distinguishes vak:FacultyType, vak:QualifiedInstance,
        vak:AbandonmentStatus .
```
