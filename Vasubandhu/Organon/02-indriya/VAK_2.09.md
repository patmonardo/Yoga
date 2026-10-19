# VAK_2.09 — Nine as Three, and the Partition

## 1. Sanskrit (Devanāgarī)

```sanskrit
दृग्भावनाशैक्षपथे नव त्रीणि अमलं त्रयम् ।
रूपीणि जीवितं दुःखे सास्रवाणि द्विधा नव ॥ २.९ ॥
```

## 2. Sanskrit (IAST)

```text
dṛgbhāvanāśaikṣapathe nava trīṇi amalaṃ trayam /
rūpīṇi jīvitaṃ duḥkhe sāsravāṇi dvidhā nava // 2.9 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| dṛg-bhāvanā-aśaikṣa-pathe | locative singular compound, distributive in force | on the Paths of seeing, cultivation, and no-more-training |
| nava | cardinal numeral, nominative plural in context | nine [Faculties] |
| trīṇi | nominative plural neuter numeral | three [Faculties], designated according to Path |
| amalam | nominative singular neuter adjective | stainless; predicates the triad |
| trayam | nominative singular neuter collective noun | the triad just defined |
| rūpīṇi | nominative plural neuter adjective | those possessing Form |
| jīvitam | nominative singular neuter noun | Life-Faculty |
| duḥkhe | nominative dual neuter adjective, substantival | the two painful Faculties: pain and distress |
| sāsravāṇi | nominative plural neuter adjective | with outflows; predicates the coordinated group |
| dvidhā | indeclinable adverb | twofold; either outflow-status |
| nava | cardinal numeral, nominative plural in context | nine [Faculties], the same nine types |

Duḥkhe is dual, not locative. Pain and distress.

**Grammar tokens.** External sandhi is opened; the Path compound remains
one token. Faculty ellipses are resolved by the Bhāṣya, not inserted into
the verse stream.

```text
# tokens: dṛg-bhāvanā-aśaikṣa-pathe nava trīṇi amalam trayam rūpīṇi jīvitam duḥkhe sāsravāṇi dvidhā nava
```

## 4. Grammar

The locative compound distributes the three designations over three Paths.
The first nine and final nine resume the same types, under different
questions. The singular collective triad takes a singular predicate;
the coordinated Form, life, and painful pair take a plural predicate.
The Bhāṣya determines the seven Form Faculties and the membership of
the nine; these are not numerals expressed in the verse.

```nltk-fcfg
% start S
# tokens: dṛg-bhāvanā-aśaikṣa-pathe nava trīṇi amalam trayam rūpīṇi jīvitam duḥkhe sāsravāṇi dvidhā nava
S[SEM=<(?paths & ?stainless & ?outflow & ?either)>] -> PATHS[SEM=?paths] STAINLESS[SEM=?stainless] OUTFLOW[SEM=?outflow] EITHER[SEM=?either]
PATHS[SEM=<(?path(nine_group,triad) & ?nine(nine_group) & ?three(triad))>] -> PATH[CASE=loc,SEM=?path] NINE[CNT=9,REF=nine_types,SEM=?nine] THREE[CASE=nom,NUM=pl,GEN=n,CNT=3,SEM=?three]
STAINLESS[SEM=<?status(?group)>] -> AMALA[CASE=nom,NUM=sg,GEN=n,SEM=?status] TRIAD[CASE=nom,NUM=sg,GEN=n,SEM=?group]
OUTFLOW[SEM=<(?status(?form) & ?status(?life) & ?status(?painful))>] -> FORM[CASE=nom,NUM=pl,GEN=n,SEM=?form] LIFE[CASE=nom,NUM=sg,GEN=n,SEM=?life] PAIR[CASE=nom,NUM=du,GEN=n,CNT=2,SEM=?painful] WITH[CASE=nom,NUM=pl,GEN=n,SEM=?status]
EITHER[SEM=<(?both(nine_group) & ?nine(nine_group))>] -> TWOFOLD[SEM=?both] NINE[CNT=9,REF=nine_types,SEM=?nine]
PATH[CASE=loc,SEM=<\g.\t.PathDesignations(g,t)>] -> 'dṛg-bhāvanā-aśaikṣa-pathe'
NINE[CNT=9,REF=nine_types,SEM=<\g.GroupCount(g,nine)>] -> 'nava'
THREE[CASE=nom,NUM=pl,GEN=n,CNT=3,SEM=<\g.GroupCount(g,three)>] -> 'trīṇi'
AMALA[CASE=nom,NUM=sg,GEN=n,SEM=<\g.WithoutOutflowsOnly(g)>] -> 'amalam'
TRIAD[CASE=nom,NUM=sg,GEN=n,SEM=<triad>] -> 'trayam'
FORM[CASE=nom,NUM=pl,GEN=n,SEM=<form_group>] -> 'rūpīṇi'
LIFE[CASE=nom,NUM=sg,GEN=n,SEM=<life_group>] -> 'jīvitam'
PAIR[CASE=nom,NUM=du,GEN=n,CNT=2,SEM=<painful_pair>] -> 'duḥkhe'
WITH[CASE=nom,NUM=pl,GEN=n,SEM=<\g.WithOutflowsOnly(g)>] -> 'sāsravāṇi'
TWOFOLD[SEM=<\g.EitherStatus(g)>] -> 'dvidhā'
```

```nltk-dep
'trīṇi' -> 'dṛg-bhāvanā-aśaikṣa-pathe' | 'nava'
'trayam' -> 'amalam'
'sāsravāṇi' -> 'rūpīṇi' | 'jīvitam' | 'duḥkhe'
'nava' -> 'dvidhā'
```

| Span | Constituent | Result |
|---|---|---|
| [0, 3) | `PATHS` | nine types, three Path-designations |
| [3, 5) | `STAINLESS` | the triad exclusively without outflows |
| [5, 9) | `OUTFLOW` | Form group, life, and painful pair with outflows |
| [9, 11) | `EITHER` | the same nine types admit either status |
| [0, 11) | `S` | Path-designation and outflow-classification kept distinct |

## 5. Translation

### Literal Translation

> On the paths of seeing, cultivation, and no-more-training, the nine are
> the three. The triad is stainless. Those possessing form, life, and the
> two painful faculties are with outflows. Nine are twofold.

### Bhāṣya-informed study translation

> On the Paths of seeing, cultivation, and no-more-training, the nine
> Faculties are designated as the three; the triad is stainless, without
> outflows. The Form Faculties, Life-Faculty, and the two painful Faculties
> are exclusively with outflows; nine admit either status.

## 6. Philosophical Translation

> Path-designation and outflow-status answer different questions. The
> three realization Faculties are without outflows; the nine constituent
> types are not restricted to their outflow-free Path operation.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| darśana-mārga | path of seeing | knowing what had not been known |
| bhāvanā-mārga | path of cultivation | the same knowing, against remaining anuśaya |
| aśaikṣa-mārga | path of no-more-training | it has been known |
| amala | stainless | glossed without outflows; not a separate classification axis |
| sāsrava | with outflows | the ten, and the nine in one way |
| anāsrava | without outflows | the triad; not causally inert |
| dvidhā | twofold | either, not both at once |
| rūpin | possessing Form | seven, in the Form Base |
| duḥkhe | pain and distress | dual |
| kṣaya-jñāna | knowledge of exhaustion | Bhāṣya: supports the derivation of one who has known |
| anutpāda-jñāna | knowledge of non-arising | paired with exhaustion; the witness's compound form is retained in the Bhāṣya |

## 8. Logical Determination

**Kārikā, derived.** The verse assigns group-level statuses and counts;
the Bhāṣya supplies the members and ordered Path-names. Twofold concerns
the possibilities of a type, not two simultaneous statuses of one instance.

```nltk-sem
path_designations : \g.\t.PathDesignations(g,t)
stainless_triad : \g.WithoutOutflowsOnly(g)
twofold_types : \g.EitherStatus(g)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(PathDesignations(nine_group,triad) & GroupCount(nine_group,nine) & GroupCount(triad,three) & WithoutOutflowsOnly(triad) & WithOutflowsOnly(form_group) & WithOutflowsOnly(life_group) & WithOutflowsOnly(painful_pair) & EitherStatus(nine_group) & GroupCount(nine_group,nine))

