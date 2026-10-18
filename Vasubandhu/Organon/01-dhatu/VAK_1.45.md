# VAK_1.45 — Named by the Basis

## 1. Sanskrit (Devanāgarī)

```sanskrit
तद्विकारविकारित्वादाश्रयाश्चक्षुरादयः ।
अतोऽसाधारणत्वाद्धि विज्ञानं तैर्निरुच्यते ॥ १.४५ ॥
```

## 2. Sanskrit (IAST)

```text
tadvikāravikāritvād āśrayāś cakṣurādayaḥ /
ato 'sādhāraṇatvād dhi vijñānaṃ tair nirucyate // 1.45 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| tad-vikāra-vikāritvāt | tatpuruṣa with abstract *-tva*; ablative singular | because of being altered by their alteration: ground of the Basis |
| āśrayāḥ | āśraya; nominative masculine plural | Bases |
| cakṣuḥ-ādayaḥ | bahuvrīhi; nominative masculine plural | the Eye and the rest |
| ataḥ | adverb from *idam*, ablative force | from this: from their being Bases |
| a-sādhāraṇatvāt | abstract noun; ablative singular | because of not being in common: ground of the name |
| hi | particle | for: the reason is stated |
| vijñānam | vijñāna; nominative neuter singular | Cognition |
| taiḥ | tad; instrumental plural | by them: the Eye and the rest |
| nirucyate | nir-√vac, present passive, third singular | is designated |

Two ablatives give two grounds. The first makes the Eye and the rest
Bases. The second, with *ataḥ*, takes that result and adds the ground of
the name. *Taiḥ* is plural because it points back to *cakṣuḥ-ādayaḥ*.

**Grammar tokens.** Verse-order IAST with sandhi opened
(`tadvikāravikāritvād āśrayāś cakṣurādayaḥ` → *tad-vikāra-vikāritvāt
āśrayāḥ cakṣuḥ-ādayaḥ*, `ato 'sādhāraṇatvād dhi` → *ataḥ a-sādhāraṇatvāt
hi*, `vijñānaṃ tair` → *vijñānam taiḥ*) and compound boundaries marked.

```text
# tokens: tad-vikāra-vikāritvāt āśrayāḥ cakṣuḥ-ādayaḥ ataḥ a-sādhāraṇatvāt hi vijñānam taiḥ nirucyate
```

## 4. Grammar

Two sentences joined by *ataḥ*. In the first, *āśrayāḥ* and
*cakṣuḥ-ādayaḥ* agree as masculine plural nominatives: a predicate noun
and its subject with no verb. The ablative *tad-vikāra-vikāritvāt* is the
ground. *Tad* points to the Cognitions those Faculties are Bases of: each
such Cognition is altered when its Faculty is altered.

In the second, *vijñānam* is the subject of the passive *nirucyate*, and
*taiḥ* is the agent of the naming. Its number must match the plural of the
first sentence (NUM is shared across the two sentences), so the name is
taken from the Eye and the rest and from nothing else. *Ataḥ* is not an
empty "therefore". It carries the Basis relation of the first sentence
into the second: Cognition is named by what is its Basis. The ablative
*a-sādhāraṇatvāt* adds the second ground: that Basis is not in common
with another Cognition.

```nltk-fcfg
% start S
# tokens: tad-vikāra-vikāritvāt āśrayāḥ cakṣuḥ-ādayaḥ ataḥ a-sādhāraṇatvāt hi vijñānam taiḥ nirucyate
S[SEM=<(?a & ?b)>] -> BASES[NUM=?q,SEM=?a] NAME[NUM=?q,SEM=?b]
BASES[NUM=?q,SEM=<all x.(?n(x) -> (?g(x) & ?b(x)))>] -> ABL[SEM=?g] ASR[CASE=nom,GEN=?k,NUM=?q,SEM=?b] NI[CASE=nom,GEN=?k,NUM=?q,SEM=?n]
NAME[NUM=?q,SEM=<all c.(?v(c) -> exists x.(?t(x) & ?a(x,c) & ?u(x) & ?r(c,x)))>] -> ATAH[SEM=?a] ABL2[SEM=?u] HI VIJ[CASE=nom,NUM=?s,SEM=?v] TAI[CASE=ins,NUM=?q,SEM=?t] V[VOICE=pass,NUM=?s,SEM=?r]
ABL[SEM=<\x.all p.(BasisOf(x,p) -> AltersWith(p,x))>] -> 'tad-vikāra-vikāritvāt'
ASR[CASE=nom,GEN=m,NUM=pl,SEM=<\x.exists k.BasisOf(x,k)>] -> 'āśrayāḥ'
NI[CASE=nom,GEN=m,NUM=pl,SEM=<\x.Faculty(x)>] -> 'cakṣuḥ-ādayaḥ'
ATAH[SEM=<\x y.BasisOf(x,y)>] -> 'ataḥ'
ABL2[SEM=<\x.all p.all q.((BasisOf(x,p) & BasisOf(x,q)) -> (p = q))>] -> 'a-sādhāraṇatvāt'
HI -> 'hi'
VIJ[CASE=nom,NUM=sg,SEM=<\c.Cognition(c)>] -> 'vijñānam'
TAI[CASE=ins,NUM=pl,SEM=<\x.Faculty(x)>] -> 'taiḥ'
V[VOICE=pass,NUM=sg,SEM=<\c x.NamedBy(c,x)>] -> 'nirucyate'
```

