# VAK_1.36 — The Outer Four

## 1. Sanskrit (Devanāgarī)

```sanskrit
छिनत्ति छिद्यते चैव बाह्यं धातुचतुष्टयम् ।
दह्यते तुलयत्येवं विवादो दग्धृतुल्ययोः ॥ १.३६ ॥
```

## 2. Sanskrit (IAST)

```text
chinatti chidyate caiva bāhyaṃ dhātucatuṣṭayam /
dahyate tulayaty evaṃ vivādo dagdhṛtulyayoḥ // 1.36 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| chinatti | √chid, present active 3rd singular | cuts |
| chidyate | √chid, present passive 3rd singular | is cut |
| ca eva | particles | and also: both voices of the one root |
| bāhyam | bāhya; nominative neuter singular | external |
| dhātu-catuṣṭayam | tatpuruṣa; nominative neuter singular | the tetrad of Principles: Visible Form, Odor, Taste, Tangible |
| dahyate | √dah, present passive 3rd singular | is burned |
| tulayati | √tul, causative-stem present active 3rd singular | weighs |
| evam | adverb | likewise: the same tetrad |
| vivādaḥ | vi-√vad; nominative masculine singular | a dispute |
| dagdhṛ-tulyayoḥ | dvandva; genitive dual | about the burner and the weighed |

*Dagdhṛ* is the agent noun of √dah; *tulya* is the gerundive of √tul. The
dispute therefore turns on the converse voices of the two settled verbs:
the tetrad is burned, but what burns is disputed; the tetrad weighs, but
what is weighed is disputed. The fire of the second position is the Fire
Principle, an Element Principle: an instance in the Tangible, not one of
the eighteen.

**Grammar tokens.** Verse-order IAST with sandhi opened (`caiva` → *ca
eva*, `bāhyaṃ` → *bāhyam*, `tulayaty evaṃ` → *tulayati evam*, `vivādo` →
*vivādaḥ*) and compound boundaries marked.

```text
# tokens: chinatti chidyate ca eva bāhyam dhātu-catuṣṭayam dahyate tulayati evam vivādaḥ dagdhṛ-tulyayoḥ
```

## 4. Grammar

Three clauses. The first predicates both voices of √chid of the external
tetrad, neuter singular. The second predicates √dah in the passive and
√tul in the active of the same tetrad, by *evam*. The third names the
dispute with a genitive dual of the two roots. The voice features carry
the hinge: the dvandva's first member must have the voice of *tulayati*
and its second the voice of *dahyate*, so the dispute asks exactly the
converse questions.

```nltk-fcfg
% start S
# tokens: chinatti chidyate ca eva bāhyam dhātu-catuṣṭayam dahyate tulayati evam vivādaḥ dagdhṛ-tulyayoḥ
S[SEM=<(?cut & ?bw & ?d)>] -> CUTCL[SEM=?cut] BWCL[VA=?a,VB=?b,SEM=?bw] DISP[VA=?b,VB=?a,SEM=?d]
CUTCL[SEM=<all x.(?t(x) -> (?p(x) & ?q(x)))>] -> V[ROOT=chid,VOICE=act,NUM=sg,SEM=?p] V[ROOT=chid,VOICE=pass,NUM=sg,SEM=?q] CA EVA BAHYA[GEN=n,NUM=sg] TETRAD[GEN=n,NUM=sg,CNT=4,SEM=?t]
BWCL[VA=?a,VB=?b,SEM=<all x.(OuterFour(x) -> (?p(x) & ?q(x)))>] -> V[ROOT=dah,VOICE=?a,NUM=sg,SEM=?p] V[ROOT=tul,VOICE=?b,NUM=sg,SEM=?q] EVAM
DISP[VA=?x,VB=?y,SEM=<(Dispute(?d) & About(?d,burner) & About(?d,weighed))>] -> VIVADA[SEM=?d] DVANDVA[CASE=gen,NUM=dual,V1=?x,V2=?y]
V[ROOT=chid,VOICE=act,NUM=sg,SEM=<\x.Cuts(x)>] -> 'chinatti'
V[ROOT=chid,VOICE=pass,NUM=sg,SEM=<\x.IsCut(x)>] -> 'chidyate'
V[ROOT=dah,VOICE=pass,NUM=sg,SEM=<\x.IsBurned(x)>] -> 'dahyate'
V[ROOT=tul,VOICE=act,NUM=sg,SEM=<\x.Weighs(x)>] -> 'tulayati'
CA -> 'ca'
EVA -> 'eva'
EVAM -> 'evam'
BAHYA[GEN=n,NUM=sg] -> 'bāhyam'
TETRAD[GEN=n,NUM=sg,CNT=4,SEM=<\x.OuterFour(x)>] -> 'dhātu-catuṣṭayam'
VIVADA[SEM=<dispute>] -> 'vivādaḥ'
DVANDVA[CASE=gen,NUM=dual,V1=act,V2=pass] -> 'dagdhṛ-tulyayoḥ'
```

```nltk-dep
'chinatti' -> 'dhātu-catuṣṭayam' | 'chidyate'
'chidyate' -> 'ca' | 'eva'
'dhātu-catuṣṭayam' -> 'bāhyam'
'dahyate' -> 'evam' | 'tulayati'
'vivādaḥ' -> 'dagdhṛ-tulyayoḥ'
```

**Close construe.** The external tetrad of Principles cuts and is also
cut. Likewise it is burned and weighs. There is a dispute about the
burner and the weighed.

The verse settles four roles of the tetrad: agent and patient of cutting,
patient of burning, agent of weighing. It leaves open the other two:
agent of burning, patient of weighing. The `VA`/`VB` swap in the grammar
is that complementarity; a dispute about "the burned and the weigher"
would not parse.

## 5. Translation

### Literal Translation

> The external tetrad of Principles cuts and is also cut. Likewise it is
> burned and it weighs. There is a dispute about the burner and the weighed.

### Bhāṣya-informed study translation

> The four external Principles—Visible Form, Odor, Taste, and Tangible—cut
> and are cut; they are burned and weigh. Whether this same fourfold group is
> also the burner and the weighed is disputed.

## 6. Philosophical Translation

The outer four do the work and undergo it. Visible Form, Odor, Taste, Tangible: axe and wood are names of that tetrad. Cutting is not a split of the Faculty. It is a divided arising of a connected stream. The Faculty does not become two. The severed limb is without it. Clarity keeps the Faculty from cutting, and from being burned, and from weighing. Sound is cut off, so it is not in the count.

The dispute is only about the burner and the weighed. One side keeps the four. The other names the Fire Principle, and heaviness. The fire is an Element Principle, an instance in the Tangible. It is not one of the eighteen.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| bāhya-dhātu-catuṣṭaya | external tetrad of Principles | Visible Form, Odor, Taste, Tangible |
| cheda | cutting | divided arising of a stream of clusters arising in connection |
| indriya | Faculty | not cut, does not cut |
| maṇi-prabhā | jewel-radiance | the clarity |
| śabda | Sound | cut off, so not burned or weighed |
| dagdhṛ | burner | agent noun of √dah: the disputed agent |
| tulya | the weighed | gerundive of √tul: the disputed patient |
| tejo-dhātu | Fire Principle | an Element Principle: the second position's burner, an instance in the Tangible |
| gurutva | heaviness | the second position's weighed; Element-dependent Tangible |

## 8. Logical Determination

**Kārikā, derived.** Every member of the external tetrad cuts and is cut,
is burned and weighs; and there is a dispute about the burner and the
weighed.

```nltk-sem
# derived by the section 4 parse
(all x.(OuterFour(x) -> (Cuts(x) & IsCut(x))) & all x.(OuterFour(x) -> (IsBurned(x) & Weighs(x))) & Dispute(dispute) & About(dispute,burner) & About(dispute,weighed))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all x.(OuterFour(x) -> (Cuts(x) & IsCut(x))) & all x.(OuterFour(x) -> (IsBurned(x) & Weighs(x))) & Dispute(dispute) & About(dispute,burner) & About(dispute,weighed))
# THEORY prose
# EXPECT prose T
all x.(OuterFour(x) <-> ((x = visible_form) | (x = odor) | (x = taste) | (x = tangible)))
all x.(AmongEighteen(x) -> ((Cuts(x) | IsCut(x) | IsBurned(x) | Weighs(x)) -> OuterFour(x)))
all x.(IsCut(x) -> ClusterStream(x))
all x.(SenseFaculty(x) -> (Clear(x) & -Cuts(x) & -IsCut(x) & -IsBurned(x) & -Weighs(x)))
exists l.(l = severed_limb & -HasFaculty(l))
exists s.(s = sound & DiscontinuousStream(s) & -IsBurned(s) & -Weighs(s))
all x.(BurnerIn(position_a,x) <-> OuterFour(x))
all x.(WeighedIn(position_a,x) <-> OuterFour(x))
all x.(BurnerIn(position_b,x) <-> (x = fire_element))
all x.(WeighedIn(position_b,x) <-> (x = heaviness))
exists f.(f = fire_element & GreatElement(f) & InstanceOf(f,tangible) & -AmongEighteen(f))
exists h.(h = heaviness & ElementDependent(h) & InstanceOf(h,tangible))
exists d.(d = dispute & -Decided(d))
# THEORY rejected_faculty_is_cut
# EXPECT rejected_faculty_is_cut F
exists x.(SenseFaculty(x) & IsCut(x))
# THEORY rejected_faculty_burns_or_weighs
# EXPECT rejected_faculty_burns_or_weighs F
exists x.(SenseFaculty(x) & (IsBurned(x) | Weighs(x)))
# THEORY rejected_sound_is_burned
# EXPECT rejected_sound_is_burned F
exists s.(s = sound & IsBurned(s))
# THEORY rejected_fire_is_a_fifth_principle
# EXPECT rejected_fire_is_a_fifth_principle F
exists f.(f = fire_element & AmongEighteen(f))
# THEORY rejected_positions_agree
# EXPECT rejected_positions_agree F
all x.(BurnerIn(position_a,x) <-> BurnerIn(position_b,x))
# THEORY rejected_dispute_decided
# EXPECT rejected_dispute_decided F
exists d.(d = dispute & Decided(d))
```

```nltk-valuation
visible_form => rupa_d
odor => gandha_d
taste => rasa_d
tangible => sprastavya_d
sound => sabda_d
burner => burner_q
weighed => weighed_q
dispute => vivada
position_a => kecid_a
position_b => kecid_b
fire_element => tejas_i
heaviness => gurutva_i
severed_limb => chinna_anga
AmongEighteen => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d,mano_d,dharma_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d}
SenseFaculty => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d}
OuterFour => {rupa_d,gandha_d,rasa_d,sprastavya_d}
Cuts => {rupa_d,gandha_d,rasa_d,sprastavya_d}
IsCut => {rupa_d,gandha_d,rasa_d,sprastavya_d}
IsBurned => {rupa_d,gandha_d,rasa_d,sprastavya_d}
Weighs => {rupa_d,gandha_d,rasa_d,sprastavya_d}
ClusterStream => {rupa_d,gandha_d,rasa_d,sprastavya_d}
Clear => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d}
DiscontinuousStream => {sabda_d}
Dispute => {vivada}
About => {(vivada,burner_q),(vivada,weighed_q)}
Decided => {}
BurnerIn => {(kecid_a,rupa_d),(kecid_a,gandha_d),(kecid_a,rasa_d),(kecid_a,sprastavya_d),(kecid_b,tejas_i)}
WeighedIn => {(kecid_a,rupa_d),(kecid_a,gandha_d),(kecid_a,rasa_d),(kecid_a,sprastavya_d),(kecid_b,gurutva_i)}
InstanceOf => {(tejas_i,sprastavya_d),(gurutva_i,sprastavya_d)}
GreatElement => {tejas_i}
ElementDependent => {gurutva_i}
HasFaculty => {}
```

**Model checks.** The verse formula holds. The prose closes the tetrad,
keeps cutting, burning, and weighing inside it, defines cutting by the
stream of clusters, keeps the Faculties clear of all four roles, and
excludes Sound. Both positions are modelled and the dispute is left
undecided; the second position's burner and weighed are an Element and an
Element-dependent instance of the Tangible, as 1.35 requires. All six
rejected theories are false.

**Bhāṣya determination.** *Saṃbandhotpādinaḥ saṃghātasrotaso
vibhaktotpādanam*: cutting is the production, as divided, of a stream of
clusters arising in connection. *Maṇiprabhāvad acchatvāt*: the Faculties
neither cut nor are burned nor weigh, because of clarity, like jewel
radiance. *Na śabda uccheditvāt*: not Sound, because it is cut off.

**Organon interpretation.** The verse settles one voice of each root and
disputes the other. The settled roles are the tetrad's; the disputed roles
are where the Element and the Principle could come apart.

```text
outer four
    cut and are cut
    are burned
    weigh

