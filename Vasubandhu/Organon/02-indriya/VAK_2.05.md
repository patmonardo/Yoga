# VAK_2.05 — As Far As That

## 1. Sanskrit (Devanāgarī)

```sanskrit
चित्ताश्रयस्तद्विकल्पः स्थितिः संक्लेश एव च ।
संभारो व्यवदानं च यावता तावदिन्द्रियम् ॥ २.५ ॥
```

## 2. Sanskrit (IAST)

```text
cittāśrayas tadvikalpaḥ sthitiḥ saṃkleśa eva ca /
saṃbhāro vyavadānaṃ ca yāvatā tāvad indriyam // 2.5 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| citta-āśrayaḥ | nominative masculine singular | Basis of Consciousness |
| tad-vikalpaḥ | nominative masculine singular | differentiation of that Basis |
| sthitiḥ | nominative feminine singular | persistence of that Basis |
| saṃkleśaḥ | nominative masculine singular | its defilement |
| eva | focusing particle | just, indeed; focuses the defilement member |
| ca | coordinating particle | and; occurs twice |
| saṃbhāraḥ | nominative masculine singular | provision for purification |
| vyavadānam | nominative neuter singular | purification |
| yāvatā | correlative, extent | as far as |
| tāvat | correlative, extent | so far |
| indriyam | nominative neuter singular | Faculty in the intended enumeration |

Vikalpa here is female and male differentiation of the living basis. It is not concept, and it is not imagination.

**Grammar tokens.** External sandhi is opened, including *saṃkleśa
eva*. The two occurrences of *ca* remain separate tokens.

```text
# tokens: citta-āśrayaḥ tad-vikalpaḥ sthitiḥ saṃkleśaḥ eva ca saṃbhāraḥ vyavadānam ca yāvatā tāvat indriyam
```

## 4. Grammar

The six nominatives form an ordered roster of roles. *Tad* in
*tad-vikalpaḥ* resumes the sixfold Basis of Consciousness identified by
the Bhāṣya. Although *vikalpa* can name a mental factor, the Bhāṣya
specifies female and male differentiation of this sixfold basis here.
*Eva* focuses the defilement member; the two *ca*s
coordinate the roster. The correlative *yāvatā ... tāvat* sets both
directions of its extent within what the Bhāṣya calls intended *here*:
every counted Faculty has one of these roles, and the role-bearers
identified in this enumeration are counted. It does not define every
use of *indriya* in all contexts.

```nltk-fcfg
% start S
# tokens: citta-āśrayaḥ tad-vikalpaḥ sthitiḥ saṃkleśaḥ eva ca saṃbhāraḥ vyavadānam ca yāvatā tāvat indriyam
S[SEM=<?limit(?roles)>] -> ROSTER[SEM=?roles] LIMIT[SEM=?limit]
ROSTER[SEM=<\x.(?a(x) | ?b(x) | ?c(x) | ?d(x) | ?e(x) | ?f(x))>] -> BASIS[CASE=nom,REF=?r,SEM=?a] DIFF[CASE=nom,REF=?r,SEM=?b] STAY[CASE=nom,SEM=?c] DEFILE[CASE=nom,FOCUS=?focus,SEM=?d] EVA[FOCUS=?focus] CA EQUIP[CASE=nom,SEM=?e] PURIFY[CASE=nom,SEM=?f] CA
LIMIT[SEM=<\P.(?extent(?faculty)(P) & ?return(?faculty)(P))>] -> YAVATA[SEM=?extent] TAVAT[SEM=?return] INDRIYAM[CASE=nom,NUM=sg,GEN=n,SEM=?faculty]
BASIS[CASE=nom,REF=basis_six,SEM=<\x.BasisOfConsciousness(x)>] -> 'citta-āśrayaḥ'
DIFF[CASE=nom,REF=basis_six,SEM=<\x.Differentiates(x,basis_six)>] -> 'tad-vikalpaḥ'
STAY[CASE=nom,SEM=<\x.Sustains(x,basis_six)>] -> 'sthitiḥ'
DEFILE[CASE=nom,FOCUS=defilement,SEM=<\x.Defiles(x,basis_six)>] -> 'saṃkleśaḥ'
EVA[FOCUS=defilement] -> 'eva'
CA -> 'ca'
EQUIP[CASE=nom,SEM=<\x.EquipsPurification(x)>] -> 'saṃbhāraḥ'
PURIFY[CASE=nom,SEM=<\x.Purifies(x)>] -> 'vyavadānam'
YAVATA[SEM=<\F.\P.all x.(F(x) -> P(x))>] -> 'yāvatā'
TAVAT[SEM=<\F.\P.all x.(P(x) -> F(x))>] -> 'tāvat'
INDRIYAM[CASE=nom,NUM=sg,GEN=n,SEM=<\x.FacultyHere(x)>] -> 'indriyam'
```

```nltk-dep
'indriyam' -> 'yāvatā' | 'tāvat' | 'citta-āśrayaḥ' | 'tad-vikalpaḥ' | 'sthitiḥ' | 'saṃkleśaḥ' | 'saṃbhāraḥ' | 'vyavadānam'
'saṃkleśaḥ' -> 'eva' | 'ca'
'vyavadānam' -> 'ca'
```

**Feature chart checkpoints.** The normalized stream has twelve
tokens. The shared `REF=basis_six` connects *tad* with its antecedent;
`FOCUS=defilement` constrains *eva*. The correlative's two lambda
functions compose the two extent directions.

| Span | Constituent | Result |
|---|---|---|
| [0, 9) | `ROSTER` | six source-ordered role predicates |
| [9, 12) | `LIMIT` | two directions of the local extent |
| [0, 12) | `S` | FacultyHere exactly over those role-bearers in this intended enumeration |

## 5. Translation

### Literal Translation

> Basis of Consciousness, its differentiation, persistence, and
> defilement; equipment and purification: as far as that, so far Faculty.

### Bhāṣya-informed study translation

> The Basis of Consciousness, its differentiation, persistence, and
> defilement, provision for purification, and purification itself:
> Faculty extends just this far.

## 6. Philosophical Translation

> Within the intended enumeration, six roles determine which powers
> count as Faculties. Governing efficacy alone does not settle membership.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| citta-āśraya | Basis of Consciousness | the six Faculties together; *citta* is not identified with the single *manas* faculty; āśraya is not ālambana |
| ṣaḍāyatana | sixfold āyatana | fundamental constitution of a living being |
| maulaṃ sattva-dravya | fundamental constitution | the commentary's phrase; not a substance thesis |
| tad-vikalpa | its differentiation | female and male in this Bhāṣya; do not generalize this local sense to every use of *vikalpa* |
| saṃbhāra | provision for purification | the five beginning with faith; not inert |
| vyavadāna | purification | the three |
| yāvatā tāvat | as far as that, so far | the membership limit within the intended enumeration |
| upasaṃkhyāna | supplementary inclusion | what is refused |
| avidyā | ignorance | governs; not a faculty here |
| vāk, pāṇi, pāda, pāyu, upastha | speech, hand, foot, anus, genital organ | proposed; excluded |

## 8. Logical Determination

**Kārikā, derived.** The parse composes the six roles into one
predicate, then applies the two sides of *yāvatā ... tāvat* to the
locally scoped `FacultyHere`. This is an extent claim for the
Bhāṣya's intended enumeration, not a definition that every governing
power in every context must satisfy these six roles. The `Basis`
relation belongs to *āśraya*; no *ālambana* relation is introduced.

```nltk-sem
roles : \x.(BasisOfConsciousness(x) | Differentiates(x,basis_six) | Sustains(x,basis_six) | Defiles(x,basis_six) | EquipsPurification(x) | Purifies(x))
forward_extent : \F.\P.all x.(F(x) -> P(x))
return_extent : \F.\P.all x.(P(x) -> F(x))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all x.(FacultyHere(x) -> (BasisOfConsciousness(x) | Differentiates(x,basis_six) | Sustains(x,basis_six) | Defiles(x,basis_six) | EquipsPurification(x) | Purifies(x))) & all x.((BasisOfConsciousness(x) | Differentiates(x,basis_six) | Sustains(x,basis_six) | Defiles(x,basis_six) | EquipsPurification(x) | Purifies(x)) -> FacultyHere(x)))

