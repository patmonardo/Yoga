# VAK_1.03 — Why Abhidharma Instruction Is Necessary

## 1. Sanskrit (Devanāgarī)

```sanskrit
धर्माणां प्रविचयमन्तरेण नास्ति क्लेशानां यत उपशान्तयेऽभ्युपायः ।
क्लेशैश्च भ्रमति भवार्णवेऽत्र लोकस्तद्धेतोरत उदितः किलैष शास्त्रः ॥ १.०३ ॥
```

## 2. Sanskrit (IAST)

```text
dharmāṇāṃ pravicayam antareṇa nāsti kleśānāṃ yata upaśāntaye 'bhyupāyaḥ /
kleśaiś ca bhramati bhavārṇave 'tra lokas taddhetor ata uditaḥ kilaiṣa śāstraḥ // 1.03 //
```

The running Sanskrit witness reads `śāstrā` at the end of this verse.
`Śāstraḥ` above is an editorial conjecture, not a reading established by that
witness. It fits `uditaḥ` and `eṣaḥ` formally, but `śāstra` is ordinarily
neuter; the exact ending remains unsettled. The Devanāgarī line reflects the
same conjecture. The translation conveys the contextual sense without
claiming that the transmitted ending has been resolved.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| dharmāṇām | genitive plural | dharmas to be discriminated |
| pravicayam | accusative singular | governed by `antareṇa` |
| antareṇa | indeclinable postposition | without |
| kleśānām | genitive plural | afflictions to be pacified |
| upaśāntaye | dative singular | purpose: for pacification |
| abhyupāyaḥ | nominative singular | adequate means |
| kleśaiḥ | instrumental plural | cause of wandering |
| bhramati | 3rd singular present | wanders |
| bhavārṇave | locative singular | in the ocean of becoming |
| lokaḥ | nominative singular | subject of `bhramati` |
| tad-dhetoḥ / ataḥ | ablatival expressions | for that reason / therefore |
| uditaḥ | past participle, nominative singular | taught, declared |
| kila | particle | reportedly; according to the received account |
| eṣaḥ śāstraḥ | nominative singular in the conjectural reading | this treatise; transmitted `śāstrā` remains unsettled |

**Grammar tokens.** Normalized IAST in verse order, including *na asti*,
*yataḥ*, and *atra* present in the Sanskrit. The compressed lexical
row *eṣaḥ śāstraḥ* becomes two tokens. `śāstraḥ` retains the displayed
conjecture, explicitly marked `READING=conjecture`; the grammar does not
establish it as the transmitted reading. No covert token is needed.

```text
# tokens: dharmāṇām pravicayam antareṇa na asti kleśānām yataḥ upaśāntaye abhyupāyaḥ kleśaiḥ ca bhramati bhavārṇave atra lokaḥ tad-dhetoḥ ataḥ uditaḥ kila eṣaḥ śāstraḥ
```

## 4. Grammar

*Antareṇa* governs the accusative *pravicayam*: without discrimination
there is no means of pacification. The instrumental *kleśaiḥ* diagnoses
wandering; *yataḥ*, *tad-dhetoḥ*, and *ataḥ* frame the grounds for teaching.
*Kila* marks a reported claim, not an unqualified historical assertion.

