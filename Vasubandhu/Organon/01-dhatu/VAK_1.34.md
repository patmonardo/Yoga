# VAK_1.34 — Taking a Support, and Appropriated

## 1. Sanskrit (Devanāgarī)

```sanskrit
सप्त सालम्बनाश्चित्तधातवोऽर्धं च धर्मतः ।
नवानुपात्तास्ते चाष्टौ शब्दश्चान्ये नव द्विधा ॥ १.३४ ॥
```

## 2. Sanskrit (IAST)

```text
sapta sālambanāś cittadhātavo 'rdhaṃ ca dharmataḥ /
navānupāttās te cāṣṭau śabdaś cānye nava dvidhā // 1.34 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| sapta | numeral, nominative | seven: the count of the consciousness Principles |
| sālambanāḥ | sa-ālambana, bahuvrīhi; nominative masculine plural | having a Support: they grasp a Condition |
| citta-dhātavaḥ | tatpuruṣa; nominative masculine plural | the consciousness Principles: the six Cognition Principles and the Mind Principle |
| ardham | neuter accusative/nominative singular | a half |
| ca | particle | and |
| dharmataḥ | dharma + -tas; ablatival adverb | with respect to the Dharma Principle |
| nava | numeral | nine |
| anupāttāḥ | an-upātta; nominative plural | Unappropriated: never taken up as a basis |
| te | tad; nominative plural | those: resumes the first count |
| aṣṭau | numeral | eight: the seven and the Dharma Principle as eighth |
| śabdaḥ | nominative masculine singular | Sound |
| anye | anya; nominative plural | the others: the rest of the eighteen |
| dvidhā | adverb of manner | twofold: Appropriated and Unappropriated |

The half is the associated portion. The eight of the second count are the
seven plus the whole Dharma Principle. The scope changes: the first count
runs over portions, the second over Principles.

**Grammar tokens.** Verse-order IAST with sandhi opened (`sālambanāś` →
*sālambanāḥ*, `cittadhātavo 'rdhaṃ` → *citta-dhātavaḥ ardham*,
`navānupāttās` → *nava anupāttāḥ*, `cāṣṭau` → *ca aṣṭau*, `śabdaś cānye`
→ *śabdaḥ ca anye*) and the compound boundary marked. *Ca* occurs three
times; *nava* twice.

```text
# tokens: sapta sālambanāḥ citta-dhātavaḥ ardham ca dharmataḥ nava anupāttāḥ te ca aṣṭau śabdaḥ ca anye nava dvidhā
```

## 4. Grammar

Two cuts, one constituent each. The Support cut predicates *sālambanāḥ* of
the seven, with the numeral agreeing in count with the class, and adds a
half of the Dharma Principle. The Appropriation cut counts nine
Unappropriated as a list, eight resumed by *te* and Sound, and gives the
other nine, the complement in the eighteen, as twofold. The count feature
`CNT` checks the arithmetic: 7 for the consciousness Principles, 8 + 1 = 9
for the list, and 9 again for the others.

```nltk-fcfg
% start S
# tokens: sapta sālambanāḥ citta-dhātavaḥ ardham ca dharmataḥ nava anupāttāḥ te ca aṣṭau śabdaḥ ca anye nava dvidhā
S[SEM=<(?a & ?b)>] -> SUPPORTCUT[SEM=?a] APPROPCUT[SEM=?b]
SUPPORTCUT[SEM=<(all x.(?c(x) -> ?s(x)) & exists h.(PortionOf(h,?d) & ?s(h)))>] -> NUMR[CNT=?k] SAL[CASE=nom,NUM=pl,SEM=?s] CITTA[CASE=nom,NUM=pl,CNT=?k,SEM=?c] HALF CA ABLT[SEM=?d]
APPROPCUT[SEM=<(all x.(?n(x) -> all i.(InstanceOf(i,x) -> -Appropriated(i))) & all x.((AmongEighteen(x) & -?n(x)) -> ?tw(x)))>] -> NUMR[CNT=?k] ANUP[CASE=nom,NUM=pl] LIST[CNT=?k,SEM=?n] ANYE NUMR[CNT=?k] DVIDHA[SEM=?tw]
LIST[CNT=9,SEM=<\x.(?e(x) | ?w(x))>] -> TE CA EIGHT[CNT=8,SEM=?e] SABDA[CNT=1,SEM=?w] CA
NUMR[CNT=7] -> 'sapta'
NUMR[CNT=9] -> 'nava'
SAL[CASE=nom,NUM=pl,SEM=<\x.TakesSupport(x)>] -> 'sālambanāḥ'
CITTA[CASE=nom,NUM=pl,CNT=7,SEM=<\x.CittaPrinciple(x)>] -> 'citta-dhātavaḥ'
HALF -> 'ardham'
CA -> 'ca'
ABLT[SEM=<dharma_principle>] -> 'dharmataḥ'
ANUP[CASE=nom,NUM=pl] -> 'anupāttāḥ'
TE -> 'te'
EIGHT[CNT=8,SEM=<\x.(CittaPrinciple(x) | (x = dharma_principle))>] -> 'aṣṭau'
SABDA[CNT=1,SEM=<\x.(x = sound)>] -> 'śabdaḥ'
ANYE -> 'anye'
DVIDHA[SEM=<\x.(exists i.(InstanceOf(i,x) & Appropriated(i)) & exists i.(InstanceOf(i,x) & -Appropriated(i)))>] -> 'dvidhā'
```

