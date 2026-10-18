# VAK_1.07 — The Wheel in a Human Language

## 1. Sanskrit (Devanāgarī)

```sanskrit
ते पुनः संस्कृता धर्मा रूपादिस्कन्धपञ्चकम् ।
स एवाध्वा कथावस्तु सनिःसाराः सवस्तुकाः ॥ १.०७ ॥
```

## 2. Sanskrit (IAST)

```text
te punaḥ saṃskṛtā dharmā rūpādiskandhapañcakam /
sa evādhvā kathāvastu saniḥsārāḥ savastukāḥ // 1.07 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| te | nominative masculine plural | those, resumed from 1.04 |
| punaḥ | indeclinable | resumes. Not “again” |
| saṃskṛtāḥ | nominative masculine plural | Conditioned |
| dharmāḥ | nominative masculine plural | dharmas |
| rūpādiskandhapañcakam | rūpa-ādi-skandha-pañcakam; collective singular predicate | the five Bases beginning with Form, gathered as one |
| saḥ eva | restrictive | that same field. The second line is not four extra heaps |
| adhvā | nominative masculine singular | the course |
| kathāvastu | kathā-vastu; compound | the reflection-term. Not “basis of discourse” |
| saniḥsārāḥ | sa-niḥsāra; bahuvrīhi, nominative masculine plural | the sāra term. Not “possessed of an exit” |
| savastukāḥ | sa-vastuka; bahuvrīhi, nominative masculine plural | possessed of vastu |

**Grammar tokens.** Normalized IAST in verse order, with sandhi opened.
The collective compound remains one leaf; *saḥ eva* becomes two.
No supplied token is needed. The singular resumption takes up the
collective field, while the final plural predicates resume its Dharmas.

```text
# tokens: te punaḥ saṃskṛtāḥ dharmāḥ rūpādi-skandha-pañcakam saḥ eva adhvā kathāvastu saniḥsārāḥ savastukāḥ
```

## 4. Grammar

The conditioned subject is masculine plural; its predicate is a neuter
singular collective. This is nominal predication, not adjective agreement.
The second line resumes that collective with *saḥ eva*. Singular
*adhvā* and *kathāvastu* do not impose their number on the final plural
*saniḥsārāḥ* and *savastukāḥ*.

```nltk-fcfg
% start S
# tokens: te punaḥ saṃskṛtāḥ dharmāḥ rūpādi-skandha-pañcakam saḥ eva adhvā kathāvastu saniḥsārāḥ savastukāḥ
S[SEM=<(?classification & ?determinations)>] -> CLASSIFICATION[SEM=?classification] RESUMPTION[SEM=?determinations]
CLASSIFICATION[SEM=<all x.(?dharma(x) -> (?conditioned(x) <-> ?bases(x)))>] -> DEM[CASE=nom,NUM=?n,GEN=?g] RESUME CONDITIONED[CASE=nom,NUM=?n,GEN=?g,SEM=?conditioned] DHARMA[CASE=nom,NUM=?n,GEN=?g,SEM=?dharma] COLLECTIVE[CASE=nom,NUM=sg,GEN=n,SEM=?bases]
RESUMPTION[SEM=<?same(?course)(?discourse)(?end)(?vastu)>] -> SAME[CASE=nom,NUM=sg,GEN=m,SEM=?same] ONLY COURSE[CASE=nom,NUM=sg,GEN=m,SEM=?course] DISCOURSE[CASE=nom,NUM=sg,GEN=n,SEM=?discourse] END[CASE=nom,NUM=?n,GEN=?g,SEM=?end] VASTU[CASE=nom,NUM=?n,GEN=?g,SEM=?vastu]
DEM[CASE=nom,NUM=pl,GEN=m] -> 'te'
RESUME -> 'punaḥ'
CONDITIONED[CASE=nom,NUM=pl,GEN=m,SEM=<\x.Conditioned(x)>] -> 'saṃskṛtāḥ'
DHARMA[CASE=nom,NUM=pl,GEN=m,SEM=<\x.Dharma(x)>] -> 'dharmāḥ'
COLLECTIVE[CASE=nom,NUM=sg,GEN=n,SEM=<\x.FiveBaseMember(x)>] -> 'rūpādi-skandha-pañcakam'
SAME[CASE=nom,NUM=sg,GEN=m,SEM=<\P.\Q.\R.\T.all x.((Dharma(x) & Conditioned(x)) -> (P(x) & Q(x) & R(x) & T(x)))>] -> 'saḥ'
ONLY -> 'eva'
COURSE[CASE=nom,NUM=sg,GEN=m,SEM=<\x.CourseDetermination(x)>] -> 'adhvā'
DISCOURSE[CASE=nom,NUM=sg,GEN=n,SEM=<\x.Kathavastu(x)>] -> 'kathāvastu'
END[CASE=nom,NUM=pl,GEN=m,SEM=<\x.HasNihsara(x)>] -> 'saniḥsārāḥ'
VASTU[CASE=nom,NUM=pl,GEN=m,SEM=<\x.HasVastu(x)>] -> 'savastukāḥ'
```

```nltk-dep
'rūpādi-skandha-pañcakam' -> 'dharmāḥ'
'dharmāḥ' -> 'te' | 'punaḥ' | 'saṃskṛtāḥ'
'adhvā' -> 'saḥ' | 'kathāvastu' | 'saniḥsārāḥ' | 'savastukāḥ'
'saḥ' -> 'eva'
```

**Close construe.** Those conditioned Dharmas are the five Bases beginning
with Form. That same field is the course, kathāvastu, and, in its Dharmas,
saniḥsāra and savastuka.

The resumption preserves one field across four functions, without making
the four predicates synonymous. The first clause classifies conditioned
Dharmas by the five Bases; it does not assert only five individual Dharmas.
The grammar's classification rule below supplies the nominal predication
through a restricted biconditional.

The Bhāṣya's glosses explain temporal course, meaningful discourse,
nirvāṇa as exit, and, in the attributed Vaibhāṣika account, *vastu* as
cause. Their mechanisms are not independently derived by the four lexical
predicates. The witness lists only four Base names, omitting *saṃjñā*;
the verse's fivefold collective is preserved without repairing that list.

## 5. Translation

### Literal Translation

> Those Conditioned dharmas are the five Bases beginning with Form. That
> same field is the course, the *kathāvastu*, the *saniḥsāra*, and the
> *savastuka*.

### Bhāṣya-informed study translation

> The conditioned dharmas are the five Bases beginning with the Form Base.
> These same dharmas are past, present, and future; subjects of discourse;
> have an exit in nirvāṇa; and possess a real basis.

## 6. Philosophical Translation

The Conditioned dharmas are the Base: the five Bases beginning with the Form Base, gathered as one. That same field is the Path of Dharma, Essential Reflection, Essential Relation, and Appearance.

```text
Base
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
| skandha | a list; heap as dismissive | Base |
| rūpa | purely material Form | Form; the first member is the Form Base |
| adhvā | a clock | Path of Dharma |
| kathāvastu | basis of discourse; topic | Essential Reflection |
| saniḥsāra | possessed of an exit | Essential Relation. A Dharma is an End |
| vastu | cause; topic; substrate | Appearance |
| savastuka | possessed of causes | possessed of that Appearance |
| punaḥ | again | resumes |

