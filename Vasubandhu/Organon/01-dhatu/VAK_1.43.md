# VAK_1.43 — Both Eyes, and the Unreached

## 1. Sanskrit (Devanāgarī)

```sanskrit
उभाभ्यामपि चक्षुर्भ्यां पश्यति व्यक्तदर्शनात् ।
चक्षुःश्रोत्रमनोऽप्राप्तविषयं त्रयमन्यथा ॥ १.४३ ॥
```

## 2. Sanskrit (IAST)

```text
ubhābhyām api cakṣurbhyāṃ paśyati vyaktadarśanāt /
cakṣuḥśrotramano 'prāptaviṣayaṃ trayam anyathā // 1.43 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| ubhābhyām | ubha; instrumental dual | with both |
| api | particle | too: one eye is not excluded |
| cakṣurbhyām | cakṣus; instrumental dual | with the two eyes |
| paśyati | √dṛś (paśya-), present active, third singular | one sees |
| vyakta-darśanāt | karmadhāraya; ablative singular | because the seeing is clearer: ablative of ground |
| cakṣuḥ-śrotra-manaḥ | samāhāra dvandva; nominative neuter singular | Eye, Ear, and Mind, taken as one set of three |
| a-prāpta-viṣayam | bahuvrīhi; nominative neuter singular | whose Condition is not reached |
| trayam | traya; nominative neuter singular | the triad: the other three of the six |
| anyathā | adverb | otherwise: the converse of the preceding predicate |

The collective dvandva is neuter singular, and so are its predicate and
*trayam*. The other three are Nose, Tongue, and Body. They reach their
Condition.

**Grammar tokens.** Verse-order IAST with sandhi opened (`cakṣurbhyāṃ` →
*cakṣurbhyām*, `cakṣuḥśrotramano 'prāptaviṣayaṃ` → *cakṣuḥ-śrotra-manaḥ
a-prāpta-viṣayam*) and compound boundaries marked.

```text
# tokens: ubhābhyām api cakṣurbhyām paśyati vyakta-darśanāt cakṣuḥ-śrotra-manaḥ a-prāpta-viṣayam trayam anyathā
```

## 4. Grammar

Two sentences. In the first, *ubhābhyām* and *cakṣurbhyām* agree as
instrumental duals: the instrument is the pair. *Api* makes the claim
inclusive. Some seeing is with both eyes, and seeing with one eye is not
denied. The ablative *vyakta-darśanāt* gives the ground: seeing with both is
clearer.

In the second, the collective dvandva counts three (CNT=3) and is neuter
singular. Its predicate *a-prāpta-viṣayam* agrees in gender and number.
*Trayam* must carry the same count: the six bases less the named three.
*Anyathā* is a predicate operator. It takes the preceding predicate and
returns its converse, so the grammar derives "reaches its Condition" for
the remaining three without a separate word.

```nltk-fcfg
% start S
# tokens: ubhābhyām api cakṣurbhyām paśyati vyakta-darśanāt cakṣuḥ-śrotra-manaḥ a-prāpta-viṣayam trayam anyathā
S[SEM=<(?a & ?b)>] -> BOTH[SEM=?a] REACH[SEM=?b]
BOTH[SEM=<(exists s.(?v(s) & ?i(s)) & exists s.(?v(s) & -?i(s)) & all s.((?v(s) & ?i(s)) -> ?g(s)))>] -> UBHA[CASE=ins,NUM=du] API INST[CASE=ins,NUM=du,SEM=?i] V[SEM=?v] ABL[SEM=?g]
REACH[SEM=<(all x.(?m(x) -> ?u(x)) & all x.((Basis(x) & -?m(x)) -> ?n(?u,x)))>] -> DV[CNT=?k,GEN=?g,NUM=?q,SEM=?m] PRED[GEN=?g,NUM=?q,SEM=?u] TRAYA[CNT=?k,GEN=?g,NUM=?q] ANY[SEM=?n]
UBHA[CASE=ins,NUM=du] -> 'ubhābhyām'
API -> 'api'
INST[CASE=ins,NUM=du,SEM=<\s.BothEyes(s)>] -> 'cakṣurbhyām'
V[SEM=<\s.Seeing(s)>] -> 'paśyati'
ABL[SEM=<\s.Clearer(s)>] -> 'vyakta-darśanāt'
DV[CNT=3,GEN=n,NUM=sg,SEM=<\x.((x = eye) | (x = ear) | (x = mind))>] -> 'cakṣuḥ-śrotra-manaḥ'
PRED[GEN=n,NUM=sg,SEM=<\x.TakesUnreached(x)>] -> 'a-prāpta-viṣayam'
TRAYA[CNT=3,GEN=n,NUM=sg] -> 'trayam'
ANY[SEM=<\P x.-P(x)>] -> 'anyathā'
```

