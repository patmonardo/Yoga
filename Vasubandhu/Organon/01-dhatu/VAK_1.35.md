# VAK_1.35 — Element, Element-dependent, Accumulated

## 1. Sanskrit (Devanāgarī)

```sanskrit
स्प्रष्टव्यं द्विविधं शेषा रूपिणो नव भौतिकाः ।
धर्मधात्वेकदेशश्च सञ्चिता दश रूपिणः ॥ १.३५ ॥
```

## 2. Sanskrit (IAST)

```text
spraṣṭavyaṃ dvividhaṃ śeṣā rūpiṇo nava bhautikāḥ /
dharmadhātvekadeśaś ca saṃcitā daśa rūpiṇaḥ // 1.35 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| spraṣṭavyam | spraṣṭavya; nominative neuter singular | the Tangible |
| dvividham | dvi-vidha; nominative neuter singular | twofold: Element and Element-dependent |
| śeṣāḥ | śeṣa; nominative masculine plural | the remaining: Form Principles other than the Tangible |
| rūpiṇaḥ | rūpin; nominative masculine plural | whose nature is Form |
| nava | numeral | nine |
| bhautikāḥ | bhautika, from bhūta; nominative masculine plural | Element-dependent |
| dharma-dhātu-ekadeśaḥ | tatpuruṣa; nominative masculine singular | one portion of the Dharma Principle |
| ca | particle | and: adds the portion to the nine |
| saṃcitāḥ | saṃ-√ci, past participle; nominative masculine plural | Accumulated: clusters of atoms |
| daśa | numeral | ten |
| rūpiṇaḥ | rūpin; nominative masculine plural | whose nature is Form |

Element is *bhūta*. Principle is *dhātu*. The portion of the Dharma
Principle is avijñapti. The two occurrences of *rūpiṇaḥ* name the same
class of ten; *śeṣāḥ* subtracts the Tangible.

**Grammar tokens.** Verse-order IAST with sandhi opened (`spraṣṭavyaṃ` →
*spraṣṭavyam*, `śeṣā rūpiṇo` → *śeṣāḥ rūpiṇaḥ*, `dharmadhātvekadeśaś` →
*dharma-dhātu-ekadeśaḥ*, `saṃcitā` → *saṃcitāḥ*) and compound boundaries
marked.

```text
# tokens: spraṣṭavyam dvividham śeṣāḥ rūpiṇaḥ nava bhautikāḥ dharma-dhātu-ekadeśaḥ ca saṃcitāḥ daśa rūpiṇaḥ
```

## 4. Grammar

Three predications. The Tangible is twofold, with neuter singular
agreement. The remaining nine Form Principles, and a portion of the
Dharma Principle, are Element-dependent. The ten Form Principles are
Accumulated. The class *rūpin* carries `CNT=10`; *śeṣāḥ* with *nava*
requires the class of ten less one, and *daśa* must match the class
exactly.

```nltk-fcfg
% start S
# tokens: spraṣṭavyam dvividham śeṣāḥ rūpiṇaḥ nava bhautikāḥ dharma-dhātu-ekadeśaḥ ca saṃcitāḥ daśa rūpiṇaḥ
S[SEM=<(?a & ?b & ?c)>] -> TWOFOLD[SEM=?a] DEPENDENT[SEM=?b] ACCUM[SEM=?c]
TWOFOLD[SEM=<?d(?t)>] -> SPR[GEN=n,NUM=sg,SEM=?t] DVI[GEN=n,NUM=sg,SEM=?d]
DEPENDENT[SEM=<(all x.(?r(x) -> all i.(InstanceOf(i,x) -> ?b(i))) & exists h.(PortionOf(h,?p) & all i.(InstanceOf(i,h) -> ?b(i))))>] -> REST[CNT=9,SEM=?r] BHAUT[NUM=pl,SEM=?b] EKADESA[SEM=?p] CA
REST[CNT=9,SEM=<\x.(?f(x) & -(x = tangible))>] -> SESA[NUM=pl] RUPIN[NUM=pl,CNT=10,SEM=?f] NUMR[CNT=9]
ACCUM[SEM=<all x.(?r(x) -> ?s(x))>] -> SAMCITA[NUM=pl,SEM=?s] NUMR[CNT=?k] RUPIN[NUM=pl,CNT=?k,SEM=?r]
SPR[GEN=n,NUM=sg,SEM=<tangible>] -> 'spraṣṭavyam'
DVI[GEN=n,NUM=sg,SEM=<\t.(exists i.(InstanceOf(i,t) & GreatElement(i)) & exists i.(InstanceOf(i,t) & ElementDependent(i)))>] -> 'dvividham'
SESA[NUM=pl] -> 'śeṣāḥ'
RUPIN[NUM=pl,CNT=10,SEM=<\x.FormBearing(x)>] -> 'rūpiṇaḥ'
NUMR[CNT=9] -> 'nava'
NUMR[CNT=10] -> 'daśa'
BHAUT[NUM=pl,SEM=<\i.ElementDependent(i)>] -> 'bhautikāḥ'
EKADESA[SEM=<dharma_principle>] -> 'dharma-dhātu-ekadeśaḥ'
CA -> 'ca'
SAMCITA[NUM=pl,SEM=<\x.Accumulated(x)>] -> 'saṃcitāḥ'
```

```nltk-dep
'dvividham' -> 'spraṣṭavyam'
'bhautikāḥ' -> 'rūpiṇaḥ' | 'dharma-dhātu-ekadeśaḥ'
'rūpiṇaḥ' -> 'śeṣāḥ' | 'nava' | 'daśa'
'dharma-dhātu-ekadeśaḥ' -> 'ca'
'saṃcitāḥ' -> 'rūpiṇaḥ'
```

**Close construe.** The Tangible is twofold. The remaining nine whose
nature is Form are Element-dependent, and a portion of the Dharma
Principle. Ten whose nature is Form are Accumulated.

Twofold is said of a Principle through its instances: some are Great
Elements, some Element-dependent. The nine are Element-dependent in every
instance. The portion is existential in the verse; the Bhāṣya names it
avijñapti. Accumulated is said of the Principle itself.

## 5. Translation

### Literal Translation

> The Tangible is twofold. The other nine whose nature is Form are Element-
> dependent. And a portion of the Dharma Principle. The ten whose nature is
> Form are Accumulated.

### Bhāṣya-informed study translation

> The Tangible is twofold. The other nine Form Principles, and one portion
> of the Dharma Principle, are Element-dependent. The ten Form Principles
> are Accumulated.

## 6. Philosophical Translation

Only the Tangible is both. The four Great Elements are there, together with the seven Element-dependent tangibles. The other nine whose nature is Form are Element-dependent. Avijñapti, the portion of the Dharma Principle, is Element-dependent. The consciousness Principles and the rest of the Dharma Principle are neither.

Buddhadeva collapses the ten Essences into the Elements. The sūtra will not. The Great Elements are four, and they are Tangible. The eye does not grasp hardness. The body does not grasp color. The fleshy mass is not the Faculty. The six Principles of the person are not a denial of the mental factors.

Accumulated is the other cut. The ten whose nature is Form are clusters of atoms. The rest are not.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| bhūta, mahābhūta | Element, Great Element | four, in the Tangible |
| bhautika | Element-dependent | *upādāya-rūpa*: Form depending on the Great Elements |
| spraṣṭavya | Tangible | the only twofold |
| avijñapti | avijñapti | the Element-dependent portion of the Dharma Principle |
| saṃcita | Accumulated | clusters of atoms |
| daśa rūpiṇaḥ | ten whose nature is Form | five Faculties and five Condition-Principles |
| viṣaya | Condition | the four Conditions among the nine |
| āyatana | Essence | the sūtra’s word |
| saṃjñā | reflection | follows consciousness |

## 8. Logical Determination

**Kārikā, derived.** The Tangible has Great Element instances and
Element-dependent instances; every instance of the other nine Form
Principles is Element-dependent, and so is every instance of some portion
of the Dharma Principle; the ten Form Principles are Accumulated.

```nltk-sem
# derived by the section 4 parse
(exists i.(InstanceOf(i,tangible) & GreatElement(i)) & exists i.(InstanceOf(i,tangible) & ElementDependent(i)) & all x.((FormBearing(x) & -(x = tangible)) -> all i.(InstanceOf(i,x) -> ElementDependent(i))) & exists h.(PortionOf(h,dharma_principle) & all i.(InstanceOf(i,h) -> ElementDependent(i))) & all x.(FormBearing(x) -> Accumulated(x)))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(exists i.(InstanceOf(i,tangible) & GreatElement(i)) & exists i.(InstanceOf(i,tangible) & ElementDependent(i)) & all x.((FormBearing(x) & -(x = tangible)) -> all i.(InstanceOf(i,x) -> ElementDependent(i))) & exists h.(PortionOf(h,dharma_principle) & all i.(InstanceOf(i,h) -> ElementDependent(i))) & all x.(FormBearing(x) -> Accumulated(x)))
# THEORY prose
# EXPECT prose T
all i.(GreatElement(i) <-> ((i = earth) | (i = water) | (i = fire) | (i = wind)))
all i.((InstanceOf(i,tangible) & ElementDependent(i)) <-> ((i = smooth) | (i = rough) | (i = heavy) | (i = light) | (i = cold) | (i = hunger) | (i = thirst)))
all i.-(GreatElement(i) & ElementDependent(i))
all x.(AmongEighteen(x) -> (exists i.(InstanceOf(i,x) & GreatElement(i)) <-> (x = tangible)))
exists h.(h = avijnapti_portion & PortionOf(h,dharma_principle) & all i.(InstanceOf(i,h) -> ElementDependent(i)))
all x.(CittaPrinciple(x) -> all i.(InstanceOf(i,x) -> (-GreatElement(i) & -ElementDependent(i))))
exists h.(h = dharma_rest & PortionOf(h,dharma_principle) & all i.(InstanceOf(i,h) -> (-GreatElement(i) & -ElementDependent(i))))
all i.(GreatElement(i) -> all f.(GraspedBy(i,f) -> (f = body)))
all i.(InstanceOf(i,visible_form) -> -GraspedBy(i,body))
exists m.(m = eye_fleshy_mass & Contains(m,earth) & -SenseFaculty(m))
exists p.(p = person & SixPrincipleShowing(p))
exists f.(f = vedana & MentalFactor(f) & FollowsCitta(f) & -Citta(f))
all x.(AmongEighteen(x) -> (Accumulated(x) <-> AtomCluster(x)))
exists t.(t = buddhadeva_thesis & AttributedTo(t,buddhadeva) & Refuted(t))
# THEORY rejected_ten_are_only_elements
# EXPECT rejected_ten_are_only_elements F
all x.(FormBearing(x) -> all i.(InstanceOf(i,x) -> GreatElement(i)))
# THEORY rejected_elements_outside_the_tangible
# EXPECT rejected_elements_outside_the_tangible F
exists i.exists x.(GreatElement(i) & InstanceOf(i,x) & -(x = tangible))
# THEORY rejected_eye_grasps_hardness
# EXPECT rejected_eye_grasps_hardness F
exists i.(GreatElement(i) & GraspedBy(i,eye))
# THEORY rejected_fleshy_mass_is_the_faculty
# EXPECT rejected_fleshy_mass_is_the_faculty F
exists m.(m = eye_fleshy_mass & SenseFaculty(m))
# THEORY rejected_mental_factors_are_citta
# EXPECT rejected_mental_factors_are_citta F
all f.(MentalFactor(f) -> Citta(f))
# THEORY rejected_avijnapti_accumulated
# EXPECT rejected_avijnapti_accumulated F
exists h.(h = avijnapti_portion & Accumulated(h))
# THEORY rejected_consciousness_element_dependent
# EXPECT rejected_consciousness_element_dependent F
exists i.exists x.(CittaPrinciple(x) & InstanceOf(i,x) & ElementDependent(i))
```

```nltk-valuation
tangible => sprastavya_d
visible_form => rupa_d
eye => caksur_d
body => kaya_d
dharma_principle => dharma_d
avijnapti_portion => dharma_avijnapti
dharma_rest => dharma_rest
earth => earth_i
water => water_i
fire => fire_i
wind => wind_i
smooth => smooth_i
rough => rough_i
heavy => heavy_i
light => light_i
cold => cold_i
hunger => hunger_i
thirst => thirst_i
vedana => vedana_i
eye_fleshy_mass => caksur_mamsapinda
person => purusa
buddhadeva => bhadanta_buddhadeva
buddhadeva_thesis => bhutamatra_thesis
AmongEighteen => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d,mano_d,dharma_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d}
FormBearing => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d}
SenseFaculty => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d}
CittaPrinciple => {mano_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d}
PortionOf => {(dharma_avijnapti,dharma_d),(dharma_rest,dharma_d)}
InstanceOf => {(caksur_i,caksur_d),(srotra_i,srotra_d),(ghrana_i,ghrana_d),(jihva_i,jihva_d),(kaya_i,kaya_d),(rupa_i,rupa_d),(sabda_i,sabda_d),(gandha_i,gandha_d),(rasa_i,rasa_d),(earth_i,sprastavya_d),(water_i,sprastavya_d),(fire_i,sprastavya_d),(wind_i,sprastavya_d),(smooth_i,sprastavya_d),(rough_i,sprastavya_d),(heavy_i,sprastavya_d),(light_i,sprastavya_d),(cold_i,sprastavya_d),(hunger_i,sprastavya_d),(thirst_i,sprastavya_d),(mano_i,mano_d),(caksurvijnana_i,caksurvijnana_d),(srotravijnana_i,srotravijnana_d),(ghranavijnana_i,ghranavijnana_d),(jihvavijnana_i,jihvavijnana_d),(kayavijnana_i,kayavijnana_d),(manovijnana_i,manovijnana_d),(avijnapti_i,dharma_avijnapti),(vedana_i,dharma_rest),(samjna_i,dharma_rest)}
GreatElement => {earth_i,water_i,fire_i,wind_i}
ElementDependent => {avijnapti_i,caksur_i,srotra_i,ghrana_i,jihva_i,kaya_i,rupa_i,sabda_i,gandha_i,rasa_i,smooth_i,rough_i,heavy_i,light_i,cold_i,hunger_i,thirst_i}
Accumulated => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d}
AtomCluster => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d}
GraspedBy => {(earth_i,kaya_d),(water_i,kaya_d),(fire_i,kaya_d),(wind_i,kaya_d),(rupa_i,caksur_d)}
Contains => {(caksur_mamsapinda,earth_i)}
MentalFactor => {vedana_i,samjna_i}
FollowsCitta => {vedana_i,samjna_i}
Citta => {mano_i,caksurvijnana_i,srotravijnana_i,ghranavijnana_i,jihvavijnana_i,kayavijnana_i,manovijnana_i}
SixPrincipleShowing => {purusa}
AttributedTo => {(bhutamatra_thesis,bhadanta_buddhadeva)}
Refuted => {bhutamatra_thesis}
```

**Model checks.** The verse formula holds. The prose fixes the four
Great Elements and the seven Element-dependent tangibles, keeps every
Great Element inside the Tangible, and makes the consciousness Principles
and the rest of the Dharma Principle neither. Great Elements are grasped
only by the body; visible Form is not. All seven rejected theories are
false, Buddhadeva's first among them.

**Bhāṣya determination.** *Bhūteṣu bhavatvāt*: the seven tangibles are
Element-dependent because they occur in the Elements. *Bhūtānāṃ
spraṣṭavyāyatana-ekadeśa-saṃgrahāt*: the Elements are included in one
portion of the Tangible Essence, so the rest is not Element.
*Paramāṇu-saṃghātatvāt*: the ten are Accumulated as clusters of atoms.

**Organon interpretation.** The Element is not the Principle. The four
sit in the Tangible, and what depends on them sits there with them.
Element-dependence and accumulation are separate cuts: avijñapti is
Element-dependent and not Accumulated.

```text
Tangible
    four Great Elements
    seven Element-dependent tangibles

