# VAK_7.22 — Six or Seven Knowledges Cultivated

## Sanskrit

### Devanāgarī

```text
षोडशे षट् सरागस्य वीतरागस्य सप्त तु ।
सरागभावनामार्गे तदूर्ध्वं सप्तभावना ॥ ७.२२ ॥
```

### IAST

```text
ṣoḍaśe ṣaṭ sarāgasya vītarāgasya sapta tu /
sarāgabhāvanāmārge tadūrdhvaṃ saptabhāvanā // VAK_7.22 //
```

## Source Caution

The verb *bhāvyante*, “are cultivated,” is carried forward from VAK 7.20.

The verse gives two reckonings:

```text
at the sixteenth moment
    six knowledges are cultivated
    for one not detached from desire

    seven knowledges are cultivated
    for one already detached from desire

after the sixteenth moment
    in the Path of Cultivation
    while desire remains
    seven knowledges are cultivated
```

The sixteenth moment is the inferential knowledge of the Path and marks entry into the Path of Cultivation.

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| ṣoḍaśe | locative singular | at the sixteenth moment |
| ṣaṭ | numeral | six |
| sa-rāgasya | genitive singular | of one possessing desire; not detached |
| vīta-rāgasya | genitive singular | of one whose desire has departed; detached |
| sapta | numeral | seven |
| tu | particle | but; whereas |
| sa-rāga | adjective | accompanied by desire |
| bhāvanā-mārge | locative singular compound | in the Path of Cultivation |
| tad-ūrdhvam | adverbial compound | above that; after that |
| sapta-bhāvanā | nominal expression | cultivation of seven |

## Grammar

The first half is construed:

```text
ṣoḍaśe
    at the sixteenth moment

sarāgasya
    for one not detached from desire

ṣaṭ bhāvyante
    six knowledges are cultivated

vītarāgasya tu
    but for one detached from desire

sapta bhāvyante
    seven are cultivated
```

The second half is construed:

```text
tadūrdhvam
    after the sixteenth moment

sarāga-bhāvanā-mārge
    in the Path of Cultivation
    while desire remains

sapta-bhāvanā
    there is cultivation of seven knowledges
```

## Literal Translation

At the sixteenth moment, six knowledges are cultivated by one possessing desire, but seven by one detached from desire. Above that, in the Path of Cultivation while desire remains, there is cultivation of seven knowledges.

## Philosophical Translation

At the final moment of the Path of Seeing, the number of knowledges cultivated depends upon whether the practitioner has already become detached from the desire-domain. The undetached practitioner cultivates six; the detached practitioner cultivates seven by adding knowledge of another mind. Thereafter, throughout the desire-associated Path of Cultivation, seven knowledges are cultivated.

## Technical Vocabulary

### ṣoḍaśa-kṣaṇa

```text
sixteenth moment
    inferential knowledge of the Path
    final moment of the Path of Seeing
    first moment belonging to the Path of Cultivation
```

The moment stands at the transition between Seeing and Cultivation.

### sarāga

```text
sa-rāga
    possessing desire
    not yet detached from the desire-domain
```

This is a technical path-status, not simply the occurrence of a presently manifest desire.

### vītarāga

```text
vīta-rāga
    desire departed
    already detached from the desire-domain
```

Prior detachment permits the additional cultivation of knowledge of another mind.

### bhāvanā-mārga

```text
bhāvanā-mārga
    Path of Cultivation
```

The truths already seen are now repeatedly developed through the removal of the afflictions abandoned by cultivation.

### sapta-bhāvanā

The seven cultivated knowledges after the sixteenth moment are:

```text
knowledge of dharmas
inferential knowledge
knowledge of suffering
knowledge of origin
knowledge of cessation
knowledge of the Path
conventional knowledge
```

At the sixteenth moment for the detached practitioner, the seventh is instead knowledge of another mind.

## Doctrinal Determination

### At the sixteenth moment

For one not detached from the desire-domain, six future knowledges are cultivated:

```text
dharma-jñāna
anvaya-jñāna
duḥkha-jñāna
samudaya-jñāna
nirodha-jñāna
mārga-jñāna
```

Two knowledges are actual in the present moment:

```text
knowledge of the Path
inferential knowledge of the Path
```

The verse, however, is principally counting the knowledges cultivated for the future.

### The detached practitioner

For one already detached from the desire-domain:

```text
the same six
    +
knowledge of another mind
```

Hence seven are cultivated.

### After the sixteenth moment

Once the practitioner has entered the continuing Path of Cultivation, while desire has not yet been abandoned, seven knowledges are cultivated:

```text
the six pure knowledges
    +
conventional knowledge
```

The present cognition varies according to whether the path being practiced is worldly or transworldly, but the verse gives the future cultivation count.

## Logical Determination

VAK 7.22 distinguishes cultivation according to two conditions:

```text
path-moment
    sixteenth moment
    or later Path of Cultivation

state of detachment
    desire remaining
    or desire already abandoned
```

The number cultivated is therefore not fixed merely by the name of the path. It depends upon the practitioner's attained condition.

```text
same path-moment
    + different prior attainment
        = different cultivation range
```

The verse continues the precise accounting begun in VAK 7.19–7.21.

## Organon Light

```text
cultivation is conditioned by
    what has already been attained
    and
    where the practitioner now stands
```

Knowledge develops within a determinate path-history.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix marga: <http://127.0.0.1:3000/marga#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_7_22
    a vak:Karika ;
    rdfs:label "VAK 7.22" ;
    vak:determines jna:SixteenthMomentCultivation,
                   jna:DetachmentConditionedCultivation,
                   jna:SevenfoldCultivationInMeditationPath .

jna:SixteenthMomentCultivation
    a jna:CultivationCount ;
    marga:occursAt marga:SixteenthSeeingMoment ;
    jna:countForUndetached 6 ;
    jna:countForDetached 7 .

jna:SevenfoldCultivationInMeditationPath
    a jna:CultivationCount ;
    marga:occursIn marga:PathOfCultivation ;
    jna:count 7 .
```

## Commit History

```text
2026-07-23 — Initial kārikā-pass analysis for VAK_7b.
```
