# VAK 5.23

## Sanskrit

रागप्रतिघमानैः स्यादतीतप्रत्युपस्थितैः ।
यत्रोत्पन्नाप्रहीणास्ते तस्मिन् वस्तुनि संयुतः ॥ ५.२३ ॥

## IAST

rāgapratighamānaiḥ syād atītapratyupasthitaiḥ |
yatrotpannāprahīṇās te tasmin vastuni saṃyutaḥ || 5.23 ||

## Padaccheda

```text
rāga-pratigha-mānaiḥ
syāt
atīta-pratyupasthitaiḥ
yatra
utpannāḥ
aprahīṇāḥ
te
tasmin
vastuni
saṃyutaḥ
```

Normalized:

```text
rāga-pratigha-mānaiḥ syāt atīta-pratyupasthitaiḥ |
yatra utpannāḥ aprahīṇāḥ te tasmin vastuni saṃyutaḥ ||
```

## Grammar

- `rāga-pratigha-mānaiḥ` — instrumental plural compound: by attachment, resistance or aversion, and pride.
- `syāt` — optative third-person singular of √`as`: one would be, may be, or is to be considered.
- `atīta-pratyupasthitaiḥ` — instrumental plural: by those that are past and presently arisen or manifest.
- `yatra` — where; with respect to whichever object or case.
- `utpannāḥ` — arisen or produced; nominative masculine plural, referring to the three afflictions.
- `aprahīṇāḥ` — not abandoned, not eliminated.
- `te` — those.
- `tasmin vastuni` — in or with respect to that object, basis, or matter.
- `saṃyutaḥ` — connected, conjoined, or bound; nominative masculine singular, referring to the person or continuum under analysis.

## Literal translation

One is connected with that object by attachment, aversion, and pride that are past or presently manifest, wherever those have arisen and have not been abandoned.

## Philosophical translation

A person remains bound to a determinate object through past or presently active attachment, aversion, and pride, provided that those afflictions have arisen with respect to that object and have not yet been eliminated.

## Analysis

Verses 5.20–5.21 examined which afflictions function as roots. Verse 5.22 classified the forms of rational response. Verse 5.23 now opens a new determination: the conditions under which a person is said to be connected or bound to an object by an affliction.

The verse selects three anuśayas:

```text
rāga
    attachment or appropriative attraction

pratigha
    resistance, aversion, hostility

māna
    comparative self-elevation or pride
```

These are all object-directed afflictions. Each establishes a determinate relation between a person and a `vastu`:

```text
rāga
    movement toward and appropriation of the object

pratigha
    movement against and rejection of the object

māna
    self-positioning through comparison with the object
```

The decisive condition is not merely that one of these afflictions existed at some time. Two qualifications are required:

```text
utpanna
    it has actually arisen with respect to the object

aprahīṇa
    it has not been abandoned
```

Thus:

```text
mere past occurrence
    does not by itself establish present bondage

past occurrence not yet abandoned
    continues to determine the relation
```

The verse therefore distinguishes temporal location from operative persistence.

An affliction may be past as an event while remaining effective because it has not been eliminated. Conversely, an affliction that has been abandoned no longer binds the continuum to its former object.

## Technical vocabulary

```text
rāga
    attachment
    appropriative attraction toward an object

pratigha
    resistance or aversion
    oppositional relation to an object

māna
    pride
    comparative self-positioning

atīta
    past
    no longer presently occurring as an event

pratyupasthita
    presently arisen or manifest
    standing forth in current activity

utpanna
    arisen
    having become actual in relation to an object

aprahīṇa
    unabandoned
    not yet eliminated by the relevant path

vastu
    object, basis, matter, or determinate case
    that with respect to which an affliction arises

saṃyuta
    connected, conjoined, or bound
    standing in an operative relation through an affliction
```

## Doctrinal determination

The verse establishes that bondage is relational rather than merely substantial.

One is not simply said to possess attachment, aversion, or pride in the abstract. One is connected:

```text
to this object
through this affliction
under these temporal conditions
with this abandonment-status
```

The operative structure is:

```text
Person
    -- through Anuśaya -->
Vastu
```

