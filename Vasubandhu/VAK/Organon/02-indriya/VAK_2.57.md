# VAK_2.57

## 1. Sanskrit (Devanāgarī)

> विपाकोऽव्याकृतो धर्मः सत्त्वाख्यो व्याकृतोद्भवः ।
>
> निःष्यन्दो हेतुसदृशो विसंयोगः क्षयो धिया ॥ २.५७ ॥

## 2. Sanskrit (IAST)

> vipāko 'vyākṛto dharmaḥ sattvākhyo vyākṛtodbhavaḥ /
>
> niḥṣyando hetusadṛśo visaṃyogaḥ kṣayo dhiyā // 2.57 //

## 3. Padaccheda

```text
vipāko                 → vipākaḥ
'vyākṛto               → avyākṛtaḥ
dharmaḥ                → dharmaḥ
sattvākhyo             → sattva-ākhyaḥ
vyākṛtodbhavaḥ         → vyākṛta-udbhavaḥ
niḥṣyando              → niḥṣyandaḥ
hetusadṛśo             → hetu-sadṛśaḥ
visaṃyogaḥ             → visaṃyogaḥ
kṣayaḥ                 → kṣayaḥ
dhiyā                  → dhiyā
```

| Form | Morphology | Lexical force here |
|---|---|---|
| vipākaḥ | nominative masculine singular | maturation-result |
| avyākṛtaḥ dharmaḥ | nominative masculine singular phrase | an indeterminate dharma |
| sattva-ākhyaḥ | nominative masculine singular compound | designated as associated with a sentient continuum |
| vyākṛta-udbhavaḥ | nominative masculine singular compound | arisen from what is morally determinate |
| niḥṣyandaḥ | nominative masculine singular | homogeneous-outflow result |
| hetu-sadṛśaḥ | nominative masculine singular compound | similar to its cause |
| visaṃyogaḥ | nominative masculine singular | disconnection |
| kṣayaḥ | nominative masculine singular | destruction / exhaustion |
| dhiyā | instrumental feminine singular of `dhī` | through insight or discriminative knowing |

`Vyākṛta` and `avyākṛta` are technical ethical classifications here. The
former denotes wholesome or unwholesome cause determinable with respect to
maturation; the latter denotes the neutral status of the matured result.

## 4. Grammar

The first half gives three cumulative predicates of `vipākaḥ`:

```text
vipākaḥ
    → avyākṛtaḥ dharmaḥ
    → sattva-ākhyaḥ
    → vyākṛta-udbhavaḥ

maturation-result
    → an indeterminate dharma
    → associated with a sentient continuum
    → arisen from what is morally determinate
```

No one predicate is sufficient by itself. The Bhāṣya adds temporal distance
and non-common appropriation to distinguish maturation from nourishment,
homogeneous continuation, and shared karmic environments.

The second half contains two nominal definitions:

```text
niḥṣyandaḥ
    → hetu-sadṛśaḥ

homogeneous outflow
    → similar to its cause

visaṃyogaḥ
    → dhiyā kṣayaḥ

disconnection
    → destruction through discriminative knowing
```

The instrumental `dhiyā` identifies the means through which destruction is
effected; it does not make `dhī` the substance destroyed.

## 5. Translation

### Close syntactic construe

> Maturation is an indeterminate dharma, designated as associated with a sentient continuum, and arisen from what is morally determinate. Homogeneous outflow is similar to its cause. Disconnection is destruction through insight.

### Bhāṣya-informed translation

> A maturation-result is an unobscured-indeterminate dharma arising later from wholesome or unwholesome karma and belonging non-commonly to one sentient continuum. A homogeneous-outflow result resembles its cause in the respects appropriate to homogeneous or pervasive causality. Disconnection is analytical cessation—the exhaustion of the afflictive bond through discriminative wisdom.

## 6. Philosophical Translation

> Results disclose their grounds in different forms. Maturation preserves causal law while changing ethical and manifest form; homogeneous outflow preserves relevant likeness; disconnection manifests the efficacy of knowing as the exhaustion of bondage. The truth of a cause is therefore neither mere repetition nor arbitrary succession, but its determinate mode of manifestation.

```text
maturation:
    determinate cause → transformed neutral individual result

homogeneous outflow:
    cause → relevant similarity in continuation

disconnection:
    discriminative knowing → exhaustion of the bond
```

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this unit |
|---|---|---|
| vipāka | maturation-result | delayed, individually appropriated, unobscured-indeterminate result of determinate karma |
| avyākṛta | indeterminate | neither wholesome nor unwholesome as a matured result |
| anivṛta-avyākṛta | unobscured-indeterminate | full Bhāṣya specification of maturation's ethical status |
| sattvākhyā | associated with a sentient continuum | belonging to a living series without positing a permanent person |
| vyākṛtodbhava | arisen from what is determinate | generated from wholesome or unwholesome karma |
| asādhāraṇa | non-common / unshared | individually appropriated result not experienced as another's maturation |
| sādhāraṇa-karma | common karma | ground of shared results such as a common environment |
| niḥṣyanda | homogeneous outflow / continuation | result similar to its cause in indexed respects |
| hetu-sadṛśa | similar to its cause | defining relation of homogeneous-outflow fruit |
| bhūmitaḥ sādṛśya | similarity by level | broad similarity sufficient for pervasive causal outflow |
| prakārataḥ sādṛśya | similarity in specific type | stronger similarity characteristic of homogeneous causality |
| visaṃyoga | disconnection | freedom from conjunction with the afflictive bond |
| kṣaya | destruction / exhaustion | cessation of the bond's causal efficacy |
| dhī | insight / discriminative knowing | wisdom through which the afflictive bond is exhausted |
| pratisaṃkhyā-nirodha | analytical cessation | disconnection realized through discriminative wisdom |

