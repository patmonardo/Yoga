# VAkK 4.45

## Sanskrit

### Devanāgarī

> क्षेमाक्षेमेतरत्कर्म कुशलाकुशलेतरत् ।  
> पुण्यापुण्यमनिञ्जं च सुखवेद्यादि च त्रयम् ॥ ४.४५ ॥

### IAST

> **kṣemākṣemetarat karma kuśalākuśaletarat |**  
> **puṇyāpuṇyam aniñjaṃ ca sukhavedyādi ca trayam || 4.45 ||**

## Padaccheda

```text
kṣema
akṣema
itarat
karma

kuśala
akuśala
itarat

puṇya
apuṇya
aniñjam
ca

sukha-vedya-ādi
ca
trayam
```

Expanded syntactically:

```text
karma
    kṣemam
    akṣemam
    itarat ca

karma
    kuśalam
    akuśalam
    itarat ca

karma
    puṇyam
    apuṇyam
    aniñjam ca

karma
    sukha-vedyādi
    trayam ca
```

## Literal translation

> **Karma is secure, insecure, or other; wholesome, unwholesome, or other; meritorious, demeritorious, or immovable; and threefold beginning with that which is to be experienced as pleasure.**

## Philosophical translation

> **Action admits of several distinct threefold classifications: according to whether it conduces to security, insecurity, or neither; according to whether it is wholesome, unwholesome, or ethically indeterminate; according to whether it is meritorious, demeritorious, or immovable; and according to whether its maturation is experienced as pleasure, pain, or neither.**

## Structural transition

Verses 4.13–4.44 concentrated on:

```text
vijñapti / avijñapti
restraint / non-restraint
acquisition
possession
loss
eligible bearer
generative domain
```

VAkK 4.45 opens a new movement from the form and persistence of action to its determinate character and maturation.

## Doctrinal determination

The verse announces four threefold divisions.

### 1. Kṣema, akṣema, and the other

```text
kṣema-karma
    action conducive to security or well-being

akṣema-karma
    action opposed to security or well-being

itarat-karma
    action falling under neither
```

This classification should not yet be collapsed into the immediately following kuśala triad. A provisional distinction is:

```text
kṣema / akṣema
    action considered through its tendency
    toward welfare or harm

kuśala / akuśala
    action considered through its ethical nature
```

The exact technical force remains for the Bhāṣya pass.

### 2. Kuśala, akuśala, and the other

```text
kuśala
    wholesome

akuśala
    unwholesome

avyākṛta
    indeterminate
```

The third member is expressed by **itarat**, “the other.” Indeterminate does not mean causally ineffective; it means not determined under the wholesome/unwholesome opposition.

### 3. Puṇya, apuṇya, and aniñja

```text
puṇya
    meritorious karma

apuṇya
    demeritorious karma

aniñja
    immovable karma
```

This classification is cosmological and result-oriented. VAkK 4.46 immediately explains its distribution by domain.

### 4. Pleasantly, painfully, or neutrally experienced

```text
sukha-vedya
    experienced as pleasure

duḥkha-vedya
    experienced as pain

aduḥkhāsukha-vedya
    experienced as neither
```

This concerns the feeling-character of karmic maturation, not necessarily the feeling present during the original action.

## Technical vocabulary

### kṣema

Security, safety, well-being, rest, preservation. Canonical first-pass rendering: **secure** or **conducive to security**.

### kuśala

Canonical rendering: **wholesome**.

### avyākṛta

Canonical rendering: **indeterminate**, preserving the sense “not distinctly determined” under the wholesome/unwholesome opposition.

### puṇya

Merit or meritorious action. It is not identical in all respects with kuśala.

### aniñja

Unmoving, unshaken, immovable. VAkK 4.46 explains the name through the fixity of maturation relative to domain.

### vedya

To be experienced or felt. Thus **sukhavedya karma** is karma whose maturation is experienced through pleasant feeling.

## Logical determination

```text
KARMA
    considered according to welfare-tendency
        → kṣema / akṣema / other

    considered according to ethical quality
        → kuśala / akuśala / indeterminate

    considered according to domain-fixed production
        → puṇya / apuṇya / aniñja

    considered according to felt maturation
        → pleasure / pain / neither
```

One substrate is divided according to multiple grounds:

```text
one substrate
    karma

multiple grounds of division
    tendency
    ethical quality
    cosmological efficacy
    experienced result
```

The verse does not create twelve unrelated entities. It gives four ways of dividing the field of karma.

## Logic of Experience

```text
[ KARMA
  WELFARE-STATUS
      kṣema | akṣema | other
  ETHICAL-STATUS
      kuśala | akuśala | avyākṛta
  DOMAIN-EFFICACY
      puṇya | apuṇya | aniñja
  FELT-MATURATION
      sukha | duḥkha | aduḥkhāsukha ]
```

Karma is not adequately represented by one moral label. A concrete act may require determinations of ethical quality, domain of production, fixity of maturation, temporal maturation, and feeling-result.

## Organon interpretation

```text
Form of action
    vijñapti / avijñapti

Persistence of action
    acquisition / possession / loss

Quality of action
    classifications beginning at 4.45

Result of action
    maturation and felt experience
```

This is the movement from:

```text
THAT karma is
    and how it persists
```

to:

```text
WHAT karma is
    as a determinate causal function
```

The central principle is:

```text
karma is one field
but it is divided according to
distinct grounds of determination
```

## OWL++ seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix karma: <http://127.0.0.1:3000/karma#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_45
    a vak:Karika ;
    rdfs:label "VAK 4.45" ;
    vak:continues vak:VAK_4_44 ;
    vak:opensSection karma:ClassificationOfKarma ;
    vak:hasTopic karma:WelfareClassification ;
    vak:hasTopic karma:EthicalClassification ;
    vak:hasTopic karma:DomainEfficacyClassification ;
    vak:hasTopic karma:FeltMaturationClassification .

karma:Karma
    karma:hasWelfareStatus karma:WelfareStatus ;
    karma:hasEthicalStatus karma:EthicalStatus ;
    karma:hasDomainEfficacy karma:DomainEfficacy ;
    karma:hasFeltMaturation karma:FeltMaturation .
```

## Determinate result

VAkK 4.45 establishes four distinct triadic classifications:

```text
secure / insecure / other
wholesome / unwholesome / indeterminate
meritorious / demeritorious / immovable
pleasantly experienced / painfully experienced / neutrally experienced
```

Its central logical result is:

```text
karma is not classified once

it is divided repeatedly
according to distinct grounds
of ethical and causal determination
```
