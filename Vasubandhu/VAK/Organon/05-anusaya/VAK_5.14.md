# VAK_5.14

## 1. Sanskrit (Devanāgarī)

```sanskrit
मिथ्यादृग्विमती ताभ्यां युक्ताविद्याथ केवला ।
निरोधमार्गदृग्घेयाः षडनास्रवगोचराः ॥ ५.१४ ॥
```

## 2. Sanskrit (IAST)

```text
mithyādṛg-vimatī tābhyāṃ yuktāvidyātha kevalā |
nirodha-mārga-dṛg-gheyāḥ ṣaḍ anāsrava-gocarāḥ || 5.14 ||
```

The verse introduces a new axis for classifying the ninety-eight anuśayas:
whether their cognitive field is contaminated or uncontaminated.

## 3. Padaccheda and Lexical Analysis

```text
mithyā-dṛk | vimatiḥ | tābhyām | yuktā | avidyā | atha | kevalā |
nirodha-mārga-dṛk-gheyāḥ | ṣaṭ | anāsrava-gocarāḥ
```

| Form | Morphology | Contextual sense |
|---|---|---|
| `mithyā-dṛk` | nominative singular feminine | false view |
| `vimatiḥ` | nominative singular feminine | doubt; divided or uncertain judgment |
| `tābhyām` | instrumental dual feminine | with those two [false view and doubt] |
| `yuktā` | nominative singular feminine | conjoined, associated |
| `avidyā` | nominative singular feminine | ignorance |
| `atha` | indeclinable connective | and further, and then |
| `kevalā` | nominative singular feminine | alone, independent |
| `nirodha-mārga-dṛk-gheyāḥ` | nominative plural masculine | abandoned through seeing cessation and path |
| `ṣaṭ` | cardinal numeral | six |
| `anāsrava-gocarāḥ` | nominative plural masculine | having an uncontaminated range or cognitive field |

`Dṛk-gheya` compresses “to be abandoned through seeing.” `Gocara` denotes the
field over which cognition ranges and is functionally parallel here to the
Bhāṣya's `ālambana` vocabulary.

## 4. Grammar

**Enumeration of the afflicted modes**

```text
mithyā-dṛk
vimatiḥ
tābhyāṃ yuktā avidyā
atha kevalā [avidyā]
```

`Tābhyām` refers to the dual pair false view and doubt. `Kevalā` agrees with an
understood repetition of `avidyā`, distinguishing independent ignorance from
ignorance associated with either member of the pair.

**Truth-field and result**

```text
nirodha-mārga-dṛk-gheyāḥ
ṣaṭ anāsrava-gocarāḥ [bhavanti]

those abandoned through seeing cessation and path
are six whose fields are uncontaminated
```

The plural masculine adjectives agree with the understood `anuśayāḥ`.
Although the verse distinguishes associated and independent modes of
ignorance, the Bhāṣya counts three anuśaya species in each truth-field:
false view, doubt, and ignorance. Thus the total is three times two, not four
times two.

## 5. Translation

### Literal Translation

> False view, doubt, ignorance associated with those two, and [ignorance]
> that is independent—the six abandoned through seeing cessation and the path
> have uncontaminated fields.

### Bhāṣya-informed study translation

> Six anuśayas have uncontaminated cognitive supports: false view, doubt, and
> ignorance concerning cessation, and the same three concerning the path.
> Ignorance may be associated with false view or doubt, or it may occur
> independently. All the remaining anuśayas have contaminated cognitive
> supports.

The three-per-truth count and the contaminated status of the complement are
made explicit by the Bhāṣya.

## 6. Philosophical Translation

> An afflicted cognition need not have an afflicted object. Cessation and the
> path remain uncontaminated even when they are denied, doubted, or not known.
> The defect belongs to the cognitive determination of the truth-field, not to
> that field's own status. Liberation therefore requires more than the mere
> presence of a true or liberative content: the relation to it must itself
> become adequate through seeing.

The verse fixes the structure of this error:

```text
uncontaminated truth-field
    + afflicted mode of determination
        = afflicted cognition of an uncontaminated object
```

The object is not falsified in itself; it is falsely determined, doubted, or
left unknown.

## 7. Technical Vocabulary

**`Anāsrava-gocara` — ranging over an uncontaminated field**

This compound qualifies the six anuśayas relationally. It does not declare
the anuśayas themselves uncontaminated. Their `gocara`—cessation or path—is
without contamination.

**`Sāsrava-ālambana` — having a contaminated cognitive support**

The complementary class is explicit in the Bhāṣya: the other ninety-two
anuśayas have contaminated cognitive supports.

**`Mithyādṛṣṭi` — false view**

Here false view denies or misconstrues cessation or path. It is abandoned by
seeing the very truth-field toward which its defective determination was
directed.