```nltk-dep
'āśrayāḥ' -> 'cakṣuḥ-ādayaḥ' | 'tad-vikāra-vikāritvāt'
'nirucyate' -> 'vijñānam' | 'taiḥ' | 'a-sādhāraṇatvāt' | 'ataḥ' | 'hi'
```

**Close construe.** Because of being altered by their alteration, the Eye
and the rest are Bases. From this, for they are not in common,
Cognition is designated by them.

Cognition arises dependent on both Basis and Support. The verse picks out
the Basis twice: once by alteration, once by not being in common.

## 5. Translation

### Literal Translation

> Because of being altered by their alteration, the Eye and the rest are
> Bases. Therefore, because they are not in common, Cognition is
> designated by them.

### Bhāṣya-informed study translation

> The Eye and the other Faculties are Bases, because Cognition is altered
> by their alteration. Therefore, because they are not shared, Cognition is
> designated by them.

## 6. Philosophical Translation

Both are required. Only one is the Basis. The cut is the alteration. Benefit and impairment of the eye, acuity and dullness, are followed by the Cognition. A change in the Visible Form is not followed in that way. The dependence on the eye is the stronger one. That is why it is the Basis.

The name follows the Basis, not the Support. Eye-Cognition, not Form-Cognition. The eye is not in common. It cannot be the Basis of another Cognition. A Visible Form can be the Support of Mind-Cognition and of another Eye-Cognition. The drum names the sound. The barley names the sprout. The Basis names the Cognition.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| vikāra | alteration | benefit, impairment, acuity, dullness |
| āśraya | Basis | the Eye and the rest |
| ālambana | Support | the Visible Form and the rest; shared |
| asādhāraṇa | not in common | the eye is the Basis of its own Cognition only |
| nirucyate | is designated | the name follows the Basis |
| bherī-śabda | drum-sound | the Basis names the product |
| yava-aṅkura | barley-sprout | the same |

## 8. Logical Determination

**Kārikā, derived.**
- Every Faculty is a Basis, and every Cognition it is the Basis of alters with it.
- Every Cognition is named by a Faculty that is its Basis and is the Basis of no other Cognition.

```nltk-sem
# derived by the section 4 parse
(all x.(Faculty(x) -> (all p.(BasisOf(x,p) -> AltersWith(p,x)) & exists k.BasisOf(x,k))) & all c.(Cognition(c) -> exists x.(Faculty(x) & BasisOf(x,c) & all p q.((BasisOf(x,p) & BasisOf(x,q)) -> (p = q)) & NamedBy(c,x))))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all x.(Faculty(x) -> (all p.(BasisOf(x,p) -> AltersWith(p,x)) & exists k.BasisOf(x,k))) & all c.(Cognition(c) -> exists x.(Faculty(x) & BasisOf(x,c) & all p q.((BasisOf(x,p) & BasisOf(x,q)) -> (p = q)) & NamedBy(c,x))))
# THEORY prose
# EXPECT prose T
all c.(Cognition(c) -> (exists x.BasisOf(x,c) & exists v.SupportOf(v,c)))
exists v.(v = blue & SupportOf(v,ec1) & -AltersWith(ec1,v))
exists x.(x = eye1 & Impaired(x) & AltersWith(ec1,x))
exists v.(v = blue & SupportOf(v,ec1) & SupportOf(v,ec2) & SupportOf(v,mc1))
all c.all v.(SupportOf(v,c) -> -NamedBy(c,v))
exists s.(s = drum_sound & NamedBy(s,drum))
exists s.(s = barley_sprout & NamedBy(s,barley))
# THEORY rejected_form_is_basis
# EXPECT rejected_form_is_basis F
exists v.exists c.(VisibleForm(v) & BasisOf(v,c))
# THEORY rejected_follows_support
# EXPECT rejected_follows_support F
all c.all v.(SupportOf(v,c) -> AltersWith(c,v))
# THEORY rejected_basis_alone
# EXPECT rejected_basis_alone F
exists c.(Cognition(c) & -exists v.SupportOf(v,c))
# THEORY rejected_eye_shared
# EXPECT rejected_eye_shared F
exists x.exists c.exists d.(Faculty(x) & BasisOf(x,c) & BasisOf(x,d) & -(c = d))
# THEORY rejected_support_unshared
# EXPECT rejected_support_unshared F
all v.(VisibleForm(v) -> all p.all q.((SupportOf(v,p) & SupportOf(v,q)) -> (p = q)))
# THEORY rejected_named_by_support
# EXPECT rejected_named_by_support F
exists c.exists v.(SupportOf(v,c) & NamedBy(c,v))
```

