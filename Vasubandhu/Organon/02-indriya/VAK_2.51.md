# VAK_2.51

## 1. Sanskrit (Devanāgarī)

> चैत्ता द्वौ संवरौ तेषां चेतसो लक्षणानि च ।
>
> चित्तानुवर्तिनः कालफलादिशुभतादिभिः ॥ २.५१ ॥

## 2. Sanskrit (IAST)

> caittā dvau saṃvarau teṣāṃ cetaso lakṣaṇāni ca /
>
> cittānuvartinaḥ kālaphalādiśubhatādibhiḥ // 2.51 //

## 3. Padaccheda

```text
caittā                       → caittāḥ
dvau                         → dvau
saṃvarau                     → saṃvarau
teṣām                        → teṣām
cetasaḥ                      → cetasaḥ
lakṣaṇāni                    → lakṣaṇāni
ca                           → ca
cittānuvartinaḥ              → citta-anuvartinaḥ
kālaphalādiśubhatādibhiḥ     → kāla-phala-ādi-śubhatā-ādibhiḥ
```

| Form | Morphology | Lexical force here |
|---|---|---|
| caittāḥ | nominative masculine plural | mental factors associated with citta |
| dvau saṃvarau | nominative masculine dual | the two restraints |
| teṣām | genitive plural pronoun | belonging to those [mental factors and restraints] |
| cetasaḥ | genitive neuter singular | belonging to citta |
| lakṣaṇāni | nominative neuter plural | conditioned marks |
| ca | conjunction | and |
| citta-anuvartinaḥ | nominative plural compound | followers of citta |
| kāla-phala-ādi | instrumental compound | by time, result, and the remaining relevant correspondences |
| śubhatā-ādibhiḥ | instrumental plural | by wholesomeness and the other ethical qualities |

`Caittāḥ` becomes `caittā` before the following voiced consonant. `Teṣāṃ
cetasaḥ` gives two genitive dependents of `lakṣaṇāni`: the marks belonging to
those accompanying dharmas and the marks belonging to citta.

## 4. Grammar

The first half supplies the subjects of the final predicate:

```text
caittāḥ
dvau saṃvarau
teṣāṃ cetasaḥ ca lakṣaṇāni
    → cittānuvartinaḥ

mental factors,
the two restraints,
and their marks together with citta's marks
    → are followers of citta
```

The instrumental compounds state the respects in which they follow:

```text
kāla-phala-ādibhiḥ
śubhatā-ādibhiḥ
    → through correspondence in time, result, and so forth,
      and in wholesomeness and the remaining ethical qualities
```

The Bhāṣya expands the compressed `ādi` expressions into ten conditions:

```text
temporal profile:
    one arising
    one duration
    one cessation
    one temporal period

causal-result profile:
    one result
    one maturation-result
    one homogeneous outflow

ethical profile:
    wholesome together
    unwholesome together
    indeterminate together
```

Here “one” is glossed as “together with,” not as numerical identity of a
separately existing result-object.

## 5. Translation

### Close syntactic construe

> The mental factors, the two restraints, and the conditioned marks belonging to them and to citta are followers of citta through time, result, and the rest, and through wholesomeness and the other ethical qualities.

### Bhāṣya-informed translation

> Citta-followers comprise all mental factors associated with citta, the restraint of concentration and the uncontaminated restraint, and the conditioned marks belonging to these and to citta. They form one coordinated event-profile with citta by arising, enduring, and ceasing together in the same temporal period; by participating together in result, maturation, and homogeneous continuation; and by sharing its wholesome, unwholesome, or indeterminate quality.

## 6. Philosophical Translation

> A Citta-event is not an isolated point accompanied by accidental attributes. It is an internally coordinated occurrence whose members share a temporal genesis, causal consequences, continuity, and ethical determination. Membership in that occurrence is established by invariants across the whole profile, not by bare simultaneity.

Thus:

```text
co-presence
    + shared temporal profile
    + shared result profile
    + shared ethical profile
    = citta-followership
```

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this unit |
|---|---|---|
| caitta | mental factor | conditioned mental operation associated with citta |
| cittānuvartin | follower of citta | dharma conforming to citta through the ten shared conditions |
| dhyāna-saṃvara | restraint of concentration | first restraint specified by the Bhāṣya |
| anāsrava-saṃvara | uncontaminated restraint | second restraint specified by the Bhāṣya |
| lakṣaṇa | conditioned mark | birth, duration, aging, and impermanence belonging to citta or its followers |
| ekotpāda-sthiti-nirodhatā | one arising, duration, and cessation | shared lifecycle of the coordinated occurrence |
| ekādhva-patitatva | falling within one temporal period | common location in the past, present, or future phase |
| phala | result | consequence in which citta and follower participate together |
| vipāka | maturation-result | karmically matured result shared within the profile |
| niḥṣyanda | homogeneous outflow | continuation in kind shared by citta and its follower |
| śubhatā | wholesomeness | first member of the shared ethical classification |
| satkāya-dṛṣṭi | view of a real personality | example used in the Bhāṣya's textual proof about causal scope |

`Anuvartin` does not mean merely “occurring afterward.” The follower conforms
to and accompanies citta through a common indexed structure.

