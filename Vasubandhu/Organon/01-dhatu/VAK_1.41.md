# VAK_1.41 — Two Portions Are View

## 1. Sanskrit (Devanāgarī)

```sanskrit
चक्षुश्च धर्मधातोश्च प्रदेशौ दृष्टिरष्टधा ।
पञ्चविज्ञानसहजा धीर्न दृष्टिरतीरणात् ॥ १.४१ ॥
```

## 2. Sanskrit (IAST)

```text
cakṣuś ca dharmadhātoś ca pradeśau dṛṣṭir aṣṭadhā /
pañcavijñānasahajā dhīr na dṛṣṭir atīraṇāt // 1.41 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| cakṣuḥ | cakṣus; nominative neuter singular | the eye: the whole Eye Principle |
| ca | particle | and |
| dharma-dhātoḥ | tatpuruṣa; genitive masculine singular | of the Dharma Principle: partitive |
| ca | particle | and |
| pradeśau | pradeśa; nominative masculine dual | two portions: of the eighteen |
| dṛṣṭiḥ | dṛṣṭi; nominative feminine singular | view |
| aṣṭadhā | adverb | eightfold: said of the Dharma Principle portion |
| pañca-vijñāna-sahajā | upapada compound; nominative feminine singular | born with the five sensory Cognitions |
| *dhīḥ* | dhī; nominative feminine singular | *prajñā* (Science of Principles), discriminative comprehension |
| na | negative particle | not |
| dṛṣṭiḥ | dṛṣṭi; nominative feminine singular | view |
| a-tīraṇāt | a-tīraṇa; ablative singular | because of not ascertaining: the ablative of ground |

*Cakṣuḥ* is nominative, not genitive. The eye is one of the two portions
of the eighteen as a whole Principle; only the Dharma Principle is divided.

**Grammar tokens.** Verse-order IAST with sandhi opened (`cakṣuś` →
*cakṣuḥ*, `dharmadhātoś` → *dharma-dhātoḥ*, `dṛṣṭir` → *dṛṣṭiḥ*, `dhīr` →
*dhīḥ*) and compound boundaries marked.

```text
# tokens: cakṣuḥ ca dharma-dhātoḥ ca pradeśau dṛṣṭiḥ aṣṭadhā pañca-vijñāna-sahajā dhīḥ na dṛṣṭiḥ a-tīraṇāt
```

## 4. Grammar

Two sentences. In the first, *ca … ca* joins two members, and the dual
*pradeśau* requires exactly two. Case carries the quantity. The nominative
*cakṣuḥ* gives the whole Principle: every instance of the eye is view. The
genitive *dharma-dhātoḥ* is partitive: some instances of the Dharma
Principle are view and some are not. The dual also closes the class:
nothing outside the two portions is view. *Aṣṭadhā* divides the Dharma
portion into eight kinds.

In the second sentence, *sahajā* and the two *dṛṣṭiḥ* agree with *dhīḥ* as
feminine singulars. The ablative *a-tīraṇāt* gives the ground: discriminative
comprehension born with the five does not ascertain, and so it is not view.

```nltk-fcfg
% start S
# tokens: cakṣuḥ ca dharma-dhātoḥ ca pradeśau dṛṣṭiḥ aṣṭadhā pañca-vijñāna-sahajā dhīḥ na dṛṣṭiḥ a-tīraṇāt
S[SEM=<(?a & ?b)>] -> VIEW[SEM=?a] NOTV[SEM=?b]
VIEW[SEM=<(?q1(\i.View(i)) & ?q2(\i.View(i)) & all i.((InstanceOf(i,?r2) & View(i)) -> ?k(i)) & all x.all i.((InstanceOf(i,x) & View(i)) -> ((x = ?r1) | (x = ?r2))))>] -> NP[CASE=nom,REF=?r1,SEM=?q1] CA NP[CASE=gen,REF=?r2,SEM=?q2] CA PRADESA[NUM=du] DRSTI[GEN=f,NUM=sg] ADV[CNT=8,SEM=?k]
NOTV[SEM=<all i.((?s(i) & ?p(i)) -> (?w(i) & -View(i)))>] -> SAHAJA[GEN=?g,NUM=?n,SEM=?s] DHI[GEN=?g,NUM=?n,SEM=?p] NA DRSTI[GEN=?g,NUM=?n] ABL[SEM=?w]
NP[CASE=nom,REF=<eye>,SEM=<\P.all i.(InstanceOf(i,eye) -> P(i))>] -> 'cakṣuḥ'
NP[CASE=gen,REF=<dharma_principle>,SEM=<\P.(exists i.(InstanceOf(i,dharma_principle) & P(i)) & exists i.(InstanceOf(i,dharma_principle) & -P(i)))>] -> 'dharma-dhātoḥ'
CA -> 'ca'
PRADESA[NUM=du] -> 'pradeśau'
DRSTI[GEN=f,NUM=sg] -> 'dṛṣṭiḥ'
ADV[CNT=8,SEM=<\i.exists k.(EightKind(k) & ViewKind(i,k))>] -> 'aṣṭadhā'
SAHAJA[GEN=f,NUM=sg,SEM=<\i.BornWithFive(i)>] -> 'pañca-vijñāna-sahajā'
DHI[GEN=f,NUM=sg,SEM=<\i.Prajna(i)>] -> 'dhīḥ'
NA -> 'na'
ABL[SEM=<\i.-Ascertains(i)>] -> 'a-tīraṇāt'
```

```nltk-dep
'dṛṣṭiḥ' -> 'pradeśau' | 'aṣṭadhā' | 'dhīḥ' | 'na' | 'a-tīraṇāt'
'pradeśau' -> 'cakṣuḥ' | 'dharma-dhātoḥ'
'cakṣuḥ' -> 'ca'
'dharma-dhātoḥ' -> 'ca'
'dhīḥ' -> 'pañca-vijñāna-sahajā'
```

**Close construe.** The eye, and of the Dharma Principle a part: these two
portions are view, eightfold. Discriminative comprehension born with the
five is not view, because it does not ascertain.

The eye and the ascertaining discriminative comprehension are view in two
senses: disclosure and examination. The grammar gives one predicate; the
Bhāṣya separates the senses.

## 5. Translation

### Literal Translation

> The eye and a portion of the Dharma Principle, two portions, are view,
> eightfold. Discriminative comprehension born with the five Cognitions is
> not view, because it does not ascertain.

### Bhāṣya-informed study translation

> The Eye Principle and an eightfold portion of the Dharma Principle, two
> portions of the eighteen, are view. The discriminative comprehension
> arising with the five sensory Cognitions is not view, because it does not
> ascertain.

## 6. Philosophical Translation

View is not the eighteen, and it is not the whole Dharma Principle. Two portions. The eye is one, whole, and it is view by disclosure, not by ascertainment. The other is eightfold discriminative comprehension in the Dharma Principle: five views beginning with the view of a real body, worldly right view, the trainee's view, the adept's view. The remainder of that Principle is not view.

Worldly right view is wholesome and Impure, and it is associated with Mind-Cognition only. Discriminative comprehension born with the five Cognitions does not ascertain. View proceeds by attentive examination. That discriminative comprehension does not. Other discriminative comprehension, afflicted or unafflicted, fails for the same reason. The cloud and the night do not stop the seeing of Visible Form. Afflicted and unafflicted, trainee and adept, are ways of seeing dharmas, not a second Principle.

The sentence that the eye sees Visible Form opens the next dispute. It is not settled here.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| pradeśa | portion | of the eighteen: the whole eye, and part of the Dharma Principle |
| dṛṣṭi | view | eightfold in the Dharma Principle; disclosure in the eye |
| satkāya-dṛṣṭi | view of a real body | first of the five; explained later |
| laukikī samyag-dṛṣṭi | worldly right view | wholesome Impure discriminative comprehension with Mind-Cognition |
| śaikṣī | the trainee's view | Pure |
| aśaikṣī | the adept's view | Pure |
| dhī | discriminative comprehension | *prajñā* |
| atīraṇa | non-ascertainment | why the fivefold discriminative comprehension is not view |
| santīrikā | ascertaining | view proceeds by attentive examination |
| rūpālocana | disclosure of Visible Form | why the eye is view |

## 8. Logical Determination

**Kārikā, derived.**
- Every instance of the eye is view.
- Some instances of the Dharma Principle are view and some are not, and its view instances fall under the eight kinds.
- No instance of any other Principle is view.
- Discriminative comprehension born with the five does not ascertain and is not view.

```nltk-sem
# derived by the section 4 parse
(all i.(InstanceOf(i,eye) -> View(i)) & exists i.(InstanceOf(i,dharma_principle) & View(i)) & exists i.(InstanceOf(i,dharma_principle) & -View(i)) & all i.((InstanceOf(i,dharma_principle) & View(i)) -> exists k.(EightKind(k) & ViewKind(i,k))) & all x i.((InstanceOf(i,x) & View(i)) -> ((x = eye) | (x = dharma_principle))) & all i.((BornWithFive(i) & Prajna(i)) -> (-Ascertains(i) & -View(i))))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all i.(InstanceOf(i,eye) -> View(i)) & exists i.(InstanceOf(i,dharma_principle) & View(i)) & exists i.(InstanceOf(i,dharma_principle) & -View(i)) & all i.((InstanceOf(i,dharma_principle) & View(i)) -> exists k.(EightKind(k) & ViewKind(i,k))) & all x i.((InstanceOf(i,x) & View(i)) -> ((x = eye) | (x = dharma_principle))) & all i.((BornWithFive(i) & Prajna(i)) -> (-Ascertains(i) & -View(i))))
# THEORY prose
# EXPECT prose T
all i.(InstanceOf(i,eye) -> (Discloses(i) & -Ascertains(i)))
all i.((InstanceOf(i,dharma_principle) & View(i)) -> Prajna(i))
all i.(Prajna(i) -> (View(i) <-> Ascertains(i)))
all i.((Prajna(i) & View(i)) -> AssociatedWith(i,mind_cognition))
exists w.(w = worldly_right_view & View(w) & Wholesome(w) & Impure(w))
exists t.(t = trainee_view & View(t) & Pure(t))
exists a.(a = adept_view & View(a) & Pure(a))
all i.((ViewKind(i,satkaya) | ViewKind(i,antagraha) | ViewKind(i,mithya) | ViewKind(i,drstiparamarsa) | ViewKind(i,silavrataparamarsa)) -> Afflicted(i))
exists o.(o = other_prajna & Prajna(o) & InstanceOf(o,dharma_principle) & -Ascertains(o) & -View(o))
exists v.(v = feeling & InstanceOf(v,dharma_principle) & -View(v))
# THEORY rejected_whole_dharma_principle_is_view
# EXPECT rejected_whole_dharma_principle_is_view F
all i.(InstanceOf(i,dharma_principle) -> View(i))
# THEORY rejected_only_part_of_eye
# EXPECT rejected_only_part_of_eye F
exists i.(InstanceOf(i,eye) & -View(i))
# THEORY rejected_eye_ascertains
# EXPECT rejected_eye_ascertains F
exists i.(InstanceOf(i,eye) & Ascertains(i))
# THEORY rejected_view_always_ascertains
# EXPECT rejected_view_always_ascertains F
all i.(View(i) -> Ascertains(i))
# THEORY rejected_five_born_prajna_is_view
# EXPECT rejected_five_born_prajna_is_view F
exists i.(Prajna(i) & BornWithFive(i) & View(i))
# THEORY rejected_mind_cognition_is_view
# EXPECT rejected_mind_cognition_is_view F
exists i.(InstanceOf(i,mind_cognition) & View(i))
# THEORY rejected_worldly_right_view_pure
# EXPECT rejected_worldly_right_view_pure F
exists w.(w = worldly_right_view & Pure(w))
```

```nltk-valuation
eye => caksur_d
dharma_principle => dharma_d
mind_cognition => manovijnana_d
worldly_right_view => laukika_vi
trainee_view => saiksa_vi
adept_view => asaiksa_vi
other_prajna => other_prajna_i
feeling => vedana_i
satkaya => satkaya_k
antagraha => antagraha_k
mithya => mithya_k
drstiparamarsa => drstiparamarsa_k
silavrataparamarsa => silavrataparamarsa_k
InstanceOf => {(srotra_i,srotra_d),(ghrana_i,ghrana_d),(jihva_i,jihva_d),(kaya_i,kaya_d),(rupa_i,rupa_d),(sabda_i,sabda_d),(gandha_i,gandha_d),(rasa_i,rasa_d),(sprastavya_i,sprastavya_d),(mano_i,mano_d),(caksurvijnana_i,caksurvijnana_d),(srotravijnana_i,srotravijnana_d),(ghranavijnana_i,ghranavijnana_d),(jihvavijnana_i,jihvavijnana_d),(kayavijnana_i,kayavijnana_d),(manovijnana_i,manovijnana_d),(caksur_seen_i,caksur_d),(caksur_tat_i,caksur_d),(satkaya_vi,dharma_d),(antagraha_vi,dharma_d),(mithya_vi,dharma_d),(drstiparamarsa_vi,dharma_d),(silavrataparamarsa_vi,dharma_d),(laukika_vi,dharma_d),(saiksa_vi,dharma_d),(asaiksa_vi,dharma_d),(other_prajna_i,dharma_d),(five_prajna_i,dharma_d),(vedana_i,dharma_d)}
View => {caksur_seen_i,caksur_tat_i,satkaya_vi,antagraha_vi,mithya_vi,drstiparamarsa_vi,silavrataparamarsa_vi,laukika_vi,saiksa_vi,asaiksa_vi}
Discloses => {caksur_seen_i,caksur_tat_i}
Ascertains => {satkaya_vi,antagraha_vi,mithya_vi,drstiparamarsa_vi,silavrataparamarsa_vi,laukika_vi,saiksa_vi,asaiksa_vi}
Prajna => {satkaya_vi,antagraha_vi,mithya_vi,drstiparamarsa_vi,silavrataparamarsa_vi,laukika_vi,saiksa_vi,asaiksa_vi,other_prajna_i,five_prajna_i}
BornWithFive => {five_prajna_i}
EightKind => {satkaya_k,antagraha_k,mithya_k,drstiparamarsa_k,silavrataparamarsa_k,laukika_k,saiksa_k,asaiksa_k}
ViewKind => {(satkaya_vi,satkaya_k),(antagraha_vi,antagraha_k),(mithya_vi,mithya_k),(drstiparamarsa_vi,drstiparamarsa_k),(silavrataparamarsa_vi,silavrataparamarsa_k),(laukika_vi,laukika_k),(saiksa_vi,saiksa_k),(asaiksa_vi,asaiksa_k)}
AssociatedWith => {(satkaya_vi,manovijnana_d),(antagraha_vi,manovijnana_d),(mithya_vi,manovijnana_d),(drstiparamarsa_vi,manovijnana_d),(silavrataparamarsa_vi,manovijnana_d),(laukika_vi,manovijnana_d),(saiksa_vi,manovijnana_d),(asaiksa_vi,manovijnana_d)}
Wholesome => {laukika_vi}
Impure => {satkaya_vi,antagraha_vi,mithya_vi,drstiparamarsa_vi,silavrataparamarsa_vi,laukika_vi}
Pure => {saiksa_vi,asaiksa_vi}
Afflicted => {satkaya_vi,antagraha_vi,mithya_vi,drstiparamarsa_vi,silavrataparamarsa_vi}
```

**Model checks.** The verse formula holds.
- Every eye instance discloses and none ascertains.
- The view instances of the Dharma Principle are discriminative comprehension, and for discriminative comprehension view is exactly ascertaining.
- Every view of that kind is associated with Mind-Cognition, because the five-born kind does not ascertain.
- Worldly right view is wholesome and Impure. The trainee's and the adept's views are Pure. The five beginning with *satkāya-dṛṣṭi* are afflicted.
- Feeling, and discriminative comprehension that does not ascertain, stay in the non-view part of the Dharma Principle.
- All seven rejected theories are false.

**Bhāṣya determination.**
- *Santīrikā hi dṛṣṭir upādhyāna-pravṛttatvāt*: view ascertains, because it proceeds by attentive examination.
- *Laukikī punaḥ samyag-dṛṣṭir mano-vijñāna-saṃprayuktā kuśalā sāsravā prajñā*: worldly right view is wholesome, Impure discriminative comprehension associated with Mind-Cognition.
- *Rūpālocanārthena*: the eye is view by disclosing Visible Form.

**Organon interpretation.** View has two senses, and the verse gives each a portion:
- The eye discloses without judging: a whole Principle at the threshold of access.
- Discriminative comprehension judges: a portion of the Dharma Principle, and only where it ascertains.

The view instances are not Mind-Cognition itself; they are associated with it. Judgment belongs to a mental factor, not to Cognition.

```text
view
    the eye, whole
    an eightfold portion of the Dharma Principle

