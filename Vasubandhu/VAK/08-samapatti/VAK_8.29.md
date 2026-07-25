# VAK_8.29

## Sanskrit

अप्रमाणानि चत्वारि व्यापादादिविपक्षतः ।
मैत्र्यद्वेषोऽपि करुणा मुदिता सुमनस्कता ॥

## IAST

apramāṇāni catvāri vyāpādādivipakṣataḥ /
maitry adveṣo 'pi karuṇā muditā sumanaskatā //

## Padaccheda

apramāṇāni | catvāri | vyāpāda-ādi-vipakṣataḥ | maitrī | adveṣaḥ | api | karuṇā | muditā | su-manaskatā

## Grammar

- **apramāṇāni catvāri** — the four immeasurables
- **vyāpāda-ādi-vipakṣataḥ** — because they are counterforces to ill will and the remaining afflictive tendencies
- **maitrī** — friendliness / loving-kindness
- **adveṣaḥ** — non-hatred; the mental factor constituting maitrī
- **karuṇā** — compassion
- **muditā** — sympathetic joy
- **sumanaskatā** — gladness or positive mental feeling

## Literal Translation

There are four immeasurables, because they counter ill will and the other afflictive tendencies. Friendliness is non-hatred; compassion and sympathetic joy are forms of gladness.

## Philosophical Translation

The four immeasurables universalize the yogin's relation to living beings by opposing the affective distortions that contract that relation. Friendliness is the active absence of hatred. Compassion and sympathetic joy transform the mental field through responsive gladness rather than through detached representation.

## Technical Vocabulary

- **apramāṇa** — immeasurable; an unrestricted contemplative relation to beings
- **vyāpāda** — ill will, hostility
- **vipakṣa** — counterforce / opposing factor
- **maitrī** — friendliness; loving-kindness
- **adveṣa** — non-hatred
- **karuṇā** — compassion
- **muditā** — sympathetic joy
- **sumanaskatā** — gladness; positive mental feeling

## Doctrinal Determination

The verse begins the analysis of the four immeasurables. They are defined first by their counteractive function: each opposes a specific distortion in the affective relation to beings. Maitrī is identified with non-hatred. Karuṇā and muditā are identified with gladness as their immediate mental basis. Upekṣā and the specific intentional forms of all four are completed in the following verse.

## Logical Determination

The immeasurable is not an indefinitely large object. It is a relation whose scope is not restricted by preference, aversion, possession, or exclusion.

The verse therefore moves from the intensive cultivation of Recognition to its extensive universality:

```text
Recognition freed in itself
    →
Recognition universalized toward beings
```

Maitrī is not a descriptive feature attributed to beings. It is the universal form of relation in which hatred no longer determines the field.

## Organon Interpretation

The four immeasurables belong to the incarnation of a higher Idea in the relational field. They are not themselves transcendental. They are concrete modes through which liberated Recognition becomes universally directed toward living beings.

The first determination is especially clear:

```text
maitrī
    =
adveṣa
```

Friendliness is not sentiment added to an otherwise neutral cognition. It is cognition whose relation to its object is no longer organized by negating hostility.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix apramana: <http://127.0.0.1:3000/apramana#> .
@prefix citta: <http://127.0.0.1:3000/citta#> .
@prefix klesa: <http://127.0.0.1:3000/klesa#> .

vak:VAK_8_29
    a vak:Karika ;
    vak:introduces apramana:FourImmeasurables .

apramana:FourImmeasurables
    apramana:counteracts klesa:HostilityAndRelatedDistortions .

apramana:Maitri
    apramana:hasMentalBasis citta:NonHatred .

apramana:Karuna
    apramana:hasMentalBasis citta:Gladness .

apramana:Mudita
    apramana:hasMentalBasis citta:Gladness .
```

## Commit History

First-pass Kārikā analysis committed after discussion.