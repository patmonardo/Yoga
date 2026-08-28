# VAK_2.30

## 1. Sanskrit (Devanāgarī)

> निवृतेऽष्टादशान्यत्र द्वादशाव्याकृते मताः ।
>
> मिद्धं सर्वाविरोधित्वाद्यत्र स्यादधिकं हि तत् ॥ २.३० ॥

## 2. Sanskrit (IAST)

> nivṛte 'ṣṭādaśānyatra dvādaśāvyākṛte matāḥ /
>
> middhaṃ sarvāvirodhitvād yatra syād adhikaṃ hi tat // 2.30 //

The research witness separates `aṣṭādaśa anyatra`; the continuous sandhi
`aṣṭādaśānyatra` is displayed here without changing the lexical division.

## 3. Padaccheda

```text
nivṛte             → nivṛte
aṣṭādaśānyatra     → aṣṭādaśa anyatra
dvādaśāvyākṛte     → dvādaśa avyākṛte
matāḥ              → matāḥ
middhaṃ            → middham
sarvāvirodhitvād   → sarva-avirodhitvāt
yatra              → yatra
syād               → syāt
adhikaṃ            → adhikam
hi                 → hi
tat                → tat
```

| Form | Morphology | Lexical force here |
|---|---|---|
| nivṛte | locative neuter singular | in the obscured [indeterminate state] |
| aṣṭādaśa | numeral | eighteen |
| anyatra | indeclinable | in the other case / elsewhere |
| dvādaśa | numeral | twelve |
| avyākṛte | locative neuter singular | in the karmically indeterminate |
| matāḥ | nominative masculine plural past passive participle | are held / accepted [as the mental factors] |
| middham | nominative neuter singular | sleepiness / torpor |
| sarva-avirodhitvāt | ablative singular abstract compound | because of compatibility with all / non-opposition to all |
| yatra | relative adverb | wherever |
| syāt | third-person singular optative | it may occur |
| adhikam | nominative neuter singular | additional |
| hi | explanatory particle | indeed / for |
| tat | nominative neuter singular pronoun | that [factor] |

## 4. Grammar

The first line distinguishes two profiles inside the indeterminate class:

```text
nivṛte [avyākṛte] aṣṭādaśa matāḥ
    → in the obscured-indeterminate state, 18 are accepted

anyatra avyākṛte dvādaśa [matāḥ]
    → in the other, unobscured-indeterminate state, 12
```

`Anyatra` is resolved by the Bhāṣya as indeterminate consciousness other than
the obscured case, hence unobscured-indeterminate.

The second line states a general conditional rule:

```text
sarva-avirodhitvāt
    → because middha is not incompatible with any ethical class

yatra syāt
    → wherever it may actually occur

adhikaṃ hi tat
    → it is there counted as an additional factor
```

The optative `syāt` and relative `yatra` preserve contingency. Compatibility
does not make `middha` universally present; it licenses its addition wherever
an actual event contains it.

## 5. Translation

### Close syntactic construe

> In the obscured [indeterminate state], eighteen are accepted; in the other indeterminate state, twelve. Because sleepiness is incompatible with none, wherever it may occur, that indeed is additional.

### Bhāṣya-informed translation

> An obscured-indeterminate desire-realm consciousness associated with self-view or extreme view contains eighteen mental factors: the ten universal factors, the six afflicted great-ground factors, `vitarka`, and `vicāra`. An unobscured-indeterminate consciousness contains twelve: the ten universal factors plus `vitarka` and `vicāra`. Sleepiness may be wholesome, unwholesome, or indeterminate, so it is added as one further factor to whichever particular consciousness-event contains it.

The Bhāṣya also attributes to teachers of the outer regions the view that
indeterminate remorse may accompany the unobscured profile, producing
thirteen. This is a reported alternative, not the principal count.

## 6. Philosophical Translation

> Karmic indeterminacy does not mean structural indeterminacy. Obscured and unobscured neutral consciousness have exact but different compositions. A factor such as sleepiness is not fixed to one ethical ground; its compatibility spans wholesome, unwholesome, and indeterminate events, while its actual presence remains moment-specific.

Restrained Organon rendering:

> The caitta profile is a time-indexed event schema. Ethical type determines the inherited base; compatibility determines which extensions are admissible; occurrence determines which admissible factor is counted at that moment. Possibility and actuality must remain separate.

“Time-indexed event schema” is a project rendering. The textual basis is the
Bhāṣya's distinction between cross-class compatibility and actual conditional
co-presence.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Bhāṣya determination |
|---|---|---|
| nivṛta-avyākṛta | obscured-indeterminate | karmically neutral yet obscured by afflicted factors |
| anivṛta-avyākṛta | unobscured-indeterminate | neutral profile lacking the six afflicted great-ground factors |
| satkāya-dṛṣṭi | view of a real self | one view associated with the obscured-indeterminate profile |
| antagrāha-dṛṣṭi | extreme view | second view associated with that profile |
| prajñā-viśeṣa | specialization of discernment | explains again why view does not add a factor |
| bahirdeśaka | teacher of the outer regions | source of the attributed thirteen-factor profile with neutral remorse |
| middha | sleepiness / torpor | optional factor capable of wholesome, unwholesome, or indeterminate modes |
| sarvāvirodhitva | compatibility with all | non-opposition to all three ethical determinations |
| avirodha | non-opposition / compatibility | admissibility relation, not an assertion of actual occurrence |
| adhika | additional | counted above a base profile when the factor actually occurs |

