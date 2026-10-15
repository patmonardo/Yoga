# VAK_1.07 — The Conditioned Bases as the Wheel of Dharma

## 1. Sanskrit (Devanāgarī)

> ते पुनः संस्कृता धर्मा रूपादिस्कन्धपञ्चकम् ।
>
> स एवाध्वा कथावस्तु सनिःसाराः सवस्तुकाः ॥ १.०७ ॥॥

## 2. Sanskrit (IAST)

> te punaḥ saṃskṛtā dharmā rūpādiskandhapañcakam /
>
> sa evādhvā kathāvastu saniḥsārāḥ savastukāḥ // 1.07 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| te | nominative masculine plural | those, resumed from 1.04 |
| punaḥ | indeclinable | resumes. Not “again” |
| saṃskṛtāḥ | nominative masculine plural | Conditioned |
| dharmāḥ | nominative masculine plural | dharmas |
| rūpādiskandhapañcakam | rūpa-ādi-skandha-pañcakam; collective singular predicate | the five bases beginning with form, gathered as one |
| saḥ eva | restrictive | that same field. The second line is not four extra heaps |
| adhvā | nominative masculine singular | the course |
| kathāvastu | kathā-vastu; compound | the reflection-term. Not “basis of discourse” |
| saniḥsārāḥ | sa-niḥsāra; bahuvrīhi, nominative masculine plural | the sāra term. Not “possessed of an exit” |
| savastukāḥ | sa-vastuka; bahuvrīhi, nominative masculine plural | possessed of vastu |

## 4. Grammar

```text
saṃskṛtā dharmāḥ
    = rūpādi-skandha-pañcakam

sa eva
    = adhvā
    = kathāvastu
    = saniḥsārāḥ
    = savastukāḥ
```

`Pañcakam` is a collective singular predicate of a plural subject: five base-members, gathered as one field. The second line is a quad. One field, four functions.

## 5. Translation

### Literal

Those Conditioned dharmas are the five bases beginning with form. That same field is the course, the *kathāvastu*, the *saniḥsāra*, and the *savastuka*.

### Bhāṣya-informed

They are called Conditioned because conditions come together and act together, and nothing is produced by one condition. The courses are gone, going, and about to go. The Prakaraṇa includes the *kathāvastu* in the eighteen principles. The prose glosses *niḥsāra* as nirvāṇa, the going-out from everything Conditioned. The Vaibhāṣikas say, *kila*, that the word *vastu* expresses cause. Those are glosses. They are not the quad.

## 6. Philosophical Translation

The Conditioned dharmas are Essential Being: the five bases beginning with the Form Base, gathered as one. That same field is the Path of Dharma, Essential Reflection, Essential Relation, and Appearance.

```text
Essential Being
    rūpādi-skandha-pañcakam

Path of Dharma
    adhvā

Essential Reflection
    kathāvastu

Essential Relation
    saniḥsāra

Appearance
    savastuka
```

## 7. Technical Vocabulary

| Sanskrit | Do not use as the reading | Determination |
|---|---|---|
| saṃskṛta | created; constructed | Conditioned |
| skandha | a list; heap as dismissive | base |
| rūpa | purely material form | form; the first member is the Form Base |
| adhvā | a clock | Path of Dharma |
| kathāvastu | basis of discourse; topic | Essential Reflection |
| saniḥsāra | possessed of an exit | Essential Relation. A Dharma is an End |
| vastu | cause; topic; substrate | Appearance |
| savastuka | possessed of causes | possessed of that Appearance |
| punaḥ | again | resumes |

The Vaibhāṣika gloss *vastu* = *hetu* is the armor-moment. Not the reading.

## 8. Logical Determination

```text
Conditioned(x) ↔ MemberOfFiveBases(x)
FiveBaseCollective = EssentialBeing
Unconditioned(x) → ¬BaseMember(x)
Conditioned(x) ↛ Impure(x)

SameField
    = Being
    = Path of Dharma
    = Essential Reflection
    = Essential Relation
    = Appearance

viṣaya      Condition
saṃskṛta    Conditioned
asaṃskṛta   Unconditioned
pratyaya    ≠ viṣaya
Construct   ≠ Condition
```

The kārikā does not name the five members. Cognition is not a word of this verse. Concept-level closure belongs to the six cognition-principles, not to this wheel by itself.

## 9. Interpretive Note

The inventory English broke the kārikā. The quad is the wheel, and it stays in the philosophical translation. The Form Base is the empirical root of appearance. That is the extension, not the literal.

The witness at `[004|26]` omits the Reflection Base. Not patched. The kārikā says five. Nirvāṇa-as-exit and *vastu*-as-cause remain glosses in the bhāṣya. What persists is Impure. A Rational Dharma does not Persist. Yoga is the key of *vastu*. It is not pasted into the literal.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_07 a vak:Karika ;
    vak:hasTopic vak:WheelOfDharma ;
    vak:belongsTo vak:Dhatunirdesa .

vak:EssentialBeing vak:namedBy vak:Skandha ;
    vak:projectTerm "base" .
vak:PathOfDharma vak:namedBy vak:Adhvan .
vak:EssentialReflection vak:namedBy vak:Kathavastu .
vak:EssentialRelation vak:namedBy vak:Sanihsara .
vak:Appearance vak:namedBy vak:Vastu .
vak:ExitGloss vak:isNotTheReading true .
vak:CauseGloss vak:isNotTheReading true .
```