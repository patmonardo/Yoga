# VAK_2.25 — Always in the Wholesome

## 1. Sanskrit (Devanāgarī)

```sanskrit
श्रद्धाप्रमादः प्रश्रब्धिरुपेक्षा ह्रीरपत्रपा ।
मूलद्वयमहिंसा च वीर्यं च कुशले सदा ॥ २.२५ ॥
```

## 2. Sanskrit (IAST)

```text
śraddhāpramādaḥ praśrabdhir upekṣā hrīr apatrapā /
mūladvayam ahiṃsā ca vīryaṃ ca kuśale sadā // 2.25 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| śraddhā | nom. sg. f. | faith |
| apramādaḥ | nom. sg. m. | heedfulness |
| praśrabdhiḥ | nom. sg. f. | pliancy |
| upekṣā | nom. sg. f. | equanimity; not neutral feeling |
| hrīḥ | nom. sg. f. | moral shame; explained later |
| apatrapā | nom. sg. f. | moral caution; explained later |
| mūla-dvayam | nom. sg. n.; numeral compound | two roots: non-greed, non-hatred |
| ahiṃsā | nom. sg. f. | non-harming |
| vīryam | nom. sg. n. | vigor |
| kuśale sadā | loc. sg. n. + adverb | always in the wholesome |

Ten, counting the two roots separately. Non-delusion is prajñā, already in the universal ten. Not counted again.
## 4. Grammar

```text
% start S
S[GROUND=wholesome] -> TenWholesome[PRESENT=always]
TenWholesome -> Faith | Heedfulness | Pliancy | Equanimity | Shame | Caution | NonGreed | NonHatred | NonHarming | Vigor
```

`GROUND=wholesome` is narrower than every-consciousness.  
The universal ten of 2.24 remain. Non-delusion is already prajñā and is not a second member.

## 5. Translation

### Literal Translation

> Faith, heedfulness, pliancy, equanimity, moral shame and moral caution,
> the two roots, non-harming, and vigor are always present in the wholesome.
### Bhāṣya-informed study translation

> Faith, heedfulness, pliancy, equanimity, moral shame and moral caution,
> the two roots, non-harming, and vigor are always present in wholesome
> consciousness.
## 6. Philosophical Translation

> The wholesome ground is narrower than every consciousness. Non-delusion is not a second member. Equanimity and attention are not opposed in nature; the distinction is of respect.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| kuśala-mahābhūmika | wholesome great-ground | every wholesome consciousness |
| śraddhā | faith | clarity; others: conviction |
| apramāda | heedfulness | attentive care; another school: guarding |
| praśrabdhi | pliancy | workability of consciousness |
| upekṣā | equanimity | evenness, non-application; not neutral feeling |
| alobha, adveṣa | non-greed, non-hatred | the two roots counted |
| amoha | non-delusion | prajñā; not counted again |
| ahiṃsā | non-harming | non-injury |
| vīrya | vigor | arousal of consciousness |
| bodhyaṅgānukūlya | favorable to an awakening factor | why the body receives the name |

## 8. Logical Determination

```python
from nltk.sem.logic import LogicParser
lp = LogicParser()

wholesome = lp.parse(r'all c.(Wholesome(c) -> (Faith(c) & Heedfulness(c) & Pliancy(c) & Equanimity(c) & NonGreed(c) & NonHatred(c) & ...))')
nondelusion = lp.parse(r'NonDelusion(x) <-> Prajna(x)')
```

The wholesome ten co-occur with the universal ten.  
Non-delusion is already prajñā.  
Name by favor is not nature.tention and equanimity
    application and non-application
    one support not settled
```

## 9. Interpretive Note

**Translation note.** The commentary explains faith as clarity; heedfulness as cultivation of the wholesome; pliancy as workability; and equanimity as evenness. The two roots are non-greed and non-hatred. Non-delusion is prajñā, already included among the great-ground factors. It also distinguishes a name assigned by favor from a factor's nature. Definitions of shame, caution, non-harming, and vigor remain brief or deferred.

The ground is every wholesome consciousness. Not ten stages. Not a claim that these arise only when a skill is developed.

Faith has two reported definitions. They are not fused. Heedfulness is care toward the wholesome dharmas, not those dharmas again. Guarding is another wording.

The equanimity result is a recorded difficulty and a deferral. Different respects are not a demonstrated solution until the shared support is accounted for.

Shame and caution are not filled from later passages. Non-harming and vigor stay the brief local definitions.

Interpretation: the wholesome is what the factors determine. Many passes. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_25
    a vak:Karika ;
    rdfs:label "VAK 2.25" ;
    vak:hasTopic vak:WholesomeGreatGround ;
    vak:belongsTo vak:Indriyanirdesa .

vak:WholesomeTen vak:inEveryWholesomeConsciousness true .
vak:EquanimityHere vak:distinctFrom vak:NeutralFeeling .

organon:NotTheFinalPass
    organon:notTheVerseEnglish true .
```
