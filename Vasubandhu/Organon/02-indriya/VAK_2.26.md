# VAK_2.26 — Always in the Afflicted

## 1. Sanskrit (Devanāgarī)

```sanskrit
मोहः प्रमादः कौशीद्यमाश्रद्ध्यं स्त्यानमौद्धत्यम् ।
क्लिष्टे सदैवाकुशले त्वाह्रीक्यमनपत्रपा ॥ २.२६ ॥
```

## 2. Sanskrit (IAST)

```text
mohaḥ pramādaḥ kauśīdyam āśraddhyaṃ styānam auddhatyam /
kliṣṭe sadaivākuśale tv āhrīkyam anapatrapā // 2.26 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| mohaḥ | nom. sg. m. | delusion |
| pramādaḥ | nom. sg. m. | heedlessness |
| kauśīdyam | nom. sg. n. | laziness |
| āśraddhyam | nom. sg. n. | lack of faith |
| styānam | nom. sg. n. | sluggishness |
| auddhatyam | nom. sg. n. | agitation |
| kliṣṭe sadā eva | loc. sg. n. + adverbs | always in the afflicted |
| akuśale tu | loc. sg. n. + particle | but in the unwholesome |
| āhrīkyam | nom. sg. n. | shamelessness |
| anapatrapā | nom. sg. f. | lack of moral caution |

Afflicted and unwholesome are not the same range.
## 4. Grammar

```text
% start S
S[GROUND=afflicted] -> Six[PRESENT=always, ONLY=true]
Six -> Delusion | Heedlessness | Laziness | LackOfFaith | Sluggishness | Agitation
S[GROUND=unwholesome] -> Six + Shamelessness + LackOfCaution
```

`GROUND=afflicted` is exclusive.  
The ten-recitation includes afflicted modes of the universal ten; they are not a second class.

## 5. Translation

### Literal Translation

> Delusion, heedlessness, laziness, lack of faith, sluggishness, and
> agitation are always present in the afflicted. But shamelessness and lack
> of moral caution are always present in the unwholesome.
### Bhāṣya-informed study translation

> Delusion, heedlessness, laziness, lack of faith, sluggishness, and
> agitation are always present in afflicted consciousness; shamelessness and
> lack of moral caution are present in unwholesome consciousness.
## 6. Philosophical Translation

> Afflicted ground is exclusive. The six are not the ten. Afflicted modes of the universal factors remain universal. Predominance names; it does not split the pair.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| kleśa-mahābhūmika | affliction great-ground | always, only in the afflicted |
| moha | delusion | avidyā |
| pramāda | heedlessness | opposed to heedfulness |
| kauśīdya | laziness | opposed to vigor |
| āśraddhya | lack of faith | opposed to faith |
| styāna | sluggishness | heaviness, unworkability |
| auddhatya | agitation | non-pacification |
| muṣita-smṛtitā | lost recollection | mindfulness afflicted |
| vikṣepa | distraction | concentration afflicted; disputed |
| akuśala-mahābhūmika | unwholesome great-ground | the two; narrower |

## 8. Logical Determination

```python
from nltk.sem.logic import LogicParser
lp = LogicParser()

afflicted = lp.parse(r'all c.(Afflicted(c) -> (Delusion(c) & Heedlessness(c) & Laziness(c) & LackOfFaith(c) & Sluggishness(c) & Agitation(c)))')
unwholesome = lp.parse(r'all c.(Unwholesome(c) -> (Afflicted(c) & Shamelessness(c) & LackOfCaution(c)))')
```

The six are exclusive to afflicted consciousness.  
The unwholesome adds the pair.  
Afflicted modes of universal factors remain universal.
## 9. Interpretive Note

**Translation note.** The commentary identifies delusion with ignorance; heedlessness with failure to cultivate wholesome dharmas; laziness with lack of energetic arousal; lack of faith with lack of clarity; sluggishness with unworkability of body and consciousness; and agitation with non-pacification of consciousness. It discusses whether the first group is only afflicted and records a damaged retort, a recitation example, and a bodily-sluggishness analogy.

Five of the ten are kept as the separately counted afflicted factors, with sluggishness added to make six. The other five are modes. And so on completes them: lack of clear comprehension is Discrimination afflicted, improper attention is attention afflicted, false resolution is resolution afflicted. Not extra definitions spelled out here.

The first alternative does not say feeling cannot occur in afflicted consciousness. It is classification in the comparison. Sluggishness is not silently added to the second row. Its omission is the next question.

The retort is damaged. Recitation against intention is the contrast. Not a restored first compound. Bodily sluggishness is the feeling analogy, not expanded, and not sleep.

Organon reading: a label is not the state. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_26
    a vak:Karika ;
    rdfs:label "VAK 2.26" ;
    vak:hasTopic vak:AfflictedGround ;
    vak:belongsTo vak:Indriyanirdesa .

vak:AfflictedSix vak:onlyInAfflictedConsciousness true .
vak:UnwholesomeTwo vak:inEveryUnwholesomeConsciousness true .

organon:ModeNotNewFactor
    organon:notTheVerseEnglish true .
```
