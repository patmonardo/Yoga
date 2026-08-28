# VAK_2.27

## 1. Sanskrit (Devanāgarī)

> क्रोधोपनाहशाठ्येर्ष्याप्रदासम्रक्षमत्सराः ।
>
> मायामदविहिंसाश्च परीत्तक्लेशभूमिकाः ॥ २.२७ ॥

## 2. Sanskrit (IAST)

> krodhopanāhaśāṭhyerṣyāpradāsamrakṣamatsarāḥ /
>
> māyāmadavihiṃsāś ca parīttakleśabhūmikāḥ // 2.27 //

## 3. Padaccheda

```text
krodhopanāhaśāṭhyerṣyāpradāsamrakṣamatsarāḥ
    → krodha-upanāha-śāṭhya-īrṣyā-pradāsa-mrakṣa-matsarāḥ

māyāmadavihiṃsāś ca
    → māyā-mada-vihiṃsāḥ ca

parīttakleśabhūmikāḥ
    → parītta-kleśa-bhūmikāḥ
```

| Form | Morphology | Lexical force here |
|---|---|---|
| krodha | masculine noun in compound | anger |
| upanāha | masculine noun in compound | resentment / retained hostility |
| śāṭhya | neuter noun in compound | deceitful crookedness |
| īrṣyā | feminine noun in compound | envy |
| pradāsa | masculine noun in compound | spite / hostile obstinacy |
| mrakṣa | masculine noun in compound | concealment of faults |
| matsara | masculine noun in compound | stinginess |
| māyā | feminine noun in compound | deception / false display |
| mada | masculine noun in compound | intoxication / prideful elation |
| vihiṃsā | feminine noun in compound | harmfulness / injuriousness |
| parītta-kleśa-bhūmikāḥ | nominative plural compound | belonging to the restricted ground of minor afflictions |

The dense surface compound `pradāsamrakṣa` separates as `pradāsa` and
`mrakṣa`. The Bhāṣya confirms the ten-member sequence but postpones detailed
definitions until its later treatment of secondary afflictions.

## 4. Grammar

The first line and the beginning of the second coordinate ten nominal
subjects. The final predicate classifies each of them:

```text
krodha ... vihiṃsāḥ
    → ten mental factors

parītta-kleśa-bhūmikāḥ
    → [each] belongs to the restricted ground of minor afflictions
```

The plural predicate does not mean that all ten necessarily co-arise as one
set. The Bhāṣya defines their common ground through three shared
restrictions:

```text
avidyā-mātreṇa saṃprayoga
    → associated only with ignorance

bhāvanā-heya
    → abandonable through cultivation

mano-bhūmika
    → belonging only to the mental sphere
```

`Parītta` therefore qualifies the extension of their operating ground. It
does not state that their ethical force or consequences are trivial.

## 5. Translation

### Close syntactic construe

> Anger, resentment, deceitful crookedness, envy, spite, concealment of faults, stinginess, deception, intoxication, and harmfulness belong to the restricted ground of minor afflictions.

### Bhāṣya-informed translation

> These ten factors form the class of restricted minor afflictions because each occurs only in association with ignorance, is abandoned through cultivation rather than through seeing, and belongs only to the mental sphere. They share these range conditions; the verse does not claim that all ten must occur together in every afflicted consciousness.

The individual definitions remain provisional at this point because the
Bhāṣya explicitly defers their detailed exposition.

## 6. Philosophical Translation

> A ground can unify factors without making them a simultaneous bundle. These afflictions belong together classificatorily because their ranges obey the same restrictions: they depend upon ignorance, arise only in the mental sphere, and are removed through cultivation. Their unity is a unity of distribution and path-treatment, not necessary co-presence.

Restrained Organon rendering:

> The class is defined intensionally by shared constraints, not extensionally as a required feature-set. Membership means satisfying the same association, domain, and abandonment rules. A valid model must therefore distinguish `ClassOfFactors` from `FactorsRequiredInEveryState`.

This distinction is project-level terminology applied to the Bhāṣya's exact
range restrictions.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination in this unit |
|---|---|---|
| parītta-kleśa-bhūmika | restricted-ground minor-affliction factor | fifth class in the mental-factor taxonomy |
| krodha | anger | detailed definition deferred |
| upanāha | resentment / grudge | detailed definition deferred |
| śāṭhya | deceitful crookedness | detailed definition deferred |
| īrṣyā | envy | detailed definition deferred |
| pradāsa | spite / hostile obstinacy | detailed definition deferred |
| mrakṣa | concealment of faults | detailed definition deferred |
| matsara | stinginess | detailed definition deferred |
| māyā | deception / false display | detailed definition deferred |
| mada | intoxication / prideful elation | detailed definition deferred |
| vihiṃsā | harmfulness | detailed definition deferred |
| avidyā-mātreṇa saṃprayoga | association only with ignorance | first restriction defining the class-ground |
| bhāvanā-heya | abandonable through cultivation | path-based restriction; not abandoned through seeing |
| mano-bhūmika | belonging to the mental sphere | excludes the sensory-consciousness spheres |
| aniyata | not fixed / indeterminate | Bhāṣya transition term for further factors outside the five fixed classes |