The Vaibhāṣika gloss *vastu* = *hetu* is the armor-moment. Not the reading.

## 8. Logical Determination

**Kārikā, derived.** The classification and the four determinations have
the same restricted domain. These predicates preserve distinctions for
further interpretation; they are not assertions that course, reflection,
relation, and appearance are identical.

```nltk-sem
# derived by the section 4 parse
((all x.(Dharma(x) -> (Conditioned(x) <-> FiveBaseMember(x)))) & (all x.((Dharma(x) & Conditioned(x)) -> (CourseDetermination(x) & Kathavastu(x) & HasNihsara(x) & HasVastu(x)))))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((all x.(Dharma(x) -> (Conditioned(x) <-> FiveBaseMember(x)))) & (all x.((Dharma(x) & Conditioned(x)) -> (CourseDetermination(x) & Kathavastu(x) & HasNihsara(x) & HasVastu(x)))))
# THEORY preceding_classification
# EXPECT preceding_classification T
all x.(Unconditioned(x) -> (Dharma(x) & -FiveBaseMember(x)))
exists x.(Dharma(x) & Conditioned(x) & Pure(x) & -Impure(x))
# THEORY rejected_conditioned_means_impure
# EXPECT rejected_conditioned_means_impure F
all x.((Dharma(x) & Conditioned(x)) -> Impure(x))
```

```nltk-valuation
Dharma => {form,feeling,reflection,formation,cognition,path,space_case}
Conditioned => {form,feeling,reflection,formation,cognition,path}
FiveBaseMember => {form,feeling,reflection,formation,cognition,path}
CourseDetermination => {form,feeling,reflection,formation,cognition,path}
Kathavastu => {form,feeling,reflection,formation,cognition,path}
HasNihsara => {form,feeling,reflection,formation,cognition,path}
HasVastu => {form,feeling,reflection,formation,cognition,path}
Unconditioned => {space_case}
Pure => {path,space_case}
Impure => {form,feeling,reflection,formation,cognition}
```

**Model checks.** The six conditioned representatives are cases, not a
six-Base roster. Removing any of their four determinations or changing
their classification must fail. Space is outside the conditioned
restriction. The Path supplies the inherited counterexample to
“conditioned means Impure.” A second test interpretation can assign one
predicate outside that restriction without assigning the others: the
verse formula does not equate their unrestricted extensions.

**Bhāṣya determination.** Conditioned Dharmas are explained through
conditions coming together and acting together, not production by one
condition alone. The name also applies to future Dharmas by kind.
The attributed cause-gloss is not turned into a general identity between
*vastu*, *hetu*, āśraya, and ālambana.

**Organon interpretation.** The following retains the Wheel reading.
Its functional names are interpreted determinations, not additional
Sanskrit leaves or equalities proved by the feature parse.

```text
Conditioned(x) ↔ MemberOfFiveBases(x)
FiveBaseCollective = Base
Unconditioned(x) → ¬BaseMember(x)
Conditioned(x) ↛ Impure(x)

SameField
    = Base
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

The kārikā does not name the five members. Cognition is not a word of this verse. Concept-level closure belongs to the six Cognition Principles, not to this wheel by itself.

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
    vak:projectTerm "Base" .
vak:PathOfDharma vak:namedBy vak:Adhvan .
vak:EssentialReflection vak:namedBy vak:Kathavastu .
vak:EssentialRelation vak:namedBy vak:Sanihsara .
vak:Appearance vak:namedBy vak:Vastu .
vak:ExitGloss vak:isNotTheReading true .
vak:CauseGloss vak:isNotTheReading true .
```