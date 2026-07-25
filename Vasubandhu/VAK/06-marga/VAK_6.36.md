# VAK 6.36

## Sanskrit

### Devanāgarī

क्षीणसप्ताष्टदोषांश एकजन्मैकवीचिकः ।  
तृतीयप्रतिपन्नश्च सोऽनागामि नवक्षयात् ॥ ६.३६ ॥

### IAST

**kṣīṇa-saptāṣṭa-doṣāṃśa ekajanmaikavīcikaḥ |**  
**tṛtīya-pratipannaś ca so 'nāgāmi nava-kṣayāt || 6.36 ||**

## Source Caution

The verse continues the nine-grade classification introduced in VAK 6.33 and applied to the desire-realm cultivation-abandonable faults in VAK 6.34–6.35.

It marks two thresholds:

```text
seven or eight grades destroyed
    → one-birth / one-interval practitioner
    → candidate for the third fruit

all nine grades destroyed
    → non-returner
```

The technical expression **ekavīcika** should be retained with caution at this stage. The kārikā associates it with the destruction of seven or eight grades and with proximity to the third fruit. Detailed distinctions belong to the Bhāṣya pass.

## Padaccheda

```text
kṣīṇa-sapta-aṣṭa-doṣa-aṃśaḥ
eka-janma-eka-vīcikaḥ

tṛtīya-pratipannaḥ
ca
saḥ
anāgāmī
nava-kṣayāt
```

## Grammar

- **kṣīṇa-sapta-aṣṭa-doṣāṃśaḥ** — nominative singular masculine compound: “one for whom seven or eight portions of the faults have been destroyed.”
- **eka-janma** — nominative singular masculine compound: “having one birth [remaining].”
- **eka-vīcikaḥ** — nominative singular masculine technical designation: “one-interval practitioner.”
- **tṛtīya-pratipannaḥ** — nominative singular masculine: “a candidate progressing toward the third fruit.”
- **ca** — indeclinable: “and.”
- **saḥ** — nominative singular masculine: “he.”
- **anāgāmī** — nominative singular masculine: “a non-returner.”
- **nava-kṣayāt** — ablative singular: “from the destruction of the ninth,” that is, when the ninth grade has been destroyed.

## Literal Translation

One for whom seven or eight portions of the faults have been destroyed is a one-birth, one-interval practitioner and a candidate for the third fruit. With the destruction of the ninth, he is a non-returner.

## Philosophical Translation

When seven or eight of the nine desire-realm cultivation-abandonable grades have been eliminated, the practitioner stands immediately near the third fruit and is designated as one with only one birth or one interval remaining. When the ninth and final grade is eliminated, the practitioner is established as a non-returner.

## The Seven- and Eight-Grade Threshold

The first half states:

```text
seven grades destroyed
or
eight grades destroyed
```

At this point the practitioner is designated:

```text
eka-janma
    one birth remaining

eka-vīcika
    one interval remaining
```

The verse groups these under the status:

```text
tṛtīya-pratipanna
    candidate toward the third fruit
```

The third fruit is non-returning.

## Destruction of the Ninth Grade

The final phrase is:

```text
nava-kṣayāt
    from destruction of the ninth
```

This completes the destruction of all nine desire-realm cultivation-abandonable grades.

The corresponding status is:

```text
anāgāmin
    non-returner
```

Thus the verse fixes the final threshold within this nine-grade sequence:

```text
grades 1–8 destroyed
    candidate toward non-returning

grade 9 destroyed
    established as non-returner
```

## Doctrinal Determination

```text
ThirdFruitCandidate {
    destroyedGrades:
        SevenOrEight

    designations:
        OneBirth
        OneInterval

    progressesToward:
        NonReturnerFruit
}

NonReturner {
    destroyedGrades:
        Nine

    status:
        EstablishedInThirdFruit
}
```

## Logical Determination

VAK 6.35 fixed the sixth-grade threshold for once-returning. VAK 6.36 now fixes the upper end of the same nine-grade scale:

```text
six grades destroyed
    once-returner

seven or eight grades destroyed
    candidate toward non-returning

nine grades destroyed
    non-returner
```

The verse is therefore a classification by completed degree of abandonment.

## OWL++ Seed

```text
Class: ThirdFruitCandidate
Class: NonReturner
Class: OneBirthPractitioner
Class: OneIntervalPractitioner
Class: DesireRealmCultivationGrade

ObjectProperty: hasDestroyedGradeCount
ObjectProperty: hasDesignation
ObjectProperty: progressesToward
ObjectProperty: isEstablishedIn

ThirdFruitCandidate
    hasDestroyedGradeCount SevenOrEight

ThirdFruitCandidate
    hasDesignation OneBirthPractitioner

ThirdFruitCandidate
    hasDesignation OneIntervalPractitioner

ThirdFruitCandidate
    progressesToward NonReturnerFruit

NonReturner
    hasDestroyedGradeCount Nine

NonReturner
    isEstablishedIn NonReturnerFruit
```

## Determinate Summary

```text
seven or eight grades destroyed
    → one-birth / one-interval practitioner
    → candidate for the third fruit

all nine grades destroyed
    → non-returner
```

VAK 6.36 completes the desire-realm nine-grade sequence by distinguishing proximity to non-returning from establishment in the third fruit.