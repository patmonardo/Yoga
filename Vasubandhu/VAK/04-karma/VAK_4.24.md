# VAK_4.24

## Sanskrit — Devanāgarī

```sanskrit
निवृतानिवृताभ्यां च नातीताभ्यां समन्वितः ।
असंवरो दुश्चरितं दौःशील्यं कर्म तत्पथः ॥
```

## Sanskrit — IAST

```iast
nivṛtānivṛtābhyāṃ ca nātītābhyāṃ samanvitaḥ |
asaṃvaro duścaritaṃ dauḥśīlyaṃ karma tatpathaḥ ||
```

## Source reference and caution

Source: `VAkK_4.24`.

The first half completes the temporal discussion of `vijñapti` begun in VAK_4.23. The second half opens the explicit determination of `asaṃvara`, non-restraint.

The opposition must be kept clear:

```text
nivṛta / anivṛta
    obscured / unobscured

saṃvara / asaṃvara
    restraint / non-restraint
```

The first pair must not be confused with the second.

## Padaccheda

```text
nivṛta-anivṛtābhyām
ca
na
atītābhyām
samanvitaḥ

asaṃvaraḥ
duścaritam
dauḥśīlyam
karma
tat-pathaḥ
```

| Form | Analysis | Working meaning |
|---|---|---|
| `nivṛta-anivṛtābhyām` | instrumental dual | with the obscured and unobscured kinds |
| `ca` | conjunction | and |
| `na` | negation | not |
| `atītābhyām` | instrumental dual | with the past forms of those two |
| `samanvitaḥ` | nominative masculine singular | endowed with; possessing |
| `asaṃvaraḥ` | nominative masculine singular | non-restraint |
| `duścaritam` | nominative neuter singular | misconduct |
| `dauḥśīlyam` | nominative neuter singular | bad discipline; ethical indiscipline |
| `karma` | nominative neuter singular | action |
| `tat-pathaḥ` | nominative masculine singular | its path; the path of that action |

The noun `avyākṛta` is understood with `nivṛta` and `anivṛta`:

```text
nivṛta-avyākṛta
    obscured-indeterminate

anivṛta-avyākṛta
    unobscured-indeterminate
```

## Literal translation

> And one is not endowed with the past obscured-indeterminate and unobscured-indeterminate manifest actions. Non-restraint is called misconduct, bad discipline, action, and the path of that action.

## Philosophical translation

> Past manifest activity of either neutral kind, obscured or unobscured, does not remain as an acquired determination of the continuum. Established non-restraint, however, is a positive karmic formation: as enacted it is misconduct, as ethical disposition it is indiscipline, as productive activity it is karma, and as a determinate course of completion it is a path of action.

## Technical analysis

### `nivṛtānivṛtābhyāṃ ... nātītābhyām samanvitaḥ`

Past manifest actions of the two neutral kinds are not possessed as continuing past determinations.

```text
neutral manifest action
    occurs
    ceases
    is not retained as past karmic possession
```

This qualifies the broad statement of VAK_4.23 concerning possession of past `vijñapti`.

### `asaṃvara`

`Asaṃvara` is not merely the absence of restraint.

The Kośa distinguishes:

```text
saṃvara
    restraint

asaṃvara
    established non-restraint

itara / madhyastha
    the other or intermediate condition
```

Therefore:

```text
asaṃvara
    ≠ simple lack of saṃvara
```

It is a positive acquired karmic determination toward harmful bodily and verbal conduct.

### `duścarita`

```text
dus-carita
    bad conduct
    wrongful course of activity
```

This views the same structure as enacted conduct.

```text
asaṃvara
    standing karmic condition

duścarita
    enacted wrongful conduct
```

### `dauḥśīlya`

`Dauḥśīlya` is the abstract noun corresponding to `duḥśīla`.

```text
śīla
    disciplined ethical form

dauḥśīlya
    malformed or defective ethical form
```

The provisional canonical translation is **bad discipline**, preserving the explicit relation to `śīla`.

### `karma tatpathaḥ`

The same structure is called `karma` insofar as it is productive activity, and `tatpathaḥ` insofar as it is the path of that action.

```text
karma
    action

tat-patha
    its determinate path
```

The verse therefore preserves a distinction later developed in the discussion of the ten karmic paths.

## Typed feature structure

```text
[ KARMIC-FORM       asaṃvara
  CONDUCT           duścarita
  ETHICAL-DISPOSITION dauḥśīlya
  ACTIVITY          karma
  PATH              karmapatha ]
```

For the first half:

```text
[ ACTION-TYPE       vijñapti
  ETHICAL-CLASS     neutral
  SUBCLASS          obscured | unobscured
  TEMPORAL-MODE     past
  POSSESSED         no ]
```

## Doctrinal determination

1. Past neutral manifest action is not possessed in either its obscured or unobscured form.
2. `Asaṃvara` is not mere privation but a positive continuing karmic condition.
3. The same negative practical structure is named according to different aspects:

```text
standing form        asaṃvara
enacted conduct      duścarita
ethical disposition  dauḥśīlya
productive activity  karma
determinate course   karmapatha
```

## Relation to VAK_4.16

VAK_4.16 gave the positive series:

```text
śīla
sucarita
karma
saṃvara
karmapatha
```

VAK_4.24 gives the corresponding negative series:

```text
dauḥśīlya
duścarita
karma
asaṃvara
karmapatha
```

The formal architecture is common; its ethical determination differs.

## Logical determination

The verse distinguishes occurrence from possession:

```text
an action occurs
    ≠
that action remains possessed
```

It also distinguishes abstract negation from determinate negation:

```text
simple absence of restraint
    intermediate condition

determinate non-restraint
    asaṃvara
```

Thus `asaṃvara` is not empty negation. It is the other of restraint made into a standing practical determination.

## Light Organon interpretation

The higher formal genus is persistent karmic form:

```text
avijñapti
    higher formal field

saṃvara
asaṃvara
itara
    determinate modes
```

The Triple is not transcendental. It incarnates the higher Idea of persistent karmic form.

## OWL++ seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_24
    a vak:Karika ;
    rdfs:label "VAK 4.24" ;
    vak:continues vak:VAK_4_23 ;
    vak:hasTopic vak:NonRestraint ;
    vak:opensBlock vak:RestraintAcquisitionBlock .

vak:NonRestraint
    a vak:KarmicForm ;
    vak:hasConductExpression vak:Misconduct ;
    vak:hasEthicalDisposition vak:BadDiscipline ;
    vak:hasKarmicCharacter vak:Karma ;
    vak:hasActionPath vak:KarmicPath .

vak:PastObscuredNeutralVijnapti
    vak:isNotPossessedBy vak:Agent .

vak:PastUnobscuredNeutralVijnapti
    vak:isNotPossessedBy vak:Agent .
```

## Verse summary

```text
VAK_4.24

Past neutral manifest action,
whether obscured or unobscured,
is not retained as a past possession.

Asaṃvara is not mere lack of restraint.
It is determinate non-restraint:

    as standing form      asaṃvara
    as conduct            duścarita
    as disposition        dauḥśīlya
    as activity           karma
    as determinate course karmapatha
```
