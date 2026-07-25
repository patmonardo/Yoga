# VAK_4.32

## Sanskrit — Devanāgarī

```sanskrit
बुद्धसङ्घकरान् धर्मानशैक्षानुभयांश्च सः ।
निर्वाणं चेति शरणं यो याति शरणत्रयम् ॥
```

## Sanskrit — IAST

```iast
buddhasaṃghakarān dharmān aśaikṣān ubhayāṃś ca saḥ |
nirvāṇaṃ ceti śaraṇaṃ yo yāti śaraṇatrayam ||
```

## Source reference and caution

Source: `VAkK_4.32`.

The verse determines the actual objects of the Three Refuges. Its compressed syntax distributes the compounds as follows:

```text
Buddha-refuge:
    buddhakarān dharmān aśaikṣān

Saṅgha-refuge:
    saṃghakarān dharmān ubhayān
    (śaikṣa and aśaikṣa)

Dharma-refuge:
    nirvāṇa
```

## Padaccheda

```text
buddha-karān
saṃgha-karān
dharmān
aśaikṣān
ubhayān
ca
saḥ
nirvāṇam
ca
iti
śaraṇam
yaḥ
yāti
śaraṇa-trayam
```

| Form | Analysis | Working meaning |
|---|---|---|
| `buddha-karān` | accusative plural masculine | constituting a Buddha |
| `saṃgha-karān` | accusative plural masculine | constituting the Saṅgha |
| `dharmān` | accusative plural masculine | dharmas |
| `aśaikṣān` | accusative plural masculine | belonging to one beyond training |
| `ubhayān` | accusative plural masculine | both kinds |
| `nirvāṇam` | accusative singular neuter | nirvāṇa |
| `śaraṇatrayam` | accusative singular neuter | the Three Refuges |

## Literal translation

> Whoever goes to the Three Refuges takes refuge in the aśaikṣa dharmas constituting the Buddha, in both the śaikṣa and aśaikṣa dharmas constituting the Saṅgha, and in nirvāṇa.

## Philosophical translation

> Going for refuge does not terminate in empirical persons or visible bodies. The Buddha-refuge is the completed ensemble of dharmas belonging to awakening beyond further training; the Saṅgha-refuge is the Path as realized by trainees and by those beyond training; and the Dharma-refuge is nirvāṇa itself, the unconditioned cessation toward which the Path proceeds.

## Technical analysis

### Buddha-refuge

The object is the `aśaikṣa` dharmas through which one is a Buddha. The refuge is therefore directed toward completed awakening, not merely toward the Buddha's physical body or historical personality.

### Saṅgha-refuge

The noble Saṅgha includes both `śaikṣa` and `aśaikṣa` persons. The refuge is in the noble Path-dharmas borne by these persons, not merely in a conventional aggregate of persons.

### Dharma-refuge

The strict object is nirvāṇa. Teaching indicates cessation, the Path realizes cessation, and nirvāṇa is cessation itself.

### `kara`

The compound-final `kara` means constituting or making. `Buddhakara-dharmas` are the dharmas through which one is a Buddha; `saṃghakara-dharmas` are the dharmas through which persons constitute the noble Saṅgha.

## Doctrinal determination

```text
Buddha:
    perfected aśaikṣa dharmas

Saṅgha:
    śaikṣa and aśaikṣa Path-dharmas

Dharma:
    nirvāṇa
```

The saint is therefore not merely an unusually virtuous personality. A saint is a continuum bearing determinate śaikṣa or aśaikṣa dharmas.

## Relation to VAK_4.30–4.31

```text
VAK_4.30
    refuge is required for the upavāsa orientation

VAK_4.31
    restraint may be acquired wholly but preserved by degrees

VAK_4.32
    determines the liberating objects toward which refuge is directed
```

## Relation to kleśa and Path

```text
śaikṣa:
    further kleśas remain to be abandoned
    or Path qualities remain to be cultivated

aśaikṣa:
    required abandonment and cultivation are complete
```

The distinction expresses the actual state of the continuum relative to kleśa, abandonment, Path, and liberation.

## Light Organon interpretation

The verse moves from sensible bearer to constitutive determination:

```text
visible Buddha
    → buddhakara dharmas

visible community
    → saṃghakara dharmas

spoken teaching
    → nirvāṇa as its final truth
```

The empirical bearer is not denied; it is comprehended through the determinations that give it Path-significance.

## Typed feature structure

```text
[ THREE-REFUGES
  BUDDHA-REFUGE
    [ OBJECT aśaikṣa-dharmas
      ROLE constitute-Buddha ]
  SANGHA-REFUGE
    [ OBJECTS [ śaikṣa-dharmas aśaikṣa-dharmas ]
      ROLE constitute-noble-Sangha ]
  DHARMA-REFUGE
    [ OBJECT nirvāṇa
      STATUS unconditioned ] ]
```

## OWL++ seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_32
    a vak:Karika ;
    rdfs:label "VAK 4.32" ;
    vak:continues vak:VAK_4_31 ;
    vak:hasTopic vak:ObjectsOfTheThreeRefuges .

vak:BuddhaRefuge
    vak:hasObject vak:BuddhaConstitutingAsaiksaDharmas .

vak:SanghaRefuge
    vak:hasObject vak:SanghaConstitutingSaiksaDharmas ;
    vak:hasObject vak:SanghaConstitutingAsaiksaDharmas .

vak:DharmaRefuge
    vak:hasObject vak:Nirvana .
```

## Verse summary

```text
Buddha refuge:
    perfected aśaikṣa dharmas

Saṅgha refuge:
    trainee and beyond-training Path-dharmas

Dharma refuge:
    nirvāṇa

Refuge is directed not merely toward empirical bearers,
but toward the liberating dharmas that make Buddha and Saṅgha what they are,
and toward nirvāṇa as the truth of Dharma.
```