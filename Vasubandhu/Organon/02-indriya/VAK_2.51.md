# VAK_2.51

## 1. Sanskrit (Devanāgarī)

> चैत्ता द्वौ संवरौ तेषां चेतसो लक्षणानि च ।
>
> चित्तानुवर्तिनः कालफलादिशुभतादिभिः ॥ २.५१ ॥

## 2. Sanskrit (IAST)

> caittā dvau saṃvarau teṣāṃ cetaso lakṣaṇāni ca /
>
> cittānuvartinaḥ kālaphalādiśubhatādibhiḥ // 2.51 //

The commentary opens with the question at 83.25, cites the kārikā
at 83.26–27, and develops the account through the closing defense
at 85.06–07. VAK 2.52 begins at 85.08 with the homogeneous cause.

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
| caittāḥ | nominative masculine plural | mental factors associated with consciousness |
| dvau saṃvarau | nominative masculine dual | the two restraints |
| teṣām | genitive plural pronoun | belonging to those [mental factors and restraints] |
| cetasaḥ | genitive neuter singular | belonging to consciousness |
| lakṣaṇāni | nominative neuter plural | conditioned marks |
| ca | conjunction | and |
| citta-anuvartinaḥ | nominative plural compound | followers of consciousness |
| kāla-phala-ādi | instrumental compound | by time, result, and the remaining relevant correspondences |
| śubhatā-ādibhiḥ | instrumental plural | by wholesomeness and the other ethical qualities |

`Caittāḥ` becomes `caittā` before the following voiced consonant. `Teṣāṃ
cetasaḥ` gives two genitive dependents of `lakṣaṇāni`: the marks belonging to
those accompanying dharmas and the marks belonging to consciousness.

## 4. Grammar

The first half supplies the subjects of the final predicate:

```text
caittāḥ
dvau saṃvarau
teṣāṃ cetasaḥ ca lakṣaṇāni
    → cittānuvartinaḥ

mental factors,
the two restraints,
and their marks together with consciousness's marks
    → are followers of consciousness
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

> The mental factors, the two restraints, and the conditioned marks belonging to them and to consciousness are followers of consciousness through time, result, and the rest, and through wholesomeness and the other ethical qualities.

### Bhāṣya-informed translation

> Followers of consciousness comprise all mental factors associated with consciousness, the restraint of concentration and the uncontaminated restraint, and the conditioned marks belonging to these and to consciousness. They correspond with consciousness in arising, persisting, and ceasing within the same temporal period; in result, maturation, and homogeneous outflow; and in wholesome, unwholesome, or indeterminate status.

## 6. Limited Organon Reading

This verse specifies how the `citta:caitta` relation is articulated in
the Bhāṣya: the followers are identified by correspondence across ten
respects, not by the word “follower” alone. Within the project's Hub
reading, this dyad is one principial extreme, with `hetu:pratyaya` the
other, organized by the invariant Hub. That architecture is a project-level
synthesis; the commentary here neither names the Hub nor identifies it
as another cause.

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this unit |
|---|---|---|
| caitta | mental factor | conditioned mental operation associated with consciousness |
| cittānuvartin | follower of consciousness | dharma corresponding to consciousness through the ten shared conditions |
| dhyāna-saṃvara | restraint of concentration | first restraint specified by the Bhāṣya |
| anāsrava-saṃvara | uncontaminated restraint | second restraint specified by the Bhāṣya |
| lakṣaṇa | conditioned mark | birth, duration, aging, and impermanence belonging to consciousness or its followers |
| ekotpāda-sthiti-nirodhatā | one arising, duration, and cessation | shared lifecycle of the coordinated occurrence |
| ekādhva-patitatva | falling within one temporal period | common location in the past, present, or future phase |
| phala | result | consequence in which consciousness and follower participate together |
| vipāka | maturation-result | karmically matured result shared within the profile |
| niḥṣyanda | homogeneous outflow | continuation in kind shared by consciousness and its follower |
| śubhatā | wholesomeness | first member of the shared ethical classification |
| satkāya-dṛṣṭi | view of a real personality | example used in the Bhāṣya's textual proof about causal scope |

`Anuvartin` does not mean merely “occurring afterward.” The follower conforms
to and accompanies consciousness through the specified correspondences.

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

Ethical concordance follows the status of consciousness:

```text
Wholesome(c)     → Wholesome(x)
Unwholesome(c)   → Unwholesome(x)
Indeterminate(c) → Indeterminate(x)
```

The smallest consciousness-complex is counted as follows in the Bhāṣya:

```text
10 universal mental factors
+ 40 marks belonging to those factors
+ 8 own-marks and secondary marks
= 58 dharmas for which consciousness is co-arisen cause
```

In the reverse direction:

```text
58
- 4 secondary marks belonging to consciousness itself
= 54 dharmas that are co-arisen causes of consciousness
```

An alternative count accepts only fourteen causes of consciousness:

```text
10 universal mental factors
+ 4 primary marks of consciousness
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

The ten correspondences identify the followers discussed here; they do not
make every relation reciprocal. The counts of fifty-eight and fifty-four,
the excluded co-arisen cases, and the ensuing debate over reciprocal
causation refine the broader definition from VAK 2.50. Keep the Bhāṣya's
account, objections, and closing defense in view before drawing a stronger
Organon conclusion.

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

organon:CoArisen organon:isBroaderThan vak:SahabhuHetu .
```

## 11. Review Status

Provisional paired study of VAK 2.51. The source unit runs from the
question at 83.25 through the closing defense at 85.06–07; VAK 2.52
begins at 85.08. The conventional translation preserves the full
sequence of definitions, counts, objections, and reply.
