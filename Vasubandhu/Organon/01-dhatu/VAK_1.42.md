# VAK_1.42 — The Eye Sees

## 1. Sanskrit (Devanāgarī)

```sanskrit
चक्षुः पश्यति रूपाणि सभागं न तदाश्रितम् ।
विज्ञानं दृश्यते रूपं न किलान्तरितं यतः ॥ १.४२ ॥
```

## 2. Sanskrit (IAST)

```text
cakṣuḥ paśyati rūpāṇi sabhāgaṃ na tadāśritam /
vijñānaṃ dṛśyate rūpaṃ na kilāntaritaṃ yataḥ // 1.42 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| cakṣuḥ | cakṣus; nominative neuter singular | the eye: agent of seeing |
| paśyati | √dṛś (paśya-), present active, third singular | sees |
| rūpāṇi | rūpa; accusative neuter plural | Visible Forms: what is seen |
| sabhāgam | sa-bhāga; nominative neuter singular | that does its own work: restricts *cakṣuḥ* |
| na | negative particle | not |
| tat-āśritam | tatpuruṣa, past participle of ā-√śri; nominative neuter singular | supported by it: *tat* is the eye |
| vijñānam | vijñāna; nominative neuter singular | Cognition: the excluded agent |
| dṛśyate | √dṛś, present passive, third singular | is seen |
| rūpam | rūpa; nominative neuter singular | a Visible Form: subject of the passive |
| na | negative particle | not |
| kila | particle | it is said: reported, not endorsed |
| antaritam | antar-√i, past participle; nominative neuter singular | screened: behind a wall |
| yataḥ | ablative adverb | since: the ground of the exclusion |

*Vijñānam* is nominative, not accusative. With *na tat-āśritam* it names the
rival agent the verse excludes. *Kila* marks the reason as the Vaibhāṣika
report; the Bhāṣya's own Sautrāntika voice does not accept it.

**Grammar tokens.** Verse-order IAST with sandhi opened (`sabhāgaṃ` →
*sabhāgam*, `tadāśritam` → *tat-āśritam*, `kilāntaritaṃ` → *kila
antaritam*) and compound boundaries marked.

```text
# tokens: cakṣuḥ paśyati rūpāṇi sabhāgam na tat-āśritam vijñānam dṛśyate rūpam na kila antaritam yataḥ
```

## 4. Grammar

Two sentences on one root. The first is active: *cakṣuḥ paśyati rūpāṇi*.
The neuter singular *sabhāgam* agrees with *cakṣuḥ* and restricts it: only
the eye that does its own work is the agent. The negated phrase *na
tat-āśritam vijñānam* agrees in the same gender and number and names the
rival agent. *Tat* takes its reference from the subject, so the rival is
the Cognition supported by the eye.

The second sentence is passive, and the grammar requires that *dṛśyate*
have the same root as *paśyati*. The passive therefore does not introduce a
new predicate. It quantifies away the agent of the first relation: nothing
sees a screened Visible Form. *Kila* carries the feature EVID=reported, and
*yataḥ* makes the passive sentence the ground of the exclusion.

```nltk-fcfg
% start S
# tokens: cakṣuḥ paśyati rūpāṇi sabhāgam na tat-āśritam vijñānam dṛśyate rūpam na kila antaritam yataḥ
S[EVID=?ev,SEM=<(?a & ?g(?rel))>] -> ACT[ROOT=?rt,REL=?rel,SEM=?a] GROUND[ROOT=?rt,EVID=?ev,SEM=?g]
ACT[ROOT=?rt,REL=?rel,SEM=<(all a.((?s(a) & ?r(a)) -> exists v.(?o(v) & ?rel(a,v))) & all a.all v.(?rel(a,v) -> (?s(a) & ?r(a))) & all c.((?asr(?ref)(c) & ?n(c)) -> -exists v.?rel(c,v)))>] -> NP[CASE=nom,GEN=?g,NUM=?m,REF=?ref,SEM=?s] V[VOICE=act,ROOT=?rt,SEM=?rel] NP[CASE=acc,NUM=pl,SEM=?o] ADJ[GEN=?g,NUM=?m,SEM=?r] NA ASR[GEN=?g,NUM=?m,SEM=?asr] NP[CASE=nom,GEN=?g,NUM=?m,SEM=?n]
GROUND[ROOT=?rt,EVID=?ev,SEM=<\R.all v.((?o(v) & ?p(v)) -> -exists x.R(x,v))>] -> V[VOICE=pass,ROOT=?rt] NP[CASE=nom,NUM=sg,SEM=?o] NA KILA[EVID=?ev] PART[SEM=?p] YATAH
NP[CASE=nom,GEN=n,NUM=sg,REF=<eye>,SEM=<\a.InstanceOf(a,eye)>] -> 'cakṣuḥ'
V[VOICE=act,ROOT=drs,SEM=<\a v.Sees(a,v)>] -> 'paśyati'
NP[CASE=acc,NUM=pl,SEM=<\v.VisibleForm(v)>] -> 'rūpāṇi'
ADJ[GEN=n,NUM=sg,SEM=<\a.Sabhaga(a)>] -> 'sabhāgam'
NA -> 'na'
ASR[GEN=n,NUM=sg,SEM=<\r c.exists a.(InstanceOf(a,r) & SupportedBy(c,a))>] -> 'tat-āśritam'
NP[CASE=nom,GEN=n,NUM=sg,SEM=<\c.Cognition(c)>] -> 'vijñānam'
V[VOICE=pass,ROOT=drs] -> 'dṛśyate'
NP[CASE=nom,NUM=sg,SEM=<\v.VisibleForm(v)>] -> 'rūpam'
KILA[EVID=reported] -> 'kila'
PART[SEM=<\v.Screened(v)>] -> 'antaritam'
YATAH -> 'yataḥ'
```

```nltk-dep
'paśyati' -> 'cakṣuḥ' | 'rūpāṇi' | 'vijñānam' | 'dṛśyate'
'cakṣuḥ' -> 'sabhāgam'
'vijñānam' -> 'na' | 'tat-āśritam'
'dṛśyate' -> 'rūpam' | 'kila' | 'yataḥ'
'rūpam' -> 'antaritam'
'antaritam' -> 'na'
```

**Close construe.** The eye sees Visible Forms, the eye that does its own
work, not the Cognition supported by it; since, it is said, a screened
Visible Form is not seen.

The ground is a modus tollens left implicit. Cognition is unresistant, so a
wall would not stop it; if Cognition saw, the screened would be seen. The
screened is not seen, so Cognition does not see. The prose theory states
the missing premise.

## 5. Translation

### Literal Translation

> The eye sees Visible Forms, the one that does its own work; not the
> Cognition supported by it. For, it is said, a screened Visible Form is not
> seen.

### Bhāṣya-informed study translation

> The eye sees Visible Forms when it does its own work; the Cognition
> supported by it does not see, since, it is said, a Visible Form screened by
> a wall is not seen.

## 6. Philosophical Translation

The verse does not say that every eye sees. It says the sabhāga eye sees, and the Cognition supported by it does not. The reason is the wall. Cognition is unresistant. A wall would not stop it. If Cognition saw, the covered would be seen. The reply that Cognition simply does not arise toward the covered is turned: it does not arise because the eye, which is resistant, has no operation when screened, and Cognition proceeds to one Condition by means of that support.

Glass, cloud, film, crystal, and water do not make the eye a contact-Faculty. Where light is not blocked, Cognition arises. Where light is blocked, it does not. The covered is unseen because Cognition has not arisen, not because the eye cannot pass a screen.

The sūtras that put seeing on the eye are read as attribution. Mind is past when dharmas are cognized. The beds do not cry. The door is a name for seeing, or the sentence collapses into "seeing for the sake of seeing." The bell sees only as support of the sound. The world says "seen," not "cognized," when Eye-Cognition has arisen. The Vibhāṣā keeps both: reached by the eye, experienced by Eye-Cognition, called seen. Cognition cognizes by presence, as the sun makes the day.

The Sautrāntika refuses the agent. Depending on eye and visibles, visual Cognition arises. No one sees. Nothing is seen. Dharmas only, Ground and Grounded only, without activity. The attribution is for discourse. The Kāśmīra position does not take that refusal. The eye sees. Mind cognizes.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| sabhāga | does its own work | the eye with Cognition |
| tad-āśrita | supported by it | Eye-Cognition; not what sees |
| antarita | screened | the wall; light blocked |
| sapratigha | resistant | the eye |
| apratigha | unresistant | Cognition |
| prāpta-viṣaya | Condition-reacher | the Body Faculty; not the eye |
| upacāra | attribution | the beds cry; the eye sees |
| nirvyāpāra | without activity | the Sautrāntika refusal |
| siddhānta | established position | the eye sees; mind cognizes |

## 8. Logical Determination

**Kārikā, derived.**
- Every eye that does its own work sees some Visible Form.
- Whatever sees is an eye that does its own work.
- No Cognition supported by an eye sees.
- On the reported ground, nothing sees a screened Visible Form.

```nltk-sem
# derived by the section 4 parse
(all a.((InstanceOf(a,eye) & Sabhaga(a)) -> exists v.(VisibleForm(v) & Sees(a,v))) & all a v.(Sees(a,v) -> (InstanceOf(a,eye) & Sabhaga(a))) & all c.((exists a.(InstanceOf(a,eye) & SupportedBy(c,a)) & Cognition(c)) -> -exists v.Sees(c,v)) & all v.((VisibleForm(v) & Screened(v)) -> -exists x.Sees(x,v)))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all a.((InstanceOf(a,eye) & Sabhaga(a)) -> exists v.(VisibleForm(v) & Sees(a,v))) & all a v.(Sees(a,v) -> (InstanceOf(a,eye) & Sabhaga(a))) & all c.((exists a.(InstanceOf(a,eye) & SupportedBy(c,a)) & Cognition(c)) -> -exists v.Sees(c,v)) & all v.((VisibleForm(v) & Screened(v)) -> -exists x.Sees(x,v)))
# THEORY prose
# EXPECT prose T
all x.(Cognition(x) -> -Resistant(x))
all a.(InstanceOf(a,eye) -> Resistant(a))
all x.((exists v.Sees(x,v)) -> Resistant(x))
all v.(Screened(v) <-> (Covered(v) & LightBlocked(v)))
exists g.(g = glass_screened & Covered(g) & -LightBlocked(g) & exists a.Sees(a,g))
all a.all v.(Sees(a,v) -> exists c.(SupportedBy(c,a) & Experiences(c,v)))
all v.(Seen(v) <-> exists a.exists c.(Sees(a,v) & Experiences(c,v)))
exists a.(InstanceOf(a,eye) & -Sabhaga(a) & -exists v.Sees(a,v))
exists x.(x = body & ReachesByContact(x) & -exists y.(y = eye & ReachesByContact(y)))
all v.(Seen(v) -> -Cognized(v))
# THEORY rejected_every_eye_sees
# EXPECT rejected_every_eye_sees F
all a.(InstanceOf(a,eye) -> exists v.Sees(a,v))
# THEORY rejected_cognition_sees
# EXPECT rejected_cognition_sees F
exists c.exists v.(Cognition(c) & Sees(c,v))
# THEORY rejected_eye_reaches_by_contact
# EXPECT rejected_eye_reaches_by_contact F
exists x.(x = eye & ReachesByContact(x))
# THEORY rejected_any_cover_blocks
# EXPECT rejected_any_cover_blocks F
all v.(Covered(v) -> -exists a.Sees(a,v))
# THEORY rejected_eye_cognizes
# EXPECT rejected_eye_cognizes F
exists a.exists v.(InstanceOf(a,eye) & Experiences(a,v))
# THEORY sautrantika_no_agent
# EXPECT sautrantika_no_agent F
-exists x.exists v.Sees(x,v)
```

```nltk-valuation
eye => caksur_d
body => kaya_d
glass_screened => glass_v
InstanceOf => {(eye_a,caksur_d),(eye_b,caksur_d),(cog_a,caksurvijnana_d),(moon_v,rupa_d),(wall_v,rupa_d),(glass_v,rupa_d)}
Sees => {(eye_a,moon_v),(eye_a,glass_v)}
VisibleForm => {moon_v,wall_v,glass_v}
Sabhaga => {eye_a,cog_a}
SupportedBy => {(cog_a,eye_a)}
Cognition => {cog_a}
Resistant => {eye_a,eye_b,wall_v}
Screened => {wall_v}
Covered => {wall_v,glass_v}
LightBlocked => {wall_v}
Experiences => {(cog_a,moon_v),(cog_a,glass_v)}
Seen => {moon_v,glass_v}
Cognized => {}
ReachesByContact => {kaya_d}
```

**Model checks.** The verse formula holds.
- The eye that does its own work sees the moon and the glass-screened form. The *tat-sabhāga* eye sees nothing.
- The Cognition supported by the eye experiences what the eye sees but does not see.
- The wall is both a cover and a light-block, so the form behind it is screened and unseen.
- The glass covers without blocking light, so its form is seen. Being covered is therefore not the reason, and the eye is not a contact-reacher like the body.
- "Seen" is fixed as what the eye reaches and the Cognition experiences, as the Vibhāṣā has it. The world says "seen", not "cognized".
- All five rejected theories are false.

The Sautrāntika theory is also false here, because this model is the Kāśmīra one. *Kila* in the verse marks that the author does not commit to it.

**Bhāṣya determination.**
- *Na vai sarvaṃ cakṣuḥ paśyati … sa-vijñānakaṃ yadā bhavati tadā paśyati*: not every eye sees, only the eye that is with Cognition.
- *Yatrālokasyāpratibandha āvṛte 'pi rūpe tatropapadyata eva cakṣur-vijñānam*: where light is not blocked, Eye-Cognition arises even toward a covered Visible Form.
- *Cakṣuḥ-saṃprāptaṃ cakṣur-vijñānānubhūtaṃ dṛṣṭam ity ucyate*: what the eye reaches and Eye-Cognition experiences is called seen.
- *Nirvyāpāraṃ hīdaṃ dharma-mātraṃ hetu-phala-mātraṃ ca*: the Sautrāntika answer is dharmas only, Ground and Grounded only, without activity.

**Organon interpretation.** The verse puts the agent on the Faculty-side Principle and the experience on Cognition. The Sautrāntika removes the agent and leaves Ground and Grounded. Both readings keep the same triad: eye, Visible Form, Eye-Cognition. They differ only on whether the copula *sees* has a subject. In the grammar that is the voice alternation:
- the active gives the relation an agent;
- the passive quantifies the agent away.

```text
eye sees
    sabhāga only
    not the supported Cognition

