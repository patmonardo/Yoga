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

The verse specifies the object-range of the cessation-oriented and
path-oriented anuśayas identified in VAK 5.14.

## 3. Padaccheda and Lexical Analysis

```text
sva-bhūmi-uparamaḥ | mārgaḥ | ṣaḍ-bhūmiḥ | nava-bhūmikaḥ |
tad-gocarāṇām | viṣayaḥ | mārgaḥ | hi | anyaḥ | anya-hetukaḥ
```

| Form | Morphology | Contextual sense |
|---|---|---|
| `sva-bhūmi-uparamaḥ` | nominative singular masculine compound | cessation belonging to its own level |
| `mārgaḥ` | nominative singular masculine | path |
| `ṣaḍ-bhūmiḥ` | nominative singular masculine compound | belonging to six levels |
| `nava-bhūmikaḥ` | nominative singular masculine adjective | belonging to nine levels |
| `tad-gocarāṇām` | genitive plural | of those whose cognitive range is that |
| `viṣayaḥ` | nominative singular masculine | object, determinate field |
| `hi` | explanatory particle | for, because |
| `anyaḥ anya-hetukaḥ` | nominative singular construction | one has another as cause; one is causally related to another |

The compact first pāda requires the Bhāṣya to distribute the six- and
nine-level predicates. They do not qualify cessation: they distinguish two
sides of the path and their corresponding afflicted object-relations.

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
is the object of those whose range is that
```

The Bhāṣya resolves the compressed construction: the six-level
`dharmajñāna` side is the object for desire-domain path-oriented anuśayas; the
nine-level `anvayajñāna` side is the object for those of the form and formless
domains.

**Causal rationale**

```text
mārgaḥ hi anyaḥ anya-hetukaḥ

for one path has another as cause
```

The distributive force of `anyaḥ ... anya-` expresses causal connection among
distinct path moments. The Bhāṣya also speaks of mutual causality, while still
restricting object-range according to counteragent function.

## 5. Translation

### Literal Translation

> Cessation is the cessation of its own level. The path, belonging to six
> levels or nine levels, is the object of those whose range is that; for one
> path has another as cause.

### Bhāṣya-informed study translation

> An anuśaya taking cessation as object takes only the cessation of its own
> level. For desire-domain anuśayas taking path as object, the six-level path
> on the side of `dharmajñāna` is their cognitive support. For path-oriented
> anuśayas of the form and formless domains, the nine-level path on the side of
> `anvayajñāna` is their support, because distinct path moments stand in causal
> relations to one another.

The allocation of the two level-counts and the restriction by counteragent
function are supplied by the Bhāṣya.

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

For an anuśaya belonging to the desire domain, only cessation of the desire
domain is its cessation-object; the same own-level rule continues through the
summit of existence. Cessation is determinate termination, not bare absence.

**`Bhūmi` — level or stage**

Here `bhūmi` indexes the differentiated domains in which affliction,
counteraction, and cessation are situated. It should not be flattened into a
mere spatial location.

**`Dharmajñāna-pakṣa` — the dharma-knowledge side of the path**

The Bhāṣya assigns this six-level path to the object-range of desire-domain
path-oriented anuśayas. Its fuller determination belongs to the later Path
and Knowledge chapters.

**`Anvayajñāna-pakṣa` — the subsequent or corresponding-knowledge side**

The Bhāṣya assigns this nine-level path to the object-range of form- and
formless-domain path-oriented anuśayas, including levels not directly seen.
The provisional English remains subordinate to its later technical analysis.

**`Pratipakṣa` — counteragent**

Object-range is not established by causal connectedness alone. The Bhāṣya
notes that `anvayajñāna` is not the counteragent to the desire domain; hence
desire-domain path-oriented anuśayas do not take that side as support.

**`Anyo 'nya-hetuka` — one path caused by another**

Path is internally causal. Distinct path determinations can condition one
another, giving the Way a systematic range that cessation, as own-level
termination, does not possess.

**`Gocara`, `viṣaya`, and `ālambana`**

The kārikā uses `gocara` and `viṣaya`; the Bhāṣya explains the relation through
`ālambana`. All concern cognitive range here, but their syntactic roles remain
distinct: the anuśaya has a range, while the determinate path is its object-
support.

## 8. Logical Determination

The cessation rule is indexical:

```text
BelongsToLevel(anuśaya, L)
AND HasObjectType(anuśaya, Cessation)
    → HasObjectSupport(anuśaya, CessationOf(L))
```

It excludes cross-level substitution:

```text
CessationOf(L1) ≠ CessationOf(L2)
    when L1 ≠ L2
```

The path rule is differentiated by domain:

```text
DesireDomain(x)
AND PathOriented(x)
    → HasObjectSupport(x, SixLevelDharmajñanaPath)

FormOrFormlessDomain(x)
AND PathOriented(x)
    → HasObjectSupport(x, NineLevelAnvayajnanaPath)
```

Causal relation is necessary but not sufficient for unrestricted range:

```text
CausallyRelated(PathA, PathB)
AND Counteracts(PathB, DomainOf(x))
    → AdmissiblePathObject(x, PathB)
```

Therefore:

```text
MutuallyCausal(Dharmajñana, Anvayajnana)
    ⇏ DesireDomainAnusayaTakes(Anvayajnana)
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
`hetu`. Nor are support and object two inert poles. The achieved bhūmi is the
concrete `āśraya` from which the next determination operates, while the path
as known truth is its `ālambana`. The Way is their determinate unity at the
higher level.

This fourfold reconstruction develops the textual relations rather than
claiming that VAK 5.15 itself enumerates the four terms. The Bhāṣya's
`pratipakṣa` restriction prevents their unity from becoming abstract: each
relation must perform the determinate work appropriate to its domain.

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

vak:OwnLevelCessationRule a vak:ObjectRangeRule ;
    vak:requires vak:AnusayaLevelIdentity ;
    vak:produces vak:CessationOfSameLevel ;
    vak:excludes vak:DifferentLevelCessation .

vak:SixLevelDharmajñanaPath
    a vak:UncontaminatedPathObject ;
    vak:objectFor vak:DesireDomainPathOrientedAnusaya .

vak:NineLevelAnvayajnanaPath
    a vak:UncontaminatedPathObject ;
    vak:objectFor vak:FormDomainPathOrientedAnusaya,
                  vak:FormlessDomainPathOrientedAnusaya .

vak:PathObjectAdmissibilityRule a vak:ObjectRangeRule ;
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

The seed distinguishes terminal level-identity from generative path-causality.
It also represents Path Objectivity through all four functions, without
claiming that their Organon synthesis is an explicit four-term list in the
kārikā.
