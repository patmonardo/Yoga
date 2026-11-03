# VAK_5.15

## 1. Sanskrit (Devanāgarī)

```sanskrit
स्वभूम्युपरमो मार्गः षड्भूमिनवभूमिकः ।
तद्गोचराणां विषयो मार्गो ह्यन्योऽन्यहेतुकः ॥ ५.१५ ॥
```

## 2. Sanskrit (IAST)

```text
svabhūmy-uparamo mārgaḥ ṣaḍbhūmi-navabhūmikaḥ |
tad-gocarāṇāṃ viṣayo mārgo hy anyo 'nya-hetukaḥ || 5.15 ||
```

The verse specifies the range of the cessation-oriented and
path-oriented anuśayas identified in VAK 5.14.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `sva-bhūmi-uparamaḥ` | nominative singular masculine compound | cessation belonging to its own level |
| `mārgaḥ` | nominative singular masculine | path |
| `ṣaḍ-bhūmi` | first member of the compound `ṣaḍbhūmi-navabhūmikaḥ` | the six-level side of the path |
| `nava-bhūmikaḥ` | nominative singular masculine adjective | belonging to nine levels |
| `tad-gocarāṇām` | genitive plural | of those whose cognitive range is that |
| `viṣayaḥ` | nominative singular masculine | Condition, determinate field |
| `hi` | explanatory particle | for, because |
| `anyaḥ anya-hetukaḥ` | nominative singular construction | one has another as cause; one is causally related to another |

Padaccheda: `sva-bhūmi-uparamaḥ | mārgaḥ |
ṣaḍ-bhūmi-nava-bhūmikaḥ | tad-gocarāṇām | viṣayaḥ |
mārgaḥ | hi | anyaḥ | anya-hetukaḥ`.
The six- and nine-level designations are compressed into one compound;
the Bhāṣya distributes them across the two knowledge-sides of the Path.

The compact first pāda requires the Bhāṣya to distribute the six- and
nine-level predicates. They do not qualify cessation: they distinguish two
sides of the path and their corresponding afflicted range-relations.

## 4. Grammar

**Own-level cessation**

```text
[nirodhaḥ] sva-bhūmi-uparamaḥ

[cessation] is the cessation of its own level
```

`Nirodha`, carried forward from VAK 5.14, is understood. The compound is not a
bare statement that something stops “on its own”; `sva-bhūmi` specifies the
level whose process has ceased.

**Distribution of the path predicates**

```text
mārgaḥ ṣaḍ-bhūmiḥ [vā] nava-bhūmikaḥ
tad-gocarāṇāṃ viṣayaḥ

the path belonging to six or nine levels
is the Condition for those whose range is that
```

The Bhāṣya resolves the compressed construction: the six-level
`dharmajñāna` side is the Condition for Desire Realm path-oriented anuśayas; the
nine-level `anvayajñāna` side is the Condition for those of the form and formless
realms.

**Causal rationale**

```text
mārgaḥ hi anyaḥ anya-hetukaḥ

for one path has another as cause
```

The distributive force of `anyaḥ ... anya-` expresses causal connection among
distinct path moments. The Bhāṣya also speaks of mutual causality, while still
restricting the range according to counteragent function.
The restriction by `pratipakṣa`, counteragent function, belongs to the
Bhāṣya's subsequent objections and qualifies the path's possible range.

## 5. Translation

### Literal Translation

> Cessation is the cessation of its own level. The path, belonging to six
> levels or nine levels, is the Condition for those whose range is that; for one
> path has another as cause.

### Bhāṣya-informed study translation

> Cessation is confined to its own level. Those whose range is the Path have
> the six-level dharmajñāna Path or the nine-level anvayajñāna Path as their
> Condition, according to domain, since one path is a cause of another.

## 6. Philosophical Translation

