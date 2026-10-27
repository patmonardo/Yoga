# VAK_3.23 Bhāṣya — From Feeling to Appropriation

## 1. Kārikā Anchor

> vittiḥ prāk maithunāt tṛṣṇā bhogamaithunarāgiṇaḥ /
> upādānaṃ tu bhogānāṃ prāptaye paridhāvataḥ // 3.23 //

> The Feeling-stage precedes sexual coupling. Craving is the state of one
> passionate about sensual enjoyment and sexual coupling; Appropriation is
> the state of one who runs about to obtain enjoyments.

## 2. Continuous Sanskrit

> paricchedasāmarthye sati—
>
> vittiḥ prāk maithunāt /
>
> vedanāvasthā yāvan maithunarāgo na samudācarati /
>
> tṛṣṇā bhogamaithunarāgiṇaḥ /
>
> kāmaguṇamaithunarāgasamudācārāvasthā tṛṣṇety ucyate yāvan na
> tadviṣayaparyeṣṭim āpadyate /
>
> upādānaṃ tu bhogānāṃ prāptaye paridhāvataḥ // 3.23 //
>
> yasyām avasthāyāṃ viṣayaprāptaye paryeṣṭim āpannaḥ sarvato dhāvati,
> asāv avasthā upādānam ity ucyate /

This natural unit runs from the second statement at printed 132.11 through
the first statement at 132.18 in `Vasubandhu/Sources/kosabhasya.txt`. The
inherited phrase *paricchedasāmarthye sati* links the Feeling-stage to the
capacity established in VAK 3.22. The next prose begins the definition of
Becoming in VAK 3.24 with *tathā ca paridhāvan*.

Word division and punctuation are editorial. No substantive conjectural
repair has been introduced; the running source remains unchanged.

## 3. Continuous Translation
Once the capacity for discrimination is present:

> Feeling is before sexual coupling.

The Feeling-stage continues as long as sexual passion has not become
actively manifest.

> Craving is the state of one passionately attached to sensual enjoyment and
> sexual coupling.

The state in which passion for sensual enjoyments and sexual coupling
becomes active is called Craving. It continues until one enters into a
search for that Condition.

> Appropriation is the state of one running about to attain enjoyments.

The state in which one has entered a search to attain the Condition and
runs everywhere for it is called Appropriation.

## 4. Commentary Movement

Vasubandhu proceeds without introducing an opponent or alternate position.
The Bhāṣya differentiates the three stages by the operation that becomes
active:

```text
capacity to discriminate causes of Feeling
    → Feeling-stage

passion becomes actively manifest
    → Craving

search to attain the Condition begins
    → Appropriation
```

The transition from Craving to Appropriation is qualitative. The Condition
is no longer only the focus of passion; activity is now organized around
seeking and attaining it. *Sarvato dhāvati*, “runs everywhere,” specifies
the reach of that pursuit.

The sought *viṣaya* is a Condition: a specific moment of the Seen and part
of the playground in which Faculties operate. Object names the comprehended
truth of Vastu, not the Condition being pursued. This keeps the sensory
relation from collapsing into a fixed target of attention.

## 5. Interpretation

### Three functional thresholds

The lower boundary of the Feeling-stage is the capacity to discriminate the
causes of the three Feelings, inherited from VAK 3.22. Its upper boundary is
the active manifestation of sexual passion. Thus Feeling is not already
Craving: the stages are discriminated by operation, not merely ranked as
increasing intensities. They are objective distinctions in the conditioned
sequence, not a universal psychological or age timetable.

### Craving and organized pursuit

The horizontal reach becomes explicit in Appropriation: pursuit extends in
all directions to attain the Condition. But its direction is supplied by
Craving. This outward expansion is not itself vertical knowing. The earlier
capacity to discriminate causes and the later activity of pursuit must
remain distinct.

### Feeling within the root-framework

Within the project's root-framework reading, Dharma Essence integrates the
sixfold Essence structure while Feeling remains a distinct determination
within the wider framework. Here Feeling is given its own stage, boundary,
and relation to passion. Integration does not collapse its role into the
six Essences or into Craving.

### Vijñāna in the wider Kośa

At the level of the Kośa's wider cognitive architecture, Vijñāna is
Discriminative Cognition joining and governing Perception and Conception;
their unity is not a homogeneous operation, and its Idea is disclosed in
the Cognition Base. Vijñāna governs Mind and guides the reading of Dharma
Base. Its relation to Avijñapti, and Avijñapti's distinct classifications
in Form Base and Dharma Base, must likewise remain discriminated. This
verse's sequence concerns Feeling, Craving, and Appropriation; it does not
make them interchangeable with that wider cognitive architecture.

## 6. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .

vak:VAK_3_23
    a vak:Karika ;
    vak:continues vak:VAK_3_22 ;
    vak:definesStage vak:FeelingStage, vak:CravingStage,
        vak:AppropriationStage .

vak:FeelingStage
    a vak:TemporalStage ;
    vak:hasDesignation vak:Vitti ;
    vak:endsAt vak:ActiveManifestationOfPassion ;
    vak:requires vak:CauseDiscriminationCapacity .

vak:CravingStage
    a vak:TemporalStage ;
    vak:hasDesignation vak:Trsna ;
    vak:orientsToward vak:SensualEnjoyment ;
    vak:endsAt vak:SearchForCondition .

vak:AppropriationStage
    a vak:TemporalStage ;
    vak:hasDesignation vak:Upadana ;
    vak:hasOperation vak:SearchForCondition ;
    vak:hasEnd vak:AttainmentOfEnjoyment ;
    organon:extendsInAllDirections true .
```

## 7. Review Status

Kārikā Anchor aligned with the kārikā study's Bhāṣya-informed translation.
The continuous Sanskrit and translation cover the second statement at 132.11
through the first statement at 132.18; the next phrase at 132.18 begins VAK
3.24. No outright omission was found in this range.
