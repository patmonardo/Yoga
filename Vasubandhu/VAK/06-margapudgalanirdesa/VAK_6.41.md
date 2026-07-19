# VAK 6.41

## Sanskrit

### Devanāgarī

न परावृत्तजन्मार्यः कामे धात्वन्तरोपगः ।  
स चोर्ध्वजश्च नैवाक्षसञ्चारपरिहाणिभाक् ॥ ६.४१ ॥

### IAST

**na parāvṛtta-janmāryaḥ kāme dhātv-antaropagaḥ |**  
**sa cordhva-jaś ca naivākṣa-saṃcāra-parihāṇi-bhāk || 6.41 ||**

## Source Caution

The verse states restrictions governing the noble practitioner who has passed into another realm. It is compact but structurally clear:

```text
having entered another realm:
    no renewed birth in the desire realm

born above:
    no transfer of faculties
    no falling away
```

The exact scope of **akṣa-saṃcāra** and **parihāṇi** should be checked against the Bhāṣya.

## Padaccheda

```text
na
parāvṛtta-janmā
āryaḥ
kāme
dhātu-antara-upagaḥ

saḥ
ca
ūrdhva-jaḥ
ca
na eva
akṣa-saṃcāra-parihāṇi-bhāk
```

## Grammar

- **na** — “not.”
- **parāvṛtta-janmā** — nominative singular masculine compound: “one whose birth has turned back” or “one undergoing a returning birth.”
- **āryaḥ** — nominative singular masculine: “the noble one.”
- **kāme** — locative singular: “in the desire realm.”
- **dhātu-antara-upagaḥ** — nominative singular masculine: “one who has gone to another realm.”
- **saḥ** — nominative singular masculine: “he.”
- **ūrdhva-jaḥ** — nominative singular masculine: “one born above.”
- **na eva** — emphatic negation: “certainly not.”
- **akṣa-saṃcāra-parihāṇi-bhāk** — nominative singular masculine compound: “one who undergoes transfer of faculties or falling away.”

## Literal Translation

The noble one who has entered another realm does not undergo a returning birth in the desire realm. Nor does one born above undergo transfer of faculties or falling away.

## Philosophical Translation

Once a noble practitioner has passed from the desire realm into another realm, that course does not reverse into renewed birth in the desire realm. Likewise, one born in the higher realms is not subject there to a transfer of faculties or to regression from the attained condition.

## Technical Determination

```text
NobleRealmTransition {
    condition:
        EnteredAnotherRealm

    excludes:
        ReturnBirthInDesireRealm
}

HigherBornNoble {
    excludes:
        FacultyTransfer
        FallingAway
}
```

## Logical Determination

The verse limits the possible transitions in the practitioner-schema:

```text
higher-realm transition
    is not reversible into desire-realm rebirth

higher birth
    excludes specified regressions
```

It therefore supplements the preceding classifications with transition constraints.

## OWL++ Seed

```text
Class: NoblePractitioner
Class: HigherRealmPractitioner
Class: DesireRealmRebirth
Class: FacultyTransfer
Class: FallingAway

ObjectProperty: entersRealm
ObjectProperty: excludesTransition
ObjectProperty: subjectTo

HigherRealmPractitioner
    excludesTransition DesireRealmRebirth

HigherRealmPractitioner
    excludesTransition FacultyTransfer

HigherRealmPractitioner
    excludesTransition FallingAway
```

## Determinate Summary

```text
A noble practitioner who has entered another realm:
    does not return to birth in the desire realm.

One born above:
    does not undergo transfer of faculties
    and does not fall away.
```

The Bhāṣya pass should determine the exact technical extent of these exclusions.