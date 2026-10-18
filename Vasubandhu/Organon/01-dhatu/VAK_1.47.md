# VAK_1.47 — The Ear, the Three, and Mind

## 1. Sanskrit (Devanāgarī)

```sanskrit
तथा श्रोत्रं त्रयाणां तु सर्वमेव स्वभूमिकम् ।
कायविज्ञानमधरस्वभूम्यनियतं मनः ॥ १.४७ ॥
```

## 2. Sanskrit (IAST)

```text
tathā śrotraṃ trayāṇāṃ tu sarvam eva svabhūmikam /
kāyavijñānam adharasvabhūmy aniyataṃ manaḥ // 1.47 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| tathā | adverb | likewise: the Eye's rule of 1.46, applied again |
| śrotram | śrotra; nominative neuter singular | the Ear |
| trayāṇām | tri; genitive plural | of the three: Nose, Tongue, Body |
| tu | particle | however: turns from the Ear to the three |
| sarvam | sarva; nominative neuter singular | everything: Faculty, Condition, and Cognition |
| eva | particle | only: no other plane |
| sva-bhūmikam | bahuvrīhi; nominative neuter singular | of its own plane: the plane of the body one is born in |
| kāya-vijñānam | tatpuruṣa; nominative neuter singular | Body-Cognition |
| adhara-sva-bhūmi | bahuvrīhi; nominative neuter singular | of a lower plane or its own |
| a-niyatam | past participle, negated; nominative neuter singular | not fixed |
| manaḥ | manas; nominative neuter singular | Mind |

The three are Nose, Tongue, and Body. The printed *adharasavabhūmi* is read
as *adhara-sva-bhūmi*. Every nominative is neuter singular, so agreement
does not separate the clauses; the particles and the order do.

**Grammar tokens.** Verse-order IAST with sandhi opened (`śrotraṃ` →
*śrotram*, `trayāṇāṃ` → *trayāṇām*, `adharasvabhūmy aniyataṃ` →
*adhara-sva-bhūmi a-niyatam*) and compound boundaries marked.

```text
# tokens: tathā śrotram trayāṇām tu sarvam eva sva-bhūmikam kāya-vijñānam adhara-sva-bhūmi a-niyatam manaḥ
```

## 4. Grammar

Three clauses. In the first, *tathā* is anaphoric. It carries the fixed
rule of 1.46 and applies it to whatever sense *śrotram* names: the Faculty
is not lower than the body, and neither the Condition nor the Cognition is
higher than the Faculty.

In the second, the Bhāṣya names the form: a general rule (*utsarga*), then
an exception (*apavāda*) begun to qualify it. The grammar builds that form
directly. The genitive plural *trayāṇām* (CNT=3, the three of 1.44) gives
the domain, *sarvam* the members, and *sva-bhūmikam* the predicate. The
following nominative, *kāya-vijñānam*, does not add a fourth member. It is
subtracted from the domain of *sarvam* and given its own predicate,
*adhara-sva-bhūmi*. The general rule thus holds only where the exception
does not.

In the third, *a-niyatam* is a predicate operator like *sarvataḥ* in 1.46.
Given the Mind as Faculty, it asserts that Mind is found on the body's
plane, above it, and below it.

```nltk-fcfg
% start S
# tokens: tathā śrotram trayāṇām tu sarvam eva sva-bhūmikam kāya-vijñānam adhara-sva-bhūmi a-niyatam manaḥ
S[SEM=<(?a & (?b & ?c))>] -> EAR[SEM=?a] THREE[SEM=?b] MIND[SEM=?c]
EAR[SEM=<?t(?h)>] -> TATHA[SEM=?t] SENSE[CASE=nom,SEM=?h]
THREE[SEM=<(all s x.((?g(s) & ?a(s,x) & -?k(s,x)) -> ?p(s,x)) & all s x.(?k(s,x) -> ?q(s,x)))>] -> GENP[CASE=gen,CNT=3,NUM=pl,SEM=?g] TU NOMN[GEN=?n,NUM=?m,SEM=?a] EVA PRED[GEN=?n,NUM=?m,SEM=?p] NOMN[GEN=?n,NUM=?m,SEM=?k] PRED[GEN=?n,NUM=?m,SEM=?q]
MIND[SEM=<?o(?f)>] -> ANI[GEN=?n,NUM=?m,SEM=?o] NOMN[GEN=?n,NUM=?m,SEM=?f]
TATHA[SEM=<\H.all s.(H(s) -> (all x y.((FacIn(s,x) & BodyIn(s,y)) -> -Below(x,y)) & all x y.((CondIn(s,x) & FacIn(s,y)) -> -Below(y,x)) & all x y.((CogIn(s,x) & FacIn(s,y)) -> -Below(y,x))))>] -> 'tathā'
SENSE[CASE=nom,SEM=<\s.Hearing(s)>] -> 'śrotram'
GENP[CASE=gen,CNT=3,NUM=pl,SEM=<\s.(Smelling(s) | Tasting(s) | Touching(s))>] -> 'trayāṇām'
TU -> 'tu'
EVA -> 'eva'
NOMN[GEN=n,NUM=sg,SEM=<\s x.(FacIn(s,x) | CondIn(s,x) | CogIn(s,x))>] -> 'sarvam'
PRED[GEN=n,NUM=sg,SEM=<\s x.exists b.(BodyIn(s,b) & Same(x,b))>] -> 'sva-bhūmikam'
NOMN[GEN=n,NUM=sg,SEM=<\s x.(Touching(s) & CogIn(s,x))>] -> 'kāya-vijñānam'
PRED[GEN=n,NUM=sg,SEM=<\s x.exists b.(BodyIn(s,b) & (Same(x,b) | Below(x,b)))>] -> 'adhara-sva-bhūmi'
ANI[GEN=n,NUM=sg,SEM=<\M.(exists s x y.(M(s,x) & BodyIn(s,y) & Same(x,y)) & exists s x y.(M(s,x) & BodyIn(s,y) & Below(y,x)) & exists s x y.(M(s,x) & BodyIn(s,y) & Below(x,y)))>] -> 'a-niyatam'
NOMN[GEN=n,NUM=sg,SEM=<\s x.(Thinking(s) & FacIn(s,x))>] -> 'manaḥ'
```

```nltk-dep
'tathā' -> 'śrotram'
'sva-bhūmikam' -> 'sarvam' | 'trayāṇām' | 'tu' | 'eva'
'adhara-sva-bhūmi' -> 'kāya-vijñānam'
'a-niyatam' -> 'manaḥ'
```

**Close construe.** Likewise the Ear. Of the three, however, everything is
of its own plane only; Body-Cognition is of a lower plane or its own. Mind
is not fixed.

"Own plane" is the plane of the body one is born in. The exception lowers
Body-Cognition and nothing else: the body and the Tangible stay.

## 5. Translation

### Literal Translation

> Likewise the Ear. Of the three, however, everything is of its own plane.
> Body-Cognition is of a lower plane or its own. Mind is not fixed.

### Bhāṣya-informed study translation

> The Ear follows the rule of the Eye. For the three beginning with the
> Nose, however, Faculty, Condition, and Cognition are all of their own
> plane, except that Body-Cognition is of a lower plane or its own. Mind is
> not fixed.

## 6. Philosophical Translation

The ear takes the eye's rule. Not lower than the body. Sound not higher than the ear. Cognition not higher than the ear. Relative to the Cognition, Sound is open. Relative to the body, both are open.

The three that reach do not take that freedom. Nose, tongue, and body: Faculty, Condition, and Cognition stay on their own plane. The exception is Body-Cognition. The body and the Tangible stay. The Cognition may drop. Own plane for one born in the Desire Realm or the first dhyāna. A lower plane for one born in the second or above.

Mind is the open one. Same plane as the body, or higher, or lower. A body of five planes does not fix the mind. Attainment and rebirth are where that is worked. Not here. The incidental discussion closes.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| tathā | likewise | the Ear follows the Eye |
| trayāṇām | of the three | Nose, Tongue, Body |
| svabhūmika | of its own plane | the general rule for the three |
| utsarga | general rule | everything of the three on its own plane |
| apavāda | exception | Body-Cognition |
| adhara-svabhūmi | lower or its own | not a higher plane |
| aniyata | not fixed | Mind |
| samāpatti | attainment | worked in its own chapter |

## 8. Logical Determination

**Kārikā, derived.**
- In every hearing, the Ear is not lower than the body, and neither the Sound nor the Ear-Cognition is higher than the Ear.
- In every smelling, tasting, and touching, every Faculty, Condition, and Cognition except Body-Cognition is of the body's plane. Body-Cognition is of the body's plane or lower.
- Mind as Faculty occurs on the body's plane, above it, and below it.

```nltk-sem
# derived by the section 4 parse
(all s.(Hearing(s) -> (all x y.((FacIn(s,x) & BodyIn(s,y)) -> -Below(x,y)) & all x y.((CondIn(s,x) & FacIn(s,y)) -> -Below(y,x)) & all x y.((CogIn(s,x) & FacIn(s,y)) -> -Below(y,x)))) & all s x.(((Smelling(s) | Tasting(s) | Touching(s)) & (FacIn(s,x) | CondIn(s,x) | CogIn(s,x)) & -(Touching(s) & CogIn(s,x))) -> exists b.(BodyIn(s,b) & Same(x,b))) & all s x.((Touching(s) & CogIn(s,x)) -> exists b.(BodyIn(s,b) & (Same(x,b) | Below(x,b)))) & exists s x y.(Thinking(s) & FacIn(s,x) & BodyIn(s,y) & Same(x,y)) & exists s x y.(Thinking(s) & FacIn(s,x) & BodyIn(s,y) & Below(y,x)) & exists s x y.(Thinking(s) & FacIn(s,x) & BodyIn(s,y) & Below(x,y)))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all s.(Hearing(s) -> (all x y.((FacIn(s,x) & BodyIn(s,y)) -> -Below(x,y)) & all x y.((CondIn(s,x) & FacIn(s,y)) -> -Below(y,x)) & all x y.((CogIn(s,x) & FacIn(s,y)) -> -Below(y,x)))) & all s x.(((Smelling(s) | Tasting(s) | Touching(s)) & (FacIn(s,x) | CondIn(s,x) | CogIn(s,x)) & -(Touching(s) & CogIn(s,x))) -> exists b.(BodyIn(s,b) & Same(x,b))) & all s x.((Touching(s) & CogIn(s,x)) -> exists b.(BodyIn(s,b) & (Same(x,b) | Below(x,b)))) & exists s x y.(Thinking(s) & FacIn(s,x) & BodyIn(s,y) & Same(x,y)) & exists s x y.(Thinking(s) & FacIn(s,x) & BodyIn(s,y) & Below(y,x)) & exists s x y.(Thinking(s) & FacIn(s,x) & BodyIn(s,y) & Below(x,y)))
# THEORY prose
# EXPECT prose T
all s.all x.((Touching(s) & (FacIn(s,x) | CondIn(s,x))) -> exists b.(BodyIn(s,b) & Same(x,b)))
exists s.exists c.exists b.(Touching(s) & CogIn(s,c) & BodyIn(s,b) & Below(c,b) & InPlane(b,dh2))
all s.all c.all b.((Touching(s) & CogIn(s,c) & BodyIn(s,b) & (InPlane(b,kama) | InPlane(b,dh1))) -> Same(c,b))
exists s.exists x.exists b.(Hearing(s) & FacIn(s,x) & BodyIn(s,b) & Below(b,x))
exists s.exists x.exists c.(Hearing(s) & FacIn(s,x) & InPlane(x,dh2) & CogIn(s,c) & InPlane(c,dh1))
# THEORY rejected_body_cognition_own_only
# EXPECT rejected_body_cognition_own_only F
all s.all c.all b.((Touching(s) & CogIn(s,c) & BodyIn(s,b)) -> Same(c,b))
# THEORY rejected_body_cognition_higher
# EXPECT rejected_body_cognition_higher F
exists s.exists c.exists b.(Touching(s) & CogIn(s,c) & BodyIn(s,b) & Below(b,c))
# THEORY rejected_tangible_lowered
# EXPECT rejected_tangible_lowered F
exists s.exists x.exists b.(Touching(s) & CondIn(s,x) & BodyIn(s,b) & -Same(x,b))
# THEORY rejected_odor_other_plane
# EXPECT rejected_odor_other_plane F
exists s.exists x.exists b.(Smelling(s) & (FacIn(s,x) | CondIn(s,x) | CogIn(s,x)) & BodyIn(s,b) & -Same(x,b))
# THEORY rejected_ear_below_body
# EXPECT rejected_ear_below_body F
exists s.exists x.exists b.(Hearing(s) & FacIn(s,x) & BodyIn(s,b) & Below(x,b))
# THEORY rejected_mind_fixed
# EXPECT rejected_mind_fixed F
all s.all x.all b.((Thinking(s) & FacIn(s,x) & BodyIn(s,b)) -> Same(x,b))
```

```nltk-valuation
kama => kama_p
dh1 => dh1_p
dh2 => dh2_p
dh3 => dh3_p
dh4 => dh4_p
Hearing => {h1,h2,h3}
Smelling => {m1}
Tasting => {t1}
Touching => {k1,k2,k3}
Thinking => {n1,n2,n3}
BodyIn => {(h1,body0),(h2,body0),(h3,body0),(m1,body0),(t1,body0),(k1,body0),(k2,body1),(k3,body2),(n1,body0),(n2,body0),(n3,body2)}
FacIn => {(h1,ear0),(h2,ear1),(h3,ear2),(m1,nose0),(t1,tongue0),(k1,body0),(k2,body1),(k3,body2),(n1,mind0),(n2,mind1),(n3,mind1)}
CondIn => {(h1,sound0),(h2,sound1),(h3,sound0),(m1,odor0),(t1,taste0),(k1,tang0),(k2,tang1),(k3,tang2)}
CogIn => {(h1,cog0),(h2,cog1),(h3,cog1),(m1,cog0),(t1,cog0),(k1,cog0),(k2,cog1),(k3,cog1)}
InPlane => {(body0,kama_p),(ear0,kama_p),(sound0,kama_p),(cog0,kama_p),(ear1,dh1_p),(sound1,dh1_p),(cog1,dh1_p),(ear2,dh2_p),(nose0,kama_p),(odor0,kama_p),(tongue0,kama_p),(taste0,kama_p),(tang0,kama_p),(body1,dh1_p),(tang1,dh1_p),(body2,dh2_p),(tang2,dh2_p),(mind0,kama_p),(mind1,dh1_p)}
Below => {(body0,ear1),(body0,sound1),(body0,cog1),(body0,ear2),(body0,body1),(body0,tang1),(body0,body2),(body0,tang2),(body0,mind1),(ear0,ear1),(ear0,sound1),(ear0,cog1),(ear0,ear2),(ear0,body1),(ear0,tang1),(ear0,body2),(ear0,tang2),(ear0,mind1),(sound0,ear1),(sound0,sound1),(sound0,cog1),(sound0,ear2),(sound0,body1),(sound0,tang1),(sound0,body2),(sound0,tang2),(sound0,mind1),(cog0,ear1),(cog0,sound1),(cog0,cog1),(cog0,ear2),(cog0,body1),(cog0,tang1),(cog0,body2),(cog0,tang2),(cog0,mind1),(ear1,ear2),(ear1,body2),(ear1,tang2),(sound1,ear2),(sound1,body2),(sound1,tang2),(cog1,ear2),(cog1,body2),(cog1,tang2),(nose0,ear1),(nose0,sound1),(nose0,cog1),(nose0,ear2),(nose0,body1),(nose0,tang1),(nose0,body2),(nose0,tang2),(nose0,mind1),(odor0,ear1),(odor0,sound1),(odor0,cog1),(odor0,ear2),(odor0,body1),(odor0,tang1),(odor0,body2),(odor0,tang2),(odor0,mind1),(tongue0,ear1),(tongue0,sound1),(tongue0,cog1),(tongue0,ear2),(tongue0,body1),(tongue0,tang1),(tongue0,body2),(tongue0,tang2),(tongue0,mind1),(taste0,ear1),(taste0,sound1),(taste0,cog1),(taste0,ear2),(taste0,body1),(taste0,tang1),(taste0,body2),(taste0,tang2),(taste0,mind1),(tang0,ear1),(tang0,sound1),(tang0,cog1),(tang0,ear2),(tang0,body1),(tang0,tang1),(tang0,body2),(tang0,tang2),(tang0,mind1),(body1,ear2),(body1,body2),(body1,tang2),(tang1,ear2),(tang1,body2),(tang1,tang2),(mind0,ear1),(mind0,sound1),(mind0,cog1),(mind0,ear2),(mind0,body1),(mind0,tang1),(mind0,body2),(mind0,tang2),(mind0,mind1),(mind1,ear2),(mind1,body2),(mind1,tang2)}
Same => {(body0,body0),(body0,ear0),(body0,sound0),(body0,cog0),(body0,nose0),(body0,odor0),(body0,tongue0),(body0,taste0),(body0,tang0),(body0,mind0),(ear0,body0),(ear0,ear0),(ear0,sound0),(ear0,cog0),(ear0,nose0),(ear0,odor0),(ear0,tongue0),(ear0,taste0),(ear0,tang0),(ear0,mind0),(sound0,body0),(sound0,ear0),(sound0,sound0),(sound0,cog0),(sound0,nose0),(sound0,odor0),(sound0,tongue0),(sound0,taste0),(sound0,tang0),(sound0,mind0),(cog0,body0),(cog0,ear0),(cog0,sound0),(cog0,cog0),(cog0,nose0),(cog0,odor0),(cog0,tongue0),(cog0,taste0),(cog0,tang0),(cog0,mind0),(ear1,ear1),(ear1,sound1),(ear1,cog1),(ear1,body1),(ear1,tang1),(ear1,mind1),(sound1,ear1),(sound1,sound1),(sound1,cog1),(sound1,body1),(sound1,tang1),(sound1,mind1),(cog1,ear1),(cog1,sound1),(cog1,cog1),(cog1,body1),(cog1,tang1),(cog1,mind1),(ear2,ear2),(ear2,body2),(ear2,tang2),(nose0,body0),(nose0,ear0),(nose0,sound0),(nose0,cog0),(nose0,nose0),(nose0,odor0),(nose0,tongue0),(nose0,taste0),(nose0,tang0),(nose0,mind0),(odor0,body0),(odor0,ear0),(odor0,sound0),(odor0,cog0),(odor0,nose0),(odor0,odor0),(odor0,tongue0),(odor0,taste0),(odor0,tang0),(odor0,mind0),(tongue0,body0),(tongue0,ear0),(tongue0,sound0),(tongue0,cog0),(tongue0,nose0),(tongue0,odor0),(tongue0,tongue0),(tongue0,taste0),(tongue0,tang0),(tongue0,mind0),(taste0,body0),(taste0,ear0),(taste0,sound0),(taste0,cog0),(taste0,nose0),(taste0,odor0),(taste0,tongue0),(taste0,taste0),(taste0,tang0),(taste0,mind0),(tang0,body0),(tang0,ear0),(tang0,sound0),(tang0,cog0),(tang0,nose0),(tang0,odor0),(tang0,tongue0),(tang0,taste0),(tang0,tang0),(tang0,mind0),(body1,ear1),(body1,sound1),(body1,cog1),(body1,body1),(body1,tang1),(body1,mind1),(tang1,ear1),(tang1,sound1),(tang1,cog1),(tang1,body1),(tang1,tang1),(tang1,mind1),(body2,ear2),(body2,body2),(body2,tang2),(tang2,ear2),(tang2,body2),(tang2,tang2),(mind0,body0),(mind0,ear0),(mind0,sound0),(mind0,cog0),(mind0,nose0),(mind0,odor0),(mind0,tongue0),(mind0,taste0),(mind0,tang0),(mind0,mind0),(mind1,ear1),(mind1,sound1),(mind1,cog1),(mind1,body1),(mind1,tang1),(mind1,mind1)}
```

**Model checks.** The verse formula holds over eleven situations:
- three hearings: a Desire-Realm ear, a first-dhyāna ear, and a second-dhyāna ear that hears by a first-dhyāna Cognition, all in a Desire-Realm body;
- a smelling and a tasting, both in the Desire Realm;
- three touchings, for beings born in the Desire Realm, the first dhyāna, and the second dhyāna;
- three thinkings: Mind on the body's plane, above it in attainment, and below it in a second-dhyāna body.

The second-dhyāna touching has body and Tangible on the second dhyāna and
Body-Cognition on the first. Nothing else in the three leaves the body's
plane. All six rejected theories are false.

**Bhāṣya determination.**
- *Ghrāṇa-jihvā-kāya-dhātūnāṃ kāya-viṣaya-vijñānāni svabhūmikāny eva*: for the Nose, Tongue, and Body Principles, the body, the Condition, and the Cognition are of their own plane only.
- *Ity utsarga-viśeṣeṇa kṛtvā punar viśeṣaṇārtham apavāda ārabhyate*: having made the general rule, an exception is begun to qualify it.
- *Kāyaḥ kāya-dhātuḥ spraṣṭavyaṃ ca svabhūmikāny eva nityaṃ bhavanti*: the body, the Body Principle, and the Tangible are always of their own plane.
- *Kāya-vijñānaṃ tu keṣāṃcit svabhūmikaṃ yathā kāma-dhātu-prathama-dhyānopapannānām / keṣāṃcid adhara-bhūmikaṃ yathā dvitīyādi-dhyānopapannānām*: Body-Cognition is of its own plane for those born in the Desire Realm or the first dhyāna, and of a lower plane for those born in the second dhyāna and above.
- *Kadācit … samāna-bhūmikaṃ mano bhavati kadācid ūrdhvādho-bhūmikam*: Mind is sometimes of the same plane, sometimes higher or lower.
- *Vistareṇa samāpatti-kośa-sthāne nirdiṣṭam*: it is explained in detail in the Samāpatti chapter.

**Organon interpretation.** The general rule and its exception are the form
of a Judgment that is being determined: the universal is stated, then a
particular is subtracted from it and given its own predicate. The three
that reach are a closed Combination. Faculty, Condition, and Cognition
stand together on the plane of the body. Body-Cognition is the one member
that can fall below the plane it serves. Mind is the open member, the one
not bound to the body's plane, and the Bhāṣya sends it to the Samāpatti
chapter. That is where Mind is gathered, and where *ekāgratā* has its
proper home.

```text
ear
    the Eye's rule

three
    own plane only

Body-Cognition
    own plane, or lower
    not higher

Mind
    not fixed

1.48 not opened
```

## 9. Interpretive Note

**Key-term evidence.** *Viṣaya* appears in *kāya-viṣaya-vijñānāni*: body, Condition, Cognition, the three members that the general rule holds on one plane. The Bhāṣya's own terms for the form of the verse are *utsarga* (general rule) and *apavāda* (exception).

**Translation note.** *Sarvam* is spelled out as Faculty, Condition, and Cognition, following *kāya-viṣaya-vijñānāni*. The exception is rendered with "except that", which makes the *utsarga*–*apavāda* form visible in English.

The hinge is the exception inside the general rule. The three stay. Body-Cognition may be lower. Mind is not held to a plane on this page.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_47 a vak:Karika ;
    vak:hasTopic vak:TheEarTheThreeAndMind ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Ear vak:follows vak:EyeRule .
vak:NoseTongueBody vak:plane vak:OwnPlane .
vak:BodyCognition vak:exceptionTo vak:OwnPlane .
vak:Mind vak:planeFixed false .
```
