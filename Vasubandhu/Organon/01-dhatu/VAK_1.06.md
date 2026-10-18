# VAK_1.06 — The Two Cessations

## 1. Sanskrit (Devanāgarī)

```sanskrit
प्रतिसंख्यानिरोधो यो विसंयोगः पृथक् पृथक् ।
उत्पादात्यन्तविघ्नोऽन्यो निरोधोऽप्रतिसंख्यया ॥ १.०६ ॥
```

## 2. Sanskrit (IAST)

```text
pratisaṃkhyānirodho yo visaṃyogaḥ pṛthak pṛthak /
utpādātyantavighno 'nyo nirodho 'pratisaṃkhyayā // 1.06 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| pratisaṃkhyā-nirodhaḥ | tatpuruṣa; nominative singular | cessation through discrimination; the first named in 1.05 |
| yaḥ | relative pronoun | which |
| visaṃyogaḥ | nominative singular | disjunction; the definition |
| pṛthak pṛthak | iterated indeclinable | separately, and separately |
| utpāda-atyanta-vighnaḥ | compound; nominative singular | absolute obstruction of arising |
| anyaḥ | nominative singular | the other |
| nirodhaḥ | nominative singular | cessation |
| apratisaṃkhyayā | instrumental | not through discrimination |

**Grammar tokens.** Verse-order IAST with sandhi opened. Both occurrences
of *pṛthak* are retained. The two defining compounds remain whole leaves.
No covert word is needed; Impure dharmas and future arising are restrictions
resolved from the Bhāṣya in the semantic vocabulary.

```text
# tokens: pratisaṃkhyā-nirodhaḥ yaḥ visaṃyogaḥ pṛthak pṛthak utpāda-atyanta-vighnaḥ anyaḥ nirodhaḥ apratisaṃkhyayā
```

## 4. Grammar

Two nominal definitions continue the dual roster of 1.05. Masculine
singular *yaḥ* links cessation through discrimination with disjunction.
Repeated *pṛthak* distributes it case by case. In the second clause,
*anyaḥ* agrees with *nirodhaḥ*; the instrumental denies attainment through
discrimination, not cessation itself.

```nltk-fcfg
% start S
# tokens: pratisaṃkhyā-nirodhaḥ yaḥ visaṃyogaḥ pṛthak pṛthak utpāda-atyanta-vighnaḥ anyaḥ nirodhaḥ apratisaṃkhyayā
S[SEM=<(?first & ?second)>] -> FIRST[SEM=?first] SECOND[SEM=?second]
FIRST[SEM=<?each(?definition(?kind)(?disjunction))>] -> KIND[CASE=nom,NUM=?n,GEN=?g,SEM=?kind] REL[CASE=nom,NUM=?n,GEN=?g,SEM=?definition] DISJUNCTION[CASE=nom,NUM=?n,GEN=?g,SEM=?disjunction] EACH[SEM=?each] EACH
SECOND[SEM=<?without(?other(?block)(?cessation))>] -> BLOCK[CASE=nom,NUM=?n,GEN=?g,SEM=?block] OTHER[CASE=nom,NUM=?n,GEN=?g,SEM=?other] CESSATION[CASE=nom,NUM=?n,GEN=?g,SEM=?cessation] WITHOUT[CASE=ins,SEM=?without]
KIND[CASE=nom,NUM=sg,GEN=m,SEM=<\x.DiscriminativeCessation(x)>] -> 'pratisaṃkhyā-nirodhaḥ'
REL[CASE=nom,NUM=sg,GEN=m,SEM=<\P.\Q.all x.(P(x) <-> Q(x))>] -> 'yaḥ'
DISJUNCTION[CASE=nom,NUM=sg,GEN=m,SEM=<\x.DisjunctionFromImpure(x)>] -> 'visaṃyogaḥ'
EACH[SEM=<\P.(P & all x.(DiscriminativeCessation(x) -> Casewise(x)))>] -> 'pṛthak'
BLOCK[CASE=nom,NUM=sg,GEN=m,SEM=<\x.AbsoluteObstructionOfFutureArising(x)>] -> 'utpāda-atyanta-vighnaḥ'
OTHER[CASE=nom,NUM=sg,GEN=m,SEM=<\P.\Q.all x.(OtherCessation(x) -> (P(x) & Q(x)))>] -> 'anyaḥ'
CESSATION[CASE=nom,NUM=sg,GEN=m,SEM=<\x.Cessation(x)>] -> 'nirodhaḥ'
WITHOUT[CASE=ins,SEM=<\P.(P & all x.(OtherCessation(x) -> -AttainedByDiscrimination(x)))>] -> 'apratisaṃkhyayā'
```

```nltk-dep
'pratisaṃkhyā-nirodhaḥ' -> 'yaḥ' | 'visaṃyogaḥ'
'visaṃyogaḥ' -> 'pṛthak'
'nirodhaḥ' -> 'utpāda-atyanta-vighnaḥ' | 'anyaḥ' | 'apratisaṃkhyayā'
```

**Close construe.** Cessation through discrimination is disjunction,
separately in each case. The other cessation, not through discrimination,
is absolute obstruction of arising.

The first definition does not make one realization discharge every
conjunction. `Casewise` preserves that distribution; its complete
conjunction-to-disjunction mapping is not encoded here. The Bhāṣya explains
the other cessation through deficiency of conditions, not destructive
action by an agent. Neither cessation is a conditioned event: their
attainment must be distinguished from producing an unconditioned Dharma.

## 5. Translation

### Literal Translation

> Cessation through discrimination is disjunction, separately and
> separately. The other cessation, not through discrimination, is the
> absolute obstruction of arising.

### Bhāṣya-informed study translation

> Cessation through discriminative comprehension is disjunction from
> Impure dharmas, separately in each case. The other cessation, not through
> discriminative comprehension, is an absolute obstruction to the arising
> of a future dharma.

## 6. Philosophical Translation

Two cessations, two attainments. They are not the same unconditioned.

The first is disjunction. It is item by item. One seeing does not end every conjunction. If it did, the rest of the Path would be useless.

The second is not that Path. A future arising is absolutely blocked because the conditions fail. What has passed cannot be taken. Liberation and mere non-production are not one cessation.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| pratisaṃkhyā | discrimination | a particular prajñā of the Noble Truths |
| nirodha | cessation | unconditioned here; the two are not one |
| visaṃyoga | disjunction | from impure dharmas |
| pṛthak pṛthak | separately | as many disjunctions as conjunctions |
| sāsrava | impure | the field of the first cessation |
| anāsrava | pure | no disjunction required where it can arise |
| apratisaṃkhyā | not through discrimination | not attained by that prajñā |
| utpāda-atyanta-vighna | absolute obstruction of arising | the second definition |
| pratyaya-vaikalya | deficiency of conditions | how the second is got |

## 8. Logical Determination

**Kārikā, derived.** `OtherCessation` is the second member of 1.05's
roster, not every cessation outside the first. Its scope is fixed here.

```nltk-sem
# derived by the section 4 parse
(((all x.(DiscriminativeCessation(x) <-> DisjunctionFromImpure(x))) & (all x.(DiscriminativeCessation(x) -> Casewise(x)))) & ((all x.(OtherCessation(x) -> (AbsoluteObstructionOfFutureArising(x) & Cessation(x)))) & (all x.(OtherCessation(x) -> -AttainedByDiscrimination(x)))))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(((all x.(DiscriminativeCessation(x) <-> DisjunctionFromImpure(x))) & (all x.(DiscriminativeCessation(x) -> Casewise(x)))) & ((all x.(OtherCessation(x) -> (AbsoluteObstructionOfFutureArising(x) & Cessation(x)))) & (all x.(OtherCessation(x) -> -AttainedByDiscrimination(x)))))
# THEORY prose
# EXPECT prose T
all x.(DiscriminativeCessation(x) -> (Cessation(x) & AttainedByDiscrimination(x)))
all x.(OtherCessation(x) -> ThroughDeficiencyOfConditions(x))
all x.(Cessation(x) -> Unconditioned(x))
# THEORY rejected_obstruction_is_disjunction
# EXPECT rejected_obstruction_is_disjunction F
all x.(OtherCessation(x) -> DisjunctionFromImpure(x))
```

```nltk-valuation
DiscriminativeCessation => {release_one,release_two}
DisjunctionFromImpure => {release_one,release_two}
Casewise => {release_one,release_two}
OtherCessation => {blocked}
AbsoluteObstructionOfFutureArising => {blocked}
Cessation => {release_one,release_two,blocked}
AttainedByDiscrimination => {release_one,release_two}
ThroughDeficiencyOfConditions => {blocked}
Unconditioned => {release_one,release_two,blocked}
```

**Model checks.** Two disjunctions exemplify casewise differentiation,
not a claim that the first cessation has only two instances. Removing
one case's distribution or assigning discriminative attainment to the
other cessation must fail. The model refutes the conflation of
non-production through deficient conditions with liberating disjunction.

**Bhāṣya determination.** The four acquisition cases below concern
Dharmas for which cessations are obtained, not four kinds of cessation.
They preserve the distinction between the unconditioned cessation and
the conditioned history of its attainment.

```text
cessation through discrimination
    = disjunction from impure dharmas
    = one per conjunction
    = attained by discrimination