```nltk-fcfg
% start S
# tokens: dharmāṇām pravicayam antareṇa na asti kleśānām yataḥ upaśāntaye abhyupāyaḥ kleśaiḥ ca bhramati bhavārṇave atra lokaḥ tad-dhetoḥ ataḥ uditaḥ kila eṣaḥ śāstraḥ
S[SEM=<?reason(?need)(?wandering)(?report)>] -> NECESSITY[SEM=?need] WANDERING[SEM=?wandering] REASON[SEM=?reason] REPORT[SEM=?report]
NECESSITY[SEM=<?without(?discriminate)(?neg(?means(?afflictions)(?purpose)))>] -> DISCRIMINATION[CASE=acc,SEM=?discriminate] WITHOUT[GOVERNS=acc,SEM=?without] NEG[SEM=?neg] COPULA[NUM=?n] AFFLICTIONS[CASE=gen,SEM=?afflictions] PTCL[K=because] PURPOSE[CASE=dat,SEM=?purpose] MEANS[CASE=nom,NUM=?n,GEN=m,SEM=?means]
DISCRIMINATION[CASE=?c,SEM=<?verb(?dharmas)>] -> DHARMAS[CASE=gen,SEM=?dharmas] DISCRIM[CASE=?c,SEM=?verb]
WANDERING[SEM=<?verb(?cause)(?place)(?world)>] -> CAUSE[CASE=ins,SEM=?cause] PTCL[K=and] WANDER[NUM=?n,PERS=third,TENSE=present,SEM=?verb] PLACE[CASE=loc,SEM=?place] PTCL[K=here] WORLD[CASE=nom,NUM=?n,SEM=?world]
REASON[SEM=?reason] -> REASONHEAD[SEM=?reason] PTCL[K=therefore]
REPORT[SEM=<?report(?taught(?work))>] -> TAUGHT[CASE=nom,NUM=?n,GEN=?g,SEM=?taught] REPORTER[SEM=?report] DEM[CASE=nom,NUM=?n,GEN=?g] WORK[CASE=nom,NUM=?n,GEN=?g,READING=conjecture,SEM=?work]
DHARMAS[CASE=gen,SEM=<dharmas>] -> 'dharmāṇām'
DISCRIM[CASE=acc,SEM=<\d.\x.Discriminates(x,d)>] -> 'pravicayam'
WITHOUT[GOVERNS=acc,SEM=<\D.\M.all x.(-D(x) -> M(x))>] -> 'antareṇa'
NEG[SEM=<\P.\x.-P(x)>] -> 'na'
COPULA[NUM=sg,TENSE=present] -> 'asti'
AFFLICTIONS[CASE=gen,SEM=<afflictions>] -> 'kleśānām'
PTCL[K=because] -> 'yataḥ'
PURPOSE[CASE=dat,SEM=<pacification>] -> 'upaśāntaye'
MEANS[CASE=nom,NUM=sg,GEN=m,SEM=<\a.\p.\x.HasMeansFor(x,p,a)>] -> 'abhyupāyaḥ'
CAUSE[CASE=ins,SEM=<afflictions>] -> 'kleśaiḥ'
PTCL[K=and] -> 'ca'
WANDER[NUM=sg,PERS=third,TENSE=present,SEM=<\c.\p.\w.WandersThrough(w,c,p)>] -> 'bhramati'
PLACE[CASE=loc,SEM=<becoming_ocean>] -> 'bhavārṇave'
PTCL[K=here] -> 'atra'
WORLD[CASE=nom,NUM=sg,SEM=<world>] -> 'lokaḥ'
REASONHEAD[SEM=<\P.\Q.\R.(P & Q & R)>] -> 'tad-dhetoḥ'
PTCL[K=therefore] -> 'ataḥ'
TAUGHT[CASE=nom,NUM=sg,GEN=m,VOICE=passive,SEM=<\w.\r.ReportsTaught(r,w)>] -> 'uditaḥ'
REPORTER[SEM=<\P.(ReceivedReport(teaching_report) & P(teaching_report))>] -> 'kila'
DEM[CASE=nom,NUM=sg,GEN=m] -> 'eṣaḥ'
WORK[CASE=nom,NUM=sg,GEN=m,READING=conjecture,SEM=<treatise>] -> 'śāstraḥ'
```

```nltk-dep
'uditaḥ' -> 'asti' | 'bhramati' | 'tad-dhetoḥ' | 'ataḥ' | 'kila' | 'śāstraḥ'
'asti' -> 'pravicayam' | 'na' | 'abhyupāyaḥ' | 'yataḥ'
'pravicayam' -> 'dharmāṇām' | 'antareṇa'
'abhyupāyaḥ' -> 'upaśāntaye'
'upaśāntaye' -> 'kleśānām'
'bhramati' -> 'kleśaiḥ' | 'ca' | 'bhavārṇave' | 'atra' | 'lokaḥ'
'śāstraḥ' -> 'eṣaḥ'
```

**Close construe.** Without discrimination of dharmas there is no means
for pacifying afflictions; through afflictions the world wanders here in
the ocean of becoming. For that reason this treatise is reportedly taught.

The negation is inside the restriction supplied by *antareṇa*, not a denial
that any means exists. The reason-connectives organize the argument; their pragmatic
force is not an inference rule proving that a teaching event occurred.
The agreement with conjectural *śāstraḥ* tests the displayed construal,
not the unresolved transmitted ending *śāstrā*.

The Bhāṣya adds instruction as the disciple's required mediation and
attributes the account of dispersed teaching and its collection by
Kātyāyanīputra and others to the Vaibhāṣikas. Neither attribution is
silently inserted into the verse's semantics.

