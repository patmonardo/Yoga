# VAK_2.44 — Awakening, Basis, and First Production

## 1. Sanskrit (Devanāgarī)

```sanskrit
बोधिलभ्या मुनेर्न प्राक् चतुस्त्रिंशत्क्षणाप्तितः ।
कामरूपाश्रये भूते निरोधाख्यादितो नृषु ॥ २.४४ ॥
```

## 2. Sanskrit (IAST)

```text
bodhilabhyā muner na prāk catustriṃśatkṣaṇāptitaḥ /
kāmarūpāśraye bhūte nirodhākhyādito nṛṣu // 2.44 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| bodhi-labhyā | nom. sg. f.; compound | acquired with awakening |
| muneḥ | gen. sg. m. | the Sage |
| na prāk | negation + adverb | not beforehand |
| catustriṃśat-kṣaṇa-āptitaḥ | adverbial ablative in -tas; compound | because of attainment in thirty-four moments |
| kāma-rūpa-āśraye | loc. sg. m.; compound | with a Desire- or Form-Realm Basis |
| bhūte | loc. sg. m.; past participle | when that Basis is present |
| nirodha-ākhyā | nom. sg. f.; compound | the attainment called cessation |
| āditaḥ | adverb | at first |
| nṛṣu | loc. pl. m. | among humans |

Basis is not the attainment's level. The opening singular concerns
cessation attainment; “both” is supplied only in the Basis clause.
The no-prior-production explanation is the Kāśmīra account,
disputed in the prose rather than endorsed by all speakers.

```text
# tokens: bodhilabhyā muneḥ na prāk catustriṃśatkṣaṇāptitaḥ kāmarūpāśraye bhūte nirodhākhyā āditaḥ nṛṣu
```
## 4. Grammar

The first five tokens complete the acquisition argument begun in
2.43. The next two supply the shared Basis of both attainments;
this does not transfer awakening-acquisition to non-reflective
attainment. The last three restrict first production of cessation
attainment to humans. Later Form-Realm production and the disputed
loss argument are explained in the prose, not this last predicate.

```nltk-fcfg
% start S
# tokens: bodhilabhyā muneḥ na prāk catustriṃśatkṣaṇāptitaḥ kāmarūpāśraye bhūte nirodhākhyā āditaḥ nṛṣu
S[SEM=<(?awakening & ?basis & ?first)>] -> AWAKENING[SEM=?awakening] BASIS[SEM=?basis] FIRST[SEM=?first]
AWAKENING[SEM=<(AcquiredWithAwakening(sage,cessation) & DeniesPriorProduction(kashmir_account,cessation) & ReportedCount(kashmir_account,thirty_four))>] -> AWAKENINGACQUIRED[CASE=nom,NUM=sg,REF=cessation] SAGE[CASE=gen] NOT BEFORE REASON[FORM=tas,CNT=34]
BASIS[SEM=<all x y.((Attainment(x) & BasisRealm(y)) -> CanAriseWithBasis(x,y))>] -> REALMBASIS[CASE=loc,CNT=2] PRESENT[CASE=loc]
FIRST[SEM=<all x.(FirstProductionAmong(cessation,x) <-> (x = humans))>] -> CESSATION[CASE=nom] INITIALLY[SCOPE=first_production] HUMANS[CASE=loc,NUM=pl]
AWAKENINGACQUIRED[CASE=nom,NUM=sg,REF=cessation] -> 'bodhilabhyā'
SAGE[CASE=gen] -> 'muneḥ'
NOT -> 'na'
BEFORE -> 'prāk'
REASON[FORM=tas,CNT=34] -> 'catustriṃśatkṣaṇāptitaḥ'
REALMBASIS[CASE=loc,CNT=2] -> 'kāmarūpāśraye'
PRESENT[CASE=loc] -> 'bhūte'
CESSATION[CASE=nom] -> 'nirodhākhyā'
INITIALLY[SCOPE=first_production] -> 'āditaḥ'
HUMANS[CASE=loc,NUM=pl] -> 'nṛṣu'
```

```nltk-dep
'bodhilabhyā' -> 'muneḥ' | 'prāk' | 'catustriṃśatkṣaṇāptitaḥ'
'prāk' -> 'na'
'kāmarūpāśraye' -> 'bhūte'
'nirodhākhyā' -> 'āditaḥ' | 'nṛṣu'
```

The three constituent lengths are 5, 2, and 3. The denial and count
are explicitly indexed to the account identified by the commentary;
this resolves the verse's argumentative voice without conflating
the contrary western proposal.

## 5. Translation

### Literal Translation

> For the Sage, [cessation attainment] is acquired with awakening,
> not beforehand, because of attainment in thirty-four moments.
> [Both occur] when a Desire- or Form-Realm Basis is present.
> The attainment called cessation [is produced] initially among humans.
### Bhāṣya-informed study translation

> For the Sage, the attainment of cessation is acquired with awakening,
> not beforehand, since awakening is attained in thirty-four moments.
> Both attainments arise with a Desire- or Form-Realm Basis.
> The attainment called cessation is first produced among humans.
## 6. Philosophical Translation

> Basis and level remain distinct. Human first production does not
> preclude later Form-Realm production. The account requiring prior
> loss is disputed through a different level-assignment. The return
> of consciousness and the status of cessation as entity or designation
> remain questions argued by different speakers.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| āśraya | Basis | Desire or Form Realm; not the attainment's level |
| āditaḥ | at first | humans only |
| saṃjñā-vedayita-nirodha | cessation of reflection and feeling | the sūtra name |
| vyutkrānta | out of order | mastery, not the beginner |
| samanantara-pratyaya | immediately preceding Condition | the Vaibhāṣika appeal to past consciousness's existence |
| anyonya-bījaka | seed of one another | the earlier teachers |
| acittikā | without consciousness | the Vaibhāṣika close |

## 8. Logical Determination

```nltk-sem
basis : all x y.((Attainment(x) & BasisRealm(y)) -> CanAriseWithBasis(x,y))
first_production : all x.(FirstProductionAmong(cessation,x) <-> (x = humans))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((AcquiredWithAwakening(sage,cessation) & DeniesPriorProduction(kashmir_account,cessation) & ReportedCount(kashmir_account,thirty_four)) & all x y.((Attainment(x) & BasisRealm(y)) -> CanAriseWithBasis(x,y)) & all x.(FirstProductionAmong(cessation,x) <-> (x = humans)))