eight
    five beginning with satkāya-dṛṣṭi
    worldly right view
    trainee
    adept

not view
    the remainder of the Dharma Principle
    discriminative comprehension born with the five Cognitions
    other discriminative comprehension that does not ascertain

eye
    view by disclosure
    the next dispute not opened

1.42 not opened
```

## 9. Interpretive Note

**Key-term evidence.** The ablative *a-tīraṇāt* is the grammatical case of ground (*hetau pañcamī*): the verse gives its own reason. The Ground here is a privation: not ascertaining. The privation alone removes the five-born discriminative comprehension from view, without any appeal to its Condition.

**Translation note.** *Cakṣuḥ* is nominative and *dharma-dhātoḥ* genitive. The earlier rendering “a portion of the eye” read the genitive into both members. The eye is a whole Principle among the two portions; only the Dharma Principle is divided.

The hinge is ascertainment. View examines. Discriminative comprehension born with the five Cognitions does not, so it is not view. The eye does not examine either. It is view by another sense: it discloses Visible Form. That second sense is what the next verse disputes.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_41 a vak:Karika ;
    vak:hasTopic vak:TwoPortionsAreView ;
    vak:belongsTo vak:Dhatunirdesa .

vak:EyePrinciple vak:viewBy vak:Disclosure .
vak:DharmaPrinciplePortion vak:viewEightfold true .
vak:PrajnaWithFiveCognitions vak:view false ;
    vak:reason vak:NonAscertainment .
```
