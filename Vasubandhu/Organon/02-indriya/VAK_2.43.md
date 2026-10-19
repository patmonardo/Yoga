# VAK_2.43 — The Attainment of Cessation

## 1. Sanskrit (Devanāgarī)

```sanskrit
निरोधाख्या तथैवेयं विहारार्थं भवाग्रजा ।
शुभा द्विवेद्यानियता चार्यस्याप्या प्रयोगतः ॥ २.४३ ॥
```

## 2. Sanskrit (IAST)

```text
nirodhākhyā tathaiveyaṃ vihārārthaṃ bhavāgrajā /
śubhā dvivedyāniyatā cāryasyāpyā prayogataḥ // 2.43 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| nirodha-ākhyā | nom. sg. f.; compound | called cessation |
| tathā eva | adverb + particle | likewise, that much |
| iyam | nom. sg. f.; pronoun | this attainment |
| vihāra-artham | acc. sg. n.; compound | for the sake of abiding |
| bhava-agra-jā | nom. sg. f.; compound | born of the summit of existence |
| śubhā | nom. sg. f. | wholesome |
| dvi-vedyā | nom. sg. f. + compound | to be experienced at two times |
| aniyatā | nom. sg. f. | unfixed |
| āryasya | gen. sg. m. | a noble person's |
| ca | conjunction | and; adds unfixed maturation |
| āpyā | nom. sg. f.; gerundive of √āp | to be acquired |
| prayogataḥ | adverbial ablative in -tas | through application |

The prose specifies peaceful abiding and the Essence of neither
reflection nor non-reflection. Unfixed concerns maturation, not
ethical indeterminacy. Sandhi is opened for parsing.

```text
# tokens: nirodhākhyā tathā eva iyam vihārārtham bhavāgrajā śubhā dvivedyā aniyatā ca āryasya āpyā prayogataḥ
```
## 4. Grammar

“Likewise” supplies cessation of consciousness and mental factors,
not the other attainment's purpose, level, or maturation timing.
The prose resolves the two times as next rebirth and a later
existence, while unfixed allows non-maturation. The acquisition
clause states the application rule for noble persons; the Buddha
exception is introduced by the following verse, not silently
folded into this clause.

```nltk-fcfg
% start S
# tokens: nirodhākhyā tathā eva iyam vihārārtham bhavāgrajā śubhā dvivedyā aniyatā ca āryasya āpyā prayogataḥ
S[SEM=<(?cessation & ?purpose & ?level & ?ethical & ?timing & ?acquisition)>] -> CESSATION[SEM=?cessation] PURPOSE[SEM=?purpose] LEVEL[SEM=?level] ETHICAL[SEM=?ethical] TIMING[SEM=?timing] ACQUISITION[SEM=?acquisition]
CESSATION[SEM=<CessationOf(attainment,consciousness_and_factors)>] -> NAMED[CASE=nom] LIKEWISE[CARRIES=cessation_only] EMPHATIC THIS[CASE=nom]
PURPOSE[SEM=<Purpose(attainment,peaceful_abiding)>] -> ABIDING[PURPOSE=peaceful_abiding]
LEVEL[SEM=<AtLevel(attainment,summit)>] -> SUMMIT[CASE=nom]
ETHICAL[SEM=<Wholesome(attainment)>] -> WHOLESOME[CASE=nom]
TIMING[SEM=<(all x.(MaturationOption(attainment,x) <-> (x = next_rebirth | x = later_existence)) & UnfixedMaturation(attainment))>] -> TWO[CNT=2] UNFIXED[AXIS=maturation] AND
ACQUISITION[SEM=<(RestrictedTo(attainment,noble) & AcquisitionRule(attainment,application))>] -> NOBLE[CASE=gen] ACQUIRABLE[CASE=nom] APPLICATION[FORM=tas]
NAMED[CASE=nom] -> 'nirodhākhyā'
LIKEWISE[CARRIES=cessation_only] -> 'tathā'
EMPHATIC -> 'eva'
THIS[CASE=nom] -> 'iyam'
ABIDING[PURPOSE=peaceful_abiding] -> 'vihārārtham'
SUMMIT[CASE=nom] -> 'bhavāgrajā'
WHOLESOME[CASE=nom] -> 'śubhā'
TWO[CNT=2] -> 'dvivedyā'
UNFIXED[AXIS=maturation] -> 'aniyatā'
AND -> 'ca'
NOBLE[CASE=gen] -> 'āryasya'
ACQUIRABLE[CASE=nom] -> 'āpyā'
APPLICATION[FORM=tas] -> 'prayogataḥ'
```

```nltk-dep
'nirodhākhyā' -> 'tathā' | 'iyam' | 'vihārārtham' | 'bhavāgrajā' | 'śubhā' | 'dvivedyā' | 'āpyā'
'tathā' -> 'eva'
'dvivedyā' -> 'aniyatā' | 'ca'
'āpyā' -> 'āryasya' | 'prayogataḥ'
```

The six constituent lengths are 4, 1, 1, 1, 3, and 3.

## 5. Translation

### Literal Translation

> This attainment, called cessation, is likewise for the sake of abiding and
> is born of the summit of existence. It is wholesome, to be experienced at
> two times or unfixed, belongs to a noble person, and is acquired through
> application.
### Bhāṣya-informed study translation

> The attainment called cessation is likewise cessation of consciousness
> and the mental factors. It is entered for peaceful abiding and belongs
> to the summit of existence. It is wholesome; its maturation may be
> experienced in the next rebirth or a later existence, or may not occur.
> It is restricted to noble persons and is acquired through application.
## 6. Philosophical Translation

> The shared cessation does not erase different purposes and levels:
> peaceful abiding at the summit is not escape sought in fourth dhyāna.
> Wholesomeness does not guarantee maturation. Acquisition through
> application is the stated rule; the Buddha exception is developed
> in the following verse.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| nirodha-samāpatti | attainment of cessation | the second attainment |
| vihārārtha | for abiding | attention preceded by reflection on peaceful abiding |
| bhavāgra | summit of existence | the level |
| naivasaṃjñā-nāsaṃjñā | neither reflection nor non-reflection | the Essence specifying the summit's level |
| dvi-vedya | two times | next rebirth, or later |
| aniyata | unfixed | may not mature |
| prayoga | application | the noble-person acquisition rule, with the Buddha exception in 2.44 |
| kṣaya-jñāna | Knowledge of exhaustion | cross-verse Buddha-acquisition discussion |

## 8. Logical Determination

```nltk-sem
timing : all x.(MaturationOption(attainment,x) <-> (x = next_rebirth | x = later_existence))
acquisition : (RestrictedTo(attainment,noble) & AcquisitionRule(attainment,application))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(CessationOf(attainment,consciousness_and_factors) & Purpose(attainment,peaceful_abiding) & AtLevel(attainment,summit) & Wholesome(attainment) & (all x.(MaturationOption(attainment,x) <-> (x = next_rebirth | x = later_existence)) & UnfixedMaturation(attainment)) & (RestrictedTo(attainment,noble) & AcquisitionRule(attainment,application)))

