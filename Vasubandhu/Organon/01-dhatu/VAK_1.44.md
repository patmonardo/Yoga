# VAK_1.44 — Equal Grasp, and the Past Basis

## 1. Sanskrit (Devanāgarī)

```sanskrit
त्रिभिर्घ्राणादिभिस्तुल्यविषयग्रहणं मतम् ।
चरमस्याश्रयोऽतीतः पञ्चानां सहजश्च तैः ॥ १.४४ ॥
```

## 2. Sanskrit (IAST)

```text
tribhir ghrāṇādibhis tulyaviṣayagrahaṇaṃ matam /
caramasyāśrayo 'tītaḥ pañcānāṃ sahajaś ca taiḥ // 1.44 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| tribhiḥ | tri; instrumental plural | by three: the count that closes the list |
| ghrāṇa-ādibhiḥ | bahuvrīhi; instrumental plural | by those beginning with the Nose: Nose, Tongue, Body |
| tulya-viṣaya-grahaṇam | tatpuruṣa; nominative neuter singular | apprehension of a Condition equal in extent |
| matam | √man, past passive participle; nominative neuter singular | is held: the doctrine, not a new proof |
| caramasya | carama; genitive singular | of the last: Mind-Cognition |
| āśrayaḥ | āśraya; nominative masculine singular | the Basis |
| atītaḥ | ati-√i, past participle; nominative masculine singular | past: ceased immediately before |
| pañcānām | pañcan; genitive plural | of the five: the sensory Cognitions |
| sahajaḥ | saha-ja; nominative masculine singular | born together: *āśrayaḥ* is understood |
| ca | particle | and: carries *atītaḥ* over to the five |
| taiḥ | tad; instrumental plural | with them: the five Cognitions |

The instrumental is the agent of the passive *matam*: by the three,
apprehension of an equal Condition is held to take place. *Sahajaḥ*
agrees with the elided *āśrayaḥ*. The Bhāṣya reads the *ca* as bringing in
the past Basis as well (*atītaś ceti ca-śabdaḥ*).

**Grammar tokens.** Verse-order IAST with sandhi opened (`tribhir
ghrāṇādibhis` → *tribhiḥ ghrāṇa-ādibhiḥ*, `caramasyāśrayo 'tītaḥ` →
*caramasya āśrayaḥ atītaḥ*, `sahajaś` → *sahajaḥ*) and compound
boundaries marked.

```text
# tokens: tribhiḥ ghrāṇa-ādibhiḥ tulya-viṣaya-grahaṇam matam caramasya āśrayaḥ atītaḥ pañcānām sahajaḥ ca taiḥ
```

## 4. Grammar

Two clauses. In the first, the numeral *tribhiḥ* and *ghrāṇa-ādibhiḥ*
agree as instrumental plurals and share a count (CNT=3): the open list
"beginning with the Nose" is closed by the numeral at Nose, Tongue, and
Body. *Matam* agrees with *tulya-viṣaya-grahaṇam* as neuter singular and
marks the claim as held doctrine (EVID=held).

In the second, two genitives divide the Cognitions. *Caramasya* is
singular: the last, Mind-Cognition. *Pañcānām* is plural (CNT=5): the
five sensory Cognitions. *Āśrayaḥ*, *atītaḥ*, and *sahajaḥ* agree as
masculine singular nominatives, so *sahajaḥ* takes *āśrayaḥ* by ellipsis.
*Taiḥ* agrees in number with *pañcānām*: the Basis is born together with
the five. *Ca* is the carrier. It takes the predicate "past" from the
first half and adds it to the five, so the grammar derives two Bases for
the five and only the past one for the last.

