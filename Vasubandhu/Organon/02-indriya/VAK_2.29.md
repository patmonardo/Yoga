# VAK_2.29

## 1. Sanskrit (Devanāgarī)

> आवेणिके त्वकुशले दृष्टियुक्ते च विंशतिः ।
>
> क्लेशैश्चतुर्भिः क्रोधाद्यैः कौकृत्येनैकविंशतिः ॥ २.२९ ॥

## 2. Sanskrit (IAST)

> āveṇike tv akuśale dṛṣṭiyukte ca viṃśatiḥ /
>
> kleśaiś caturbhiḥ krodhādyaiḥ kaukṛtyenaikaviṃśatiḥ // 2.29 //

## 3. Padaccheda

```text
āveṇike            → āveṇike
tv                  → tu
akuśale            → akuśale
dṛṣṭiyukte         → dṛṣṭi-yukte
ca                  → ca
viṃśatiḥ           → viṃśatiḥ
kleśaiś            → kleśaiḥ
caturbhiḥ          → caturbhiḥ
krodhādyaiḥ        → krodha-ādyaiḥ
kaukṛtyenaikaviṃśatiḥ
                    → kaukṛtyena eka-viṃśatiḥ
```

| Form | Morphology | Lexical force here |
|---|---|---|
| āveṇike | locative neuter singular | in the isolated case |
| akuśale | locative neuter singular | in unwholesome consciousness |
| dṛṣṭi-yukte | locative neuter singular compound | in consciousness associated with a view |
| viṃśatiḥ | nominative feminine singular numeral | twenty |
| kleśaiḥ caturbhiḥ | instrumental plural phrase | with any one of four [root] afflictions |
| krodha-ādyaiḥ | instrumental plural compound | with a secondary affliction beginning with anger |
| kaukṛtyena | instrumental neuter singular | with remorse |
| eka-viṃśatiḥ | nominative feminine singular numeral | twenty-one |

The Bhāṣya distributes the instrumental alternatives. The four afflictions
are greed, hostility, conceit, and doubt. `Krodhādyaiḥ` then introduces a
separate class of secondary afflictions beginning with anger; it does not
mean “four afflictions beginning with anger.”

## 4. Grammar

The first line gives two twenty-factor cases:

```text
āveṇike akuśale
    → in an isolated unwholesome consciousness

dṛṣṭi-yukte ca
    → and in one associated with view

viṃśatiḥ
    → there are 20 mental factors
```

The Bhāṣya defines `āveṇika` as a state in which ignorance occurs without an
additional distinct affliction such as greed. “Ignorance alone” does not
remove the other factors required by the universal, afflicted, unwholesome,
and desire-realm grounds.

The second line carries one count across three alternatives:

```text
one of four root afflictions
or one secondary affliction beginning with anger
or remorse
    → 21 mental factors
```

The singular event-profile takes one additional factor in each case; the
verse does not require all the alternatives to be conjoined.

## 5. Translation

### Close syntactic construe

> In an isolated unwholesome consciousness, and in one associated with view, there are twenty [mental factors]. With [one of] the four afflictions, with [a secondary affliction] beginning with anger, or with remorse, there are twenty-one.

### Bhāṣya-informed translation

> An unwholesome desire-realm consciousness in which ignorance occurs without another distinct affliction contains twenty mental factors. A consciousness associated with wrong view, attachment to views, or attachment to rules and observances also contains twenty, because view is an afflicted specialization of discernment already included among the universal factors. Adding greed, hostility, conceit, doubt, one secondary affliction beginning with anger, or remorse raises the total to twenty-one.

The count distinguishes a modified operation of an inherited factor from the
addition of a numerically distinct associated factor.

## 6. Philosophical Translation

> Description must follow functional identity rather than vocabulary. “View” adds a determination to discernment but no new constituent, because it is discernment operating in an afflicted mode. Greed, hostility, conceit, doubt, the secondary afflictions, and remorse are distinct associates and therefore enlarge the event-profile. A new predicate does not necessarily mean a new factor.

Restrained Organon rendering:

> State specialization and state extension are different operations. Specializing an inherited factor changes its mode while preserving cardinality; adjoining a distinct factor changes both membership and count. The model must resolve identity before counting labels.

This distinction is a project rendering of the Bhāṣya's explanation that
view is a `prajñā-viśeṣa`, a special determination of discernment.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Bhāṣya determination |
|---|---|---|
| āveṇika-citta | isolated consciousness | ignorance present without another distinct root or secondary affliction |
| akuśala | unwholesome | ethical determination of all profiles counted here |
| dṛṣṭi-yukta | associated with view | discernment operating as one of three unwholesome views |
| prajñā-viśeṣa | special determination of discernment | explains why view does not add to the count |
| mithyā-dṛṣṭi | wrong view | first view-associated case named by the Bhāṣya |
| dṛṣṭi-parāmarśa | attachment to views | second view-associated case |
| śīla-vrata-parāmarśa | attachment to rules and observances | third view-associated case |
| rāga | greed / attachment | one of four distinct root afflictions that adds one factor |
| pratigha | hostility | one of the four |
| māna | conceit | one of the four |
| vicikitsā | doubt | one of the four |
| krodhādi | secondary affliction beginning with anger | any one adds a distinct twenty-first factor |
| kaukṛtya | remorse | here an unwholesome conditional twenty-first factor |

