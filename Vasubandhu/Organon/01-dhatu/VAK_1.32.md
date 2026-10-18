# VAK_1.32 — With Both, With One, With Neither

## 1. Sanskrit (Devanāgarī)

```sanskrit
सवितर्कविचारा हि पञ्च विज्ञानधातवः ।
अन्त्यास्त्रयस्त्रिप्रकाराः शेषा उभयवर्जिताः ॥ १.३२ ॥
```

## 2. Sanskrit (IAST)

```text
savitarkavicārā hi pañca vijñānadhātavaḥ /
antyās trayas triprakārāḥ śeṣā ubhayavarjitāḥ // 1.32 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| sa-vitarka-vicārāḥ | bahuvrīhi; nominative masculine plural | with vitarka and with vicāra |
| hi | particle | restrictive (*niyamārtha*): always, not sometimes |
| pañca | numeral | five |
| vijñāna-dhātavaḥ | tatpuruṣa; nominative masculine plural | the Cognition Principles |
| antyāḥ | antya; nominative masculine plural | the last; Mind, Dharma, Mind-Cognition |
| trayaḥ | tri; nominative masculine plural | three |
| tri-prakārāḥ | bahuvrīhi; nominative masculine plural | of three kinds |
| śeṣāḥ | śeṣa; nominative masculine plural | the remaining ten |
| ubhaya-varjitāḥ | tatpuruṣa; varjita, past participle; nominative masculine plural | without both |

Vitarka and vicāra stay Sanskrit. The last three are the Mind Principle, the Dharma Principle, and the Mind-Cognition Principle. The Dharma Principle is not the Dharma Essence.

**Grammar tokens.** Verse-order IAST with sandhi opened (`antyās trayas`
→ *antyāḥ trayaḥ*, `śeṣā ubhaya-` → *śeṣāḥ ubhaya-*) and compound
boundaries marked.

```text
# tokens: sa-vitarka-vicārāḥ hi pañca vijñāna-dhātavaḥ antyāḥ trayaḥ tri-prakārāḥ śeṣāḥ ubhaya-varjitāḥ
```

## 4. Grammar

Three clauses answer the Bhāṣya's three questions. Each predicate is a
masculine plural bahuvrīhi or participle agreeing with *dhātavaḥ*, stated
or understood. *Hi* is restrictive: it licenses the exclusive reading of
the first clause, so the five have the kind "with both" and no other. *Tri-
prakārāḥ* gives the last three at least three kinds. *Ubhaya-varjitāḥ*
gives the ten "without both"; the Bhāṣya adds *nityam*, always.

```nltk-fcfg
% start S
# tokens: sa-vitarka-vicārāḥ hi pañca vijñāna-dhātavaḥ antyāḥ trayaḥ tri-prakārāḥ śeṣāḥ ubhaya-varjitāḥ
S[SEM=<(?five & ?last & ?rest)>] -> FIVECL[SEM=?five] LASTCL[SEM=?last] RESTCL[SEM=?rest]
FIVECL[SEM=<all x.(?subj(x) -> all k.(Kind(x,k) <-> ?pred(k)))>] -> PRED[CASE=nom,NUM=?n,GEN=?g,SEM=?pred] HI[RESTR=yes] FIVE SUBJ[CASE=nom,NUM=?n,GEN=?g,SEM=?subj]
LASTCL[SEM=<all x.(?subj(x) -> ?tri(x))>] -> LAST[CASE=nom,NUM=?n,GEN=?g,SEM=?subj] THREE[CASE=nom,NUM=?n,GEN=?g] TRI[CASE=nom,NUM=?n,GEN=?g,SEM=?tri]
RESTCL[SEM=<all x.(?subj(x) -> all k.(Kind(x,k) <-> ?pred(k)))>] -> REST[CASE=nom,NUM=?n,GEN=?g,SEM=?subj] PRED[CASE=nom,NUM=?n,GEN=?g,SEM=?pred]
PRED[CASE=nom,NUM=pl,GEN=m,SEM=<\k.(k = with_both)>] -> 'sa-vitarka-vicārāḥ'
HI[RESTR=yes] -> 'hi'
FIVE -> 'pañca'
SUBJ[CASE=nom,NUM=pl,GEN=m,SEM=<\x.FiveCognition(x)>] -> 'vijñāna-dhātavaḥ'
LAST[CASE=nom,NUM=pl,GEN=m,SEM=<\x.LastThree(x)>] -> 'antyāḥ'
THREE[CASE=nom,NUM=pl,GEN=m] -> 'trayaḥ'
TRI[CASE=nom,NUM=pl,GEN=m,SEM=<\x.(Kind(x,with_both) & Kind(x,vicara_only) & Kind(x,without_both))>] -> 'tri-prakārāḥ'
REST[CASE=nom,NUM=pl,GEN=m,SEM=<\x.(AmongEighteen(x) & -FiveCognition(x) & -LastThree(x))>] -> 'śeṣāḥ'
PRED[CASE=nom,NUM=pl,GEN=m,SEM=<\k.(k = without_both)>] -> 'ubhaya-varjitāḥ'
```

```nltk-dep
'sa-vitarka-vicārāḥ' -> 'hi' | 'vijñāna-dhātavaḥ'
'vijñāna-dhātavaḥ' -> 'pañca'
'tri-prakārāḥ' -> 'trayaḥ'
'trayaḥ' -> 'antyāḥ'
'ubhaya-varjitāḥ' -> 'śeṣāḥ'
```

**Close construe.** For the five Cognition Principles are with vitarka and
vicāra. The last three are of three kinds. The rest are without both.

A kind is a way a Principle occurs with respect to the pair: with both,
vicāra alone, vitarka alone, or without both. *Hi* makes the first clause
exclusive. *Tri-prakārāḥ* is not exclusive: the Bhāṣya finds a fourth kind,
vicāra itself in the Desire Realm and the first concentration, inside the
Dharma Principle, and says it does not fall within the three. That clarifies
the verse; it does not contradict it.

The three kinds are not three Principles. They are three ways the last three occur.

## 5. Translation

### Literal Translation

> The five Cognition Principles are with vitarka and with vicāra. The last
> three are of three kinds. The rest are without both.

### Bhāṣya-informed study translation

> The five Cognition Principles are accompanied by both vitarka and vicāra.
> The last three—Mind Principle, Dharma Principle, and Mind-Cognition
> Principle—are of three kinds; the remaining ten are without both.

## 6. Philosophical Translation

The five Cognitions do not occur without the pair. The last three take the pair, or one of the pair, or neither, by the level. The ten whose nature is Form take neither, because association is not their way.

Vitarka and vicāra are not counted twice. Each is without a second of itself, and each is with the other. That is why a level with both has four kinds, not three.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| vitarka | vitarka | not translated on this page |
| vicāra | vicāra | not translated on this page |
| pañca vijñāna-dhātavaḥ | five Cognition Principles | always with both |
| antyāḥ trayaḥ | the last three | Mind, Dharma, Mind-Cognition |
| dharma-dhātu | Dharma Principle | not the Dharma Essence |
| tri-prakāra | of three kinds | by level, not by name |
| dhyānāntara | intermediate concentration | without vitarka, with vicāra |
| bhavāgra | summit of existence | without both |
| ubhaya-varjita | without both | the ten whose nature is Form |
| asaṃprayukta | unassociated | the rest of the Dharma Principle |

## 8. Logical Determination

**Kārikā, derived.** The five Cognition Principles have exactly the kind
"with both"; the last three have at least the kinds "with both", "vicāra
alone", and "without both"; the remaining ten have exactly the kind
"without both".

```nltk-sem
# derived by the section 4 parse
(all x.(FiveCognition(x) -> all k.(Kind(x,k) <-> (k = with_both))) & all x.(LastThree(x) -> (Kind(x,with_both) & Kind(x,vicara_only) & Kind(x,without_both))) & all x.((AmongEighteen(x) & -FiveCognition(x) & -LastThree(x)) -> all k.(Kind(x,k) <-> (k = without_both))))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all x.(FiveCognition(x) -> all k.(Kind(x,k) <-> (k = with_both))) & all x.(LastThree(x) -> (Kind(x,with_both) & Kind(x,vicara_only) & Kind(x,without_both))) & all x.((AmongEighteen(x) & -FiveCognition(x) & -LastThree(x)) -> all k.(Kind(x,k) <-> (k = without_both))))
# THEORY prose
# EXPECT prose T
all i.(AssocNonPair(i) -> (KindAt(i,kama,with_both) & KindAt(i,first_dhyana,with_both) & KindAt(i,intermediate,vicara_only) & KindAt(i,second_onward,without_both)))
all i.(Unassociated(i) -> all l.(Level(l) -> KindAt(i,l,without_both)))
exists x.(x = vicara & KindAt(x,intermediate,without_both))
all l.(BothLevel(l) -> (KindAt(vitarka,l,vicara_only) & KindAt(vicara,l,vitarka_only)))
-(exists l.KindAt(vitarka,l,with_both)) & -(exists l.KindAt(vicara,l,with_both))
PortionOf(vitarka,dharma_principle) & PortionOf(vicara,dharma_principle)
all x.(LastThree(x) -> all k.(Kind(x,k) <-> exists i.exists l.(PortionOf(i,x) & KindAt(i,l,k))))
all l.(BothLevel(l) -> (exists i.KindAt(i,l,with_both) & exists i.KindAt(i,l,vicara_only) & exists i.KindAt(i,l,vitarka_only) & exists i.KindAt(i,l,without_both)))
all x.(FormNatured(x) -> NotAssociated(x))
all x.(NotAssociated(x) -> all k.(Kind(x,k) -> (k = without_both)))
# THEORY rejected_five_sometimes_without
# EXPECT rejected_five_sometimes_without F
exists x.(FiveCognition(x) & Kind(x,without_both))
# THEORY rejected_dharma_exactly_three_kinds
# EXPECT rejected_dharma_exactly_three_kinds F
-Kind(dharma_principle,vitarka_only)
# THEORY rejected_one_kind_per_principle
# EXPECT rejected_one_kind_per_principle F
exists x.(LastThree(x) & exists k.all j.(Kind(x,j) <-> (j = k)))
# THEORY rejected_vitarka_with_second_vitarka
# EXPECT rejected_vitarka_with_second_vitarka F
exists l.KindAt(vitarka,l,with_both)
# THEORY rejected_intermediate_has_vitarka
# EXPECT rejected_intermediate_has_vitarka F
exists i.KindAt(i,intermediate,with_both)
# THEORY rejected_form_natured_with_pair
# EXPECT rejected_form_natured_with_pair F
exists x.(FormNatured(x) & (Kind(x,with_both) | Kind(x,vicara_only) | Kind(x,vitarka_only)))
```

```nltk-valuation
with_both => both_k
vicara_only => vicara_only_k
vitarka_only => vitarka_only_k
without_both => neither_k
kama => kama_l
first_dhyana => dhyana1_l
intermediate => antara_l
second_onward => higher_l
vitarka => vitarka_i
vicara => vicara_i
dharma_principle => dharma_d
AmongEighteen => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,mano_d,dharma_d,manovijnana_d}
FiveCognition => {caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d}
LastThree => {mano_d,dharma_d,manovijnana_d}
FormNatured => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d}
NotAssociated => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d}
Kind => {(caksurvijnana_d,both_k),(srotravijnana_d,both_k),(ghranavijnana_d,both_k),(jihvavijnana_d,both_k),(kayavijnana_d,both_k),(mano_d,both_k),(mano_d,vicara_only_k),(mano_d,neither_k),(manovijnana_d,both_k),(manovijnana_d,vicara_only_k),(manovijnana_d,neither_k),(dharma_d,both_k),(dharma_d,vicara_only_k),(dharma_d,neither_k),(dharma_d,vitarka_only_k),(caksur_d,neither_k),(srotra_d,neither_k),(ghrana_d,neither_k),(jihva_d,neither_k),(kaya_d,neither_k),(rupa_d,neither_k),(sabda_d,neither_k),(gandha_d,neither_k),(rasa_d,neither_k),(sprastavya_d,neither_k)}
Level => {kama_l,dhyana1_l,antara_l,higher_l}
BothLevel => {kama_l,dhyana1_l}
KindAt => {(mano_i,kama_l,both_k),(mano_i,dhyana1_l,both_k),(mano_i,antara_l,vicara_only_k),(mano_i,higher_l,neither_k),(manovijnana_i,kama_l,both_k),(manovijnana_i,dhyana1_l,both_k),(manovijnana_i,antara_l,vicara_only_k),(manovijnana_i,higher_l,neither_k),(dharma_assoc_i,kama_l,both_k),(dharma_assoc_i,dhyana1_l,both_k),(dharma_assoc_i,antara_l,vicara_only_k),(dharma_assoc_i,higher_l,neither_k),(dharma_unassoc_i,kama_l,neither_k),(dharma_unassoc_i,dhyana1_l,neither_k),(dharma_unassoc_i,antara_l,neither_k),(dharma_unassoc_i,higher_l,neither_k),(vitarka_i,kama_l,vicara_only_k),(vitarka_i,dhyana1_l,vicara_only_k),(vicara_i,kama_l,vitarka_only_k),(vicara_i,dhyana1_l,vitarka_only_k),(vicara_i,antara_l,neither_k)}
PortionOf => {(mano_i,mano_d),(manovijnana_i,manovijnana_d),(dharma_assoc_i,dharma_d),(dharma_unassoc_i,dharma_d),(vitarka_i,dharma_d),(vicara_i,dharma_d)}
AssocNonPair => {mano_i,manovijnana_i,dharma_assoc_i}
Unassociated => {dharma_unassoc_i}
```

**Model checks.** Five, three, and ten partition the eighteen. The five
have only "with both"; the ten only "without both". The Mind and
Mind-Cognition Principles have exactly three kinds; the Dharma Principle
has four, because vicāra itself is in it. On the Desire Realm and the first
concentration all four kinds occur; the intermediate concentration has
vicāra alone for the associated portion and none "with both"; from the
second concentration through the summit, without both. Neither vitarka nor
vicāra is ever "with both", since neither has a second of itself.

**Bhāṣya determination.** *Hi* has the force of restriction. The last three
vary by level: Desire Realm and first concentration with both,
intermediate concentration vicāra alone, second concentration through the
summit without both. The whole unassociated Dharma Principle, and vicāra in
the intermediate concentration, are without both. Vitarka is vicāra-alone
always; vicāra on a level with both is vitarka-alone. Hence the quoted rule:
on a level with both, Dharmas are of four kinds. The ten Form-natured
Principles are always without both, because they are not associated.

**Organon interpretation.** The cut now runs on two axes: Principle and
level. Kind is a relation between a Principle (through its portions) and a
level, not a fixed label on the Principle. The verse states three kinds
for the last three; the prose finds the fourth by turning the pair on
itself. The Dharma Principle carries vitarka and vicāra as its own
portions; the Dharma Essence is not substituted. 1.33 is not opened. The
earlier schematic follows.

```text
five Cognition Principles
    always with vitarka and vicāra

