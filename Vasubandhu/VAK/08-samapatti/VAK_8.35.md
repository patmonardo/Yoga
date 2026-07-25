# VAK_8.35

## Sanskrit

अभिभ्वायतनान्यष्टौ द्वयमाद्यविमोक्षवत् ।
द्वे द्वितीयवत् अन्यानि पुनः शुभविमोक्षवत् ॥

## IAST

abhibhvāyatanāny aṣṭau dvayam ādya-vimokṣavat /
dve dvitīyavat anyāni punaḥ śubha-vimokṣavat //

## Padaccheda

abhibhū-āyatanāni | aṣṭau | dvayam | ādya-vimokṣavat | dve | dvitīyavat | anyāni | punaḥ | śubha-vimokṣavat

## Literal Translation

There are eight spheres of mastery. A pair is like the first Deliverance; two are like the second; the remaining ones, again, are like the Deliverance through the pure.

## Philosophical Translation

Eight mastery-spheres are distinguished. The first pair is patterned after the first Deliverance, the next pair after the second, and the remaining four after the Deliverance through the pure. The Deliverances thus provide the practical templates, while the mastery-spheres intensify command over the corresponding object-fields.

## Technical Vocabulary

- **abhibhū-āyatana** — sphere or base of mastery; an object-field brought under practiced cognitive command
- **aṣṭau** — eight
- **ādya-vimokṣavat** — like the first Deliverance
- **dvitīyavat** — like the second
- **śubha-vimokṣavat** — like the Deliverance through the pure or beautiful
- **āyatana** — a mediated field or base through which a determinate relation becomes operative

## Doctrinal Determination

The verse introduces the eight abhibhvāyatanas, traditionally rendered as spheres or bases of mastery. Their classification is derivative:

1. the first two correspond to the pattern of the first Deliverance;
2. the next two correspond to the second Deliverance;
3. the remaining four correspond to the pure Deliverance.

The verse therefore does not yet enumerate their detailed objects. It establishes their dependency upon the previously analyzed Deliverances.

## Logical Determination

The movement is from release to command:

- **vimokṣa** loosens domination by an object-field;
- **abhibhū-āyatana** establishes mastery within that field.

The same mediated relation is retained, but its practical determination changes. What was first a field from which one is delivered becomes a field over which cognition acquires stable authority.

## Organon Interpretation

The appearance of **āyatana** is decisive. These are not merely internal states or isolated qualities. They are structured relations between practitioner and object-field.

Thus the mastery-sphere is a transformation of Essential Relation:

```text
faculty ↔ object-field
        ↓
practiced mastery of the relation
```

The practitioner does not abolish the field. The relation is reconfigured so that the field no longer dictates the form of cognition.

In this first pass, the verse supports a distinction:

```text
Deliverance
    freedom from domination by a field

Mastery-sphere
    positive command within that field
```

This remains a practical classification. It should not yet be forced into a final Samāpatti or Samādhi determination before the bhāṣya and subsequent passes.

## OWL++ Seed

```turtle
@prefix vak: <https://example.org/vak/> .
@prefix yoga: <https://example.org/yoga/> .

vak:VAK_8_35 a vak:Karika ;
    vak:teaches vak:EightMasterySpheres .

vak:EightMasterySpheres a vak:PracticeComplex ;
    vak:memberCount 8 ;
    vak:derivedFrom vak:Deliverances .

vak:FirstMasteryPair vak:patternedAfter vak:FirstDeliverance .
vak:SecondMasteryPair vak:patternedAfter vak:SecondDeliverance .
vak:RemainingFourMasterySpheres vak:patternedAfter vak:PureDeliverance .

vak:MasterySphere a vak:Ayatana ;
    vak:practicalFunction vak:MasteryOfObjectField .
```

## Commit History

- First-pass kārikā analysis committed after identifying the derivative relation between the eight mastery-spheres and the first three Deliverances.
