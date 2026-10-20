# VAK_2.53 — Application, and the Associated Cause

## 1. Sanskrit (Devanāgarī)

```sanskrit
प्रयोगजास्तयोरेव श्रुतचिन्तामयादिकाः ।
संप्रयुक्तकहेतुस्तु चित्तचैत्ताः समाश्रयाः ॥ २.५३ ॥
```

## 2. Sanskrit (IAST)

```text
prayogajās tayor eva śrutacintāmayādikāḥ /
saṃprayuktakahetus tu cittacaittāḥ samāśrayāḥ // 2.53 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| prayogajāḥ | masculine nominative plural compound adjective | produced by application |
| tayoḥ eva | genitive dual pronoun + emphatic particle | of the equal and superior alone, resumed from 2.52 |
| śruta-cintā-maya-ādikāḥ | masculine nominative plural compound adjective | qualities born of hearing and thought, with cultivation supplied by the Bhāṣya |
| saṃprayuktaka-hetuḥ | masculine nominative singular compound | associated cause |
| citta-caittāḥ | masculine nominative plural coordinated compound | consciousness and the mental factors |
| samāśrayāḥ | masculine nominative plural compound adjective | sharing numerically the same support moment, per the Bhāṣya |

**Grammar tokens.** External sandhi is opened at *prayogajās tayor* and *hetus tu*. *Tayoḥ* resumes the equal and superior from 2.52; the Bhāṣya identifies the open *ādi* as cultivation.

```text
# tokens: prayogajāḥ tayoḥ eva śrutacintāmayādikāḥ saṃprayuktakahetuḥ tu cittacaittāḥ samāśrayāḥ
```

## 4. Grammar

```nltk-fcfg
% start S
# tokens: prayogajāḥ tayoḥ eva śrutacintāmayādikāḥ saṃprayuktakahetuḥ tu cittacaittāḥ samāśrayāḥ
S[SEM=<(?application & ?association)>] -> APPLICATION[SEM=?application] ASSOCIATION[SEM=?association]
APPLICATION[SEM=<(ApplicationBorn(hearing) & ApplicationBorn(thought) & CauseFor(hearing,equal) & CauseFor(hearing,superior) & CauseFor(thought,equal) & CauseFor(thought,superior))>] -> PRODUCED[CASE=nom,NUM=pl] RANGE[CASE=gen,NUM=du,REF=equal_superior] ONLY EXAMPLES[CASE=nom,NUM=pl,OPEN=true]
PRODUCED[CASE=nom,NUM=pl] -> 'prayogajāḥ'
RANGE[CASE=gen,NUM=du,REF=equal_superior] -> 'tayoḥ'
ONLY -> 'eva'
EXAMPLES[CASE=nom,NUM=pl,OPEN=true] -> 'śrutacintāmayādikāḥ'
ASSOCIATION[SEM=<(AssociatedCause(citta,caitta) & SameSupport(citta,caitta))>] -> HEAD[CASE=nom,NUM=sg] CONTRAST PAIR[CASE=nom,NUM=pl] SUPPORT[CASE=nom,NUM=pl,IDENTITY=same]
HEAD[CASE=nom,NUM=sg] -> 'saṃprayuktakahetuḥ'
CONTRAST -> 'tu'
PAIR[CASE=nom,NUM=pl] -> 'cittacaittāḥ'
SUPPORT[CASE=nom,NUM=pl,IDENTITY=same] -> 'samāśrayāḥ'
```

```nltk-dep
'prayogajāḥ' -> 'tayoḥ' | 'eva' | 'śrutacintāmayādikāḥ'
'saṃprayuktakahetuḥ' -> 'tu' | 'cittacaittāḥ' | 'samāśrayāḥ'
```

**Feature chart checkpoints.** Application spans [0, 4), association [4, 8), and the root [0, 8). Changing the resumed dual to singular, the associated pair to singular, or shared-support identity blocks the parse. The verse's open *ādi* does not itself enumerate cultivation.

## 5. Translation

### Literal Translation

> Application-produced [qualities] are causes of those two alone: those
> born of hearing, thought, and the rest. The associated cause is
> consciousness and mental factors of the same support.
### Bhāṣya-informed study translation

> Application-produced qualities are homogeneous causes of the equal or
> superior only: those born of hearing, thought, and cultivation.
> Associated cause is consciousness and mental factors sharing one
> support.
## 6. Philosophical Translation

> Application gives worldly qualities a directed homogeneous-cause range: equal or superior results. Association adds a different causal determination for consciousness and mental factors sharing one support. The Bhāṣya tests that support against apparent matches across different continua.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| prayogaja | produced by application | not by birth |
| cintāmaya | born of thought | not saṃjñā |
| pañca-samatā | five equalities | Bhāṣya account of association; do not infer all five from *samāśraya* alone |
| samāśraya | same support | the identical faculty moment, not merely the same kind |

## 8. Logical Determination

**Kārikā, derived.** The root `SEM` carries the equal/superior antecedent into the application clause and treats same support as the associated-cause predicate. The Bhāṣya supplies cultivation, the scope across realms, and the necessary identity of a faculty moment; these are separate prose theories.

```nltk-sem
application : ApplicationBorn(hearing) & ApplicationBorn(thought) & CauseFor(hearing,equal) & CauseFor(hearing,superior) & CauseFor(thought,equal) & CauseFor(thought,superior)
association : AssociatedCause(citta,caitta) & SameSupport(citta,caitta)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(ApplicationBorn(hearing) & ApplicationBorn(thought) & CauseFor(hearing,equal) & CauseFor(hearing,superior) & CauseFor(thought,equal) & CauseFor(thought,superior)) & (AssociatedCause(citta,caitta) & SameSupport(citta,caitta))

