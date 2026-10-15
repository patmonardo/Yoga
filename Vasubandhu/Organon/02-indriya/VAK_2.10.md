# VAK_2.10 — Maturation, and What Produces It

## 1. Sanskrit (Devanāgarī)

> विपाको जीवितं द्वेधा द्वादश अन्त्याष्टकादृते ।
>
> दौर्मनस्याच्च तत्त्वेकं सविपाकं दश द्विधा ॥ २.१० ॥

## 2. Sanskrit (IAST)

> vipāko jīvitaṃ dvedhā dvādaśa antyāṣṭakādṛte /
>
> daurmanasyāc ca tattv ekaṃ savipākaṃ daśa dvidhā // 2.10 //

Tattvekam is tat tu ekam. The consonant of tat assimilates before tu.

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
life
    → maturation
    qualified: concentration-generated life is not

twelve, apart from the final eight and distress
    → either maturation or not
    seven of form, mind, pain, pleasure, gladness, neutral feeling

distress
    → never maturation
    → that one alone always produces maturation

ten
    → either produce maturation or not
    mind, the other four feelings, the five beginning with faith
```

Tu is only, and stands out of metrical place.

## 5. Translation

### Literal Translation

Life is maturation. Twelve are twofold, apart from the final eight and distress. That one alone possesses maturation as its result. Ten are twofold.

### Bhāṣya-informed study translation

Life is maturation. The qualification follows. When an arhat sustains the lifespan-formations by the prāntakoṭika fourth dhyāna, that life-faculty is not maturation. Life other than that is. The explanation adopted here is that concentration turns aside the impetus born of prior action and projects an impetus born of concentration.

Twelve, excluding the final eight and distress, are both maturation and not. Of the seven beginning with the eye, those from development are not maturation. The rest are. Mind and the four feelings other than distress, when wholesome or afflicted, are not maturation. Neither are the instances tied to deportment, craft, or magical creation. The rest are.

Distress is not maturation. The sūtra of three actions, to be experienced as gladness, distress, or neutral feeling, is read as experience through association, not as maturation. Distress arises and is calmed by particular conceptual construction. Maturation is not like that. The Vaibhāṣikas conclude it is never maturation. It does not occur in those free from attachment, and maturation is not excluded that way.

That one alone, distress, always has maturation as its result. It is not indeterminate, and it is not without outflows, because it is not concentrated. Ten are twofold: mind, the feelings other than distress, and the five beginning with faith. Wholesome with outflows, or unwholesome, they produce maturation. Without outflows, or indeterminate, they do not. The rest produce none.

## 6. Philosophical Translation

What the instance is, and what it produces, are separate. Life is received maturation, except the life concentration projects. Distress is never received. It is produced and calmed by present construction. That same distress always produces future maturation. Non-inheritance is not causal innocence.

Organon rendering:

Two directions on one jewel. Incoming is vipāka. Outgoing is savipāka. Distress sits on neither side the same way. The received English that says karmic for both is the English not accepted. Not the verse English.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| vipāka | maturation | the present result of prior action |
| savipāka | possessing maturation | produces a future result |
| antya-aṣṭaka | final eight | the five and the three |
| upacayika | from development | a material faculty that is not maturation |
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

The opening rule is qualified before the twelve are counted. Concentration-generated life is not maturation. Resource-maturation converted to lifespan, a remainder drawn forward, and Ghoṣaka's great elements are reported alternatives. The adopted explanation is the turned impetus. The digression on why, where, and the Buddha's three months is marked incidental. It is not a practical instruction.

Distress and the sūtra of three actions stay apart. Association is not maturation. The Vaibhāṣika reasons are construction, the immediate-offense counterexample, and absence in those free from attachment. Gladness still has room to be maturation. Distress does not.

Eight with life as eighth: wholesome in a favorable destiny, unwholesome in an unfavorable one. Mind is either in either. Pleasure, gladness, and neutral feeling are wholesome maturation. Pain is unwholesome. Both sexual marks in a favorable destiny: the condition is unwholesome acquisition. The faculty itself is projected by wholesome action.

Organon reading: the two predicates are the method. The received collapse is refused. Not the verse English.

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
