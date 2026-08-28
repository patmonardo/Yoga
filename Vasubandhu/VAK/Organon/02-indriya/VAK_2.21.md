# VAK_2.21

## 1. Sanskrit (Devanāgarī)

> बहुभिर्युक्त एकान्नविंशत्यामलवर्जितैः ।
>
> द्विलिङ्ग आर्यो रागी एकलिङ्गद्वयामलवर्जितैः ॥ २.२१ ॥

## 2. Sanskrit (IAST)

> bahubhir yukta ekānnaviṃśatyāmalavarjitaiḥ /
>
> dviliṅga āryo rāgī ekaliṅgadvayāmalavarjitaiḥ // 2.21 //

The Bhāṣya divides the compressed syntax into two cases. `Dviliṅga` completes
the first case; it does not qualify `ārya`. The second case begins with
`āryo rāgī`, a noble trainee who still possesses attachment.

## 3. Padaccheda

```text
bahubhir             → bahubhiḥ
yukta                → yuktaḥ
ekānnaviṃśatyāmalavarjitaiḥ
                     → ekānna-viṃśatyā amala-varjitaiḥ
dviliṅga             → dvi-liṅgaḥ
āryo                 → āryaḥ
rāgī                 → rāgin
ekaliṅgadvayāmalavarjitaiḥ
                     → eka-liṅga-dvaya-amala-varjitaiḥ
```

| Form | Morphology | Lexical force here |
|---|---|---|
| bahubhiḥ | instrumental plural | with many; interpreted by the Bhāṣya as the greatest number |
| yuktaḥ | nominative masculine singular | endowed with |
| ekānna-viṃśatyā | instrumental singular numeral | with one less than twenty, nineteen |
| amala-varjitaiḥ | instrumental plural compound | with the stainless faculties excluded |
| dvi-liṅgaḥ | nominative masculine singular | possessing both sexual faculties |
| āryaḥ | nominative masculine singular | noble person |
| rāgin | nominative masculine singular | possessing attachment |
| eka-liṅga-dvaya-amala-varjitaiḥ | instrumental plural compound | with one sexual faculty and two stainless faculties excluded |

`Amala`, “stainless,” is determined by the Bhāṣya as the three
uncontaminated realization faculties. The second compound expresses two
exclusion counts: one of the two sexual faculties and two of the three
stainless faculties.

## 4. Grammar

The first nineteenfold case is:

```text
bahubhiḥ yuktaḥ ekānna-viṃśatyā
    → one endowed with the greatest number is endowed with 19

amala-varjitaiḥ dvi-liṅgaḥ
    → a person possessing both sexual faculties,
      with the stainless faculties excluded
```

The Bhāṣya supplies `samagrendriya`, “possessing complete faculties,” as a
qualification of this first subject.

The second case carries forward the same predicate and count by ellipsis:

```text
āryaḥ rāgī [ekānna-viṃśatyā yuktaḥ]
    → a noble person still possessing attachment
      [is endowed with 19]

eka-liṅga-dvaya-amala-varjitaiḥ
    → with one sexual faculty and two stainless faculties excluded
```

The Bhāṣya specifies the second subject as an `avītarāga śaikṣa`, a trainee
not yet free from attachment. Only the uncontaminated faculty appropriate to
the trainee's present path-state is possessed; the other two are excluded.

## 5. Translation

### Close syntactic construe

> One endowed with the greatest number is endowed with nineteen, the stainless faculties being excluded—a person possessing both sexual faculties. A noble person who still possesses attachment [also has nineteen], with one sexual faculty and two stainless faculties excluded.

### Bhāṣya-informed translation

> Two different persons may possess the maximum of nineteen faculties. A person possessing both sexual faculties and otherwise complete faculties has all except the three uncontaminated realization faculties. A noble trainee who is not yet free from attachment has only one sexual faculty and only the one uncontaminated realization faculty appropriate to the present path-stage, excluding the other sexual faculty and the other two uncontaminated faculties.

The two cases have the same count because each excludes three from the total
twenty-two, but the excluded members are different.

## 6. Philosophical Translation

> Maximum numerical possession does not identify one kind of subject. A fully equipped worldly continuum reaches nineteen by lacking every uncontaminated realization faculty. A noble trainee reaches nineteen by possessing one such faculty while excluding one sexual faculty and the two realization faculties incompatible with the present stage. Equal extension thus embodies opposed determinations.

Organon rendering:

> The configuration space has two maximal states with the same cardinality but different governing forms. One maximizes conditioned equipment while lacking realization; the other is path-organized and excludes features incompatible with its developmental state. System identity belongs to typed inclusion and exclusion, not feature count.

