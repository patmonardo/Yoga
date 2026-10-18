# VAK_1.48 — Two Cognitions, the Permanent, the Faculty

## 1. Sanskrit (Devanāgarī)

```sanskrit
पञ्च बाह्या द्विविज्ञेया नित्या धर्मा असंस्कृताः ।
धर्मार्धमिन्द्रियं ये च द्वादशाध्यात्मिकाः स्मृताः ॥ १.४८ ॥
```

## 2. Sanskrit (IAST)

```text
pañca bāhyā dvivijñeyā nityā dharmā asaṃskṛtāḥ /
dharmārdham indriyaṃ ye ca dvādaśādhyātmikāḥ smṛtāḥ // 1.48 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| pañca | pañcan; nominative | five |
| bāhyāḥ | bāhya; nominative masculine plural | external: the six outer of 1.39 less the Dharma Principle |
| dvi-vijñeyāḥ | dvigu with gerundive; nominative masculine plural | knowable by two Cognitions, and by no third |
| nityāḥ | nitya; nominative masculine plural | permanent: the predicate, placed first |
| dharmāḥ | dharma; nominative masculine plural | dharmas |
| a-saṃskṛtāḥ | past participle, negated; nominative masculine plural | unconditioned |
| dharma-ardham | tatpuruṣa; nominative neuter singular | a portion of the Dharma Principle |
| indriyam | indriya; nominative neuter singular | Faculty: predicate noun, keeps its own number |
| ye | yad; nominative masculine plural | those which |
| ca | particle | and: adds the twelve to the subject of *indriyam* |
| dvādaśa | dvādaśan; nominative | twelve |
| ādhyātmikāḥ | ādhyātmika; nominative masculine plural | internal: the twelve of 1.39 |
| smṛtāḥ | √smṛ, past passive participle; nominative masculine plural | taught: handed down as such |

The printed *divijñeyāḥ* is read as *dvi-vijñeyāḥ*. A portion (*ardha*) is
not a count of half. *Indriyam* stays neuter singular although one of its
subjects is plural: it names the class, not the members.

**Grammar tokens.** Verse-order IAST with sandhi opened (`bāhyā
dvivijñeyā nityā dharmā` → *bāhyāḥ dvi-vijñeyāḥ nityāḥ dharmāḥ*,
`dharmārdham` → *dharma-ardham*, `dvādaśādhyātmikāḥ` → *dvādaśa
ādhyātmikāḥ*) and compound boundaries marked.

```text
# tokens: pañca bāhyāḥ dvi-vijñeyāḥ nityāḥ dharmāḥ a-saṃskṛtāḥ dharma-ardham indriyam ye ca dvādaśa ādhyātmikāḥ smṛtāḥ
```

## 4. Grammar

Three clauses, each answering one of the Bhāṣya's questions: which is
known by which, which is permanent, which is Faculty.

In the first, the numeral *pañca* and *bāhyāḥ* share a count (CNT=5). The
predicate *dvi-vijñeyāḥ* is a numeric quantifier over Cognitions: there
are two distinct knowers, and every knower is one of them.

In the second, the predicate *nityāḥ* comes first. The subject is
*dharmāḥ a-saṃskṛtāḥ*, a noun with its agreeing participle (masculine
plural). The clause is a restricted universal: unconditioned dharmas are
permanent.

In the third, *dharma-ardham* is a partitive quantifier like the genitive
portion of 1.41. It asserts that some of the Dharma Principle is Faculty
and some is not. *Indriyam* agrees with it as neuter singular. The
relative *ye* is plural and opens the second subject. *Dvādaśa* and
*ādhyātmikāḥ* share CNT=12, the internal twelve of 1.39. *Ca* joins them
to *indriyam* as a second subject. *Smṛtāḥ* agrees with *ye* and marks
the class as taught (EVID=taught).

```nltk-fcfg
% start S
# tokens: pañca bāhyāḥ dvi-vijñeyāḥ nityāḥ dharmāḥ a-saṃskṛtāḥ dharma-ardham indriyam ye ca dvādaśa ādhyātmikāḥ smṛtāḥ
S[SEM=<(?a & (?b & ?c))>] -> KNOWN[SEM=?a] PERM[SEM=?b] FAC[SEM=?c]
KNOWN[SEM=<all x.(?n(x) -> ?p(x))>] -> NUMR[CNT=?k] ADJ[CNT=?k,GEN=?g,NUM=?m,SEM=?n] KPRED[GEN=?g,NUM=?m,SEM=?p]
PERM[SEM=<all x.((?n(x) & ?a(x)) -> ?p(x))>] -> PPRED[GEN=?g,NUM=?m,SEM=?p] NOUN[GEN=?g,NUM=?m,SEM=?n] PART[GEN=?g,NUM=?m,SEM=?a]
FAC[SEM=<(?q(?f) & all x.(?r(x) -> ?f(x)))>] -> PORT[GEN=?g,NUM=?s,SEM=?q] FPRED[GEN=?g,NUM=?s,SEM=?f] REL[NUM=?m] CA NUMR[CNT=?k] ADJ[CNT=?k,GEN=m,NUM=?m,SEM=?r] SMR[EVID=taught,NUM=?m]
NUMR[CNT=5] -> 'pañca'
NUMR[CNT=12] -> 'dvādaśa'
ADJ[CNT=5,GEN=m,NUM=pl,SEM=<\x.(Outer(x) & -(x = dharma))>] -> 'bāhyāḥ'
ADJ[CNT=12,GEN=m,NUM=pl,SEM=<\x.Inner(x)>] -> 'ādhyātmikāḥ'
KPRED[GEN=m,NUM=pl,SEM=<\x.exists c.exists d.(Knows(c,x) & Knows(d,x) & -(c = d) & all k.(Knows(k,x) -> ((k = c) | (k = d))))>] -> 'dvi-vijñeyāḥ'
PPRED[GEN=m,NUM=pl,SEM=<\x.Permanent(x)>] -> 'nityāḥ'
NOUN[GEN=m,NUM=pl,SEM=<\x.InstanceOf(x,dharma)>] -> 'dharmāḥ'
PART[GEN=m,NUM=pl,SEM=<\x.Unconditioned(x)>] -> 'a-saṃskṛtāḥ'
PORT[GEN=n,NUM=sg,SEM=<\P.(exists x.(InstanceOf(x,dharma) & P(x)) & exists x.(InstanceOf(x,dharma) & -P(x)))>] -> 'dharma-ardham'
FPRED[GEN=n,NUM=sg,SEM=<\x.Faculty(x)>] -> 'indriyam'
REL[NUM=pl] -> 'ye'
CA -> 'ca'
SMR[EVID=taught,NUM=pl] -> 'smṛtāḥ'
```

```nltk-dep
'dvi-vijñeyāḥ' -> 'bāhyāḥ'
'bāhyāḥ' -> 'pañca'
'nityāḥ' -> 'dharmāḥ'
'dharmāḥ' -> 'a-saṃskṛtāḥ'
'indriyam' -> 'dharma-ardham' | 'ye' | 'ca'
'ye' -> 'smṛtāḥ'
'smṛtāḥ' -> 'ādhyātmikāḥ'
'ādhyātmikāḥ' -> 'dvādaśa'
```

**Close construe.** The five external are knowable by two. Permanent are
the unconditioned dharmas. A portion of the Dharma Principle is Faculty,
and those twelve that are taught as internal.

The five external are the outer six of 1.39 without the Dharma Principle.
The twelve internal are the six Faculties and the six Cognitions.

## 5. Translation

### Literal Translation

> The five external are knowable by two. Permanent are the unconditioned
> dharmas. A portion of the Dharma is Faculty, and the twelve taught as
> internal.

### Bhāṣya-informed study translation

> The five external Principles are each knowable by two Cognitions.
> Unconditioned dharmas are permanent. A portion of the Dharma Principle is
> Faculty, and so are the twelve Principles taught as internal.

## 6. Philosophical Translation

The five external are known twice. They are experienced by their own Cognition, then known by Mind-Cognition. The remaining thirteen are not the Condition of the five. Mind-Cognition alone knows them.

No Principle is permanent as a whole. The permanent is a portion of the Dharma Principle, the unconditioned dharmas. The rest are impermanent.

Faculty is the handoff. A portion of the Dharma Principle, and the twelve internal. The five beginning with the eye keep their names. The seven Mind Principles are the one Mind Faculty. Female and male are a portion of the body. The five external, and the remaining portion of the Dharma Principle, are not Faculty. Twenty-two are stated. The Ābhidharmikas set Mind after life, because Mind takes a Support.

The chapter closes on that cut.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| bāhya | external | the five Conditions of the senses |
| dvi-vijñeya | knowable by two | own Cognition and Mind-Cognition |
| anubhūta | experienced | by the Cognition of its own sense |
| nitya | permanent | a portion only |
| asaṃskṛta | unconditioned | the permanent portion |
| dharma-ardha | a portion of the Dharma | not a count of half |
| adhyātmika | internal | the twelve |
| indriya | Faculty | the twenty-two of the sūtra |
| sālambana | takes a Support | why Mind is recited after life |

## 8. Logical Determination

**Kārikā, derived.**
- Each of the five external Principles is known by exactly two Cognitions.
- Every unconditioned dharma is permanent.
- Some of the Dharma Principle is Faculty and some is not; every internal Principle is Faculty.

```nltk-sem
# derived by the section 4 parse
(all x.((Outer(x) & -(x = dharma)) -> exists c d.(Knows(c,x) & Knows(d,x) & -(c = d) & all k.(Knows(k,x) -> ((k = c) | (k = d))))) & all x.((InstanceOf(x,dharma) & Unconditioned(x)) -> Permanent(x)) & exists x.(InstanceOf(x,dharma) & Faculty(x)) & exists x.(InstanceOf(x,dharma) & -Faculty(x)) & all x.(Inner(x) -> Faculty(x)))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all x.((Outer(x) & -(x = dharma)) -> exists c d.(Knows(c,x) & Knows(d,x) & -(c = d) & all k.(Knows(k,x) -> ((k = c) | (k = d))))) & all x.((InstanceOf(x,dharma) & Unconditioned(x)) -> Permanent(x)) & exists x.(InstanceOf(x,dharma) & Faculty(x)) & exists x.(InstanceOf(x,dharma) & -Faculty(x)) & all x.(Inner(x) -> Faculty(x)))
# THEORY prose
# EXPECT prose T
all x.((Principle(x) & -(Outer(x) & -(x = dharma))) -> all k.(Knows(k,x) -> (k = mcog)))
all x.(Principle(x) -> Knows(mcog,x))
all x.(Permanent(x) -> (Unconditioned(x) & InstanceOf(x,dharma)))
all p.(Principle(p) -> -Permanent(p))
all x.((Outer(x) & -(x = dharma)) -> -Faculty(x))
exists f.(f = female & InstanceOf(f,body) & Faculty(f))
exists m.(m = mind & Faculty(m) & TakesSupport(m))
exists l.(l = life & Faculty(l) & InstanceOf(l,dharma) & -TakesSupport(l))
# THEORY rejected_dharma_known_by_two
# EXPECT rejected_dharma_known_by_two F
exists c.exists d.(Knows(c,dharma) & Knows(d,dharma) & -(c = d))
# THEORY rejected_principle_permanent
# EXPECT rejected_principle_permanent F
exists p.(p = dharma & Permanent(p))
# THEORY rejected_conditioned_permanent
# EXPECT rejected_conditioned_permanent F
exists x.(Permanent(x) & -Unconditioned(x))
# THEORY rejected_all_dharma_faculty
# EXPECT rejected_all_dharma_faculty F
all x.(InstanceOf(x,dharma) -> Faculty(x))
# THEORY rejected_no_dharma_faculty
# EXPECT rejected_no_dharma_faculty F
all x.(InstanceOf(x,dharma) -> -Faculty(x))
# THEORY rejected_external_faculty
# EXPECT rejected_external_faculty F
exists x.(Outer(x) & -(x = dharma) & Faculty(x))
```

```nltk-valuation
dharma => dharma_d
body => body_d
mind => mind_d
mcog => mcog_d
female => female_f
life => life_f
Principle => {eye_d,ear_d,nose_d,tongue_d,body_d,mind_d,form_d,sound_d,odor_d,taste_d,tangible_d,dharma_d,ecog_d,scog_d,gcog_d,jcog_d,kcog_d,mcog_d}
Inner => {eye_d,ear_d,nose_d,tongue_d,body_d,mind_d,ecog_d,scog_d,gcog_d,jcog_d,kcog_d,mcog_d}
Outer => {form_d,sound_d,odor_d,taste_d,tangible_d,dharma_d}
Knows => {(ecog_d,form_d),(scog_d,sound_d),(gcog_d,odor_d),(jcog_d,taste_d),(kcog_d,tangible_d),(mcog_d,eye_d),(mcog_d,ear_d),(mcog_d,nose_d),(mcog_d,tongue_d),(mcog_d,body_d),(mcog_d,mind_d),(mcog_d,form_d),(mcog_d,sound_d),(mcog_d,odor_d),(mcog_d,taste_d),(mcog_d,tangible_d),(mcog_d,dharma_d),(mcog_d,ecog_d),(mcog_d,scog_d),(mcog_d,gcog_d),(mcog_d,jcog_d),(mcog_d,kcog_d),(mcog_d,mcog_d)}
InstanceOf => {(space_u,dharma_d),(pratisamkhya_u,dharma_d),(apratisamkhya_u,dharma_d),(life_f,dharma_d),(sukha_f,dharma_d),(sraddha_f,dharma_d),(samjna_x,dharma_d),(female_f,body_d),(male_f,body_d)}
Unconditioned => {space_u,pratisamkhya_u,apratisamkhya_u}
Permanent => {space_u,pratisamkhya_u,apratisamkhya_u}
Faculty => {eye_d,ear_d,nose_d,tongue_d,body_d,mind_d,ecog_d,scog_d,gcog_d,jcog_d,kcog_d,mcog_d,life_f,sukha_f,sraddha_f,female_f,male_f}
TakesSupport => {mind_d,ecog_d,scog_d,gcog_d,jcog_d,kcog_d,mcog_d}
```

**Model checks.** The verse formula holds.
- Each of the five external is known by its own Cognition and by Mind-Cognition, and by nothing else.
- The remaining thirteen, the Dharma Principle among them, are known by Mind-Cognition alone.
- Only the three unconditioned dharmas are permanent. No Principle as a whole is permanent.
- The Dharma Principle contains Faculties (life, pleasure, faith) and non-Faculties (the unconditioned, perception).
- Female and male are Faculties within the body.
- Mind takes a Support; life does not.
- All six rejected theories are false.

**Bhāṣya determination.**
- *Rūpa-śabda-gandha-rasa-spraṣṭavya-dhātavo yathā-saṃkhyaṃ cakṣuḥ-śrotra-ghrāṇa-jihvā-kāya-vijñānair anubhūtā mano-vijñānena vijñāyante*: the five are experienced by their own Cognitions and known by Mind-Cognition.
- *Śeṣās trayodaśa dhātavaḥ pañcānāṃ vijñāna-kāyānām aviṣayatvād ekena mano-vijñānena vijñeyāḥ*: the remaining thirteen, not being the Condition of the five, are knowable by Mind-Cognition alone.
- *Na kaścit sakalo 'sti nityo dhātuḥ*: no Principle is permanent in its entirety.
- *Tena dharma-dhātv-ekadeśo nityaḥ śeṣā anityāḥ*: so a portion of the Dharma Principle is permanent; the rest are impermanent.
- *Ābhidhārmikās tu … jīvitendriyānantaraṃ mana-indriyaṃ paṭhanti / sālambanatvāt*: the Ābhidharmikas recite the Mind Faculty after the life Faculty, because it takes a Support.
- *Śeṣāḥ pañca dhātavo dharma-dhātu-pradeśaś ca nendriyam iti siddham*: the remaining five Principles and a portion of the Dharma Principle are not Faculty.

**Organon interpretation.** The chapter ends where Experience becomes
Judgment. A Visible Form is first experienced (*anubhūta*) by
Eye-Cognition, then known (*vijñāyate*) by Mind-Cognition. The second
knowing is what lets the Fact be judged: Mind-Cognition re-combines every
Principle, including itself, and is the only knower of the thirteen that
the senses do not reach. Permanence enters only as a portion, the
unconditioned. Faculty is the handoff: the Combinations studied in this
chapter now pass, as powers, to the Indriya chapter, where Ground and
Condition are to be settled.

```text
known by two
    Visible Form, Sound, Odor, Taste, Tangible

