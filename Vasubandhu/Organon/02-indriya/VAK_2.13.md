# VAK_2.13

## 1. Sanskrit (Devanāgarī)

> मनोवित्तित्रयं त्रेधा द्विहेया दुर्मनस्कता ।
>
> नव भावनया पञ्च त्वहेयान्यपि न त्रयम् ॥ २.१३ ॥

## 2. Sanskrit (IAST)

> manovittitrayaṃ tredhā dviheyā durmanaskatā /
>
> nava bhāvanayā pañca tv aheyāny api na trayam // 2.13 //

## 3. Padaccheda

```text
manovittitrayaṃ     → manaḥ-vitti-trayam
tredhā              → tredhā
dviheyā             → dvi-heyā
durmanaskatā        → durmanaskatā
nava                → nava
bhāvanayā           → bhāvanayā
pañca tv            → pañca tu
aheyāny api         → aheyāni api
na trayam           → na trayam
```

| Form | Morphology | Lexical force here |
|---|---|---|
| manas | compound member | mind-faculty |
| vitti-trayam | nominative neuter singular compound | triad of feelings: pleasure, gladness, and neutral feeling |
| tredhā | indeclinable adverb | in three ways |
| dvi-heyā | nominative feminine singular compound | to be abandoned in two ways; agrees with `durmanaskatā` |
| durmanaskatā | nominative feminine singular | distress; equivalent here to `daurmanasya` |
| nava | nominative plural numeral | nine faculties |
| bhāvanayā | instrumental feminine singular | by cultivation |
| pañca | nominative plural numeral | the five beginning with confidence |
| tu | contrastive particle | however |
| aheyāni | nominative neuter plural | not to be abandoned |
| api | additive particle | also |
| na | negation | not |
| trayam | nominative neuter singular | the triad of realization-faculties |

`Manovittitrayam` gathers four faculties, not three: mind together with a
triad of feelings. The Bhāṣya identifies the three feelings as `sukha`,
`saumanasya`, and `upekṣā`.

## 4. Grammar

The opening assigns three possible abandonment-statuses to four faculties:

```text
manaḥ-vitti-trayaṃ tredhā
    → mind and the triad of feelings are threefold
```

The Bhāṣya supplies the three possibilities:

```text
darśana-prahātavya
    → to be abandoned by seeing

bhāvanā-prahātavya
    → to be abandoned by cultivation

aprahātavya / aheya
    → not to be abandoned
```

The next clause concerns distress:

```text
dvi-heyā durmanaskatā
    → distress is to be abandoned in two ways
    → by seeing or by cultivation
```

`Nava bhāvanayā` continues an understood `heyāni`:

```text
nava [heyāni] bhāvanayā
    → nine are [to be abandoned] by cultivation
```

The final clauses distinguish mixed and fixed non-abandonment:

```text
pañca tu aheyāni api
    → the five, however, may also be not abandoned

na trayam
    → the triad is not [to be abandoned]
```

For the five, `api` adds non-abandonment to cultivation-abandonment. For the
triad, the Bhāṣya states that abandonment never applies.

## 5. Translation

### Close syntactic construe

> Mind and the triad of feelings are threefold; distress is to be abandoned in two ways. Nine are [to be abandoned] by cultivation. The five, however, may also be not abandoned; the triad is not [to be abandoned].

### Bhāṣya-informed translation

> Mind, pleasure, gladness, and neutral feeling may be abandoned by seeing, abandoned by cultivation, or not abandoned. Distress may be abandoned by seeing or cultivation. The seven material faculties, life, and pain are abandoned only through cultivation. The five beginning with confidence are abandoned by cultivation when with outflows but are not abandoned when without outflows. The three realization-faculties are never abandoned, because what is faultless is not fit for abandonment.

The Bhāṣya closes the classification with:

```text
na hi nirdoṣaṃ prahāṇārham
    → what is faultless is not fit to be abandoned
```

## 6. Philosophical Translation

> The Path does not act upon faculty-names as undifferentiated wholes. One functional faculty may have an instance removed by seeing, another instance exhausted through cultivation, and an uncontaminated instance that must be preserved. Distress has no faultless remainder, while the five path-equipment faculties divide according to their with-outflow or without-outflow operation. The stainless realization-faculties are not products to be discarded after use; their faultlessness excludes them from abandonment.

