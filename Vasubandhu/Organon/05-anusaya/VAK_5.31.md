# VAK_5.31

## 1. Sanskrit (Devanāgarī)

```sanskrit
निरोधमार्गदृग्घेयाः सर्वे स्वाधिकगोचराः ।
अनास्रवास्त्रिधात्वन्त्यत्रयानास्रवगोचराः ॥ ५.३१ ॥
```

## 2. Sanskrit (IAST)

```text
nirodhamārgadṛggheyāḥ sarve svādhikagocarāḥ |
anāsravās tridhātvantyatrayānāsravagocarāḥ || 5.31 ||
```

The Bhāṣya treats this verse as completing the Support ordering between
sixteen Consciousness classes and sixteen Dharma classes begun in 5.29.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `nirodha-dṛk-heyāḥ` | nominative plural compound | dharmas to be abandoned by seeing cessation |
| `mārga-dṛk-heyāḥ` | nominative plural compound | dharmas to be abandoned by seeing the path |
| `sarve` | nominative plural masculine | all, in every realm |
| `sva-adhika-gocarāḥ` | nominative plural compound | in a cognitive range with their own corresponding Consciousness added |
| `anāsravāḥ` | nominative plural masculine | Dharmas without influx |
| `tri-dhātu-antya-traya` | compound member | the final three Consciousness classes in each of the three domains |
| `anāsrava-gocarāḥ` | nominative plural compound | within the range also of Consciousness without influx |

The bare compound `svādhika` could sound like an indefinite “own and
additional” range. The Bhāṣya determines it exactly: the previously established
range is retained, and the Consciousness corresponding to the Dharma's own
abandonment class is added.

## 4. Grammar

**Cessation- and path-seeing classes**

```text
nirodha-dṛk-heyāḥ mārga-dṛk-heyāḥ sarve
    sva-adhika-gocarāḥ
```

`Sarve` distributes the rule across all three realms. `Sva-adhika` is resolved
by the Bhāṣya separately for the cessation-class and path-class: each receives
its own corresponding Consciousness in addition to the cognitive range
already computed for that domain in 5.29–5.30.

**Undefiled dharmas**

```text
anāsravāḥ
    [tri-dhātu-antya-traya-anāsrava]-gocarāḥ
```

The Bhāṣya resolves `antya-traya` as the final three Consciousness classes
within each domain: those to be abandoned by seeing cessation, seeing the
Path, and cultivation. The final `anāsrava` adds Consciousness without
influx itself.

## 5. Translation

### Literal Translation

> All [Dharmas] to be abandoned by seeing cessation or the Path lie within a
> cognitive range with their own [corresponding Consciousness] added.
> [Dharmas] without influx lie in the range of the final three [Consciousness
> classes] in the three domains and of [Consciousness] without influx.

### Bhāṣya-informed study translation

> In each of the three domains, Dharmas to be abandoned by seeing cessation
> or the Path lie in the previously established cognitive range with their
> own corresponding Consciousness class added. Dharmas without influx lie
> in the range of the final three Consciousness classes in each domain—those
> to be abandoned by seeing cessation, seeing the Path, and cultivation—and
> of Consciousness without influx.

## 6. Philosophical Translation

> The cessation- and Path-seeing Dharma classes extend an established
> cognitive range by one class: the Consciousness corresponding to their
> own abandonment type. Dharmas without influx have a different ten-class
> range. With these additions the sixteen-class Support ordering is
> complete. The Bhāṣya then uses that result twice, first for Cognition
> taking the pleasure faculty as Support and then for Cognition taking that
> Cognition as Support. Each step requires its own anuśaya assessment.

The Support relation does not make a Dharma identical with the Consciousness
or Cognition taking it. Nor does an admissible Support relation by itself
show that an anuśaya lies latent there.

## 7. Technical Vocabulary

**`Nirodha-dṛg-heya` and `mārga-dṛg-heya` — abandoned by seeing cessation and the Path**

The final two of the five abandonment classes within each conditioned
domain. Each gains its own corresponding Consciousness class in addition to
the range already established for its domain.

**`Svādhika` — with one's own added**

The Bhāṣya gives an exact operation:

```text
ExtendedRange = PreviousDomainRange ∪ {OwnCorrespondingConsciousness}
```

**`Antya-traya` — the final three**

The Consciousness classes to be abandoned by seeing cessation, seeing the
Path, and cultivation in each of the three domains.

**`Anāsrava` — without influx**

Here it describes both a Dharma class and a Consciousness class. The Dharma
class without influx is Support for nine final domain-based classes plus
the Consciousness class without influx, making ten.

**`Ālambana-vyavasthā` and `diṅmātra` — Support ordering and indication**

The completed matrix orders which of sixteen Dharma classes can be Supports
for which of sixteen Consciousness classes. `Diṅmātra` introduces an
example of applying that ordering to anuśaya questions, not a full answer
to every possible question.

**`Sukhendriya` — pleasure faculty**

The worked example first classifies it into seven kinds: one Desire Realm
kind to be abandoned by cultivation, five Form Realm kinds, and one without
influx. Those kinds serve as Supports for twelve Cognition classes.