```nltk-dep
'sālambanāḥ' -> 'citta-dhātavaḥ' | 'ardham'
'citta-dhātavaḥ' -> 'sapta'
'ardham' -> 'dharmataḥ' | 'ca'
'anupāttāḥ' -> 'nava' | 'te' | 'śabdaḥ'
'te' -> 'aṣṭau' | 'ca'
'śabdaḥ' -> 'ca'
'dvidhā' -> 'anye'
'anye' -> 'nava'
```

**Close construe.** Seven consciousness Principles have a Support, and a
half with respect to the Dharma Principle. Nine are Unappropriated: those
eight, and Sound. The other nine are twofold.

The first cut quantifies over the consciousness Principles and asserts
only that some portion of the Dharma Principle has a Support; which
portion, the verse leaves to the Bhāṣya. The anaphor *te … aṣṭau* is
resolved in the lexicon by the Bhāṣya's own naming: the seven and the
whole Dharma Principle. Unappropriated is said of every instance;
twofold means some instance is Appropriated and some is not.

## 5. Translation

### Literal Translation

> Seven consciousness Principles have a Support, and a half with respect to
> the Dharma Principle. Nine are Unappropriated: those eight, and Sound. The
> other nine are twofold.

### Bhāṣya-informed study translation

> Seven consciousness Principles and the mental-factor portion of the Dharma
> Principle take a Support. Nine are Unappropriated: those eight and Sound.
> The other nine are twofold.

## 6. Philosophical Translation

Taking a Support is the seven, and the associated half of the Dharma Principle. The ten whose nature is Form do not take a Support. Neither does the unassociated half.

Appropriation is a different cut. The nine that never are appropriated are the seven, the whole Dharma Principle, and Sound. The other nine are Appropriated only when present and, for the four meanings, only when not separate from the Faculty. Appropriated is the basis citta has taken up. Benefit and injury run both ways. That is what is called animate.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| sālambana | taking a Support | glossed *viṣaya-grahaṇa*, grasping a Condition |
| anālambana | not taking a Support | the ten of Form, and the unassociated half |
| viṣaya | Condition | what is grasped (1.29) |
| citta-dhātu | consciousness Principle | the six Cognition Principles and the Mind Principle |
| ardham dharmataḥ | a half of the Dharma Principle | the associated mental factors |
| anupātta | Unappropriated | nine, in every instance |
| upātta | Appropriated | a present Faculty, or a present meaning not separate from it |
| adhiṣṭhāna | basis | what citta and the mental factors take up |
| śabda | Sound | among the nine always Unappropriated |
| sacetana | animate | the world's name for Appropriated |

## 8. Logical Determination

**Kārikā, derived.** Every consciousness Principle takes a Support, and
some portion of the Dharma Principle does; every instance of the seven,
the Dharma Principle, and Sound is Unappropriated; each other Principle
among the eighteen has Appropriated and Unappropriated instances.

