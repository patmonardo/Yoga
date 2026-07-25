# VAK 6.06

## Sanskrit

### Devanāgarī

व्यपकर्षद्वयवतो नासन्तुष्टमहेच्छयोः ।
लब्धे भूयःस्पृहातुष्टिरलब्धेच्छा महेच्छता ॥ ६.६ ॥

### IAST

vyapakarṣa-dvayavato nāsantuṣṭa-mahecchayoḥ |
labdhe bhūyaḥ-spṛhātuṣṭir alabdhēcchā mahecchatā || 6.6 ||

## Padaccheda

| Pada | Form | Determination |
|---|---|---|
| vyapakarṣa-dvaya-vataḥ | genitive singular masculine | of one possessing the two separations |
| na | particle | not |
| asantuṣṭa-mahecchayoḥ | genitive dual | of the discontented person and the person of great desires |
| labdhe | locative singular | with respect to what has been obtained |
| bhūyaḥ-spṛhā | nominative singular feminine | desire for more |
| atuṣṭiḥ | nominative singular feminine | discontent |
| alabdhē | locative singular | with respect to what has not been obtained |
| icchā | nominative singular feminine | desire |
| mahecchatā | nominative singular feminine | great desire |

## Literal Translation

Cultivation belongs to one possessing the two separations, not to the discontented or greatly desirous. Desire for more of what has already been obtained is discontent; desire for what has not been obtained is great desire.

## Philosophical Translation

One who enters cultivation must possess the twofold separation; cultivation does not properly belong to one agitated by dissatisfaction or expansive desire. Dissatisfaction seeks an increase in what is already possessed, while great desire reaches toward possessions not yet acquired.

## Technical Vocabulary

### vyapakarṣa-dvaya

The two withdrawals are bodily and mental separation. Physical solitude without mental withdrawal is insufficient, while inward detachment without practical reorganization remains unstable.

### atuṣṭi

Discontent is desire for more of what is already possessed. Possession does not terminate desire but becomes the ground for quantitative increase.

### mahecchatā

Great desire is desire for what has not yet been obtained. It expands the field of possession into new objects.

## Analysis

VAK 6.05 established conduct, learning, reflection, and cultivation. VAK 6.06 adds the practical and affective conditions of cultivation: bodily withdrawal, mental withdrawal, freedom from discontent, and freedom from great desire.

The verse distinguishes two movements of desire:

```text
atuṣṭi
    more of what is possessed

mahecchatā
    acquisition of what is unpossessed
```

These form an endless cycle:

```text
unobtained
    → desired
    → obtained
    → desired in greater quantity
```

The Path must interrupt both the extensive and intensive expansion of desire.

## Logical Determination

Discontent is quantitative intensification within an existing object-class. Great desire is extensive expansion into new object-classes.

```text
more
    versus
other
```

The twofold withdrawal opposes this cycle externally and internally:

```text
kāya-vyapakarṣa
    removes immediate occasions

citta-vyapakarṣa
    removes their continuing representation
```

## Interpretive Note

The verse shows that bhāvanā requires a concrete reorganization of life. The practitioner begins to withdraw from the ordinary loka-structure of acquisition, comparison, and indefinite increase. This is the empirical and sannyāsa dimension of the trans-loka Path.

## Organon Note

```text
CultivationReadyPractitioner
    possesses BodilySeparation
    possesses MentalSeparation
    excludes Discontent
    excludes GreatDesire
```

## OWL++ Seed

```text
Class: Practitioner
Class: CultivationReadyPractitioner
Class: Separation
Class: BodilySeparation
Class: MentalSeparation
Class: Desire
Class: Discontent
Class: GreatDesire
Class: ObtainedObject
Class: UnobtainedObject

BodilySeparation SubClassOf Separation
MentalSeparation SubClassOf Separation
Discontent SubClassOf Desire
GreatDesire SubClassOf Desire

ObjectProperty: possessesSeparation
    Domain: Practitioner
    Range: Separation

ObjectProperty: desiresObject
    Domain: Desire
    Range: Object

CultivationReadyPractitioner SubClassOf
    possessesSeparation some BodilySeparation

CultivationReadyPractitioner SubClassOf
    possessesSeparation some MentalSeparation

Discontent SubClassOf
    desiresObject only ObtainedObject

GreatDesire SubClassOf
    desiresObject only UnobtainedObject
```

## Determinate Summary

```text
Cultivation requires:
    bodily separation
    mental separation
    freedom from discontent
    freedom from great desire

atuṣṭi
    desire for more of what is obtained

mahecchatā
    desire for what is not obtained
```
