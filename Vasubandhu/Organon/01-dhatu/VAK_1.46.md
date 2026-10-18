# VAK_1.46 — Not Lower, Not Higher

## 1. Sanskrit (Devanāgarī)

```sanskrit
न कायस्याधरं चक्षुरूर्ध्वं रूपं न चक्षुषः ।
विज्ञानं चास्य रूपं तु कायस्योभे च सर्वतः ॥ १.४६ ॥
```

## 2. Sanskrit (IAST)

```text
na kāyasyādharaṃ cakṣur ūrdhvaṃ rūpaṃ na cakṣuṣaḥ /
vijñānaṃ cāsya rūpaṃ tu kāyasyobhe ca sarvataḥ // 1.46 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| na | negative particle | not: the fixed rule is stated negatively |
| kāyasya | kāya; genitive singular | than the Body: standard of comparison |
| adharam | adhara; nominative neuter singular | lower: of a lower plane |
| cakṣuḥ | cakṣus; nominative neuter singular | the Eye |
| ūrdhvam | ūrdhva; nominative neuter singular | higher: of a higher plane |
| rūpam | rūpa; nominative neuter singular | Visible Form |
| cakṣuṣaḥ | cakṣus; genitive singular | than the Eye |
| vijñānam ca | vijñāna; nominative neuter singular, with particle | and Cognition: takes the same predicate |
| asya | idam; genitive singular | of this: of the Eye-Cognition just named |
| tu | particle | but: turns from the fixed rule to the open cases |
| ubhe ca | ubha; nominative neuter dual, with particle | and both: Visible Form and Cognition |
| sarvataḥ | adverb | in every way: higher, lower, or the same |

Higher and lower are planes (*bhūmi*), not height. The planes are the
Desire Realm and the four dhyānas. The genitive gives the standard of the
comparison.

**Grammar tokens.** Verse-order IAST with sandhi opened
(`kāyasyādharaṃ cakṣur ūrdhvaṃ` → *kāyasya adharam cakṣuḥ ūrdhvam*,
`vijñānaṃ cāsya` → *vijñānam ca asya*, `kāyasyobhe` → *kāyasya ubhe*).

```text
# tokens: na kāyasya adharam cakṣuḥ ūrdhvam rūpam na cakṣuṣaḥ vijñānam ca asya rūpam tu kāyasya ubhe ca sarvataḥ
```

## 4. Grammar

Three clauses: two fixed rules and one open rule. Each fixed rule is a
negated comparison. A nominative is compared, through a comparative
adjective, with a genitive standard. The adjective agrees with the
nominative (neuter singular). Every member is said of one act of seeing,
so each word denotes a role in a seeing situation (`\s x.EyeIn(s,x)`), and
the comparison is between the planes of the members.

In the second rule, *vijñānam ca* has no predicate of its own. *Ca* makes
it take the comparative and the standard of *rūpam*: Cognition, too, is
not higher than the Eye. *Vijñānam* also gives the reference (REF=cog)
that the pronoun *asya* must match in the next clause.

The third clause turns with *tu*. *Sarvataḥ* is a relation operator. Given
two roles, it asserts all three alternatives: lower, higher, and the same.
It applies once to Visible Form against *asya*, and through the dual
*ubhe* twice against the Body: once for Visible Form, once for Cognition.

```nltk-fcfg
% start S
# tokens: na kāyasya adharam cakṣuḥ ūrdhvam rūpam na cakṣuṣaḥ vijñānam ca asya rūpam tu kāyasya ubhe ca sarvataḥ
S[SEM=<(?a & (?b & ?c))>] -> CL1[SEM=?a] CL2[REF=?r,SEM=?b] OPEN[REF=?r,SEM=?c]
CL1[SEM=<all s.all x.all y.((?n(s,x) & ?g(s,y)) -> -?a(x,y))>] -> NEG GENT[SEM=?g] ADJ[GEN=?k,NUM=?q,SEM=?a] NOM[GEN=?k,NUM=?q,REF=eye,SEM=?n]
CL2[REF=?r,SEM=<(all s.all x.all y.((?n(s,x) & ?g(s,y)) -> -?a(x,y)) & all s.all x.all y.((?m(s,x) & ?g(s,y)) -> -?a(x,y)))>] -> ADJ[GEN=?k,NUM=?q,SEM=?a] NOM[GEN=?k,NUM=?q,REF=form,SEM=?n] NEG GENT[SEM=?g] NOM[GEN=?k,NUM=?q,REF=?r,SEM=?m] CA
OPEN[REF=?r,SEM=<(?o(?f,?h) & ?u(?o,?b))>] -> ASYA[REF=?r,SEM=?h] NOM[REF=form,SEM=?f] TU GENT[SEM=?b] UBHE[NUM=du,SEM=?u] CA SARV[SEM=?o]
NEG -> 'na'
CA -> 'ca'
TU -> 'tu'
GENT[SEM=<\s y.BodyIn(s,y)>] -> 'kāyasya'
GENT[SEM=<\s y.EyeIn(s,y)>] -> 'cakṣuṣaḥ'
ADJ[GEN=n,NUM=sg,SEM=<\x y.Below(x,y)>] -> 'adharam'
ADJ[GEN=n,NUM=sg,SEM=<\x y.Below(y,x)>] -> 'ūrdhvam'
NOM[GEN=n,NUM=sg,REF=eye,SEM=<\s x.EyeIn(s,x)>] -> 'cakṣuḥ'
NOM[GEN=n,NUM=sg,REF=form,SEM=<\s x.FormIn(s,x)>] -> 'rūpam'
NOM[GEN=n,NUM=sg,REF=cog,SEM=<\s x.CogIn(s,x)>] -> 'vijñānam'
ASYA[REF=cog,SEM=<\s y.CogIn(s,y)>] -> 'asya'
UBHE[NUM=du,SEM=<\O B.(O(\s x.FormIn(s,x),B) & O(\s x.CogIn(s,x),B))>] -> 'ubhe'
SARV[SEM=<\X Y.(exists s x y.(X(s,x) & Y(s,y) & Below(x,y)) & exists s x y.(X(s,x) & Y(s,y) & Below(y,x)) & exists s x y.(X(s,x) & Y(s,y) & Same(x,y)))>] -> 'sarvataḥ'
```

```nltk-dep
'adharam' -> 'cakṣuḥ' | 'kāyasya' | 'na'
'ūrdhvam' -> 'rūpam' | 'cakṣuṣaḥ' | 'na' | 'vijñānam'
'vijñānam' -> 'ca'
'sarvataḥ' -> 'rūpam' | 'asya' | 'ubhe' | 'tu'
'ubhe' -> 'kāyasya' | 'ca'
```

**Close construe.** Not lower than the Body is the Eye. Higher, a Visible
Form is not, than the Eye; and Cognition. But of this, the Visible Form;
and of the Body, both, in every way.

The Bhāṣya reads *asya* as the Eye-Cognition just named
(*anantaroktasya cakṣur-vijñānasya*). The open clause does not say the
alternatives may occur. It says all three occur.

## 5. Translation

### Literal Translation

> The Eye is not lower than the Body. A Visible Form is not higher than the
> Eye, and Cognition too. But relative to this, a Visible Form; and
> relative to the Body, both, in every way.

### Bhāṣya-informed study translation

> The Eye is never of a lower plane than the Body. A Visible Form is never
> of a higher plane than the Eye, nor is Eye-Cognition. Relative to that
> Cognition, however, a Visible Form is of a higher, lower, or the same
> plane; and relative to the Body, so are both.

## 6. Philosophical Translation

The four are not locked to one plane. The rule is the lock that remains. The eye may stand with the body or above it. It does not stand below the body. A Visible Form may stand with the eye or below it. It does not stand above the eye. Cognition does not stand above the eye. Relative to the Cognition, the Visible Form is free: higher, lower, or the same. Relative to the body, both are free in the same three ways.

The range is narrower than the freedom. Body, eye, and Visible Form run through five planes, the Desire Realm through the fourth dhyāna. Eye-Cognition runs through two, the Desire Realm and the first dhyāna. A second-dhyāna eye still sees by a first-dhyāna Cognition. The open alternatives do not put Eye-Cognition in the second, third, or fourth.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| bhūmi | plane | the Desire Realm and the four dhyānas |
| adhara | lower | a lower plane, not a lower place |
| ūrdhva | higher | a higher plane |
| svabhūmika | of its own plane | the birth-plane, or the plane of the seer |
| kāma-dhātu | Desire Realm | the first of the five |
| dhyāna | dhyāna | four planes above the Desire Realm |
| sarvataḥ | in every way | higher, lower, or the same |
| niyama | fixed rule | the eye is not lower than the Body |

## 8. Logical Determination

**Kārikā, derived.**
- In every seeing, the Eye is not of a lower plane than the Body.
- The Visible Form and the Cognition are not of a higher plane than the Eye.
- Against the Cognition, the Visible Form occurs higher, lower, and the same. Against the Body, both occur higher, lower, and the same.

```nltk-sem
# derived by the section 4 parse
(all s x y.((EyeIn(s,x) & BodyIn(s,y)) -> -Below(x,y)) & all s x y.((FormIn(s,x) & EyeIn(s,y)) -> -Below(y,x)) & all s x y.((CogIn(s,x) & EyeIn(s,y)) -> -Below(y,x)) & exists s x y.(FormIn(s,x) & CogIn(s,y) & Below(x,y)) & exists s x y.(FormIn(s,x) & CogIn(s,y) & Below(y,x)) & exists s x y.(FormIn(s,x) & CogIn(s,y) & Same(x,y)) & exists s x y.(FormIn(s,x) & BodyIn(s,y) & Below(x,y)) & exists s x y.(FormIn(s,x) & BodyIn(s,y) & Below(y,x)) & exists s x y.(FormIn(s,x) & BodyIn(s,y) & Same(x,y)) & exists s x y.(CogIn(s,x) & BodyIn(s,y) & Below(x,y)) & exists s x y.(CogIn(s,x) & BodyIn(s,y) & Below(y,x)) & exists s x y.(CogIn(s,x) & BodyIn(s,y) & Same(x,y)))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all s x y.((EyeIn(s,x) & BodyIn(s,y)) -> -Below(x,y)) & all s x y.((FormIn(s,x) & EyeIn(s,y)) -> -Below(y,x)) & all s x y.((CogIn(s,x) & EyeIn(s,y)) -> -Below(y,x)) & exists s x y.(FormIn(s,x) & CogIn(s,y) & Below(x,y)) & exists s x y.(FormIn(s,x) & CogIn(s,y) & Below(y,x)) & exists s x y.(FormIn(s,x) & CogIn(s,y) & Same(x,y)) & exists s x y.(FormIn(s,x) & BodyIn(s,y) & Below(x,y)) & exists s x y.(FormIn(s,x) & BodyIn(s,y) & Below(y,x)) & exists s x y.(FormIn(s,x) & BodyIn(s,y) & Same(x,y)) & exists s x y.(CogIn(s,x) & BodyIn(s,y) & Below(x,y)) & exists s x y.(CogIn(s,x) & BodyIn(s,y) & Below(y,x)) & exists s x y.(CogIn(s,x) & BodyIn(s,y) & Same(x,y)))
# THEORY prose
# EXPECT prose T
all s.all c.(CogIn(s,c) -> (InPlane(c,kama) | InPlane(c,dh1)))
exists s.exists x.exists c.(EyeIn(s,x) & InPlane(x,dh2) & CogIn(s,c) & InPlane(c,dh1))
exists s.exists x.exists y.(EyeIn(s,x) & BodyIn(s,y) & Below(y,x))
exists s.exists x.(FormIn(s,x) & InPlane(x,dh4))
exists s.(BodyIn(s,kbody) & EyeIn(s,keye) & FormIn(s,kform) & CogIn(s,kcog) & InPlane(kcog,kama))
# THEORY rejected_one_plane
# EXPECT rejected_one_plane F
all s.all x.all y.((EyeIn(s,x) & CogIn(s,y)) -> Same(x,y))
# THEORY rejected_eye_below_body
# EXPECT rejected_eye_below_body F
exists s.exists x.exists y.(EyeIn(s,x) & BodyIn(s,y) & Below(x,y))
# THEORY rejected_higher_form_seen
# EXPECT rejected_higher_form_seen F
exists s.exists x.exists y.(FormIn(s,x) & EyeIn(s,y) & Below(y,x))
# THEORY rejected_cognition_above_eye
# EXPECT rejected_cognition_above_eye F
exists s.exists x.exists y.(CogIn(s,x) & EyeIn(s,y) & Below(y,x))
# THEORY rejected_cognition_in_second_dhyana
# EXPECT rejected_cognition_in_second_dhyana F
exists s.exists c.(CogIn(s,c) & InPlane(c,dh2))
# THEORY rejected_form_never_above_cognition
# EXPECT rejected_form_never_above_cognition F
all s.all x.all y.((FormIn(s,x) & CogIn(s,y)) -> -Below(y,x))
```

```nltk-valuation
kama => kama_p
dh1 => dh1_p
dh2 => dh2_p
dh3 => dh3_p
dh4 => dh4_p
kbody => body0
keye => eye0
kform => form0
kcog => cog0
BodyIn => {(s1,body0),(s3,body0),(s4,body0),(s5,body0),(s6,body1),(s7,body1),(s8,body2),(s9,body0)}
EyeIn => {(s1,eye0),(s3,eye2),(s4,eye2),(s5,eye2),(s6,eye1),(s7,eye1),(s8,eye2),(s9,eye4)}
FormIn => {(s1,form0),(s3,form0),(s4,form1),(s5,form2),(s6,form0),(s7,form1),(s8,form2),(s9,form4)}
CogIn => {(s1,cog0),(s3,cog1),(s4,cog1),(s5,cog1),(s6,cog1),(s7,cog1),(s8,cog1),(s9,cog1)}
InPlane => {(body0,kama_p),(eye0,kama_p),(form0,kama_p),(cog0,kama_p),(eye2,dh2_p),(cog1,dh1_p),(form1,dh1_p),(form2,dh2_p),(body1,dh1_p),(eye1,dh1_p),(body2,dh2_p),(eye4,dh4_p),(form4,dh4_p)}
Below => {(body0,eye2),(body0,cog1),(body0,form1),(body0,form2),(body0,body1),(body0,eye1),(body0,body2),(body0,eye4),(body0,form4),(eye0,eye2),(eye0,cog1),(eye0,form1),(eye0,form2),(eye0,body1),(eye0,eye1),(eye0,body2),(eye0,eye4),(eye0,form4),(form0,eye2),(form0,cog1),(form0,form1),(form0,form2),(form0,body1),(form0,eye1),(form0,body2),(form0,eye4),(form0,form4),(cog0,eye2),(cog0,cog1),(cog0,form1),(cog0,form2),(cog0,body1),(cog0,eye1),(cog0,body2),(cog0,eye4),(cog0,form4),(eye2,eye4),(eye2,form4),(cog1,eye2),(cog1,form2),(cog1,body2),(cog1,eye4),(cog1,form4),(form1,eye2),(form1,form2),(form1,body2),(form1,eye4),(form1,form4),(form2,eye4),(form2,form4),(body1,eye2),(body1,form2),(body1,body2),(body1,eye4),(body1,form4),(eye1,eye2),(eye1,form2),(eye1,body2),(eye1,eye4),(eye1,form4),(body2,eye4),(body2,form4)}
Same => {(body0,body0),(body0,eye0),(body0,form0),(body0,cog0),(eye0,body0),(eye0,eye0),(eye0,form0),(eye0,cog0),(form0,body0),(form0,eye0),(form0,form0),(form0,cog0),(cog0,body0),(cog0,eye0),(cog0,form0),(cog0,cog0),(eye2,eye2),(eye2,form2),(eye2,body2),(cog1,cog1),(cog1,form1),(cog1,body1),(cog1,eye1),(form1,cog1),(form1,form1),(form1,body1),(form1,eye1),(form2,eye2),(form2,form2),(form2,body2),(body1,cog1),(body1,form1),(body1,body1),(body1,eye1),(eye1,cog1),(eye1,form1),(eye1,body1),(eye1,eye1),(body2,eye2),(body2,form2),(body2,body2),(eye4,eye4),(eye4,form4),(form4,eye4),(form4,form4)}
```

**Model checks.** The verse formula holds over eight seeings taken from the
Bhāṣya's cases:
- a Desire-Realm being with its own eye (all one plane);
- the same being with a second-dhyāna eye seeing Desire-Realm, first-dhyāna, and second-dhyāna Visible Forms;
- a fourth-dhyāna eye seeing fourth-dhyāna Visible Forms;
- a first-dhyāna being seeing its own and lower Visible Forms;
- a second-dhyāna being with its own eye.

In every case Eye-Cognition is of the Desire Realm or the first dhyāna. A
second-dhyāna eye sees by a first-dhyāna Cognition, which puts the
Cognition below both the eye and, for a second-dhyāna being, the Body.
All six rejected theories are false.

**Bhāṣya determination.**
- *Sarveṣāṃ bhedaḥ*: there is difference in all of them.
- *Dvitīya-dhyāna-cakṣuṣā svāni rūpāṇi paśyataḥ kāya-rūpe svabhūmike cakṣus tad-bhūmikaṃ vijñānaṃ prathama-dhyāna-bhūmikam*: seeing his own Visible Forms by a second-dhyāna eye, body and Visible Form are of his own plane, the eye of that plane, the Cognition of the first dhyāna.
- *Ayaṃ tu niyamaḥ*: this, however, is the fixed rule.
- *Na hi kadācid ūrdhva-bhūmikaṃ rūpam adho-bhūmikenā cakṣuṣā draṣṭuṃ śakyate*: a Visible Form of a higher plane can never be seen by an eye of a lower plane.
- *Asyety anantaroktasya cakṣur-vijñānasya rūpaṃ sarvato viṣayaḥ ūrdhvam adhaḥ svabhūmau ca*: "of this" means of the Eye-Cognition just stated; the Visible Form is its Condition in every way, higher, lower, and of its own plane.
- *Kāyasya cobhe rūpa-vijñāne sarvato bhavataḥ*: and relative to the Body, both Visible Form and Cognition are in every way.

**Organon interpretation.** A seeing is a Combination (*saṃyoga*) of four
Principles that need not share a plane. A being of the Desire Realm can see
with a second-dhyāna eye. The eye is not of the body's world: "that is not
my beautiful house." What holds the Combination together is not one plane
but a fixed rule, and the rule is a pair of negative Judgments: not lower,
not higher. Here Samādhi transfers the Principle across planes. The eye is
raised, but the Cognition stays at the first dhyāna, which is as far as
Eye-Cognition reaches. The Fact of seeing comes into existence as a
Judgment whose terms are drawn from different Realms.

```text
eye
    not lower than the Body

Visible Form
    not higher than the eye

Cognition
    not higher than the eye
    two planes only

open
    Visible Form relative to Cognition
    both relative to the Body

1.47 not opened
```

## 9. Interpretive Note

**Key-term evidence.** *Viṣaya* appears in the Bhāṣya's gloss of the open clause: the Visible Form is the Condition (*viṣaya*) of Eye-Cognition "in every way", above, below, and on its own plane. The Condition is free of the plane of its Cognition; the fixed rule binds it only to the eye.

**Translation note.** *Asya* is rendered "that Cognition" with the Bhāṣya, and *sarvataḥ* is spelled out as higher, lower, or the same plane. Higher and lower translate plane (*bhūmi*), not position.

The hinge is the fixed rule after the cases. The cases differ. The eye does not go below the Body. The Visible Form does not go above the eye. Cognition does not go above the eye.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_46 a vak:Karika ;
    vak:hasTopic vak:NotLowerNotHigher ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Eye vak:notLowerThan vak:Body .
vak:VisibleForm vak:notHigherThan vak:Eye .
vak:EyeCognition vak:notHigherThan vak:Eye .
```