last three
    Desire Realm and first concentration: with both
    intermediate concentration: vicāra alone
    second concentration through the summit: without both

exceptions inside the three
    vitarka: vicāra alone
    vicāra in desire and first: vitarka alone
    unassociated Dharma Principle: without both
    vicāra in the intermediate: without both

four kinds on a level with both
    associated, other than the pair: with both
    vitarka: with vicāra alone
    unassociated: without both
    vicāra: with vitarka alone

remaining ten
    always without both

1.33 not opened
```

## 9. Interpretive Note

**Translation note.** The five Cognition Principles are always associated with
both terms. The last three vary by level: desire and the first concentration
have both, intermediate concentration has vicāra alone, and the second
concentration through the summit has neither. The commentary separately
classifies vitarka as with vicāra alone, vicāra in desire and the first
concentration as with vitarka alone, and unassociated Dharma-Principle (and
vicāra in the intermediate concentration) as without both. Thus the cited
fourfold distinction on a level with both clarifies, rather than alters, the
verse's threefold statement; the remaining ten are Form-natured and
unassociated.

The hinge is hi. The five are not sometimes with the pair. The last three are the ones that vary, and the variation is the level. The four kinds are required because vitarka and vicāra cannot associate with a second of themselves.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_32 a vak:Karika ;
    vak:hasTopic vak:VitarkaVicaraCut ;
    vak:belongsTo vak:Dhatunirdesa .

vak:FiveCognitionPrinciples vak:alwaysWith vak:Vitarka, vak:Vicara .
vak:LastThree vak:ofThreeKinds true .
vak:TenOfFormNature vak:withoutBoth true .
```