# THEORY prose
# EXPECT prose T
all x.(ProposedActionPower(x) -> -FacultyHere(x))
all x.(IgnoranceOrOther(x) -> -FacultyHere(x))
exists x y.(Governs(x,y) & -FacultyHere(x))
(FacultyHere(female_faculty) & FacultyHere(male_faculty) & -FacultyHere(genital_action_power))

# THEORY rejected_governance_suffices
# EXPECT rejected_governance_suffices F
all x.((exists y.Governs(x,y)) -> FacultyHere(x))

# THEORY rejected_action_powers_included
# EXPECT rejected_action_powers_included F
all x.(ProposedActionPower(x) -> FacultyHere(x))

# THEORY rejected_sex_faculty_is_action_organ
# EXPECT rejected_sex_faculty_is_action_organ F
all x.((x = genital_action_power) -> (x = female_faculty | x = male_faculty))
```

The prose theory accepts the objection's premise: ignorance and the
proposed action powers exercise governing efficacy in their respective
fields. It tests the reply's scope restriction rather than denying
those causal relations. The final countermodel keeps the genital
action organ proposed for pleasure distinct from the female and male
Faculties that govern sexed differentiation in 2.02.

```nltk-valuation
basis_six => sixfold_basis
female_faculty => female_f
male_faculty => male_f
genital_action_power => genital_power
BasisOfConsciousness => {eye,ear,nose,tongue,body,mind}
Differentiates => {(female_f,sixfold_basis),(male_f,sixfold_basis)}
Sustains => {(life,sixfold_basis)}
Defiles => {(pleasure,sixfold_basis),(pain,sixfold_basis),(gladness,sixfold_basis),(distress,sixfold_basis),(equanimity,sixfold_basis)}
EquipsPurification => {faith,vigor,mindfulness,concentration,comprehension}
Purifies => {shall_know,knowledge,has_known}
FacultyHere => {eye,ear,nose,tongue,body,mind,female_f,male_f,life,pleasure,pain,gladness,distress,equanimity,faith,vigor,mindfulness,concentration,comprehension,shall_know,knowledge,has_known}
ProposedActionPower => {speech,hand,foot,anus,genital_power}
IgnoranceOrOther => {ignorance}
Governs => {(ignorance,formations),(speech,speaking),(hand,taking),(foot,moving),(anus,excretion),(genital_power,pleasure_act)}
```

This finite witness has the Bhāṣya's 6 + 2 + 1 + 5 + 5 + 3 roster.
The verse itself names six roles, not their member counts. The model
does not establish that no other tradition can call a power
*indriya*, or that the five provisions cease to govern purification
because the three receive the purification role in this enumeration.

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the
verse translation): Faculty is the Basis of Consciousness, its differentiation,
its persistence, and its defilement, together with its equipment and its
purification: as far as these extend, so far is faculty. The six faculties
are the Basis of Consciousness; its differentiation is through the female and
male faculties, their persistence through life, their defilement through
the feelings, the provision for purification through the five, and
purification through the three. Ignorance and the rest, and speech and the
other action-organs, are therefore not counted.

2.01 gave the predicate. 2.02 narrowed it to apprehension. 2.03 and 2.04 filled defilement and purification. This verse stops the count.

The objector is right that ignorance governs formations, and that speech and the four govern their acts. The reply does not deny that. Iha bounds the enumeration. Sāṃkhya counts action-faculties of this kind. In Sāṃkhya Kārikā 25–27 and 33, its eleven Faculties include Manas, while Buddhi and Ahaṃkāra belong with Manas to the threefold inner instrument. This places the Sāṃkhya Faculty list at the Manas level without making Manas the whole of Consciousness. As Rational Overlord in the Organon synthesis, this ordering governs how the Kośa's twenty-two Faculties are compared and placed; they are not a fuller list of Sāṃkhya's eleven. The Kośa passage itself does not name Sāṃkhya.

The five are provision. They are not inert: 2.03 already has them check and draw the path. The three are purification itself. 2.04 already split them into seeing, cultivation, and one who has known. No chronology in which the five stop before the three begin.

Here **Consciousness** renders *citta* in *cittāśraya*. The six faculties
form its Basis; *citta* is not thereby identified with the single
*manas* faculty among them. The Kośa's account concerns both Reason and
Understanding in the Organon reading. Reason remains higher than
Understanding, and important Ideas cannot be reduced to Understanding's
functions. This ordering is a project determination, not a claim stated
by this verse. Mental factors may be understood as factors of
Consciousness, but the Bhāṣya specifies *tad-vikalpa* here as female and
male differentiation of the sixfold Basis.

Interpretation: membership is the discriminator. The six roles define the intended scope. The victim traverses that path and not the powers left outside it. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_05
    a vak:Karika ;
    rdfs:label "VAK 2.05" ;
    vak:hasTopic vak:MembershipLimit ;
    vak:belongsTo vak:Indriyanirdesa .

vak:TwentyTwoIndriyas vak:boundedBy vak:SixIntendedRoles .
vak:SixIntendedRoles vak:hasMembers vak:ConsciousnessBasis,
    vak:Differentiation, vak:Persistence, vak:Defilement,
    vak:Provision, vak:Purification .
vak:Ignorance vak:notIncludedIn vak:TwentyTwoIndriyas .
vak:Speech vak:notIncludedIn vak:TwentyTwoIndriyas .

organon:MembershipDiscriminator
    organon:bounds vak:TwentyTwoIndriyas ;
    organon:notTheVerseEnglish true .
```
