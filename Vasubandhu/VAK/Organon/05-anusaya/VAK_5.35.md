# VAK_5.35

## 1. Sanskrit (Devanāgarī)

```sanskrit
कामे सपर्यवस्थानाः क्लेशाः कामास्रवो विना ।
मोहेनानुशया एव रूपारूप्ये भवास्रवः ॥ ५.३५ ॥
```

## 2. Sanskrit (IAST)

```text
kāme saparyavasthānāḥ kleśāḥ kāmāsravo vinā |
mohenānuśayā eva rūpārūpye bhavāsravaḥ || 5.35 ||
```

After VAK 5.34 explains the manifestation of a particular kleśa, VAK 5.35
reclassifies the afflictive field according to the sustained currents called
`āsravas`.

## 3. Padaccheda and Lexical Analysis

```text
kāme | sa-paryavasthānāḥ | kleśāḥ | kāma-āsravaḥ | vinā |
mohena | anuśayāḥ | eva | rūpa-arūpye | bhava-āsravaḥ
```

| Form | Morphology | Contextual sense |
|---|---|---|
| `kāme` | locative singular | in the desire-domain |
| `sa-paryavasthānāḥ` | nominative plural compound | together with the paryavasthānas |
| `kleśāḥ` | nominative plural masculine | afflictions |
| `kāma-āsravaḥ` | nominative singular masculine | the influx of desire |
| `vinā mohena` | indeclinable governing instrumental | apart from delusion or ignorance |
| `anuśayāḥ eva` | nominative plural with restrictive particle | the anuśayas alone |
| `rūpa-arūpye` | locative dual | in the form- and formless-domains |
| `bhava-āsravaḥ` | nominative singular masculine | the influx of existence |

The singular collective predicates `kāmāsravaḥ` and `bhavāsravaḥ` gather
plural afflictive factors under new functional classifications.

## 4. Grammar

**Desire-influx**

```text
kāme [vartamānāḥ]
sa-paryavasthānāḥ kleśāḥ
vinā mohena
    kāma-āsravaḥ [veditavyaḥ]
```

The locative fixes the domain; `sa-paryavasthānāḥ` includes the enveloping or
manifest secondary afflictions; and `vinā mohena` excludes ignorance for
separate classification. The Bhāṣya supplies “is to be understood as.”

**Existence-influx**

```text
rūpa-arūpye [vartamānāḥ]
anuśayāḥ eva
[vinā mohena]
    bhava-āsravaḥ [veditavyaḥ]
```

The Bhāṣya explicitly carries `vinā mohena` into the second half. `Eva`
restricts the present enumeration to anuśayas, but does not assert that no
paryavasthānas occur in the higher domains.

## 5. Translation

### Literal Translation

> In the desire-domain, the afflictions together with the paryavasthānas,
> apart from delusion, are the desire-influx. In the form- and formless-domains,
> the anuśayas alone, [again apart from delusion], are the existence-influx.

### Bhāṣya-informed study translation

> The desire-influx comprises forty-one factors: thirty-one desire-domain
> anuśayas after exclusion of the five modes of ignorance, together with ten
> paryavasthānas. The existence-influx comprises fifty-two factors: twenty-six
> non-ignorance anuśayas in the form-domain and twenty-six in the formless-
> domain. Higher-domain torpor and restlessness are not denied; the Kāśmīra
> explanation says they are not independently counted here because they lack
> independence.

The exact enumerations, the carried-forward exclusion of ignorance, and the
reason for omitting higher-domain paryavasthānas are supplied by the Bhāṣya.

## 6. Philosophical Translation

> The afflictive event of VAK 5.34 belongs to a larger continuity. Recurrent
> dispositions and manifestations are gathered according to the current by
> which they sustain a domain of conditioned existence. Desire-influx includes
> the more manifest envelopments of desire-life; existence-influx gathers the
> non-ignorance tendencies of the concentrated higher domains under one
> functionally unified stream. Ignorance is withheld because its operation
> traverses the three domains and will constitute a current of its own.

The classifications do not manufacture new dharmas. They redescribe one
determinate afflictive field according to different practical functions.

## 7. Technical Vocabulary

**`Āsrava` — influx or contaminating current**

A canonical functional grouping of afflictive factors. The Bhāṣya introduces
three: desire-influx, existence-influx, and ignorance-influx.

**`Kāmāsrava` — desire-influx**

The non-ignorance afflictions of the desire-domain together with its ten
paryavasthānas: forty-one counted items.

**`Bhavāsrava` — existence-influx**

The non-ignorance anuśayas of the form- and formless-domains combined: fifty-
two counted items.

**`Paryavasthāna` — afflictive envelopment or manifest domination**

Included independently in desire-influx. Torpor and restlessness occur in the
higher domains, but the Kāśmīra reply excludes them as separate members of this
enumeration because of `asvātantrya`.