The Bhāṣya speaks of a named view as a form of the universal discernment
factor. It does not posit view as a twenty-first factor alongside discernment.

## 8. Logical Determination

The unwholesome desire-realm base is:

```text
UnwholesomeBase =
      UniversalGreatGroundTen
    ∪ AfflictedGreatGroundSix
    ∪ UnwholesomeGreatGroundTwo
    ∪ {Vitarka, Vicāra}

Count(UnwholesomeBase) = 20
```

The isolated profile is exactly this base:

```text
IsolatedUnwholesomeProfile
    = UnwholesomeBase

DistinctAdditionalAffliction = none
```

View specializes an existing member:

```text
ViewMode ∈ {
    WrongView,
    AttachmentToViews,
    AttachmentToRulesAndObservances
}

BaseFunction(ViewMode) = Discernment
Discernment ∈ UniversalGreatGroundTen

ViewAssociatedProfile
    = specialize(UnwholesomeBase.Discernment, ViewMode)

Count = 20
```

A distinct associated factor extends the set:

```text
AdditionalFactor ∈ {
    Greed,
    Hostility,
    Conceit,
    Doubt,
    one SecondaryAfflictionBeginningWithAnger,
    Remorse
}

ExtendedUnwholesomeProfile
    = UnwholesomeBase ∪ {AdditionalFactor}

Count = 21
```

The governing rule is:

```text
Specialization(existingFactor)
    → count unchanged

Addition(distinctFactor)
    → count + 1

DifferentName(x, y)
    ⇏ DistinctFactor(x, y)
```

## 9. Interpretive Note

VAK 2.29 uses counting to force an ontological and functional decision. The
unwholesome base contains twenty factors inherited from four sources: the ten
universal factors, six specifically afflicted factors, two specifically
unwholesome factors, and the desire-realm pair `vitarka` and `vicāra`.

An isolated unwholesome consciousness has this base with ignorance but no
additional distinct affliction. The other five afflicted great-ground factors
remain present because they are necessary throughout afflicted consciousness;
“ignorance alone” concerns the absence of another root or secondary
affliction, not an otherwise empty mental state.

The view-associated case demonstrates mode specialization. Wrong view,
attachment to views, and attachment to rules and observances are forms of
discernment. Since discernment is already universally present, applying an
afflicted view-mode changes the determination of that factor without adding a
new member.

The other cases demonstrate extension. Greed, hostility, conceit, doubt, a
secondary affliction, or remorse is a distinct associated factor. Each raises
the profile from twenty to twenty-one. The same arithmetic therefore records
a conceptual distinction:

```text
modification of what is already present
    versus
addition of another present factor
```

This is exactly why mental-factor analysis cannot be implemented as a bag of
descriptive tags. Two tags may denote one factor under different modes, while
one optional association may introduce a genuinely new factor. Identity and
provenance must be resolved before cardinality.

For the Kośa Technē, the restrained result is:

```text
specializeFactor(profile, factor, mode)
    preserves membership count

associateFactor(profile, distinctFactor)
    increments membership count
```

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_29
    a vak:Karika ;
    rdfs:label "VAK 2.29" ;
    vak:hasTopic vak:UnwholesomeCaittaProfiles ;
    vak:belongsTo vak:Indriyanirdesa .

vak:UnwholesomeBaseProfile
    vak:inherits vak:UniversalGreatGroundTen,
        vak:AfflictedGreatGroundSix,
        vak:UnwholesomeGreatGroundTwo ;
    vak:requires vak:Vitarka,
        vak:Vicara ;
    vak:hasCount 20 .

vak:ViewAssociatedProfile
    vak:hasBase vak:UnwholesomeBaseProfile ;
    vak:specializes vak:Discernment ;
    vak:hasCount 20 .

vak:ExtendedUnwholesomeProfile
    vak:hasBase vak:UnwholesomeBaseProfile ;
    vak:addsOneFrom vak:FourRootAfflictions,
        vak:SecondaryAfflictionsBeginningWithAnger,
        vak:Remorse ;
    vak:hasCount 21 .

organon:FactorIdentityBeforeCounting
    a organon:InterpretiveReconstruction ;
    organon:distinguishes organon:FactorSpecialization,
        organon:DistinctFactorAddition ;
    organon:inferredFrom vak:UnwholesomeCaittaProfiles .
```
