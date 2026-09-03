# VAK_5.23

## 1. Sanskrit (Devanāgarī)

```sanskrit
रागप्रतिघमानैः स्यादतीतप्रत्युपस्थितैः ।
यत्रोत्पन्नाप्रहीणास्ते तस्मिन् वस्तुनि संयुतः ॥ ५.२३ ॥
```

## 2. Sanskrit (IAST)

```text
rāga-pratigha-mānaiḥ syād atīta-pratyupasthitaiḥ |
yatrotpannāprahīṇās te tasmin vastuni saṃyutaḥ || 5.23 ||
```

The verse begins a new relational analysis of bondage. The Bhāṣya introduces
attachment, aversion, and conceit as particular-character afflictions and
contrasts them with the general-character afflictions treated in VAK 5.24.

## 3. Padaccheda and Lexical Analysis

```text
rāga-pratigha-mānaiḥ | syāt | atīta-pratyupasthitaiḥ | yatra |
utpannāḥ | aprahīṇāḥ | te | tasmin | vastuni | saṃyutaḥ
```

| Form | Morphology | Contextual sense |
|---|---|---|
| `rāga-pratigha-mānaiḥ` | instrumental plural compound | through attachment, aversion, and conceit |
| `syāt` | third-person singular optative of `√as` | one would be; one is considered |
| `atīta-pratyupasthitaiḥ` | instrumental plural compound | by past or presently arisen afflictions |
| `yatra` | relative adverb | where; with respect to whichever object |
| `utpannāḥ` | nominative plural masculine | arisen, become actual |
| `aprahīṇāḥ` | nominative plural masculine | unabandoned, not eliminated |
| `te` | nominative plural pronoun | those [afflictions] |
| `tasmin vastuni` | locative singular | in or with respect to that object or matter |
| `saṃyutaḥ` | nominative singular masculine | connected, bound |

The Bhāṣya glosses the kārikā's `pratyupasthita` with `pratyutpanna`, fixing
the relevant temporal contrast as past and present.

## 4. Grammar

**Instrument of connectedness**

```text
rāga-pratigha-mānaiḥ
atīta-pratyupasthitaiḥ
saṃyutaḥ syāt

one is connected through attachment, aversion, and conceit
that are past or present
```

The instrumental compounds specify the afflictions through which the
connection holds. The singular subject of `syāt` and `saṃyutaḥ` is an
understood person or continuum.

**Relative-correlative object index**

```text
yatra [vastuni] utpannāḥ te aprahīṇāḥ,
tasmin vastuni [taiḥ] saṃyutaḥ

with respect to whichever object those afflictions arose
and remain unabandoned,
one is connected with that object through them
```

`Yatra ... tasmin` ensures identity of the object of arising and the object of
continued bondage. `Aprahīṇāḥ` is not a synonym for “present”; it qualifies
past and present afflictions alike.

## 5. Translation

### Literal Translation

> Through past or present attachment, aversion, and conceit, one is connected
> with that object regarding which those [afflictions] have arisen and remain
> unabandoned.

### Bhāṣya-informed study translation

> Attachment, aversion, and conceit are particular-character afflictions. A
> person is bound through a past or present instance of one of them precisely
> to the particular object regarding which it arose, so long as the affliction
> has not been abandoned. These afflictions do not necessarily arise in every
> person or toward every object.

The classification as `svalakṣaṇa-kleśa` and the threefold denial of universal
occurrence are supplied by the Bhāṣya.

## 6. Philosophical Translation

> Bondage is not an abstract property of a subject. It is a determinate
> relation in which this person is connected with this object through an
> affliction that actually arose and has not been overcome. The occurrence may
> have passed temporally while its determining efficacy remains. Chronological
> absence therefore does not constitute liberation; only abandonment removes
> the bond sustained by the past determination.

The relation requires five coordinates:

```text
person
affliction-type
particular object
temporal status
abandonment status
```

Remove the object-index and a particular affliction is falsely promoted into a
universal trait. Remove abandonment-status and a past event is falsely treated
as either fully active or wholly ineffective.

## 7. Technical Vocabulary

**`Svalakṣaṇa-kleśa` — particular-character affliction**

The Bhāṣya assigns attachment, aversion, and conceit to this class. Each arises
selectively with respect to a determinate object; none necessarily occurs for
every person with respect to every object.

**`Sāmānya-kleśa` — general-character affliction**

View, doubt, and ignorance form the contrasting class. The Bhāṣya names them
here but reserves their rule of connectedness for VAK 5.24.

**`Rāga` — attachment**

An appropriative attraction toward a particular `vastu`. Its existence in a
continuum does not entail attachment toward all objects.

**`Pratigha` — aversion or resistance**

An oppositional relation indexed to the object regarding which it arose.

**`Māna` — conceit**

Comparative self-positioning through a determinate object or basis of
comparison. Its bond is likewise object-specific.