cessation not through discrimination
    = absolute obstruction of arising
    = deficiency of conditions
    = not attained by discrimination
```

```text
impure, able to arise                 first only
pure and conditioned, unable          second only
impure, unable to arise               both
pure, able to arise                   neither
```

## 9. Interpretive Note

**Translation note.** The Bhāṣya explains that discriminative comprehension here is the prajñā that considers the Noble Truths and that there are as many disjunctions as conjunctions. It distinguishes this separately attained cessation from the other cessation, which blocks a future dharma's arising when its conditions are absent.

The first cessation is not nothing. It is disjunction, separately. The second is not that disjunction. A future dharma is blocked because its conditions are gone. The eye and the mind occupied with one Form cannot later take what has already passed.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_06 a vak:Karika ;
    vak:hasTopic vak:TwoCessations ;
    vak:belongsTo vak:Dhatunirdesa .

vak:PratisamkhyaNirodha a vak:UnconditionedDharma, vak:PureDharma ;
    vak:definedAs vak:Disjunction ;
    vak:attainedBy vak:Discrimination .

vak:ApratisamkhyaNirodha a vak:UnconditionedDharma, vak:PureDharma ;
    vak:definedAs vak:AbsoluteObstructionOfArising ;
    vak:attainedBy vak:DeficiencyOfConditions .
```