other nine of Form
    only Element-dependent
    five Faculties, four Conditions

Dharma Principle
    avijñapti Element-dependent
    the rest neither

consciousness Principles
    neither

Buddhadeva
    ten Essences are only Elements
    rejected by the four, and by the grasp

Accumulated
    the ten whose nature is Form
    the rest not

1.36 not opened
```

## 9. Interpretive Note

**Key-term evidence.** *Bhautika* is *upādāya-rūpa*, Form taken up depending on the Great Elements. 2.65 makes this relation a Ground: the Elements are fivefold Grounds of such Form (*pañcadhā rūpahetavaḥ*). Here the relation is only named; its protocol is deferred to 2.65.

**Translation note.** The Bhāṣya specifies the Tangible’s two kinds as the Great Elements and Element-dependent tangibles. The other nine Form Principles are five Faculties and four Conditions; the Dharma Principle portion is *avijñapti*. The ten accumulated Form Principles are clusters of atoms: five Faculties and five Condition-Principles.

The hinge is the Tangible. It is the only Principle that is both Element and Element-dependent. The sūtra on the Tangible says the four and the Form that depends on them. That is the refusal of Buddhadeva. The accumulation is a separate count.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_35 a vak:Karika ;
    vak:hasTopic vak:ElementAndElementDependent ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Tangible vak:twofold true .
vak:NineOfForm vak:elementDependentOnly true .
vak:Avijnapti vak:elementDependent true .
vak:TenOfForm vak:accumulated true .
```
