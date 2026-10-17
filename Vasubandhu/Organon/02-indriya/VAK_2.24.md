# VAK_2.24 — In Every Consciousness

## 1. Sanskrit (Devanāgarī)

> वेदना चेतना संज्ञा छन्दः स्पर्शो मतिः स्मृतिः ।
>
> मनस्कारोऽधिमोक्षश्च समाधिः सर्वचेतसि ॥ २.२४ ॥

## 2. Sanskrit (IAST)

> vedanā cetanā saṃjñā cchandaḥ sparśo matiḥ smṛtiḥ /
>
> manaskāro 'dhimokṣaś ca samādhiḥ sarvacetasi // 2.24 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| vedanā | nominative | feeling |
| cetanā | nominative | volition |
| saṃjñā | nominative | reflection |
| chandaḥ | nominative | wish to perform |
| sparśaḥ | nominative | contact |
| matiḥ | nominative | Discrimination |
| smṛtiḥ | nominative | mindfulness |
| manaskāraḥ | nominative | attention |
| adhimokṣaḥ | nominative | resolution |
| samādhiḥ | nominative | concentration |
| sarva-cetasi | locative | in every consciousness |

Mati is prajñā. Discrimination, not discernment. Smṛti is non-loss of the support. Samādhi is one-pointedness, not the perfected absorption.

## 4. Grammar

```text
% start S
S[GROUND=every-consciousness] -> Ten[PRESENT=together]
Ten -> Feeling | Volition | Reflection | Wish | Contact | Discrimination | Mindfulness | Attention | Resolution | Concentration
```

`GROUND=every-consciousness` forces co-presence of the ten.  
`kila` reports the claim; it does not by itself reject it.

## 5. Translation

### Literal Translation

Feeling, volition, reflection, wish to perform, contact, Discrimination, mindfulness, attention, resolution, and concentration, in every consciousness.

### Bhāṣya-informed study translation

> These ten are present together in every moment of consciousness. Feeling is experience, volition is mental action, reflection is take-up of the mark, contact is the touching born of faculty, meaning, and cognition, Discrimination is prajñā. The distinction of consciousness and factors is subtle, harder in moments than in streams.

## 6. Philosophical Translation

> Presence in every consciousness is not equal strength, not correctness, and not ethical quality. The ten co-occur; they do not become one.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| vedanā | feeling | three experiences, not together |
| cetanā | volition | cittābhisaṃskāra, mental action |
| saṃjñā | reflection | take-up of the mark; gloss damaged |
| chanda | wish to perform | kartṛkāmatā; not craving |
| sparśa | contact | faculty, viṣaya, cognition |
| mati | Discrimination | prajñā; not every discrimination correct |
| smṛti | mindfulness | non-loss of the support |
| manaskāra | attention | application of consciousness |
| adhimokṣa | resolution | adhimukti, settling upon |
| samādhi | concentration | one-pointedness |
| kila | it is said | reportive |

## 8. Logical Determination

```python
from nltk.sem.logic import LogicParser
lp = LogicParser()

ten = lp.parse(r'all c.(Consciousness(c) -> (Feeling(c) & Volition(c) & Reflection(c) & Contact(c) & Discrimination(c) & ...))')
not_strength = lp.parse(r'-all c x.(Present(c,x) -> EqualStrength(c,x))')
```

Presence is co-occurrence, not identity of strength or quality.  
The ground is every consciousness; the support is not the ground.

## 9. Interpretive Note

The question was left at 2.23. These are the great-ground factors because the ground is every consciousness. Not because they are exalted.

Volition and wish to perform are different. Reflection and Discrimination are different. The recognition-gloss is damaged. The distinction of the two entries does not depend on restoring it.

Contact is not confined to bodily touch. Viṣaya in that definition is not decided as an external thing by this sentence. Mindfulness is non-loss of the support, not only memory of a past event. The ground is every consciousness. That does not make every consciousness their common support.

The plant analogy is difficulty, not impossibility. The universal claim, the definitions, and the difficulty of seeing the differences stay apart. No rival list. No school named. Kila alone is not a rejection.

Organon reading: the ten are the first closure of the pair. Universal function is not universal adequacy. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_24
    a vak:Karika ;
    rdfs:label "VAK 2.24" ;
    vak:hasTopic vak:GreatGroundTen ;
    vak:belongsTo vak:Indriyanirdesa .

vak:GreatGroundTen vak:inEveryConsciousness true .
vak:Mati vak:is vak:Discrimination .

organon:PresenceNotAdequacy
    organon:notTheVerseEnglish true .
```