```nltk-fcfg
% start S
# tokens: tribhiḥ ghrāṇa-ādibhiḥ tulya-viṣaya-grahaṇam matam caramasya āśrayaḥ atītaḥ pañcānām sahajaḥ ca taiḥ
S[SEM=<(?a & ?b)>] -> EQ[SEM=?a] SUP[SEM=?b]
EQ[SEM=<all x.(?n(x) -> ?p(x))>] -> NUMR[CASE=ins,CNT=?k,NUM=pl] NI[CASE=ins,CNT=?k,NUM=pl,SEM=?n] PRED[GEN=?g,NUM=?s,SEM=?p] MATA[EVID=held,GEN=?g,NUM=?s]
SUP[SEM=<(all c.(?l(c) -> exists b.(?r(b,c) & ?t(b))) & all c.all b.((?l(c) & ?r(b,c)) -> ?t(b)) & all c.(?f(c) -> (exists b.(?r(b,c) & ?h(b,c)) & exists b.(?r(b,c) & ?k(?t,b)))))>] -> LASTG[CASE=gen,NUM=sg,SEM=?l] ASR[CASE=nom,GEN=?g,NUM=?s,SEM=?r] ATI[CASE=nom,GEN=?g,NUM=?s,SEM=?t] FIVEG[CASE=gen,NUM=?p,SEM=?f] SAHA[CASE=nom,GEN=?g,NUM=?s,SEM=?h] CA[SEM=?k] TAI[CASE=ins,NUM=?p]
NUMR[CASE=ins,CNT=3,NUM=pl] -> 'tribhiḥ'
NI[CASE=ins,CNT=3,NUM=pl,SEM=<\x.((x = nose) | (x = tongue) | (x = body))>] -> 'ghrāṇa-ādibhiḥ'
PRED[GEN=n,NUM=sg,SEM=<\x.EqualGrasp(x)>] -> 'tulya-viṣaya-grahaṇam'
MATA[EVID=held,GEN=n,NUM=sg] -> 'matam'
LASTG[CASE=gen,NUM=sg,SEM=<\x.MindCog(x)>] -> 'caramasya'
ASR[CASE=nom,GEN=m,NUM=sg,SEM=<\y z.BasisOf(y,z)>] -> 'āśrayaḥ'
ATI[CASE=nom,GEN=m,NUM=sg,SEM=<\y.Past(y)>] -> 'atītaḥ'
FIVEG[CASE=gen,CNT=5,NUM=pl,SEM=<\x.FiveCog(x)>] -> 'pañcānām'
SAHA[CASE=nom,GEN=m,NUM=sg,SEM=<\y z.Coborn(y,z)>] -> 'sahajaḥ'
CA[SEM=<\P y.P(y)>] -> 'ca'
TAI[CASE=ins,NUM=pl] -> 'taiḥ'
```

```nltk-dep
'matam' -> 'tulya-viṣaya-grahaṇam' | 'ghrāṇa-ādibhiḥ'
'ghrāṇa-ādibhiḥ' -> 'tribhiḥ'
'āśrayaḥ' -> 'caramasya' | 'atītaḥ'
'sahajaḥ' -> 'pañcānām' | 'taiḥ' | 'ca'
```

**Close construe.** By the three beginning with the Nose, apprehension of
an equal Condition is held. Of the last, the Basis is past. Of the five,
a Basis born together with them, and past as well.

Equal means count for count: as many Faculty-atoms, so many
Condition-atoms. The Basis of a Cognition is not timed as its Condition
is.

## 5. Translation

### Literal Translation

> By the three beginning with the Nose, apprehension of an equal Condition
> is held. The Basis of the last is past. Of the five, a co-born one too,
> with them.

### Bhāṣya-informed study translation

> The three Faculties beginning with the Nose, it is held, apprehend a
> Condition equal in extent to themselves. The Basis of the last Cognition
> is past; the five sensory Cognitions have a Basis born together with
> them, and the past one as well.

## 6. Philosophical Translation

Equal apprehension belongs to the three that reach. As many Faculty-atoms, so many Condition-atoms, and Cognition arises from the meeting. Eye and ear have no measure. A hair-tip, a grape, a mountain, by the opening of the eye. The ear likewise: a mosquito, a cloud. Mind is unformed. Size is not determined of it.