**`Asvātantrya` — lack of independence**

A classificatory, not existential, exclusion. A factor may occur in a domain
without possessing the independent functional standing required to be counted
as a separate member of the present aggregate.

**Threefold `sādharmya` — shared functional character**

The form- and formless-domain anuśayas are unified as one existence-influx
because both groups are ethically indeterminate (`avyākṛta`), inward-directed
(`antarmukha-pravṛtta`), and situated in concentrated levels
(`samāhita-bhūmika`).

**Alternative functional classifications**

The Bhāṣya says that the same anuśayas are also taught as four floods
(`ogha`), four yokes (`yoga`), and four appropriations (`upādāna`). These are
distinct classificatory views upon the analyzed field.

## 8. Logical Determination

VAK 5.35 applies new membership predicates to already determined factors:

```text
MemberOf(x, KāmaĀsrava)
    iff Domain(x) = Desire
    AND [Kleśa(x) OR Paryavasthāna(x)]
    AND NOT Avidyā(x)

MemberOf(x, BhavaĀsrava)
    iff Domain(x) in {Form, Formless}
    AND Anuśaya(x)
    AND NOT Avidyā(x)
```

The Bhāṣya's objection and answer add a rule of independent counting:

```text
OccursIn(x, Domain)
    ⇏ IndependentlyCountedIn(x, Classification)

HigherDomainParyavasthāna(x)
AND LacksIndependence(x)
    → NOT IndependentlyCountedIn(x, BhavaĀsrava)
```

The unity of existence-influx is generated by shared determinations:

```text
Shared(
    EthicallyIndeterminate,
    InwardDirected,
    ConcentratedLevel
)
    → AggregateAs(FormAnuśayas, FormlessAnuśayas, BhavaĀsrava)
```

Thus:

```text
new valid classification
    ≠ new entity

one dharma-field
    → multiple functionally determined Views
```

## 9. Interpretive Note

**Source determination.** The Bhāṣya begins from “these same anuśayas” and
projects them into several canonical arrangements: influxes, floods, yokes,
and appropriations. VAK 5.35 defines the first two influxes. Their membership
is exact, numerically accountable, and governed by functional independence.

**From event to stream.** VAK 5.34 produced a manifest kleśa from cause,
object, and application. VAK 5.35 now shows how determinate afflictive factors
belong to currents that sustain modes of conditioned existence:

```text
event-producing causal circuit
    → recurrence and mutual reinforcement
        → domain-sustaining āsrava
```

The stream is not a second substance above its members. It is their organized
continuity under a common function.

**The karmically determinate living continuum.** In the project's Yoga–Organon
reconstruction, the `jīva` with non-zero karma-vipāka is the transactional
continuum through which these currents have concrete existence. The jīva does
not stand outside the impure dharma-field as a finished subject; its present
life is the Product in which prior karma, latent anuśaya, objective occasion,
and cognitive operation continue to meet.

**The direction of the Path.** The movement from avidyā to vidyā must transform
not only isolated kleśa-events but the recurrent organization that makes them
a stream. The Path therefore carries the conditioned afflictions into knowledge
by determining their domains, relations, grounds, manifestations, and modes of
aggregation. What was blindly reproduced as āsrava becomes objectively
comprehended as a system—and thereby available for cessation.

## 10. OWL++ Seed

```text
Class: AfflictiveFactor
Class: Anusaya
Class: Paryavasthana
Class: Asrava
Class: DesireInflux
    SubClassOf: Asrava
Class: ExistenceInflux
    SubClassOf: Asrava
Class: FunctionalClassification

ObjectProperty: belongsToDomain
    Domain: AfflictiveFactor
    Range: Domain

ObjectProperty: memberOfInflux
    Domain: AfflictiveFactor
    Range: Asrava

ObjectProperty: sharesFunctionalCharacterWith
    Domain: AfflictiveFactor
    Range: AfflictiveFactor

DataProperty: isIgnorance
    Domain: AfflictiveFactor
    Range: Boolean

DataProperty: hasIndependentStanding
    Domain: AfflictiveFactor
    Range: Boolean

Rule: DesireDomainFactor(?x)
    AND [Anusaya(?x) OR Paryavasthana(?x)]
    AND isIgnorance(?x, false)
    -> memberOfInflux(?x, DesireInflux)

Rule: HigherDomainAnusaya(?x)
    AND isIgnorance(?x, false)
    -> memberOfInflux(?x, ExistenceInflux)

Constraint: occursInDomain(?x, ?d)
    doesNotEntail hasIndependentMembership(?x, ?classification)

View: AsravaClassification
    Projects: UnderlyingAnusayaField
    Preserves: FactorIdentity, Domain, FunctionalGround, Provenance
```

The seed treats `āsrava` as a functionally grounded view of the same afflictive
field. It preserves the factors and their relations rather than multiplying
the ontology whenever the classification changes.