**`Atīta` and `pratyutpanna` — past and present**

The Bhāṣya clarifies that the verse includes both temporal classes. Future
afflictions are not included in this particular rule of actual arisen
connection.

**`Utpanna` — arisen**

The affliction must have become actual with respect to the object. Mere
possibility or class-membership does not establish the bond.

**`Aprahīṇa` — unabandoned**

The decisive persistence condition. An affliction may be past as an occurrence
yet remain effective because the Path has not eliminated it.

**`Vastu` and `saṃyuta`**

`Vastu` is the determinate object or matter regarding which the affliction
arose. `Saṃyuta` names the person's resulting connectedness with that object;
it should not be collapsed into the co-arising relation `saṃprayukta` analyzed
in VAK 5.18.

## 8. Logical Determination

The particular bondage relation is:

```text
AfflictionType(a) ∈ {Attachment, Aversion, Conceit}
AND AfflictsContinuum(a, p)
AND AroseRegarding(a, v)
AND TemporalStatus(a) ∈ {Past, Present}
AND NotAbandoned(a)
    → ConnectedThrough(p, v, a)
```

The object identity is strict:

```text
AroseRegarding(a, v1)
    ⇏ ConnectedThrough(p, v2, a)
        when v1 ≠ v2
```

Temporal and operative status must be separated:

```text
Past(a)
    ⇏ Abandoned(a)

NotPresentlyOccurring(a)
    ⇏ Inoperative(a)

Abandoned(a)
    → NoLongerConnectsThrough(p, v, a)
```

The Bhāṣya's threefold negation blocks universalization:

```text
not for every person
not necessarily
not toward every object
```

## 9. Interpretive Note

VAK 5.23 places the fourfold circuit inside a single concrete bond:

```text
hetu
    the arisen and still-unabandoned particular affliction

phala
    the person's continuing connectedness with its object

āśraya
    the concrete continuum in which the disposition remains operative

ālambana
    the particular vastu regarding which it arose
```

Here the Product is not an external thing standing opposite the Subject. It is
the achieved relation `ConnectedThrough(person, object, affliction)`. The
Subject inheres in this relation through its continuum; the object is
determinate as the affliction's `ālambana`; the unabandoned affliction is the
operative `hetu`; the continuing bond is its `phala`.

This gives Hegelian determinate negation a precise practical content. Merely
passing into the past is abstract negation: the event is no longer now, but its
determining relation persists. `Prahāṇa` is concrete negation because it removes
the efficacy through which the past continues to organize the present.

```text
chronological past
    event no longer occurring
    but relation may remain operative

abandonment
    determining efficacy transformed
    therefore bond no longer reproduced
```

The Path in itself contains the adequate operation of abandonment; the Path-
bhūmi in appearance exhibits that operation as an altered field of possible
relations. A claim of progress is therefore tested not by elapsed time or a
new self-description, but by whether the former object-bond can still be
generated.

This also protects the Subject from being converted into a bundle of global
traits. “Attached,” “averse,” or “conceited” is incomplete until the system
records toward what, through which occurrence, at what time, and with what
abandonment-status. Subjectivity becomes concrete through indexed relations.

This is Organon–Yoga–Hegel reconstruction. Its textual ground is the Bhāṣya's
`svalakṣaṇa-kleśa` classification, the verse's object identity, and the
distinction between temporal pastness and abandonment.

## 10. OWL++ Seed

```ttl
vak:VAK_5_23 a vak:Karika ;
    rdfs:label "VAK 5.23" ;
    vak:continues vak:VAK_5_22 ;
    vak:hasTopic vak:ParticularAfflictiveConnection,
                 vak:PastOperativeDisposition .

vak:ParticularCharacterAffliction
    vak:includes vak:Attachment,
                 vak:Aversion,
                 vak:Conceit .

vak:AfflictiveConnectionRule a vak:RelationRule ;
    vak:requires vak:ActualArisingRegardingObject,
                 vak:PastOrPresentTemporalStatus,
                 vak:UnabandonedStatus ;
    vak:produces vak:PersonObjectConnection .

vak:PersonObjectConnection
    vak:hasHetuFunction vak:UnabandonedParticularAffliction ;
    vak:hasPhalaFunction vak:ContinuingBond ;
    vak:hasAsrayaFunction vak:AfflictedContinuum ;
    vak:hasAlambanaFunction vak:ParticularVastu .

vak:ChronologicalPastness
    owl:distinctFrom vak:Abandonment .

vak:GeneralCharacterAffliction
    vak:includes vak:View,
                 vak:Doubt,
                 vak:Ignorance ;
    vak:determinedFurtherIn vak:VAK_5_24 .
```

The seed represents bondage as an indexed relation rather than a Boolean
property of a person. It keeps temporal status distinct from operative
abandonment.
