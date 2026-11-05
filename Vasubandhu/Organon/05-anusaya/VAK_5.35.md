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

After VAK 5.34 explains the arising of a particular kleśa, VAK 5.35
reclassifies the afflictive field under the first two `āsravas`.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `kāme` | locative singular | in the Desire Realm |
| `sa-paryavasthānāḥ` | nominative plural compound | together with the paryavasthānas |
| `kleśāḥ` | nominative plural masculine | afflictions |
| `kāma-āsravaḥ` | nominative singular masculine | the influx of desire |
| `vinā mohena` | indeclinable governing instrumental | apart from delusion or ignorance |
| `anuśayāḥ eva` | nominative plural with restrictive particle | the anuśayas alone |
| `rūpa-arūpye` | locative dual | in the Form and Formless Realms |
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

The locative fixes the realm; `sa-paryavasthānāḥ` includes the
envelopments; and `vinā mohena` excludes ignorance for
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
> apart from delusion, are the desire-influx. In the Form and Formless Realms,
> the anuśayas alone, [again apart from delusion], are the existence-influx.

### Bhāṣya-informed study translation

> In the Desire Realm, afflictions together with paryavasthānas, apart from
> ignorance, constitute the desire āsrava. In the Form and Formless Realms,
> only the anuśayas, again apart from ignorance, constitute the existence
> āsrava.

## 6. Philosophical Translation

> The first two āsravas classify afflictive factors by realm and by what the
> present enumeration counts. The Desire Realm total includes ten envelopments;
> the higher-realm total counts only non-ignorance anuśayas. The objection about
> torpor and restlessness makes presence in a realm distinct from separate
> membership in this count. The Kāśmīra reply names lack of independence as
> the reason for that exclusion, leaving its fuller criterion unstated here.

This classification gives the individual-path inquiry a precise inventory of
what is counted. It does not by itself describe an individual's course of
affliction or the reason the two higher realms form one āsrava; the latter
question opens in 5.36.

## 7. Technical Vocabulary

**`Āsrava` — influx or contaminating current**

A canonical functional grouping of afflictive factors. The Bhāṣya introduces
three: desire-influx, existence-influx, and ignorance-influx.

**`Kāmāsrava` — desire-influx**

The non-ignorance afflictions of the Desire Realm together with its ten
paryavasthānas: forty-one counted items.

**`Bhavāsrava` — existence-influx**

The non-ignorance anuśayas of the Form and Formless Realms combined: fifty-
two counted items.

**`Paryavasthāna` — afflictive envelopment**

Included independently in desire-influx. Torpor and restlessness occur in the
higher realms, but the Kāśmīra reply excludes them as separate members of this
enumeration because of `asvātantrya`.

**`Asvātantrya` — lack of independence**

A reason attributed to the Kāśmīra teachers for excluding the two named
higher-realm envelopments from this count. The present unit does not define
a general criterion of independence.

**`Dravya` — counted factor**

The Bhāṣya counts forty-one factors under desire āsrava and fifty-two under
existence āsrava. The Kāśmīra reply about higher-realm paryavasthānas concerns
whether they are counted independently here.

**Alternative functional classifications**

The Bhāṣya also lists four floods (`ogha`), four yokes (`yoga`), and four
appropriations (`upādāna`). Their detailed membership is treated later.

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

one afflictive field
    → multiple named classifications
```

## 9. Interpretive Note

**Source determination.** The Bhāṣya begins with “these very anuśayas” and
lists three āsravas, four floods, four yokes, and four appropriations. It then
gives exact memberships for desire and existence āsrava: thirty-one plus ten
and twenty-six plus twenty-six. The *Prakaraṇa* objection names additional
higher-realm envelopments, and the Kāśmīra answer excludes them from the
present count because they lack independence.

**Organon determination.** Occurrence, domain, and counted membership must be
represented separately. A factor can occur in a realm and still be omitted
from a particular total. This is a project-level reading of the objection and
reply, not a general criterion for independence supplied by the source.

**The individual path.** These counts constrain any later account of how
an individual's afflictions operate: a claim about a given factor must say
which realm and which classification it concerns. This unit establishes the
inventory; 5.36 asks why the two higher realms are combined and why ignorance
is separately classified.

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
    Projects: UnderlyingAfflictiveField
    Preserves: FactorIdentity, realm, Provenance
```

The seed treats `āsrava` as a functionally grounded view of the same afflictive
field. It preserves the factors and their relations rather than multiplying
the ontology whenever the classification changes.
