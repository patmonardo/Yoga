# VAK_2.37 — The Acquisition Matrix

## 1. Sanskrit (Devanāgarī)

```sanskrit
त्रैयध्विकानां त्रिविधा शुभादीनां शुभादिका ।
स्वधातुका तदाप्तानामनाप्तानां चतुर्विधा ॥ २.३७ ॥
```

## 2. Sanskrit (IAST)

```text
traiyadhvikānāṃ trividhā śubhādīnāṃ śubhādikā /
svadhātukā tadāptānām anāptānāṃ caturvidhā // 2.37 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| traiyadhvikānām | gen. pl. m.; adjective | of dharmas of the three times |
| trividhā | nom. sg. f. | threefold |
| śubhādīnām | gen. pl. m.; compound | of wholesome and the rest |
| śubhādikā | nom. sg. f.; compound | correspondingly wholesome and so forth |
| svadhātukā | nom. sg. f.; adjective | of the same realm |
| tadāptānām | gen. pl. m.; compound | of those included in that realm |
| anāptānām | gen. pl. m.; past passive participle | of those not included in a realm |
| caturvidhā | nom. sg. f. | fourfold |

Here *dhātu* means Realm; *anāpta* means not realm-included, not
unacquired. The prose supplies acquisition as the feminine subject.

```text
# tokens: traiyadhvikānām trividhā śubhādīnām śubhādikā svadhātukā tadāptānām anāptānām caturvidhā
```

## 4. Grammar

Four clauses classify acquisition by time, ethical status, Realm,
and the combined range for uncontaminated dharmas. The first clause
does not identify the dharma's time with its acquisition's time.
The prose's *yathākramam* makes the ethical and Realm clauses
respectively matched, not unrestricted cross-products.

```nltk-fcfg
% start S
# tokens: traiyadhvikānām trividhā śubhādīnām śubhādikā svadhātukā tadāptānām anāptānām caturvidhā
S[SEM=<(?time & ?ethical & ?realm & ?aggregate)>] -> TEMPORAL[SEM=?time] ETHICAL[SEM=?ethical] REALM[SEM=?realm] AGGREGATE[SEM=?aggregate]
TEMPORAL[SEM=<all x y.((Time(x) & Time(y)) -> TemporalOption(x,y))>] -> TIMES[CASE=gen,NUM=pl,CNT=3] THREE[CNT=3]
ETHICAL[SEM=<all x.(EthicalClass(x) -> EthicalMatch(x,x))>] -> ETHICALS[CASE=gen,NUM=pl] CORRESPONDING[MATCH=respectively]
REALM[SEM=<all x.(Realm(x) -> RealmMatch(x,x))>] -> SAME[MATCH=same_realm] INCLUDED[CASE=gen,NUM=pl]
AGGREGATE[SEM=<all x.(AcquisitionClass(x) -> AggregateOption(x))>] -> UNINCLUDED[CASE=gen,NUM=pl,REF=uncontaminated] FOUR[CNT=4]
TIMES[CASE=gen,NUM=pl,CNT=3] -> 'traiyadhvikānām'
THREE[CNT=3] -> 'trividhā'
ETHICALS[CASE=gen,NUM=pl] -> 'śubhādīnām'
CORRESPONDING[MATCH=respectively] -> 'śubhādikā'
SAME[MATCH=same_realm] -> 'svadhātukā'
INCLUDED[CASE=gen,NUM=pl] -> 'tadāptānām'
UNINCLUDED[CASE=gen,NUM=pl,REF=uncontaminated] -> 'anāptānām'
FOUR[CNT=4] -> 'caturvidhā'
```

```nltk-dep
'trividhā' -> 'traiyadhvikānām'
'śubhādikā' -> 'śubhādīnām'
'svadhātukā' -> 'tadāptānām'
'caturvidhā' -> 'anāptānām'
```

The four two-token constituents have spans [0, 2), [2, 4), [4, 6),
and [6, 8). Counts are lexical constraints; the model and regression
tests separately check the actual inventories.

## 5. Translation

### Literal Translation

> For dharmas of the three times, acquisition is threefold. For wholesome
> and the rest, it has the corresponding ethical status. Of those included
> in a realm, it belongs to that same realm; of those not included, it is
> fourfold.
### Bhāṣya-informed study translation

> For past, future, and present dharmas, acquisition is threefold in time.
> For wholesome, unwholesome, and indeterminate dharmas, acquisition is
> respectively wholesome, unwholesome, and indeterminate. For dharmas
> included in a Realm, acquisition belongs to that same Realm;
> for those not included in a Realm, it is fourfold in all.
## 6. Philosophical Translation

> Acquisition is classified in relation to what is acquired, without
> merely copying its temporal position. Ethical status and Realm
> correspond respectively; uncontaminated dharmas yield a combined
> fourfold range of acquisition, not a fourth Realm.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| traiyadhvika | of the three times | dharma-time and acquisition-time are distinct indices |
| svadhātuka | of the same Realm | Realm-included dharmas have same-Realm acquisition |
| anāpta | not included in a realm | not unacquired |
| anāsrava | uncontaminated | not a Realm; not equivalent to unconditioned |
| samāsena / samasya | in summary / taken together | fourfold collectively, with subtype restrictions |
| kila | it is said | reportive opening supplied by the Bhāṣya |

## 8. Logical Determination

The temporal matrix represents the general classification, not a claim
that each individual dharma has all nine combinations. The following
verse explicitly gives exceptions. These are separate classifications,
not a free Cartesian product across time, ethics, and Realm.

```nltk-sem
temporal : all x y.((Time(x) & Time(y)) -> TemporalOption(x,y))
ethical : all x.(EthicalClass(x) -> EthicalMatch(x,x))
realm : all x.(Realm(x) -> RealmMatch(x,x))
aggregate : all x.(AcquisitionClass(x) -> AggregateOption(x))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all x y.((Time(x) & Time(y)) -> TemporalOption(x,y)) & all x.(EthicalClass(x) -> EthicalMatch(x,x)) & all x.(Realm(x) -> RealmMatch(x,x)) & all x.(AcquisitionClass(x) -> AggregateOption(x)))

