# VAK_1.19 — Three Commonalities and One Principle

## 1. Sanskrit (Devanāgarī)

> जातिगोचरविज्ञानसामान्यादेकधातुता ।
>
> द्वित्वेऽपि चक्षुरादीनां शोभार्थं तु द्वयोद्भवः ॥ १.१९ ॥

## 2. Sanskrit (IAST)

> jātigocaravijñānasāmānyād ekadhātutā /
>
> dvitve 'pi cakṣurādīnāṃ śobhārthaṃ tu dvayodbhavaḥ // 1.19 //

## 3. Lexical Analysis

```text
jātigocaravijñānasāmānyāt → jāti-gocara-vijñāna-sāmānyāt
ekadhātutā                 → eka-dhātutā
dvitve 'pi                 → dvitve api
cakṣurādīnām               → cakṣus-ādīnām
śobhārtham                 → śobhā-artham
dvayodbhavaḥ               → dvaya-udbhavaḥ
```

| Form | Morphology | Lexical force here |
|---|---|---|
| jāti | feminine noun in compound | shared faculty-kind, as specified by the Bhāṣya |
| gocara | masculine noun in compound | condition-range; the Bhāṣya specifies visible form for the eye |
| vijñāna | neuter noun in compound | corresponding principle |
| sāmānyāt | ablative neuter singular | because of commonality or shared determination |
| eka-dhātutā | nominative feminine singular abstract noun | status of constituting one principle |
| dvitve | locative neuter singular | despite or in the condition of duality |
| api | concessive particle | even though |
| cakṣus-ādīnām | genitive plural | of the eye and the analogous paired faculties |
| śobhā-artham | accusative neuter singular used adverbially | for the sake of beauty or symmetry |
| tu | contrastive particle | however; changes from classification to paired embodiment |
| dvaya-udbhavaḥ | nominative masculine singular | arising or occurrence as a pair |

The Bhāṣya restricts `cakṣus-ādīni` here to the paired eye, ear, and nose
faculties. Tongue and body do not generate the proposed increase from
eighteen to twenty-one principles.

## 4. Grammar

The first line gives an ablative cause:

```text
jāti-gocara-vijñāna-sāmānyāt
    because of commonality of
        kind,
        condition-range,
        and corresponding principle

eka-dhātutā
    there is one-principle status
```

`Dvitve api` is concessive: the bodily faculty occurs in two sites, yet this
numerical duality does not overturn principial unity.

The Bhāṣya distributes the three commonalities for the eye:

```text
two eyes
    share eye-nature                 → base / faculty-kind
    share visible form as condition  → essence / condition-field
    support one eye-principle        → principle / principial relation
```

The Bhāṣya says both are supports of one eye-*vijñāna*. In the project
terminology, this is one eye-principle; the statement does not specify
whether both supports are active in every particular act of seeing.

The same construction is to be applied analogically to the two ears and two
nostril sites. The three grounds must be considered together: shared kind
alone, shared object-field alone, or the principle relation alone is not offered
as the sufficient ground.

`Tu` marks a change of question in the second line. The first line explains
why two bodily sites count as one principle. The second explains why that
one principle has two bodily sites:

```text
classificatory unity
    → base + essence + principle

paired embodiment
    → practical bodily form for beauty
```

The aesthetic explanation is not a fourth criterion of principial unity.

## 5. Translation

### Literal Translation

> Because of commonality of kind, condition-range, and principle, the eye and the others have one-principle status even though dual. Their arising as a pair, however, is for the sake of beauty.

### Bhāṣya-informed study translation

> The two eyes constitute one eye-principle because they share one faculty-kind, take visible form as their condition, and support one eye-principle. The same reasoning applies to the paired ears and nasal faculties. Their bodily occurrence in pairs is said to serve the beauty of the bodily support; it does not multiply the principles.

The second translation distinguishes paired bodily instances from the
principial determination they jointly support. *Skandha* is Base; the
bodily *āśraya* remains a support, not a Base.

## 6. Philosophical Translation

> Two bodily supports can constitute one principle. Their unity is grounded
> in shared faculty-kind, condition-range, and principle-relation, not in
> numerical singleness. Their continued pairing is a separate question:
> the Bhāṣya gives beauty as its reason.

The three commonalities can be read at the project level through Base,
Essence, and Principle. This is a concise philosophical determination, not
a claim that those are lexical translations of *jāti*, *gocara*, and
*vijñāna*.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| jāti | shared faculty-kind | base-side determination common to paired supports |
| gocara | condition-range / field | essence-side determination shared by the paired faculties |
| vijñāna | principle | the shared relation in the Bhāṣya's explanation |
| sāmānya | commonality | shared determination grounding one-principle status |
| jāti-sāmānya | commonality of kind | both bodily sites possess the same faculty-nature |
| gocara-sāmānya | commonality of condition-range | both take the same condition-class |
| vijñāna-sāmānya | commonality of principle | both support one eye-principle |
| eka-dhātutā | one-principle status | principial unity despite numerical embodiment |
| dvitva | duality | occurrence as two bodily sites |
| āśraya | support | bodily faculty-site; distinct from Base (*skandha*) |
| śobhā | beauty / symmetry | stated reason for paired bodily occurrence |
| vairūpya | deformity / asymmetry | result imagined for one-sided embodiment |

## 8. Logical Determination

```text
objection
    eighteen principles
    + second eye + second ear + second nasal site
    → twenty-one

reply
    shared faculty-kind
    + shared condition-range
    + shared principle-relation
    → one principle for each pair

embodiment
    two bodily supports remain
    → beauty explains the pairing, not principial unity

project census
    five Bases; twelve Essences; eighteen Principles
```

## 9. Interpretive Note

The hinge is *sāmānya*: commonality across two supports. The three common
determinations—not bodily number alone—ground one principle. Interpretation
of the three grounds and the separate beauty explanation is in the Bhāṣya.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_19
    a vak:Karika ;
    rdfs:label "VAK 1.19" ;
    vak:hasTopic vak:OnePrincipleStatusAcrossPairedFaculties ;
    vak:belongsTo vak:Dhatunirdesa .

vak:OnePrincipleStatus
    vak:groundedIn vak:CommonFacultyKind , vak:CommonObjectRange ,
        vak:CommonPrincipleRelation ;
    vak:compatibleWith vak:NumericallyMultipleSupports .

vak:PairedEyeSupports
    vak:constitute vak:OneEyePrinciple ;
    vak:share vak:EyeNature , vak:VisibleFormRange ,
        vak:EyePrincipleRelation .

vak:NumericalMultiplicity
    vak:doesNotImply vak:PrincipleMultiplicity .

vak:PairedEmbodiment
    vak:hasStatedPurpose vak:BodilyBeauty ;
    vak:distinctFrom vak:GroundOfPrincipleUnity .
```