The arrangements are the seats of those atoms: cumin flower on the pupil, birch of the ear, probe in the pot, half-moon of the tongue, the body like the body. Clear skin keeps the eye-atoms from scattering. Crystal-clear, they do not cover one another. The body never works with all its atoms. If it did, the Basis would disintegrate. One atom does not produce Cognition. The five take an accumulation as Basis and as Support. An atom is invisible because it is not seen.

The Basis is not timed as the Condition is. The Condition of the five is present. The Condition of Mind-Cognition is of the three times. The Basis of Mind-Cognition is past: Mind that ceased immediately before. The five have that past Basis too, and a co-born Basis: the Eye with Eye-Cognition, through the Body with Body-Cognition. Two Bases. The four alternatives keep Basis and the immediately preceding Condition from collapsing. The eye is Basis and not that Condition. Immediately past Mind is both. The immediately past mental Dharma Principle is the Condition and not the Basis.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| tulya-viṣaya-grahaṇa | apprehension of a Condition equal in extent | Nose, Tongue, Body |
| aniyama | no rule | eye and ear |
| amūrta | unformed | Mind; no size |
| sabhāga | does its own work | not all the body-atoms |
| tatsabhāga | corresponds and does not | the remainder |
| saṃcita | accumulated | one atom does not produce Cognition |
| carama | the last | Mind-Cognition |
| āśraya | Basis | distinct from *ālambana* (Support) |
| sahaja āśraya | co-born Basis | the eye, and so on |
| atīta āśraya | past Basis | Mind that ceased immediately before |
| samanantara-pratyaya | immediately preceding Condition | not the same as Basis |

## 8. Logical Determination

**Kārikā, derived.**
- Nose, Tongue, and Body grasp equally.
- Every Mind-Cognition has a Basis, and every Basis it has is past.
- Every one of the five sensory Cognitions has a co-born Basis and a past Basis.

```nltk-sem
# derived by the section 4 parse
(all x.(((x = nose) | (x = tongue) | (x = body)) -> EqualGrasp(x)) & all c.(MindCog(c) -> exists b.(BasisOf(b,c) & Past(b))) & all c b.((MindCog(c) & BasisOf(b,c)) -> Past(b)) & all c.(FiveCog(c) -> (exists b.(BasisOf(b,c) & Coborn(b,c)) & exists b.(BasisOf(b,c) & Past(b)))))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all x.(((x = nose) | (x = tongue) | (x = body)) -> EqualGrasp(x)) & all c.(MindCog(c) -> exists b.(BasisOf(b,c) & Past(b))) & all c b.((MindCog(c) & BasisOf(b,c)) -> Past(b)) & all c.(FiveCog(c) -> (exists b.(BasisOf(b,c) & Coborn(b,c)) & exists b.(BasisOf(b,c) & Past(b)))))
# THEORY prose
# EXPECT prose T
all x.(Faculty(x) -> (EqualGrasp(x) <-> all g.(GraspBy(x,g) -> EqualAtoms(g))))
exists g.(GraspBy(eye,g) & FewerAtoms(g))
exists g.(GraspBy(eye,g) & EqualAtoms(g))
exists g.(GraspBy(eye,g) & MoreAtoms(g))
exists g.(GraspBy(ear,g) & FewerAtoms(g))
exists g.(GraspBy(ear,g) & MoreAtoms(g))
exists m.(m = mind & -Rupin(m) & all g.(GraspBy(m,g) -> -Measured(g)))
all x.all g.((Rupin(x) & GraspBy(x,g)) -> Accumulated(g))
all g.(GraspBy(body,g) -> -AllAtoms(g))
all c.all v.((FiveCog(c) & CondOf(v,c)) -> Present(v))
exists v.(CondOf(v,mc) & Past(v))
exists v.(CondOf(v,mc) & Present(v))
exists v.(CondOf(v,mc) & Future(v))
exists x.(x = eye & BasisOf(x,ec) & Coborn(x,ec) & -Samanantara(x,ec))
exists x.(x = pastmental & Samanantara(x,ec) & -BasisOf(x,ec))
exists x.(x = pastmind & BasisOf(x,ec) & Samanantara(x,ec))
exists x.(-BasisOf(x,ec) & -Samanantara(x,ec))
all x.(BasisOf(x,mc) -> Samanantara(x,mc))
exists x.(Samanantara(x,mc) & -BasisOf(x,mc))
# THEORY rejected_eye_equal
# EXPECT rejected_eye_equal F
all g.(GraspBy(eye,g) -> EqualAtoms(g))
# THEORY rejected_mind_measured
# EXPECT rejected_mind_measured F
exists g.(GraspBy(mind,g) & Measured(g))
# THEORY rejected_one_atom
# EXPECT rejected_one_atom F
exists x.exists g.(Rupin(x) & GraspBy(x,g) & -Accumulated(g))
# THEORY rejected_mind_coborn
# EXPECT rejected_mind_coborn F
exists c.exists b.(MindCog(c) & BasisOf(b,c) & Coborn(b,c))
# THEORY rejected_five_only_coborn
# EXPECT rejected_five_only_coborn F
all c.(FiveCog(c) -> all b.(BasisOf(b,c) -> Coborn(b,c)))
# THEORY rejected_five_past_condition
# EXPECT rejected_five_past_condition F
exists c.exists v.(FiveCog(c) & CondOf(v,c) & Past(v))
# THEORY rejected_basis_is_samanantara
# EXPECT rejected_basis_is_samanantara F
all x.all c.(BasisOf(x,c) <-> Samanantara(x,c))
```

