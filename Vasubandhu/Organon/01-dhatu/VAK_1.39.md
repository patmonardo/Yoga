# VAK_1.39 — Inner Twelve, and the Work

## 1. Sanskrit (Devanāgarī)

```sanskrit
द्वादशाध्यात्मिका हित्वा रूपादीन् धर्मसंज्ञकः ।
सभागस्तत्सभागाश्च शेषा यो न स्वकर्मकृत् ॥ १.३९ ॥
```

## 2. Sanskrit (IAST)

```text
dvādaśādhyātmikā hitvā rūpādīn dharmasaṃjñakaḥ /
sabhāgas tatsabhāgāś ca śeṣā yo na svakarmakṛt // 1.39 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| dvādaśa | numeral | twelve |
| ādhyātmikāḥ | adhi-ātma + -ika; nominative masculine plural | inner: near citta as support |
| hitvā | √hā, absolutive | having set aside |
| rūpa-ādīn | bahuvrīhi; accusative masculine plural | those beginning with Visible Form: the six Condition Principles |
| dharma-saṃjñakaḥ | bahuvrīhi; nominative masculine singular | the one called Dharma: the Dharma Principle |
| sabhāgaḥ | sa-bhāga; nominative masculine singular | *sabhāga*: sharing in the work |
| tat-sabhāgāḥ | tatpuruṣa; nominative masculine plural | *tat-sabhāga*: of that kind, without the work |
| ca | particle | and: the rest are also *sabhāga* |
| śeṣāḥ | śeṣa; nominative masculine plural | the rest: the other seventeen |
| yaḥ | yad; nominative masculine singular | whichever |
| na | negative particle | not |
| sva-karma-kṛt | upapada compound; nominative masculine singular | doing its own work |

The one called Dharma is the Dharma Principle. Inner is not a self. It is
proximity to citta, and citta is designated self because it is the
support of the I-maker.

**Grammar tokens.** Verse-order IAST with sandhi opened (`dvādaśādhyātmikā`
→ *dvādaśa ādhyātmikāḥ*, `sabhāgas` → *sabhāgaḥ*, `tatsabhāgāś` →
*tat-sabhāgāḥ*, `śeṣā yo` → *śeṣāḥ yaḥ*) and compound boundaries marked.

```text
# tokens: dvādaśa ādhyātmikāḥ hitvā rūpa-ādīn dharma-saṃjñakaḥ sabhāgaḥ tat-sabhāgāḥ ca śeṣāḥ yaḥ na sva-karma-kṛt
```

## 4. Grammar

Two sentences. The first counts the inner by subtraction: the absolutive
*hitvā* sets aside an accusative class of six, and the numeral must match
the remainder of the eighteen, twelve. The second names the Dharma
Principle as *sabhāga* and makes "the rest" relative to it: the constant
introduced by *dharma-saṃjñakaḥ* is the one *śeṣāḥ* subtracts. The
relative clause *yaḥ na sva-karma-kṛt* gives the condition for
*tat-sabhāga*; *na* sets the clause's polarity to negative, so the
work predicate enters the second sentence negated for *tat-sabhāga*. *Ca*
adds the positive case: the rest are also *sabhāga* when they do the work.

```nltk-fcfg
% start S
# tokens: dvādaśa ādhyātmikāḥ hitvā rūpa-ādīn dharma-saṃjñakaḥ sabhāgaḥ tat-sabhāgāḥ ca śeṣāḥ yaḥ na sva-karma-kṛt
S[SEM=<(?a & ?b)>] -> INNER[SEM=?a] WORK[SEM=?b]
INNER[SEM=<all x.(AmongEighteen(x) -> (?in(x) <-> -?ex(x)))>] -> NUMR[CNT=?r] ADHY[NUM=pl,SEM=?in] HITVA EXCL[CASE=acc,NUM=pl,REST=?r,SEM=?ex]
WORK[SEM=<(all i.(InstanceOf(i,?d) -> Sabhaga(i)) & all x.((AmongEighteen(x) & -(x = ?d)) -> all i.(InstanceOf(i,x) -> ((-?w(i) -> TatSabhaga(i)) & (?w(i) -> Sabhaga(i))))))>] -> DHARMA[NUM=sg,SEM=?d] SAB[NUM=sg] TAT[NUM=pl] CA SESA[NUM=pl] REL[NUM=sg,POL=neg,SEM=?w]
REL[NUM=sg,POL=neg,SEM=?w] -> YAH[NUM=sg] NA SVAKARMA[NUM=sg,SEM=?w]
NUMR[CNT=12] -> 'dvādaśa'
ADHY[NUM=pl,SEM=<\x.Inner(x)>] -> 'ādhyātmikāḥ'
HITVA -> 'hitvā'
EXCL[CASE=acc,NUM=pl,REST=12,SEM=<\x.OuterPrinciple(x)>] -> 'rūpa-ādīn'
DHARMA[NUM=sg,SEM=<dharma_principle>] -> 'dharma-saṃjñakaḥ'
SAB[NUM=sg] -> 'sabhāgaḥ'
TAT[NUM=pl] -> 'tat-sabhāgāḥ'
CA -> 'ca'
SESA[NUM=pl] -> 'śeṣāḥ'
YAH[NUM=sg] -> 'yaḥ'
NA -> 'na'
SVAKARMA[NUM=sg,SEM=<\i.DoesOwnWork(i)>] -> 'sva-karma-kṛt'
```

```nltk-dep
'ādhyātmikāḥ' -> 'dvādaśa' | 'hitvā'
'hitvā' -> 'rūpa-ādīn'
'sabhāgaḥ' -> 'dharma-saṃjñakaḥ'
'tat-sabhāgāḥ' -> 'śeṣāḥ' | 'ca'
'śeṣāḥ' -> 'sva-karma-kṛt'
'sva-karma-kṛt' -> 'yaḥ' | 'na'
```

**Close construe.** Twelve are inner, having set aside those beginning
with Visible Form. The one called Dharma is *sabhāga*; and the rest are
*tat-sabhāga*, whichever does not do its own work.

*Sabhāga* and *tat-sabhāga* are said of instances, not of whole
Principles. The Dharma Principle has only *sabhāga* instances. The other
seventeen have both, divided by the work.

## 5. Translation

### Literal Translation

> Twelve are inner, having set aside those beginning with visible. The one
> called dharma is sabhāga. And the rest are tat-sabhāga, whichever does not
> do its own work.

### Bhāṣya-informed study translation

> Twelve Principles are internal, excluding the six beginning with Visible
> Form. The Dharma Principle is *sabhāga*; the others are *sabhāga* when
> performing their own function, and *tat-sabhāga* when they do not.

## 6. Philosophical Translation

Inner is not a self inside. Citta is called self because it supports the I-maker, and the twelve are inner because they are near that Basis: six Cognitions, six Bases. The six beginning with Visible Form are outer because they are Conditions. The Cognition Principles do not fall out of the twelve. When past they are the Mind Principle. The mark holds in all three times, or the Mind Principle would be past only.

Sabhāga is doing one's own work. The Dharma Principle always does it. The citta that all dharmas are without self takes them as Support, and the next moment takes that citta. Two moments cover them. The rest do the work or fail it. The eye that sees is sabhāga. The eye that ceases without having seen, or that will not arise, is tat-sabhāga. The Kāśmīras count four. The Westerners split the last and count five. Mind fails only by not being of a nature to arise.

The eye is uncommon. One eye is not the seeing of two. Visible Form is common. One moon is seen by many, and it is sabhāga for the seer and tat-sabhāga for the one who does not see. Odor seems uncommon because it is grasped on contact. It is common in possibility: the same Odor might have been another's cognition. The eye cannot be that.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| ādhyātmika | inner | near citta as support; not a self |
| bāhya | outer | the six Condition Principles, with the Dharma Principle |
| āśraya | Basis | the six with the Cognitions make twelve; distinct from *ālambana* (Support) |
| citta | citta | designated self as support of the I-maker |
| dharma-saṃjñaka | the one called dharma | the Dharma Principle; not an essence |
| sabhāga | sharing in the work | Faculty, Condition, and Cognition taking one another up; or contact as common result |
| tat-sabhāga | of that kind | the same kind, without the work |
| sva-karma-kṛt | does its own work | the sabhāga side |
| asādhāraṇa | uncommon | the eye, settled by one continuum |
| sādhāraṇa | common | Visible Form, settled by many |

## 8. Logical Determination

**Kārikā, derived.** Among the eighteen, the inner are exactly those not
among the six beginning with Visible Form; every instance of the Dharma
Principle is *sabhāga*; every instance of the rest is *tat-sabhāga* if it
does not do its own work, and *sabhāga* if it does.

```nltk-sem
# derived by the section 4 parse
(all x.(AmongEighteen(x) -> (Inner(x) <-> -OuterPrinciple(x))) & all i.(InstanceOf(i,dharma_principle) -> Sabhaga(i)) & all x.((AmongEighteen(x) & -(x = dharma_principle)) -> all i.(InstanceOf(i,x) -> ((-DoesOwnWork(i) -> TatSabhaga(i)) & (DoesOwnWork(i) -> Sabhaga(i))))))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all x.(AmongEighteen(x) -> (Inner(x) <-> -OuterPrinciple(x))) & all i.(InstanceOf(i,dharma_principle) -> Sabhaga(i)) & all x.((AmongEighteen(x) & -(x = dharma_principle)) -> all i.(InstanceOf(i,x) -> ((-DoesOwnWork(i) -> TatSabhaga(i)) & (DoesOwnWork(i) -> Sabhaga(i))))))
# THEORY prose
# EXPECT prose T
all x.(Inner(x) <-> (Basis(x) | CognitionPrinciple(x)))
all x.(Inner(x) <-> NearCittaAsBasis(x))
-exists s.Self(s)
exists c.(c = citta & DesignatedSelf(c) & SupportOfIMaker(c))
all x.(CognitionPrinciple(x) -> Inner(x))
exists m.(m = mind & MarkAcrossTimes(m))
all i.(InstanceOf(i,dharma_principle) -> DoesOwnWork(i))
all i.-(Sabhaga(i) & TatSabhaga(i))
all i.((InstanceOf(i,eye) & TatSabhaga(i)) -> (Ceased(i) | Ceasing(i) | AboutToCease(i) | NotToArise(i)))
exists v.(v = kasmira & KindCount(v,four_n)) & exists v.(v = western & Splits(v,not_to_arise))
all i.((InstanceOf(i,mind) & TatSabhaga(i)) -> NotToArise(i))
all i.all x.((InstanceOf(i,x) & -ConditionMeaning(x)) -> all p.all q.((Person(p) & Person(q)) -> (SabhagaFor(i,p) <-> SabhagaFor(i,q))))
exists i.(i = moon & InstanceOf(i,visible_form) & exists p.exists q.(SabhagaFor(i,p) & SabhagaFor(i,q) & -(p = q)) & exists r.(Person(r) & -SabhagaFor(i,r)))
all x.(ConditionMeaning(x) -> Common(x))
all x.(SenseFaculty(x) -> -Common(x))
exists x.(x = odor & ContactGrasped(x) & Common(x))
# THEORY rejected_inner_is_a_self
# EXPECT rejected_inner_is_a_self F
exists s.Self(s)
# THEORY rejected_cognitions_outer
# EXPECT rejected_cognitions_outer F
exists x.(CognitionPrinciple(x) & -Inner(x))
# THEORY rejected_dharma_tat_sabhaga
# EXPECT rejected_dharma_tat_sabhaga F
exists i.(InstanceOf(i,dharma_principle) & TatSabhaga(i))
# THEORY rejected_rest_always_sabhaga
# EXPECT rejected_rest_always_sabhaga F
all x.(AmongEighteen(x) -> all i.(InstanceOf(i,x) -> Sabhaga(i)))
# THEORY rejected_mind_fails_by_ceasing
# EXPECT rejected_mind_fails_by_ceasing F
exists i.(InstanceOf(i,mind) & TatSabhaga(i) & -NotToArise(i))
# THEORY rejected_eye_relative_to_seer
# EXPECT rejected_eye_relative_to_seer F
exists i.(InstanceOf(i,eye) & exists p.exists q.(SabhagaFor(i,p) & Person(q) & -SabhagaFor(i,q)))
# THEORY rejected_contact_grasped_uncommon
# EXPECT rejected_contact_grasped_uncommon F
exists x.(ContactGrasped(x) & -Common(x))
```

```nltk-valuation
dharma_principle => dharma_d
eye => caksur_d
mind => mano_d
visible_form => rupa_d
odor => gandha_d
moon => rupa_moon
citta => citta_c
self_designation => atma_prajnapti
kasmira => kasmira_v
western => pascatya_v
four_n => four_n
five_n => five_n
not_to_arise => anutpatti_k
AmongEighteen => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d,mano_d,dharma_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d}
SenseFaculty => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d}
Basis => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,mano_d}
CognitionPrinciple => {caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d}
ConditionMeaning => {rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d}
OuterPrinciple => {rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d,dharma_d}
Inner => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,mano_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d}
NearCittaAsBasis => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,mano_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d}
Self => {}
DesignatedSelf => {citta_c}
SupportOfIMaker => {citta_c}
MarkAcrossTimes => {mano_d}
InstanceOf => {(caksur_seen,caksur_d),(caksur_ceased,caksur_d),(caksur_ceasing,caksur_d),(caksur_about,caksur_d),(caksur_anutp,caksur_d),(srotra_seen,srotra_d),(srotra_ceased,srotra_d),(srotra_ceasing,srotra_d),(srotra_about,srotra_d),(srotra_anutp,srotra_d),(ghrana_seen,ghrana_d),(ghrana_ceased,ghrana_d),(ghrana_ceasing,ghrana_d),(ghrana_about,ghrana_d),(ghrana_anutp,ghrana_d),(jihva_seen,jihva_d),(jihva_ceased,jihva_d),(jihva_ceasing,jihva_d),(jihva_about,jihva_d),(jihva_anutp,jihva_d),(kaya_seen,kaya_d),(kaya_ceased,kaya_d),(kaya_ceasing,kaya_d),(kaya_about,kaya_d),(kaya_anutp,kaya_d),(mano_work,mano_d),(mano_anutp,mano_d),(caksurvijnana_work,caksurvijnana_d),(caksurvijnana_anutp,caksurvijnana_d),(srotravijnana_work,srotravijnana_d),(srotravijnana_anutp,srotravijnana_d),(ghranavijnana_work,ghranavijnana_d),(ghranavijnana_anutp,ghranavijnana_d),(jihvavijnana_work,jihvavijnana_d),(jihvavijnana_anutp,jihvavijnana_d),(kayavijnana_work,kayavijnana_d),(kayavijnana_anutp,kayavijnana_d),(manovijnana_work,manovijnana_d),(manovijnana_anutp,manovijnana_d),(rupa_moon,rupa_d),(rupa_unseen,rupa_d),(sabda_work,sabda_d),(sabda_unseen,sabda_d),(gandha_work,gandha_d),(gandha_unseen,gandha_d),(rasa_work,rasa_d),(rasa_unseen,rasa_d),(sprastavya_work,sprastavya_d),(sprastavya_unseen,sprastavya_d),(dharma_i,dharma_d),(dharma_asamskrta,dharma_d)}
DoesOwnWork => {caksur_seen,srotra_seen,ghrana_seen,jihva_seen,kaya_seen,mano_work,caksurvijnana_work,srotravijnana_work,ghranavijnana_work,jihvavijnana_work,kayavijnana_work,manovijnana_work,rupa_moon,sabda_work,gandha_work,rasa_work,sprastavya_work,dharma_i,dharma_asamskrta}
Sabhaga => {caksur_seen,srotra_seen,ghrana_seen,jihva_seen,kaya_seen,mano_work,caksurvijnana_work,srotravijnana_work,ghranavijnana_work,jihvavijnana_work,kayavijnana_work,manovijnana_work,rupa_moon,sabda_work,gandha_work,rasa_work,sprastavya_work,dharma_i,dharma_asamskrta}
TatSabhaga => {caksur_ceased,caksur_ceasing,caksur_about,caksur_anutp,srotra_ceased,srotra_ceasing,srotra_about,srotra_anutp,ghrana_ceased,ghrana_ceasing,ghrana_about,ghrana_anutp,jihva_ceased,jihva_ceasing,jihva_about,jihva_anutp,kaya_ceased,kaya_ceasing,kaya_about,kaya_anutp,mano_anutp,caksurvijnana_anutp,srotravijnana_anutp,ghranavijnana_anutp,jihvavijnana_anutp,kayavijnana_anutp,manovijnana_anutp,rupa_unseen,sabda_unseen,gandha_unseen,rasa_unseen,sprastavya_unseen}
NotToArise => {caksur_anutp,srotra_anutp,ghrana_anutp,jihva_anutp,kaya_anutp,mano_anutp,caksurvijnana_anutp,srotravijnana_anutp,ghranavijnana_anutp,jihvavijnana_anutp,kayavijnana_anutp,manovijnana_anutp}
Ceased => {caksur_ceased,srotra_ceased,ghrana_ceased,jihva_ceased,kaya_ceased}
Ceasing => {caksur_ceasing,srotra_ceasing,ghrana_ceasing,jihva_ceasing,kaya_ceasing}
AboutToCease => {caksur_about,srotra_about,ghrana_about,jihva_about,kaya_about}
Person => {p1,p2,p3}
SabhagaFor => {(caksur_seen,p1),(caksur_seen,p2),(caksur_seen,p3),(srotra_seen,p1),(srotra_seen,p2),(srotra_seen,p3),(ghrana_seen,p1),(ghrana_seen,p2),(ghrana_seen,p3),(jihva_seen,p1),(jihva_seen,p2),(jihva_seen,p3),(kaya_seen,p1),(kaya_seen,p2),(kaya_seen,p3),(mano_work,p1),(mano_work,p2),(mano_work,p3),(caksurvijnana_work,p1),(caksurvijnana_work,p2),(caksurvijnana_work,p3),(srotravijnana_work,p1),(srotravijnana_work,p2),(srotravijnana_work,p3),(ghranavijnana_work,p1),(ghranavijnana_work,p2),(ghranavijnana_work,p3),(jihvavijnana_work,p1),(jihvavijnana_work,p2),(jihvavijnana_work,p3),(kayavijnana_work,p1),(kayavijnana_work,p2),(kayavijnana_work,p3),(manovijnana_work,p1),(manovijnana_work,p2),(manovijnana_work,p3),(rupa_moon,p1),(rupa_moon,p2),(sabda_work,p1),(gandha_work,p1),(rasa_work,p1),(sprastavya_work,p1),(dharma_i,p1),(dharma_i,p2),(dharma_i,p3),(dharma_asamskrta,p1),(dharma_asamskrta,p2),(dharma_asamskrta,p3)}
Common => {rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d}
ContactGrasped => {gandha_d,rasa_d,sprastavya_d}
KindCount => {(kasmira_v,four_n),(pascatya_v,five_n)}
Splits => {(pascatya_v,anutpatti_k)}
```

**Model checks.** The verse formula holds. The prose makes the inner the
six Bases and six Cognitions, near citta as Basis, with no self; the
Cognitions stay inner by the mark across the times. Every Dharma instance
does its work. The eye's failures are the Kāśmīra four; mind fails only
by not being of a nature to arise. The eye is *sabhāga* for all or none;
the moon is *sabhāga* for two seers and not for a third. All seven
rejected theories are false.

**Bhāṣya determination.** *Ahaṃkāra-sanniśrayatvāc cittam ātmeti
prajñapyate*: citta is designated self as support of the I-maker. *Dvābhyāṃ
kṣaṇābhyāṃ sarve dharmā ālambanībhavanti*: in two moments all dharmas are
Support, so the Dharma Principle is always *sabhāga*. *Bhāga* is the
mutual taking-up of Faculty, Condition, and Cognition, or contact as
their common result.

**Organon interpretation.** *Sabhāga* is the Principle at work in the
triad of Faculty, Condition, and Cognition. *Tat-sabhāga* is the same
kind with the triad not completed. Uncommon and common divide the triad:
the Faculty is one continuum's, the Condition many.

```text
twelve inner
    six cognitions
    six Bases