> Cessation and path are both uncontaminated truth-fields, but they possess
> different relational forms. Cessation is the determinate ending of the
> afflictive process belonging to a particular level. Path is an articulated
> process whose moments condition other moments and therefore extend across a
> wider structure of levels. The end is intelligible through exactly what has
> ended; the way is intelligible through the causal mediation by which one
> transformation produces another.

Thus:

```text
cessation
    = level-indexed completion

path
    = causally articulated transformation
```

Neither is an indeterminate beyond. Each has its own positive relational
structure.

## 7. Technical Vocabulary

**`Svabhūmy-uparama` — cessation of one's own level**

For an anuśaya belonging to the Desire Realm, only cessation of the desire
realm serves as its Support; the same own-level rule continues through the
summit of existence. Cessation is determinate termination, not bare absence.

**`Bhūmi` — level or stage**

Here `bhūmi` indexes the differentiated levels on which affliction,
counteraction, and cessation are situated. It should not be flattened into a
mere spatial location.

**`Dharmajñāna-pakṣa` — the dharma-knowledge side of the path**

The Bhāṣya assigns this six-level path to the Support range of Desire Realm
path-oriented anuśayas. Its fuller determination belongs to the later Path
and Knowledge chapters.

**`Anvayajñāna-pakṣa` — the subsequent or corresponding-knowledge side**

The Bhāṣya assigns this nine-level path to the Support range of path-oriented
anuśayas belonging to the Form and Formless realms, including levels not
directly seen.
The provisional English remains subordinate to its later technical analysis.

**`Pratipakṣa` — counteragent**

Support range is not established by causal connectedness alone. The Bhāṣya
notes that `anvayajñāna` is not the counteragent to the Desire Realm; hence
Desire Realm path-oriented anuśayas do not take that side as Support.

**`Anyo 'nya-hetuka` — one path caused by another**

Path is internally causal. Distinct path determinations can condition one
another, giving the Way a systematic range that cessation, as own-level
termination, does not possess.

**`Gocara`, `viṣaya`, and `ālambana`**

The kārikā uses `gocara` and `viṣaya`; the Bhāṣya explains the relation through
`ālambana`. Here `gocara` marks the anuśaya's range, `viṣaya` names the
Path as its Condition in the verse, and `ālambana` names the Path as its
Support in the prose. This local relation does not make the three terms
lexical synonyms.

## 8. Logical Determination

The cessation rule is indexical:

```text
BelongsToLevel(anuśaya, L)
AND HasSupportType(anuśaya, Cessation)
    → HasSupport(anuśaya, CessationOf(L))
```

It excludes cross-level substitution:

```text
CessationOf(L1) ≠ CessationOf(L2)
    when L1 ≠ L2
```

The path rule is differentiated by realm:

```text
DesireRealm(x)
AND PathOriented(x)
    → HasSupport(x, SixLevelDharmajñanaPath)

FormOrFormlessRealm(x)
AND PathOriented(x)
    → HasSupport(x, NineLevelAnvayajnanaPath)
```

Causal relation is necessary but not sufficient for unrestricted range:

```text
CausallyRelated(PathA, PathB)
AND Counteracts(PathB, RealmOf(x))
    → AdmissiblePathSupport(x, PathB)
```

Therefore:

```text
MutuallyCausal(Dharmajñana, Anvayajnana)
    ⇏ DesireRealmAnusayaTakes(Anvayajnana)
```

The missing condition is appropriate counteragent function.

## 9. Interpretive Note

VAK 5.15 differentiates the two uncontaminated terms of VAK 5.14 with unusual
precision. Cessation is the Product as achieved result: it is exactly the
cessation of this determinate level of afflictive organization. Mārga is not
merely a process leading from one level to another. It is itself the higher
level of Objectivity in which Theory and the Path-bhūmis are one articulated
system: the truth is objectively determined and that determination acquires
achieved existence through the levels of the Way.

```text
Telos
    determinate completion of a specified level

Way
    higher Objectivity articulated as Theory and Path-bhūmis
```