Faculty
    not cut
    does not cut
    not burned
    does not weigh
    clarity, like jewel-radiance

Sound
    not in the burn or the weighing
    cut off

dispute
    the four are burner and weighed
    or the Fire Principle burns, heaviness is weighed

1.37 not opened
```

## 9. Interpretive Note

**Translation correction.** *Tulya* is a gerundive, "to be weighed"; the earlier "weigher" made the dispute repeat what the verse had settled (*tulayati*, it weighs). The anchor now reads "the burner and the weighed".

**Translation note.** The Bhāṣya identifies the four as Visible Form, Odor, Taste, and Tangible, and explains cutting as division in a stream of clusters. The Faculties are not cut or burned. It records two positions on the burner and the weighed: the same fourfold group, or the Fire Principle alone as burner and heaviness alone as what is weighed.

The hinge is the Faculty. A severed limb does not divide it. The dispute does not reopen the tetrad. It only asks what burns and what is weighed.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_36 a vak:Karika ;
    vak:hasTopic vak:OuterFour ;
    vak:belongsTo vak:Dhatunirdesa .

vak:OuterFour vak:cuts true ; vak:isCut true ; vak:isBurned true ; vak:weighs true .
vak:Faculty vak:isCut false .
vak:FirePrinciple vak:disputedAs vak:Burner .
vak:Heaviness vak:disputedAs vak:Weighed .
```