```nltk-dep
'paśyati' -> 'cakṣurbhyām' | 'vyakta-darśanāt'
'cakṣurbhyām' -> 'ubhābhyām' | 'api'
'a-prāpta-viṣayam' -> 'cakṣuḥ-śrotra-manaḥ' | 'trayam'
'trayam' -> 'anyathā'
```

**Close construe.** One sees with both eyes too, because the seeing is
clearer. Eye, Ear, and Mind, as a set, have a Condition not reached; the
triad is otherwise.

A Faculty takes an unreached Condition when there is an interval between
them. "Reached" is the converse: arising without an interval
(*nirantarotpatti*), not a touch.

## 5. Translation

### Literal Translation

> One sees with both eyes too, because the seeing is clearer. Eye, Ear, and
> Mind do not reach their Condition. The three are otherwise.

### Bhāṣya-informed study translation

> One sees with both eyes as well, because the seeing is clearer. Eye, Ear,
> and Mind apprehend a Condition they do not reach; the other three—Nose,
> Tongue, and Body—apprehend a Condition they reach.

## 6. Philosophical Translation

No rule forces one eye. Both open, the seeing is cleaner. One open and one half-closed, a double moon. That is not the alteration of one eye alone, and Cognition does not break because a support breaks. Cognition is not stationed in a place.

Reached and unreached then divide the six. Eye, Ear, and Mind do not reach. A distant Visible Form is seen. The collyrium in the eye is not. A distant sound is heard. If they reached, the divine eye and ear would not arise here for those in dhyāna. The nose does not. Mind is not Form, so it cannot reach. Some give the ear both, because a sound inside the ear is heard. Nose, tongue, and body reach. The nose reaches because Odor is not grasped without the out-breath. Reaching is arising without an interval.

The atom dispute is the cost of that interval. The Kāśmīras say atoms do not touch. Whole contact would merge them. Partial contact would give them parts. A struck hand does not stick. A struck heap does not scatter, because a Wind Principle holds it. Without an interval means nothing between, not a touch. The Bhadanta position is the one to accept: they do not touch; where there is no interval, the designation is used. Assemblages are not a second thing beside the atoms.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| ubhābhyām api | with both too | no exclusive rule |
| vyakta-darśana | clearer seeing | both eyes open |
| aprāpta-viṣaya | whose Condition is not reached | Eye, Ear, Mind |
| prāpta-viṣaya | apprehends a Condition it reaches | Nose, Tongue, Body |
| prāpti | reaching | arising without an interval |
| nirantara | without an interval | nothing between |
| paramāṇu | atom | partless; does not touch |
| vāyu-dhātu | Wind Principle | holds the heap, or scatters it |
| spṛṣṭa-saṃjñā | the designation touching | used where there is no interval |

## 8. Logical Determination

**Kārikā, derived.** Some seeing is with both eyes and some is not, and
seeing with both is clearer. Eye, Ear, and Mind take an unreached
Condition. Every other basis does not.

