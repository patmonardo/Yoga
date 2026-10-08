# VAK_2.29 — Counting Unwholesome Mental Factors

## 1. Sanskrit (Devanāgarī)

> आवेणिके त्वकुशले दृष्टियुक्ते च विंशतिः ।
>
> क्लेशैश्चतुर्भिः क्रोधाद्यैः कौकृत्येनैकविंशतिः ॥ २.२९ ॥

## 2. Sanskrit (IAST)

> āveṇike tv akuśale dṛṣṭiyukte ca viṃśatiḥ /
>
> kleśaiś caturbhiḥ krodhādyaiḥ kaukṛtyenaikaviṃśatiḥ // 2.29 //

## 3. Lexical Analysis

```text
āveṇike                 → āveṇike
tv                      → tu
akuśale                 → akuśale
dṛṣṭiyukte              → dṛṣṭi-yukte
ca                      → ca
viṃśatiḥ                → viṃśatiḥ
kleśaiś                 → kleśaiḥ
caturbhiḥ               → caturbhiḥ
krodhādyaiḥ             → krodha-ādyaiḥ
kaukṛtyenaikaviṃśatiḥ   → kaukṛtyena eka-viṃśatiḥ
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| āveṇike | locative neuter singular | in the isolated case |
| akuśale | locative neuter singular | in unwholesome consciousness |
| dṛṣṭi-yukte | locative neuter singular compound | in consciousness associated with a view |
| viṃśatiḥ | nominative feminine singular numeral | twenty |
| kleśaiḥ caturbhiḥ | instrumental plural phrase | with one of four afflictions |
| krodha-ādyaiḥ | instrumental plural compound | with a secondary affliction beginning with anger |
| kaukṛtyena | instrumental neuter singular | with remorse |
| eka-viṃśatiḥ | nominative feminine singular numeral | twenty-one |

The Bhāṣya distributes the additions. The four afflictions are greed,
hostility, conceit, and doubt. The anger-beginning secondary afflictions
are a distinct category; the commentary counts one such associate at a
time.

## 4. Grammar

The first line gives two cases with the same total:

```text
āveṇike akuśale
    → in isolated unwholesome consciousness

dṛṣṭi-yukte ca
    → and in consciousness associated with a view

viṃśatiḥ
    → twenty mental factors
```

The second line distributes the additional-factor cases:

```text
one of four afflictions
or one secondary affliction beginning with anger
or remorse
    → twenty-one mental factors
```

The view-associated case stays at twenty because view is a particular
determination of already-counted discernment. The separate associations
increase the count by one.

## 5. Scientific English Rendering

### Kārikā

> In isolated unwholesome consciousness and in consciousness associated
> with a view there are twenty [mental factors]. With one of the four
> afflictions, a secondary affliction beginning with anger, or remorse,
> there are twenty-one.

### Bhāṣya-informed rendering

> An isolated unwholesome consciousness contains twenty mental factors:
> ten universal great-ground factors, six afflicted great-ground factors,
> two unwholesome great-ground factors, *vitarka*, and *vicāra*.
> Unwholesome consciousness associated with wrong view, attachment to
> views, or attachment to rules and observances also contains twenty,
> because view is a particular form of discernment already counted in
> the universal factors. Association with one of the four afflictions—
> greed, hostility, conceit, or doubt—with one secondary affliction
> beginning with anger, or with remorse, makes twenty-one.

“Isolated” excludes another distinct affliction such as greed; it does
not exclude the factors required by the universal, afflicted,
unwholesome, and Desire-Principle grounds.

## 6. Interpretation

The verse and Bhāṣya distinguish specialization from addition. Wrong
view, attachment to views, and attachment to rules and observances are
particular determinations of the already-counted discernment factor;
naming the determination does not create a second factor. By contrast,
greed, hostility, conceit, doubt, one secondary affliction, or remorse
is an additional associated factor and increases the total.

The count therefore depends on resolving identity before counting:

```text
mode of an existing factor → same count
distinct associated factor → count increases by one
```

In the inner-instrument Techne, *mati* is identified with *prajñā* in
VAK 2.24, supporting the project rendering Science of Principles. A
particular view can determine that factor without being counted again
alongside it. This project application preserves the Bhāṣya's local
identity argument; it does not equate every Idea with a distinct
cognitive act.

The Kośa's governing synthesis: Vijñāna is Discriminative Cognition joining
and governing Perception and Conception. Their unity is Inconceivable as a
homogeneous operation; its Idea is disclosed in the Cognition Base. Vijñāna
governs Mind and guides the reading of Dharma Base. Form Base and Dharma
Base both include the same *avijñapti* in distinct classifications, and
Vijñāna bears a *prati* relation to *avijñapti*. This synthesis remains
distinct from the local count of associated mental factors.

## 7. Logical Determination

```text
UnwholesomeBase =
      UniversalGreatGroundTen
    ∪ AfflictedGreatGroundSix
    ∪ UnwholesomeGreatGroundTwo
    ∪ {Vitarka, Vicāra}

Count(UnwholesomeBase) = 20
```

```text
ViewMode ∈ {
    WrongView,
    AttachmentToViews,
    AttachmentToRulesAndObservances
}

BaseFunction(ViewMode) = Discernment
ViewAssociatedProfile = specialize(UnwholesomeBase, Discernment, ViewMode)
Count(ViewAssociatedProfile) = 20
```

```text
DistinctAdditionalFactor ∈ {
    one of Greed, Hostility, Conceit, Doubt,
    one SecondaryAfflictionBeginningWithAnger,
    Remorse
}

ExtendedProfile = UnwholesomeBase ∪ {DistinctAdditionalFactor}
Count(ExtendedProfile) = 21
```

## 8. Interpretive Note

“Ignorance alone” in the isolated case means no further distinct
affliction such as greed; it does not remove the other required factors.
Likewise, view's unwholesome classification is specific to wrong view
and the two attachments named by the Bhāṣya. The passage does not classify
all views as unwholesome.

The additions in the second line are alternatives, not a combined list.
The verse counts a profile with one additional factor, not a profile
containing the four afflictions, several secondary afflictions, and
remorse all together.

## 9. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_29
    a vak:Karika ;
    rdfs:label "VAK 2.29" ;
    vak:hasTopic vak:UnwholesomeMentalFactorCounts ;
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
    vak:addsOneAlternativeFrom vak:FourAfflictions,
        vak:SecondaryAfflictionsBeginningWithAnger,
        vak:Remorse ;
    vak:hasCount 21 .

organon:FactorCounting
    organon:distinguishes organon:FactorSpecialization,
        organon:DistinctFactorAddition .
```
