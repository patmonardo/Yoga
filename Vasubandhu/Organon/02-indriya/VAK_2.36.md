# VAK_2.36 — Acquisition and Non-Acquisition

## 1. Sanskrit (Devanāgarī)

> नामकायादयश्चेति प्राप्तिर्लाभः समन्वयः ।
>
> प्राप्त्यप्राप्ती स्वसंतानपतितानां निरोधयोः ॥ २.३६ ॥

## 2. Sanskrit (IAST)

> nāmakāyādayaś ceti prāptir lābhaḥ samanvayaḥ /
>
> prāptyaprāptī svasaṃtānapatitānāṃ nirodhayoḥ // 2.36 //

The opening completes the VAK 2.35 catalogue. The research witness spaces
*svasaṃtāna patitānām*; the compound is joined for analysis.

## 3. Lexical Analysis

```text
nāmakāyādayaś ceti       → nāma-kāya-ādayaḥ ca iti
prāptir                   → prāptiḥ
lābhaḥ                    → lābhaḥ
samanvayaḥ                → samanvayaḥ
prāptyaprāptī             → prāpti-aprāptī
svasaṃtānapatitānāṃ       → sva-saṃtāna-patitānām
nirodhayoḥ                → nirodhayoḥ
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| nāma-kāya-ādayaḥ | nominative masculine plural compound | groups of names and related formations |
| iti | closing particle | completes the preceding catalogue |
| prāptiḥ | nominative feminine singular | acquisition |
| lābhaḥ | nominative masculine singular | obtaining |
| samanvayaḥ | nominative masculine singular | possession or continued endowment |
| prāpti-aprāptī | nominative feminine dual | acquisition and non-acquisition |
| sva-saṃtāna-patitānām | genitive plural compound | of what belongs to one's own continuum |
| nirodhayoḥ | genitive dual | of the two cessations |

## 4. Scientific English Rendering

> Groups of names and related formations complete the catalogue.
> Acquisition is obtaining and possession. Acquisition and non-acquisition
> apply to conditioned Dharmas belonging to one's own continuum and, among
> the unconditioned, to the two cessations.

The Bhāṣya distinguishes first obtaining what was absent or relinquished
from continuing to possess what has been obtained. It excludes another
continuum, what belongs to no continuum, and space from the relation's
range.

## 5. Interpretation

The verse specifies the boundary of a technical relation. *Prāpti* is not
the present manifestation of a Dharma, nor a loose predicate that can be
assigned to anything. It concerns a Dharma's acquisition or continued
endowment within the continuum to which it belongs; *aprāpti* is its
contrary only within this admissible range.

The Bhāṣya then makes the profound issue explicit. The Vaibhāṣikas treat
acquisition and non-acquisition as distinct real dissociated formations.
The critical account preserves the practical difference while rejecting an
additional entity: the status can be grounded in a continuum's seed-capacity,
transformation of support, and mastery of renewed arising.

The transition is therefore:

```text
Manifest event
    is not identical to
Continuum-status

Continuum-status
    is not identical to
An additional real possession-entity
```

This gives the Hub its first exact task. Vijñāna does not merely register an
event in the Impure Wheel; it governs the intelligibility of how a Dharma's
causal capacity is retained, transformed, foreclosed, or made available
across the continuum.

The Kośa's governing synthesis remains: Vijñāna is Discriminative Cognition
joining and governing Perception and Conception. Their unity is
Inconceivable as homogeneous operation, with its Idea disclosed in the
Cognition Base. Vijñāna governs Mind and guides Dharma Base. Form Base and
Dharma Base both classify the same *avijñapti*, with Vijñāna bearing a
*prati* relation to it. The local dispute over *prāpti* concerns how a
continuum-status is grounded, not whether these terms collapse into one.

## 6. Logical Determination

The relation's range:

```text
Admissible(S, D)
    := Conditioned(D) and BelongsToOwnContinuum(D, S)
       or D is one of the two cessations
```

The first definition:

```text
Prapti(S, D)
    := NewlyObtained(S, D)
       or ContinuesToPossess(S, D)

Aprapti(S, D)
    := not Prapti(S, D)
       within Admissible(S, D)
```

Thus:

```text
OutsideRange(S, D)
    is not Aprapti(S, D)
```

The disputed ground:

```text
Vaibhasika:
    Prapti(S, D) requires an additional real Dharma

Critical account:
    Prapti(S, D) is designated from
        SeedCapacity(S, D)
        + SupportTransformation(S)
        + RenewedArisingCapacity(S, D)
        + Mastery(S, D)
```

## 7. Interpretive Note

The Bhāṣya does not deny the difference between acquired and unacquired
status. It asks what makes that difference true. Its critical line opposes
the inference from the word “possession” to a distinct real Dharma:
scriptural possession can also mean mastery, tolerance, or failure to
expel. It further argues that acquisition cannot be a universal production
cause, since unconditioned Dharmas do not arise and different degrees of
affliction require a more discriminating ground.

For abandoned afflictions, the support is transformed by the Paths of
seeing and cultivation so that it cannot produce the relevant affliction
again. The Bhāṣya compares that support to rice burned by fire. For
effortless wholesome Dharmas, possession rests on unimpaired seed-capacity;
for effort-produced wholesome Dharmas, it rests on mastery of renewed
arising. This is the distinction required to understand why a continuum may
be held back from a result it has not attained without treating absence as
a mere lack of present appearance.

## 8. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_36
    a vak:Karika ;
    rdfs:label "VAK 2.36" ;
    vak:hasTopic vak:AcquisitionAndNonAcquisition ;
    vak:belongsTo vak:Indriyanirdesa .

vak:Acquisition
    vak:includes vak:NewObtaining,
        vak:ContinuedPossession ;
    vak:hasDomain vak:OwnContinuumDharma,
        vak:TwoCessations .

vak:NonAcquisition
    vak:isContraryTo vak:Acquisition ;
    vak:hasDomain vak:OwnContinuumDharma,
        vak:TwoCessations .

vak:CriticalAccountOfAcquisition
    vak:groundsStatusIn vak:SeedCapacity,
        vak:SupportTransformation,
        vak:RenewedArisingCapacity,
        vak:Mastery ;
    vak:rejects vak:AdditionalRealPossessionEntity .
```
