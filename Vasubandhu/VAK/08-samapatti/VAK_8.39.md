# VAK_8.39

## Sanskrit

सद्धर्मो द्विविधः शास्तुरागमाधिगमात्मकः ।
धातारस्तस्य वक्तारः प्रतिपत्तार एव च ॥

## IAST

saddharmo dvividhaḥ śāstur āgamādhigamātmakaḥ /
dhātāras tasya vaktāraḥ pratipattāra eva ca //

## Padaccheda

sat-dharmaḥ | dvi-vidhaḥ | śāstuḥ | āgama-adhigama-ātmakaḥ | dhātāraḥ | tasya | vaktāraḥ | pratipattāraḥ | eva | ca

## Literal Translation

The True Dharma of the Teacher is twofold, consisting of scripture and realization. Its bearers are those who teach it and those who practice it.

## Philosophical Translation

The Teacher's True Dharma has two forms: transmitted doctrine and achieved realization. It is preserved by those who speak the teaching and by those who actually enter and embody its practice.

## Technical Vocabulary

- **saddharma** — True Dharma; the authentic teaching as transmitted and realized
- **śāstṛ** — Teacher; here the Buddha
- **āgama** — transmitted teaching, scripture, authoritative doctrine
- **adhigama** — realization, attainment, direct acquisition of the teaching's truth
- **dhātṛ** — bearer, preserver, supporter
- **vaktṛ** — speaker, teacher, expounder
- **pratipattṛ** — practitioner; one who enters upon and realizes the path

## Doctrinal Determination

The Dharma survives in two inseparable modes:

1. **Āgama** — the Dharma as taught, remembered, studied, and explained.
2. **Adhigama** — the Dharma as practiced, attained, and realized.

Accordingly, its bearers are likewise twofold: teachers preserve its articulation, while practitioners preserve its actuality.

## Logical Determination

The verse refuses to identify the Dharma with text alone or with private attainment alone. Doctrine without realization becomes empty transmission; realization without transmission loses its communicable form.

## Organon Interpretation

This is a clean unity of objective and subjective actuality:

- **Āgama** gives the articulated universal form of the Dharma.
- **Adhigama** gives its realized singular actuality.

The True Dharma exists only where these remain joined through living bearers.

## OWL++ Seed

```turtle
@prefix vak: <https://example.org/vak#> .

vak:Saddharma a vak:TwofoldDharma ;
    vak:hasMode vak:Agama , vak:Adhigama .

vak:Agama a vak:TransmittedTeaching .
vak:Adhigama a vak:RealizedAttainment .

vak:TeacherBearer a vak:DharmaBearer ;
    vak:bears vak:Agama .

vak:PractitionerBearer a vak:DharmaBearer ;
    vak:bears vak:Adhigama .
```

## Commit History

- First-pass Sanskrit, translation, and light doctrinal analysis committed verse by verse.
