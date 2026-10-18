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

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `kāme` | locative singular | in the Desire Realm |
| `sa-paryavasthānāḥ` | nominative plural compound | together with the paryavasthānas |
| `kleśāḥ` | nominative plural masculine | afflictions |
| `kāma-āsravaḥ` | nominative singular masculine | the influx of desire |
| `vinā mohena` | indeclinable governing instrumental | apart from delusion or ignorance |
| `anuśayāḥ eva` | nominative plural with restrictive particle | the anuśayas alone |
| `rūpa-arūpye` | locative dual | in the form- and Formless Realms |
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

The locative fixes the realm; `sa-paryavasthānāḥ` includes the enveloping or
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
paryavasthānas occur in the higher realms.

## 5. Translation

### Literal Translation

> In the Desire Realm, the afflictions together with the paryavasthānas,
> apart from delusion, are the desire-influx. In the form- and Formless Realms,
> the anuśayas alone, [again apart from delusion], are the existence-influx.

### Bhāṣya-informed study translation

> In the Desire Realm, afflictions together with paryavasthānas, apart from
> ignorance, constitute the desire āsrava. In the form and formless realms,
> only the anuśayas, again apart from ignorance, constitute the existence
> āsrava.

## 6. Philosophical Translation

> The afflictive event of VAK 5.34 belongs to a larger continuity. Recurrent
> dispositions and manifestations are gathered according to the current by
> which they sustain a realm of conditioned existence. Desire-influx includes
> the more manifest envelopments of desire-life; existence-influx gathers the
> non-ignorance tendencies of the concentrated higher realms under one
> functionally unified stream. Ignorance is withheld because its operation
> traverses the three realms and will constitute a current of its own.

The classifications do not manufacture new dharmas. They redescribe one
determinate afflictive field according to different practical functions.

## 7. Technical Vocabulary

**`Āsrava` — influx or contaminating current**

A canonical functional grouping of afflictive factors. The Bhāṣya introduces
three: desire-influx, existence-influx, and ignorance-influx.

**`Kāmāsrava` — desire-influx**

The non-ignorance afflictions of the Desire Realm together with its ten
paryavasthānas: forty-one counted items.

**`Bhavāsrava` — existence-influx**

The non-ignorance anuśayas of the form- and Formless Realms combined: fifty-
two counted items.

**`Paryavasthāna` — afflictive envelopment or manifest domination**

Included independently in desire-influx. Torpor and restlessness occur in the
higher realms, but the Kāśmīra reply excludes them as separate members of this
enumeration because of `asvātantrya`.

**`Asvātantrya` — lack of independence**

A classificatory, not existential, exclusion. A factor may occur in a realm
without possessing the independent functional standing required to be counted
as a separate member of the present total.

**`Dravya` — counted factor**

The Bhāṣya counts forty-one factors under desire āsrava and fifty-two under
existence āsrava. The Kāśmīra reply about higher-realm paryavasthānas concerns
whether they are counted independently here.

**Alternative functional classifications**

The Bhāṣya says that the same anuśayas are also taught as four floods
(`ogha`), four yokes (`yoga`), and four appropriations (`upādāna`). These are
distinct classificatory views upon the analyzed field.

## 8. Logical Determination

VAK 5.35 applies new membership predicates to already determined factors:

```text
MemberOf(x, KāmaĀsrava)
    iff Realm(x) = Desire
    AND [Kleśa(x) OR Paryavasthāna(x)]
    AND NOT Avidyā(x)

MemberOf(x, BhavaĀsrava)
    iff Realm(x) in {Form, Formless}
    AND Anuśaya(x)
    AND NOT Avidyā(x)
```

The Bhāṣya's objection and answer add a rule of independent counting:

```text
OccursIn(x, realm)
    ⇏ IndependentlyCountedIn(x, Classification)

HigherRealmParyavasthāna(x)
AND LacksIndependence(x)
    → NOT IndependentlyCountedIn(x, BhavaĀsrava)
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
        → realm-sustaining āsrava
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
by determining their realms, relations, grounds, manifestations, and modes of
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

ObjectProperty: belongsToRealm
    Domain: AfflictiveFactor
    Range: realm

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

Rule: DesireRealmFactor(?x)
    AND [Anusaya(?x) OR Paryavasthana(?x)]
    AND isIgnorance(?x, false)
    -> memberOfInflux(?x, DesireInflux)

Rule: HigherRealmAnusaya(?x)
    AND isIgnorance(?x, false)
    -> memberOfInflux(?x, ExistenceInflux)

Constraint: occursInRealm(?x, ?d)
    doesNotEntail hasIndependentMembership(?x, ?classification)

View: AsravaClassification
    Projects: UnderlyingAnusayaField
    Preserves: FactorIdentity, realm, FunctionalGround, Provenance
```

The seed treats `āsrava` as a functionally grounded view of the same afflictive
field. It preserves the factors and their relations rather than multiplying
the ontology whenever the classification changes.