# THEORY prose_distinctions
# EXPECT prose_distinctions T
ResultBaseCount(attainment,four_bases) & CanFailToMature(attainment)
-PastAcquired(attainment) & -FutureCultivated(attainment) & -DispassionAcquisitionRule(attainment)

# THEORY crossverse_disputed_accounts
# EXPECT crossverse_disputed_accounts T
AcquisitionAt(buddha,knowledge_of_exhaustion) & MasteryWithoutPriorProduction(mastery_reply)
EarlierProduction(western_account) & -EarlierProduction(kashmir_account) & ReportedMomentCount(kashmir_account,thirty_four)

# THEORY rejected_unfixed_is_ethical_indeterminate
# EXPECT rejected_unfixed_is_ethical_indeterminate F
Wholesome(attainment) & EthicallyIndeterminate(attainment)

# THEORY rejected_necessary_next_rebirth_maturation
# EXPECT rejected_necessary_next_rebirth_maturation F
all x.(MaturationOption(attainment,x) -> (x = next_rebirth))

# THEORY rejected_merging_prior_production_accounts
# EXPECT rejected_merging_prior_production_accounts F
EarlierProduction(kashmir_account) & EarlierProduction(western_account)
```

```nltk-valuation
attainment => cessation_attainment
consciousness_and_factors => consciousness_factor_group
peaceful_abiding => peaceful_abiding_purpose
summit => summit_level
next_rebirth => next_rebirth_period
later_existence => later_existence_period
noble => noble_person_class
application => application_method
four_bases => four_base_count
buddha => buddha_case
knowledge_of_exhaustion => exhaustion_knowledge_moment
mastery_reply => mastery_reply_account
western_account => western_teachers
kashmir_account => kashmir_teachers
thirty_four => thirty_four_count
CessationOf => {(cessation_attainment,consciousness_factor_group)}
Purpose => {(cessation_attainment,peaceful_abiding_purpose)}
AtLevel => {(cessation_attainment,summit_level)}
Wholesome => {cessation_attainment}
MaturationOption => {(cessation_attainment,next_rebirth_period),(cessation_attainment,later_existence_period)}
UnfixedMaturation => {cessation_attainment}
RestrictedTo => {(cessation_attainment,noble_person_class)}
AcquisitionRule => {(cessation_attainment,application_method)}
ResultBaseCount => {(cessation_attainment,four_base_count)}
CanFailToMature => {cessation_attainment}
PastAcquired => {}
FutureCultivated => {}
DispassionAcquisitionRule => {}
EthicallyIndeterminate => {}
AcquisitionAt => {(buddha_case,exhaustion_knowledge_moment)}
MasteryWithoutPriorProduction => {mastery_reply_account}
EarlierProduction => {western_teachers}
ReportedMomentCount => {(kashmir_teachers,thirty_four_count)}
```

The timing options are alternatives, not two mandatory results.
The count predicate labels the four-Base maturation, not four
simultaneous attainment tokens. Cross-verse accounts are indexed
by speaker; the model tests that they are not merged, not which
one is historically or doctrinally true. The reported thirty-four
is checked as 16 + 2 × 9 = 34 in the regression test.

## 9. Interpretive Note

**Translation note.** Attention preceded by reflection on peaceful
abiding differs from the non-reflective attainment's escape motive.
The summit is the level of the Essence of neither reflection nor
non-reflection. Unfixed maturation can mean no maturation at all,
not an ethically indeterminate attainment.

The inherited Bhāṣya extends into the first half of 2.44, where
the Buddha exception and prior-production debate occur; that
continuation is explicitly labeled, not attributed to this verse.
The shared Basis of the two attainments belongs to the remaining
2.44 discussion. *Kila* qualifies the reported thirty-four moments;
the damaged sentence about non-emergence remains uncertain.

In the Organon reading, Cognition joins and governs Perception and
Conception and guides the Dharma Base, remaining distinct from
consciousness and Mind. Sharing a cessation-description does not
erase differences of purpose, level, result, and acquisition.
Neither temporary cessation nor mastery over it is silently
identified with liberation.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_43 a vak:Karika ; vak:hasTopic vak:AttainmentOfCessation .
vak:LikewiseIn2_43 vak:carries vak:ConsciousnessAndFactorCessation .
vak:CessationAttainment vak:purpose vak:PeacefulAbiding ;
    vak:maturationTiming vak:NextRebirth, vak:LaterExistence ;
    vak:canFailToMature true .
```