The difference matters. If cessation were bare nothing, it could not be
indexed to the structure overcome. If path were merely an external means, it
would not generate its own successive determinations. The verse instead gives
both a positive logical form:

```text
what ceases
    determines the cessation

one path moment
    determines and is determined through another
```

This is where all four determinations become internal to Mārga:

```text
hetu
    the path-moment as reason and generative condition

phala
    the achieved path-bhūmi and its determinate cessation

āśraya
    the attained level as the concrete basis in which the Way operates

ālambana
    the path and cessation objectively determined as truth-fields
```

Cause and result are not two externally juxtaposed events. A produced path-
moment becomes a condition for a further path-moment; `phala` becomes a new
`hetu`. Nor are Basis and Support two inert poles. The achieved bhūmi is the
concrete `āśraya` from which the next determination operates, while the path
as known truth is its `ālambana`. The Way is their determinate unity at the
higher level.

This fourfold reconstruction develops the textual relations rather than
claiming that VAK 5.15 itself enumerates the four terms. The Bhāṣya's
`pratipakṣa` restriction prevents their unity from becoming abstract: each
relation must perform the determinate work appropriate to its realm.

The Subject consequently encounters neither a static Goal nor a prefabricated
road. Objectivity here includes both Theory—the path and cessation known as
truth—and Path-bhūmi—their achieved, supported actuality. In the Product, the
objective truth, the basis of its realization, its generative reason, and its
result reciprocally determine the concrete meaning of liberation. Telos
specifies what the Way must accomplish; the Way rises as the higher level in
which that truth becomes actual.

This is Organon reconstruction. Its textual ground is the own-level character
of cessation, the six- and nine-level differentiation of path, the causal
relation among path moments, and the Bhāṣya's counteragent restriction.

## 10. OWL++ Seed

```ttl
vak:VAK_5_15 a vak:Karika ;
    rdfs:label "VAK 5.15" ;
    vak:continues vak:VAK_5_14 ;
    vak:hasTopic vak:OwnLevelCessation,
                 vak:CausallyArticulatedPath .

vak:OwnLevelCessationRule a vak:SupportRangeRule ;
    vak:requires vak:AnusayaLevelIdentity ;
    vak:produces vak:CessationOfSameLevel ;
    vak:excludes vak:DifferentLevelCessation .

vak:SixLevelDharmajñanaPath
    a vak:UncontaminatedPathSupport ;
    vak:conditionFor vak:DesireRealmPathOrientedAnusaya ;
    vak:supportFor vak:DesireRealmPathOrientedAnusaya .

vak:NineLevelAnvayajnanaPath
    a vak:UncontaminatedPathSupport ;
    vak:conditionFor vak:FormRealmPathOrientedAnusaya,
                     vak:FormlessRealmPathOrientedAnusaya ;
    vak:supportFor vak:FormRealmPathOrientedAnusaya,
                  vak:FormlessRealmPathOrientedAnusaya .

vak:PathSupportAdmissibilityRule a vak:SupportRangeRule ;
    vak:requires vak:CausalPathRelation,
                 vak:AppropriateCounteragentFunction .

vak:CausallyArticulatedPath
    vak:hasMoment vak:PriorPathDetermination,
                  vak:SubsequentPathDetermination ;
    vak:hasRelation vak:MutualCausalConditioning .

vak:PathObjectivity a vak:HigherObjectivity ;
    vak:unifies vak:TheoreticalDetermination,
                vak:PathBhumiActualization ;
    vak:articulates vak:HetuFunction,
                    vak:PhalaFunction,
                    vak:AsrayaFunction,
                    vak:AlambanaFunction .
```

The seed keeps the verse's Condition relation and the Bhāṣya's Support relation
distinct while distinguishing terminal level-identity from generative
path-causality. It also represents Path Objectivity through all four functions, without
claiming that their Organon synthesis is an explicit four-term list in the
kārikā.
