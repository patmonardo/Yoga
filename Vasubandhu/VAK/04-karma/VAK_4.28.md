# VAK_4.28

## Sanskrit — Devanāgarī

```sanskrit
काल्यं ग्राह्योऽन्यतो नीचैः स्थितेनोक्तानुवादिता ।
उपवासः समग्राङ्गो निर्भूषेणानिशाक्षयात् ॥
```

## Sanskrit — IAST

```iast
kālyaṃ grāhyo 'nyato nīcaiḥ sthitenoktānuvāditā |
upavāsaḥ samagrāṅgo nirbhūṣeṇāniśākṣayāt ||
```

## Source reference and caution

Source: `VAkK_4.28`.

The verse specifies the concrete procedure and conditions for undertaking the one-day-and-night upavāsa restraint introduced in VAK 4.27.

## Padaccheda

```text
kālyam
grāhyaḥ
anyataḥ
nīcaiḥ
sthitena
ukta-anuvāditā

upavāsaḥ
samagra-aṅgaḥ
nirbhūṣeṇa
ā-niśā-kṣayāt
```

| Form | Analysis | Working meaning |
|---|---|---|
| `kālyam` | adverb from `kāla` | at the proper time; in the morning |
| `grāhyaḥ` | gerundive | is to be undertaken or received |
| `anyataḥ` | ablative/adverbial | from another |
| `nīcaiḥ` | adverb | lower down; humbly |
| `sthitena` | instrumental singular | by one standing or situated |
| `uktānuvāditā` | `ukta` + `anu-vad` abstract expression | repetition of what has been spoken |
| `upavāsaḥ` | nominative singular | upavāsa observance |
| `samagrāṅgaḥ` | nominative singular compound | complete in its limbs |
| `nirbhūṣeṇa` | instrumental singular | by one without adornment |
| `āniśākṣayāt` | temporal expression | until the end of the night |

## Literal translation

> The upavāsa is to be undertaken in the morning, from another, by one standing in a lower position and repeating what has been said. It must be complete in all its limbs, observed without adornment, until the end of the night.

## Philosophical translation

> The one-day observance is formally received at the proper morning time from another person. The recipient places himself in a deferential position and makes the spoken norm his own by repeating it. The observance must be accepted as an integral whole, embodied without ornamental self-display, and sustained through the completion of the night.

## Technical analysis

### `kālyaṃ grāhyaḥ`

The observance is undertaken at its proper beginning, ordinarily the morning. Its temporal form is instituted before the day is lived under it.

```text
morning undertaking
    → day-long observance
    → completion through the night
```

### `anyataḥ`

The vow is received from another person. Private intention alone does not constitute the complete formal acquisition.

```text
another communicates the established form
    → the recipient enters that form
```

### `nīcaiḥ sthitena`

The recipient occupies a lower bodily position. Posture expresses that the recipient does not legislate the norm from isolated preference but places himself under an already established form.

### `uktānuvāditā`

The recipient repeats what the other has pronounced.

```text
formula spoken by another
    → formula repeated by the recipient
    → norm becomes a first-person undertaking
```

Repetition is appropriation rather than empty duplication.

### `samagrāṅgaḥ`

The observance must possess all its limbs. It is one articulated whole, not an accidental selection of disconnected rules.

```text
whole observance
    → differentiated into limbs

limbs
    → sustain the whole
```

### `nirbhūṣeṇa`

The observer is unadorned. The vow therefore includes embodied presentation and temporarily suspends ornamental self-display.

### `āniśākṣayāt`

The observance continues until the end of the night, completing the full day-and-night period specified in VAK 4.27.

## Procedural structure

```text
proper time
    kālyam

mediating person
    anyataḥ

embodied posture
    nīcaiḥ sthitena

verbal appropriation
    uktānuvāditā

completeness
    samagrāṅga

bodily presentation
    nirbhūṣeṇa

temporal completion
    ā niśākṣayāt
```

The vow becomes actual through the unity of time, interpersonal relation, body, speech, content, appearance, and duration.

## Typed feature structure

```text
[ OBSERVANCE       upavāsa
  ACQUISITION-TIME morning
  MEDIATOR         another-person
  RECIPIENT-STANCE lower-position
  SPEECH-ACT       responsive-repetition
  COMPLETENESS     all-limbs
  ADORNMENT        absent
  TERMINUS         end-of-night ]
```

## Doctrinal determination

1. Upavāsa begins at the proper morning time.
2. It is received from another person.
3. The recipient assumes a deferential bodily posture.
4. The formula is repeated responsively.
5. The observance must be complete in all its limbs.
6. The observer remains unadorned.
7. The vow lasts until the night has ended.

## Relation to VAK 4.26–4.27

```text
VAK 4.26
    prātimokṣa restraint is acquired
    through another and formal communication

VAK 4.27
    the upavāsa undertaking lasts
    one day and one night

VAK 4.28
    specifies the complete procedure
    by which that bounded form is instituted
```

## Light Organon interpretation

A person becomes a determinate practical subject by entering a recognized form. The vow is not a private mental state but a socially mediated unity of declaration, acceptance, posture, conduct, and duration.

```text
ordinary act
    + vow-form
        → moment of a sustained life-structure
```

The spoken universal becomes the subject's own determination through responsive repetition.

```text
before repetition:
    the vow is spoken to me

through repetition:
    the vow is spoken by me

after repetition:
    the vow determines me
```

## OWL++ seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_28
    a vak:Karika ;
    rdfs:label "VAK 4.28" ;
    vak:continues vak:VAK_4_27 ;
    vak:hasTopic vak:UpavasaUndertakingProcedure .

vak:UpavasaUndertaking
    vak:hasBeginning vak:Morning ;
    vak:isReceivedFrom vak:OtherPerson ;
    vak:requiresSpeechAct vak:ResponsiveRepetition ;
    vak:requiresCompleteness vak:AllLimbs ;
    vak:requiresPresentation vak:UnadornedPresentation ;
    vak:hasTerminus vak:EndOfNight .

vak:VowRecipient
    vak:assumesPosture vak:LowerPosition ;
    vak:repeatsStatementOf vak:VowAdministrator .

vak:ResponsiveRepetition
    vak:generates vak:PersonallyAssumedVowForm .
```

## Verse summary

```text
VAK 4.28

The upavāsa vow is formally instituted through:

    proper time
    another person
    deferential posture
    responsive speech
    all constituent limbs
    unadorned embodiment
    completion of the night

A vow becomes actual through a complete unity of intention, speech, body, social mediation, and time.
```
