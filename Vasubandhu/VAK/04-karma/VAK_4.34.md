# VAK_4.34

## Sanskrit — Devanāgarī

```sanskrit
मृषावादप्रसङ्गाच्च सर्वशिक्षाव्यतिक्रमे ।
प्रतिक्षेपणसावद्यान्मद्यादेवान्यगुप्तये ॥
```

## Sanskrit — IAST

```iast
mṛṣāvādaprasaṅgāc ca sarvaśikṣāvyatikrame |
pratikṣepaṇasāvadyān madyād evānyaguptaye ||
```

## Source reference and caution

Source: `VAkK_4.34`.

The project source prints `mṛṣāvādaprasaṅgācca sarvaśikṣāvyatikrame / pratikṣepaṇasāvadyānmadyādeva anyuguptaye //`. The final expression is read provisionally as `madyāt eva anya-guptaye`, “from intoxicants precisely for the protection of the others.” The exact argumentative distribution of the first three phrases should be checked against the Bhāṣya.

## Padaccheda

```text
mṛṣā-vāda-prasaṅgāt ca
sarva-śikṣā-vyatikrame
pratikṣepaṇa-sāvadyāt
madyāt eva
anya-guptaye
```

## Literal translation

> Because complete transgression of the training rules would involve false speech, and because repudiation is blameworthy; abstention from intoxicants in particular is for the protection of the other rules.

## Philosophical translation

> A vow is not exhausted by the moment in which it is pronounced. To profess a discipline while rejecting its entire content implicates the practitioner in untruth, and deliberate repudiation of an accepted training is itself a fault. The prohibition of intoxicants has a distinctive systemic function: it preserves recollection and vigilance, thereby protecting the practitioner’s capacity to maintain all the other restraints.

## Technical analysis

### `mṛṣāvādaprasaṅgāt`

A declared undertaking creates a future practical relation. If the whole discipline is repudiated while restrained status is still claimed, false profession follows.

### `sarvaśikṣāvyatikrame`

The phrase concerns transgression of the training as a whole, not merely a single lapse. Imperfect observance remains distinct from complete denial of the discipline.

### `pratikṣepaṇasāvadyāt`

`pratikṣepaṇa` is repudiation: rejection of the authority of the accepted rule. This is stronger than weakness or accidental breach and is itself blameworthy.

### `madyād evānyaguptaye`

The intoxicant precept protects the remaining disciplines:

```text
intoxication
    → loss of recollection
    → negligence
    → vulnerability to other transgressions
```

It confirms the functional classification of VAK 4.29:

```text
first four precepts
    śīlāṅga

fifth precept
    apramādāṅga
```

The fifth is a second-order restraint: it protects the cognitive capacity through which the direct restraints remain operative.

## Doctrinal determination

1. Complete repudiation of professed training threatens truthfulness.
2. Rejection of an accepted discipline is itself blameworthy.
3. Abstention from intoxicants preserves recollection and vigilance.
4. The fifth precept protects all the other lay restraints.

## Relation to kleśa and Path

Ordinary restraint guards against both direct kleśa-driven acts and conditions that weaken discrimination. Intoxication removes the guard through which existing kleśas are prevented from becoming action. This prepares for the Path, which later directly discriminates and abandons kleśa.

## Light Organon interpretation

A durable normative form requires protection of the subject’s capacity to remain a bearer of that form. The fifth precept is therefore not merely one rule beside four others; it preserves rule-governed agency itself.

## OWL++ seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_34
    a vak:Karika ;
    rdfs:label "VAK 4.34" ;
    vak:continues vak:VAK_4_33 ;
    vak:hasTopic vak:ProtectionOfLayDiscipline .

vak:IntoxicantRestraint
    rdfs:subClassOf vak:NonNegligenceLimb ;
    vak:protects vak:OtherLayRestraints ;
    vak:preserves vak:Recollection ;
    vak:preserves vak:Vigilance .

vak:RepudiationOfAcceptedTraining
    vak:hasEthicalCharacter vak:Blameworthy .
```

## Verse summary

```text
VAK 4.34

Complete repudiation of professed training
threatens truthfulness.

Rejection of an accepted discipline
is itself blameworthy.

The intoxicant precept
protects the other restraints
by preserving recollection and vigilance.
```
