# VAK_1.33 — Without the Other Two

## 1. Sanskrit (Devanāgarī)

```sanskrit
निरूपणानुस्मरणविकल्पेनाविकल्पकाः ।
तौ प्रज्ञा मानसी व्यग्रा स्मृतिः सर्वैव मानसी ॥ १.३३ ॥
```

## 2. Sanskrit (IAST)

```text
nirūpaṇānusmaraṇavikalpenāvikalpakāḥ /
tau prajñā mānasī vyagrā smṛtiḥ sarvaiva mānasī // 1.33 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| nirūpaṇa-anusmaraṇa-vikalpena | dvandva inside tatpuruṣa; instrumental singular | in respect of examining and recollective vikalpa |
| avikalpakāḥ | a-vikalpaka, bahuvrīhi; nominative masculine plural | called without vikalpa |
| tau | tad; nominative masculine dual | those two: the examining and the recollective |
| prajñā | nominative feminine singular | prajñā |
| mānasī | mānasa; nominative feminine singular | mental: associated with Mind-Cognition |
| vyagrā | vy-agra; nominative feminine singular | unconcentrated |
| smṛtiḥ | nominative feminine singular | smṛti |
| sarvā | sarva; nominative feminine singular | all |
| eva | particle | just; all of it without restriction |

The understood subject is the five Cognition Principles of 1.32. The verse says nirūpaṇa. The commentary says abhinirūpaṇa. Both stay.

**Grammar tokens.** Verse-order IAST with sandhi opened
(`-vikalpenāvikalpakāḥ` → *-vikalpena avikalpakāḥ*, `sarvaiva` → *sarvā
eva*) and compound boundaries marked. *Mānasī* occurs twice, once in each
identification.

```text
# tokens: nirūpaṇa-anusmaraṇa-vikalpena avikalpakāḥ tau prajñā mānasī vyagrā smṛtiḥ sarvā eva mānasī
```

## 4. Grammar

Two sentences. The first has the five Cognition Principles of 1.32 as
understood subject: *avikalpakāḥ* is masculine plural, and the instrumental
compound restricts the negation to two kinds of vikalpa. The second
identifies the two: dual *tau* resumes them, and two feminine noun phrases
answer, each with agreeing adjectives. *Sarvā eva* removes the
concentration restriction that *vyagrā* imposes on the first.

```nltk-fcfg
% start S
# tokens: nirūpaṇa-anusmaraṇa-vikalpena avikalpakāḥ tau prajñā mānasī vyagrā smṛtiḥ sarvā eva mānasī
S[SEM=<(?neg & ?ident)>] -> NEG[SEM=?neg] IDENT[SEM=?ident]
NEG[SEM=<all x.(FiveCognition(x) -> (CalledAvikalpaka(x) & -exists p.(Possesses(x,p) & ?resp(p))))>] -> RESPECT[CASE=ins,SEM=?resp] AVIK[CASE=nom,NUM=pl,GEN=m]
IDENT[SEM=<(?a & ?b)>] -> TAU[NUM=dual] FIRST[SEM=?a] SECOND[SEM=?b]
FIRST[SEM=<all p.(Vikalpa(p,examining) <-> (?n(p) & ?m(p) & ?v(p)))>] -> HEADN[CASE=nom,NUM=sg,GEN=?g,SEM=?n] MENT[CASE=nom,NUM=sg,GEN=?g,SEM=?m] VY[CASE=nom,NUM=sg,GEN=?g,SEM=?v]
SECOND[SEM=<all p.(Vikalpa(p,recollective) <-> (?n(p) & ?m(p)))>] -> HEADN[CASE=nom,NUM=sg,GEN=?g,SEM=?n] ALLQ[CASE=nom,NUM=sg,GEN=?g] EVA MENT[CASE=nom,NUM=sg,GEN=?g,SEM=?m]
RESPECT[CASE=ins,SEM=<\p.(Vikalpa(p,examining) | Vikalpa(p,recollective))>] -> 'nirūpaṇa-anusmaraṇa-vikalpena'
AVIK[CASE=nom,NUM=pl,GEN=m] -> 'avikalpakāḥ'
TAU[NUM=dual] -> 'tau'
HEADN[CASE=nom,NUM=sg,GEN=f,SEM=<\p.Prajna(p)>] -> 'prajñā'
MENT[CASE=nom,NUM=sg,GEN=f,SEM=<\p.Mental(p)>] -> 'mānasī'
VY[CASE=nom,NUM=sg,GEN=f,SEM=<\p.Unconcentrated(p)>] -> 'vyagrā'
HEADN[CASE=nom,NUM=sg,GEN=f,SEM=<\p.Smrti(p)>] -> 'smṛtiḥ'
ALLQ[CASE=nom,NUM=sg,GEN=f] -> 'sarvā'
EVA -> 'eva'
```

```nltk-dep
'avikalpakāḥ' -> 'nirūpaṇa-anusmaraṇa-vikalpena'
'tau' -> 'prajñā' | 'smṛtiḥ'
'prajñā' -> 'mānasī' | 'vyagrā'
'smṛtiḥ' -> 'sarvā' | 'mānasī'
'sarvā' -> 'eva'
```

**Close construe.** [The five] are without vikalpa by examining and
recollective vikalpa. Those two are: mental prajñā, unconcentrated; smṛti,
all of it, mental.

The instrumental restricts the negation: the five lack only the examining
and the recollective. They keep the intrinsic kind, vitarka, which 1.32
gave them. The name *avikalpaka* is therefore by the missing two, as the
Bhāṣya's one-footed horse is called footless. Both identifications are
biconditionals: examining vikalpa is exactly unconcentrated mental prajñā;
recollective vikalpa is exactly mental smṛti, concentrated or not.

The instrumental restricts the negation. It does not deny the third kind.

## 5. Translation

### Literal Translation

> They are without vikalpa in respect of examining and recollective vikalpa.
> Those two are unconcentrated mental prajñā, and all mental smṛti.

### Bhāṣya-informed study translation

> The five sensory Cognition Principles lack examining and recollective
> discrimination. Those two are, respectively, unconcentrated mental
> discriminative comprehension and all mental mindfulness.

## 6. Philosophical Translation

The five are with the pair, and still called without vikalpa. The name covers two of the three. The one they have is vitarka, and that is the intrinsic kind. Examining is unconcentrated mental prajñā. Recollecting is all mental smṛti. Neither is a Cognition of the five.

The five do have prajñā and smṛti, as every Cognition does; theirs are not mental, so they are not vikalpa. What makes prajñā and smṛti vikalpa is association with Mind-Cognition.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| avikalpaka | without vikalpa | in respect of the other two |
| svabhāva-vikalpa | intrinsic vikalpa | vitarka |
| abhinirūpaṇa-vikalpa | examining vikalpa | unconcentrated mental prajñā |
| anusmaraṇa-vikalpa | recollective vikalpa | all mental smṛti |
| mānasī | mental | associated with Mind-Cognition |
| vyagrā | unconcentrated | asamāhitā |
| prajñā | prajñā | not science on this page |
| smṛti | smṛti | all of it that is mental |

## 8. Logical Determination

**Kārikā, derived.** The five Cognition Principles are called without
vikalpa and possess no examining or recollective vikalpa; examining
vikalpa is exactly unconcentrated mental prajñā; recollective vikalpa is
exactly mental smṛti.

```nltk-sem
# derived by the section 4 parse
(all x.(FiveCognition(x) -> (CalledAvikalpaka(x) & -exists p.(Possesses(x,p) & (Vikalpa(p,examining) | Vikalpa(p,recollective))))) & all p.(Vikalpa(p,examining) <-> (Prajna(p) & Mental(p) & Unconcentrated(p))) & all p.(Vikalpa(p,recollective) <-> (Smrti(p) & Mental(p))))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all x.(FiveCognition(x) -> (CalledAvikalpaka(x) & -exists p.(Possesses(x,p) & (Vikalpa(p,examining) | Vikalpa(p,recollective))))) & all p.(Vikalpa(p,examining) <-> (Prajna(p) & Mental(p) & Unconcentrated(p))) & all p.(Vikalpa(p,recollective) <-> (Smrti(p) & Mental(p))))
# THEORY prose
# EXPECT prose T
all p.all k.(Vikalpa(p,k) -> ((k = intrinsic) | (k = examining) | (k = recollective)))
all p.(Vikalpa(p,intrinsic) <-> Vitarka(p))
all x.(FiveCognition(x) -> exists p.(Possesses(x,p) & Vikalpa(p,intrinsic)))
all p.(Mental(p) <-> AssociatedWith(p,mind_cognition))
all p.(Vikalpa(p,recollective) -> (Concentrated(p) | Unconcentrated(p)))
exists p.(Vikalpa(p,recollective) & Concentrated(p)) & exists p.(Vikalpa(p,recollective) & Unconcentrated(p))
exists x.(FiveCognition(x) & exists p.(Possesses(x,p) & Prajna(p) & -Vikalpa(p,examining)))
exists h.(h = horse & OneFooted(h) & CalledFootless(h))
exists v.(v = vitarka & DeferredTo(v,caitasika_section))
# THEORY rejected_five_without_any_vikalpa
# EXPECT rejected_five_without_any_vikalpa F
exists x.(FiveCognition(x) & -exists p.(Possesses(x,p) & Vikalpa(p,intrinsic)))
# THEORY rejected_fourth_vikalpa
# EXPECT rejected_fourth_vikalpa F
exists p.exists k.(Vikalpa(p,k) & -(k = intrinsic) & -(k = examining) & -(k = recollective))
# THEORY rejected_concentrated_prajna_examines
# EXPECT rejected_concentrated_prajna_examines F
exists p.(Prajna(p) & Concentrated(p) & Vikalpa(p,examining))
# THEORY rejected_recollection_only_unconcentrated
# EXPECT rejected_recollection_only_unconcentrated F
all p.(Vikalpa(p,recollective) -> Unconcentrated(p))
# THEORY rejected_sense_prajna_examines
# EXPECT rejected_sense_prajna_examines F
exists p.(Prajna(p) & -Mental(p) & Vikalpa(p,examining))
# THEORY rejected_five_examine
# EXPECT rejected_five_examine F
exists x.exists p.(FiveCognition(x) & Possesses(x,p) & Vikalpa(p,examining))
```

```nltk-valuation
intrinsic => intrinsic_k
examining => examining_k
recollective => recollective_k
mind_cognition => manovijnana_d
vitarka => vitarka_i
caitasika_section => caitasika_ch2
horse => asva
FiveCognition => {caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d}
Possesses => {(caksurvijnana_d,vitarka_i),(caksurvijnana_d,prajna_sense),(caksurvijnana_d,smrti_sense),(srotravijnana_d,vitarka_i),(srotravijnana_d,prajna_sense),(srotravijnana_d,smrti_sense),(ghranavijnana_d,vitarka_i),(ghranavijnana_d,prajna_sense),(ghranavijnana_d,smrti_sense),(jihvavijnana_d,vitarka_i),(jihvavijnana_d,prajna_sense),(jihvavijnana_d,smrti_sense),(kayavijnana_d,vitarka_i),(kayavijnana_d,prajna_sense),(kayavijnana_d,smrti_sense)}
Vikalpa => {(vitarka_i,intrinsic_k),(prajna_vyagra,examining_k),(smrti_vyagra,recollective_k),(smrti_samahita,recollective_k)}
Vitarka => {vitarka_i}
Prajna => {prajna_sense,prajna_vyagra,prajna_samahita}
Smrti => {smrti_sense,smrti_vyagra,smrti_samahita}
Mental => {prajna_vyagra,prajna_samahita,smrti_vyagra,smrti_samahita}
AssociatedWith => {(prajna_vyagra,manovijnana_d),(prajna_samahita,manovijnana_d),(smrti_vyagra,manovijnana_d),(smrti_samahita,manovijnana_d)}
Unconcentrated => {prajna_vyagra,smrti_vyagra}
Concentrated => {prajna_samahita,smrti_samahita}
CalledAvikalpaka => {caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d}
OneFooted => {asva}
CalledFootless => {asva}
DeferredTo => {(vitarka_i,caitasika_ch2)}
```

**Model checks.** Vikalpa has exactly three kinds. The five Cognition
Principles possess vitarka (intrinsic vikalpa) and also prajñā and smṛti of
their own, which are not mental and so are not vikalpa. Mental prajñā is
examining only when unconcentrated; mental smṛti is recollective whether
concentrated or not. Giving one of the five an examining vikalpa, or making
concentrated prajñā examine, falsifies the theory.

**Bhāṣya determination.** The objection comes from 1.32: the five are with
vitarka and vicāra, so how are they without vikalpa? Vikalpa is threefold:
intrinsic, examining, recollective. The five have the intrinsic, which is
vitarka and is indicated later among the mental factors, and lack the other
two; so they are called without vikalpa, as a one-footed horse is called
footless. Mental means associated with Mind-Cognition; *vyagrā* means
unconcentrated.

**Organon interpretation.** The name is by privation, not by absence of
the whole kind. The five Cognitions construct (vitarka) but do not examine
or recollect; examining and recollecting are Mind-Cognition work. The
same mental factor, prajñā or smṛti, is vikalpa or not by its
association, so kind is again a relation, as it was in 1.32. 1.34 is not
opened. The earlier schematic follows.

```text
five Cognition Principles
    with vitarka and vicāra
    called without vikalpa
    because they lack the other two

three vikalpas
    intrinsic = vitarka
    examining = unconcentrated mental prajñā
    recollective = all mental smṛti

the horse
    one foot, called footless
    the name is by the missing two

1.34 not opened
```

## 9. Interpretive Note

**Translation note.** The Bhāṣya distinguishes intrinsic *vikalpa* (identified with *vitarka*) from examining and recollective discrimination, and compares the five Cognitions to a one-footed horse called footless.

The hinge is the instrumental. Without it, the five could not be with vitarka and without vikalpa. The horse is the commentary's own measure of the name.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_33 a vak:Karika ;
    vak:hasTopic vak:WithoutTheOtherTwo ;
    vak:belongsTo vak:Dhatunirdesa .

vak:FiveCognitionPrinciples vak:without
    vak:ExaminingVikalpa, vak:RecollectiveVikalpa .
vak:IntrinsicVikalpa vak:is vak:Vitarka .
vak:ExaminingVikalpa vak:is vak:UnconcentratedMentalPrajna .
vak:RecollectiveVikalpa vak:is vak:AllMentalSmrti .
```