# THEORY prose
# EXPECT prose T
(NamedOn(nine_group,seeing,first_f) & NamedOn(nine_group,cultivation,second_f) & NamedOn(nine_group,no_more_training,third_f))
(GroupCount(form_group,seven) & GroupCount(life_group,one) & GroupCount(painful_pair,two))
all x.(NineType(x) <-> (CanHaveOutflows(x) & CanBeWithoutOutflows(x)))
all x.(RealizationFaculty(x) -> WithoutOutflowsOnly(x))
all x.(FormFaculty(x) -> WithOutflowsOnly(x))
(WithOutflowsOnly(life_f) & WithOutflowsOnly(pain_f) & WithOutflowsOnly(distress_f))

# THEORY rejected_faith_exclusively_without_outflows
# EXPECT rejected_faith_exclusively_without_outflows F
all x.(FaithGroup(x) -> -CanHaveOutflows(x))

# THEORY rejected_triad_twofold
# EXPECT rejected_triad_twofold F
EitherStatus(triad) & EitherStatus(nine_group)

# THEORY rejected_swapped_path_names
# EXPECT rejected_swapped_path_names F
NamedOn(nine_group,seeing,second_f) & NamedOn(nine_group,cultivation,first_f)
```

```nltk-valuation
nine_group => nine_types
triad => realization_triad
form_group => seven_form_types
life_group => life_type
painful_pair => pain_distress_types
nine => count_nine
three => count_three
seven => count_seven
one => count_one
two => count_two
seeing => seeing_path
cultivation => cultivation_path
no_more_training => no_more_training_path
first_f => shall_know
second_f => knowledge
third_f => one_who_has_known
life_f => life
pain_f => pain
distress_f => distress
PathDesignations => {(nine_types,realization_triad)}
GroupCount => {(nine_types,count_nine),(realization_triad,count_three),(seven_form_types,count_seven),(life_type,count_one),(pain_distress_types,count_two)}
WithoutOutflowsOnly => {realization_triad,shall_know,knowledge,one_who_has_known}
WithOutflowsOnly => {seven_form_types,life_type,pain_distress_types,eye,ear,nose,tongue,body,female,male,life,pain,distress}
EitherStatus => {nine_types}
NamedOn => {(nine_types,seeing_path,shall_know),(nine_types,cultivation_path,knowledge),(nine_types,no_more_training_path,one_who_has_known)}
NineType => {mind,pleasure,gladness,neutral,faith,vigor,mindfulness,concentration,comprehension}
CanHaveOutflows => {mind,pleasure,gladness,neutral,faith,vigor,mindfulness,concentration,comprehension}
CanBeWithoutOutflows => {mind,pleasure,gladness,neutral,faith,vigor,mindfulness,concentration,comprehension}
FaithGroup => {faith,vigor,mindfulness,concentration,comprehension}
RealizationFaculty => {shall_know,knowledge,one_who_has_known}
FormFaculty => {eye,ear,nose,tongue,body,female,male}
```

The three type-sets contain 3, 10, and 9 distinct Faculty-names, totaling
22; group and count labels are not additional Faculties. Count predicates
record the numerals, so their agreement with set cardinalities requires
separate tests. Nine types are not nine factors co-present in every
Path-event. This finite model does not prove the scriptural rebuttal;
the paired Bhāṣya preserves its two alternative replies and two
positive grounds.

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the
verse translation): The three are not three further items. They are the
same nine, named by the path-task. The triad is stainless. Those
possessing form, life, and the two painful faculties are with outflows.
Nine, as types, can be either.

The chapter has named the twenty-two and defined the feelings. This verse qualifies them by path and by outflow.

Nothing unprecedented to know is the path-task, not omniscience. Suffering fully known is not the loss of the power to cognize it again.

Twofold is either status across instances, not both in one instance. With outflows is not unwholesome, and not the arhat's bodily feeling denied. Conditioned and unconditioned are not this classification.

Some restrict the five. The first reply limits the citation to the faculties without outflows. The alternative limits it to the outsider whose wholesome roots are severed. Or marks an alternative, not a second step that must be joined. The Wheel not yet turned, and the fivefold examination, are the positive grounds. The last quotation is abbreviated in the Sanskrit. It is not completed from elsewhere.

Interpretation: the Path-task determines the realization name without
making every instance of the nine constituent types outflow-free.
The distinction is between qualified operation and type-level capacity,
not between three extra substances and nine original substances.
Stainless here means without outflows; a project-level account of Pure
and Impure must not replace that explicit gloss.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_09
    a vak:Karika ;
    rdfs:label "VAK 2.09" ;
    vak:hasTopic vak:NineAsThree ;
    vak:belongsTo vak:Indriyanirdesa .

vak:NineFaculties vak:namedOn vak:PathOfSeeing, vak:PathOfCultivation, vak:PathOfNoMoreTraining .
vak:Triad vak:stainless true .
vak:SevenOfForm vak:withOutflows true .
vak:LifeFaculty vak:withOutflows true .
vak:PainFaculty vak:withOutflows true .
vak:DistressFaculty vak:withOutflows true .
vak:NineFaculties vak:twofold true .

organon:PathConfiguration
    organon:distinguishes vak:PathDesignation, vak:OutflowStatus ;
    organon:doesNotRequireNineCoPresent true .
```