# THEORY prose_level_and_later_production
# EXPECT prose_level_and_later_production T
AtLevel(cessation,summit) & AtLevel(nonreflective,fourth_dhyana)
LaterProductionAmong(cessation,form_realm) & RequiresPriorLoss(main_account,cessation) & -RequiresPriorLoss(other_school,cessation)

# THEORY reported_return_positions
# EXPECT reported_return_positions T
ConsciousInAttainment(vasumitra_account) & -ConsciousInAttainment(vaibhasika_account)
MutualSeedAccount(earlier_teachers) & PastConditionAccount(vaibhasika_account)

# THEORY rejected_buddha_acquisition_applies_to_both
# EXPECT rejected_buddha_acquisition_applies_to_both F
all x.(Attainment(x) -> AcquiredWithAwakening(sage,x))

# THEORY rejected_basis_equals_attainment_level
# EXPECT rejected_basis_equals_attainment_level F
all x y.(CanAriseWithBasis(x,y) -> AtLevel(x,y))

# THEORY rejected_human_restriction_applies_to_all_later_production
# EXPECT rejected_human_restriction_applies_to_all_later_production F
all x.(LaterProductionAmong(cessation,x) -> (x = humans))
```

```nltk-valuation
sage => sage_person
cessation => cessation_attainment
nonreflective => nonreflective_attainment
kashmir_account => kashmir_teachers
thirty_four => thirty_four_count
humans => human_class
form_realm => form_realm_basis
summit => summit_level
fourth_dhyana => fourth_dhyana_level
main_account => summit_and_loss_account
other_school => fourth_dhyana_school
vasumitra_account => vasumitra_position
vaibhasika_account => vaibhasika_position
earlier_teachers => earlier_teachers_position
AcquiredWithAwakening => {(sage_person,cessation_attainment)}
DeniesPriorProduction => {(kashmir_teachers,cessation_attainment)}
ReportedCount => {(kashmir_teachers,thirty_four_count)}
Attainment => {cessation_attainment,nonreflective_attainment}
BasisRealm => {desire_realm_basis,form_realm_basis}
CanAriseWithBasis => {(cessation_attainment,desire_realm_basis),(cessation_attainment,form_realm_basis),(nonreflective_attainment,desire_realm_basis),(nonreflective_attainment,form_realm_basis)}
FirstProductionAmong => {(cessation_attainment,human_class)}
AtLevel => {(cessation_attainment,summit_level),(nonreflective_attainment,fourth_dhyana_level)}
LaterProductionAmong => {(cessation_attainment,form_realm_basis)}
RequiresPriorLoss => {(summit_and_loss_account,cessation_attainment)}
ConsciousInAttainment => {vasumitra_position}
MutualSeedAccount => {earlier_teachers_position}
PastConditionAccount => {vaibhasika_position}
```

The Basis matrix has four class-level options; it does not state
that every person can enter either attainment. Reported return
positions are indexed, not merged into one ontology. The first
half's full argument is retained in the preceding paired Bhāṣya
and linked from this one; the same debate is not silently treated
as universally accepted.

## 9. Interpretive Note

**Translation note.** The awakening clause is singular. The shared
Basis clause alone concerns both attainments. The loss requirement
follows within the summit-level account; another school assigns
cessation also to fourth dhyāna and so avoids that inference,
but its assignment is challenged. The damaged *pañcavyavacāra*
quotation remains marked rather than expanded into five destinies.

In the Organon reading, Cognition joins and governs Perception and
Conception and guides the Dharma Base, remaining distinct from
consciousness and Mind. A shared Basis is not identity of level,
purpose, or acquisition. Explaining the return of consciousness
also requires distinguishing a condition for resumption from
the separate claim that the intervening non-operation is a real
entity. Life begins the next topic.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_44 a vak:Karika ; vak:hasTopic vak:BasisAndFirstProduction .
vak:CessationAttainment vak:firstProducedAmong vak:Humans .
vak:BasisRealm vak:distinctFrom vak:AttainmentLevel .
vak:ReturnOfConsciousness vak:settled false .
```
