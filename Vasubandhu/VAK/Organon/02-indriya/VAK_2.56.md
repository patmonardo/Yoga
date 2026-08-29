# VAK_2.56

## 1. Sanskrit (Devanāgarī)

> विपाकफलमन्त्यस्य पूर्वस्याधिपतं फलम् ।
>
> सभागसर्वत्रगयोर्निष्यन्दः पौरुषं द्वयोः ॥ २.५६ ॥

## 2. Sanskrit (IAST)

> vipākaphalam antyasya pūrvasyādhipataṃ phalam /
>
> sabhāgasarvatragayor niṣyandaḥ pauruṣaṃ dvayoḥ // 2.56 //

## 3. Padaccheda

```text
vipākaphalam             → vipāka-phalam
antyasya                 → antyasya
pūrvasyādhipatam         → pūrvasya adhipatam
phalam                   → phalam
sabhāgasarvatragayoḥ     → sabhāga-sarvatragayoḥ
niṣyandaḥ                → niṣyandaḥ
pauruṣam                 → pauruṣam
dvayoḥ                   → dvayoḥ
```

| Form | Morphology | Lexical force here |
|---|---|---|
| vipāka-phalam | nominative/accusative neuter singular compound | maturation-fruit |
| antyasya | genitive masculine singular | of the last [cause] |
| pūrvasya | genitive masculine singular | of the first [cause] |
| adhipatam phalam | nominative/accusative neuter singular phrase | fruit of predominance |
| sabhāga-sarvatragayoḥ | genitive masculine dual compound | of the homogeneous and pervasive causes |
| niṣyandaḥ | nominative masculine singular | homogeneous-outflow fruit |
| pauruṣam | nominative/accusative neuter singular | fruit of efficacious activity |
| dvayoḥ | genitive masculine dual | of the two [remaining causes] |

`Antya` and `pūrva` point back to the ordering of the six causes in VAK 2.49:
the last is maturation cause and the first is conditioning cause. `Dvayoḥ`
denotes the co-arisen and associated causes left after the other four have
been assigned their principal fruits.

## 4. Grammar

The first half contains two parallel genitive assignments:

```text
antyasya [hetoḥ]
    → vipāka-phalam

pūrvasya [hetoḥ]
    → adhipatam phalam
```

The second half completes the mapping:

```text
sabhāga-sarvatragayoḥ
    → niṣyandaḥ [phalam]

dvayoḥ [sahabhū-saṃprayuktakayoḥ]
    → pauruṣam [phalam]
```

The ellipses are resolved through the sixfold list and the Bhāṣya. The verse
assigns principal fruit-types; it does not grammatically assert that every
cause can have only the one fruit named here.

## 5. Translation

### Close syntactic construe

> The last [cause] has maturation as its fruit; the first has predominance as its fruit. The homogeneous and pervasive [causes] have homogeneous outflow; the two [remaining causes] have the fruit of efficacious activity.

### Bhāṣya-informed translation

> Maturation cause is principally distinguished by maturation-fruit, and conditioning cause by the fruit of predominance. Homogeneous and pervasive causes principally yield homogeneous outflow, while co-arisen and associated causes yield the fruit of operative efficacy. These are defining mappings rather than an exclusive one-to-one table: several causes can also possess a fruit of efficacious activity when their function produces a simultaneous or immediately subsequent result.

## 6. Philosophical Translation

> A cause is not fully comprehended until the form in which its efficacy becomes manifest is determined. Ground may appear in its result as delayed maturation, enabling predominance, homogeneous continuation, or present operative activity. The same event can stand within several such rational relations without those relations becoming interchangeable.

The four modes are:

```text
vipāka:
    delayed, individually appropriated maturation

adhipati:
    enabling, directing, assisting, or not obstructing

niṣyanda:
    continuation through relevant similarity

pauruṣa:
    manifestation of a dharma's operative efficacy
```

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this unit |
|---|---|---|
| vipāka-phala | maturation-fruit | later, non-common result arising from a morally determinate cause |
| adhipati-phala | fruit of predominance | result enabled, supported, directed, or permitted by conditioning cause |
| niṣyanda-phala | homogeneous-outflow fruit | result similar to its cause in the relevant indexed respects |
| pauruṣa-phala | fruit of efficacious activity | result of a dharma's operative function, normally simultaneous or immediately subsequent |
| puruṣakāra | efficacious activity | figurative person-like activity attributed to a dharma's causal function |
| vipāka-hetu | maturation cause | last member of the six-cause list |
| kāraṇa-hetu | conditioning cause | first member of the six-cause list |
| adhipati | predominance | ranges from non-obstruction to positive direct or indirect assistance |
| sattvākhyā | associated with a sentient being | required individual-continuum status of strict maturation-fruit |
| anivṛtāvyākṛta | unobscured-indeterminate | ethical status of maturation-fruit |
| asādhāraṇa | non-common | individually appropriated and not experienced by another continuum |
| sādhāraṇa-karma | common karma | cause of shared environmental or receptacle-world results |

`Pauruṣa` should not be rendered simply as “human result.” The Bhāṣya marks
the expression as figurative: it concerns operative efficacy analogous to a
person's activity.

`Adhipati` likewise does not require forceful production. Non-obstruction is
already its minimal form; principal conditioning causes may add positive
assistance.

## 8. Logical Determination

The principal mapping table is:

