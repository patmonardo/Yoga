# VAK_2.59

## 1. Sanskrit (Devanāgarī)

> वर्तमानाः फलं पञ्च गृह्णन्ति द्वौ प्रयच्छतः ।
>
> वर्तमानाभ्यतीतौ द्वौ एकोऽतीतः प्रयच्छति ॥ २.५९ ॥

## 2. Sanskrit (IAST)

> vartamānāḥ phalaṃ pañca gṛhṇanti dvau prayacchataḥ /
>
> vartamānābhyatītau dvau eko 'tītaḥ prayacchati // 2.59 //

## 3. Padaccheda

```text
vartamānāḥ           → vartamānāḥ
phalam               → phalam
pañca                 → pañca
gṛhṇanti              → gṛhṇanti
dvau                  → dvau
prayacchataḥ          → prayacchataḥ
vartamānābhyatītau    → vartamānau abhyatītau
dvau                  → dvau
ekaḥ                  → ekaḥ
atītaḥ                → atītaḥ
prayacchati           → prayacchati
```

| Form | Morphology | Lexical force here |
|---|---|---|
| vartamānāḥ | nominative masculine plural | being present / presently occurring |
| phalam | accusative neuter singular | fruit / result |
| pañca | nominative masculine plural | five causes |
| gṛhṇanti | third-person plural present active of √`grah` | take, acquire a determinate relation to |
| dvau | nominative masculine dual | two causes |
| prayacchataḥ | third-person dual present active of `pra-√yam` | give / deliver |
| vartamānau | nominative masculine dual | the two while present |
| abhyatītau | nominative masculine dual | the same two when past |
| ekaḥ | nominative masculine singular | one cause |
| atītaḥ | nominative masculine singular | being past |
| prayacchati | third-person singular present active | gives / brings its result to manifestation |

The compact compound-like sequence `vartamānābhyatītau` coordinates two
temporal qualifications of the following dual `dvau`: the two give both while
present and when past. The final singular then isolates the maturation cause.

## 4. Grammar

The first pāda places the temporal predicate before its counted subject:

```text
vartamānāḥ pañca
    phalaṃ gṛhṇanti

five, while present,
    take fruit
```

The remainder distributes fruit-giving through three constructions:

```text
dvau [vartamānau] prayacchataḥ
    → two give while present

dvau vartamānau abhyatītau [prayacchataḥ]
    → two give while present and when past

ekaḥ atītaḥ prayacchati
    → one gives when past
```

The first `dvau` is supplied with `vartamānau` from the opening qualification,
as the Bhāṣya confirms. Number performs the doctrinal classification: five
take, two give simultaneously, two can give across present and past, and one
gives only after passing into the past.

## 5. Translation

### Close syntactic construe

> Five, being present, take fruit; two give [it while present]. Two give [it]
> while present and when past; one, being past, gives [it].

### Bhāṣya-informed translation

> Five of the causes assume seed-status toward their fruits only while present.
> The co-arisen and associated causes also manifest their fruits while present;
> the homogeneous and pervasive causes can manifest theirs while present or
> past; and the maturation cause manifests its fruit only after it is past.

## 6. Philosophical Translation

> A cause first becomes determinately capable of a result and then, according
> to its causal type, brings that result to manifestation. Some causes contain
> these moments in one present conjunction; some continue into an immediately
> succeeding occurrence; maturation requires temporal distance. Causal law is
> therefore internally temporal, not an abstract link between finished things.

```text
take fruit
    = assume seed-status toward a determinate result

give fruit
    = the determinate result becomes manifest
```

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this unit |
|---|---|---|
| phala-grahaṇa | taking fruit | becoming a seed determinately ordered toward a fruit |
| phala-pradāna | giving fruit | actual manifestation of the causally determined fruit |
| bījabhāvopagama | assumption of seed-status | Bhāṣya definition of taking fruit |
| vartamāna | present | phase of current causal operation |
| atīta / abhyatīta | past | phase in which the cause has ceased as present but may give fruit |
| sahabhū-hetu | co-arisen cause | takes and gives fruit in the present |
| saṃprayuktaka-hetu | associated cause | takes and gives fruit in the present |
| sabhāga-hetu | homogeneous cause | takes in the present; gives in the present or past |
| sarvatraga-hetu | pervasive cause | takes in the present; gives in the present or past |
| vipāka-hetu | maturation cause | takes in the present; gives only when past |
| kāraṇa-hetu | conditioning cause | omitted from the fixed count because it does not invariably have a fruit |
| niṣpuruṣakāratva | absence of operative activity | reason a future cause cannot yet take fruit |