```nltk-sem
# derived by the section 4 parse
(exists s.(Seeing(s) & BothEyes(s)) & exists s.(Seeing(s) & -BothEyes(s)) & all s.((Seeing(s) & BothEyes(s)) -> Clearer(s)) & all x.(((x = eye) | (x = ear) | (x = mind)) -> TakesUnreached(x)) & all x.((Basis(x) & -((x = eye) | (x = ear) | (x = mind))) -> -TakesUnreached(x)))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(exists s.(Seeing(s) & BothEyes(s)) & exists s.(Seeing(s) & -BothEyes(s)) & all s.((Seeing(s) & BothEyes(s)) -> Clearer(s)) & all x.(((x = eye) | (x = ear) | (x = mind)) -> TakesUnreached(x)) & all x.((Basis(x) & -((x = eye) | (x = ear) | (x = mind))) -> -TakesUnreached(x)))
# THEORY prose
# EXPECT prose T
all x.(Basis(x) -> (TakesUnreached(x) <-> exists v.(Takes(x,v) & -Nirantara(x,v))))
exists s.(HalfClosed(s) & DoubleMoon(s) & -BothEyes(s))
all c.(Cognition(c) -> -Located(c))
exists v.(v = distant_moon & Takes(eye,v) & -Nirantara(eye,v))
exists v.(v = collyrium & Nirantara(eye,v) & -Takes(eye,v))
exists v.(v = hidden_form & -Nirantara(eye,v) & -Takes(eye,v))
exists v.(v = distant_sound & Takes(ear,v) & -Nirantara(ear,v))
exists v.(v = other_realm_form & Takes(eye,v) & -Nirantara(eye,v))
exists m.(m = mind & -Rupin(m) & -exists v.Nirantara(m,v))
exists v.(v = coarising_odor & Nirantara(nose,v) & -Takes(nose,v))
all v.(Takes(nose,v) -> Breath(v))
all a.all b.((Atom(a) & Atom(b)) -> -Touch(a,b))
exists a.exists b.(Atom(a) & Atom(b) & Nirantara(a,b))
all a.all b.(DesignatedTouching(a,b) <-> Nirantara(a,b))
# THEORY reported_ear_both
# EXPECT reported_ear_both T
exists v.exists w.(Takes(ear,v) & Nirantara(ear,v) & Takes(ear,w) & -Nirantara(ear,w))
# THEORY rejected_one_eye_only
# EXPECT rejected_one_eye_only F
all s.(Seeing(s) -> -BothEyes(s))
# THEORY rejected_eye_reaches
# EXPECT rejected_eye_reaches F
all v.(Takes(eye,v) -> Nirantara(eye,v))
# THEORY rejected_every_unreached_seen
# EXPECT rejected_every_unreached_seen F
all v.((VisibleForm(v) & -Nirantara(eye,v)) -> Takes(eye,v))
# THEORY rejected_mind_reaches
# EXPECT rejected_mind_reaches F
exists v.Nirantara(mind,v)
# THEORY rejected_nose_unreached
# EXPECT rejected_nose_unreached F
exists v.(Takes(nose,v) & -Nirantara(nose,v))
# THEORY rejected_atoms_touch
# EXPECT rejected_atoms_touch F
exists a.exists b.(Atom(a) & Atom(b) & Touch(a,b))
# THEORY rejected_reaching_is_touching
# EXPECT rejected_reaching_is_touching F
all x.all v.(Nirantara(x,v) -> Touch(x,v))
```