`Sattvākhyā` is relational and classificatory. It must not be translated as
though maturation belonged to an eternal self.

`Dhī` is stronger than ordinary recognition. In this causal definition it
names knowing that performs the discriminative work through which the bond is
exhausted.

## 8. Logical Determination

Strict maturation-result is:

```text
VipakaResult(r, c) :=
    UnobscuredIndeterminate(r)
    AND AssociatedWithSentientContinuum(r)
    AND MorallyDeterminate(c)
    AND ArisesFrom(r, c)
    AND TemporallyLaterThan(r, c)
    AND NonCommon(r)
```

This excludes shared karmic products:

```text
ProducedByKarma(r)
AND CommonlyEnjoyable(r)
    → NOT StrictVipakaResult(r)
    → Possibly AdhipatiFruit(r)
```

Individual appropriation is non-transferable:

```text
KarmaOf(agentA, k)
AND VipakaResult(r, k)
    → ExperiencedInContinuum(r, agentA)
    AND NOT MaturationOf(r, agentB's karma)
```

Homogeneous outflow requires indexed resemblance:

```text
NisyandaFruit(r, c)
    → Similar(r, c, similarityProfile)
```

The homogeneous/pervasive relation admits four cases:

| Case | Homogeneous cause | Pervasive cause | Determination |
|---|---:|---:|---|
| 1 | yes | no | same specific type without pervasive status |
| 2 | no | yes | pervasive affliction producing another afflictive class |
| 3 | yes | yes | pervasive and same specific afflictive type |
| 4 | no | no | remaining causal cases |

Disconnection is:

```text
DiscriminativeWisdom(d)
AND Exhausts(d, AfflictiveBond(b))
    → Disconnection(b)
    → AnalyticalCessation(b)
```

Read with VAK 2.55:

```text
Wisdom destroys the bond's causal capacity
    ⇏ Wisdom manufactures an unconditioned object
```

## 9. Interpretive Note

VAK 2.57 supplies result-semantics rather than another list. Each fruit is
identified through a different invariant:

```text
VipakaProfile {
    ethicalStatus: unobscuredIndeterminate,
    provenance: morallyDeterminateKarma,
    scope: oneSentientContinuum,
    temporalRelation: delayed,
    sharing: nonCommon
}

NisyandaProfile {
    similarityDimensions,
    causalType,
    continuation
}

DisconnectionProfile {
    discriminativeOperation,
    exhaustedBond,
    futureNonArising
}
```

This makes the difference between a shared environment and an individual
faculty intelligible. Both may have karmic provenance, but only the latter is
strict maturation when it belongs non-commonly to the relevant continuum.
The classification depends upon causal relation, not surface origin alone.

The `niḥṣyanda` definition confirms that a yield stream requires a similarity
schema. A generator that merely emits subsequent values is too weak an
analogy. The system must specify what is preserved:

```text
same level?
same afflicted status?
same specific type?
```

The strongest determination is `visaṃyogaḥ kṣayo dhiyā`. Earlier we proposed
that Prajñā is not a sensation or a finished Concept but Path-forming
discrimination. This verse gives that reconstruction a Kośa coordinate:

```text
dhī
    → operates discriminatively
    → exhausts the afflictive bond
    → realizes disconnection
```

The kārikā says `dhī`, not `prajñā`, and the comparison must remain
interpretive. Still, it supports the functional claim that discriminative
knowing is understood through what it does along the Path, not merely through
a conceptual image of “wisdom.”

For the Agent, this suggests that Knowledge cannot be represented only as a
stored proposition. A liberative determination carries an operation and its
verified consequence:

```text
KnowledgeRecord {
    discrimination,
    targetBond,
    exhaustionEvidence,
    resultingNonArising
}
```

This remains an Organon reconstruction. The primary Kośa claim is narrower:
disconnection is the destruction effected through wisdom.

The textual layers are:

```text
kārikā
    → defines maturation, homogeneous outflow, and disconnection

Bhāṣya
    → adds delayed and non-common maturation,
      indexed similarity, fourfold causal analysis,
      and analytical cessation

Organon reconstruction
    → models result-semantics and relates dhī
      to Path-forming discrimination
```

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .

vak:VipakaResult a organon:ResultType .
vak:NisyandaResult a organon:ResultType .
vak:DisconnectionResult a organon:LiberativeResultType .

organon:VipakaProfile a organon:OcularResultSchema ;
    organon:requires organon:UnobscuredIndeterminateStatus,
        organon:MorallyDeterminateProvenance,
        organon:SentientContinuumScope,
        organon:TemporalDelay,
        organon:NonCommonAppropriation .

organon:NisyandaProfile a organon:OcularResultSchema ;
    organon:requires organon:SimilarityDimensions,
        organon:CausalType,
        organon:ContinuationProfile .

organon:DisconnectionProfile a organon:OcularResultSchema ;
    organon:requires organon:DiscriminativeOperation,
        organon:ExhaustedBond,
        organon:FutureNonArising .

vak:Dhi a organon:DiscriminativeKnowing .
vak:Dhi organon:exhausts vak:AfflictiveBond .
vak:AfflictiveBond organon:hasResultWhenExhausted vak:DisconnectionResult .

organon:hasSimilarityDimension a organon:ObjectProperty .
organon:belongsToContinuum a organon:ObjectProperty .
organon:hasAppropriationScope a organon:ObjectProperty .
organon:exhausts a organon:ObjectProperty .
```