## 5. Translation

### Literal Translation

> Since without discrimination of dharmas there is no means for the
> pacification of the afflictions, and since through the afflictions the
> world wanders here in the ocean of becoming, for that reason this treatise
> is said to have been taught.

### Bhāṣya-informed study translation

> Without discrimination of dharmas, there is no means to pacify the
> afflictions; through the afflictions, the world wanders in this ocean of
> becoming. For this reason, this treatise is said to have been taught.

## 6. Philosophical Translation

> Abhidharma instruction is necessary because liberation requires a capacity the unaided disciple does not yet possess: exact discrimination of dharmas. That capacity makes the pacification of the afflictions possible and answers their causal power to sustain wandering.

Organon rendering:

> The śāstra is an instrument for producing discriminative capacity. Its analysis is justified neither as inventory nor speculation, but as the indispensable operation by which affliction can be pacified.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Determination |
|---|---|---|
| dharmapravicaya | discrimination of dharmas | indispensable cognitive operation |
| kleśopaśānti | pacification of affliction | practical end of discrimination |
| abhyupāya | adequate means | here denied apart from pravicaya |
| bhavārṇava | ocean of becoming | glossed as the great ocean of saṃsāra |
| abhidharmopadeśa | Abhidharma instruction | Bhāṣya: pedagogical mediation |
| kila | reportedly | preserves distance from received doctrine |
| prakīrṇa | dispersed | Bhāṣya: mode of Buddha's teaching in the Vaibhāṣika account |

## 8. Logical Determination

**Kārikā, derived.** Here `x` ranges over possible possessors of the
capacity and means. The absent discrimination excludes means to
pacification; discrimination alone is not asserted sufficient.
`ReportsTaught` keeps the teaching inside a received report.

```nltk-sem
# derived by the section 4 parse
((all x.(-Discriminates(x,dharmas) -> -HasMeansFor(x,pacification,afflictions))) & WandersThrough(world,afflictions,becoming_ocean) & (ReceivedReport(teaching_report) & ReportsTaught(teaching_report,treatise)))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((all x.(-Discriminates(x,dharmas) -> -HasMeansFor(x,pacification,afflictions))) & WandersThrough(world,afflictions,becoming_ocean) & (ReceivedReport(teaching_report) & ReportsTaught(teaching_report,treatise)))
```

```nltk-valuation
dharmas => dharmas
pacification => pacification
afflictions => afflictions
world => beings
becoming_ocean => ocean
teaching_report => report
treatise => work
Discriminates => {(disciple,dharmas),(learner,dharmas)}
HasMeansFor => {(disciple,pacification,afflictions)}
WandersThrough => {(beings,afflictions,ocean)}
ReceivedReport => {report}
ReportsTaught => {(report,work)}
```

**Model checks.** The disciple discriminates and has means; the learner
discriminates without yet having means. Thus the model rejects the
converse, which would make discrimination sufficient. Adding a means
for someone without discrimination must falsify the verse formula.
A report's truth in this model does not assert the reported event as fact.

**Bhāṣya determination and Organon interpretation.** The following
pedagogical sequence retains the earlier analysis; its instruction step
comes from the commentary. It is not a chain of material implications
derived from the verse's token stream.

```text
kleśa → wandering in becoming
kleśa-pacification requires dharmapravicaya
dharmapravicaya requires instruction for the disciple
therefore: Abhidharma śāstra is taught
```

## 9. Interpretive Note

**Translation note.** The Bhāṣya explains that disciples cannot discriminate dharmas without Abhidharma instruction, and discusses who first taught the treatise, including the Vaibhāṣika account of its dispersed teaching and later collection.

VAK 1.02 defined the treatise as equipment for attaining stainless prajñā. VAK 1.03 identifies its operation: instruction generates the disciple's capacity to discriminate. Teaching does not bestow liberation externally; it enables the Cognition by which affliction can be pacified.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
vak:VAK_1_03 a vak:Karika ; vak:hasTopic vak:NecessityOfDharmapravicaya ; vak:belongsTo vak:Dhatunirdesa .
vak:AbhidharmaInstruction vak:enables vak:Dharmapravicaya .
vak:Dharmapravicaya vak:necessaryFor vak:KlesaPacification .
vak:Klesa vak:causes vak:WanderingInBecoming .
```
