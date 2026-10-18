# VAK_1.30 — Threefold, and Fourteen

## 1. Sanskrit (Devanāgarī)

```sanskrit
त्रिधान्ये कामधात्वाप्ताः सर्वे रूपे चतुर्दश ।
विना गन्धरसघ्राणजिह्वाविज्ञानधातुभिः ॥ १.३० ॥
```

## 2. Sanskrit (IAST)

```text
tridhānye kāmadhātvāptāḥ sarve rūpe caturdaśa /
vinā gandharasaghrāṇajihvāvijñānadhātubhiḥ // 1.30 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| tridhā | indeclinable | in three ways: wholesome, unwholesome, indeterminate |
| anye | anya; nominative masculine plural | the others; the ten remaining after the eight of 1.29 |
| kāma-dhātu-āptāḥ | tatpuruṣa; āpta, past participle of *āp*; nominative masculine plural | connected with the Desire Realm |
| sarve | sarva; nominative masculine plural | all eighteen |
| rūpe | rūpa; locative singular, for *rūpa-dhātau* | in the Form Realm |
| caturdaśa | numeral | fourteen |
| vinā | indeclinable, governing the instrumental | excluding |
| gandha-rasa-ghrāṇa-jihvā-vijñāna-dhātubhiḥ | dvandva inside tatpuruṣa; instrumental plural | the Odor, Taste, nose-Cognition, and tongue-Cognition Principles |

The closing compound excludes four Principles, not six: *vijñāna* distributes over *ghrāṇa* and *jihvā*. Nose and tongue, the Faculties, are not in the exclusion.

**Grammar tokens.** Verse-order IAST with sandhi opened (`tridhānye` →
*tridhā anye*) and compound boundaries marked. The closing compound stays
one token; its internal distribution is stated in the instrumental's SEM.

```text
# tokens: tridhā anye kāma-dhātu-āptāḥ sarve rūpe caturdaśa vinā gandha-rasa-ghrāṇa-jihvā-vijñāna-dhātubhiḥ
```

## 4. Grammar

Three clauses. *Tridhā anye* closes the ethical question of 1.29: the others
are threefold. *Kāma-dhātu-āptāḥ sarve* opens the realm question: the
participle agrees with *sarve*. *Rūpe caturdaśa* reuses *āptāḥ* by ellipsis;
*vinā* takes the instrumental of exclusion. The realm stem *dhātu* in
*kāma-dhātu* and *rūpe* (*rūpa-dhātau*) names a Realm, not one of the
eighteen Principles.

```nltk-fcfg
% start S
# tokens: tridhā anye kāma-dhātu-āptāḥ sarve rūpe caturdaśa vinā gandha-rasa-ghrāṇa-jihvā-vijñāna-dhātubhiḥ
S[SEM=<(?ethical & ?desire & ?form)>] -> ETHICAL[SEM=?ethical] DESIRE[SEM=?desire] FORMREALM[SEM=?form]
ETHICAL[SEM=<all x.(?others(x) -> ?tri(x))>] -> TRI[SEM=?tri] OTHERS[CASE=nom,NUM=pl,GEN=m,SEM=?others]
DESIRE[SEM=<all x.(?all(x) -> ?conn(x))>] -> CONN[CASE=nom,NUM=?n,GEN=?g,SEM=?conn] ALL[CASE=nom,NUM=?n,GEN=?g,SEM=?all]
FORMREALM[SEM=<all x.(AmongEighteen(x) -> (ConnectedWith(x,?realm) <-> -?excl(x)))>] -> IN[CASE=loc,SEM=?realm] FOURTEEN WITHOUT[GOV=?c] EXCL[CASE=?c,SEM=?excl]
TRI[SEM=<\x.Threefold(x)>] -> 'tridhā'
OTHERS[CASE=nom,NUM=pl,GEN=m,SEM=<\x.(AmongEighteen(x) & -OnlyIndeterminate(x))>] -> 'anye'
CONN[CASE=nom,NUM=pl,GEN=m,SEM=<\x.ConnectedWith(x,desire_realm)>] -> 'kāma-dhātu-āptāḥ'
ALL[CASE=nom,NUM=pl,GEN=m,SEM=<\x.AmongEighteen(x)>] -> 'sarve'
IN[CASE=loc,SEM=<form_realm>] -> 'rūpe'
FOURTEEN -> 'caturdaśa'
WITHOUT[GOV=ins] -> 'vinā'
EXCL[CASE=ins,SEM=<\x.((x = odor) | (x = taste) | (x = nose_cognition) | (x = tongue_cognition))>] -> 'gandha-rasa-ghrāṇa-jihvā-vijñāna-dhātubhiḥ'
```

```nltk-dep
'tridhā' -> 'anye'
'kāma-dhātu-āptāḥ' -> 'sarve'
'caturdaśa' -> 'rūpe' | 'vinā'
'vinā' -> 'gandha-rasa-ghrāṇa-jihvā-vijñāna-dhātubhiḥ'
```

**Close construe.** The others are threefold. All are connected with the
Desire Realm. In the Form Realm, fourteen, without the Odor, Taste,
nose-Cognition, and tongue-Cognition Principles.

The counts are extensional: ten others, eighteen in the Desire Realm,
fourteen in the Form Realm are checked on the finite valuation. `Threefold`
means able to be wholesome, unwholesome, or indeterminate; the grounds for
each are in the prose. The Form Realm clause is a biconditional over the
eighteen, so nose and tongue, the Faculties, stay in by the verse itself.

*Tridhā* does not mean three realms. The realm question begins at *kāmadhātvāptāḥ*.

## 5. Translation

### Literal Translation

> The others are threefold. All are connected with the Desire Realm. In the
> Form Realm, fourteen, excluding the Odor, Taste, nose-Cognition, and
> tongue-Cognition Principles.

### Bhāṣya-informed study translation

> The other ten are threefold. All eighteen are connected with the Desire
> Realm; fourteen occur in the Form Realm, excluding the Principles of Odor,
> Taste, nose-Cognition, and tongue-Cognition.

## 6. Philosophical Translation

The ethical cut finishes the ten. The realm cut begins a new question. Threefold is not three realms.

The Form Realm drops four Principles: two Conditions, and the two Cognitions that take them. It does not drop the two Faculties. Absence of the support removes the Cognition. Absence of a use does not, by itself, remove the Faculty.

Three levels stay apart. The Form Base is a Base; the Visible Form Principle and the other Form-bearing Principles are Principles; the Form Realm is a Realm. The Form Base gathers exactly the ten Form-bearing Principles without being one of them. The Form Realm shares the name *rūpa-dhātu* with the Visible Form Principle and is not it.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| anye | the others | the ten after the eight |
| tridhā | threefold | wholesome, unwholesome, indeterminate |
| kuśala | wholesome | not the Pure |
| akuśala | unwholesome | not the Impure |
| avyākṛta | indeterminate | not declared either |
| kāmadhātu | Desire Realm | a Realm, not one of the eighteen |
| rūpadhātu | Form Realm | a Realm, not the Visible Form Principle |
| āpta | connected | not separated from |
| gandha-dhātu | Odor Principle | excluded from the fourteen |
| rasa-dhātu | Taste Principle | excluded from the fourteen |
| ghrāṇa-vijñāna-dhātu | nose-Cognition Principle | one Principle, not two |
| jihvā-vijñāna-dhātu | tongue-Cognition Principle | likewise |
| vijñāna | Cognition | not Principle |
| dhātu | Principle | the eighteen, except the Realm names |

## 8. Logical Determination

**Kārikā, derived.** Three universals: the others (the eighteen minus the
eight only-indeterminate) are threefold; all eighteen are connected with
the Desire Realm; among the eighteen, connection with the Form Realm holds
exactly when a Principle is not one of the four excluded.

```nltk-sem
# derived by the section 4 parse
(all x.((AmongEighteen(x) & -OnlyIndeterminate(x)) -> Threefold(x)) & all x.(AmongEighteen(x) -> ConnectedWith(x,desire_realm)) & all x.(AmongEighteen(x) -> (ConnectedWith(x,form_realm) <-> -((x = odor) | (x = taste) | (x = nose_cognition) | (x = tongue_cognition)))))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all x.((AmongEighteen(x) & -OnlyIndeterminate(x)) -> Threefold(x)) & all x.(AmongEighteen(x) -> ConnectedWith(x,desire_realm)) & all x.(AmongEighteen(x) -> (ConnectedWith(x,form_realm) <-> -((x = odor) | (x = taste) | (x = nose_cognition) | (x = tongue_cognition)))))
# THEORY prose
# EXPECT prose T
all x.(Threefold(x) <-> (CanBeWholesome(x) & CanBeUnwholesome(x) & CanBeIndeterminate(x)))
all x.(CittaPrinciple(x) -> ThreefoldBy(x,association))
ThreefoldBy(dharma_principle,nature) & ThreefoldBy(dharma_principle,association) & ThreefoldBy(dharma_principle,arising)
ThreefoldBy(visible_form,vijnapti) & ThreefoldBy(sound,vijnapti)
all x.(AmongEighteen(x) -> (Threefold(x) <-> exists g.ThreefoldBy(x,g)))
PortionOf(pratisamkhya_nirodha,dharma_principle) & CanBeWholesome(pratisamkhya_nirodha)
all x.(AmongEighteen(x) <-> PrincipleLevel(x))
BaseLevel(form_base) & RealmLevel(desire_realm) & RealmLevel(form_realm)
all x.(-(BaseLevel(x) & PrincipleLevel(x)) & -(BaseLevel(x) & RealmLevel(x)) & -(RealmLevel(x) & PrincipleLevel(x)))
all x.(PrincipleLevel(x) -> (GatheredIn(x,form_base) <-> FormBearing(x)))
MorselFood(odor) & MorselFood(taste) & MorselFood(tangible)
SupportOf(odor,nose_cognition) & SupportOf(taste,tongue_cognition)
all x.all y.((SupportOf(y,x) & -ConnectedWith(y,form_realm)) -> -ConnectedWith(x,form_realm))
HasUse(tangible) & HasUse(nose) & HasUse(tongue)
AttributedToOthers(dhyana_account) & Explained(varnayanti_account)
# THEORY rejected_realm_is_principle
# EXPECT rejected_realm_is_principle F
exists x.(RealmLevel(x) & AmongEighteen(x))
# THEORY rejected_form_realm_is_visible_form
# EXPECT rejected_form_realm_is_visible_form F
exists x.(x = form_realm & x = visible_form)
# THEORY rejected_form_base_is_principle
# EXPECT rejected_form_base_is_principle F
exists x.(x = form_base & PrincipleLevel(x))
# THEORY rejected_eight_are_threefold
# EXPECT rejected_eight_are_threefold F
exists x.(OnlyIndeterminate(x) & Threefold(x))
# THEORY rejected_faculties_excluded
# EXPECT rejected_faculties_excluded F
exists x.(((x = nose) | (x = tongue)) & -ConnectedWith(x,form_realm))
# THEORY rejected_tangible_excluded_as_food
# EXPECT rejected_tangible_excluded_as_food F
exists x.(x = tangible & -ConnectedWith(x,form_realm))
# THEORY rejected_cognition_without_support
# EXPECT rejected_cognition_without_support F
exists x.exists y.(SupportOf(y,x) & -ConnectedWith(y,form_realm) & ConnectedWith(x,form_realm))
```

```nltk-valuation
desire_realm => kama_dhatu
form_realm => rupa_dhatu_realm
form_base => rupa_skandha
visible_form => rupa_d
sound => sabda_d
odor => gandha_d
taste => rasa_d
tangible => sprastavya_d
nose => ghrana_d
tongue => jihva_d
nose_cognition => ghranavijnana_d
tongue_cognition => jihvavijnana_d
dharma_principle => dharma_d
pratisamkhya_nirodha => pratisamkhya_nirodha_m
association => samprayoga_g
nature => svabhava_g
arising => samuttha_g
vijnapti => vijnapti_g
dhyana_account => dhyana_account_m
varnayanti_account => varnayanti_account_m
AmongEighteen => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d,mano_d,dharma_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d}
PrincipleLevel => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d,mano_d,dharma_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d}
BaseLevel => {rupa_skandha}
RealmLevel => {kama_dhatu,rupa_dhatu_realm}
FormBearing => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d}
GatheredIn => {(caksur_d,rupa_skandha),(srotra_d,rupa_skandha),(ghrana_d,rupa_skandha),(jihva_d,rupa_skandha),(kaya_d,rupa_skandha),(rupa_d,rupa_skandha),(sabda_d,rupa_skandha),(gandha_d,rupa_skandha),(rasa_d,rupa_skandha),(sprastavya_d,rupa_skandha)}
OnlyIndeterminate => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,gandha_d,rasa_d,sprastavya_d}
Threefold => {rupa_d,sabda_d,mano_d,dharma_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d}
CanBeWholesome => {rupa_d,sabda_d,mano_d,dharma_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d,pratisamkhya_nirodha_m}
CanBeUnwholesome => {rupa_d,sabda_d,mano_d,dharma_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d}
CanBeIndeterminate => {rupa_d,sabda_d,mano_d,dharma_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d}
CittaPrinciple => {mano_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d}
ThreefoldBy => {(mano_d,samprayoga_g),(caksurvijnana_d,samprayoga_g),(srotravijnana_d,samprayoga_g),(ghranavijnana_d,samprayoga_g),(jihvavijnana_d,samprayoga_g),(kayavijnana_d,samprayoga_g),(manovijnana_d,samprayoga_g),(dharma_d,svabhava_g),(dharma_d,samprayoga_g),(dharma_d,samuttha_g),(rupa_d,vijnapti_g),(sabda_d,vijnapti_g)}
PortionOf => {(pratisamkhya_nirodha_m,dharma_d)}
ConnectedWith => {(caksur_d,kama_dhatu),(srotra_d,kama_dhatu),(ghrana_d,kama_dhatu),(jihva_d,kama_dhatu),(kaya_d,kama_dhatu),(rupa_d,kama_dhatu),(sabda_d,kama_dhatu),(gandha_d,kama_dhatu),(rasa_d,kama_dhatu),(sprastavya_d,kama_dhatu),(mano_d,kama_dhatu),(dharma_d,kama_dhatu),(caksurvijnana_d,kama_dhatu),(srotravijnana_d,kama_dhatu),(ghranavijnana_d,kama_dhatu),(jihvavijnana_d,kama_dhatu),(kayavijnana_d,kama_dhatu),(manovijnana_d,kama_dhatu),(caksur_d,rupa_dhatu_realm),(srotra_d,rupa_dhatu_realm),(ghrana_d,rupa_dhatu_realm),(jihva_d,rupa_dhatu_realm),(kaya_d,rupa_dhatu_realm),(rupa_d,rupa_dhatu_realm),(sabda_d,rupa_dhatu_realm),(sprastavya_d,rupa_dhatu_realm),(mano_d,rupa_dhatu_realm),(dharma_d,rupa_dhatu_realm),(caksurvijnana_d,rupa_dhatu_realm),(srotravijnana_d,rupa_dhatu_realm),(kayavijnana_d,rupa_dhatu_realm),(manovijnana_d,rupa_dhatu_realm)}
MorselFood => {gandha_d,rasa_d,sprastavya_d}
SupportOf => {(gandha_d,ghranavijnana_d),(rasa_d,jihvavijnana_d)}
HasUse => {sprastavya_d,ghrana_d,jihva_d}
AttributedToOthers => {dhyana_account_m}
Explained => {varnayanti_account_m}
```

**Model checks.** Ten others, all threefold, each with at least one ground:
association for the seven Cognition and Mind Principles; nature,
association, and arising for the Dharma Principle; *vijñapti* for Visible
Form and Sound. Eighteen in the Desire Realm; fourteen in the Form Realm.
Three levels are disjoint: one Base, eighteen Principles, two Realms. The
Form Base gathers exactly the ten Form-bearing Principles and is none of
them. Removing a Faculty from the Form Realm, or admitting a Cognition
whose support is absent, falsifies the theory.

**Bhāṣya determination.** Odor and Taste are absent from the Form Realm
because they are morsel food, and those born there are free of passion for
it; their Cognitions go with the support. The Tangible is morsel food too,
yet stays: what is not food in it serves as support of a Faculty, as basis,
and as covering. The nose and tongue Faculties stay: arising is by force of
a cause, not of a use, and craving there proceeds by way of the person, not
by way of the Condition. The concentration account is the others'; the
closing explanation is introduced by *evaṃ tu varṇayanti*.

**Organon interpretation.** The levels are not interchangeable views of one
list. The Form Base, the Form-bearing Principles, and the Form Realm are
three determinations at three levels; the same *rūpa* can be named at each,
and each is checked separately. The Form Base gathers ten Principles and is
not a Principle; the Form Realm shares a name with a Principle and is not
it. How Base and Principle relate as levels of Cognition is left open.
1.31 is not opened. The earlier schematic follows.

```text
the other ten
    threefold
    the Cognition Principle, the seven, by association
    Dharma Principle by nature, association, arising
    Visible Form and Sound by vijñapti

