# VAK_2.27 — The Restricted Ground of Afflictions

## 1. Sanskrit (Devanāgarī)

> क्रोधोपनाहशाठ्येर्ष्याप्रदासम्रक्षमत्सराः ।
>
> मायामदविहिंसाश्च परीत्तक्लेशभूमिकाः ॥ २.२७ ॥

## 2. Sanskrit (IAST)

> krodhopanāhaśāṭhyerṣyāpradāsamrakṣamatsarāḥ /
>
> māyāmadavihiṃsāś ca parīttakleśabhūmikāḥ // 2.27 //

## 3. Lexical Analysis

```text
krodhopanāhaśāṭhyerṣyāpradāsamrakṣamatsarāḥ
    → krodha-upanāha-śāṭhya-īrṣyā-pradāsa-mrakṣa-matsarāḥ
māyāmadavihiṃsāś ca
    → māyā-mada-vihiṃsāḥ ca
parīttakleśabhūmikāḥ
    → parītta-kleśa-bhūmikāḥ
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| krodha | masculine noun in compound | anger |
| upanāha | masculine noun in compound | resentment |
| śāṭhya | neuter noun in compound | deceitful crookedness |
| īrṣyā | feminine noun in compound | envy |
| pradāsa | masculine noun in compound | spite |
| mrakṣa | masculine noun in compound | concealment of faults |
| matsara | masculine noun in compound | stinginess |
| māyā | feminine noun in compound | deception |
| mada | masculine noun in compound | intoxication |
| vihiṃsā | feminine noun in compound | harmfulness |
| parītta-kleśa-bhūmikāḥ | nominative plural compound | belonging to the restricted ground of afflictions |

The dense sequence *pradāsamrakṣa* divides into *pradāsa* and *mrakṣa*.
The Bhāṣya confirms the ten members but defers their individual
definitions.

## 4. Grammar

Ten nominal subjects are classified by the final predicate:

```text
krodha ... vihiṃsāḥ
    → ten mental factors

parītta-kleśa-bhūmikāḥ
    → belonging to the restricted ground of afflictions
```

The Bhāṣya defines their shared range by association with ignorance,
abandonment through cultivation, and operation only in the mental sphere.
The plural predicate names a class; it does not say that all ten
necessarily co-arise as one set.

## 5. Scientific English Rendering

### Kārikā

> Anger, resentment, deceitful crookedness, envy, spite, concealment of
> faults, stinginess, deception, intoxication, and harmfulness belong to
> the restricted ground of afflictions.

### Bhāṣya-informed rendering

> These factors belong to the restricted ground of afflictions because
> they are associated only with ignorance that is abandonable through
> cultivation and belongs to the mental sphere. Their individual
> definitions will be given in the discussion of secondary afflictions.
> The five classes of mental factors have now been stated. There are also
> further unfixed factors, such as initial examination, sustained
> examination, regret, and torpor.

“Restricted” describes the range of this class, not the moral significance
of an individual occurrence. “Unfixed” translates *aniyata* here; it does
not mean ethically indeterminate.

## 6. Interpretation

The ten members share three stated restrictions: their association is
with ignorance, they are abandonable through cultivation, and they
operate only in the mental sphere. The Bhāṣya does not assert that they
form a bundle necessarily present together in every consciousness or
every afflicted consciousness. Nor does *parītta* declare their effects
trivial.

In the Organon framework, the ten Samyama-bhūmis describe Path-related
operation of mental factors, with Buddha Dharma as the 11th Bhūmi. This
verse supports only its own stated constraints; it does not assign the
ten factors to individual Bhūmis or establish co-occurrence. The
following count inquiry must determine particular distributions rather
than assuming them from the class name.

The Kośa's governing synthesis: Vijñāna is Discriminative Cognition joining
and governing Perception and Conception. Their unity is Inconceivable as a
homogeneous operation; its Idea is disclosed in the Cognition Base. Vijñāna
governs Mind and guides the reading of Dharma Base. Form Base and Dharma
Base both include the same *avijñapti* in distinct classifications, and
Vijñāna bears a *prati* relation to *avijñapti*. This does not turn the
mental factors into Faculties.

## 7. Logical Determination

```text
RestrictedAfflictionClass = {
    Anger,
    Resentment,
    DeceitfulCrookedness,
    Envy,
    Spite,
    ConcealmentOfFaults,
    Stinginess,
    Deception,
    Intoxication,
    Harmfulness
}

For every factor f in RestrictedAfflictionClass:
    AssociatedWith(f, Ignorance)
    ∧ AbandonedThrough(f, Cultivation)
    ∧ OperatesOnlyIn(f, MentalSphere)
```

Class membership supplies shared range constraints, not a compulsory
co-arising rule:

```text
f, g ∈ RestrictedAfflictionClass
    ⇏ NecessarilyCoarises(f, g)
```

The Bhāṣya's *aniyata* examples name further factors beyond the five
classes without specifying their full distributions in this verse.

## 8. Interpretive Note

The verse closes the fivefold classification introduced in VAK 2.23,
then the Bhāṣya immediately acknowledges factors not fixed to those
classes. The taxonomy is systematic but not an exhaustive inventory of
every mental factor. The next unit asks how many factors necessarily
occur in particular consciousnesses.

“Restricted ground of afflictions” names the class in this verse.
*Upakleśa*, the discussion where individual definitions are deferred,
is rendered separately as “secondary afflictions”; the two terms are
not treated as interchangeable names for identical ranges.

## 9. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_27
    a vak:Karika ;
    rdfs:label "VAK 2.27" ;
    vak:hasTopic vak:RestrictedAfflictionGround ;
    vak:belongsTo vak:Indriyanirdesa ;
    vak:closes vak:FivefoldCaittaGroundTaxonomy .

vak:RestrictedAfflictionGround
    vak:hasMember vak:Anger,
        vak:Resentment,
        vak:DeceitfulCrookedness,
        vak:Envy,
        vak:Spite,
        vak:ConcealmentOfFaults,
        vak:Stinginess,
        vak:Deception,
        vak:Intoxication,
        vak:Harmfulness ;
    vak:hasAssociationRestriction vak:Ignorance ;
    vak:hasAbandonmentType vak:AbandonedThroughCultivation ;
    vak:hasOperatingSphere vak:MentalSphere ;
    vak:doesNotImply vak:UniversalJointPresence .

vak:FurtherUnfixedFactors
    vak:hasExample vak:InitialExamination,
        vak:SustainedExamination,
        vak:Regret,
        vak:Torpor .

organon:GroundClass
    a organon:InterpretiveReconstruction ;
    organon:definedBy organon:SharedRangeConstraints ;
    organon:distinctFrom organon:RequiredBundle .
```