`Avyākṛta` is rendered “indeterminate” in its karmic-ethical sense. It does
not mean that the event lacks determinate factors or cannot be classified.

## 8. Logical Determination

The obscured-indeterminate base is:

```text
ObscuredIndeterminateBase =
      UniversalGreatGroundTen
    ∪ AfflictedGreatGroundSix
    ∪ {Vitarka, Vicāra}

Count = 18
```

View specializes discernment without addition:

```text
ViewMode ∈ {RealSelfView, ExtremeView}
BaseFunction(ViewMode) = Discernment

specialize(Discernment, ViewMode)
    → Count remains 18
```

The unobscured-indeterminate base is:

```text
UnobscuredIndeterminateBase =
      UniversalGreatGroundTen
    ∪ {Vitarka, Vicāra}

Count = 12
```

The attributed external-school variant is:

```text
AcceptsNeutralRemorse(OuterRegionTeachers)
    → UnobscuredIndeterminateBase ∪ {Remorse}
    → Count = 13
```

`Middha` supplies a general compatibility transform:

```text
EthicalMode(Middha)
    ∈ {Wholesome, Unwholesome, Indeterminate}

Compatible(Middha, profileType)
    for every ethical profileType
```

But addition is event-local:

```text
AtTime(t):
    Profile(event, t) = BaseProfile(eventType)

    if OccursIn(Middha, event, t):
        Profile(event, t) = BaseProfile(eventType) ∪ {Middha}
        Count(event, t) = BaseCount(eventType) + 1
```

Therefore:

```text
Compatible(Middha, profileType)
    ⇏ PresentInEveryEvent(Middha, profileType)
```

## 9. Interpretive Note

VAK 2.30 completes the desire-realm count profiles by discriminating two
kinds of karmically indeterminate consciousness. The obscured form contains
the six afflicted great-ground factors and therefore totals eighteen. The
unobscured form lacks that inherited set and totals twelve. Neutrality in
karmic result is compatible with either obscuration or its absence.

The two views named by the Bhāṣya again confirm the identity-before-counting
rule of VAK 2.29. Self-view and extreme view are determinations of discernment,
not additional factors beside it. The profile changes qualitatively while its
cardinality remains eighteen.

`Middha` then introduces a new rule. It cannot be assigned exclusively to a
wholesome, unwholesome, or indeterminate ground because it may bear any of
those determinations. Its organizing relation is compatibility rather than
ground-wide necessity.

This is where the user's time-schema reading becomes exact:

```text
profile type
    states what must be present
    and what may be present

event at time t
    states which admissible factors actually occur
```

The factor is counted only in the event in which it occurs. A timeless list
of everything compatible with a profile would falsely convert possibility
into simultaneous actuality.

The project's phrase “Pure Sattva” may name this demand for a completely
discriminated event-form, but it remains an external characterization here.
The Kośa's textual achievement is already sufficient: ethical status,
obscuration, functional specialization, compatibility, and momentary
occurrence are separate axes of one mental-event calculus.

For the Kośa Technē:

```text
EventProfile<t> = {
    inheritedBase,
    specializedModes,
    compatibleExtensions,
    extensionsActualAt<t>
}
```

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_30
    a vak:Karika ;
    rdfs:label "VAK 2.30" ;
    vak:hasTopic vak:IndeterminateCaittaProfiles,
        vak:MiddhaCompatibility ;
    vak:belongsTo vak:Indriyanirdesa .

vak:ObscuredIndeterminateProfile
    vak:inherits vak:UniversalGreatGroundTen,
        vak:AfflictedGreatGroundSix ;
    vak:requires vak:Vitarka,
        vak:Vicara ;
    vak:hasCount 18 .

vak:UnobscuredIndeterminateProfile
    vak:inherits vak:UniversalGreatGroundTen ;
    vak:requires vak:Vitarka,
        vak:Vicara ;
    vak:hasCount 12 .

vak:Middha
    vak:compatibleWith vak:WholesomeProfile,
        vak:UnwholesomeProfile,
        vak:IndeterminateProfile ;
    vak:countedOnlyWhen vak:ActuallyOccurrent .

organon:TimeIndexedEventProfile
    a organon:InterpretiveReconstruction ;
    organon:distinguishes organon:CompatiblePossibility,
        organon:EventLocalActuality ;
    organon:inferredFrom vak:MiddhaCompatibility .
```