`Niḥṣyanda` should remain distinct from `āsrava`. The former is homogeneous
causal continuation; the latter concerns contaminating outflow. English
“outflow” does not erase the Sanskrit distinction.

## 8. Logical Determination

The ten-condition predicate is:

```text
CittaFollower(x, c) :=
    SameArising(x, c)
    AND SameDuration(x, c)
    AND SameCessation(x, c)
    AND SameTemporalPeriod(x, c)
    AND SharedResult(x, c)
    AND SharedMaturation(x, c)
    AND SharedHomogeneousOutflow(x, c)
    AND EthicalConcordance(x, c)
```

Ethical concordance expands by the current value of citta:

```text
Wholesome(c)     → Wholesome(x)
Unwholesome(c)   → Unwholesome(x)
Indeterminate(c) → Indeterminate(x)
```

The smallest citta-complex is counted as follows in the Bhāṣya:

```text
10 universal mental factors
+ 40 marks belonging to those factors
+ 8 own-marks and secondary marks
= 58 dharmas for which citta is co-arisen cause
```

In the reverse direction:

```text
58
- 4 secondary marks belonging to citta itself
= 54 dharmas that are co-arisen causes of citta
```

An alternative count accepts only fourteen causes of citta:

```text
10 universal mental factors
+ 4 primary marks of citta
= 14
```

The Kāśmīra Vaibhāṣika rejects that narrower count by appeal to the
`Prakaraṇagrantha`; the rejection is an attributed scholastic determination,
not wording found in the kārikā.

The inclusion relations remain asymmetric:

```text
SahabhuHetu(x, y)
    → CoArisen(x, y)

CoArisen(x, y)
    ⇏ SahabhuHetu(x, y)
```

Excluded counterexamples include secondary marks, certain derived material
forms, and acquisitions that may precede or follow the acquired dharma. They
fail the complete shared-result profile.

## 9. Interpretive Note

VAK 2.51 turns `cittānuvartin` into a strict membership protocol. A factor
does not belong internally to a Citta-event merely because it appears nearby
or bears a mental label. It must share the event's genesis, temporal phase,
causal consequences, homogeneous continuation, and ethical quality.

This is stronger than event-coordination metadata. It is an Ocular Schema for
the event's internal causal unity:

```text
CittaEvent {
    members,
    temporalProfile,
    resultProfile,
    continuationProfile,
    ethicalProfile,
    directionalCausalEdges
}
```

The asymmetry between fifty-eight and fifty-four shows why the final field is
necessary. Membership in one occurrence does not entail that every causal
edge is reciprocal. The schema must represent both the enclosure and the
direction of efficacy.

The Python generator analogy illuminates `niḥṣyanda` at the project level:

```python
def homogeneous_series(state):
    while state.is_conditioned:
        yield state.next_of_same_causal_kind()
```

`yield` preserves suspended state and produces a sequence rather than one
completed collection. Similarly, homogeneous outflow identifies a
continuation in kind across a causal series. But the analogy has limits:
`niḥṣyanda` is a doctrinal result-type, not executable control flow, and it
must not be confused with contaminating `āsrava`.

The passage also clarifies how Citta can be a Chakra without becoming a
simple substance. Its unity is the coordinated turning of determinations
through shared temporal, causal, and ethical profiles. The Kośa makes that
conditioned structure exact; any Yoga account of Buddhi, Ahaṃkāra, and Manas
must be related to it later rather than inserted into the primary analysis.

The textual layers are:

```text
kārikā
    → names the followers and their shared profiles

Bhāṣya
    → specifies the two restraints, ten conditions,
      numerical causal complex, exclusions, and school dispute

Organon reconstruction
    → models followership as typed event membership
      and compares homogeneous continuation to a yield stream
```

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .

vak:CittaFollower a organon:ConditionedDetermination .
vak:MentalFactor a vak:CittaFollower .
vak:ConcentrationRestraint a vak:CittaFollower .
vak:UncontaminatedRestraint a vak:CittaFollower .
vak:ConditionedMarkOfCittaComplex a vak:CittaFollower .

organon:CittaEventProfile a organon:OcularSchema ;
    organon:requires organon:TemporalProfile,
        organon:ResultProfile,
        organon:ContinuationProfile,
        organon:EthicalProfile,
        organon:DirectionalCausalEdge .

organon:sharesArisingWith a organon:SymmetricProperty .
organon:sharesDurationWith a organon:SymmetricProperty .
organon:sharesCessationWith a organon:SymmetricProperty .
organon:sharesTemporalPeriodWith a organon:SymmetricProperty .
organon:sharesResultWith a organon:SymmetricProperty .
organon:sharesMaturationWith a organon:SymmetricProperty .
organon:sharesHomogeneousOutflowWith a organon:SymmetricProperty .
organon:sharesEthicalQualityWith a organon:SymmetricProperty .

vak:CittaFollower organon:follows vak:Citta ;
    organon:belongsTo organon:CittaEventProfile .

vak:HomogeneousOutflow a organon:ContinuationType ;
    organon:projectAnalogy organon:StatefulYieldStream .

organon:CoArisen organon:isBroaderThan vak:SahabhuHetu .
```