reason
    a screened Visible Form is not seen
    Cognition is unresistant

screen
    not contact
    light blocked or not

attribution
    by the support
    the beds cry

Sautrāntika
    no agent
    dharmas only
    Ground and Grounded only

Kāśmīra
    the eye sees
    mind cognizes

1.43 not opened
```

## 9. Interpretive Note

**Key-term evidence.** *Tat-āśrita* is the participle of *āśraya*. The eye is the support of Eye-Cognition, and the Bhāṣya gives the reason Cognition fails to arise behind a wall: *āśrayeṇaika-viṣaya-pravṛttatvāt*, because it proceeds to one Condition by means of its Basis. Basis (*āśraya*), Condition (*viṣaya*), and Cognition form the triad of 1.38–1.39, here with the agent placed on the Basis. The Sautrāntika phrase *hetu-phala-mātram* is rendered Ground and Grounded only.

**Translation note.** The Bhāṣya explains *sabhāga* as exercising the Faculty’s own function and develops the intervening-screen argument. It preserves both the position that the Eye sees and the Sautrāntika view that Cognition sees; its closing account is the Kāśmīra position.

The hinge is the wall. If Cognition saw, resistance would not matter. The established sentence keeps the seeing on the eye that does its own work. The Sautrāntika sentence withdraws the agent. Both are on the page. The position recorded at the close is the Kāśmīra one.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_42 a vak:Karika ;
    vak:hasTopic vak:TheEyeSees ;
    vak:belongsTo vak:Dhatunirdesa .

vak:SabhagaEye vak:sees vak:VisibleForm .
vak:SupportedCognition vak:sees false .
vak:KashmiraPosition vak:holds "the eye sees; mind cognizes" .
```