```nltk-valuation
eye => eye_f
ear => ear_f
mind => mind_f
nose => nose_f
distant_moon => moon_v
collyrium => anjana_v
hidden_form => hidden_v
distant_sound => far_sound_v
other_realm_form => divya_v
coarising_odor => sahabhu_odor_v
Basis => {eye_f,ear_f,mind_f,nose_f,tongue_f,body_f}
Seeing => {s_both,s_one,s_half}
BothEyes => {s_both}
Clearer => {s_both}
HalfClosed => {s_half}
DoubleMoon => {s_half}
Cognition => {cog_c}
Located => {}
Rupin => {eye_f,ear_f,nose_f,tongue_f,body_f}
VisibleForm => {moon_v,anjana_v,hidden_v,divya_v}
TakesUnreached => {eye_f,ear_f,mind_f}
Takes => {(eye_f,moon_v),(eye_f,divya_v),(ear_f,far_sound_v),(ear_f,inner_sound_v),(mind_f,dharma_v),(nose_f,odor_v),(tongue_f,taste_v),(body_f,tangible_v)}
Nirantara => {(eye_f,anjana_v),(ear_f,inner_sound_v),(nose_f,odor_v),(nose_f,sahabhu_odor_v),(tongue_f,taste_v),(body_f,tangible_v),(atom_a,atom_b)}
Breath => {odor_v}
Atom => {atom_a,atom_b}
Touch => {}
DesignatedTouching => {(eye_f,anjana_v),(ear_f,inner_sound_v),(nose_f,odor_v),(nose_f,sahabhu_odor_v),(tongue_f,taste_v),(body_f,tangible_v),(atom_a,atom_b)}
```

**Model checks.** The verse formula holds. Unreached is defined per
Faculty: it takes at least one Condition across an interval.
- The eye sees the distant moon and, as the divine eye, a form of another Realm. It does not see the collyrium on it, and it does not see every unreached form.
- Mind is not Form and reaches nothing.
- The nose does not grasp the odor that arises with it, and grasps only on the breath.
- No two atoms touch, yet some have no interval between them; "touching" is the designation for exactly that.
- The reported view that the ear takes both reached and unreached sound is true in the model. It does not break the verse, because one unreached Condition is enough to place the ear with the eye and mind.
- All seven rejected theories are false.

**Bhāṣya determination.**
- *Dvayor vivṛtayoḥ pariśuddhataraṃ darśanaṃ bhavati*: with both eyes open the seeing is clearer.
- *Vijñānasya deśāpratiṣṭhitatvāt*: Cognition is not stationed in a place, so it does not break when one support breaks.
- *Manas tv arūpitvāt prāptum evāśaktam*: mind, being formless, cannot reach at all.
- *Keyaṃ prāptir nāma / nirantarotpattiḥ*: reaching is arising without an interval.
- *Nirantare tu spṛṣṭa-saṃjñeti bhadantaḥ … bhadanta-mataṃ caiṣṭavyam*: "touching" is the designation where there is no interval, and the Bhadanta's view is to be accepted.

**Organon interpretation.** Reaching is a relation of arising, not of
place. The Faculty and its Condition reach when nothing intervenes in
their arising. The triad of 1.38–1.42 here gets its distance relation, and
for Mind the distance is no distance at all, because Mind has no place.

```text
eyes
    one or both
    both cleaner
    half-closed gives a double moon

unreached
    eye, ear, mind

reached
    nose, tongue, body
    arising without an interval

atoms
    do not touch
    designation where there is no interval
    the Bhadanta position is accepted

1.44 not opened
```

## 9. Interpretive Note

**Key-term evidence.** *Viṣaya* enters in the compound *a-prāpta-viṣaya*: the Condition is what the Faculty takes, whether reached or not. The Bhāṣya defines reaching (*prāpti*) as arising without an interval (*nirantarotpatti*), so the relation between a Faculty and its Condition is a relation of arising, not of place. That supports the provisional rendering Condition over “object”: *viṣaya* is a moment in the arising of Cognition, not a thing located over against the Faculty.

**Translation note.** *Anyathā* is rendered by naming the three and their converse predicate; the verse gives no separate word for “reaching.”

The hinge is the interval. Reaching is arising with nothing between. That is not a touch of atoms. The designation touching is used where there is no interval. The position to accept is the Bhadanta's.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_43 a vak:Karika ;
    vak:hasTopic vak:BothEyesAndTheUnreached ;
    vak:belongsTo vak:Dhatunirdesa .

vak:EyeEarMind vak:reachesCondition false .
vak:NoseTongueBody vak:reachesCondition true .
vak:Atom vak:touches false .
```
