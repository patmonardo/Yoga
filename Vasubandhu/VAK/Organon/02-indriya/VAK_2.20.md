# VAK_2.20

## 1. Sanskrit (Devanāgarī)

> सर्वाल्पैर्निःशुभोऽष्टाभिर्विन्मनःकायजीवितैः ।
>
> युक्तो बालस्तथारूप्ये उपेक्षायुर्मनःशुभैः ॥ २.२० ॥

## 2. Sanskrit (IAST)

> sarvālpair niḥśubho 'ṣṭābhir vinmanaḥkāyajīvitaiḥ /
>
> yukto bālas tathārūpye upekṣāyurmanaḥśubhaiḥ // 2.20 //

The surface form `vin-` is resolved by the Bhāṣya as `vit`, a collective
designation for feeling or experiencing. It denotes all five feeling
faculties here, not one additional faculty named “vit.”

## 3. Padaccheda

```text
sarvālpair           → sarva-alpaiḥ
niḥśubho             → niḥ-śubhaḥ
aṣṭābhir             → aṣṭābhiḥ
vinmanaḥkāyajīvitaiḥ → vit-manas-kāya-jīvitaiḥ
yukto                → yuktaḥ
bālas                → bālaḥ
tathā                → tathā
ārūpye               → ārūpye
upekṣāyurmanaḥśubhaiḥ
                     → upekṣā-āyus-manas-śubhaiḥ
```

| Form | Morphology | Lexical force here |
|---|---|---|
| sarva-alpaiḥ | instrumental plural superlative expression | with the fewest of all |
| niḥ-śubhaḥ | nominative masculine singular | one without wholesome faculties |
| aṣṭābhiḥ | instrumental plural numeral | with eight faculties |
| vit | compound member, lexically explained by the Bhāṣya | feeling or experiencing; collectively, the five feelings |
| manas | compound member | mind faculty |
| kāya | compound member | body faculty |
| jīvita | compound member | life faculty |
| yuktaḥ | nominative masculine singular | endowed with / conjoined with |
| bālaḥ | nominative masculine singular | ordinary person, as defined by the Bhāṣya |
| tathā | indeclinable | likewise |
| ārūpye | locative singular | in the formless realm |
| upekṣā | compound member | neutral-feeling faculty |
| āyus | compound member | life faculty |
| śubha | compound member | wholesome faculties; narrowed by the Bhāṣya to the five beginning with confidence |

## 4. Grammar

The first clause answers the question “who possesses the fewest faculties?”

```text
niḥśubhaḥ bālaḥ
    → an ordinary person without wholesome faculties

sarva-alpaiḥ aṣṭābhiḥ ... yuktaḥ
    → is endowed with the fewest of all: eight

vit-manas-kāya-jīvitaiḥ
    → with the feelings, mind, body, and life
```

The Bhāṣya expands `vit` into the five feeling faculties, making the count:

```text
5 feelings + mind + body + life = 8
```

The second clause coordinates a parallel minimum:

```text
tathā ārūpye bālaḥ
    → likewise, an ordinary person in the formless realm

upekṣā-āyus-manas-śubhaiḥ [yuktaḥ]
    → is endowed with neutral feeling, life, mind,
      and the wholesome faculties
```

Here `yuktaḥ` is understood from the first clause. The Bhāṣya constrains
`śubha` by both the total count and the ordinary status of the subject: it
means the five faculties beginning with confidence, not the three
uncontaminated realization faculties.

## 5. Translation

### Close syntactic construe

> An ordinary person without wholesome faculties is endowed with the fewest of all—with eight: the feelings, mind, body, and life. Likewise, in the formless realm, [an ordinary person is endowed] with neutral feeling, life, mind, and the wholesome faculties.

### Bhāṣya-informed translation

> The minimum number of possessed faculties is eight. One whose wholesome roots have been severed possesses the five feelings together with body, mind, and life. An ordinary person in the formless realm also possesses eight: neutral feeling, life, mind, and the five wholesome faculties beginning with confidence.

The two configurations share only neutral feeling, life, and mind. Their equal
cardinality does not indicate identical composition or ethical-path status.

## 6. Philosophical Translation

> The smallest possible faculty-total is not one uniform minimum essence. One eightfold continuum retains embodiment and the complete feeling range while lacking wholesome roots. Another lacks material faculties and four feelings while retaining the five wholesome powers of cultivation. Numerical identity therefore conceals qualitative and structural opposition.

Organon rendering:

> A minimum viable Agent cannot be specified by cardinality alone. The same resource count can realize different architectures: an embodied affective survival profile without wholesome direction, or a formless cognitive-practical profile organized by the five path faculties. Type and relation determine the system, not quantity.

