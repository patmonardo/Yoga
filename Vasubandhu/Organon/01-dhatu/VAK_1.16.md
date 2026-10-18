# VAK_1.16 — The Cognition Base

## 1. Sanskrit (Devanāgarī)

```sanskrit
विज्ञानं प्रतिविज्ञप्तिः मन आयतनं च तत् ।
धातवः सप्त च मताः षड्विज्ञानान्यथो मनः ॥ १.१६ ॥
```

## 2. Sanskrit (IAST)

```text
vijñānaṃ prativijñaptiḥ mana āyatanaṃ ca tat /
dhātavaḥ sapta ca matāḥ ṣaḍvijñānāny atho manaḥ // 1.16 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| vijñānam | nominative neuter | Cognition |
| prativijñaptiḥ | nominative feminine | respective apprehension |
| mana āyatanam | nominative | Mind Essence |
| tat | nominative | that |
| dhātavaḥ | nominative plural | Principles |
| sapta matāḥ | numeral and participle | seven are accepted |
| ṣaṭ vijñānāni | numeral and plural | six cognitions |
| atho manaḥ | connective and nominative | and Mind |

**Grammar tokens.** Verse-order IAST with sandhi opened; combined table
rows are separated below. *Mana āyatanam* is kept as the Mind-Essence
compound, normalized as `mana-āyatanam`. Final *manaḥ* is read as Mind
Principle by the Bhāṣya. No supplied leaf is required.

```text
# tokens: vijñānam prativijñaptiḥ mana-āyatanam ca tat dhātavaḥ sapta ca matāḥ ṣaṭ-vijñānāni atho manaḥ
```

## 4. Grammar

Three nominal clauses define Cognition, identify its Essence projection,
and enumerate its Principles. Predicate nouns need not share gender:
neuter *vijñānam* is defined by feminine *prativijñaptiḥ*. Plural *matāḥ*
agrees with *dhātavaḥ*, not the singular Base.

```nltk-fcfg
% start S
# tokens: vijñānam prativijñaptiḥ mana-āyatanam ca tat dhātavaḥ sapta ca matāḥ ṣaṭ-vijñānāni atho manaḥ
S[SEM=<(?d & ?e & ?p)>] -> DEFINITION[SEM=?d] ESSENCE[SEM=?e] PRINCIPLES[SEM=?p]
DEFINITION[SEM=<?pred(?base)>] -> BASE[CASE=nom,NUM=?n,SEM=?base] APPREHENSION[CASE=nom,NUM=?n,SEM=?pred]
ESSENCE[SEM=<?essence(?base)>] -> ESSENCEHEAD[CASE=nom,NUM=?n,GEN=?g,SEM=?essence] AND BASEPRON[CASE=nom,NUM=?n,GEN=?g,SEM=?base]
PRINCIPLES[SEM=<?count(?six(?mind))>] -> PRINCIPLEHEAD[CASE=nom,NUM=?n,GEN=?g] COUNT[SEM=?count] AND ACCEPTED[CASE=nom,NUM=?n,GEN=?g] SIX[SEM=?six] ALSO MIND[CASE=nom,SEM=?mind]
BASE[CASE=nom,NUM=sg,GEN=n,SEM=<cognition_base>] -> 'vijñānam'
APPREHENSION[CASE=nom,NUM=sg,GEN=f,SEM=<\b.RespectiveApprehension(b)>] -> 'prativijñaptiḥ'
ESSENCEHEAD[CASE=nom,NUM=sg,GEN=n,SEM=<\b.EssenceProjection(b,mind_essence)>] -> 'mana-āyatanam'
AND -> 'ca'
BASEPRON[CASE=nom,NUM=sg,GEN=n,SEM=<cognition_base>] -> 'tat'
PRINCIPLEHEAD[CASE=nom,NUM=pl,GEN=m] -> 'dhātavaḥ'
COUNT[SEM=<\P.(P & CountedPrinciples(cognition_base,seven))>] -> 'sapta'
ACCEPTED[CASE=nom,NUM=pl,GEN=m] -> 'matāḥ'
SIX[CASE=nom,NUM=pl,GEN=n,SEM=<\m.all x.(PrincipleMember(x,cognition_base) <-> (SixCognitionPrinciple(x) | x=m))>] -> 'ṣaṭ-vijñānāni'
ALSO -> 'atho'
MIND[CASE=nom,NUM=sg,GEN=n,SEM=<mind_principle>] -> 'manaḥ'
```

```nltk-dep
'prativijñaptiḥ' -> 'vijñānam'
'mana-āyatanam' -> 'ca' | 'tat'
'matāḥ' -> 'dhātavaḥ' | 'ṣaṭ-vijñānāni'
'dhātavaḥ' -> 'sapta' | 'ca'
'ṣaṭ-vijñānāni' -> 'atho' | 'manaḥ'
```

**Close construe.** Cognition is respective apprehension; that is also
the Mind Essence. Its Principles are accepted as seven: the six Cognition
Principles and Mind, here the Mind Principle.

The Bhāṣya resolves the first subject as Cognition Base and apprehension
as respective to each Condition. `EssenceProjection` is a classification
relation, not identity between a Base and an Essence. The seven-member
roster is not seven simultaneous Cognitions or seven independent substances.
The Form and Dharma classifications summarized by the commentary depend
on 1.04–1.15; this pilot does not supply their missing formal derivation.

## 5. Translation

### Literal Translation

> Cognition is respective apprehension. And that is the Mind Essence. Seven
> principles are accepted: the six Cognitions, and Mind.

### Bhāṣya-informed study translation

> The Cognition Base is respective apprehension of each Condition. It is
> also the Mind Essence. In the Principle arrangement, it is counted as
> seven Principles: the six Cognition Principles and the Mind Principle.

## 6. Philosophical Translation

What is defined is the Base. As Essence it is Mind; as Principle it is seven, and the last of these is the Mind Principle.

## 7. Technical Vocabulary

| Sanskrit | Rendering |
|---|---|
| vijñāna-skandha | Cognition Base |
| prativijñapti | respective apprehension |
| mana-āyatana | Mind Essence |
| manovijñānadhātu | Mind-Cognition Principle |
| manodhātu | Mind Principle |
| upalabdhi | apprehension |

## 8. Logical Determination

**Kārikā, derived.** The semantic referent of the first two clauses is the
Base as a classification, not an individual moment of Cognition.

```nltk-sem
# derived by the section 4 parse
(RespectiveApprehension(cognition_base) & EssenceProjection(cognition_base,mind_essence) & ((all x.(PrincipleMember(x,cognition_base) <-> (SixCognitionPrinciple(x) | x=mind_principle))) & CountedPrinciples(cognition_base,seven)))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(RespectiveApprehension(cognition_base) & EssenceProjection(cognition_base,mind_essence) & ((all x.(PrincipleMember(x,cognition_base) <-> (SixCognitionPrinciple(x) | x=mind_principle))) & CountedPrinciples(cognition_base,seven)))
```

```nltk-valuation
cognition_base => cognition_class
mind_essence => mind_capacity
mind_principle => mind_role
seven => seven_count
RespectiveApprehension => {cognition_class}
EssenceProjection => {(cognition_class,mind_capacity)}
SixCognitionPrinciple => {eye_cog,ear_cog,nose_cog,tongue_cog,body_cog,mental_cog}
PrincipleMember => {(eye_cog,cognition_class),(ear_cog,cognition_class),(nose_cog,cognition_class),(tongue_cog,cognition_class),(body_cog,cognition_class),(mental_cog,cognition_class),(mind_role,cognition_class)}
CountedPrinciples => {(cognition_class,seven_count)}
```

**Model checks.** The roster equivalence excludes extra members. Tests
also count six distinct Cognition Principles and a distinct seventh
Mind Principle in this valuation. `seven` alone is a numeral label, not
arithmetic implemented by FOL. Removing Mind or adding an eighth member
must falsify the formula.

**Bhāṣya determination.** The six groups run from Eye-Cognition to
Mind-Cognition. The seventh classification is Mind Principle, not a new
seventh kind of Cognition. Its temporal office is developed in 1.17.

The Base is Cognition, respective apprehension, in six groups. The Essence of that Base is the Mind Essence. The Principles are seven. The seventh Cognition Principle is the Mind Principle.

The close is five Bases, twelve Essences, and eighteen Principles.

## 9. Interpretive Note

**Translation note.** The Bhāṣya explains Cognition as apprehension with respect to each Condition and divides it into six groups, from Eye-Cognition through Mind-Cognition. It reads the final *manaḥ* as *manodhātu* (Mind Principle), not as Mind alone; the seven Principles are the six Cognition Principles and the Mind Principle.

The verse cross-classifies the Cognition Base as Mind Essence and seven
Principles. The next verse specifies the support-role of the Mind Principle.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_16 a vak:Karika ;
    vak:hasTopic vak:CognitionBase .
vak:CognitionEssence vak:is vak:MindEssence .
vak:MindPrinciple vak:is vak:SeventhCognitionPrinciple .
```
