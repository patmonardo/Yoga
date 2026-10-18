# VAK_1.21 — Feeling and Reflection as Distinct Bases

## 1. Sanskrit (Devanāgarī)

```sanskrit
विवादमूलसंसारहेतुत्वात् क्रमकारणात् ।
चैत्तेभ्यो वेदनासंज्ञे पृथक्स्कन्धौ निवेशितौ ॥ १.२१ ॥
```

## 2. Sanskrit (IAST)

```text
vivādamūlasaṃsārahetutvāt kramakāraṇāt /
caittebhyo vedanāsaṃjñe pṛthakskandhau niveśitau // 1.21 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| vivāda-mūla-saṃsāra-hetutvāt | ablative singular abstract compound | because of being causes of the roots of dispute and of saṃsāra |
| krama-kāraṇāt | ablative neuter singular | because of the reason of order |
| caittebhyaḥ | ablative plural | from the other mental factors |
| vedanā-saṃjñe | feminine dual | feeling and reflection |
| pṛthak-skandhau | masculine dual | two distinct bases |
| niveśitau | past participle dual | established |

The commentary supplies *pradhāna-hetu*: principal cause. Feeling and reflection are not the only causes. The local Devanāgarī sometimes reads *cittebhyaḥ*. The prose and the IAST support *caittebhyaḥ*.

**Grammar tokens.** Verse-order IAST with external sandhi opened and
compound boundaries marked. The compound containing both causal fields
remains one leaf. *Pṛthak* is separated from *skandhau*, as in the prose.
No covert token is supplied.

```text
# tokens: vivāda-mūla-saṃsāra-hetutvāt krama-kāraṇāt caittebhyaḥ vedanā-saṃjñe pṛthak skandhau niveśitau
```

## 4. Grammar

The two initial ablatives give reasons for placement. *Caittebhyaḥ*
marks separation from the other mental factors, not removal from the
mental-factor class. Feminine dual *vedanāsaṃjñe* names the pair;
masculine dual *niveśitau* follows the predicate *skandhau*.

```nltk-fcfg
% start S
# tokens: vivāda-mūla-saṃsāra-hetutvāt krama-kāraṇāt caittebhyaḥ vedanā-saṃjñe pṛthak skandhau niveśitau
S[SEM=<?reasons(?placement)>] -> REASONS[SEM=?reasons] PLACEMENT[SEM=?placement]
REASONS[SEM=<\P.(?causal & ?order & P)>] -> CAUSAL[CASE=abl,SEM=?causal] ORDER[CASE=abl,SEM=?order]
PLACEMENT[SEM=<?pair(?separate(?other)(?placed(?bases)))>] -> OTHER[CASE=?case,NUM=pl,SEM=?other] PAIR[CASE=nom,NUM=?n,GEN=f,SEM=?pair] SEPARATE[OBJCASE=?case,SEM=?separate] BASES[CASE=nom,NUM=?n,GEN=?g,SEM=?bases] PLACED[CASE=nom,NUM=?n,GEN=?g,SEM=?placed]
CAUSAL[CASE=abl,SEM=<(CauseOfDisputeRoots(feeling) & CauseOfDisputeRoots(reflection) & CauseOfSamsara(feeling) & CauseOfSamsara(reflection))>] -> 'vivāda-mūla-saṃsāra-hetutvāt'
ORDER[CASE=abl,SEM=<OrderReasonForSeparateBases(base_order)>] -> 'krama-kāraṇāt'
OTHER[CASE=abl,NUM=pl,SEM=<other_mental_factors>] -> 'caittebhyaḥ'
PAIR[CASE=nom,NUM=dual,GEN=f,SEM=<\P.(P(feeling) & P(reflection))>] -> 'vedanā-saṃjñe'
SEPARATE[OBJCASE=abl,SEM=<\o.\P.\x.(P(x) & SeparatelyFrom(x,o))>] -> 'pṛthak'
BASES[CASE=nom,NUM=dual,GEN=m,SEM=<\x.SeparateBasePlacement(x)>] -> 'skandhau'
PLACED[CASE=nom,NUM=dual,GEN=m,SEM=<\P.\x.P(x)>] -> 'niveśitau'
```

```nltk-dep
'niveśitau' -> 'vivāda-mūla-saṃsāra-hetutvāt' | 'krama-kāraṇāt' | 'vedanā-saṃjñe' | 'skandhau'
'skandhau' -> 'pṛthak'
'pṛthak' -> 'caittebhyaḥ'
```

**Close construe.** Because of being causes of the roots of dispute and
of saṃsāra, and because of the reason of order, Feeling and Reflection
are placed as separate Bases apart from the other mental factors.

The projection records the asserted reasons and the placement, not a
material implication that claims causal sufficiency. The Bhāṣya resolves
the causal compound's distribution; the root grammar does not yet assign
the two named fixations. The reason of order is acknowledged by name,
not demonstrated here. Dual agreement links the pair with the predicate
and participle without forcing feminine subject and masculine predicate
to share gender. Separation is represented as a classification relation,
not a historical event in which Feeling and Reflection ceased being
mental factors.

## 5. Translation

### Literal Translation

> Because they are causes of the roots of dispute and of saṃsāra, and
> because of the reason of order, feeling and reflection are established as
> two distinct bases apart from the other mental factors.

### Bhāṣya-informed study translation

> Because they are causes of the roots of dispute and of saṃsāra, and because
> of the reason of order, feeling and reflection were established as distinct
> Bases apart from the other mental factors.

## 6. Philosophical Translation

Again, two lines. The first names the reasons. The second names the placement.

The question is why two mental factors receive separate Bases rather than
being gathered with the rest in the Formations Base. Not because they cease
to be mental factors. Their operations are the principal hinges of the two
roots of dispute, and of continued wandering.

Feeling is undergoing. The hinge is the savor of that undergoing. Under that savor, one clings to sensual desire. Reflection takes up the mark. The hinge is the inverted mark. Under that inversion, one clings to views. Principal, not sole.

The one who wanders is greedy for the savor of feeling and inverted in reflection. The two determinations join in one subject. They are not two independent inventories.

The last reason is the order of the bases. It is promised in three ways. It is not given here.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| caitta | mental factor | the class they leave, as bases |
| vedanā | feeling | undergoing; not the fixation |
| saṃjñā | reflection | takes up the mark |
| saṃskāra-skandha | formations-base | where the other mental factors remain |
| vivāda-mūla | root of dispute | the two fixations |
| kāmādhyavasāna | fixation upon sensual desire | principal cause: feeling |
| dṛṣṭyadhyavasāna | fixation upon views | principal cause: reflection |
| vedanā-svāda | savor of feeling | the mediation |
| viparīta-saṃjñā | inverted reflection | not every reflection |
| pradhāna-hetu | principal cause | not sole |
| krama | order | deferred |

## 8. Logical Determination

**Kārikā, derived.** The two causal fields, the announced order reason,
and the two separate placements are asserted together.

```nltk-sem
# derived by the section 4 parse
((CauseOfDisputeRoots(feeling) & CauseOfDisputeRoots(reflection) & CauseOfSamsara(feeling) & CauseOfSamsara(reflection)) & OrderReasonForSeparateBases(base_order) & ((SeparateBasePlacement(feeling) & SeparatelyFrom(feeling,other_mental_factors)) & (SeparateBasePlacement(reflection) & SeparatelyFrom(reflection,other_mental_factors))))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((CauseOfDisputeRoots(feeling) & CauseOfDisputeRoots(reflection) & CauseOfSamsara(feeling) & CauseOfSamsara(reflection)) & OrderReasonForSeparateBases(base_order) & ((SeparateBasePlacement(feeling) & SeparatelyFrom(feeling,other_mental_factors)) & (SeparateBasePlacement(reflection) & SeparatelyFrom(reflection,other_mental_factors))))
# THEORY prose
# EXPECT prose T
MentalFactor(feeling) & MentalFactor(reflection)
PrincipalCause(feeling,sensual_fixation) & PrincipalCause(reflection,view_fixation)
DisputeRoot(sensual_fixation) & DisputeRoot(view_fixation)
MediatedBy(feeling,savor) & MediatedBy(reflection,inversion)
GreedyForSavor(wanderer) & InvertedReflection(wanderer) & Wanders(wanderer)
# THEORY rejected_separate_bases_are_not_mental_factors
# EXPECT rejected_separate_bases_are_not_mental_factors F
all x.(SeparateBasePlacement(x) -> -MentalFactor(x))
# THEORY rejected_principal_means_sole
# EXPECT rejected_principal_means_sole F
all x.all y.(PrincipalCause(x,y) -> SoleCause(x,y))
# THEORY rejected_feeling_and_reflection_are_the_roots
# EXPECT rejected_feeling_and_reflection_are_the_roots F
DisputeRoot(feeling) & DisputeRoot(reflection)
```

```nltk-valuation
feeling => feeling_factor
reflection => reflection_factor
other_mental_factors => remaining_factor_class
base_order => announced_order_reason
sensual_fixation => sensual_root
view_fixation => view_root
savor => savor_mediation
inversion => inversion_mediation
wanderer => wandering_person
CauseOfDisputeRoots => {feeling_factor,reflection_factor}
CauseOfSamsara => {feeling_factor,reflection_factor}
OrderReasonForSeparateBases => {announced_order_reason}
SeparateBasePlacement => {feeling_factor,reflection_factor}
SeparatelyFrom => {(feeling_factor,remaining_factor_class),(reflection_factor,remaining_factor_class)}
MentalFactor => {feeling_factor,reflection_factor,another_factor}
PrincipalCause => {(feeling_factor,sensual_root),(reflection_factor,view_root)}
DisputeRoot => {sensual_root,view_root}
MediatedBy => {(feeling_factor,savor_mediation),(reflection_factor,inversion_mediation)}
SoleCause => {}
GreedyForSavor => {wandering_person}
InvertedReflection => {wandering_person}
Wanders => {wandering_person}
```

**Model checks.** Two factor representatives receive separate Base
placements while remaining mental factors. Their two root assignments
and mediations must not be swapped. The factors and the fixations have
different denotations; causing a root is not being that root.
An empty `SoleCause` extension rejects the inference from principal to
sole without enumerating every additional condition. The wandering
person witnesses both qualifications in one subject, not one person
for savor and another for inversion.

**Bhāṣya determination.** Savoring Feeling mediates attachment to sensual
desire; inverted Reflection mediates attachment to views. These are
qualified routes, not assertions that every Feeling is attachment or
every Reflection inverted. The order argument is promised in three
ways and deferred. No missing demonstration is supplied by the valuation.

**Organon interpretation.** The distinction is internal articulation:
separate Bases make different operative hinges explicit while preserving
their common mental-factor status. The schema must retain both the
shared class and the different functions, rather than convert separation
into unrelated substances. The earlier schematic follows.

```text
why not both only in the formations-base?

feeling
    → savor
    → fixation upon sensual desire
    → a root of dispute

reflection
    → inverted mark
    → fixation upon views
    → a root of dispute

greed for the savor
    and inverted reflection
    → the one who wanders

principal ≠ sole
order of the bases → 1.22
1.22 not opened
```

## 9. Interpretive Note

**Translation note.** The Bhāṣya names fixation on sensual desire and fixation
on views as the two roots of dispute. Feeling, through its savor, and
reflection, through inversion, are their respective principal causes and are
also principal causes of saṃsāra. It announces but defers a threefold
demonstration of the reason of order.

The hinge is *pṛthak*: apart, and still mental factors. Interpretation of the two roots is in the Bhāṣya.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_21 a vak:Karika ;
    vak:hasTopic vak:FeelingAndReflectionAsBases ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Feeling vak:remains vak:MentalFactor ;
    vak:hasSeparateBase true ;
    vak:isPrincipalCauseOf vak:SensualFixation .
vak:Reflection vak:remains vak:MentalFactor ;
    vak:hasSeparateBase true ;
    vak:isPrincipalCauseOf vak:ViewFixation .
vak:BaseOrder vak:deferredTo vak:VAK_1_22 .
```
