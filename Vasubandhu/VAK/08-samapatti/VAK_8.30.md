# VAK_8.30

## Sanskrit

उपेक्षालोभः आकारः सुखिता दुःखिता वत ।
मोदन्तामिति सत्त्वाश्च कामसत्त्वास्तु गोचरः ॥

## IAST

upekṣālobhaḥ ākāraḥ sukhitā duḥkhitā vata /
modantām iti sattvāś ca kāmasattvās tu gocaraḥ //

## Padaccheda

upekṣā | alobhaḥ | ākāraḥ | sukhitāḥ | duḥkhitāḥ | vata | modantām | iti | sattvāḥ | ca | kāma-sattvāḥ | tu | gocaraḥ

## Grammar

- **upekṣā alobhaḥ** — equanimity is non-greed / non-attachment
- **ākāraḥ** — the cognitive aspect or mode
- **sukhitāḥ** — “may they be happy”
- **duḥkhitāḥ vata** — “alas, they are suffering”
- **modantām** — “may they rejoice”
- **iti** — thus; marking the contemplative formulations
- **sattvāḥ** — beings
- **kāma-sattvāḥ tu gocaraḥ** — beings of the desire realm are the object-field

## Literal Translation

Equanimity is non-greed. Their modes are: “May beings be happy,” “Alas, they are suffering,” and “May they rejoice.” Beings of the desire realm are their object-field.

## Philosophical Translation

The four immeasurables take determinate relational form. Friendliness wills happiness, compassion recognizes suffering, sympathetic joy affirms flourishing, and equanimity is non-appropriation. Their field is the community of beings situated in desire.

## Technical Vocabulary

- **upekṣā** — equanimity
- **alobha** — non-greed; non-appropriation
- **ākāra** — cognitive aspect / determinate mode
- **sukhita** — happy; flourishing
- **duḥkhita** — suffering
- **muditā** — sympathetic joy
- **sattva** — sentient being
- **gocara** — object-field
- **kāmasattva** — being of the desire realm

## Doctrinal Determination

The verse assigns the immeasurables their specific modes. Maitrī takes the form “May beings be happy.” Karuṇā responds to beings as suffering. Muditā takes the form “May they rejoice.” Upekṣā is constituted by alobha, non-greed or non-appropriation.

The object-field is not an abstract infinity. It is the field of desire-realm beings, where attachment, aversion, suffering, and partiality actually operate.

## Logical Determination

The immeasurables are universal modes of relation, but their universality is concrete. Each one negates a finite distortion of relation:

- maitrī negates ill will
- karuṇā negates cruelty
- muditā negates resentment toward another's flourishing
- upekṣā negates appropriation and possessive partiality

Their immeasurability lies not in numerical extension alone, but in relation freed from finite preference and exclusion.

## Organon Interpretation

This is the first clear appearance of what may be called Buddha-Mind as a universal relational field. It is not a private exalted state and not a feature-model of beings. It is Reason taking beings as a whole under modes adequate to freedom.

Upekṣā as alobha is especially decisive. Equanimity is not indifference. It is relation without appropriation. The other is neither seized as mine nor rejected as alien.

The sequence may be read provisionally as:

```text
maitrī
    affirmation of happiness

karuṇā
    recognition of suffering

muditā
    affirmation of flourishing

upekṣā
    universality without appropriation
```

This is not yet a forced triad. It is a fourfold articulation of unrestricted practical Recognition.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix apramana: <http://127.0.0.1:3000/apramana#> .
@prefix citta: <http://127.0.0.1:3000/citta#> .
@prefix realm: <http://127.0.0.1:3000/realm#> .

vak:VAK_8_30
    a vak:Karika ;
    vak:specifies apramana:FourImmeasurables ;
    vak:assignsObjectField realm:DesireRealmBeings .

apramana:Maitri
    apramana:hasMode apramana:MayBeingsBeHappy .

apramana:Karuna
    apramana:hasMode apramana:RecognitionOfSuffering .

apramana:Mudita
    apramana:hasMode apramana:MayBeingsRejoice .

apramana:Upeksa
    apramana:hasConstitution citta:NonAppropriation .

citta:NonAppropriation
    rdfs:subClassOf citta:Alobha .
```

## Commit History

First-pass Kārikā analysis committed after discussion.