six outer
    beginning with Visible Form

Dharma Principle
    always sabhāga

the rest
    sabhāga if the work is done
    tat-sabhāga if not

eye
    uncommon
    one continuum

Visible Form
    common
    many continua
    sabhāga for the seer
    tat-sabhāga for the one who does not see

Odor and the rest
    contact-grasped
    common in possibility

1.40 not opened
```

## 9. Interpretive Note

**Key-term evidence.** *Āśraya* (Basis) enters as the six Bases that, with the six Cognitions, make the inner twelve; *ālambana* (Support) as what the Dharma Principle always is for mind-cognition. The definition of *bhāga* names the triad that 1.38 left implicit: Faculty, Condition, and Cognition taking one another up, with contact as their common result (3.30, *saṃnipāta-ja*).

**Translation note.** The twelve internal Principles are the six Bases and their six Cognitions. The Dharma Principle is always *sabhāga*; the other Principles are *sabhāga* when exercising their own function and *tat-sabhāga* when not.

The hinge is the work. Inner is proximity, not a self. Sabhāga is not a second Principle. It is the Principle doing what it is for. Tat-sabhāga is the same kind when the work is not done. The Dharma Principle does not have that failure.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_39 a vak:Karika ;
    vak:hasTopic vak:InnerTwelveAndTheWork ;
    vak:belongsTo vak:Dhatunirdesa .

vak:TwelvePrinciples vak:inner true .
vak:DharmaPrinciple vak:alwaysSabhaga true .
vak:EyePrinciple vak:uncommon true .
vak:VisiblePrinciple vak:common true .
```
