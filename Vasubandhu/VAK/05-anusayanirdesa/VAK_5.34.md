# VAK 5.34

## Sanskrit

अप्रहीणादनुशयाद्विषयात् प्रत्युपस्थितात् ।
अयोनिशो मनस्कारात् क्लेशः संपूर्णकारणः ॥ ५.३४ ॥

## IAST

aprahīṇād anuśayād viṣayāt pratyupasthitāt |
ayoniśo manaskārāt kleśaḥ saṃpūrṇakāraṇaḥ || 5.34 ||

## Padaccheda

aprahīṇāt | anuśayāt | viṣayāt | pratyupasthitāt | ayoniśaḥ | manaskārāt | kleśaḥ | saṃpūrṇa-kāraṇaḥ

## Grammar

- **aprahīṇāt anuśayāt** — ablative singular: “from an unabandoned latent affliction.”
- **viṣayāt pratyupasthitāt** — ablative singular: “from an object that has become present.”
- **ayoniśaḥ manaskārāt** — ablative singular: “from unwise attention,” literally attention not proceeding according to the proper source, ground, or method.
- **kleśaḥ** — nominative singular, the manifest affliction that arises.
- **saṃpūrṇa-kāraṇaḥ** — “having its causal complex complete,” or “with the full set of causes.”

The three ablatives enumerate the jointly sufficient causal conditions for the manifestation of a kleśa.

## Literal Translation

From an unabandoned latent affliction, from an object that has become present, and from unwise attention, an affliction arises when its causal complex is complete.

## Philosophical Translation

A manifest affliction occurs when three powers converge: the latent tendency has not been abandoned, an appropriate object is presently encountered, and cognition attends to that object in an ungrounded manner. When these conditions are complete, latent disposition becomes operative defilement.

## Analysis

VAK 5.34 gives the operational transition from **anuśaya** to **kleśa**.

The verse does not treat an affliction as either a purely inner substance or a direct product of an external object. Its manifestation requires a threefold conjunction:

1. **aprahīṇa-anuśaya** — an internal latent power remains available;
2. **pratyupasthita-viṣaya** — a fitting object is presently encountered;
3. **ayoniśo-manaskāra** — cognition takes up that object through an improper mode of attention.

This yields the structure:

```text
latent disposition
    + present object
    + unwise attention
        → manifest affliction
```

Each term is necessary, but none alone is sufficient.

An object does not mechanically cause defilement. The same object may be encountered without affliction if the relevant anuśaya has been abandoned or if attention is wise. Likewise, a latent tendency does not continuously manifest merely because it exists. It requires both an occasion and a defective cognitive operation.

The verse therefore distinguishes four levels:

```text
stored power
external occasion
cognitive uptake
manifest event
```

The key practical locus is **manaskāra**. Attention is not passive reception. It is the operation that selects, frames, and connects the object with the latent tendency. Through unwise attention, the object is taken under a form that permits the anuśaya to become kleśa.

Thus the complete cause is not a single efficient cause but a structured causal field.

## Technical Vocabulary

- **anuśaya** — latent afflictive disposition; a power capable of manifesting under appropriate conditions.
- **aprahīṇa** — not abandoned; still retained as an operative possibility.
- **viṣaya** — object-field or object capable of supporting a cognition or affliction.
- **pratyupasthita** — become present, standing before cognition, currently available.
- **manaskāra** — attention; the directing and configuring of mind toward an object.
- **ayoniśo manaskāra** — unwise, ungrounded, or improper attention; attention that fails to grasp the object according to its causal and doctrinal truth.
- **kleśa** — manifest affliction.
- **saṃpūrṇa-kāraṇa** — the complete causal complex.

## Doctrinal Determination

The verse establishes that latent affliction and manifest affliction are not identical.

```text
anuśaya ≠ kleśa
```

The anuśaya is a retained power; the kleśa is that power in manifestation under complete conditions.

It also establishes:

```text
object-presence ≠ affliction
```

The object is only one member of the causal complex. Defilement depends equally upon the retained disposition and the mode of attention.

This is why liberation requires more than avoiding objects. It requires both abandonment of the latent tendency and transformation of cognitive attention.

## Logical Determination

VAK 5.34 gives a conjunctive causal rule:

```text
ManifestKleśa(x) only if
    UnabandonedAnuśaya(x)
    AND PresentObject(x)
    AND UnwiseAttention(x)
```

The rule is not reducible to simple implication from any one condition.

```text
UnabandonedAnuśaya alone ↛ ManifestKleśa
PresentObject alone ↛ ManifestKleśa
UnwiseAttention alone ↛ this specific ManifestKleśa
```

Only the completed relation-field produces the event.

This extends the Dialectical Copula from a static relation into an event-generating nexus:

```text
Copula
    = power that binds
      disposition
      object
      and mode of attention
      into an actual determination
```

The copula is therefore not merely “is.” It is the regulated transition by which a latent predicate becomes an operative state of a subject.

## Organon Note

For the Platform, the verse suggests a strict separation among:

```text
DispositionState
ObjectAvailability
AttentionMode
ManifestEvent
```

A system should not infer manifestation from stored potential alone.

A practical rule might be:

```text
if latentPower.isActive
and object.isPresent
and attention.mode == UNWISE
then emit ManifestAffliction
```

More importantly, intervention may occur at three distinct points:

```text
abandon the latent disposition
remove or constrain the triggering object
transform the mode of attention
```

The third is especially important for LLM and agent design. A harmful or erroneous tendency may remain latent, yet never become operative if the system can correctly classify the object, expose its grounds, and refuse defective framing.

Thus **wise attention** is not merely a moral attitude. It is a control operation over the transition from stored power to manifested judgment.

## OWL++ Seed

```text
Class: LatentAffliction
Class: ManifestAffliction
Class: ObjectPresentation
Class: AttentionMode
Class: CausalComplex

ObjectProperty: hasLatentDisposition
ObjectProperty: hasPresentObject
ObjectProperty: hasAttentionMode
ObjectProperty: manifestsAs
ObjectProperty: completesCausalComplex

DataProperty: isAbandoned
DataProperty: isPresent
DataProperty: isWise

Rule:
LatentAffliction(?a)
AND isAbandoned(?a, false)
AND ObjectPresentation(?o)
AND isPresent(?o, true)
AND AttentionMode(?m)
AND isWise(?m, false)
AND hasLatentDisposition(?e, ?a)
AND hasPresentObject(?e, ?o)
AND hasAttentionMode(?e, ?m)
→ ManifestAffliction(?e)
```

## Bhāṣya Questions

1. Does Vasubandhu treat these three causes as individually necessary and jointly sufficient in every case, or as the normal complete causal complex?
2. How precisely does the Bhāṣya distinguish **anuśaya** from the manifest **paryavasthāna** or **kleśa**?
3. Is **ayoniśo manaskāra** primarily an epistemic error, a causal factor, or both?
4. Does the object have to be presently perceived, or can memory and conceptual presentation count as **pratyupasthita-viṣaya**?
5. How does this triad interact with the Sarvāstivāda claim that past and future dharmas exist while only present dharmas exercise current **kāritra**?