**`Vimati / vicikitsā` — doubt**

The kārikā's `vimati` is glossed by the Bhāṣya as `vicikitsā`. Its object may
be uncontaminated while its undecided cognitive relation remains afflicted.

**Associated and independent `avidyā`**

Associated ignorance accompanies false view or doubt. Independent ignorance
is not reducible to either conjunction. These are two modes of ignorance, but
`avidyā` remains one of the three anuśaya species counted for cessation and
one of the three counted for path.

**`Nirodha` — cessation**

The uncontaminated truth of cessation. False view, doubt, and ignorance
concerning it are abandoned through seeing cessation.

**`Mārga` — path**

The uncontaminated truth of the path. It is distinct from cessation as the
effective course is distinct from the cessation realized through it.

## 8. Logical Determination

The sixfold class is generated by a compact product:

```text
{FalseView, Doubt, Ignorance}
    × {Cessation, Path}
        = SixUncontaminatedObjectAnusayas
```

The ninety-eight are thereby partitioned:

```text
98 anuśayas
    ├── 6 with uncontaminated cognitive supports
    └── 92 with contaminated cognitive supports
```

The decisive typing constraints are:

```text
Afflicted(Cognition)
    ⇏ Contaminated(ObjectSupport)

Uncontaminated(ObjectSupport)
    ⇏ Unafflicted(Cognition)
```

More positively:

```text
HasObjectSupport(cognition, object)
AND Afflicted(cognition)
AND Uncontaminated(object)
    is a coherent determination
```

The mode of abandonment is object-specific:

```text
Misdetermines(x, Cessation)
    → AbandonedBySeeing(x, Cessation)

Misdetermines(x, Path)
    → AbandonedBySeeing(x, Path)
```

The truth that is misconceived supplies the determinate field through whose
seeing the corresponding affliction is removed.

## 9. Interpretive Note

VAK 5.14 gives us perhaps the clearest evidence yet that `ālambana` cannot be
reduced to a ready-made external object. Cessation and path are objective
truth-fields, but their presence does not determine the quality of the
cognitive act. The relation must itself be typed:

```text
status of the objective field
status of the cognitive relation
status of the resulting cognition
```

This clarifies the transactional manifestation of Reason. The Product can
contain a valid determination—cessation or path—while the Subject's relation
to that determination remains denial, indecision, or ignorance. Concrete
Existence is therefore not divided into a pure object on one side and an
afflicted subject on the other. The determinate result is their relation:

```text
ObjectSupport(Cessation or Path)
    × CognitiveMode(FalseView, Doubt, or Ignorance)
        → concrete afflicted cognition
```

The truth-field remains what it is throughout this defective transaction.
What must be transformed is the form in which the Subject determines it.
Seeing is consequently not an abstract cancellation of error. It is the
production of an adequate relation to the same determinate truth that had
been denied, doubted, or obscured.

The distinction between cessation and path is also essential to the Product.
Cessation determines the achieved end; path determines the effective process.
One may acknowledge an end while misconceiving its means, or propose a means
while failing to comprehend genuine cessation. The twofold objective display
must therefore preserve both Telos and Way.

This is Organon reconstruction. Its textual ground is the kārikā's
`anāsrava-gocara` and the Bhāṣya's explicit distinction between the afflicted
anuśaya and the uncontaminated status of its cognitive support.

## 10. OWL++ Seed

```ttl
vak:VAK_5_14 a vak:Karika ;
    rdfs:label "VAK 5.14" ;
    vak:continues vak:VAK_5_13 ;
    vak:hasTopic vak:UncontaminatedObjectAnusaya,
                 vak:CognitionObjectStatusDistinction .

vak:SixUncontaminatedObjectAnusayas
    vak:generatedFrom vak:ThreeAfflictedModes,
                      vak:TwoUncontaminatedTruthFields ;
    vak:memberCount 6 .

vak:ThreeAfflictedModes
    vak:includes vak:FalseView,
                 vak:Doubt,
                 vak:Ignorance .

vak:TwoUncontaminatedTruthFields
    vak:includes vak:Cessation,
                 vak:Path .

vak:Cessation a vak:UncontaminatedObjectSupport .
vak:Path a vak:UncontaminatedObjectSupport .

vak:UncontaminatedObjectSupport
    owl:distinctFrom vak:UnafflictedCognition .

vak:RemainingNinetyTwoAnusayas
    vak:hasObjectSupportType vak:ContaminatedObjectSupport .

vak:AdequateSeeingRule a vak:TransformationRule ;
    vak:transforms vak:AfflictedCognitiveRelation ;
    vak:preserves vak:TruthFieldIdentity ;
    vak:produces vak:AdequateRelationToTruth .
```

The seed types cognition, cognitive relation, and objective support
separately. It does not infer the status of one from the status of another.