**`Saṃskṛtālambana` — taking conditioned Dharmas as Supports**

This qualifies the Form Realm anuśayas in the first and second applications.
It is a restriction on their Support, not a name for all Form Realm
Consciousness classes.

**`Sukhendriyālambanālambana` — taking a pleasure-faculty-taking Cognition as Support**

The second question nests the relation: the pleasure faculty is Support for
a first Cognition; that Cognition is Support for a second. This expands the
second Cognition's admissible classes from twelve to fourteen.

## 8. Logical Determination

For each domain `d`, let `B(d)` be the five-, eight-, or ten-class
Consciousness range from 5.29–5.30. For the cessation- and Path-seeing
Dharma classes, 5.31 adds the corresponding Consciousness class:

```text
Range(CessationClass, d) = B(d) ∪ {CessationConsciousness(d)}
Range(PathClass, d)      = B(d) ∪ {PathConsciousness(d)}

|B(Desire)|   = 5    → extended range = 6
|B(Form)|     = 8    → extended range = 9
|B(Formless)| = 10   → extended range = 11
```

For Dharmas without influx:

```text
Range(WithoutInfluxDharma)
    = {CessationConsciousness(d), PathConsciousness(d),
       CultivationConsciousness(d) for d in the three domains}
      ∪ {WithoutInfluxConsciousness}

    cardinality = (3 × 3) + 1 = 10
```

The worked example then uses the completed Support relation twice:

```text
PleasureFacultyKinds = 1 Desire + 5 Form + 1 without influx = 7

C1 = {Cognition classes taking the pleasure faculty as Support}
   = 4 Desire + 5 Form + 2 Formless + 1 without influx = 12

C2 = {Cognition classes taking a member of C1 as Support}
   = C1 + 2 further Formless classes = 14
```

The final two Formless classes added to `C2` are those to be abandoned by
seeing suffering and seeing origination. The text then revises the applicable
anuśaya list: four Desire Realm classes, Form Realm anuśayas taking
conditioned Supports, and four Formless Realm classes. This is a typed
inference, subject to `yathāsaṃbhavam`; the Support relation alone does not
give an anuśaya count.

The passage does not identify Consciousness with Basis (`āśraya`) or infer
an afflictive `hetu`–`phala` production from every Support relation.

## 9. Interpretive Note

**Source determination.** 5.31 completes the five abandonment classes in
each of the three domains and the class without influx: sixteen Dharma
classes in all. The same sixteenfold classification applies to Consciousness.
The Bhāṣya then demonstrates the Support ordering on a nested case, moving
from seven forms of a faculty to twelve and fourteen Cognition classes.

**The Product as a new premise.** As an Organon reconstruction, the prior
five-, eight-, and ten-class ranges become premises for the additive six-,
nine-, and eleven-class ranges. The completed matrix then becomes a premise
for the two pleasure-faculty questions. This names a logical reuse of the
result; the Bhāṣya supplies the counts and relations, not the fourfold
Organon vocabulary.

**Comparative synthesis.** For the inquiry into individual cognition, the
nested case is especially useful: one Cognition can take another Cognition
as Support while that first Cognition takes a faculty as Support. The Kośa
states the admissible classes and applicable anuśayas; any comparison with
Yoga stages or triadic cognitive powers must preserve those typed relations
before proposing a wider model.

## 10. OWL++ Seed

```text
Class: DharmaClass
Class: ConsciousnessClass
Class: CognitionClass
Class: Domain
Class: AbandonmentType
Class: SupportRelation

ObjectProperty: belongsToRealm
    Domain: DharmaClass or ConsciousnessClass
    Range: Domain

ObjectProperty: hasAbandonmentType
    Domain: DharmaClass or ConsciousnessClass
    Range: AbandonmentType

ObjectProperty: takesAsSupport
    Domain: ConsciousnessClass or CognitionClass
    Range: DharmaClass or CognitionClass

ObjectProperty: extendsRangeWith
    Domain: DharmaClass
    Range: ConsciousnessClass

Rule: NirodhaAbandonableDharma(?d)
    AND PreviousRealmRangeMember(?c, ?d)
    -> takesAsSupport(?c, ?d)

Rule: NirodhaAbandonableDharma(?d)
    AND OwnNirodhaConsciousness(?c, ?d)
    -> takesAsSupport(?c, ?d)

Rule: MargaAbandonableDharma(?d)
    AND PreviousRealmRangeMember(?c, ?d)
    -> takesAsSupport(?c, ?d)

Rule: MargaAbandonableDharma(?d)
    AND OwnMargaConsciousness(?c, ?d)
    -> takesAsSupport(?c, ?d)

Rule: UndefiledDharma(?d)
    AND FinalThreeRealmConsciousness(?c)
    -> takesAsSupport(?c, ?d)

Rule: UndefiledDharma(?d)
    AND UndefiledConsciousness(?c)
    -> takesAsSupport(?c, ?d)

Constraint: takesAsSupport(?c, ?d)
    doesNotEntail determinateAnusayaCount(?d)
```

The seed completes the typed Support layer, including Cognition as a possible
Support, while leaving anuśaya adherence as a further inference.