```nltk-sem
# derived by the section 4 parse
(all x.(CittaPrinciple(x) -> TakesSupport(x)) & exists h.(PortionOf(h,dharma_principle) & TakesSupport(h)) & all x.((CittaPrinciple(x) | (x = dharma_principle) | (x = sound)) -> all i.(InstanceOf(i,x) -> -Appropriated(i))) & all x.((AmongEighteen(x) & -(CittaPrinciple(x) | (x = dharma_principle) | (x = sound))) -> (exists i.(InstanceOf(i,x) & Appropriated(i)) & exists i.(InstanceOf(i,x) & -Appropriated(i)))))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all x.(CittaPrinciple(x) -> TakesSupport(x)) & exists h.(PortionOf(h,dharma_principle) & TakesSupport(h)) & all x.((CittaPrinciple(x) | (x = dharma_principle) | (x = sound)) -> all i.(InstanceOf(i,x) -> -Appropriated(i))) & all x.((AmongEighteen(x) & -(CittaPrinciple(x) | (x = dharma_principle) | (x = sound))) -> (exists i.(InstanceOf(i,x) & Appropriated(i)) & exists i.(InstanceOf(i,x) & -Appropriated(i)))))
# THEORY prose
# EXPECT prose T
all x.(Item(x) -> (TakesSupport(x) <-> (CittaPrinciple(x) | (x = dharma_associated))))
all x.(TakesSupport(x) <-> GraspsCondition(x))
all x.((AmongEighteen(x) & FormBearing(x)) -> -TakesSupport(x))
exists x.(x = dharma_nonassociated & PortionOf(x,dharma_principle) & -TakesSupport(x))
exists x.(x = dharma_principle & AmongEighteen(x) & -Item(x))
all x.(FourMeaning(x) <-> (ConditionMeaning(x) & -(x = sound)))
all i.all x.((InstanceOf(i,x) & SenseFaculty(x)) -> (Appropriated(i) <-> Present(i)))
all i.all x.((InstanceOf(i,x) & FourMeaning(x)) -> (Appropriated(i) <-> (Present(i) & NotSeparateFromFaculty(i))))
all i.(Appropriated(i) <-> TakenAsBasis(i))
all i.(TakenAsBasis(i) -> MutualBenefitInjury(i))
all i.(Appropriated(i) <-> CalledAnimate(i))
exists i.(InstanceOf(i,sound) & Present(i) & -Appropriated(i))
# THEORY rejected_unassociated_half_takes_support
# EXPECT rejected_unassociated_half_takes_support F
exists x.(x = dharma_nonassociated & TakesSupport(x))
# THEORY rejected_form_takes_support
# EXPECT rejected_form_takes_support F
exists x.(AmongEighteen(x) & FormBearing(x) & TakesSupport(x))
# THEORY rejected_the_two_cuts_coincide
# EXPECT rejected_the_two_cuts_coincide F
all x.(AmongEighteen(x) -> (TakesSupport(x) <-> exists i.(InstanceOf(i,x) & Appropriated(i))))
# THEORY rejected_past_faculty_appropriated
# EXPECT rejected_past_faculty_appropriated F
exists i.exists x.(InstanceOf(i,x) & SenseFaculty(x) & -Present(i) & Appropriated(i))
# THEORY rejected_presence_suffices
# EXPECT rejected_presence_suffices F
all i.all x.((InstanceOf(i,x) & FourMeaning(x) & Present(i)) -> Appropriated(i))
# THEORY rejected_sound_twofold
# EXPECT rejected_sound_twofold F
exists i.(InstanceOf(i,sound) & Appropriated(i))
```