all eighteen
    connected with the Desire Realm

Form Realm
    fourteen
    excluding Odor, Taste
    excluding nose-Cognition, tongue-Cognition
    not excluding nose and tongue

1.31 not opened
```

## 9. Interpretive Note

**Translation note.** The Bhāṣya identifies the other ten as the Principles
left after the preceding count and explains threefold as wholesome,
unwholesome, or indeterminate. All eighteen are connected with the Desire
Realm. In the Form Realm, Odor and Taste are absent, so nose- and
tongue-Cognition lack their Conditions; the Faculties themselves remain, for
support and bodily appearance. Other proposed explanations of the exclusion
remain attributed in the commentary.

The hinge is the verse boundary. *Tridhā anye* closes the ethical question. *Kāmadhātvāptāḥ* opens the realms. The exclusion is four Principles.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_30 a vak:Karika ;
    vak:hasTopic vak:ThreefoldAndFourteen ;
    vak:belongsTo vak:Dhatunirdesa .

vak:OtherTen vak:ethicalStatus vak:Wholesome, vak:Unwholesome, vak:Indeterminate .
vak:EighteenPrinciples vak:connectedWith vak:DesireRealm .
vak:FormRealm vak:includesCount 14 ;
    vak:excludes vak:SmellPrinciple, vak:TastePrinciple,
        vak:NoseCognitionPrinciple, vak:TongueCognitionPrinciple .
```
