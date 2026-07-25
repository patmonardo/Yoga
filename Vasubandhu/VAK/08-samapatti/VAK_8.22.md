# VAkK 8.22

## Sanskrit

अष्टौ सामन्तकान्येषां शुद्धादुःखासुखानि हि ।
आर्यं चाद्यं त्रिधा केचित् अतर्कं ध्यानमन्तरम् ॥ VAkK_8.22 ॥

## IAST

aṣṭau sāmantakāny eṣāṃ śuddhāduḥkhāsukhāni hi /
āryaṃ cādyaṃ tridhā kecid atarkaṃ dhyānam antaram // VAkK_8.22 //

## Source Caution

The source file reads `ārya cādyaṃ tridhā kecit atarka dhyānamantaram`. This is normalized here to `āryaṃ cādyaṃ tridhā kecid atarkaṃ dhyānam antaram` for grammatical agreement and standard sandhi.

The second half is compressed and prepares VAkK 8.23. The phrase `tridhā` begins the threefold classification completed in the next verse.

## Padaccheda

- aṣṭau
- sāmantakāni
- eṣām
- śuddha
- aduḥkhāsukhāni
- hi
- āryam
- ca
- ādyam
- tridhā
- kecit
- atarkam
- dhyānam
- antaram

## Grammar

- **aṣṭau** — nominative plural, “eight.”
- **sāmantakāni** — nominative plural neuter, “neighboring attainments” or “preparatory stages.”
- **eṣām** — genitive plural, “of these.”
- **śuddha** — nominative plural neuter in compound relation, “pure.”
- **aduḥkhāsukhāni** — nominative plural neuter, “neither-painful-nor-pleasant.”
- **āryam** — nominative singular neuter, “noble.”
- **ādyam** — nominative singular neuter, “the first.”
- **tridhā** — adverb, “threefold” or “in three ways.”
- **kecit** — “some [teachers].”
- **atarkam** — nominative singular neuter, “without vitarka.”
- **dhyānam antaram** — “the intermediate dhyāna.”

## Literal Translation

The eight neighboring attainments belonging to these are pure and neither-painful-nor-pleasant. The first is also noble. Some [teach] a threefold division; the intermediate dhyāna is without vitarka.

## Philosophical Translation

All eight neighboring attainments are pure and affectively neutral. The first neighboring attainment also has a noble form. The chapter then begins a final threefold classification of samādhi by the presence or absence of discursive factors: the intermediate dhyāna is free from vitarka, though the completion of the division is deferred to the following verse.

## Technical Vocabulary

- **sāmantaka** — neighboring attainment; preparatory stage contiguous with a fundamental attainment.
- **śuddha** — pure but still worldly.
- **aduḥkhāsukha** — neither painful nor pleasant; affective neutrality.
- **ārya** — noble; supramundane.
- **atarka** — without vitarka.
- **dhyānāntara** — intermediate dhyāna, situated between the first and second dhyānas.

## Doctrinal Determination

This verse gathers the doctrine of the neighboring attainments before the Samāpatti section closes.

1. There are eight neighboring attainments corresponding to the eight fundamental attainments.
2. They are pure rather than savoring-associated.
3. Their feeling-tone is neither-painful-nor-pleasant.
4. The first neighboring attainment additionally has a noble form.
5. The intermediate dhyāna is introduced as lacking vitarka.

The first neighboring attainment is exceptional because it can serve directly in the noble path. The intermediate dhyāna is also exceptional because it cannot be reduced simply to either the first or second dhyāna.

## Logical Determination

The verse performs two closing operations.

First, it completes the classification of the preparatory grounds:

```text
eight neighboring attainments
    → pure
    → affectively neutral

first neighboring attainment
    → additionally noble
```

Second, it begins the final division by discursive constitution:

```text
samādhi
    → with vitarka and vicāra
    → without vitarka but with vicāra
    → without both
```

Only the middle member is stated here. VAkK 8.23 supplies the outer members and thereby completes the division genetically.

## Organon Light

A complete system cannot merely list the states that exist. It must also specify the grounds of its intermediate forms.

The intermediate dhyāna is not an accidental hybrid. It is required by the gradual withdrawal of discursivity:

```text
vitarka and vicāra
    ↓ removal of vitarka
vicāra alone
    ↓ removal of vicāra
neither remains
```

This is a genuine transition because the middle stage exhibits the determinate ground by which the first passes into the higher samādhis.

## OWL++ Seed

```text
Class: NeighboringAttainment
Class: PureAttainment
Class: NobleAttainment
Class: AffectivelyNeutralAttainment
Class: IntermediateDhyana
Class: Vitarka
Class: Vicara

Axiom:
NeighboringAttainment SubClassOf PureAttainment

Axiom:
NeighboringAttainment SubClassOf AffectivelyNeutralAttainment

Axiom:
FirstNeighboringAttainment SubClassOf NobleAttainment

Axiom:
IntermediateDhyana hasFactor some Vicara

Axiom:
IntermediateDhyana hasFactor exactly 0 Vitarka
```

## Commit History

- Initial Sanskrit-first analysis of VAkK 8.22.
