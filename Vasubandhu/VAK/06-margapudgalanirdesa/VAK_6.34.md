# VAK 6.34

## Sanskrit

### Devanāgarī

अक्षीणभावनाहेयः फलस्थः सप्तकृत्परः ।  
त्रिचतुर्विधमुक्तस्तु द्वित्रिजन्मा कुलंकुलः ॥ ६.३४ ॥

### IAST

**akṣīṇa-bhāvanā-heyaḥ phalasthaḥ saptakṛt-paraḥ |**  
**tri-catur-vidha-muktas tu dvi-tri-janmā kulaṃkulaḥ || 6.34 ||**

## Source Caution

The verse classifies two forms of the stream-enterer according to the number of cultivation-abandonable grades already eliminated.

The first is the stream-enterer in whom none of those grades has yet been exhausted. The second has been liberated from three or four grades.

The verse is descriptive and classificatory. Detailed explanation of how the rebirth counts are calculated belongs to the Bhāṣya pass.

## Padaccheda

```text
akṣīṇa-bhāvanā-heyaḥ
phala-sthaḥ
sapta-kṛt-paraḥ

tri-catur-vidha-muktaḥ
tu
dvi-tri-janmā
kulaṃkulaḥ
```

## Grammar

- **akṣīṇa-bhāvanā-heyaḥ** — nominative singular masculine: “one for whom the factors abandonable through cultivation are not exhausted.”
- **phala-sthaḥ** — nominative singular masculine: “one established in the fruit.”
- **sapta-kṛt-paraḥ** — nominative singular masculine: “one for whom seven times is the maximum”; the seven-at-most practitioner.
- **tri-catur-vidha-muktaḥ** — nominative singular masculine: “liberated from three or four kinds,” here three or four grades.
- **tu** — indeclinable: “but,” marking the contrast.
- **dvi-tri-janmā** — nominative singular masculine: “one having two or three births.”
- **kulaṃkulaḥ** — nominative singular masculine technical designation: “family-to-family.”

## Literal Translation

The one established in the fruit for whom the factors abandonable through cultivation are not exhausted is a seven-at-most. But one liberated from three or four grades, having two or three births, is a family-to-family practitioner.

## Philosophical Translation

Among those established in the first fruit, the practitioner who has not yet exhausted any of the cultivation-abandonable grades is classified as one whose wandering extends to at most seven further existences. The practitioner who has already been freed from three or four such grades is classified as family-to-family, with only two or three births remaining.

## The Seven-at-Most

```text
sapta-kṛt-para
    seven-at-most
```

This is a stream-enterer established in the first fruit but with the cultivation-abandonable factors still unexhausted.

```text
first fruit attained
    but
cultivation-abandonable grades not yet exhausted
    therefore
seven-at-most
```

The expression gives the maximum remaining range, not a requirement that exactly seven births must occur.

## The Family-to-Family Practitioner

```text
kulaṃkula
    family-to-family
```

This practitioner has already been liberated from three or four grades among the cultivation-abandonable factors.

```text
three or four grades eliminated
    →
two or three births remaining
    →
family-to-family
```

The verse therefore places the family-to-family practitioner further along the cultivation sequence than the seven-at-most practitioner.

## Relation to the Ninefold Scale

VAK 6.33 introduced nine grades of faults and qualities. VAK 6.34 begins to classify practitioners according to how many of those grades have been eliminated.

```text
0 grades eliminated
    seven-at-most

3 or 4 grades eliminated
    family-to-family
```

The intermediate and subsequent classifications continue in the following verses.

## Doctrinal Determination

```text
SevenAtMost {
    fruit:
        StreamEntry

    cultivationAbandonableGradesExhausted:
        Zero

    maximumRemainingBirths:
        Seven
}

FamilyToFamily {
    fruit:
        StreamEntry

    cultivationAbandonableGradesExhausted:
        ThreeOrFour

    remainingBirths:
        TwoOrThree
}
```

## Logical Determination

VAK 6.34 applies the ninefold grading system to the stream-enterer.

```text
same attained fruit
    differentiated by
number of cultivation-abandonable grades removed
```

The verse therefore distinguishes degree within one fruit-state:

```text
stream-entry
    with no cultivation-grade exhausted
        → seven-at-most

stream-entry
    with three or four grades exhausted
        → family-to-family
```

No larger interpretation is required at this stage. The verse records a technical classification based on prior elimination and remaining births.

## Interpretive Note

The key first-pass point is that attainment of stream-entry does not erase differences in the remaining cultivation-work. Practitioners established in the same fruit are further classified according to how much of the ninefold residue has already been eliminated.

## OWL++ Seed

```text
Class: StreamEnterer
Class: SevenAtMost
Class: FamilyToFamily
Class: CultivationAbandonableGrade
Class: RemainingBirthRange

ObjectProperty: establishedInFruit
ObjectProperty: hasExhaustedGradeCount
ObjectProperty: hasMaximumRemainingBirths
ObjectProperty: hasRemainingBirthRange

SevenAtMost
    subClassOf StreamEnterer

SevenAtMost
    hasExhaustedGradeCount ZeroGrades

SevenAtMost
    hasMaximumRemainingBirths SevenBirths

FamilyToFamily
    subClassOf StreamEnterer

FamilyToFamily
    hasExhaustedGradeCount ThreeOrFourGrades

FamilyToFamily
    hasRemainingBirthRange TwoOrThreeBirths
```

## Determinate Summary

```text
Among those established in stream-entry:

    if no cultivation-abandonable grade
    has been exhausted:
        seven-at-most

    if three or four grades
    have been exhausted:
        family-to-family
        with two or three births remaining
```

VAK 6.34 begins the graded classification of stream-enterers by correlating eliminated cultivation-grades with the maximum number of remaining births.