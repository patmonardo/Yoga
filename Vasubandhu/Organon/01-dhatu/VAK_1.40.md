# VAK_1.40 — Abandoned by Seeing, by Cultivation, or Not

## 1. Sanskrit (Devanāgarī)

```sanskrit
दश भावनया हेयाः पञ्च चान्त्यास्त्रयस्त्रिधा ।
न दृष्टिहेयमक्लिष्टं न रूपं नाप्यषष्ठजम् ॥ १.४० ॥
```

## 2. Sanskrit (IAST)

```text
daśa bhāvanayā heyāḥ pañca cāntyās trayas tridhā /
na dṛṣṭiheyam akliṣṭaṃ na rūpaṃ nāpy aṣaṣṭhajam // 1.40 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| daśa | numeral | ten: the Form Principles (*rūpiṇaḥ*) |
| bhāvanayā | bhāvanā; instrumental singular | by cultivation |
| heyāḥ | √hā, gerundive; nominative masculine plural | to be abandoned: said of Principles |
| pañca | numeral | five: the sensory Cognition Principles |
| ca | particle | and: *pañca* shares the predicate |
| antyāḥ | antya; nominative masculine plural | the last, in the order of recitation |
| trayaḥ | tri; nominative masculine plural | three: Mind, Dharma, Mind-Cognition |
| tridhā | adverb | of three kinds: seeing, cultivation, not abandoned |
| na | negative particle | not: once for each excluded class |
| dṛṣṭi-heyam | tatpuruṣa gerundive; nominative neuter singular | abandoned by seeing: said of any dharma |
| akliṣṭam | a-kliṣṭa; nominative neuter singular | the unafflicted |
| rūpam | rūpa; nominative neuter singular | Form |
| api | particle | also |
| a-ṣaṣṭha-jam | upapada compound; nominative neuter singular | not born from the sixth, the Mind Essence |

The sixth is the Mind Essence (*mana-āyatana*). The last three are the
Mind, Dharma, and Mind-Cognition Principles.

**Grammar tokens.** Verse-order IAST with sandhi opened (`cāntyās` → *ca
antyāḥ*, `trayas` → *trayaḥ*, `akliṣṭaṃ` → *akliṣṭam*, `nāpy` → *na api*)
and compound boundaries marked.

```text
# tokens: daśa bhāvanayā heyāḥ pañca ca antyāḥ trayaḥ tridhā na dṛṣṭi-heyam akliṣṭam na rūpam na api a-ṣaṣṭha-jam
```

## 4. Grammar

Three clauses in two genders. The first two count Principles, so the
gerundive *heyāḥ* is masculine plural, with *dhātavaḥ* understood. *Daśa*
and *pañca* share it, and the count must make fifteen. *Antyāḥ trayaḥ*
adds the last three, and the grammar requires fifteen plus three: the
whole eighteen. *Tridhā* says that each of the three has instances of all
three kinds.

The third clause shifts to the neuter singular. *Dṛṣṭi-heyam* is said of
any dharma, not of a Principle, and each of the three negated subjects
must agree with it in gender and number. Each *na* removes one class from
abandonment by seeing. *A-ṣaṣṭha-jam* carries its own negative, so the
exclusion reads: whatever is not born from the sixth is not abandoned by
seeing.

```nltk-fcfg
% start S
# tokens: daśa bhāvanayā heyāḥ pañca ca antyāḥ trayaḥ tridhā na dṛṣṭi-heyam akliṣṭam na rūpam na api a-ṣaṣṭha-jam
S[SEM=<(?a & ?b & ?c)>] -> CUL[CNT=15,SEM=?a] TRI[CNT=3,SEM=?b] EXCL[SEM=?c]
CUL[CNT=15,SEM=<all x.((?p(x) | ?q(x)) -> all i.(InstanceOf(i,x) -> ?m(i)))>] -> NUMR[CNT=10,SEM=?p] VP[GEN=m,NUM=pl,SEM=?m] NUMR[CNT=5,SEM=?q] CA
VP[GEN=?g,NUM=?n,SEM=?m] -> INS[SEM=?m] HEYA[GEN=?g,NUM=?n]
TRI[CNT=?k,SEM=<all x.(?l(x) -> (exists i.(InstanceOf(i,x) & DarsanaHeya(i)) & exists i.(InstanceOf(i,x) & BhavanaHeya(i)) & exists i.(InstanceOf(i,x) & Aheya(i))))>] -> ANTYA[NUM=pl,SEM=?l] NUMR[CNT=?k] TRIDHA[CNT=?k]
EXCL[SEM=<(all i.(?a(i) -> -?h(i)) & all i.(?b(i) -> -?h(i)) & all i.(?c(i) -> -?h(i)))>] -> NA DHEYA[GEN=?g,NUM=?n,SEM=?h] NP[GEN=?g,NUM=?n,SEM=?a] NA NP[GEN=?g,NUM=?n,SEM=?b] NA API NP[GEN=?g,NUM=?n,SEM=?c]
NUMR[CNT=10,SEM=<\x.Rupin(x)>] -> 'daśa'
NUMR[CNT=5,SEM=<\x.SensoryCognition(x)>] -> 'pañca'
NUMR[CNT=3] -> 'trayaḥ'
INS[SEM=<\i.BhavanaHeya(i)>] -> 'bhāvanayā'
HEYA[GEN=m,NUM=pl] -> 'heyāḥ'
CA -> 'ca'
ANTYA[NUM=pl,SEM=<\x.LastThree(x)>] -> 'antyāḥ'
TRIDHA[CNT=3] -> 'tridhā'
NA -> 'na'
API -> 'api'
DHEYA[GEN=n,NUM=sg,SEM=<\i.DarsanaHeya(i)>] -> 'dṛṣṭi-heyam'
NP[GEN=n,NUM=sg,SEM=<\i.Unafflicted(i)>] -> 'akliṣṭam'
NP[GEN=n,NUM=sg,SEM=<\i.Form(i)>] -> 'rūpam'
NP[GEN=n,NUM=sg,SEM=<\i.-BornFromSixth(i)>] -> 'a-ṣaṣṭha-jam'
```

```nltk-dep
'heyāḥ' -> 'bhāvanayā' | 'daśa' | 'pañca'
'pañca' -> 'ca'
'tridhā' -> 'trayaḥ'
'trayaḥ' -> 'antyāḥ'
'dṛṣṭi-heyam' -> 'na' | 'akliṣṭam' | 'rūpam' | 'a-ṣaṣṭha-jam'
'a-ṣaṣṭha-jam' -> 'api'
```

**Close construe.** Ten are to be abandoned by cultivation, and five. The
last three are of three kinds. What is unafflicted is not abandoned by
seeing; nor Form; nor what is not born from the sixth.

The count clauses speak of Principles; the exclusion speaks of dharmas.
Abandonment is a status of instances, so the model reads every clause
through `InstanceOf`.

## 5. Translation

### Literal Translation

> Ten are abandoned by cultivation, and five. The last three are threefold.
> Nothing unafflicted is abandoned by seeing, nor Form, nor what is not born
> from the sixth.

### Bhāṣya-informed study translation

> The ten Form Principles and the five sensory Cognition Principles are
> abandoned by cultivation. The last three—the Mind, Dharma, and
> Mind-Cognition Principles—are of three kinds. Nothing unafflicted is
> abandoned by seeing, nothing of Form, and nothing not born from the sixth
> Essence.

## 6. Philosophical Translation

Abandonment by seeing does not reach Form, and it does not reach the five sensory Cognitions. Those fifteen are abandoned by cultivation. Only the last three take all three statuses. What is abandoned by seeing in them is the eighty-eight, what arises with them, their acquisitions, and their attendants. The rest of the Impure in them is abandoned by cultivation. The Pure is not abandoned.

The objection offers two more for seeing: ordinary-person status, and body and speech action to a bad destination, because both oppose the path. The verse excludes them. Ordinary-person status is unafflicted and indeterminate. It is still possessed when the wholesome roots are cut, and when attachment is gone. Body and speech action is Form. Seeing does not abandon Form. And there is no misapprehension of the truths in that status. If seeing abandoned it, the status would still be there at the receptivity to Dharma-knowledge of suffering.

The sixth is the Mind Essence. What is not born from it, including what is born of the five Faculties, is not abandoned by seeing. The cut is the Mind Essence, not the five.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| darśana-heya | abandoned by seeing | the verse says dṛṣṭi-heya |
| bhāvanā-heya | abandoned by cultivation | the ten Form Principles and the five sensory Cognitions |
| aheya | not abandoned | the Pure |
| antyāḥ trayaḥ | the last three | Mind, Dharma, Mind-Cognition Principles |
| anuśaya | latent affliction | eighty-eight, with what arises with them |
| pṛthagjanatva | ordinary-person status | unafflicted and indeterminate |
| aṣaṣṭhaja | not born from the sixth | the sixth is the Mind Essence |
| mana-āyatana | Mind Essence | the sixth; Essence renders āyatana |
| sāsrava | Impure | the remainder, abandoned by cultivation |
| anāsrava | Pure | not abandoned |

## 8. Logical Determination

**Kārikā, derived.** Every instance of a Form Principle or a sensory
Cognition Principle is abandoned by cultivation. Each of the last three
Principles has instances abandoned by seeing, instances abandoned by
cultivation, and instances not abandoned. No unafflicted instance, no Form
instance, and no instance not born from the sixth is abandoned by seeing.

```nltk-sem
# derived by the section 4 parse
(all x.((Rupin(x) | SensoryCognition(x)) -> all i.(InstanceOf(i,x) -> BhavanaHeya(i))) & all x.(LastThree(x) -> (exists i.(InstanceOf(i,x) & DarsanaHeya(i)) & exists i.(InstanceOf(i,x) & BhavanaHeya(i)) & exists i.(InstanceOf(i,x) & Aheya(i)))) & all i.(Unafflicted(i) -> -DarsanaHeya(i)) & all i.(Form(i) -> -DarsanaHeya(i)) & all i.(-BornFromSixth(i) -> -DarsanaHeya(i)))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all x.((Rupin(x) | SensoryCognition(x)) -> all i.(InstanceOf(i,x) -> BhavanaHeya(i))) & all x.(LastThree(x) -> (exists i.(InstanceOf(i,x) & DarsanaHeya(i)) & exists i.(InstanceOf(i,x) & BhavanaHeya(i)) & exists i.(InstanceOf(i,x) & Aheya(i)))) & all i.(Unafflicted(i) -> -DarsanaHeya(i)) & all i.(Form(i) -> -DarsanaHeya(i)) & all i.(-BornFromSixth(i) -> -DarsanaHeya(i)))
# THEORY prose
# EXPECT prose T
all x.(LastThree(x) <-> (x = mind | x = dharma_principle | x = mind_cognition))
all i.(DarsanaHeya(i) <-> (SeeingAnusaya(i) | exists a.(SeeingAnusaya(a) & (ArisesWith(i,a) | AcquisitionOf(i,a) | AttendantOf(i,a)))))
all i.(BhavanaHeya(i) <-> (Impure(i) & -DarsanaHeya(i)))
all i.(Aheya(i) <-> Pure(i))
all i.(exists x.InstanceOf(i,x) -> (Pure(i) <-> -Impure(i)))
all i.(exists x.InstanceOf(i,x) -> (Unafflicted(i) <-> -Afflicted(i)))
all i.(BornOfFiveFaculties(i) -> -BornFromSixth(i))
exists p.(p = prthagjanatva & Unafflicted(p) & Indeterminate(p) & OpposesPath(p) & BhavanaHeya(p))
exists p.(p = prthagjanatva & PossessedBy(p,root_cutter) & PossessedBy(p,free_of_attachment))
exists k.(k = bad_destination_action & Form(k) & OpposesPath(k) & BhavanaHeya(k))
exists g.(g = greedy_eye_cognition & Afflicted(g) & BornOfFiveFaculties(g) & BhavanaHeya(g))
exists s.(s = sixth & s = mind_essence)
# THEORY rejected_opposition_suffices
# EXPECT rejected_opposition_suffices F
all i.(OpposesPath(i) -> DarsanaHeya(i))
# THEORY rejected_ordinary_status_by_seeing
# EXPECT rejected_ordinary_status_by_seeing F
exists p.(p = prthagjanatva & DarsanaHeya(p))
# THEORY rejected_form_by_seeing
# EXPECT rejected_form_by_seeing F
exists i.(Form(i) & DarsanaHeya(i))
# THEORY rejected_affliction_suffices
# EXPECT rejected_affliction_suffices F
all i.(Afflicted(i) -> DarsanaHeya(i))
# THEORY rejected_fifteen_have_pure
# EXPECT rejected_fifteen_have_pure F
exists x.((Rupin(x) | SensoryCognition(x)) & exists i.(InstanceOf(i,x) & Aheya(i)))
# THEORY rejected_pure_abandoned
# EXPECT rejected_pure_abandoned F
exists i.(Pure(i) & -Aheya(i))
# THEORY rejected_last_three_cultivation_only
# EXPECT rejected_last_three_cultivation_only F
exists x.(LastThree(x) & all i.(InstanceOf(i,x) -> BhavanaHeya(i)))
```

```nltk-valuation
dharma_principle => dharma_d
mind => mano_d
mind_cognition => manovijnana_d
prthagjanatva => prthagjanatva_i
bad_destination_action => apayika_karma_i
greedy_eye_cognition => caksurvijnana_raga_i
root_cutter => samucchinna_p
free_of_attachment => vitaraga_p
sixth => mana_ayatana
mind_essence => mana_ayatana
Rupin => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d}
SensoryCognition => {caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d}
LastThree => {mano_d,dharma_d,manovijnana_d}
InstanceOf => {(caksur_i,caksur_d),(srotra_i,srotra_d),(ghrana_i,ghrana_d),(jihva_i,jihva_d),(kaya_i,kaya_d),(rupa_i,rupa_d),(sabda_i,sabda_d),(gandha_i,gandha_d),(rasa_i,rasa_d),(sprastavya_i,sprastavya_d),(apayika_karma_i,rupa_d),(caksurvijnana_i,caksurvijnana_d),(srotravijnana_i,srotravijnana_d),(ghranavijnana_i,ghranavijnana_d),(jihvavijnana_i,jihvavijnana_d),(kayavijnana_i,kayavijnana_d),(caksurvijnana_raga_i,caksurvijnana_d),(anusaya_i,dharma_d),(anusaya_prapti_i,dharma_d),(anusaya_jati_i,dharma_d),(prthagjanatva_i,dharma_d),(avijnapti_i,dharma_d),(dharma_cult_i,dharma_d),(marga_i,dharma_d),(nirvana_i,dharma_d),(mano_view_i,mano_d),(mano_cult_i,mano_d),(mano_pure_i,mano_d),(manovijnana_view_i,manovijnana_d),(manovijnana_cult_i,manovijnana_d),(manovijnana_pure_i,manovijnana_d)}
DarsanaHeya => {anusaya_i,anusaya_prapti_i,anusaya_jati_i,mano_view_i,manovijnana_view_i}
BhavanaHeya => {caksur_i,srotra_i,ghrana_i,jihva_i,kaya_i,rupa_i,sabda_i,gandha_i,rasa_i,sprastavya_i,apayika_karma_i,caksurvijnana_i,srotravijnana_i,ghranavijnana_i,jihvavijnana_i,kayavijnana_i,caksurvijnana_raga_i,prthagjanatva_i,avijnapti_i,dharma_cult_i,mano_cult_i,manovijnana_cult_i}
Aheya => {marga_i,nirvana_i,mano_pure_i,manovijnana_pure_i}
Afflicted => {caksurvijnana_raga_i,anusaya_i,anusaya_prapti_i,anusaya_jati_i,dharma_cult_i,mano_view_i,mano_cult_i,manovijnana_view_i,manovijnana_cult_i}
Unafflicted => {caksur_i,srotra_i,ghrana_i,jihva_i,kaya_i,rupa_i,sabda_i,gandha_i,rasa_i,sprastavya_i,apayika_karma_i,caksurvijnana_i,srotravijnana_i,ghranavijnana_i,jihvavijnana_i,kayavijnana_i,prthagjanatva_i,avijnapti_i,marga_i,nirvana_i,mano_pure_i,manovijnana_pure_i}
Impure => {caksur_i,srotra_i,ghrana_i,jihva_i,kaya_i,rupa_i,sabda_i,gandha_i,rasa_i,sprastavya_i,apayika_karma_i,caksurvijnana_i,srotravijnana_i,ghranavijnana_i,jihvavijnana_i,kayavijnana_i,caksurvijnana_raga_i,anusaya_i,anusaya_prapti_i,anusaya_jati_i,prthagjanatva_i,avijnapti_i,dharma_cult_i,mano_view_i,mano_cult_i,manovijnana_view_i,manovijnana_cult_i}
Pure => {marga_i,nirvana_i,mano_pure_i,manovijnana_pure_i}
Form => {caksur_i,srotra_i,ghrana_i,jihva_i,kaya_i,rupa_i,sabda_i,gandha_i,rasa_i,sprastavya_i,apayika_karma_i,avijnapti_i}
BornFromSixth => {anusaya_i,anusaya_prapti_i,anusaya_jati_i,dharma_cult_i,marga_i,mano_view_i,mano_cult_i,mano_pure_i,manovijnana_view_i,manovijnana_cult_i,manovijnana_pure_i}
BornOfFiveFaculties => {caksurvijnana_i,srotravijnana_i,ghranavijnana_i,jihvavijnana_i,kayavijnana_i,caksurvijnana_raga_i}
OpposesPath => {apayika_karma_i,prthagjanatva_i}
Indeterminate => {prthagjanatva_i}
SeeingAnusaya => {anusaya_i}
ArisesWith => {(mano_view_i,anusaya_i),(manovijnana_view_i,anusaya_i)}
AcquisitionOf => {(anusaya_prapti_i,anusaya_i)}
AttendantOf => {(anusaya_jati_i,anusaya_i)}
PossessedBy => {(prthagjanatva_i,samucchinna_p),(prthagjanatva_i,vitaraga_p)}
```

**Model checks.** The verse formula holds. In the prose the three statuses
partition the instances:
- seeing takes the eighty-eight, with what arises with them, their
  acquisitions, and their attendants;
- cultivation takes the rest of the Impure;
- the Pure is not abandoned.

Ordinary-person status opposes the path, yet it is abandoned by
cultivation. So is bad-destination action, which is Form. Greedy
Eye-Cognition is afflicted but born of the five Faculties, so seeing does
not take it either. All seven rejected theories are false.

**Bhāṣya determination.** *Aṣṭāśīty anuśayāḥ tat-sahabhuvas tat-prāptayaś
ca sānucarā darśana-heyāḥ*: seeing takes the eighty-eight, with what arises
with them, their acquisitions, and their attendants. *Akliṣṭāvyākṛtaṃ ca
pṛthagjanatvam*: ordinary-person status is unafflicted and indeterminate.
*Ṣaṣṭham ucyate mana-āyatanam*: the sixth is the Mind Essence.

**Organon interpretation.** Abandonment by seeing has a three-part access
condition: afflicted, not Form, and born from the Mind Essence. Opposing
the path does not meet it, and affliction alone does not either. Seeing
reaches only what the sixth Essence produces; the five Faculties and Form
are reached by cultivation.

The Pure is not abandoned because the Pure does the abandoning. Seeing and
cultivation are Pure paths; what they abandon is the Impure. The third
status is the agent of the other two.

```text
fifteen
    ten Form Principles
    five sensory Cognitions
    abandoned by cultivation

last three
    seeing
    cultivation
    not abandoned

excluded from seeing
    unafflicted
    Form
    not born from the Mind Essence

ordinary-person status
    unafflicted, indeterminate
    still possessed when roots are cut

body and speech action
    Form
    not abandoned by seeing

1.41 not opened
```

## 9. Interpretive Note

**Translation note.** The Bhāṣya identifies “the sixth” as the Mind Essence (*mana-āyatana*), so the translation names the Essence. *Tridhā* is rendered “of three kinds”: each of the last three has instances in all three statuses.

The hinge is the exclusion. Opposing the path is not enough. Seeing abandons only what is afflicted, not Form, and born from the sixth. The fifteen never enter that count.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_40 a vak:Karika ;
    vak:hasTopic vak:AbandonmentBySeeingOrCultivation ;
    vak:belongsTo vak:Dhatunirdesa .

vak:TenOfForm vak:abandonedBy vak:Cultivation .
vak:LastThree vak:pathStatus "threefold" .
vak:SeeingAbandonment vak:excludes vak:Unafflicted, vak:Form, vak:NotBornFromTheSixth .
```