“Minimum viable Agent,” “resource count,” and “architecture” are Organon
reconstructions. The Kārikā and Bhāṣya classify minimum faculty-possession in
two doctrinally specified continuums.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| sarvālpa | fewest of all | global minimum faculty-count, here eight |
| niḥśubha | without wholesome faculties | defined by the Bhāṣya as one whose wholesome roots are severed |
| samucchinna-kuśala-mūla | one whose wholesome roots are completely severed | Bhāṣya determination of the first minimum case |
| vit | feeling / experiencing | collective expression for all five feeling faculties |
| vedayate | experiences | verbal explanation offered by the Bhāṣya for `vit` |
| bāla | ordinary person | defined here as `pṛthagjana`, excluding a noble person |
| pṛthagjana | ordinary person | Bhāṣya gloss fixing the subject-status of the formless case |
| ārūpya | formless realm | setting of the second minimum configuration |
| śubha-indriya | wholesome faculties | in this count, the five beginning with confidence |
| śraddhādi-pañcaka | five beginning with confidence | confidence, energy, mindfulness, concentration, and discernment |

The Bhāṣya explicitly rejects including the three realization faculties under
`śubha`: the subject is an ordinary person, and the stated total is eight.

## 8. Logical Determination

The minimum cardinality is:

```text
ForEvery valid living FacultyConfiguration c:
    Count(c) ≥ 8
```

The first witness of that minimum is:

```text
FiveFeelings
    = {Pleasure, Pain, Gladness, Distress, NeutralFeeling}

SeveredWholesomeRootsMinimum
    = FiveFeelings ∪ {Body, Mind, Life}

Count = 8
WholesomePathFive ∩ Configuration = ∅
```

The second witness is:

```text
WholesomePathFive
    = {Confidence, Energy, Mindfulness,
       Concentration, Discernment}

FormlessOrdinaryMinimum
    = {NeutralFeeling, Life, Mind} ∪ WholesomePathFive

Count = 8
MaterialFaculties ∩ Configuration = ∅
```

Therefore:

```text
Count(SeveredWholesomeRootsMinimum)
    = Count(FormlessOrdinaryMinimum)

SeveredWholesomeRootsMinimum
    ≠ FormlessOrdinaryMinimum
```

The shared invariant is exactly the triad from VAK 2.17:

```text
Intersection(
    SeveredWholesomeRootsMinimum,
    FormlessOrdinaryMinimum)
        = {NeutralFeeling, Life, Mind}
```

## 9. Interpretive Note

VAK 2.20 changes the question from the closure generated by a selected
faculty to the lower bound of the entire possession-system. Eight is the
minimum, but the verse immediately prevents us from treating that number as
a sufficient model.

The first configuration belongs to a person whose wholesome roots have been
severed. `Niḥśubha` does not mean absence of all functioning or all affect.
That continuum still possesses body, life, mind, and the complete fivefold
feeling range. What is absent is wholesome path-capacity.

The second configuration is almost an inversion. The formless ordinary
person lacks body and sensory faculties and possesses only neutral feeling,
yet retains confidence, energy, mindfulness, concentration, and discernment.
These are wholesome but contaminated faculties available to an ordinary
person; they are not the uncontaminated realization faculties of a noble
path-stage.

The two minima demonstrate why a karmic ISA cannot compile a state from a
count alone:

```text
FacultyCount
    = coarse invariant

FacultyConfiguration
    = typed members
    + relations
    + realm
    + ethical condition
    + path status
```

The common core of the opposed configurations is neutral feeling, life, and
mind. Around that invariant triad, embodiment and affect can form one kind of
continuum, while wholesome cultivation capacities can form another. The
Kośa Agent therefore needs structural typing and provenance, not merely an
array length or a scalar measure of power.

This is also a warning against interpreting “more faculties” as “better
Agent.” The minimum formless profile has the same number as the profile whose
wholesome roots are severed, yet their practical determination is opposed.
Rational-moral evaluation must inspect the configuration and its direction,
not maximize the count.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_20
    a vak:Karika ;
    rdfs:label "VAK 2.20" ;
    vak:hasTopic vak:MinimumFacultyConfiguration ;
    vak:belongsTo vak:Indriyanirdesa .

vak:SeveredWholesomeRootsMinimum
    a vak:FacultyConfiguration ;
    vak:hasFaculty vak:FiveFeelingFaculties,
        vak:BodyFaculty,
        vak:MindFaculty,
        vak:LifeFaculty ;
    vak:hasCount 8 ;
    vak:excludes vak:FiveBeginningWithConfidence .

vak:FormlessOrdinaryMinimum
    a vak:FacultyConfiguration ;
    vak:hasFaculty vak:NeutralFeelingFaculty,
        vak:LifeFaculty,
        vak:MindFaculty,
        vak:FiveBeginningWithConfidence ;
    vak:hasCount 8 ;
    vak:hasRealm vak:FormlessRealm ;
    vak:hasSubjectStatus vak:OrdinaryPerson .

vak:MinimumFacultyConfiguration
    vak:hasLowerBound 8 ;
    vak:hasWitness vak:SeveredWholesomeRootsMinimum,
        vak:FormlessOrdinaryMinimum .

organon:StructuralStateTyping
    a organon:InterpretiveReconstruction ;
    organon:rejects organon:CountOnlyRepresentation ;
    organon:requires organon:TypedFacultyMembership,
        organon:RealmContext,
        organon:EthicalCondition,
        organon:PathStatus ;
    organon:inferredFrom vak:MinimumFacultyConfiguration .
```
