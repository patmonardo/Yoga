# VAK 6.33

## Sanskrit

### Devanāgarī

नवप्रकारा दोषा हि भूमौ भूमौ तथा गुणाः ।  
मृदुमध्याधिमात्राणां पुनर्मृद्वादिभेदतः ॥ ६.३३ ॥

### IAST

**nava-prakārā doṣā hi bhūmau bhūmau tathā guṇāḥ |**  
**mṛdu-madhyādhimātrāṇāṃ punar mṛdv-ādi-bhedataḥ || 6.33 ||**

## Source Caution

This verse gives the grading scheme presupposed by the subsequent classification of practitioners. It does not yet assign particular persons to each grade; it establishes the ninefold scale itself.

The key structure is:

```text
three principal grades:
    mild
    medium
    strong

with each principal grade again divided into:
    mild
    medium
    strong

therefore:
    nine grades
```

The same ninefold grading applies both to faults and to qualities within each level.

## Padaccheda

```text
nava-prakārāḥ
doṣāḥ
hi
bhūmau bhūmau
tathā
guṇāḥ

mṛdu-madhya-adhimātrāṇām
punaḥ
mṛdu-ādi-bhedataḥ
```

## Grammar

- **nava-prakārāḥ** — nominative plural masculine: “of nine kinds.”
- **doṣāḥ** — nominative plural masculine: “faults,” here the defilements or defects to be abandoned.
- **hi** — indeclinable: “for,” “indeed.”
- **bhūmau bhūmau** — distributive locative singular: “in each level.”
- **tathā** — indeclinable: “likewise.”
- **guṇāḥ** — nominative plural masculine: “qualities,” “virtues,” or advantageous factors.
- **mṛdu-madhya-adhimātrāṇām** — genitive plural: “of the mild, medium, and strong.”
- **punaḥ** — indeclinable: “again,” indicating a second-order subdivision.
- **mṛdu-ādi-bhedataḥ** — ablative singular compound: “because of the distinction beginning with mild,” that is, because each of the three is again divided into mild, medium, and strong.

## Literal Translation

For in each level the faults are of nine kinds, and likewise the qualities, because the mild, medium, and strong are again distinguished beginning with mild.

## Philosophical Translation

Within every level, both the faults to be removed and the qualities to be developed are graded in nine ways. This results because each of the three principal degrees—mild, medium, and strong—is itself subdivided into mild, medium, and strong.

## The Ninefold Scale

The verse establishes a simple three-by-three classification:

```text
mild:
    mild-mild
    mild-medium
    mild-strong

medium:
    medium-mild
    medium-medium
    medium-strong

strong:
    strong-mild
    strong-medium
    strong-strong
```

Thus:

```text
3 principal grades
    ×
3 subordinate grades
    =
9 grades
```

## Faults and Qualities

The same formal scale applies to two distinct series:

```text
doṣa
    fault
    defect
    defilement-grade

guṇa
    quality
    virtue
    advantageous grade
```

The verse therefore provides a common measure for:

```text
what is to be abandoned
    and
what is to be developed
```

At the kārikā-pass level, no further distribution is required. The following verses apply this grading to the successive stages and fruit-types.

## In Each Level

The distributive expression **bhūmau bhūmau** indicates that the ninefold grading recurs at every relevant level:

```text
each level
    has
        nine grades of faults
        nine grades of qualities
```

The structure is therefore recursive rather than confined to one isolated stage.

## Doctrinal Determination

```text
NinefoldGrading {
    principalGrades:
        Mild
        Medium
        Strong

    subordinateGrades:
        Mild
        Medium
        Strong

    totalGrades:
        Nine

    appliesTo:
        Faults
        Qualities

    scope:
        EachLevel
}
```

## Logical Determination

VAK 6.33 introduces a nested qualitative classification:

```text
first differentiation:
    mild
    medium
    strong

second differentiation within each:
    mild
    medium
    strong
```

The result is not a numerical measure but an ordered qualitative matrix.

```text
quality differentiated once
    → three grades

quality differentiated again within itself
    → nine grades
```

This verse supplies the formal scale that the following kārikās use to classify abandonment and attainment.

## OWL++ Seed

```text
Class: NinefoldGrade
Class: PrincipalGrade
Class: SubordinateGrade
Class: MildGrade
Class: MediumGrade
Class: StrongGrade
Class: FaultGrade
Class: QualityGrade
Class: Level

ObjectProperty: hasPrincipalGrade
ObjectProperty: hasSubordinateGrade
ObjectProperty: gradesFault
ObjectProperty: gradesQuality
ObjectProperty: appliesAtLevel

NinefoldGrade
    hasPrincipalGrade MildGrade

NinefoldGrade
    hasPrincipalGrade MediumGrade

NinefoldGrade
    hasPrincipalGrade StrongGrade

NinefoldGrade
    gradesFault FaultGrade

NinefoldGrade
    gradesQuality QualityGrade
```

## Determinate Summary

```text
In each level:

    faults are graded ninefold
    qualities are graded ninefold

because:

    mild
    medium
    strong

are each again divided into:

    mild
    medium
    strong
```

VAK 6.33 establishes the recurring ninefold qualitative scale used by the subsequent verses to distinguish degrees of abandonment, progress, and attainment.