# VAK 6.71

## Sanskrit

अनास्रवाणि बोध्यङ्गमार्गाङ्गानि द्विधेतरे ।
सकलाः प्रथमे ध्याने अनागम्ये प्रीतिवर्जिताः ॥

*anāsravāṇi bodhyaṅga-mārgāṅgāni dvidhetare /*
*sakalāḥ prathame dhyāne anāgamye prīti-varjitāḥ //*

## Padaccheda

- *anāsravāṇi* — without outflows; pure
- *bodhyaṅgāni* — factors of Bodhi
- *mārgāṅgāni* — factors of the Path
- *dvidhā* — in two modes
- *itare* — the others
- *sakalāḥ* — complete; all present
- *prathame dhyāne* — in the first dhyāna
- *anāgamye* — in the preliminary ground
- *prīti-varjitāḥ* — without joy

## Literal Translation

The factors of Bodhi and the factors of the Path are without outflows. The others are of both kinds. All are present in the first dhyāna; in the preliminary ground they are without joy.

## Philosophical Translation

The seven Bodhi factors and the eight Path factors are exclusively pure. The other five groups may occur either with or without outflows. The complete bodhipakṣya system can occur in the first dhyāna; in the preliminary ground all are present except joy.

## Purity Status

The verse distinguishes:

```text
bodhyaṅga
mārgāṅga
    exclusively anāsrava
```

The other five groups are twofold:

```text
smṛtyupasthāna
samyakprahāṇa
ṛddhipāda
indriya
bala

    sāsrava or anāsrava
```

The same named Path-factor can therefore occur in mundane preparation or in noble cultivation.

## Ground Distribution

```text
first dhyāna
    complete bodhipakṣya field

anāgamya
    all except prīti
```

The first dhyāna supplies a complete contemplative basis. The preliminary ground supports the system without the joy factor.

## Doctrinal Determination

Purity-status and contemplative ground are separate determinations:

```text
what status a factor has
    sāsrava / anāsrava

where it can occur
    contemplative ground
```

Functional identity does not by itself determine either purity or distribution.

## Organon Lite

```text
BodhipakshyaFactor
    hasPurityStatus
    occursInGround

Bodhyanga
    hasPurityStatus Anasrava

Marganga
    hasPurityStatus Anasrava

Priti
    occursIn FirstDhyana
    notOccursIn Anagamya
```

## OWL++ Seed

```turtle
@prefix bodhi: <http://127.0.0.1:3000/bodhi#> .

bodhi:Bodhyanga
    bodhi:hasPurityStatus bodhi:Anasrava .

bodhi:Marganga
    bodhi:hasPurityStatus bodhi:Anasrava .

bodhi:OtherFiveGroups
    bodhi:mayHavePurityStatus bodhi:Sasrava ;
    bodhi:mayHavePurityStatus bodhi:Anasrava .

bodhi:FirstDhyana
    bodhi:supports bodhi:CompleteBodhipakshyaSystem .

bodhi:Anagamya
    bodhi:supports bodhi:BodhipakshyaWithoutPriti .
```

## Determinate Summary

VAK 6.71 classifies the Bodhi factors and Path factors as exclusively pure, while the other five bodhipakṣya groups may be mundane or pure. It then locates the complete system in the first dhyāna and excludes joy from the preliminary ground.