known by one
    the remaining thirteen

permanent
    unconditioned dharmas
    a portion of the Dharma Principle

Faculty
    a portion of the Dharma Principle
    the twelve internal

not Faculty
    the five external
    the remaining portion

chapter complete
    2.01 not opened
```

## 9. Interpretive Note

**Key-term evidence.** *Viṣaya* appears in *aviṣayatvāt*: the thirteen are not the Condition of the five Cognitions. *Ālambana* appears in *sālambanatvāt*: Mind is recited after life because it takes a Support. The two terms stay apart even in the closing verse.

**Translation note.** The five are Visible Form, Sound, Odor, Taste, and Tangible, each knowable by its corresponding sensory Cognition and by Mind-Cognition. Only the unconditioned portion of the Dharma Principle is permanent. The Faculties within its portion and the twelve internal Principles are enumerated further in the Bhāṣya.

The hinge is the close. Two Cognitions for the five external. Permanence only as a portion. Faculty as a portion and the twelve internal. The Exposition of the Principles ends on that.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_48 a vak:Karika ;
    vak:hasTopic vak:TwoCognitionsThePermanentTheFaculty ;
    vak:belongsTo vak:Dhatunirdesa ;
    vak:closesChapter true .

vak:FiveExternal vak:knownBy vak:OwnCognition, vak:MindCognition .
vak:UnconditionedDharmas vak:permanent true .
vak:TwelveInternal vak:faculty true .
```
