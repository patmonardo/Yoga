# VAK_1.31 — Three in the Formless

## 1. Sanskrit (Devanāgarī)

```sanskrit
आरूप्याप्ता मनोधर्ममनोविज्ञानधातवः ।
सास्रवानास्रवा एते त्रयः शेषास्तु सास्रवाः ॥ १.३१ ॥
```

## 2. Sanskrit (IAST)

```text
ārūpyāptā manodharmamanovijñānadhātavaḥ /
sāsravānāsravā ete trayaḥ śeṣās tu sāsravāḥ // 1.31 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| ārūpya-āptāḥ | tatpuruṣa; āpta, past participle of *āp*; nominative masculine plural | connected with the Formless Realm |
| mano-dharma-mano-vijñāna-dhātavaḥ | dvandva inside tatpuruṣa; nominative masculine plural | the Mind, Dharma, and Mind-Cognition Principles |
| sa-āsrava-an-āsravāḥ | dvandva of two bahuvrīhis; nominative masculine plural | Impure and Pure |
| ete | etad; nominative masculine plural | these; the three just named |
| trayaḥ | tri; nominative masculine plural | three |
| śeṣāḥ | śeṣa; nominative masculine plural | the remaining fifteen |
| tu | particle | but; contrasts the fifteen with the three |
| sa-āsravāḥ | sa-āsrava, bahuvrīhi; nominative masculine plural | Impure |

The compound names three Principles, not three Essences. The Dharma Principle is not the Dharma Essence.

**Grammar tokens.** Verse-order IAST with sandhi opened (`ārūpyāptā` →
*ārūpya-āptāḥ*, `sāsravānāsravā` → *sa-āsrava-an-āsravāḥ*, `śeṣās tu` →
*śeṣāḥ tu*) and compound boundaries marked. Each compound stays one token;
its members are stated in the SEM.

```text
# tokens: ārūpya-āptāḥ mano-dharma-mano-vijñāna-dhātavaḥ sa-āsrava-an-āsravāḥ ete trayaḥ śeṣāḥ tu sa-āsravāḥ
```

## 4. Grammar

Three clauses. The first completes the realm count of 1.30: the participle
agrees with the three-member compound. The second opens a new cut: *ete
trayaḥ* resumes the three, and the dvandva predicates both Impure and Pure.
The third contrasts the rest with *tu*: Impure only. All adjectives are
masculine plural, agreeing with *dhātavaḥ*.

```nltk-fcfg
% start S
# tokens: ārūpya-āptāḥ mano-dharma-mano-vijñāna-dhātavaḥ sa-āsrava-an-āsravāḥ ete trayaḥ śeṣāḥ tu sa-āsravāḥ
S[SEM=<(?formless & ?both & ?rest)>] -> FORMLESS[SEM=?formless] BOTH[SEM=?both] REST[SEM=?rest]
FORMLESS[SEM=<all x.(AmongEighteen(x) -> (?conn(x) <-> ?three(x)))>] -> CONN[CASE=nom,NUM=?n,GEN=?g,SEM=?conn] THREE[CASE=nom,NUM=?n,GEN=?g,SEM=?three]
BOTH[SEM=<all x.(?these(x) -> ?pair(x))>] -> PAIR[CASE=nom,NUM=?n,GEN=?g,SEM=?pair] THESE[CASE=nom,NUM=?n,GEN=?g,SEM=?these] TRI[CASE=nom,NUM=?n,GEN=?g]
REST[SEM=<all x.(?rest(x) -> (?imp(x) & -HasPureInstance(x)))>] -> REMAIN[CASE=nom,NUM=?n,GEN=?g,SEM=?rest] TU IMP[CASE=nom,NUM=?n,GEN=?g,SEM=?imp]
CONN[CASE=nom,NUM=pl,GEN=m,SEM=<\x.ConnectedWith(x,formless_realm)>] -> 'ārūpya-āptāḥ'
THREE[CASE=nom,NUM=pl,GEN=m,SEM=<\x.((x = mind) | (x = dharma_principle) | (x = mind_cognition))>] -> 'mano-dharma-mano-vijñāna-dhātavaḥ'
PAIR[CASE=nom,NUM=pl,GEN=m,SEM=<\x.(HasImpureInstance(x) & HasPureInstance(x))>] -> 'sa-āsrava-an-āsravāḥ'
THESE[CASE=nom,NUM=pl,GEN=m,SEM=<\x.(AmongEighteen(x) & ConnectedWith(x,formless_realm))>] -> 'ete'
TRI[CASE=nom,NUM=pl,GEN=m] -> 'trayaḥ'
REMAIN[CASE=nom,NUM=pl,GEN=m,SEM=<\x.(AmongEighteen(x) & -ConnectedWith(x,formless_realm))>] -> 'śeṣāḥ'
TU -> 'tu'
IMP[CASE=nom,NUM=pl,GEN=m,SEM=<\x.HasImpureInstance(x)>] -> 'sa-āsravāḥ'
```

```nltk-dep
'ārūpya-āptāḥ' -> 'mano-dharma-mano-vijñāna-dhātavaḥ'
'sa-āsrava-an-āsravāḥ' -> 'ete'
'ete' -> 'trayaḥ'
'sa-āsravāḥ' -> 'śeṣāḥ' | 'tu'
```

**Close construe.** Connected with the Formless are the Mind, Dharma, and
Mind-Cognition Principles. These three are Impure and Pure. But the rest
are Impure.

Impure and Pure are predicated of a Principle through its instances: a
Principle has Pure instances, Impure instances, or both. *Tu* sets the
fifteen against the three, so their Impurity is exclusive; the Bhāṣya says
so with *ekānta-sāsravāḥ*.

The second line is a new cut. It is not restricted to births in the Formless.

## 5. Translation

### Literal Translation

> Connected with the Formless are the Mind Principle, the Dharma Principle,
> and the Mind-Cognition Principle. These three are Impure and Pure. The
> rest are Impure.

### Bhāṣya-informed study translation

> Connected with the Formless are the Mind Principle, Dharma Principle, and
> Mind-Cognition Principle. These three are Impure and Pure; the remaining
> fifteen are Impure.

## 6. Philosophical Translation

The Formless drops the ten whose nature is Form, and the five Cognitions that take them. What remains is Mind, Dharma, and Mind-Cognition. That is a birth-cut, not a denial that the Concept has Form.

The Pure and the Impure are a second cut. These three admit both. The fifteen do not. Pure here is Path or unconditioned. It is not the Formless.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| ārūpya | Formless Realm | a Principle of Principles; not one of the eighteen |
| āpta | connected | not separated from |
| mano-dhātu | Mind Principle | the seventh of the Cognition Principle |
| dharma-dhātu | Dharma Principle | not the Dharma Essence |
| mano-vijñāna-dhātu | Mind-Cognition Principle | one of the six |
| vijñāna | Cognition | not Principle |
| sāsrava | Impure | not outflow-bearing |
| anāsrava | Pure | Path or unconditioned, in this cut |
| śeṣāḥ | the remaining fifteen | exclusively Impure |

## 8. Logical Determination

**Kārikā, derived.** Among the eighteen, connection with the Formless holds
exactly for the three; the three have both Impure and Pure instances; the
rest have Impure instances and no Pure one.

```nltk-sem
# derived by the section 4 parse
(all x.(AmongEighteen(x) -> (ConnectedWith(x,formless_realm) <-> ((x = mind) | (x = dharma_principle) | (x = mind_cognition)))) & all x.((AmongEighteen(x) & ConnectedWith(x,formless_realm)) -> (HasImpureInstance(x) & HasPureInstance(x))) & all x.((AmongEighteen(x) & -ConnectedWith(x,formless_realm)) -> (HasImpureInstance(x) & -HasPureInstance(x))))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all x.(AmongEighteen(x) -> (ConnectedWith(x,formless_realm) <-> ((x = mind) | (x = dharma_principle) | (x = mind_cognition)))) & all x.((AmongEighteen(x) & ConnectedWith(x,formless_realm)) -> (HasImpureInstance(x) & HasPureInstance(x))) & all x.((AmongEighteen(x) & -ConnectedWith(x,formless_realm)) -> (HasImpureInstance(x) & -HasPureInstance(x))))
# THEORY prose
# EXPECT prose T
all x.(AmongEighteen(x) -> (-ConnectedWith(x,formless_realm) <-> (FormNatured(x) | exists y.(FormNatured(y) & SupportAndCondition(y,x)))))
all z.(FreeOfFormPassion(z) <-> BornIn(z,formless_realm))
all i.(Pure(i) <-> (InPathTruth(i) | Unconditioned(i)))
all x.(HasPureInstance(x) <-> exists i.(InstanceOf(i,x) & Pure(i)))
all x.(HasImpureInstance(x) <-> exists i.(InstanceOf(i,x) & -Pure(i)))
all i.(Unconditioned(i) -> InstanceOf(i,dharma_principle))
all x.(Principle(x) <-> (AmongEighteen(x) | RealmLevel(x)))
EssenceLevel(dharma_essence) & RealmLevel(formless_realm)
all x.(RealmLevel(x) -> -AmongEighteen(x))
all r.(RealmLevel(r) -> exists x.(AmongEighteen(x) & ConnectedWith(x,r)))
all x.(EssenceLevel(x) -> -Principle(x))
# THEORY rejected_form_natured_in_formless
# EXPECT rejected_form_natured_in_formless F
exists x.(FormNatured(x) & ConnectedWith(x,formless_realm))
# THEORY rejected_five_cognitions_in_formless
# EXPECT rejected_five_cognitions_in_formless F
exists x.(exists y.(FormNatured(y) & SupportAndCondition(y,x)) & ConnectedWith(x,formless_realm))
# THEORY rejected_pure_means_formless
# EXPECT rejected_pure_means_formless F
all i.(Pure(i) <-> exists x.(InstanceOf(i,x) & ConnectedWith(x,formless_realm)))
# THEORY rejected_fifteen_have_pure
# EXPECT rejected_fifteen_have_pure F
exists x.(AmongEighteen(x) & -ConnectedWith(x,formless_realm) & HasPureInstance(x))
# THEORY rejected_three_only_pure
# EXPECT rejected_three_only_pure F
exists x.(ConnectedWith(x,formless_realm) & -HasImpureInstance(x))
# THEORY rejected_dharma_principle_is_essence
# EXPECT rejected_dharma_principle_is_essence F
exists x.(x = dharma_principle & EssenceLevel(x))
# THEORY rejected_formless_among_eighteen
# EXPECT rejected_formless_among_eighteen F
exists x.(x = formless_realm & AmongEighteen(x))
# THEORY rejected_formless_not_principle
# EXPECT rejected_formless_not_principle F
exists x.(x = formless_realm & -Principle(x))
```

```nltk-valuation
mind => mano_d
dharma_principle => dharma_d
mind_cognition => manovijnana_d
dharma_essence => dharma_ayatana
formless_realm => arupya_dhatu
AmongEighteen => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,mano_d,dharma_d,manovijnana_d}
Principle => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,mano_d,dharma_d,manovijnana_d,arupya_dhatu}
EssenceLevel => {dharma_ayatana}
RealmLevel => {arupya_dhatu}
ConnectedWith => {(mano_d,arupya_dhatu),(dharma_d,arupya_dhatu),(manovijnana_d,arupya_dhatu)}
FormNatured => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d}
SupportAndCondition => {(rupa_d,caksurvijnana_d),(sabda_d,srotravijnana_d),(gandha_d,ghranavijnana_d),(rasa_d,jihvavijnana_d),(sprastavya_d,kayavijnana_d),(caksur_d,caksurvijnana_d),(srotra_d,srotravijnana_d),(ghrana_d,ghranavijnana_d),(jihva_d,jihvavijnana_d),(kaya_d,kayavijnana_d)}
InstanceOf => {(caksur_d_imp,caksur_d),(srotra_d_imp,srotra_d),(ghrana_d_imp,ghrana_d),(jihva_d_imp,jihva_d),(kaya_d_imp,kaya_d),(rupa_d_imp,rupa_d),(sabda_d_imp,sabda_d),(gandha_d_imp,gandha_d),(rasa_d_imp,rasa_d),(sprastavya_d_imp,sprastavya_d),(caksurvijnana_d_imp,caksurvijnana_d),(srotravijnana_d_imp,srotravijnana_d),(ghranavijnana_d_imp,ghranavijnana_d),(jihvavijnana_d_imp,jihvavijnana_d),(kayavijnana_d_imp,kayavijnana_d),(mano_d_imp,mano_d),(dharma_d_imp,dharma_d),(manovijnana_d_imp,manovijnana_d),(mano_d_path,mano_d),(dharma_d_path,dharma_d),(manovijnana_d_path,manovijnana_d),(dharma_d_unc,dharma_d)}
Pure => {mano_d_path,dharma_d_path,manovijnana_d_path,dharma_d_unc}
InPathTruth => {mano_d_path,dharma_d_path,manovijnana_d_path}
Unconditioned => {dharma_d_unc}
HasPureInstance => {mano_d,dharma_d,manovijnana_d}
HasImpureInstance => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,mano_d,dharma_d,manovijnana_d}
FreeOfFormPassion => {arupya_born}
BornIn => {(arupya_born,arupya_dhatu)}
```

**Model checks.** Eighteen Principles; three connected with the Formless,
fifteen not. The fifteen are exactly the ten Form-natured Principles and
the five Cognitions that take them as support and Condition. Each Principle
has an Impure instance; only the three have Pure instances, by Path for
all three and by the unconditioned for the Dharma Principle alone. Making a
Form-natured Principle Formless-connected, or giving one of the fifteen a
Pure instance, falsifies the theory. The Formless Realm is a Principle of
Principles constituted by the three; the Dharma Essence is not a
Principle, and the Dharma Principle is not the Dharma Essence.

**Bhāṣya determination.** Those free of passion for Form are born there,
so the ten Form-natured Principles do not occur there, nor the five
Cognition Principles that have those as support and Condition. Pure is
what is included in the Path-truth or the unconditioned; the rest is
Impure. The fifteen are *ekānta-sāsrava*, exclusively Impure. There is no
rival school in the unit.

**Organon interpretation.** The realm count closes: eighteen, fourteen,
three. A second cut, Impure and Pure, is not a realm cut: Pure is not the
Formless, and Pure instances of the three occur wherever the Path occurs.
The Dharma Principle carries the unconditioned at Principle level; the
Dharma Essence is the same Dharma at Essence level and is not substituted
for it. 1.32 is not opened. The earlier schematic follows.

```text
Formless
    not the ten whose nature is Form
    not the five Cognition Principles that take them
    three: Mind Principle, Dharma Principle, Mind-Cognition Principle

these three
    Impure and Pure

the fifteen
    exclusively Impure

Pure
    included in the Path
    or included in the unconditioned

1.32 not opened
```

## 9. Interpretive Note

**Translation note.** The three are Mind, Dharma, and Mind-Cognition
Principles; they are connected with the Formless Realm because the ten
Form-natured Principles and the five Cognition Principles taking them as
support and Condition do not occur there. The Pure instances belong to the
Path-truth or the unconditioned; the other instances are Impure. The remaining
fifteen are exclusively Impure.

The hinge is the second line. The three names carry forward. The Pure and the Impure do not mean three Formless things that are both at once. They mean these three Principles have instances of both.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_31 a vak:Karika ;
    vak:hasTopic vak:ThreeInTheFormless ;
    vak:belongsTo vak:Dhatunirdesa .

vak:FormlessRealm vak:includes
    vak:MindPrinciple, vak:DharmaPrinciple, vak:MindCognitionPrinciple .
vak:TheseThree vak:admits vak:Impure, vak:Pure .
vak:RemainingFifteen vak:exclusively vak:Impure .
```