```nltk-valuation
blue => blue_v
eye1 => eye_a
ec1 => eyecog_a
ec2 => eyecog_b
mc1 => manocog_a
drum_sound => drum_sound_s
drum => drum_d
barley_sprout => sprout_s
barley => barley_d
Faculty => {eye_a,eye_b,body_a,mind_a}
VisibleForm => {blue_v}
Cognition => {eyecog_a,eyecog_b,bodycog_a,manocog_a}
BasisOf => {(eye_a,eyecog_a),(eye_b,eyecog_b),(body_a,bodycog_a),(mind_a,manocog_a)}
SupportOf => {(blue_v,eyecog_a),(blue_v,eyecog_b),(blue_v,manocog_a),(soft_v,bodycog_a)}
AltersWith => {(eyecog_a,eye_a),(eyecog_b,eye_b),(bodycog_a,body_a),(manocog_a,mind_a)}
Impaired => {eye_a}
NamedBy => {(eyecog_a,eye_a),(eyecog_b,eye_b),(bodycog_a,body_a),(manocog_a,mind_a),(drum_sound_s,drum_d),(sprout_s,barley_d)}
```

**Model checks.** The verse formula holds.
- Every Cognition has both a Basis and a Support.
- One blue is the Support of two persons' Eye-Cognitions and of a Mind-Cognition. The Eye-Cognition does not alter with it, but it does alter with an impaired eye.
- No Cognition is named by its Support. Drum-sound and barley-sprout are named by what they arise from.
- The Bhāṣya runs the argument "through the Body" (*evaṃ yāvat kāyaḥ*). The model keeps Mind at one Cognition and does not test its unsharedness further.
- All six rejected theories are false.

**Bhāṣya determination.**
- *Ubhayādhīnāyāṃ vijñānotpattau*: Cognition arises dependent on both.
- *Cakṣur-ādīnāṃ hi vikāreṇa tad-vijñānānāṃ vikāro bhavaty anugrahopaghāta-paṭu-mandatānuvidhānāt*: when the Eye and the rest are altered, their Cognitions are altered, following benefit, impairment, acuity, and dullness.
- *Na tu rūpādīnāṃ vikāreṇa tad-vikāraḥ*: there is no such alteration from an alteration of Visible Forms and the rest.
- *Na hi cakṣur anyasya vijñānasyāśrayī-bhavitum utsahate*: an eye cannot be the Basis of another Cognition.
- *Rūpaṃ tu mano-vijñānasyālambanī-bhavaty anya-cakṣur-vijñānasyāpi*: a Visible Form becomes the Support of Mind-Cognition and of another Eye-Cognition.
- *Yathā bherī-śabdo yava-aṅkuraḥ*: as drum-sound and barley-sprout.

**Organon interpretation.** The name is a Judgment. "Eye-Cognition" joins a
singular Cognition to the one moment of the Dhātu Triadic Plane that
belongs to it alone. The Support is the universal side: one blue for many
Cognitions. The Basis is the singular side. When the Fact of a Cognition
comes into existence, it is named by its Basis and not by its Support, and
that is the negative moment of the Judgment: this blue is not mine. The
Combination (*saṃyoga*) of Faculty and Condition is required for the
arising, but the Combination does not name itself. The Basis names it. The
Yogasūtra's *ekāgratā* is the converse case to watch for later: a
Combination held to one Support.

```text
both required
    Basis and Support

Basis
    the one whose alteration the Cognition follows

name
    from the Basis
    because the Basis is not in common

Support
    in common
    Mind-Cognition and another Eye-Cognition

1.46 not opened
```

## 9. Interpretive Note

**Key-term evidence.** *Āśraya* and *ālambana* are set against each other in one Bhāṣya sentence: the eye cannot become the Basis (*āśrayī-bhavitum*) of another Cognition, but a Visible Form becomes the Support (*ālambanī-bhavati*) of Mind-Cognition and of another Eye-Cognition. That fixes the two renderings: Basis is unshared and named; Support is shared and not named.

**Translation note.** The Bhāṣya says the Cognitions alter with changes in their Faculties, while an alteration of Visible Forms and the other Conditions does not similarly change them. Cognition depends on both a Faculty as Basis and a Visible Form as Support; the Support may be shared by more than one Cognition, while the Basis is specific.

The hinge is the name. The Support is shared. The Basis is not. Cognition is designated by the Basis that is not in common.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_45 a vak:Karika ;
    vak:hasTopic vak:NamedByTheBasis ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Eye vak:basisOf vak:EyeCognition .
vak:VisibleForm vak:supportOf vak:EyeCognition, vak:MindCognition .
vak:Cognition vak:namedBy vak:Basis .
```