```nltk-valuation
sound => sabda_d
dharma_principle => dharma_d
dharma_associated => dharma_samprayukta
dharma_nonassociated => dharma_asamprayukta
AmongEighteen => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d,mano_d,dharma_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d}
Item => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d,mano_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d,dharma_samprayukta,dharma_asamprayukta}
CittaPrinciple => {mano_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d}
TakesSupport => {mano_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d,dharma_samprayukta}
GraspsCondition => {mano_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d,dharma_samprayukta}
FormBearing => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d}
SenseFaculty => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d}
ConditionMeaning => {rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d}
FourMeaning => {rupa_d,gandha_d,rasa_d,sprastavya_d}
PortionOf => {(dharma_samprayukta,dharma_d),(dharma_asamprayukta,dharma_d)}
InstanceOf => {(caksur_present,caksur_d),(caksur_past,caksur_d),(srotra_present,srotra_d),(srotra_past,srotra_d),(ghrana_present,ghrana_d),(ghrana_past,ghrana_d),(jihva_present,jihva_d),(jihva_past,jihva_d),(kaya_present,kaya_d),(kaya_past,kaya_d),(rupa_bound,rupa_d),(rupa_hair,rupa_d),(rupa_earth,rupa_d),(gandha_bound,gandha_d),(gandha_hair,gandha_d),(gandha_earth,gandha_d),(rasa_bound,rasa_d),(rasa_hair,rasa_d),(rasa_earth,rasa_d),(sprastavya_bound,sprastavya_d),(sprastavya_hair,sprastavya_d),(sprastavya_earth,sprastavya_d),(sabda_present,sabda_d),(mano_now,mano_d),(caksurvijnana_now,caksurvijnana_d),(srotravijnana_now,srotravijnana_d),(ghranavijnana_now,ghranavijnana_d),(jihvavijnana_now,jihvavijnana_d),(kayavijnana_now,kayavijnana_d),(manovijnana_now,manovijnana_d),(dharma_now,dharma_d)}
Present => {caksur_present,srotra_present,ghrana_present,jihva_present,kaya_present,rupa_bound,rupa_hair,rupa_earth,gandha_bound,gandha_hair,gandha_earth,rasa_bound,rasa_hair,rasa_earth,sprastavya_bound,sprastavya_hair,sprastavya_earth,sabda_present,mano_now,caksurvijnana_now,srotravijnana_now,ghranavijnana_now,jihvavijnana_now,kayavijnana_now,manovijnana_now,dharma_now}
NotSeparateFromFaculty => {rupa_bound,gandha_bound,rasa_bound,sprastavya_bound}
Appropriated => {caksur_present,srotra_present,ghrana_present,jihva_present,kaya_present,rupa_bound,gandha_bound,rasa_bound,sprastavya_bound}
TakenAsBasis => {caksur_present,srotra_present,ghrana_present,jihva_present,kaya_present,rupa_bound,gandha_bound,rasa_bound,sprastavya_bound}
MutualBenefitInjury => {caksur_present,srotra_present,ghrana_present,jihva_present,kaya_present,rupa_bound,gandha_bound,rasa_bound,sprastavya_bound}
CalledAnimate => {caksur_present,srotra_present,ghrana_present,jihva_present,kaya_present,rupa_bound,gandha_bound,rasa_bound,sprastavya_bound}
```

**Model checks.** The verse formula holds. The prose fixes the
half as the associated portion and denies a Support to the ten of Form
and the unassociated half. It makes the Dharma Principle a Principle
without being an Item of the first count, which is the change of scope.
Faculties are Appropriated exactly when present; the four meanings
exactly when present and not separate from the Faculty. Present Sound
stays Unappropriated. All six rejected theories are false.

**Bhāṣya determination.** *Sālambana viṣaya-grahaṇāt*: having a Support
is grasping a Condition. *Upātta* is what citta and the mental factors
take up as a basis, following one another in benefit and injury; the
world calls it animate.

**Organon interpretation.** The two cuts do not coincide. What takes a
Support is never Appropriated, and what is Appropriated never takes a
Support. Cognition grasps; the body it has taken up is grasped as basis.

```text
take a Support
    seven consciousness Principles
    associated half of the Dharma Principle

do not take a Support
    ten whose nature is Form
    unassociated half of the Dharma Principle

always Unappropriated
    the seven
    the whole Dharma Principle
    Sound

twofold
    five Faculties: Appropriated when present
    four meanings: Appropriated when present and not separate from the Faculty
    otherwise Unappropriated

Appropriated
    taken up by citta and the mental factors as a basis
    benefit and injury follow both ways

1.35 not opened
```

## 9. Interpretive Note

**Key-term evidence.** The Bhāṣya glosses *sālambana* by *viṣaya-grahaṇāt*. Having a Support (*ālambana*) is grasping a Condition (*viṣaya*). 1.29 kept the two apart: a Condition is where a thing acts, a Support is what citta and the mental factors grasp. Here the grasped Condition is the Support. Neither is a Ground (*hetu*).

**Translation note.** The seven consciousness Principles are the five sensory Cognitions, the Mind-Cognition Principle, and the Mind Principle; the relevant half of the Dharma Principle is its mental-factor portion. The nine unappropriated are those seven, the Dharma Principle, and Sound. “Appropriated” means taken up by consciousness and mental factors as a basis through mutual benefit or injury—the animate, as the world calls it.

The hinge is the change of scope. The first count uses a half. The second count uses the whole Dharma Principle. Sound joins the nine. The definition of appropriated is the close.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_34 a vak:Karika ;
    vak:hasTopic vak:SupportAndAppropriation ;
    vak:belongsTo vak:Dhatunirdesa .

vak:SevenCittaPrinciples vak:takesSupport true .
vak:AssociatedDharmaHalf vak:takesSupport true .
vak:NineAlwaysUnappropriated vak:includes
    vak:SevenCittaPrinciples, vak:DharmaPrinciple, vak:SoundPrinciple .
```
