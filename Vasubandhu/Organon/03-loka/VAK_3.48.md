# VAK_3.48 — Circumference and the First Mountains

## 1. Sanskrit (Devanāgarī)

```sanskrit
समन्ततस्तु त्रिगुणं तत्र मेरुर्युगन्धरः ।
ईशाधारः खदिरकः सुदर्शनगिरिस्तथा ॥ ३.४८ ॥
```

## 2. Sanskrit (IAST)

```text
samantatas tu triguṇaṃ tatra merur yugandharaḥ /
īśādhāraḥ khadirakaḥ sudarśanagiris tathā // 3.48 //
```

The local Sanskrit witnesses read `īśādhāraḥ`; that form is retained here.
Its relation to the better-known mountain name `Īṣādhara` remains a
philological question for critical-edition review.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| samantataḥ | indeclinable adverb | all around, by the circumference |
| tu | adversative or transitional particle | but; now as to another measure |
| triguṇam | neuter singular, used predicatively | threefold, three times as great |
| tatra | indeclinable | there, upon the golden earth-maṇḍala |
| meruḥ | nominative masculine singular | Meru, clarified by the Bhāṣya as the central mountain |
| yugandharaḥ | nominative masculine singular | first named surrounding mountain |
| īśādhāraḥ | nominative masculine singular | mountain name in the local witness |
| khadirakaḥ | nominative masculine singular | named surrounding mountain |
| sudarśana-giriḥ | nominative masculine singular compound | Mount Sudarśana |
| tathā | indeclinable | likewise, and also |

## 4. Grammar

The opening completes the measurement of 3.47:

```text
[jalakāñcanamaṇḍalam]
    samantataḥ
    tu triguṇam [bhavati]

[the water-and-gold maṇḍala]
    when reckoned all around,
    is threefold
```

The second statement begins a list whose finite verb is understood:

```text
tatra [kāñcanamahīmaṇḍale]
    meruḥ
    yugandharaḥ
    īśādhāraḥ
    khadirakaḥ
    sudarśanagiriḥ tathā
    [santi]
```

“There” is specified by the Bhāṣya as the golden earth-maṇḍala situated above
the waters. The mountain list continues into 3.49; 3.48 alone does not yet
state all eight names.

## 5. Translation

### Literal Translation
> All around, however, it is threefold. There are Meru, Yugandhara, Īśādhāra,
> Khadiraka, and likewise Mount Sudarśana.

### Bhāṣya-informed study translation

> All around, however, the circumference is threefold [the transverse extent].
> There are Meru, Yugandhara, Īśādhāra, Khadiraka, and likewise Sudarśana.

## 6. Philosophical Translation

> The measured support-field now becomes oriented space. Its transverse extent
> is converted into an encircling measure, and within that field a center is
> established together with surrounding structures. Meru is not merely added
> to a list of physical objects: it supplies a middle relative to which the
> remaining mountains acquire ordered positions. The Physical World passes
> from measurable extension to an internally addressed field.

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this unit |
|---|---|---|
| samantataḥ | all around | circumferential rather than transverse reckoning |
| triguṇa | threefold | circumference calculated as three times the transverse measure |
| parikṣepa | circumference / encircling measure | Bhāṣya specification of `samantataḥ` |
| parigaṇyamāna | being reckoned | indicates a measurement operation |
| kāñcanamayī mahī | golden earth | ground upon which the mountains are established |
| pratiṣṭhā | established upon / based upon | support relation of mountains to golden earth |
| Meru / Sumeru | Meru | mountain placed at the middle of the system |
| Yugandhara | Yugandhara | first named surrounding mountain |
| Īśādhāra | Īśādhāra | local witness form of a mountain name; critically unresolved |
| Khadiraka | Khadiraka | named surrounding mountain |
| Sudarśana-giri | Mount Sudarśana | named surrounding mountain |
| madhye | in the middle | Bhāṣya determination of Sumeru's position |
| paricāya-avasthita | positioned around | Bhāṣya determination of the other mountains' relation to Sumeru |

The measurement relation is:

```text
transverse extent        1,203,450 yojanas
circumference            3,610,350 yojanas
relation                 circumference = 3 × transverse extent
```

## 8. Logical Determination

### From transverse measure to circumference

```text
measured breadth
    → circumferential operation
        → encircling measure
```

`Samantataḥ` does not introduce another independent magnitude. The Bhāṣya
reads `triguṇa` as an operation upon the measure already established in 3.47.

### From extension to orientation

```text
extended support-field
    + designated middle
        → oriented spatial field
```

An expanse has breadth without yet possessing a privileged internal address.
With Sumeru in the middle, other positions can be stated relationally as
surrounding it.

### Support and placement

```text
remaining water
    supports golden earth
        supports the mountain system
```

The mountain geography presupposes the generated and dimensioned foundations
of 3.45–3.47. Placement does not replace genesis; it adds internal articulation
to the already produced container.

### Enumeration remains open

```text
3.48 names five mountains
    + 3.49 names three mountains
        → eight great mountains
```

The total of eight is supplied by the Bhāṣya and completed textually only with
3.49. The present study therefore records the forward continuation without
prematurely absorbing the next Kārikā into this one.

## 9. Interpretive Note

**Translation note.** The Bhāṣya takes the threefold measure as circumference:
3,610,350 yojanas. The mountains stand on the golden earth over the waters; Sumeru
is central, with the others arranged around it. The local reading `īśādhāraḥ` is
retained; its relation to the better-known `Īṣādhara` remains a textual question,
not silently resolved. The exact circumferential total, golden-earth location,
eight-mountain scope, and center-surrounding relation are Bhāṣya determinations.

At the project level, the account proceeds from measured extension to circumference, center, and surrounding placement. This relational spatial order needs no symbolic identification of Sumeru with a yogic axis.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .

vak:VAK_3_48
    a vak:Karika ;
    vak:continues vak:ContainerWorldAccount ;
    vak:completesMeasurement loka:WaterGoldMandala ;
    vak:beginsEnumeration loka:GreatMountainSystem .

loka:WaterGoldMandala
    loka:hasTransverseExtentYojanas 1203450 ;
    loka:hasCircumferenceYojanas 3610350 ;
    loka:hasCircumferenceRatio 3 .

loka:GreatMountainSystem
    loka:isEstablishedUpon loka:GoldenEarth ;
    loka:hasCenter loka:Sumeru ;
    loka:hasSurroundingMember loka:Yugandhara,
        loka:Isadhara,
        loka:Khadiraka,
        loka:SudarsanaMountain .

loka:Isadhara
    vak:hasWitnessForm "īśādhāra" ;
    vak:hasPhilologicalStatus vak:Unresolved .

organon:OrientedWorldField
    a organon:ProjectInterpretation ;
    organon:developsFrom organon:MeasuredSupportField ;
    organon:hasRelations organon:Circumference,
        organon:Center,
        organon:SurroundingPosition ;
    organon:enables organon:RelationalAddress .
```
