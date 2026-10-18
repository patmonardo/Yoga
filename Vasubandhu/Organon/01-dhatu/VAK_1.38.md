# VAK_1.38 — Three Ways, One Dravya, Three Moments

## 1. Sanskrit (Devanāgarī)

```sanskrit
त्रिधान्ये द्रव्यवानेकः क्षणिकाः पश्चिमास्त्रयः ।
चक्षुर्विज्ञानधात्वोः स्यात् पृथग्लाभः सहापि च ॥ १.३८ ॥
```

## 2. Sanskrit (IAST)

```text
tridhānye dravyavān ekaḥ kṣaṇikāḥ paścimās trayaḥ /
cakṣurvijñānadhātvoḥ syāt pṛthag lābhaḥ sahāpi ca // 1.38 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| tridhā | adverb of manner | in three ways: maturation-born, upacaya-reinforced, continuity-born |
| anye | anya; nominative masculine plural | the others: the four left by 1.37 |
| dravyavān | dravya-vat; nominative masculine singular | bearing *dravya* |
| ekaḥ | eka; nominative masculine singular | one: the Dharma Principle |
| kṣaṇikāḥ | kṣaṇa + -ika; nominative masculine plural | momentary |
| paścimāḥ | paścima; nominative masculine plural | last: in the order of recitation |
| trayaḥ | tri; nominative masculine plural | three: Mind, Dharma, Mind-Cognition |
| cakṣur-vijñāna-dhātvoḥ | dvandva; genitive dual | of the Eye Principle and the Eye-Cognition Principle |
| syāt | √as, optative 3rd singular | there may be |
| pṛthak | adverb | separately |
| lābhaḥ | lābha; nominative masculine singular | acquisition |
| saha | adverb | together |
| api ca | particles | also; and: gathers the further working for Visible Form |

The others are Visible Form, Taste, Odor, and Tangible: eighteen less the
five Faculties, Sound, and the eight of 1.37. The one is the Dharma
Principle. The last three are the Mind Principle, the Dharma Principle,
and the Mind-Cognition Principle.

**Grammar tokens.** Verse-order IAST with sandhi opened (`tridhānye` →
*tridhā anye*, `paścimās trayaḥ` → *paścimāḥ trayaḥ*, `pṛthag` → *pṛthak*,
`sahāpi` → *saha api*) and compound boundaries marked. The dvandva
*cakṣur-vijñāna-dhātvoḥ* is read *cakṣur-dhātu* + *cakṣur-vijñāna-dhātu*,
as the Bhāṣya does.

```text
# tokens: tridhā anye dravyavān ekaḥ kṣaṇikāḥ paścimāḥ trayaḥ cakṣur-vijñāna-dhātvoḥ syāt pṛthak lābhaḥ saha api ca
```

## 4. Grammar

Four predications. The first three are nominal sentences whose subject
carries a count: *anye* is the class of four, *ekaḥ* is one and is read
as uniqueness, *paścimāḥ trayaḥ* is the class of three. The fourth is a
modal sentence: the genitive dual supplies the pair, *syāt* makes the
claim one of possibility, and *pṛthak* and *saha* give the two ways of
acquiring it. *Api ca* adds nothing to the formula; the Bhāṣya reads it as
gathering the same working for Visible Form.

```nltk-fcfg
% start S
# tokens: tridhā anye dravyavān ekaḥ kṣaṇikāḥ paścimāḥ trayaḥ cakṣur-vijñāna-dhātvoḥ syāt pṛthak lābhaḥ saha api ca
S[SEM=<(?a & ?b & ?c & ?d)>] -> THREEWAYS[SEM=?a] ONE[SEM=?b] LAST[SEM=?c] ACQ[SEM=?d]
THREEWAYS[SEM=<all x.(?k(x) -> ?p(x))>] -> TRIDHA[SEM=?p] ANYE[NUM=pl,CNT=4,SEM=?k]
ONE[SEM=<exists x.(?p(x) & all y.(?p(y) -> (y = x)))>] -> DRAVYAVAT[NUM=sg,SEM=?p] EKA[NUM=sg,CNT=1]
LAST[SEM=<all x.(?k(x) -> ?p(x))>] -> KSANIKA[NUM=pl,SEM=?p] PASCIMA[NUM=pl,CNT=?n,SEM=?k] TRI[NUM=pl,CNT=?n]
ACQ[SEM=<(?pair(?sep) & ?pair(?tog))>] -> PAIR[CASE=gen,NUM=dual,SEM=?pair] SYAT PRTHAK[SEM=?sep] LABHA[NUM=sg] SAHA[SEM=?tog] API CA
TRIDHA[SEM=<\x.(exists i.(InstanceOf(i,x) & Born(i,vipaka)) & exists i.(InstanceOf(i,x) & Born(i,upacaya)) & exists i.(InstanceOf(i,x) & Born(i,naisyandika)))>] -> 'tridhā'
ANYE[NUM=pl,CNT=4,SEM=<\x.Remaining(x)>] -> 'anye'
DRAVYAVAT[NUM=sg,SEM=<\x.DravyaBearing(x)>] -> 'dravyavān'
EKA[NUM=sg,CNT=1] -> 'ekaḥ'
KSANIKA[NUM=pl,SEM=<\x.Momentary(x)>] -> 'kṣaṇikāḥ'
PASCIMA[NUM=pl,CNT=3,SEM=<\x.LastThree(x)>] -> 'paścimāḥ'
TRI[NUM=pl,CNT=3] -> 'trayaḥ'
PAIR[CASE=gen,NUM=dual,SEM=<\R.R(eye_principle,eye_cognition)>] -> 'cakṣur-vijñāna-dhātvoḥ'
SYAT -> 'syāt'
PRTHAK[SEM=<\a b.(exists c.(AcqCase(c) & Acquires(c,a) & -Acquires(c,b)) & exists c.(AcqCase(c) & Acquires(c,b) & -Acquires(c,a)))>] -> 'pṛthak'
LABHA[NUM=sg] -> 'lābhaḥ'
SAHA[SEM=<\a b.exists c.(AcqCase(c) & Acquires(c,a) & Acquires(c,b))>] -> 'saha'
API -> 'api'
CA -> 'ca'
```

```nltk-dep
'tridhā' -> 'anye'
'dravyavān' -> 'ekaḥ'
'kṣaṇikāḥ' -> 'trayaḥ'
'trayaḥ' -> 'paścimāḥ'
'syāt' -> 'lābhaḥ'
'lābhaḥ' -> 'cakṣur-vijñāna-dhātvoḥ' | 'pṛthak' | 'saha'
'saha' -> 'api'
'api' -> 'ca'
```

**Close construe.** The others are threefold. One is *dravya*-bearing.
The last three are momentary. Of the Eye and Eye-Cognition Principles
there may be acquisition separately, and also together.

*Syāt* is read as existence among the cases of acquisition: separately
in each direction, and together. "Neither" is the Bhāṣya's, not the
verse's. Threefold is said through instances, as in 1.37. *Ekaḥ* is
uniqueness: no other Principle bears *dravya*.

## 5. Translation

### Literal Translation

> The others are of three kinds. One is dravya-bearing. The last three are
> momentary. Of the eye-Principle and the Cognition Principle there may be
> separate acquisition, and also together.

### Bhāṣya-informed study translation

> The four remaining Principles are threefold. One is *dravya*-bearing. The
> last three are momentary. The Eye Principle and the Eye-Cognition Principle
> may be acquired separately or together.

## 6. Philosophical Translation

Four Principles remain after the verse that named the causal kinds. Those four take all three: maturation, upacaya-reinforcement, homogeneous continuation. The one that bears dravya is not one of them. It is the Dharma Principle, because the unconditioned is in it, and the commentary calls the unconditioned dravya because it is the core. That claim is the commentary's. It does not make any of the eighteen a substance.

The last three are momentary in one place only. The first Pure complex, the receptivity to dharma-knowledge of suffering, has one moment without homogeneous continuation. The citta of that moment is Mind Principle and Mind-Cognition Principle. What arises with it is the Dharma Principle. Outside that moment, no conditioned dharma lacks the continuation.

Acquisition of the Eye and of the Eye-Cognition is not one event. Separate, together, or neither. Possession repeats the four. The particle extends the same working to Visible Form.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| anye | the others | Visible Form, Taste, Odor, Tangible |
| vipākaja | maturation-born | one of the three |
| aupacayika | upacaya-reinforced | one of the three; not the atomic accumulation of 1.35 |
| naiḥṣyandika | homogeneous continuation | not an outflow |
| dravyavān | dravya-bearing | the Dharma Principle alone |
| sāra | core | the commentary's reason; not a substance |
| kṣaṇika | momentary | one moment in the first Pure complex |
| anāsrava | Pure | the first complex |
| cakṣur-dhātu | Eye Principle | the Faculty as Principle |
| cakṣur-vijñāna-dhātu | Eye-Cognition Principle | acquisition may split from the eye |
| lābha | acquisition | separate or together |
| samanvāgama | possession | four cases |

## 8. Logical Determination

**Kārikā, derived.** Each of the remaining four has maturation-born,
upacaya-reinforced, and continuity-born instances; exactly one Principle
bears *dravya*; the last three are momentary; and among the cases of
acquisition the Eye and Eye-Cognition Principles are acquired each
without the other, and together.

```nltk-sem
# derived by the section 4 parse
(all x.(Remaining(x) -> (exists i.(InstanceOf(i,x) & Born(i,vipaka)) & exists i.(InstanceOf(i,x) & Born(i,upacaya)) & exists i.(InstanceOf(i,x) & Born(i,naisyandika)))) & exists x.(DravyaBearing(x) & all y.(DravyaBearing(y) -> (y = x))) & all x.(LastThree(x) -> Momentary(x)) & exists c.(AcqCase(c) & Acquires(c,eye_principle) & -Acquires(c,eye_cognition)) & exists c.(AcqCase(c) & Acquires(c,eye_cognition) & -Acquires(c,eye_principle)) & exists c.(AcqCase(c) & Acquires(c,eye_principle) & Acquires(c,eye_cognition)))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all x.(Remaining(x) -> (exists i.(InstanceOf(i,x) & Born(i,vipaka)) & exists i.(InstanceOf(i,x) & Born(i,upacaya)) & exists i.(InstanceOf(i,x) & Born(i,naisyandika)))) & exists x.(DravyaBearing(x) & all y.(DravyaBearing(y) -> (y = x))) & all x.(LastThree(x) -> Momentary(x)) & exists c.(AcqCase(c) & Acquires(c,eye_principle) & -Acquires(c,eye_cognition)) & exists c.(AcqCase(c) & Acquires(c,eye_cognition) & -Acquires(c,eye_principle)) & exists c.(AcqCase(c) & Acquires(c,eye_principle) & Acquires(c,eye_cognition)))
# THEORY prose
# EXPECT prose T
all x.(Remaining(x) <-> ((x = visible_form) | (x = taste) | (x = odor) | (x = tangible)))
all x.(AmongEighteen(x) -> (DravyaBearing(x) <-> exists i.(InstanceOf(i,x) & Unconditioned(i))))
all i.(Unconditioned(i) -> Core(i))
all x.(LastThree(x) <-> ((x = mind) | (x = dharma_principle) | (x = mind_cognition)))
all x.(AmongEighteen(x) -> (Momentary(x) <-> exists i.(InstanceOf(i,x) & InMoment(i,first_pure) & -Born(i,naisyandika))))
all i.(InMoment(i,first_pure) -> Pure(i))
all i.((InMoment(i,first_pure) & Citta(i)) <-> (InMoment(i,first_pure) & (InstanceOf(i,mind) | InstanceOf(i,mind_cognition))))
all i.((InMoment(i,first_pure) & -Citta(i)) -> InstanceOf(i,dharma_principle))
all x.(LastThree(x) -> all i.((InstanceOf(i,x) & -Unconditioned(i) & -InMoment(i,first_pure)) -> Born(i,naisyandika)))
exists c.(c = kama_gradual & Acquires(c,eye_principle) & -Acquires(c,eye_cognition))
exists c.(c = formless_to_second & Acquires(c,eye_principle) & -Acquires(c,eye_cognition))
exists c.(c = second_seeing & Acquires(c,eye_cognition) & -Acquires(c,eye_principle))
exists c.(c = second_to_below & Acquires(c,eye_cognition) & -Acquires(c,eye_principle))
exists c.(c = formless_to_desire & Acquires(c,eye_principle) & Acquires(c,eye_cognition))
exists c.(c = formless_to_brahma & Acquires(c,eye_principle) & Acquires(c,eye_cognition))
exists p.(p = second_not_seeing & Possesses(p,eye_principle) & -Possesses(p,eye_cognition))
exists p.(p = desire_without_eye & Possesses(p,eye_cognition) & -Possesses(p,eye_principle))
exists p.(p = desire_with_eye & Possesses(p,eye_principle) & Possesses(p,eye_cognition))
exists p.(p = formless_being & -Possesses(p,eye_principle) & -Possesses(p,eye_cognition))
SameWorkingFor(eye_principle,visible_form) & SameWorkingFor(eye_cognition,visible_form)
# THEORY rejected_dravya_in_every_principle
# EXPECT rejected_dravya_in_every_principle F
all x.(AmongEighteen(x) -> DravyaBearing(x))
# THEORY rejected_second_dravya_bearer
# EXPECT rejected_second_dravya_bearer F
exists x.(DravyaBearing(x) & -(x = dharma_principle))
# THEORY rejected_all_conditioned_momentary
# EXPECT rejected_all_conditioned_momentary F
all x.(AmongEighteen(x) -> Momentary(x))
# THEORY rejected_momentary_outside_first_pure
# EXPECT rejected_momentary_outside_first_pure F
exists i.exists x.(LastThree(x) & InstanceOf(i,x) & -Unconditioned(i) & -InMoment(i,first_pure) & -Born(i,naisyandika))
# THEORY rejected_one_acquisition
# EXPECT rejected_one_acquisition F
all c.(AcqCase(c) -> (Acquires(c,eye_principle) <-> Acquires(c,eye_cognition)))
# THEORY rejected_possession_follows_the_eye
# EXPECT rejected_possession_follows_the_eye F
all p.(Being(p) -> (Possesses(p,eye_cognition) -> Possesses(p,eye_principle)))
# THEORY rejected_remaining_twofold_only
# EXPECT rejected_remaining_twofold_only F
all x.(Remaining(x) -> -exists i.(InstanceOf(i,x) & Born(i,upacaya)))
```

```nltk-valuation
vipaka => vipaka_m
upacaya => upacaya_m
naisyandika => naisyandika_m
visible_form => rupa_d
taste => rasa_d
odor => gandha_d
tangible => sprastavya_d
mind => mano_d
dharma_principle => dharma_d
mind_cognition => manovijnana_d
eye_principle => caksur_d
eye_cognition => caksurvijnana_d
first_pure => duhkhe_dharmajnanaksanti
kama_gradual => kama_kramasah
formless_to_second => arupya_to_dhyana2
second_seeing => dhyana2_sammukhi
second_to_below => dhyana2_to_adhah
formless_to_desire => arupya_to_kama
formless_to_brahma => arupya_to_brahmaloka
second_not_seeing => p_dhyana2_asammukhi
desire_without_eye => p_kama_alabdha
desire_with_eye => p_kama_labdha
formless_being => p_arupya
AmongEighteen => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d,mano_d,dharma_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d}
Remaining => {rupa_d,rasa_d,gandha_d,sprastavya_d}
DravyaBearing => {dharma_d}
LastThree => {mano_d,dharma_d,manovijnana_d}
Momentary => {mano_d,dharma_d,manovijnana_d}
InstanceOf => {(rupa_vip,rupa_d),(rupa_upa,rupa_d),(rupa_nai,rupa_d),(rasa_vip,rasa_d),(rasa_upa,rasa_d),(rasa_nai,rasa_d),(gandha_vip,gandha_d),(gandha_upa,gandha_d),(gandha_nai,gandha_d),(sprastavya_vip,sprastavya_d),(sprastavya_upa,sprastavya_d),(sprastavya_nai,sprastavya_d),(mano_ksanti,mano_d),(mano_later,mano_d),(manovijnana_ksanti,manovijnana_d),(manovijnana_later,manovijnana_d),(dharma_ksanti,dharma_d),(dharma_later,dharma_d),(dharma_asamskrta,dharma_d)}
Born => {(rupa_vip,vipaka_m),(rupa_upa,upacaya_m),(rupa_nai,naisyandika_m),(rasa_vip,vipaka_m),(rasa_upa,upacaya_m),(rasa_nai,naisyandika_m),(gandha_vip,vipaka_m),(gandha_upa,upacaya_m),(gandha_nai,naisyandika_m),(sprastavya_vip,vipaka_m),(sprastavya_upa,upacaya_m),(sprastavya_nai,naisyandika_m),(mano_later,naisyandika_m),(manovijnana_later,naisyandika_m),(dharma_later,naisyandika_m)}
Unconditioned => {dharma_asamskrta}
Core => {dharma_asamskrta}
InMoment => {(mano_ksanti,duhkhe_dharmajnanaksanti),(manovijnana_ksanti,duhkhe_dharmajnanaksanti),(dharma_ksanti,duhkhe_dharmajnanaksanti)}
Citta => {mano_ksanti,manovijnana_ksanti,mano_later,manovijnana_later}
Pure => {mano_ksanti,manovijnana_ksanti,dharma_ksanti}
AcqCase => {kama_kramasah,arupya_to_dhyana2,dhyana2_sammukhi,dhyana2_to_adhah,arupya_to_kama,arupya_to_brahmaloka}
Acquires => {(kama_kramasah,caksur_d),(arupya_to_dhyana2,caksur_d),(dhyana2_sammukhi,caksurvijnana_d),(dhyana2_to_adhah,caksurvijnana_d),(arupya_to_kama,caksur_d),(arupya_to_kama,caksurvijnana_d),(arupya_to_brahmaloka,caksur_d),(arupya_to_brahmaloka,caksurvijnana_d)}
Being => {p_dhyana2_asammukhi,p_kama_alabdha,p_kama_labdha,p_arupya}
Possesses => {(p_dhyana2_asammukhi,caksur_d),(p_kama_alabdha,caksurvijnana_d),(p_kama_labdha,caksur_d),(p_kama_labdha,caksurvijnana_d)}
SameWorkingFor => {(caksur_d,rupa_d),(caksurvijnana_d,rupa_d)}
```

**Model checks.** The verse formula holds. The prose names the four and
the three. It makes *dravya*-bearing exactly the having of an
unconditioned instance, which only the Dharma Principle has. Momentary
is the having of an instance in the first Pure moment that lacks
continuity; outside that moment every conditioned instance of the three
is continuity-born. The six acquisition cases and four possession cases
are the Bhāṣya's. All seven rejected theories are false.

**Bhāṣya determination.** *Asaṃskṛtaṃ hi sāratvād dravyam*: the
unconditioned is *dravya* because it is the core. *Prathamānāsrave duḥkhe
dharma-jñāna-kṣānti-kalāpe kṣaṇam ekam anaiḥṣyandikāḥ*: in the first Pure
complex, receptivity to Dharma-knowledge of suffering, the three are for
one moment not continuity-born. *Anyaḥ saṃskṛto nāsti kaścid
anaiḥṣyandikaḥ*: no other conditioned dharma lacks it.

**Organon interpretation.** Continuity is the rule of the conditioned;
the one exception is the first moment of the Path, which has no
homogeneous predecessor. What persists the series is Dharma, not the
Elements. The model scopes the exception claim to the three; 1.37 keeps
the Faculties' continuation from being counted as a separate class.

```text
four
    three causal kinds

