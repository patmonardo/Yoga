# VAK_2.49

## 1. Sanskrit (Devanāgarī)

> कारणं सहभूश्चैव सभागः संप्रयुक्तकः ।
>
> सर्वत्रगो विपाकाख्यः षड्विधो हेतुरिष्यते ॥ २.४९ ॥

## 2. Sanskrit (IAST)

> kāraṇaṃ sahabhūś caiva sabhāgaḥ saṃprayuktakaḥ /
>
> sarvatrago vipākākhyaḥ ṣaḍvidho hetur iṣyate // 2.49 //

## 3. Padaccheda

```text
kāraṇam             → kāraṇam
sahabhūś            → sahabhūḥ
caiva                → ca eva
sabhāgaḥ             → sabhāgaḥ
saṃprayuktakaḥ       → saṃprayuktakaḥ
sarvatragaḥ          → sarvatragaḥ
vipākākhyaḥ          → vipāka-ākhyaḥ
ṣaḍvidhaḥ            → ṣaṭ-vidhaḥ
hetur                → hetuḥ
iṣyate               → iṣyate
```

| Form | Morphology | Lexical force here |
|---|---|---|
| kāraṇam | nominative/accusative neuter singular, used as the first causal name | conditioning cause |
| sahabhūḥ | nominative masculine singular | co-arisen cause |
| ca eva | conjunction plus emphatic particle | and indeed |
| sabhāgaḥ | nominative masculine singular | homogeneous cause |
| saṃprayuktakaḥ | nominative masculine singular | associated cause |
| sarvatragaḥ | nominative masculine singular | pervasive cause |
| vipāka-ākhyaḥ | nominative masculine singular compound | called maturation [cause] |
| ṣaṭ-vidhaḥ | nominative masculine singular compound | sixfold |
| hetuḥ | nominative masculine singular | cause / causal ground |
| iṣyate | third-person singular present passive of √`iṣ` | is accepted / is held to be |

`Kāraṇam` is the lexicalized name of the first cause; the remaining names are
masculine epithets of the understood `hetuḥ`. The verse enumerates all six but
does not yet define five of them.

## 4. Grammar

The verse is an enumerative nominal construction completed by one finite verb:

```text
kāraṇam
sahabhūḥ
sabhāgaḥ
saṃprayuktakaḥ
sarvatragaḥ
vipāka-ākhyaḥ
    → ṣaḍvidhaḥ hetuḥ iṣyate

[these six]
    → cause is held to be sixfold
```

`Ca eva` emphasizes the inclusion of the co-arisen cause while linking the
series. `Vipākākhyaḥ` is a dependent determinative compound:

```text
vipāka + ākhya
    → bearing the name “maturation”
```

The passive `iṣyate` marks an accepted doctrinal enumeration rather than
asserting that the sixfold list has been demonstrated within the kārikā. The
Bhāṣya begins the demonstration with only its first member, `kāraṇa-hetu`.

## 5. Translation

### Close syntactic construe

> Conditioning, co-arisen, homogeneous, associated, pervasive, and that called maturation: cause is held to be sixfold.

### Bhāṣya-informed translation

> The Kośa accepts six distinct causes: the conditioning cause, co-arisen cause, homogeneous cause, associated cause, pervasive cause, and maturation cause. The first is defined broadly by non-obstruction with respect to a dharma actually arising; its principal instances additionally possess productive efficacy.

## 6. Philosophical Translation

> A conditioned event is not comprehended by attaching the undifferentiated label “cause” to whatever preceded it. Causal intelligibility requires distinct forms of dependence. Even the broadest causal field must distinguish what merely permits an arising from what positively contributes to its production.

The first distinction is therefore:

```text
permissive causal field
    ≠
productive causal ground
```

The six causes are a typed causal schema, not six interchangeable names for
one relation.

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this unit |
|---|---|---|
| hetu | cause / causal ground | mode through which a conditioned dharma's arising is genetically explained |
| kāraṇa-hetu | conditioning cause | broadly, every other dharma insofar as it does not obstruct the arising; principally, a positively productive condition |
| sahabhū-hetu | co-arisen cause | mutually conditioning coexistence; enumerated here, analyzed subsequently |
| sabhāga-hetu | homogeneous cause | causal continuity of a relevantly similar type; enumerated here, analyzed subsequently |
| saṃprayuktaka-hetu | associated cause | causal association, especially among citta and caittas; enumerated here, analyzed subsequently |
| sarvatraga-hetu | pervasive cause | pervasive afflicted causality; enumerated here, analyzed subsequently |
| vipāka-hetu | maturation cause | karmically determinate cause of maturation-result; enumerated here, analyzed subsequently |
| avighna-bhāva | state of non-obstruction | Bhāṣya definition of `kāraṇa-hetu` in its broad scope |
| vighna | obstruction | capacity or operation that blocks an arising |
| utpādana-sāmarthya | capacity for production | positive efficacy belonging to principal conditioning causes |
| kāraṇa-paramparā | succession of causes | mediated causal series invoked by an attributed alternative view |