“Restricted” is preferred to “small” where the operating range is at issue.
The inherited label “minor affliction” is retained as the class name without
implying moral insignificance.

## 8. Logical Determination

Let:

```text
MinorAfflictionClass = {
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
```

Membership is defined by shared constraints:

```text
ForEvery factor f:
    MinorAfflictionFactor(f)
        → AssociatedOnlyWith(f, Ignorance)
        ∧ AbandonedBy(f, Cultivation)
        ∧ OperatesOnlyIn(f, MentalSphere)
```

It does not generate a universal conjunction rule:

```text
MinorAfflictionFactor(f)
∧ MinorAfflictionFactor(g)
    ⇏ NecessarilyCoarises(f, g)
```

This differs from the earlier grounds:

```text
UniversalGreatGroundFactor(f)
    → PresentIn(f, EveryCitta)

WholesomeGreatGroundFactor(f)
    → PresentIn(f, EveryWholesomeCitta)

MinorAfflictionFactor(f)
    → Range(f) satisfies three restrictions
      without universal presence in every afflicted citta
```

The fivefold taxonomy is now complete:

```text
CaittaGroundClass =
      UniversalGreatGround
    | WholesomeGreatGround
    | AfflictedGreatGround
    | UnwholesomeGreatGround
    | RestrictedMinorAfflictionGround
```

But the class union is not exhaustive of all mental factors:

```text
Exists factor f:
    MentalFactor(f)
    ∧ NotFixedToFiveGrounds(f)
```

The Bhāṣya names initial thought, sustained thought, regret, and torpor as
such `aniyata` factors, preparing the subsequent count analysis.

## 9. Interpretive Note

VAK 2.27 closes the fivefold taxonomy introduced in VAK 2.23, but it also
forces a refinement of what “ground” means. In the first four classes, the
Bhāṣya emphasized universal presence throughout a specified domain: every
consciousness, every wholesome consciousness, every afflicted consciousness,
or every unwholesome consciousness. The restricted-affliction class is not
presented as another universally co-arising bundle.

Its unity lies instead in three common restrictions. Each factor associates
only with ignorance, belongs only to the mental sphere, and is abandoned
through cultivation. The class therefore combines:

```text
association condition
    + operating domain
    + abandonment procedure
```

This is a genuine path-sensitive taxonomy. `Bhāvanā-heya` makes the means of
removal part of the factor's classification. Two factors may be grouped not
because they look alike or always appear together, but because they occupy
the same relation to ignorance, mental operation, and cultivation.

The point is also methodologically protective. If the ten names were encoded
as one `MinorAfflictionFeatureSet` required in every relevant state, the model
would assert precisely what the Bhāṣya does not say. A class-ground must be
represented by membership constraints rather than compulsory joint
instantiation.

Vasubandhu then closes the five classes while immediately noting factors not
fixed to them. The taxonomy is systematic without pretending that every
mental factor belongs universally to one ground. The next calculation must
therefore determine actual co-presence from the type of consciousness and the
conditional presence of these unfixed factors.

For the Kośa Technē, the restrained result is:

```text
GroundClass
    = shared range constraints

RequiredBundle
    = necessary co-presence rule

GroundClass ≠ RequiredBundle
```

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_27
    a vak:Karika ;
    rdfs:label "VAK 2.27" ;
    vak:hasTopic vak:RestrictedMinorAfflictionGround ;
    vak:belongsTo vak:Indriyanirdesa ;
    vak:closes vak:FivefoldCaittaGroundTaxonomy .

vak:RestrictedMinorAfflictionGround
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
    vak:hasAssociationRestriction vak:IgnoranceOnly ;
    vak:hasAbandonmentType vak:AbandonedThroughCultivation ;
    vak:hasOperatingDomain vak:MentalSphereOnly ;
    vak:doesNotImply vak:UniversalJointPresence .

organon:GroundClass
    a organon:InterpretiveReconstruction ;
    organon:definedBy organon:SharedRangeConstraints ;
    organon:distinctFrom organon:RequiredBundle ;
    organon:inferredFrom vak:RestrictedMinorAfflictionGround .
```