dharma-Principle
    alone dravya-bearing
    the unconditioned is in it

last three
    momentary
    one moment, first Pure complex
    no other conditioned dharma lacks the continuation

eye : eye-cognition
    acquisition separate
    acquisition together
    neither
    possession fourfold

api
    the same for visible

1.39 not opened
```

## 9. Interpretive Note

**Key-term evidence.** *Naiḥṣyandika* is again the work of a Ground (*sabhāga-hetu*), and the momentary three are defined by its failure: the first Pure moment has no homogeneous predecessor to be its Ground. The unconditioned is the core (*sāra*) and is Grounded in nothing; it is the one *dravya*. Ground and core part company here.

**Principle, not Faculty.** The verse says *cakṣur-dhātu*, not *cakṣur-indriya*, and *api ca* adds Visible Form: Eye, Visible Form, and Eye-Cognition are in view as three Principles. Their conjunction is not stated here; 1.42 cites *cakṣur hi pratītya rūpāṇi cotpadyate cakṣur-vijñānam*, and 3.30 makes contact *saṃnipāta-ja*. The model keeps only the acquisition cases.

**Translation note.** The four remaining Principles are Visible Form, Taste, Odor, and Tangible, each of three kinds: maturation-born, increase-reinforced, and continuity-born. The Dharma Principle alone bears *dravya* because it includes the unconditioned. The last three are Mind, Dharma, and Mind-Cognition, momentary at the first Pure moment. Eye and Eye-Cognition may be acquired separately or together.

The hinge is the one moment. Momentary does not mean every dharma lasts a moment. It means these three, once, lack homogeneous continuation. Dravya stays the commentary's word for the unconditioned in the Dharma Principle. It is not a substance of the eighteen.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_38 a vak:Karika ;
    vak:hasTopic vak:ThreeWaysOneDravya ;
    vak:belongsTo vak:Dhatunirdesa .

vak:DharmaPrinciple vak:dravyaBearing true .
vak:LastThree vak:momentaryIn vak:FirstPureComplex .
vak:EyePrinciple vak:acquisitionIndependentOf vak:EyeCognitionPrinciple .
```