# THEORY prose_combined_range
# EXPECT prose_combined_range T
all y.(AggregateOption(y) <-> exists x.(UnincludedKind(x) & AllowedAcquisition(x,y)))

# THEORY rejected_temporal_identity
# EXPECT rejected_temporal_identity F
all x y.(TemporalOption(x,y) -> (x = y))

# THEORY rejected_four_for_each_unincluded_kind
# EXPECT rejected_four_for_each_unincluded_kind F
all x y.((UnincludedKind(x) & AcquisitionClass(y)) -> AllowedAcquisition(x,y))

# THEORY rejected_uncontaminated_is_fourth_realm
# EXPECT rejected_uncontaminated_is_fourth_realm F
Realm(uncontaminated) & AcquisitionClass(uncontaminated)

# THEORY rejected_all_unincluded_are_unconditioned
# EXPECT rejected_all_unincluded_are_unconditioned F
all x.(UnincludedKind(x) -> Unconditioned(x))
```

```nltk-valuation
uncontaminated => uncontaminated_class
Time => {past,future,present}
TemporalOption => {(past,past),(past,future),(past,present),(future,past),(future,future),(future,present),(present,past),(present,future),(present,present)}
EthicalClass => {wholesome,unwholesome,indeterminate}
EthicalMatch => {(wholesome,wholesome),(unwholesome,unwholesome),(indeterminate,indeterminate)}
Realm => {desire_realm,form_realm,formless_realm}
RealmMatch => {(desire_realm,desire_realm),(form_realm,form_realm),(formless_realm,formless_realm)}
AcquisitionClass => {desire_realm,form_realm,formless_realm,uncontaminated_class}
AggregateOption => {desire_realm,form_realm,formless_realm,uncontaminated_class}
UnincludedKind => {nondiscriminative_cessation,discriminative_cessation,path_truth}
Unconditioned => {nondiscriminative_cessation,discriminative_cessation,space}
AllowedAcquisition => {(nondiscriminative_cessation,desire_realm),(nondiscriminative_cessation,form_realm),(nondiscriminative_cessation,formless_realm),(discriminative_cessation,form_realm),(discriminative_cessation,formless_realm),(discriminative_cessation,uncontaminated_class),(path_truth,uncontaminated_class)}
```

The two cessations have respectively three options each, but different
sets; path-truth has only uncontaminated acquisition. Their union has
four members. Space is not an acquisition-bearing unincluded kind:
the exclusion from 2.36 remains in force. This finite model tests
classification and accounting, not occurrence or causal sufficiency.

## 9. Interpretive Note

**Translation note.** The Bhāṣya's reportive *kila* continues the preceding
dispute rather than declaring its ontology settled. Its *samāsena*
and *samasya* make the fourfold count collective. The trainee-status
transition at 64.25 leads into 2.38; it is not a claim in this kārikā.

In the Organon reading, Cognition joins and governs Perception and
Conception and guides the Dharma Base, without becoming consciousness
or Mind. A bare possession flag loses the relation's determinations:
the acquired dharma and its acquisition can have different times,
while the ethical and Realm rules require correspondence. Preserve
those different relations rather than imposing one identity rule.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_37 a vak:Karika ; vak:hasTopic vak:AcquisitionMatrix .
vak:DharmaTime vak:distinctIndexFrom vak:AcquisitionTime .
vak:UnincludedAcquisition vak:combinedRangeCount 4 ;
    vak:requiresSubtypeRestriction true .
```