`Hetu` should not be inflated into an absolute metaphysical Ground in the
primary translation. Here it belongs to the Kośa's analysis of conditioned
arising. Conversely, “cause” must not conceal the qualitative differences
among the six causal types.

## 8. Logical Determination

The kārikā declares the type system:

```text
HetuType :=
    Karana
  | Sahabhu
  | Sabhaga
  | Samprayuktaka
  | Sarvatraga
  | Vipaka
```

Only `kāraṇa-hetu` is unfolded in this Bhāṣya unit. Its broad rule is:

```text
Conditioned(x)
AND Dharma(y)
AND y ≠ x
AND ActuallyArising(x)
AND NOT Obstructs(y, Arising(x))
    → BroadKaranaHetu(y, x)
```

The qualification `ActuallyArising(x)` matters. Knowledge can obstruct the
arising of a defilement that otherwise might arise, but this does not refute
the definition concerning the causal field of the event that does arise.

Principal conditioning causes add positive efficacy:

```text
EyeFaculty + VisibleForm
    → ProductivelyConditions(VisualCognition)

Food
    → ProductivelyConditions(Body)

Seed
    → ProductivelyConditions(Sprout)
```

Thus:

```text
PrincipalKaranaHetu(y, x)
    → BroadKaranaHetu(y, x)
    AND ProductivelyContributes(y, Arising(x))

BroadKaranaHetu(y, x)
    ⇏ ProductivelyContributes(y, Arising(x))
```

This blocks two invalid inferences:

```text
NonObstruction(y, x)
    ⇏ simultaneous production of x by y

NonObstruction(person, action)
    ⇏ agency or moral authorship of that action
```

An attributed alternative view gives every conditioning cause mediated
efficacy through a causal succession:

```text
ObjectOf(Nirvana, MentalCognition₁)
    → ... causal sequence ...
    → VisualCognitionₙ
```

That universal-efficacy thesis is reported by the Bhāṣya as the position of
others; it is not silently adopted as the verse's definition.

## 9. Interpretive Note

VAK 2.49 opens the causal section because VAK 2.46 had already made causes
and conditions indispensable to arising, while VAK 2.48 assigned different
result-statuses to structural determinations. The question now becomes
unavoidable:

```text
By what typed causal relation did this result arise?
```

The answer begins by refusing a damaged schema in which every dependency is
stored as the same generic edge. `Hetu` is a sum type whose members must retain
their own logical behavior. Even within its first member, the Bhāṣya exposes
two levels:

```text
KāraṇaHetu {
    broad: nonObstruction,
    principal: productiveEfficacy
}
```

This is important for an Ocular Schema. A causal record should state whether
something merely belongs to the permissive field, positively produces the
event, operates through a mediated sequence, or belongs to one of the other
five causal forms. Otherwise the database hides the very logical schema that
the Kośa labors to disclose.

The faculty example is especially significant:

```text
eye + visible form → visual cognition
```

The Indriya does not act alone, and Citta does not act as an unexplained
sovereign. Faculty, registered field, and differentiated cognition belong to
a typed causal enclosure. The forthcoming analysis can therefore specify how
the Indriya architecture gives lawful form to appearance without denying
Citta's participation in its constitution.

The six `hetus` remain held apart from the `pratyayas` at this stage. Neither
their later conjunction nor Samādhi should be projected into VAK 2.49. This
verse first establishes the causal types; their relations must be earned by
the subsequent analysis.

The textual layers remain distinct:

```text
kārikā
    → enumerates six causes

Bhāṣya
    → analyzes kāraṇa-hetu through non-obstruction,
      productive efficacy, objections, and an alternative view

Organon reconstruction
    → treats the distinctions as requirements for an explicit
      Ocular causal schema
```

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .

vak:Hetu a organon:CausalRelationType .
vak:KaranaHetu a vak:Hetu .
vak:SahabhuHetu a vak:Hetu .
vak:SabhagaHetu a vak:Hetu .
vak:SamprayuktakaHetu a vak:Hetu .
vak:SarvatragaHetu a vak:Hetu .
vak:VipakaHetu a vak:Hetu .

organon:NonObstruction a organon:PermissiveCausalRelation .
organon:ProductiveEfficacy a organon:ProductiveCausalRelation .
organon:MediatedCausalSuccession a organon:CausalPath .

vak:KaranaHetu
    organon:broadCriterion organon:NonObstruction ;
    organon:principalCriterion organon:ProductiveEfficacy .

organon:actuallyArising a organon:ObjectProperty .
organon:doesNotObstruct a organon:ObjectProperty .
organon:productivelyContributesTo a organon:ObjectProperty .
organon:hasCausalType a organon:ObjectProperty .
organon:hasCausalProvenance a organon:ObjectProperty .

organon:OcularCausalSchema a organon:Schema ;
    organon:requires vak:Hetu,
        organon:CausalProvenance,
        organon:PermissiveCausalRelation,
        organon:ProductiveCausalRelation .
```
