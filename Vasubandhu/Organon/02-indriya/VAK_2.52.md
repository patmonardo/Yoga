# VAK_2.52

## 1. Sanskrit (Devanāgarī)

> सभागहेतुः सदृशाः स्वनिकायभुवोऽग्रजाः ।
>
> अन्योऽन्यं नवभूमिस्तु मार्गः समविशिष्टयोः ॥ २.५२ ॥

## 2. Sanskrit (IAST)

> sabhāgahetuḥ sadṛśāḥ svanikāyabhuvo 'grajāḥ /
>
> anyo 'nyaṃ navabhūmis tu mārgaḥ samaviśiṣṭayoḥ // 2.52 //

## 3. Padaccheda

```text
sabhāgahetuḥ          → sabhāga-hetuḥ
sadṛśāḥ               → sadṛśāḥ
svanikāyabhuvo        → sva-nikāya-bhuvaḥ
'grajāḥ               → agrajāḥ
anyo 'nyam            → anyaḥ anyam
navabhūmiḥ            → nava-bhūmiḥ
tu                    → tu
mārgaḥ                → mārgaḥ
samaviśiṣṭayoḥ        → sama-viśiṣṭayoḥ
```

| Form | Morphology | Lexical force here |
|---|---|---|
| sabhāga-hetuḥ | nominative masculine singular compound | homogeneous cause |
| sadṛśāḥ | nominative masculine plural adjective | similar dharmas |
| sva-nikāya-bhuvaḥ | nominative masculine plural compound | belonging to their own class and level |
| agrajāḥ | nominative masculine plural adjective | arisen previously / prior-born |
| anyaḥ anyam | reciprocal accusative construction | one another / each the other |
| nava-bhūmiḥ | nominative masculine singular compound | [the Path] belonging to nine levels |
| tu | adversative particle | but / however |
| mārgaḥ | nominative masculine singular | the Path |
| sama-viśiṣṭayoḥ | locative dual compound | with respect to the equal and the superior |

`Bhuvaḥ` is read with the Bhāṣya as level-membership (`sva-bhūmi`) joined to
class-membership (`sva-nikāya`). The first half uses plural predicates because
the prior similar dharmas are the members functioning under the singular
causal type `sabhāga-hetu`.

## 4. Grammar

The ordinary rule is a compact nominal definition:

```text
sadṛśāḥ
sva-nikāya-bhuvaḥ
agrajāḥ
    → sabhāga-hetuḥ

similar dharmas,
belonging to their own class and level,
and arisen previously
    → are homogeneous cause
```

All three restrictions are conjunctive. Resemblance without prior arising is
not enough, and prior arising without the relevant similarity and membership
is not `sabhāga-hetu`.

The second half introduces an exception with `tu`:

```text
nava-bhūmiḥ mārgaḥ
    → anyaḥ anyam [sabhāga-hetuḥ]
    → sama-viśiṣṭayoḥ

the Path across nine levels
    → [its members are] homogeneous causes for one another
    → with respect to equal or superior members
```

The reciprocal expression does not abolish temporal direction. The Bhāṣya
retains the requirement that an arisen Path-dharma grounds an unarisen future
Path-dharma; “one another” distributes causal reach across the nine levels.

## 5. Translation

### Close syntactic construe

> Similar [dharmas] that belong to their own class and level and have arisen previously are homogeneous cause. But the Path across the nine levels [serves] reciprocally [as homogeneous cause] with respect to what is equal or superior.

### Bhāṣya-informed translation

> An earlier dharma is homogeneous cause for a later similar dharma ordinarily only within its own class and meditative level. The Path is exceptional: because it is adventitious to the nine levels and is not appropriated by their respective cravings, a Path-dharma in one level can become homogeneous cause for a future Path-dharma in another—but only when the result is equal or superior, never deliberately inferior.

## 6. Philosophical Translation

> Homogeneous causality is the transmission of determinate capacity through time. Ordinary formations reproduce their type within an inherited class and level. Cultivated Path-form, however, can cross those level-bound enclosures because it operates within them without belonging to their craving. Its continuation is developmental rather than merely repetitive: an achieved form grounds what preserves or intensifies it.

The causal direction is:

```text
prior similar determination
    → equal later determination
    OR
    → superior later determination

superior cultivated determination
    ↛ deliberately inferior homogeneous result
```

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this unit |
|---|---|---|
| sabhāga-hetu | homogeneous cause | prior similar dharma genetically continuing into a later similar dharma |
| sadṛśa | similar | qualitative correspondence required for homogeneous causality |
| sva-nikāya | own class / own group | ordinary class-bound restriction upon the causal series |
| sva-bhūmi | own level / plane | ordinary level-bound restriction upon the causal series |
| agraja | prior-born | temporal priority belonging to the definition of the cause |
| mārga | Path | conditioned liberating series able to cross the nine levels |
| nava-bhūmi | nine levels | preliminary concentration, intermediate concentration, four concentrations, and three formless attainments |
| āgantuka | adventitious / not native | present within a level without appropriation by its craving |
| sama-viśiṣṭa | equal or superior | permitted qualitative direction of Path causality |
| hetūpacaya | accumulation of causes | strengthening that determines relative equality or superiority |
| prayogaja | produced through application | quality generated through deliberate practice rather than birth alone |
| śrutamayī | born of hearing | learned quality whose causal reach varies by realm |
| cintāmayī | born of reflection | reflected quality admitted in the desire realm in this matrix |
| bhāvanāmayī | born of cultivation | cultivated quality operating in the form and formless realms |
| upapatti-pratilambhika | obtained through birth | naturally acquired quality contrasted with deliberate application |

