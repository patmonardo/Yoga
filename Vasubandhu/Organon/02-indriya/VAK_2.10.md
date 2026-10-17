# VAK_2.10 — Maturation, and What Produces It

## 1. Sanskrit (Devanāgarī)

```sanskrit
विपाको जीवितं द्वेधा द्वादश अन्त्याष्टकादृते ।
दौर्मनस्याच्च तत्त्वेकं सविपाकं दश द्विधा ॥ २.१० ॥
```

## 2. Sanskrit (IAST)

```text
vipāko jīvitaṃ dvedhā dvādaśa antyāṣṭakādṛte /
daurmanasyāc ca tattv ekaṃ savipākaṃ daśa dvidhā // 2.10 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| vipākaḥ | nominative | maturation; the present result |
| jīvitam | nominative | life |
| dvedhā | indeclinable | twofold, on that axis |
| dvādaśa | nominative | twelve |
| antya-aṣṭakāt ṛte | ablative | apart from the final eight |
| daurmanasyāt ca | ablative | and apart from distress |
| tat tu ekam | nominative | that one alone |
| sa-vipākam | nominative | possessing maturation as result |
| daśa dvidhā | nominative | ten are twofold |

Vipāka is what the present instance is. Savipāka is what it produces. The two questions are not one word.

## 4. Grammar

```text
% start S
S[IS=maturation] -> Life[EXCEPT=concentration]
S[HAS=maturation-result, ALWAYS=true] -> Distress
S[IS=?i, HAS=?h] -> Twelve
```

`IS` and `HAS` are distinct features. Distress unifies only with `HAS`.

## 5. Translation

### Literal Translation

> Life is maturation. Twelve are twofold, apart from the final eight and
> distress. That one alone possesses maturation as its result. Ten are
> twofold.

### Bhāṣya-informed study translation

> Life is maturation. Twelve are twofold except the final eight and
> distress; of these, that one alone is with maturation. Ten are twofold.

## 6. Philosophical Translation

> Incoming is vipāka. Outgoing is savipāka. Distress sits on neither side the same way.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| vipāka | maturation | the present result of prior action |
| savipāka | possessing maturation | produces a future result |
| antya-aṣṭaka | final eight | the five and the three |
| upacayika | from development | a Form faculty that is not maturation |
| airyāpathika | deportment | indeterminate; not maturation |
| śailpasthānika | craft | indeterminate |
| nairmāṇika | magical creation | indeterminate |
| parikalpa-viśeṣa | particular conceptual construction | produces and calms distress |
| prāntakoṭika | the named fourth dhyāna | the arhat's lifespan act |
| āyuḥsaṃskāra | lifespan-formation | the digression |
| jīvitasaṃskāra | life-formation | distinguished, or not, by the alternatives |

## 8. Logical Determination

```text
is maturation
    ≠ produces maturation

life
    → maturation, except concentration-projected life

twelve
    → either
    seven of form, mind, pain, pleasure, gladness, neutral feeling

never maturation
    = distress + final eight

distress
    → never maturation
    → always produces maturation

ten
    → either produce or not
    mind, four feelings, five beginning with faith

never produce
    = seven of form, life, the three

1 + 12 + 9 = 22
1 + 10 + 11 = 22
```

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the
verse translation): What the instance is, and what it produces, are
separate. Life is received maturation, except the life concentration
projects. Distress is never received. It is produced and calmed by present
construction, yet always produces future maturation. Ten can either
produce it or not.

The opening rule is qualified before the twelve are counted. Concentration-generated life is not maturation. Resource-maturation converted to lifespan, a remainder drawn forward, and Ghoṣaka's Great Elements are reported alternatives. The adopted explanation is the turned impetus. The digression on why, where, and the Buddha's three months is marked incidental. It is not a practical instruction.

Distress and the sūtra of three actions stay apart. Association is not maturation. The Vaibhāṣika reasons are construction, the immediate-offense counterexample, and absence in those free from attachment. Gladness still has room to be maturation. Distress does not.

Eight with life as eighth: wholesome in a favorable destiny, unwholesome in an unfavorable one. Mind is either in either. Pleasure, gladness, and neutral feeling are wholesome maturation. Pain is unwholesome. Both sexual marks in a favorable destiny: the condition is unwholesome acquisition. The faculty itself is projected by wholesome action.

Interpretation: the two predicates are the method. The received collapse is refused. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_10
    a vak:Karika ;
    rdfs:label "VAK 2.10" ;
    vak:hasTopic vak:Maturation, vak:ProducesMaturation ;
    vak:belongsTo vak:Indriyanirdesa .

vak:LifeFaculty vak:isMaturation true ;
    vak:exception vak:ConcentrationProjectedLife .
vak:DistressFaculty vak:isMaturation false ;
    vak:producesMaturation true .

organon:TwoPredicates
    organon:notOneKarmicWord true ;
    organon:notTheVerseEnglish true .
```
