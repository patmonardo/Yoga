# VAK_8.10 — Absent Limbs in the Defiled Dhyānas

## Sanskrit

### Devanāgarī

```text
क्लिष्टेष्वसत्प्रीतिसुखं प्रसादः सम्प्रधीः स्मृतिः ।
उपेक्षास्मृतिशुद्धिश्च केचित् प्रस्रब्ध्युपेक्षणे ॥ ८.१० ॥
```

### IAST

```text
kliṣṭeṣv asat prītisukhaṃ prasādaḥ saṃpradhīḥ smṛtiḥ /
upekṣāsmṛtiśuddhiś ca kecit prasrabdhyupekṣaṇe // VAK_8.10 //
```

## Source Caution

The transmitted form `saṃpradhīḥ` is compressed and doctrinally technical. In the present context it is taken with `smṛti` as the discriminative awareness and mindfulness characteristic of the third dhyāna.

The verse assigns absent limbs across the four defiled dhyānas rather than denying that all the listed factors are absent from every defiled dhyāna.

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| kliṣṭeṣu | locative plural | in the defiled dhyānas |
| asat | present participle of `as` with negation | not present; absent |
| prīti-sukham | compound | rapture and ease |
| prasādaḥ | nominative singular | inner clarity; confidence |
| saṃpradhīḥ | nominative singular | clear discriminative awareness |
| smṛtiḥ | nominative singular | mindfulness |
| upekṣā-smṛti-śuddhiḥ | nominative singular | purity of equanimity and mindfulness |
| ca | indeclinable | and |
| kecit | nominative plural | some authorities |
| prasrabdhi-upekṣaṇe | dual | tranquility and equanimity |

## Grammar

The governing construction is:

```text
kliṣṭeṣu ... asat
    in the defiled [dhyānas], ... is absent
```

The factors are distributed successively:

```text
first defiled dhyāna
    prīti and sukha absent

second defiled dhyāna
    prasāda absent

third defiled dhyāna
    saṃpradhī and smṛti absent

fourth defiled dhyāna
    purity of equanimity and mindfulness absent
```

The final pāda records an alternative view:

```text
kecit
    some authorities hold

prasrabdhi-upekṣaṇe
    tranquility and equanimity [are absent]
```

## Literal Translation

In the defiled dhyānas, rapture and ease, inner clarity, clear awareness and mindfulness, and the purity of equanimity and mindfulness are absent. Some hold that tranquility and equanimity are absent.

## Philosophical Translation

Each defiled dhyāna lacks the limb whose presence would express its corresponding purity. The first lacks the rapture and ease born of true separation; the second lacks inner clarity; the third lacks lucid awareness and mindfulness; the fourth lacks the purification of equanimity and mindfulness. According to another lineage, the absence is stated more generally as the absence of tranquility and equanimity.

## Technical Vocabulary

### kliṣṭa

```text
kliṣṭa
    afflicted
    contaminated
    accompanied by defilement
```

A dhyāna may retain its level and general structure while being internally compromised by affliction.

### prasāda

Here `prasāda` is not generic faith. It is the inward clarity characteristic of the second dhyāna. Defilement clouds that clarity.

### saṃpradhī

The term indicates lucid discriminative awareness. In the third dhyāna it functions together with mindfulness to prevent the practitioner from becoming confused by refined ease.

### upekṣā-smṛti-śuddhi

The fourth dhyāna is marked not merely by equanimity and mindfulness, but by their purification.

```text
upekṣā
    equanimity

smṛti
    mindfulness

śuddhi
    purification
```

Defilement leaves the nominal level intact while spoiling this purity.

## Doctrinal Determination

VAK 8.10 shows that a dhyāna can be classified by level and still fail in quality.

| Dhyāna | Limb absent when defiled |
|---|---|
| first | rapture and ease born of separation |
| second | inner clarity |
| third | clear awareness and mindfulness |
| fourth | purity of equanimity and mindfulness |

Thus:

```text
same level
    does not imply
same purity
```

The defiled attainment preserves enough structure to belong to a dhyāna-stage, but lacks the factor that would make that stage properly wholesome and lucid.

## Logical Determination

The verse distinguishes **formal membership** from **qualitative adequacy**.

```text
formal membership
    the state still counts as a dhyāna of that level

qualitative adequacy
    the decisive limb of purity is actually present
```

This is important for the chapter's method. Classification is not exhausted by counting limbs. The decisive question is whether the characteristic factor is present in the right quality.

```text
nominal structure
    can persist

essential quality
    can fail
```

## Organon Light

The first pass remains Kośa-clean.

The immediate lesson is qualitative:

```text
an attainment is not purified
merely because it resembles
its pure counterpart in structure
```

The difference lies in the presence or absence of the determining quality itself.

This fits the project's emerging principle:

```text
Logic
    is not empty abstraction from content

Logic
    is the determination of content
    according to its qualitative truth
```

That stronger reconstruction belongs to the later Organon pass; here it is only lightly marked.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix sam: <http://127.0.0.1:3000/samapatti#> .
@prefix dhy: <http://127.0.0.1:3000/dhyana#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_8_10
    a vak:Karika ;
    rdfs:label "VAK 8.10" ;
    vak:determines sam:DefiledDhyanaAbsences,
                   sam:QualitativeAdequacyDistinction .

sam:DefiledDhyanaAbsences
    a sam:DistributedAbsencePattern ;
    sam:assigns dhy:FirstDhyana sam:AbsenceOfRaptureAndEase ;
    sam:assigns dhy:SecondDhyana sam:AbsenceOfInnerClarity ;
    sam:assigns dhy:ThirdDhyana sam:AbsenceOfAwarenessAndMindfulness ;
    sam:assigns dhy:FourthDhyana sam:AbsenceOfPurifiedEquanimityAndMindfulness .

sam:QualitativeAdequacyDistinction
    a sam:LogicalDetermination ;
    sam:distinguishes sam:FormalStageMembership,
                      sam:PresenceOfDeterminingQuality .
```

## Commit History

```text
2026-07-25 — Initial kārikā-pass analysis.
```
