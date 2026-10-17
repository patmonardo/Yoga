# VAK_2.27 — The Limited Ground

## 1. Sanskrit (Devanāgarī)

```sanskrit
क्रोधोपनाहशाठ्येर्ष्याप्रदासम्रक्षमत्सराः ।
मायामदविहिंसाश्च परीत्तक्लेशभूमिकाः ॥ २.२७ ॥
```

## 2. Sanskrit (IAST)

```text
krodhopanāhaśāṭhyerṣyāpradāsamrakṣamatsarāḥ /
māyāmadavihiṃsāś ca parīttakleśabhūmikāḥ // 2.27 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| krodha | nom. sg. m. | anger |
| upanāha | nom. sg. m. | resentment |
| śāṭhya | nom. sg. n. | crookedness |
| īrṣyā | nom. sg. f. | envy |
| pradāsa | nom. sg. m. | spite |
| mrakṣa | nom. sg. n. | concealment |
| matsara | nom. sg. m. | stinginess |
| māyā | nom. sg. f. | deception |
| mada | nom. sg. m. | intoxication |
| vihiṃsā | nom. sg. f. | harmfulness |
| parītta-kleśa-bhūmikāḥ | nom. pl. f.; compound | of the limited-affliction ground |

The English of the ten is provisional. Definitions are deferred.
## 4. Grammar

```text
% start S
S[GROUND=limited-affliction] -> TenLimited
TenLimited -> Anger | Resentment | Crookedness | Envy | Spite | Concealment | Stinginess | Deception | Intoxication | Harmfulness
S[ASSOCIATED=ignorance, ABANDON=cultivation, SPHERE=mental] -> TenLimited
```

`GROUND=limited-affliction` does not force co-presence of the ten.  
Association is only with ignorance abandonable by cultivation and of the mental sphere.

## 5. Translation

### Literal Translation

> Anger, resentment, crookedness, envy, spite, concealment, stinginess,
> deception, intoxication, and harmfulness belong to the ground of limited
> afflictions.
### Bhāṣya-informed study translation

> Anger, resentment, crookedness, envy, spite, concealment, stinginess,
> deception, intoxication, and harmfulness belong to the ground of limited
> afflictions.
## 6. Philosophical Translation

> Limited-affliction ground is restriction, not universality. The ten share the same associated ignorance; they do not share one moment.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| parītta-kleśa-bhūmika | limited-affliction ground | range, not slightness |
| avidyā-mātreṇa | only with ignorance | among afflictions |
| bhāvanā-heya | abandonable through cultivation | not through seeing |
| mano-bhūmika | of the mental sphere | not the five sensory consciousnesses |
| upakleśa | secondary affliction | where the definitions wait |
| aniyata | unfixed | not ethically indeterminate |

## 8. Logical Determination

```python
from nltk.sem.logic import LogicParser
lp = LogicParser()

limited = lp.parse(r'all x.(LimitedAffliction(x) -> (Associated(x,Ignorance) & Abandonable(Ignorance,cultivation) & Sphere(Ignorance,mental)))')
not_together = lp.parse(r'-all x y.(LimitedAffliction(x) & LimitedAffliction(y) -> CoPresent(x,y))')
```

Shared restriction, not co-presence.  
The five classes are stated; others remain unfixed.

## 9. Interpretive Note

**Translation note.** The commentary associates this class only with ignorance abandoned by cultivation in the mental sphere, then names five classes of mental factors and unfixed examples: initial and sustained examination, regret, and torpor. It defers the factors' definitions and leaves the list open.

Anger is not resentment. Crookedness is not deception. Spite is not harmfulness. The distinctions are named. They are not yet explained. Concealment and intoxication are not complete definitions. Intoxication is not settled as a substance.

Secondary affliction is the deferred discussion. It is not identified with this class. Ground remains range of operation.

The unfixed examples leave the list open. Their distributions wait on the count of what must be in a given consciousness.

Organon reading: shared constraints are not a required bundle. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_27
    a vak:Karika ;
    rdfs:label "VAK 2.27" ;
    vak:hasTopic vak:LimitedAfflictionGround ;
    vak:belongsTo vak:Indriyanirdesa .

vak:LimitedTen vak:necessarilyTogether false .
vak:FiveClasses vak:exhaustive false .

organon:ClassNotBundle
    organon:notTheVerseEnglish true .
```
