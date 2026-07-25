# VAK 6.35

## Sanskrit

### Devanāgarī

आपञ्चमप्रकारघ्नो द्वितीयप्रतिपन्नकः ।  
क्षीणषष्ठप्रकारस्तु सकृदागाम्यसौ पुनः ॥ ६.३५ ॥

### IAST

**āpañcama-prakāraghno dvitīya-pratipannakaḥ |**  
**kṣīṇa-ṣaṣṭha-prakāras tu sakṛdāgāmy asau punaḥ || 6.35 ||**

## Source Caution

The verse continues the nine-grade scheme introduced in VAK 6.33 and applied to stream-enterers in VAK 6.34.

The relevant grades here are the cultivation-abandonable faults of the desire realm.

```text
up to five grades destroyed
    candidate for the second fruit

sixth grade destroyed
    once-returner
```

The verse is classificatory. It identifies the practitioner according to how many of the nine grades have been eliminated.

## Padaccheda

```text
ā-pañcama-prakāra-ghnaḥ
dvitīya-pratipannakaḥ

kṣīṇa-ṣaṣṭha-prakāraḥ
tu
sakṛd-āgāmī
asau
punaḥ
```

## Grammar

- **ā-pañcama-prakāra-ghnaḥ** — nominative singular masculine compound: “one who has destroyed up through the fifth grade.”
- **dvitīya-pratipannakaḥ** — nominative singular masculine: “a candidate progressing toward the second fruit.”
- **kṣīṇa-ṣaṣṭha-prakāraḥ** — nominative singular masculine compound: “one for whom the sixth grade has been exhausted.”
- **tu** — indeclinable: “but” or “whereas.”
- **sakṛd-āgāmī** — nominative singular masculine: “once-returner.”
- **asau** — nominative singular masculine: “that one.”
- **punaḥ** — indeclinable: “again,” here marking the next determination in the sequence.

## Literal Translation

One who has destroyed up through the fifth grade is a candidate progressing toward the second fruit. But one for whom the sixth grade has been exhausted is a once-returner.

## Philosophical Translation

Within the ninefold grading of cultivation-abandonable faults in the desire realm, the practitioner who has eliminated no more than the first five grades is classified as progressing toward the second noble fruit. When the sixth grade is eliminated, that practitioner is established as a once-returner.

## The Second Fruit

The second fruit is:

```text
sakṛd-āgāmi-phala
    fruit of once-returning
```

The verse distinguishes the candidate for this fruit from the person established in it.

```text
grades 1–5 destroyed
    second-fruit candidate

grade 6 destroyed
    once-returner
```

## Candidate and Fruit-Holder

### Candidate

```text
dvitīya-pratipannaka
    progressing toward the second fruit
```

The practitioner is still classified by movement toward the fruit while the destruction has reached only as far as the fifth grade.

### Once-Returner

```text
sakṛd-āgāmin
    once-returner
```

The destruction of the sixth grade marks establishment in the second fruit.

## Relation to the Nine Grades

VAK 6.33 established nine grades for faults and qualities:

```text
1. mild-mild
2. mild-medium
3. mild-strong
4. medium-mild
5. medium-medium
6. medium-strong
7. strong-mild
8. strong-medium
9. strong-strong
```

VAK 6.35 applies that structure to the transition into the second fruit.

```text
up through grade 5
    candidate

grade 6 exhausted
    fruit-holder
```

## Doctrinal Determination

```text
SecondFruitCandidate {
    destroyedGrades:
        OneThroughFive

    status:
        ProgressingTowardOnceReturn
}

OnceReturner {
    destroyedGrades:
        OneThroughSix

    fruit:
        OnceReturnFruit
}
```

## Logical Determination

The verse gives a threshold classification:

```text
five grades destroyed
    still candidate

six grades destroyed
    established in fruit
```

The change in name follows the crossing of a determinate grade-boundary.

## Interpretive Note

For the first kārikā pass, the essential point is purely classificatory. The verse does not yet require a broader explanation of the path. It fixes the relation between the number of grades destroyed and the practitioner’s status.

## OWL++ Seed

```text
Class: SecondFruitCandidate
Class: OnceReturner
Class: OnceReturnFruit
Class: DesireRealmCultivationFault
Class: FifthGradeDestroyed
Class: SixthGradeDestroyed

ObjectProperty: hasDestroyedGrade
ObjectProperty: progressesToward
ObjectProperty: isEstablishedIn

SecondFruitCandidate
    hasDestroyedGrade FifthGradeDestroyed

SecondFruitCandidate
    progressesToward OnceReturnFruit

OnceReturner
    hasDestroyedGrade SixthGradeDestroyed

OnceReturner
    isEstablishedIn OnceReturnFruit
```

## Determinate Summary

```text
Within the nine grades
of desire-realm faults:

    destruction through grade 5
        → candidate for the second fruit

    destruction of grade 6
        → once-returner
```

VAK 6.35 fixes the grade-threshold at which progress toward the second fruit becomes establishment in the fruit of once-returning.
