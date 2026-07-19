# VAK 6.21

## Sanskrit

### Devanāgarī

कामाश्रयाण्यग्रधर्मान् द्वयाश्रयान् लभतेऽङ्गना ।
भूमित्यागात्त्यजत्यार्यस्तान्यनार्यस्तु मृत्युनाः ॥ ६.२१ ॥

### IAST

**kāmāśrayāṇy agradharmān dvayāśrayān labhate ’ṅganā |**  
**bhūmityāgāt tyajaty āryas tāny anāryas tu mṛtyunā || 6.21 ||**

## Padaccheda

- kāma-āśrayāṇi
- agra-dharmān
- dvaya-āśrayān
- labhate
- aṅganā
- bhūmi-tyāgāt
- tyajati
- āryaḥ
- tāni
- anāryaḥ tu
- mṛtyunā

## Grammar

- **kāma-āśrayāṇi** — nominative plural neuter, agreeing with the four *nirvedhabhāgīyāni* understood from VAK 6.20: “having the desire-domain as their support.”
- **agra-dharmān** — accusative plural masculine: “the Highest Mundane Dharmas.”
- **dvaya-āśrayān** — accusative plural masculine agreeing with *agradharmān*: “having the two supports.”
- **labhate** — third-person singular middle present of √*labh*: “obtains.”
- **aṅganā** — nominative singular feminine: “a woman.”
- **bhūmi-tyāgāt** — ablative singular compound: “through abandoning the level.”
- **tyajati** — third-person singular active present of √*tyaj*: “abandons” or “loses.”
- **āryaḥ** — nominative singular masculine: “the Noble one.”
- **tāni** — accusative plural neuter: “those,” referring to the four preparations.
- **anāryaḥ tu** — “but the non-Noble” or ordinary person.
- **mṛtyunā** — instrumental singular: “through death.”

## Literal Translation

The preparations have the desire-domain as their support. A woman obtains Highest Mundane Dharmas supported by both bases. A Noble one loses them through abandoning their level, but a non-Noble through death.

## Philosophical Translation

Although the preparations for penetration arise upon concentration-levels, they are supported by a being belonging to the desire-domain. At the stage of the Highest Mundane Dharmas, a woman may possess them in relation to either the female or male bodily support. A Noble one relinquishes them only by leaving the concentration-level upon which they depend, whereas an ordinary person relinquishes them with the termination of that life.

## Doctrinal Determination

The verse distinguishes the bodily support (*āśraya*) from the concentration-level (*bhūmi*). The four preparations depend upon a desire-domain bodily existence even when their cognitive ground belongs to a form-domain concentration.

At the Highest Mundane Dharmas, the text differentiates the possible bodily supports. A woman may obtain them in relation to either female or male support; the classification concerns the support under which the preparation may be acquired.

Loss also differs according to practitioner-status:

- a Noble practitioner loses the preparations through abandonment of their concentration-level;
- an ordinary practitioner loses them through death, that is, through termination of the present life-continuum.

The verse therefore classifies the preparations by bodily support, possible sex-support, and mode of loss.

## Logical Determination

```text
PreparationsForPenetration {
    bodilySupport: DesireDomain
}

HighestMundaneDharmas {
    femalePractitionerMayAcquireOn: [
        FemaleSupport,
        MaleSupport
    ]
}

NoblePractitioner {
    losesPreparationsThrough:
        AbandonmentOfLevel
}

OrdinaryPractitioner {
    losesPreparationsThrough:
        Death
}
```

## OWL++ Seed

```text
Class: DesireDomainSupport
Class: FemaleSupport
Class: MaleSupport
Class: NoblePractitioner
Class: OrdinaryPractitioner
Class: AbandonmentOfLevel
Class: Death

ObjectProperty: hasBodilySupport
ObjectProperty: mayBeAcquiredOnSupport
ObjectProperty: losesThrough

Nirvedhabhagiya
    hasBodilySupport only DesireDomainSupport

HighestMundaneDharmas
    mayBeAcquiredOnSupport FemaleSupport

HighestMundaneDharmas
    mayBeAcquiredOnSupport MaleSupport

NoblePractitioner
    losesThrough only AbandonmentOfLevel

OrdinaryPractitioner
    losesThrough only Death
```

## Determinate Summary

All four preparations depend upon a desire-domain bodily support. At the Highest Mundane Dharmas, a woman may obtain them with either bodily support. A Noble practitioner loses the preparations through abandoning their level; an ordinary practitioner loses them through death.