Organon rendering:

> VAK 1.48 is the suspended Dhātu map to which this path-classification returns. Abandonment is a typed transformation of qualified Faculty-instances within that map: seeing removes some faults, cultivation exhausts others, and faultless operation is retained. The Agent preserves Faculty identity and Dhātu locus while determining whether a qualified instance is abandoned or carried forward.

This rendering does not identify `prahāṇa` with software deletion. It uses a
technical analogy to preserve the Bhāṣya's instance-sensitive distinctions.

**Transcendental Time determination (Organon, not translation):** Seeing, cultivation, and non-abandonment are different path-relations to a qualified faculty-instance, not a one-size-fits-all chronology of deleting and replacing faculties. Universal Cognition names the operations of seeing and cultivation; the particular Ideas are the faulted or faultless modes to which abandonment applies. A faculty-type may persist through distinct determinations, and non-abandonability does not imply that every event persists uninterruptedly.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| darśana-prahātavya | to be abandoned by seeing | removed through direct seeing of truth |
| bhāvanā-prahātavya | to be abandoned by cultivation | removed through sustained development after seeing |
| aprahātavya / aheya | not to be abandoned | faultless or without-outflow operation preserved by the Path |
| heya | to be abandoned | fit to be relinquished under a specified path-operation |
| prahāṇa | abandonment | path-removal of a faulted determination or mode |
| vitti-traya | triad of feelings | pleasure, gladness, and neutral feeling |
| durmanaskatā / daurmanasya | distress | abandonable by seeing or cultivation, never non-abandonable |
| jīvitāṣṭama | group ending with life as the eighth | seven material faculties plus life |
| śraddhādi | those beginning with confidence | cultivation-abandonable when with outflows; non-abandonable when without outflows |
| realization triad | three realization-faculties | exclusively without outflows and therefore never abandoned |
| nirdoṣa | faultless | Bhāṣya ground for non-abandonment |
| prakārabheda | distinction of types | Bhāṣya phrase closing the extended classificatory block |

“Not to be abandoned” marks a technical path-status of faultless faculties;
it does not mean causally inert or exempt from analysis.

## 8. Logical Determination

The abandonment-status domain is:

```text
AbandonmentStatus
    = {BySeeing, ByCultivation, NotAbandoned}
```

The faculty partitions are:

```text
Threefold
    = {Mind,
       Pleasure,
       Gladness,
       NeutralFeeling}

AllowedStatus(Threefold)
    = {BySeeing, ByCultivation, NotAbandoned}
```

```text
TwofoldDistress
    = {Distress}

AllowedStatus(Distress)
    = {BySeeing, ByCultivation}
```

```text
CultivationOnly
    = {SevenMaterialFaculties,
       Life,
       Pain}

RequiredStatus(CultivationOnly)
    = ByCultivation
```

```text
FivePathEquipmentFaculties
    = {Confidence,
       Energy,
       Recollection,
       Concentration,
       Prajna}

Sasrava(x)
    → Status(x, ByCultivation)

Anasrava(x)
    → Status(x, NotAbandoned)
```

```text
ThreeRealizationFaculties
    → RequiredStatus(NotAbandoned)
```

The type-count is exhaustive:

```text
4 + 1 + 9 + 5 + 3 = 22
```

Abandonment applies to qualified instances:

```text
SameFacultyType(x, y)
∧ DifferentOutflowStatus(x, y)
    → MayHaveDifferentAbandonmentStatus(x, y)
```

The governing validity rule is:

```text
Faultless(x)
    → NotFitForAbandonment(x)
```

## 9. Interpretive Note

**Organon time-reading:** The path's temporal work is differentiated by what a mode requires: seeing removes some faults, cultivation addresses others, and faultlessness is preserved. This is not a universal linear biography or an instruction to destroy embodied life; it is a rule for classifying the path-relation of particular instances.

VAK 2.13 completes the long `prakārabheda`, the classification of the
twenty-two faculties by their different modes. Its final axis is explicitly
practical: what is removed by seeing, what requires cultivation, and what is
not to be abandoned?

