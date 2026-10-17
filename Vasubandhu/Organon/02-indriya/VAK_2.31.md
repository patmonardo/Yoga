# VAK_2.31 — What the Higher Levels Drop

## 1. Sanskrit (Devanāgarī)

> कौकृत्यमिद्धाकुशलान्याद्ये ध्याने न सन्त्यतः ।
>
> ध्यानान्तरे वितर्कश्च विचारश्चाप्यतः परम् ॥ २.३१ ॥

## 2. Sanskrit (IAST)

> kaukṛtyamiddhākuśalāny ādye dhyāne na santy ataḥ /
>
> dhyānāntare vitarkaś ca vicāraś cāpy ataḥ param // 2.31 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| kaukṛtya-middha-akuśalāni | nominative | regret, torpor, and the unwholesome |
| ādye dhyāne | locative | in the first dhyāna |
| na santi | | are not present |
| ataḥ | indeclinable | of what was stated |
| dhyāna-antare | locative | in the intermediate dhyāna |
| vitarkaḥ ca | | vitarka also |
| vicāraḥ ca api | | vicāra also |
| ataḥ param | | beyond this |

Ataḥ points back to the desire-realm distribution. Not a cause.

## 4. Grammar

```text
% start S
S[LEVEL=first] -> DesireBase[REGRET=false, TORPOR=false, UNWHOLESOME=false]
S[LEVEL=intermediate] -> First[VITARKA=false]
S[LEVEL=beyond] -> Intermediate[VICARA=false, DECEPTION=false, CROOKEDNESS=false]
```

Exclusions accumulate.  
Vitarka drops at the intermediate; vicāra at the beyond.  
Intoxication is not named in the further drop.

## 5. Translation

### Literal Translation

Regret, torpor, and the unwholesome are not present in the first dhyāna, of these. In the intermediate dhyāna, vitarka also. Beyond this, vicāra also.

### Bhāṣya-informed study translation

> Regret, torpor, and the unwholesome are absent in the first dhyāna. In the intermediate, vitarka also. Beyond, vicāra also, and deception and crookedness. Exclusions accumulate. The rest remains as before. Crookedness reaches only as far as Brahmā.

## 6. Philosophical Translation

> The higher levels drop factors; they do not invent new ones. Unwholesome is excluded; not every affliction is. The accumulation is the rule.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| ādya-dhyāna | first dhyāna | drops regret, torpor, unwholesome operation |
| dhyānāntara | intermediate dhyāna | drops vitarka; vicāra remains |
| ataḥ param | beyond this | second and higher, and the formless |
| yathā-pratiṣiddham | as previously excluded | carried upward |
| śāṭhya, mada, māyā | crookedness, intoxication, deception | the three exceptions at the first |
| parṣat-sambandha | connection with an assembly | why crookedness stops at Brahmā |
| kṣepa | evasion | Brahmā's response |

Mada is not conceit. Middha is not sluggishness.

## 8. Logical Determination

```python
from nltk.sem.logic import LogicParser
lp = LogicParser()

first = lp.parse(r'all c.(FirstDhyana(c) -> -Regret(c) & -Torpor(c) & -Unwholesome(c))')
inter = lp.parse(r'all c.(Intermediate(c) -> First(c) & -Vitarka(c))')
beyond = lp.parse(r'all c.(Beyond(c) -> Intermediate(c) & -Vicara(c) & -Deception(c) & -Crookedness(c))')
```

Exclusions accumulate.  
Unwholesome is excluded; not every affliction.  
Intoxication is not named in the further drop.

## 9. Interpretive Note

The Brahmā episode supports the upper limit of crookedness. The question is Aśvajit's. The titles are Brahmā's. The commentary calls the response an evasion made without knowing. Not an assertion of creative authority. The story is not completed from elsewhere. Assembly-dependence is stated for crookedness. Not expanded into a theory of both factors.

The title sequence is damaged. Creator, Producer is provisional. Four and I am are contextual readings.

The close indexes three variables: which level, which consciousness, how many factors. The remainder as before keeps what was not altered.

Organon reading: level, ethical character, and factor-identity stay apart. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_31
    a vak:Karika ;
    rdfs:label "VAK 2.31" ;
    vak:hasTopic vak:HigherLevelExclusions ;
    vak:belongsTo vak:Indriyanirdesa .

vak:FirstDhyana vak:excludes vak:Regret, vak:Torpor, vak:Unwholesome .
vak:IntermediateDhyana vak:excludes vak:Vitarka .
vak:BeyondIntermediate vak:excludes vak:Vicara, vak:Deception, vak:Crookedness .

organon:IntoxicationNotInTheFurtherDrop
    organon:notTheVerseEnglish true .
```