“Configuration space,” “maximal state,” and “system identity” are Organon
reconstructions. The textual analysis concerns the two greatest
faculty-possession profiles.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| bahubhiḥ samanvāgata | endowed with the greatest number | Bhāṣya formulation of the maximum-possession question |
| ekānna-viṃśati | one less than twenty | nineteen, the maximum co-possession count here |
| amala-indriya | stainless faculty | one of the three uncontaminated realization faculties |
| dvi-liṅga | possessing both sexual faculties | qualification of the first, worldly maximum |
| samagra-indriya | possessing complete faculties | Bhāṣya qualification of the first case |
| ārya | noble person | subject of the second maximum |
| rāgin | possessing attachment | marks that the noble trainee is not yet free from attachment |
| avītarāga | not free from attachment | Bhāṣya specification of `rāgin` |
| śaikṣa | trainee | noble path-status of the second subject |
| eka-liṅga | one sexual faculty | one exclusion from the noble configuration |

The Bhāṣya's closing sentence says that the extended examination of faculty
properties, introduced incidentally from their division by realms, is now
complete. This closes the present configuration analysis, not the entire
Indriya chapter.

## 8. Logical Determination

Let the complete inventory be:

```text
AllFaculties = 22 typed faculties
StainlessThree
    = {IShallKnow, Knowledge, OneWhoHasKnown}
SexualTwo
    = {Female, Male}
```

The worldly maximum is:

```text
WorldlyMaximum
    = AllFaculties − StainlessThree

Count(WorldlyMaximum) = 22 − 3 = 19
```

The noble trainee maximum is stage-relative:

```text
StageAppropriateStainlessFaculty ∈ StainlessThree

NobleTraineeMaximum
    = AllFaculties
      − {one member of SexualTwo}
      − {two stage-inappropriate members of StainlessThree}

Count(NobleTraineeMaximum) = 22 − 1 − 2 = 19
```

Therefore:

```text
Count(WorldlyMaximum)
    = Count(NobleTraineeMaximum)
    = 19

WorldlyMaximum
    ≠ NobleTraineeMaximum
```

Their realization status is opposed:

```text
WorldlyMaximum ∩ StainlessThree = ∅

Count(NobleTraineeMaximum ∩ StainlessThree) = 1
```

## 9. Interpretive Note

VAK 2.21 reaches the upper bound of the possession analysis, but it refuses
to turn that bound into a hierarchy of worth. Nineteen is the greatest number
of faculties one person can possess, yet the number is realized through two
different exclusion programs.

The first subject is worldly, possesses both sexual faculties, and is
otherwise complete. This person reaches nineteen precisely by lacking all
three uncontaminated realization faculties. Numerical abundance therefore
coexists with the complete absence of noble realization.

The second subject is a noble trainee who still has attachment. This person
possesses one sexual faculty and the one uncontaminated faculty appropriate
to the current path-stage. One sexual faculty and the other two
uncontaminated faculties are excluded. The exclusions are not deficiencies
measured against the first case; they express compatibility with a
determinate path-state.

The karmic ISA has thus become an exclusion-sensitive type system:

```text
ValidConfiguration
    = IncludedFaculties
    + RequiredDependencies
    + ExcludedIncompatibilities
    + PathStage
```

Two configurations can have identical size while differing in every feature
that matters for realization. The Agent must therefore validate negative
constraints as rigorously as positive possession. An invalid faculty for a
given stage cannot be made acceptable by preserving the correct count.

This also sharpens the Rational Moral Agent. “Maximum capability” is not the
telos. A worldly continuum may maximize conditioned differentiation while
lacking realization altogether. Rational-moral form lies in the correct
organization, purification, and stage-appropriate limitation of capacities.

The Bhāṣya closes the extended faculty-property inquiry here. The sequence
from necessary triad through minimum and maximum configurations has generated
a typed state space governed by implication, mutual exclusion, realm,
ethical condition, and path-stage.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_21
    a vak:Karika ;
    rdfs:label "VAK 2.21" ;
    vak:hasTopic vak:MaximumFacultyConfiguration ;
    vak:belongsTo vak:Indriyanirdesa ;
    vak:closes vak:ExtendedFacultyPropertyAnalysis .

vak:WorldlyMaximum
    a vak:FacultyConfiguration ;
    vak:hasCount 19 ;
    vak:hasSexualFacultyCount 2 ;
    vak:excludes vak:ThreeStainlessFaculties .

vak:NobleTraineeMaximum
    a vak:FacultyConfiguration ;
    vak:hasCount 19 ;
    vak:hasSexualFacultyCount 1 ;
    vak:hasStainlessFacultyCount 1 ;
    vak:excludes vak:OneSexualFaculty,
        vak:TwoStageInappropriateStainlessFaculties ;
    vak:hasPathStatus vak:TraineeNotFreeFromAttachment .

organon:ExclusionSensitiveStateType
    a organon:InterpretiveReconstruction ;
    organon:requires organon:IncludedCapabilities,
        organon:RequiredDependencies,
        organon:ExcludedIncompatibilities,
        organon:PathStage ;
    organon:rejects organon:CardinalityAsIdentity ;
    organon:inferredFrom vak:MaximumFacultyConfiguration .
```