The threefold status of mind, pleasure, gladness, and neutral feeling shows
again that the Path does not discard a faculty merely because contaminated
instances occur. The same faculty can participate in a view-bound fault, a
residual cultivation-bound condition, or a faultless operation. Its type is
stable while the path-status of its instances differs.

Distress has no non-abandonable mode. VAK 2.10 showed it to be always
productive of maturation; VAK 2.11 showed it always ethically determined;
VAK 2.13 now confirms that every instance belongs to something the Path must
abandon, whether through seeing or cultivation.

The nine cultivation-only faculties make another important distinction.
Seeing truth does not simply erase embodied structure, life-continuity, or
bodily pain. Their conditioned course is exhausted through cultivation. The
Path is therefore not a single cognitive correction applied uniformly to
every layer of the Agent.

The five beginning with confidence divide by outflow-status. Their
with-outflow instances are cultivation-abandonable; their without-outflow
instances are preserved. The three realization-faculties are more decisive:
they are exclusively without outflows and never abandoned. Vasubandhu's
maxim states the rule cleanly: what is faultless is not fit for abandonment.

This gives our layered Object Model a necessary transformation discipline:

```text
for each determination in each natural or spiritual layer,
    preserve its faculty identity
    inspect its qualified mode
    apply the path-operation licensed for that mode

never infer:
    one faulted instance
        → delete the governing faculty itself
```

**Return to Dhātu at its last kārikā.** VAK 1.48's incidence map
returns in exact detail. The seven material Faculties and Life
belong to the cultivation-only group; their Dhātu loci remain the
five internal sensory Domains, a part of Body, and the Essence-
Domain portion. Mind and the three feeling-Faculties named with it
are threefold in path-status; Mind maps across the Citta Domains,
and feelings occupy the Essence-Domain portion. The five beginning
with Confidence and the three realization-Faculties correspond to
the wholesome path group, with the final three only partly placed
in the Essence-Domain. VAK 2.13 does not replace any of these
positions: it returns to the terminal Dhātu map to specify which
qualified instances are abandoned, cultivated, or preserved.

This is the Fichtean return in mind. The negation falls on the
faulted instance, not the Faculty or its Dhātu placement. Conversely,
the non-abandonable status of a faultless operation does not turn
each occurrence into a permanent event. The return reconstructs the
same mapped architecture under the path's distinct operations.

The fivefold natural object and ten Samyama-bhūmis are Yoga–Organon
architecture, not terms in VAK 2.13. The textual contribution is the
three-way abandonment policy that the reconfigured Rational Moral Agent must
be capable of executing across a differentiated field.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_13
    a vak:Karika ;
    rdfs:label "VAK 2.13" ;
    vak:hasTopic vak:AbandonmentStatusPartition ;
    vak:belongsTo vak:Indriyanirdesa .

vak:AbandonmentStatusPartition
    vak:hasStatus vak:BySeeing,
        vak:ByCultivation,
        vak:NotAbandoned ;
    vak:hasTotalCount 22 .

vak:MindPleasureGladnessNeutralFeeling
    vak:allowsStatus vak:BySeeing,
        vak:ByCultivation,
        vak:NotAbandoned ;
    vak:hasCount 4 .

vak:DistressFaculty
    vak:allowsStatus vak:BySeeing,
        vak:ByCultivation ;
    vak:excludesStatus vak:NotAbandoned .

vak:SevenMaterialFacultiesLifeAndPain
    vak:requiresStatus vak:ByCultivation ;
    vak:hasCount 9 .

vak:FivePathEquipmentFaculties
    vak:hasSasravaStatus vak:ByCultivation ;
    vak:hasAnasravaStatus vak:NotAbandoned .

vak:ThreeRealizationFaculties
    vak:requiresStatus vak:NotAbandoned ;
    vak:hasGround vak:Faultless .

organon:TypedTransformationPolicy
    a organon:InterpretiveReconstruction ;
    organon:operatesOn vak:QualifiedFacultyInstance ;
    organon:preserves vak:FacultyIdentity ;
    organon:variesBy vak:AbandonmentStatus ;
    organon:inferredFrom vak:AbandonmentStatusPartition .
```