```nltk-valuation
nose => nose_f
tongue => tongue_f
body => body_f
eye => eye_f
ear => ear_f
mind => mind_f
pastmind => pastmind_b
pastmental => pastmental_d
mc => mano_c
ec => eye_c
Faculty => {eye_f,ear_f,nose_f,tongue_f,body_f,mind_f}
Rupin => {eye_f,ear_f,nose_f,tongue_f,body_f}
EqualGrasp => {nose_f,tongue_f,body_f}
GraspBy => {(eye_f,g_hair),(eye_f,g_grape),(eye_f,g_mountain),(ear_f,g_mosquito),(ear_f,g_thunder),(nose_f,g_nose),(tongue_f,g_tongue),(body_f,g_body),(mind_f,g_mind)}
EqualAtoms => {g_grape,g_nose,g_tongue,g_body}
FewerAtoms => {g_hair,g_mosquito}
MoreAtoms => {g_mountain,g_thunder}
Measured => {g_hair,g_grape,g_mountain,g_mosquito,g_thunder,g_nose,g_tongue,g_body}
Accumulated => {g_hair,g_grape,g_mountain,g_mosquito,g_thunder,g_nose,g_tongue,g_body}
AllAtoms => {}
MindCog => {mano_c}
FiveCog => {eye_c,body_c}
BasisOf => {(eye_f,eye_c),(pastmind_b,eye_c),(body_f,body_c),(pastmind_b,body_c),(pastmind_b,mano_c)}
Coborn => {(eye_f,eye_c),(body_f,body_c)}
Samanantara => {(pastmind_b,eye_c),(pastmental_d,eye_c),(pastmind_b,body_c),(pastmental_d,body_c),(pastmind_b,mano_c),(pastmental_d,mano_c)}
Past => {pastmind_b,pastmental_d,v_past}
Present => {v_present,v_touch}
Future => {v_future}
CondOf => {(v_present,eye_c),(v_touch,body_c),(v_past,mano_c),(v_present,mano_c),(v_future,mano_c)}
```

**Model checks.** The verse formula holds. Equal grasp is defined per
Faculty: every grasp it makes meets as many Condition-atoms as
Faculty-atoms.
- The eye sees a hair-tip with fewer atoms, a grape with equal, a mountain with more. The ear hears a mosquito and thunder. Neither is held to the count.
- Mind is not Form, and no grasp of it has a measure.
- Every grasp of a Faculty with Form meets an accumulation; the body never works with all its atoms.
- The Condition of the five is present. The Condition of Mind-Cognition is past, present, or future.
- For Eye-Cognition the four alternatives are all filled: the eye is Basis only, the past mental Dharma Principle is immediately preceding Condition only, past Mind is both, and a present Condition is neither.
- For Mind-Cognition every Basis is an immediately preceding Condition, but not conversely.
- All seven rejected theories are false.