# THEORY prose_cultivation
# EXPECT prose_cultivation T
ApplicationBorn(cultivation) & CauseFor(cultivation,equal) & CauseFor(cultivation,superior)

# THEORY prose_association_and_coarising
# EXPECT prose_association_and_coarising T
all x.all y.(AssociatedCause(x,y) -> CoarisenCause(x,y)) & CoarisenCause(citta,caitta)

# THEORY rejected_inferior_application
# EXPECT rejected_inferior_application F
CauseFor(hearing,inferior) & ApplicationBorn(hearing)

# THEORY rejected_same_kind_suffices
# EXPECT rejected_same_kind_suffices F
AssociatedCause(citta,other_caitta) & SameKindSupport(citta,other_caitta)

# THEORY rejected_coarisen_converse
# EXPECT rejected_coarisen_converse F
all x.all y.(CoarisenCause(x,y) -> AssociatedCause(x,y))
```

```nltk-valuation
hearing => h
thought => t
cultivation => v
equal => eq
superior => sup
inferior => inf
citta => c
caitta => m
other_caitta => n
mark => k
ApplicationBorn => {h,t,v}
CauseFor => {(h,eq),(h,sup),(t,eq),(t,sup),(v,eq),(v,sup)}
AssociatedCause => {(c,m),(m,c)}
SameSupport => {(c,m),(m,c)}
SameKindSupport => {(c,n)}
CoarisenCause => {(c,m),(m,c),(c,k)}
```

The finite model confirms the verse cases and rejects an inferior application result, same-kind support across another continuum, and the converse from co-arisen cause to associated cause. The Bhāṣya pass below tests why those distinctions matter; its models witness this reading without proving a textual emendation.

## 9. Interpretive Note

The Bhāṣya explicitly supplies *bhāvanāmaya* (born of cultivation) under the verse's *ādi* and specifies the available hearing/thought/cultivation series by realm. The applied qualities cause an equal or superior result, not an inferior one. Birth-acquired wholesome and afflicted dharmas are treated differently. The four unobscured-indeterminate sorts have their own descending causal range; these details are prose specifications, not new words in the verse.

For associated cause, sameness of aspect, object, and time does not yet secure association: different continua can share those descriptions. *Samāśraya* requires the identical faculty moment. The Bhāṣya then distinguishes association by five equalities from co-arisen cause by mutual result. The reported unarisen case in the homogeneous-cause discussion remains textually delicate and is not converted into a new universal rule here.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_53 a vak:Karika ; vak:hasTopic vak:AssociatedCause .
vak:SameSupport vak:numerical true .
```