But this relation holds only when:

```text
the anuśaya has arisen regarding that vastu
and
the anuśaya has not been abandoned
```

This yields a fourfold determination:

```text
affliction-type
    rāga / pratigha / māna

temporal mode
    past / presently manifest

object
    the vastu regarding which it arose

path-status
    abandoned / unabandoned
```

The verse therefore prevents the crude claim that every person is bound to every object by every affliction.

Bondage is indexed.

## Logical determination

Verse 5.23 presents `saṃyoga` as a conditioned relation.

```text
saṃyuta(Person, Vastu)
```

cannot be inferred merely from:

```text
Anuśaya exists
```

It requires a more determinate conjunction:

```text
Anuśaya(?a)
hasType(?a, RagaOrPratighaOrMana)
hasArisenRegarding(?a, ?v)
notAbandoned(?a)
hasTemporalMode(?a, PastOrPresent)
    -> connectedWith(?person, ?v)
```

The essential distinction is:

```text
occurrence
    ≠
continuing efficacy
```

A past event may remain logically active if its determining power has not been removed.

This is the practical significance of `aprahīṇa`:

```text
past in time
    yet present in efficacy
```

The verse thus separates chronological presence from causal and normative presence.

## Relation to 5.17–5.18

Verses 5.17–5.18 analyzed how anuśayas adhere through object and conjunction.

Verse 5.23 now turns that analysis toward the subject or continuum:

```text
5.17–5.18
    how the anuśaya adheres

5.23
    when the person is connected to an object through it
```

The relation is no longer treated from the side of the affliction alone. It is now expressed as a practical status of the person.

## Organon note

The architectural lesson is that latent or historical state cannot be modeled as mere archival data.

```text
PastEvent
    may still impose
CurrentConstraint
```

A system therefore needs separate properties for:

```text
occurredAt
isCurrentlyManifest
hasBeenAbandoned
remainsOperative
hasObject
```

The crucial rule is:

```text
past
    does not imply
inactive
```

This is directly relevant to agent memory and practical learning. A prior cognition, error, commitment, or disposition can continue to structure present behavior even when it is not currently manifest.

The system must therefore distinguish:

```text
historical trace
operative disposition
current activation
successful elimination
```

The Kośa is already specifying an indexed state machine rather than a flat list of mental contents.

## OWL++ seed

```text
Class: AfflictiveConnection

Class: ObjectDirectedAnusaya
    SubClassOf: Anusaya

Class: Raga
    SubClassOf: ObjectDirectedAnusaya

Class: Pratigha
    SubClassOf: ObjectDirectedAnusaya

Class: Mana
    SubClassOf: ObjectDirectedAnusaya

ObjectProperty: hasArisenRegarding
    Domain: Anusaya
    Range: Vastu

ObjectProperty: connectsPersonTo
    Domain: Anusaya
    Range: Vastu

ObjectProperty: afflictsContinuum
    Domain: Anusaya
    Range: PersonContinuum

DataProperty: hasTemporalMode
    Range: {past, present, future}

DataProperty: hasAbandonmentStatus
    Range: {abandoned, unabandoned}

Rule:
    ObjectDirectedAnusaya(?a)
    afflictsContinuum(?a, ?p)
    hasArisenRegarding(?a, ?v)
    hasTemporalMode(?a, ?t)
    swrlb:member(?t, PastOrPresent)
    hasAbandonmentStatus(?a, unabandoned)
    -> connectedWith(?p, ?v)
```

## Bhāṣya questions

1. Does `pratyupasthita` here designate the present temporal category generally, or specifically an affliction presently manifest in consciousness?
2. Why are `rāga`, `pratigha`, and `māna` treated together in this rule, while the remaining anuśayas are deferred to 5.24?
3. Does `vastu` mean the particular object previously taken by the affliction, or a broader doctrinal basis or category?
4. How does the Bhāṣya distinguish an anuśaya that is past but unabandoned from one that is presently active?
5. Is `saṃyutaḥ` here ordinary conjunction, bondage to an object, or a technical relation distinct from `saṃprayukta`?

## Commit

```text
Add VAK 5.23 analysis
```