`Agraja` is temporal, not merely logical, priority. `Sabhāga` therefore names
a serial causal relation rather than static resemblance.

`Āgantuka` does not mean that the Path is external to conditioned experience.
It operates in the levels but is not owned by the craving that ordinarily
fixes a dharma to one of them.

## 8. Logical Determination

The ordinary rule is:

```text
Similar(x, y)
AND SameClass(x, y)
AND SameLevel(x, y)
AND PriorTo(x, y)
    → SabhagaHetu(x, y)
```

The Path relaxes only the same-level restriction:

```text
PathDharma(x)
AND PathDharma(y)
AND InNinePathLevels(x, y)
AND PriorTo(x, y)
AND Grade(x) ≤ Grade(y)
    → SabhagaHetu(x, y)
```

Its mobility is grounded in non-appropriation:

```text
PathDharma(x)
AND LocatedIn(x, level)
AND NOT AppropriatedBy(CravingOf(level), x)
    → AdventitiousTo(x, level)
```

The principal monotonicity constraint is:

```text
ProducedThroughApplication(x)
AND SabhagaHetu(x, y)
    → Grade(y) ≥ Grade(x)
```

The Path divisions have decreasing forward reach:

```text
PathOfSeeing      → seeing, cultivation, no-more-learning
PathOfCultivation → cultivation, no-more-learning
PathOfNoMoreLearning → no-more-learning
```

Faculty grade further restricts transmission:

```text
WeakFacultyPath  → weak OR sharp future Path
SharpFacultyPath → sharp future Path only
```

The modes of produced knowledge are realm-indexed:

```text
DesireRealm:
    Hearing    → Hearing OR Reflection
    Reflection → Reflection

FormRealm:
    Hearing     → Hearing OR Cultivation
    Cultivation → Cultivation

FormlessRealm:
    Cultivation → Cultivation
```

These matrices are Bhāṣya determinations. The kārikā itself gives the compact
ordinary rule and the equal-or-superior Path exception.

## 9. Interpretive Note

VAK 2.52 turns homogeneous outflow into an explicitly genetic series. The
cause must be earlier, similar, and normally enclosed within the same class
and level. A homogeneous stream therefore does not merely emit repeated
tokens; it transmits a determinate capacity under typed constraints.

The Python `yield` analogy now becomes stronger but also more exact:

```python
def cultivated_path(current):
    while current.has_future_path:
        future = current.next_equal_or_superior()
        yield future
        current = future
```

The stateful generator preserves provenance from an earlier determination to
a later one. The Path adds a monotonic grade constraint. Yet `sabhāga-hetu`
is a doctrinal causal relation, not literally a computation, and ordinary
birth-acquired or defiled series obey different matrices.

The most important determination is the Path's `āgantuka` status:

```text
operative within a Bhūmi
    + not appropriated by that Bhūmi's craving
    = able to transmit across Bhūmis
```

This is not yet an escape from conditioned reality. It is a conditioned
series whose causal membership is no longer fixed by ordinary realm-belonging.
That makes Path knowledge technically visible as directed development rather
than a mysterious leap.

For an Ocular Schema, a homogeneous edge must therefore expose:

```text
source and target
temporal priority
similarity criterion
class membership
level membership
grade relation
mode of acquisition
appropriation status
```

Without those fields, “same kind” hides the actual causal Logic.

The reception question should remain historically separate. Later Yogācāra
appropriation of Kośa/Bhāṣya analysis can establish scholastic inheritance
without making Yogācāra identical with Sarvāstivāda. This verse itself
belongs to the causal system expounded and criticized within the Bhāṣya; it
does not state a later lineage relation.

The textual layers are:

```text
kārikā
    → defines ordinary homogeneous cause and the Path exception

Bhāṣya
    → supplies the nine levels, adventitious status, grades,
      Path divisions, faculty distinctions, and knowledge matrices

Organon reconstruction
    → models homogeneous causality as a typed,
      provenance-preserving, monotonic continuation
```

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .

vak:SabhagaHetu a organon:DiachronicCausalRelation .
vak:PathDharma a organon:ConditionedDetermination .
vak:PathLevel a organon:LevelType .
vak:AdventitiousToLevel a organon:MembershipStatus .

organon:priorTo a organon:TransitiveProperty .
organon:similarTo a organon:SymmetricProperty .
organon:belongsToClass a organon:ObjectProperty .
organon:belongsToLevel a organon:ObjectProperty .
organon:hasGrade a organon:ObjectProperty .
organon:hasAcquisitionMode a organon:ObjectProperty .
organon:appropriatedBy a organon:ObjectProperty .

vak:OrdinarySabhagaRule a organon:CausalRule ;
    organon:requires organon:TemporalPriority,
        organon:Similarity,
        organon:SameClass,
        organon:SameLevel .

vak:PathSabhagaRule a organon:CausalRule ;
    organon:requires organon:TemporalPriority,
        organon:PathSimilarity,
        organon:EqualOrSuperiorGrade,
        vak:AdventitiousToLevel ;
    organon:relaxes organon:SameLevel .

organon:OcularHomogeneousSchema a organon:OcularSchema ;
    organon:requires organon:CausalProvenance,
        organon:TemporalPriority,
        organon:Similarity,
        organon:ClassMembership,
        organon:LevelMembership,
        organon:GradeRelation,
        organon:AcquisitionMode,
        organon:AppropriationStatus .
```
