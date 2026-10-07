# VAK_2.30

## 1. Sanskrit (Devanāgarī)

> निवृतेऽष्टादशान्यत्र द्वादशाव्याकृते मताः ।
>
> मिद्धं सर्वाविरोधित्वाद्यत्र स्यादधिकं हि तत् ॥ २.३० ॥

The research witness separates *aṣṭādaśa anyatra*; the continuous form
*aṣṭādaśānyatra* is displayed above, with the lexical division retained
below.

## 2. Sanskrit (IAST)

> nivṛte 'ṣṭādaśānyatra dvādaśāvyākṛte matāḥ /
>
> middhaṃ sarvāvirodhitvād yatra syād adhikaṃ hi tat // 2.30 //

## 3. Lexical Analysis

```text
nivṛte           → nivṛte
aṣṭādaśānyatra   → aṣṭādaśa anyatra
dvādaśāvyākṛte   → dvādaśa avyākṛte
matāḥ            → matāḥ
middham          → middham
sarvāvirodhitvāt → sarva-avirodhitvāt
yatra            → yatra
syād             → syāt
adhikaṃ          → adhikam
hi               → hi
tat              → tat
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| nivṛte | locative neuter singular | in the obscured-indeterminate case |
| aṣṭādaśa | numeral | eighteen |
| anyatra | indeclinable | in the other case |
| dvādaśa | numeral | twelve |
| avyākṛte | locative neuter singular | in ethically indeterminate consciousness |
| matāḥ | nominative masculine plural past passive participle | are accepted as the count |
| middham | nominative neuter singular | torpor |
| sarva-avirodhitvāt | ablative singular abstract compound | because compatible with all |
| yatra | relative adverb | wherever |
| syāt | third-person singular optative | it may occur |
| adhikam | nominative neuter singular | additional |
| hi | explanatory particle | for |
| tat | nominative neuter singular pronoun | that factor |

## 4. Grammar

The first line gives two ethically indeterminate profiles:

```text
nivṛte [avyākṛte] aṣṭādaśa matāḥ
    → eighteen are accepted in the obscured-indeterminate case

anyatra avyākṛte dvādaśa [matāḥ]
    → twelve in the other, unobscured-indeterminate case
```

The Bhāṣya resolves *anyatra* as the indeterminate case other than the
obscured one. The second line gives a conditional addition:

```text
because torpor is compatible with all:
    wherever it occurs, it is counted as an additional factor
```

The relative *yatra* and optative *syāt* express contingency. Compatibility
does not make torpor universally present.

## 5. Scientific English Rendering

### Kārikā

> In obscured-indeterminate consciousness eighteen are accepted; in the
> other indeterminate case, twelve. Because torpor is incompatible with
> none, wherever it occurs, that factor is additional.

### Bhāṣya-informed rendering

> In the Desire Principle, consciousness associated with self-view or
> extreme view is obscured-indeterminate. It has eighteen mental factors:
> ten universal great-ground factors, six afflicted great-ground factors,
> *vitarka*, and *vicāra*. As before, view does not add a further factor.
> The indeterminate case other than the obscured one is
> unobscured-indeterminate. Twelve factors are accepted there: the ten
> universal great-ground factors, *vitarka*, and *vicāra*. Teachers of
> the outer regions also accept indeterminate remorse; on their account,
> consciousness associated with it has thirteen factors.

> Torpor is compatible with all the factors described above because it
> may be wholesome, unwholesome, or indeterminate. Wherever it occurs,
> it is counted as an additional factor: where there are twenty-two,
> there are twenty-three; where there are twenty-three, there are
> twenty-four; and so forth.

The teachers of the outer regions' thirteen-factor profile and a
twelve-factor profile with torpor both total thirteen, but arise from
different additions and must not be conflated.

## 6. Interpretation

The verse completes the indeterminate Desire-Principle profiles. The
obscured case includes the six afflicted factors and totals eighteen;
the unobscured case omits them and totals twelve. The two views named by
the Bhāṣya are determinations of already-counted discernment, not an
additional factor.

Torpor's cross-class compatibility and its actual occurrence are
different relations. It can occur with wholesome, unwholesome, or
indeterminate consciousness, but *yatra syāt* makes the addition
conditional: count it only where present. The Bhāṣya explicitly gives
22→23 and 23→24; applying the rule to the eighteen- and twelve-factor
profiles yields nineteen and thirteen, respectively, as deductions.

The Kośa's governing synthesis: Vijñāna is Discriminative Cognition joining
and governing Perception and Conception. Their unity is Inconceivable as a
homogeneous operation; its Idea is disclosed in the Cognition Base. Vijñāna
governs Mind and guides the reading of Dharma Base. Form Base and Dharma
Base both include the same *avijñapti* in distinct classifications, and
Vijñāna bears a *prati* relation to *avijñapti*. This synthesis is distinct
from the local profile counts of associated mental factors.

## 7. Logical Determination

```text
ObscuredIndeterminateBase =
      UniversalGreatGroundTen
    ∪ AfflictedGreatGroundSix
    ∪ {Vitarka, Vicāra}

Count(ObscuredIndeterminateBase) = 18
```

```text
UnobscuredIndeterminateBase =
      UniversalGreatGroundTen
    ∪ {Vitarka, Vicāra}

Count(UnobscuredIndeterminateBase) = 12
```

The reported alternative and conditional torpor rule:

```text
OuterRegionTeachers:
    UnobscuredIndeterminateBase ∪ {IndeterminateRemorse}
    → 13

For any profile p:
    Present(Middha, p) → Count(p) + 1
```

These two routes to thirteen are not the same profile. Compatibility of
torpor with a class does not entail that it occurs in every member of the
class.

## 8. Interpretive Note

*Avyākṛta* here means ethically indeterminate, not lacking a determinate
factor structure; it is distinct from *aniyata*, “unfixed,” used of
factors in VAK 2.27. The obscured-indeterminate case shows that karmic
indeterminacy can coexist with affliction.

The alternative about indeterminate remorse is explicitly attributed to
teachers of the outer regions. The Bhāṣya does not adjudicate that view
here. Torpor is a distinct conditional addition; equal totals do not imply
identical membership or attribution.

## 9. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_30
    a vak:Karika ;
    rdfs:label "VAK 2.30" ;
    vak:hasTopic vak:IndeterminateFactorProfiles,
        vak:TorporCompatibility ;
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

vak:OuterRegionTeachers
    vak:accepts vak:UnobscuredIndeterminateRemorseProfile .

vak:Torpor
    vak:compatibleWith vak:Wholesome,
        vak:Unwholesome,
        vak:Indeterminate ;
    vak:increasesCountOnlyWhenPresent true .
```