**Bhāṣya determination.**
- *Yāvanto hīndriya-paramāṇavas tāvanto hi viṣaya-paramāṇavaḥ sametya vijñānaṃ janayanti*: as many Faculty-atoms, so many Condition-atoms come together and produce Cognition.
- *Cakṣuḥ-śrotrābhyāṃ tv aniyamaḥ*: for eye and ear there is no rule.
- *Manas tv amūrtatvād eveti nāsya parimāṇa-paricchedaḥ saṃpradhāryate*: Mind is unformed, so no measure of it is considered.
- *Na caika indriya-paramāṇur viṣaya-paramāṇur vā vijñānaṃ janayati*: one Faculty-atom or one Condition-atom does not produce Cognition.
- *Mano-vijñāna-dhātoḥ samanantara-niruddhaṃ mana āśrayaḥ*: the Basis of the Mind-Cognition Principle is Mind that ceased immediately before.
- *Atītaś ceti ca-śabdaḥ*: the word "and" means "past as well."
- *Ete pañca vijñāna-kāyā indriya-dvayāśrayāḥ*: these five groups of Cognition have two Bases.
- *Catuṣ-koṭikaḥ … mano-vijñānasya pūrva-pādakaḥ*: four alternatives for the five; for Mind-Cognition, whatever is Basis is also immediately preceding Condition, but not conversely.

**Organon interpretation.** The Basis is the one moment of the Dhātu
Triadic Plane that is not timed with the Condition. The Condition of the
five is present; their Basis is present and past. Mind-Cognition stands on
the past alone, which is why its Condition can be of the three times. Equal
grasp is a count of atoms meeting in arising, not a size measured from
outside: the measure belongs to the arising of Cognition, and Mind, which
has no form, has none. That is the point Donald Hoffman presses against
materialist cognitive science. Smelling is a relation of arising, and its
measure is not the measure of the physical.

```text
equal
    nose, tongue, body
    atom for atom

no rule
    eye, ear
    fewer, equal, more

Basis of the last
    past

Basis of the five
    co-born
    and past

four
    eye: Basis only
    past mental Dharma Principle: Condition only
    past Mind: both
    the rest: neither

1.45 not opened
```

## 9. Interpretive Note

**Key-term evidence.** *Āśraya* enters as the Basis that is timed: past for Mind-Cognition, co-born and past for the five. The Bhāṣya separates it from *samanantara-pratyaya*, the immediately preceding Condition, by four alternatives, and from the Condition of Cognition by time (*viṣayo vartamānaḥ pañcānāṃ caramasya trikālaḥ*). Basis is therefore kept distinct from Support (*ālambana*) and from Condition (*viṣaya*, *pratyaya*).

**Translation note.** The Bhāṣya explains the claim as each of the three Faculties apprehending a Condition equal in extent to itself. It identifies the last Cognition as Mind-Cognition, based on the immediately past Mind; the five sensory Cognitions are based on that past Mind and on their co-arising Faculties. *Sahajaḥ* is rendered with its understood *āśrayaḥ*, and *ca* with the past Basis the Bhāṣya reads into it.

The hinge is the two Bases. The Condition of the five is present. Their Basis is not only present. The eye is co-born with the seeing. Mind that has just ceased is the other Basis. Mind-Cognition has only the past one.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_44 a vak:Karika ;
    vak:hasTopic vak:EqualGraspAndThePastBasis ;
    vak:belongsTo vak:Dhatunirdesa .

vak:NoseTongueBody vak:graspsEqual true .
vak:MindCognition vak:basis vak:ImmediatelyPastMind .
vak:FiveCognitions vak:basis vak:CobornFaculty, vak:PastMind .
```