| Cause | Principal fruit |
|---|---|
| `vipāka-hetu` | `vipāka-phala` |
| `kāraṇa-hetu` | `adhipati-phala` |
| `sabhāga-hetu` | `niṣyanda-phala` |
| `sarvatraga-hetu` | `niṣyanda-phala` |
| `sahabhū-hetu` | `pauruṣa-phala` |
| `saṃprayuktaka-hetu` | `pauruṣa-phala` |

This is a principal-role relation:

```text
PrincipalFruitType(causeType, fruitType)
```

It is not an exclusive function:

```text
PrincipalFruitType(c, f)
    ⇏ HasNoOtherFruitType(c)
```

The Bhāṣya's broader activity rule is:

```text
OperativeFunction(c, r)
AND (Simultaneous(r, c) OR ImmediatelyAfter(r, c))
    → PaurushaFruit(r, c)
```

Maturation cause is normally excluded because its defining fruit is delayed:

```text
VipakaHetu(c)
AND TemporallyDistant(r, c)
    → NOT ImmediatePaurushaFruit(r, c)
```

An alternative view admits a distant fruit of activity for maturation cause,
like crops as the fruit of a farmer's work. This is reported, not adopted as
the principal definition.

Strict maturation-fruit requires:

```text
UnobscuredIndeterminate(r)
AND AssociatedWithSentientContinuum(r)
AND ArisesLaterFromMorallyDeterminateCause(r, c)
AND NonCommon(r)
    → VipakaFruit(r, c)
```

Shared environment is distinguished:

```text
ProducedByCommonKarma(world)
    → AdhipatiFruit(world)
    AND Common(world)
    AND NOT StrictIndividualVipakaFruit(world)
```

Similarity for homogeneous outflow is indexed:

```text
SabhagaHetu(c, r)
    → SameRelevantType(c, r)

SarvatragaHetu(c, r)
    → SameLevel(c, r)
    AND Afflicted(c)
    AND Afflicted(r)
    BUT MAYBE NOT SameSpecificAfflictionType(c, r)
```

## 9. Interpretive Note

VAK 2.56 converts the cause inventory into a cause-fruit schema. The crucial
advance is not that every input receives an output label. It is that each
fruit expresses a different way in which causal ground becomes manifest.

```text
CauseOccurrence
    → PrincipalFruitProfile
    + AdditionalApplicableFruitProfiles
    + TemporalRelation
    + AppropriationScope
    + SimilarityDimensions
```

That prevents two opposite errors. A one-to-one table would conceal the
Bhāṣya's admission that several causes also exercise efficacious activity. A
single generic `result` edge would erase the distinctions the table exists to
establish.

The `adhipati` discussion returns to the broad conditioning field:

```text
minimal predominance
    = not blocking the arising

positive predominance
    = directly or indirectly assisting it
```

The ten sense-spheres can predominate with respect to the five sensory
cognitions; karma can predominate with respect to the shared receptacle-world;
hearing can indirectly occasion the desire to see. Predominance is therefore
an enabling topology, not merely efficient force.

Maturation introduces individual appropriation. A strict maturation-fruit
belongs to the sentient continuum whose morally determinate karma matured:

```text
AgentA's karma
    → AgentA's non-common maturation

AgentA's karma
    ↛ AgentB's individual maturation
```

Common karma can nevertheless condition a shared world as a fruit of
predominance. The Ocular Schema must distinguish private-continuum provenance
from shared-environment provenance.

The earlier software analogy also acquires a result-type layer:

```text
yield same causal kind      → niṣyanda
return matured result       → vipāka
enable another operation    → adhipati
execute present function    → pauruṣa
```

These remain explanatory analogies. Their value is to prevent one software
method named `cause()` from hiding four logically different manifestations.

The textual layers are:

```text
kārikā
    → assigns principal fruits to the six causes

Bhāṣya
    → qualifies the mapping, defines the four fruits,
      distinguishes common and non-common results,
      and indexes similarity

Organon reconstruction
    → requires a qualified many-to-many cause-fruit schema
      with temporal, appropriation, and similarity profiles
```

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .

vak:VipakaFruit a organon:FruitType .
vak:AdhipatiFruit a organon:FruitType .
vak:NisyandaFruit a organon:FruitType .
vak:PaurushaFruit a organon:FruitType .

vak:VipakaHetu organon:hasPrincipalFruitType vak:VipakaFruit .
vak:KaranaHetu organon:hasPrincipalFruitType vak:AdhipatiFruit .
vak:SabhagaHetu organon:hasPrincipalFruitType vak:NisyandaFruit .
vak:SarvatragaHetu organon:hasPrincipalFruitType vak:NisyandaFruit .
vak:SahabhuHetu organon:hasPrincipalFruitType vak:PaurushaFruit .
vak:SamprayuktakaHetu organon:hasPrincipalFruitType vak:PaurushaFruit .

organon:hasPrincipalFruitType a organon:ObjectProperty .
organon:hasAdditionalFruitType a organon:ObjectProperty .
organon:hasTemporalRelation a organon:ObjectProperty .
organon:hasAppropriationScope a organon:ObjectProperty .
organon:hasSimilarityProfile a organon:ObjectProperty .

organon:IndividualMaturation a organon:NonCommonResult .
organon:ReceptacleWorld a organon:CommonResult .

organon:OcularCauseFruitSchema a organon:OcularSchema ;
    organon:requires organon:CauseType,
        organon:PrincipalFruitType,
        organon:AdditionalFruitType,
        organon:TemporalRelation,
        organon:AppropriationScope,
        organon:SimilarityProfile .
```
