# VAkK 8.23

## Sanskrit

त्रिधा अदुःखासुखं तच्च महाब्रह्मफलं च तत् ।
सवितर्कविचारोऽधःसमाधिः परतोऽद्वयः ॥ VAkK_8.23 ॥

## IAST

tridhā aduḥkhāsukhaṃ tac ca mahābrahmaphalaṃ ca tat /
savitarkavicāro 'dhaḥsamādhiḥ parato 'dvayaḥ // VAkK_8.23 //

## Source Caution

The source prints `tridhā aduḥkhāsukhaṃtacca`; this is segmented here as `tridhā aduḥkhāsukhaṃ tac ca`. The verse continues the discussion of the intermediate dhyāna from VAkK 8.22.

## Padaccheda

- tridhā
- aduḥkha-asukham
- tat
- ca
- mahābrahma-phalam
- ca
- tat
- sa-vitarka-vicāraḥ
- adhaḥ-samādhiḥ
- parataḥ
- a-dvayaḥ

## Grammar

- **tridhā** — indeclinable, “in three ways” or “threefold.”
- **aduḥkhāsukham** — nominative singular neuter, “neither painful nor pleasant.”
- **tat ca** — “and that,” referring to the intermediate dhyāna introduced in the preceding verse.
- **mahābrahmaphalam** — nominative singular neuter, “having Great Brahmā as its fruit” or “resulting in the Great Brahmā state.”
- **savitarkavicāraḥ** — nominative singular masculine, “accompanied by vitarka and vicāra.”
- **adhaḥsamādhiḥ** — nominative singular masculine, “the lower samādhi.”
- **parataḥ** — indeclinable, “beyond that,” “above that.”
- **advayaḥ** — nominative singular masculine, “without the two”; here, without both vitarka and vicāra.

## Literal Translation

That intermediate dhyāna is threefold, neither painful nor pleasant, and has Great Brahmā as its result. The lower samādhi is accompanied by vitarka and vicāra; beyond that, [samādhi] is without the two.

## Philosophical Translation

The intermediate dhyāna is internally differentiated into three modes, is affectively neutral, and bears the Great Brahmā state as its cosmological result. With respect to discursive factors, samādhi is then divided genetically: the lower samādhi contains both vitarka and vicāra; the intermediate dhyāna removes vitarka while retaining vicāra; all higher samādhis are free from both.

## Technical Vocabulary

- **antaradhyāna** — intermediate dhyāna, between the first and second dhyānas.
- **tridhā** — threefold; here, the standard three modes of pure, uncontaminated, and defiled attainment.
- **aduḥkhāsukha** — neither painful nor pleasant; affective neutrality.
- **mahābrahmaphala** — the Great Brahmā state as result.
- **vitarka** — initial discursive application or coarse examination.
- **vicāra** — sustained examination or subtle discursive consideration.
- **samādhi** — collectedness; the unifying cognitive determination.
- **advaya** — lacking both members of the stated pair.

## Doctrinal Determination

The verse completes the account of the intermediate dhyāna and uses it to establish a three-level classification of samādhi.

The intermediate dhyāna is:

1. **threefold** in mode;
2. **neither painful nor pleasant** in feeling;
3. productive of the **Great Brahmā** result;
4. free from **vitarka** while still retaining **vicāra**.

This yields the complete classification:

```text
lower samādhi
    vitarka + vicāra

intermediate dhyāna
    no vitarka + vicāra

higher samādhis
    no vitarka + no vicāra
```

The intermediate dhyāna is therefore not an accidental gap. It is the explicit mediating ground between the coarse discursivity of the first dhyāna and the nondiscursive collectedness of the higher attainments.

## Logical Determination

The verse presents a genetic division rather than a merely external classification.

The lower samādhi contains both determinations. The intermediate dhyāna negates the first while preserving the second. The higher samādhis negate both.

```text
(vitarka, vicāra)
    → (¬vitarka, vicāra)
    → (¬vitarka, ¬vicāra)
```

Each transition specifies its ground:

- the intermediate stage is grounded in the removal of vitarka;
- the higher stage is grounded in the subsequent removal of vicāra.

Thus the complete division is generated from the determinate transformation of the pair itself. This is why VAkK 8.23 forms a genuine transition verse: it closes the objective field of samāpatti by specifying every stage through the presence or absence of its discursive factors.

## Organon Light

The 2×2 dhyānic plane belongs to the sphere of objective determinations. Vitarka and vicāra are not yet the Concept; they are determinate factors whose combinations define the objective stages of collectedness.

VAkK 8.23 completes that field by exhausting the admissible configurations relevant to the hierarchy:

```text
both present
only vicāra present
neither present
```

The point is not that the higher samādhi becomes an empty absence. Rather, the objective determinations have been progressively idealized until samādhi can be considered independently of both discursive factors.

This prepares the transition from **Samāpatti**, the attained objective configuration, to **Samādhi**, the determinate Concept of that configuration. VAkK 8.24 can therefore begin the doctrine of the liberative samādhis because the complete field of fundamental attainments has now been genetically specified.

## OWL++ Seed

```text
Class: Samadhi
Class: LowerSamadhi
Class: IntermediateDhyana
Class: HigherSamadhi
Class: Vitarka
Class: Vicara
Class: GreatBrahmaResult

ObjectProperty: hasFactor
ObjectProperty: lacksFactor
ObjectProperty: hasResult
ObjectProperty: immediatelyHigherThan

LowerSamadhi
    hasFactor Vitarka
    hasFactor Vicara

IntermediateDhyana
    lacksFactor Vitarka
    hasFactor Vicara
    hasResult GreatBrahmaResult

HigherSamadhi
    lacksFactor Vitarka
    lacksFactor Vicara

IntermediateDhyana
    immediatelyHigherThan LowerSamadhi

HigherSamadhi
    immediatelyHigherThan IntermediateDhyana
```

## Commit History

- Initial Sanskrit-first analysis of VAkK 8.23.