`Bīja` here is not a tiny substance stored somewhere in the continuum. It is
the determinate causal status assumed by a presently operative dharma with
respect to a fruit. The Bhāṣya, not the kārikā alone, supplies this definition.

## 8. Logical Determination

The six causes form a temporally typed causal matrix:

| Cause | Takes fruit | Gives fruit | Temporal form |
|---|---|---|---|
| co-arisen | present | present | simultaneous |
| associated | present | present | simultaneous |
| homogeneous | present | present or past | immediately successive continuity |
| pervasive | present | present or past | immediately successive continuity |
| maturation | present | past only | temporally non-immediate maturation |
| conditioning | present when fruit-determinate | variable | excluded from the invariant enumeration |

```text
Present(cause)
AND DeterminatelyOrderedToward(cause, fruit)
    → TakesFruit(cause, fruit)

ManifestsThrough(fruit, cause, time)
    → GivesFruit(cause, fruit, time)
```

The implication is asymmetrical:

```text
GivesFruit(cause, fruit)
    → TakesFruit(cause, fruit)

TakesFruit(cause, fruit)
    ↛ GivesFruit(cause, fruit)
```

The Bhāṣya's final aggregates of an arhat instantiate the second case: they can
assume causal determination without a later continuation in which that fruit
is delivered.

The homogeneous and pervasive cases require precision. “Giving while
present” describes a causal sequence whose fruit arises immediately after the
cause. It does not make two successive moments numerically simultaneous. By
the time the fruit is arisen, both occurrences can be spoken of as past, yet
the fruit is not given a second time.

## 9. Interpretive Note

VAK 2.59 converts the earlier inventory of causes and fruits into a small
temporal instruction set. Cause-type determines not merely *which* result
relation holds but *when* its two operations are licensed:

```text
CausalInstruction {
    causeType,
    resultType,
    takePhase,
    givePhase,
    successionMode,
    evidence
}
```

This is the beginning of a karmic ISA only in the Organon reconstruction. The
kārikā itself gives the scheduling constraints; the Bhāṣya identifies taking
with seed-status and works through the fourfold alternatives. An Ocular Schema
must preserve those layers and must not flatten `takesFruit` and `givesFruit`
into a generic `causes` edge.

The temporal distinctions also prevent premature importation of Samādhi. What
we have here is the articulation of the `hetu` side: causal capacity, its
temporal persistence, and result-manifestation. The forthcoming `pratyaya`
analysis supplies a different classification of conditional relations. Their
eventual systematic conjunction remains an Organon task, not a statement made
by this verse.

The Bhāṣya's four additional fruits—support, application, causal assemblage,
and cultivation—belong to “other teachers.” They record an alternative
extension of the fruit taxonomy and should not silently be merged into the
five-fruit system already analyzed.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .

vak:FruitTaking a organon:CausalOperation ;
    organon:definedBy vak:AssumptionOfSeedStatus .

vak:FruitGiving a organon:CausalOperation ;
    organon:definedBy vak:ResultManifestation .

vak:AssumptionOfSeedStatus a organon:GeneticDetermination .
vak:Present a organon:TemporalPhase .
vak:Past a organon:TemporalPhase .
vak:Simultaneous a organon:SuccessionMode .
vak:ImmediatelySuccessive a organon:SuccessionMode .
vak:TemporallyDistant a organon:SuccessionMode .

organon:takesFruit a organon:ObjectProperty .
organon:givesFruit a organon:ObjectProperty .
organon:licensedDuring a organon:ObjectProperty .
organon:hasSuccessionMode a organon:ObjectProperty .

vak:CoarisenCause organon:licensedDuring vak:Present ;
    organon:hasSuccessionMode vak:Simultaneous .

vak:AssociatedCause organon:licensedDuring vak:Present ;
    organon:hasSuccessionMode vak:Simultaneous .

vak:HomogeneousCause organon:hasSuccessionMode vak:ImmediatelySuccessive .
vak:PervasiveCause organon:hasSuccessionMode vak:ImmediatelySuccessive .
vak:MaturationCause organon:licensedDuring vak:Past ;
    organon:hasSuccessionMode vak:TemporallyDistant .

organon:TemporalCausalInstruction a organon:OcularSchema ;
    organon:requires organon:CauseType,
        organon:ResultType,
        organon:TakePhase,
        organon:GivePhase,
        organon:SuccessionMode,
        organon:ProvenanceEvidence .
```
