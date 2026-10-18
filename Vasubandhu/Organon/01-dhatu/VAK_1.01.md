# VAK_1.01 — Liberation through Instruction According to Reality

## 1. Sanskrit (Devanāgarī)

```sanskrit
यः सर्वथासर्वहतान्धकारः संसारपङ्काज्जगदुज्जहार ।
तस्मै नमस्कृत्य यथार्थशास्त्रे शास्त्रं प्रवक्ष्याम्यभिधर्मकोशम् ॥ १.०१ ॥
```

## 2. Sanskrit (IAST)

```text
yaḥ sarvathāsarvahatāndhakāraḥ saṃsārapaṅkājjagadujjahāra /
tasmai namaskṛtya yathārthaśāstre śāstraṃ pravakṣyāmy abhidharmakośam // 1.01 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| yaḥ | nominative masculine singular | he who |
| sarvathā | indeclinable | in every way |
| sarva-hata-andhakāraḥ | nominative masculine singular | whose darkness is destroyed concerning everything |
| saṃsāra-paṅkāt | ablative singular | from the mire of saṃsāra |
| jagat | accusative neuter singular | the world |
| ujjahāra | third-person singular perfect | lifted up, raised out |
| tasmai | dative masculine singular | to him |
| namaskṛtya | absolutive | having bowed |
| yathārtha-śāstre | dative singular of *yathārtha-śāstṛ* | to the teacher according to reality |
| śāstram | accusative neuter singular | treatise, teaching |
| pravakṣyāmi | first-person singular future | I shall proclaim |
| abhidharmakośam | accusative neuter singular | Treasury of Abhidharma |

**Grammar tokens.** Normalized IAST in verse order; sandhi is opened,
not the Sanskrit witness changed. Hyphenated compounds remain single
tokens corresponding to the table rows. No supplied token is needed.

```text
# tokens: yaḥ sarvathā sarva-hata-andhakāraḥ saṃsāra-paṅkāt jagat ujjahāra tasmai namaskṛtya yathārtha-śāstre śāstram pravakṣyāmi abhidharmakośam
```

## 4. Grammar

The relative *yaḥ* and correlative *tasmai* refer to the same teacher.
The adjectives agree with that masculine singular referent; the dative
*yathārtha-śāstre* identifies the recipient of homage. The absolutive
*namaskṛtya* shares the first-person subject of *pravakṣyāmi*.

```nltk-fcfg
% start S
# tokens: yaḥ sarvathā sarva-hata-andhakāraḥ saṃsāra-paṅkāt jagat ujjahāra tasmai namaskṛtya yathārtha-śāstre śāstram pravakṣyāmi abhidharmakośam
S[SEM=<?r(?h)(?a)>] -> RELCL[NUM=?n,GEN=?g,SEM=?r] HOMAGE[NUM=?n,GEN=?g,SEM=?h] ANNOUNCE[SEM=?a]
RELCL[NUM=?n,GEN=?g,SEM=<?rel(?quality)(?rescue)>] -> REL[CASE=nom,NUM=?n,GEN=?g,SEM=?rel] QUALITY[CASE=nom,NUM=?n,GEN=?g,SEM=?quality] RESCUE[NUM=?n,SEM=?rescue]
QUALITY[CASE=?c,NUM=?n,GEN=?g,SEM=<?mode(?quality)>] -> ADV[SEM=?mode] ADJ[CASE=?c,NUM=?n,GEN=?g,SEM=?quality]
RESCUE[NUM=?n,SEM=<?verb(?world)(?source)>] -> SOURCE[CASE=abl,SEM=?source] N[CASE=acc,NUM=sg,GEN=n,SEM=?world] V[NUM=?n,PERS=third,TENSE=perfect,SEM=?verb]
HOMAGE[NUM=?n,GEN=?g,SEM=<?bow(?teacher)>] -> CORR[CASE=dat,NUM=?n,GEN=?g] ABS[PERS=first,SEM=?bow] TEACHER[CASE=dat,NUM=?n,GEN=?g,SEM=?teacher]
ANNOUNCE[SEM=<?verb(?work)>] -> WORK[CASE=acc,NUM=?n,GEN=?g] V[NUM=sg,PERS=first,TENSE=future,SEM=?verb] TITLE[CASE=acc,NUM=?n,GEN=?g,SEM=?work]
REL[CASE=nom,NUM=sg,GEN=m,SEM=<\P.\Q.\H.\A.exists x.(P(x) & Q(x) & H(x) & A)>] -> 'yaḥ'
ADV[SEM=<\P.\x.(P(x) & DarknessDestroyedEveryWay(x))>] -> 'sarvathā'
ADJ[CASE=nom,NUM=sg,GEN=m,SEM=<\x.DarknessDestroyedRegardingAll(x)>] -> 'sarva-hata-andhakāraḥ'
SOURCE[CASE=abl,SEM=<samsara_mire>] -> 'saṃsāra-paṅkāt'
N[CASE=acc,NUM=sg,GEN=n,SEM=<world>] -> 'jagat'
V[NUM=sg,PERS=third,TENSE=perfect,SEM=<\w.\s.\x.RaisedFrom(x,w,s)>] -> 'ujjahāra'
CORR[CASE=dat,NUM=sg,GEN=m] -> 'tasmai'
ABS[PERS=first,SEM=<\P.\x.(P(x) & BowedTo(speaker,x))>] -> 'namaskṛtya'
TEACHER[CASE=dat,NUM=sg,GEN=m,SEM=<\x.TeachesAccordingToReality(x)>] -> 'yathārtha-śāstre'
WORK[CASE=acc,NUM=sg,GEN=n] -> 'śāstram'
V[NUM=sg,PERS=first,TENSE=future,SEM=<\w.(Treatise(w) & AnnouncesFutureExposition(speaker,w))>] -> 'pravakṣyāmi'
TITLE[CASE=acc,NUM=sg,GEN=n,SEM=<kosa>] -> 'abhidharmakośam'
```

```nltk-dep
'pravakṣyāmi' -> 'ujjahāra' | 'namaskṛtya' | 'śāstram'
'ujjahāra' -> 'yaḥ' | 'sarva-hata-andhakāraḥ' | 'saṃsāra-paṅkāt' | 'jagat'
'sarva-hata-andhakāraḥ' -> 'sarvathā'
'namaskṛtya' -> 'tasmai'
'tasmai' -> 'yathārtha-śāstre'
'śāstram' -> 'abhidharmakośam'
```

**Close construe.** He who has darkness destroyed in every way and
regarding all, who raised the world from the mire of saṃsāra: having
bowed to him, the teacher according to reality, I shall proclaim the
Abhidharmakośa treatise.

The parse binds the relative and correlative through one semantic variable,
not an equality between their nominative and dative cases. The Bhāṣya
identifies this teacher as Buddha and explains rescue through instruction,
not supernatural intervention. Those explanations are not extra overt
tokens. The future is an announcement, not an assertion that exposition
has already occurred; the temporal ordering of homage is stated in the
construe but not independently axiomatized in this FOL projection.

## 5. Translation

### Literal Translation

> Having bowed to him whose darkness has been destroyed in every way and
> concerning everything, who raised the world from the mire of saṃsāra — to
> that teacher according to reality — I shall proclaim the treatise, the
> *Abhidharmakośa*.

### Bhāṣya-informed study translation

> Having bowed to the teacher who teaches according to reality, whose
> darkness has been destroyed in every way and with respect to all, and who
> raised the world from the mire of saṃsāra, I shall expound the
> *Abhidharmakośa* treatise.

## 6. Philosophical Translation

> The work begins by bowing to the one whose ignorance has been extinguished in every way and concerning everything, who raises beings out of saṃsāric entanglement, and who teaches according to reality. The *Abhidharmakośa* is then announced as the śāstra to be proclaimed.

Organon rendering:

> Abhidharma begins from the overcoming of darkness. The Buddha is not invoked as ornament but as the actual disclosure of Dharma: one who has destroyed obscuration and lifted the world from the mud of appearance. The treatise is therefore a treasury of determinate reality.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| andhakāra | darkness | ignorance / obscuration |
| saṃsāra-paṅka | mire of saṃsāra | entangled cyclic appearance |
| jagat | world | beings/world-process caught in saṃsāra |
| yathārtha-śāstṛ | teacher according to reality | epithet of the Buddha in the dative singular `yathārthaśāstre` |
| śāstra | treatise / teaching | principled doctrinal exposition |
| abhidharmakośa | Treasury of Abhidharma | treasury of Dharma-analysis |

## 8. Logical Determination

**Kārikā, derived.** The parse composes the teacher's qualifications,
rescue, homage, and announcement. Both universal qualifications on the
destruction of darkness are retained as distinct predicates. Their internal
quantification over modes and knowables is not expanded in this pilot.

```nltk-sem
# derived by the section 4 parse
exists x.(DarknessDestroyedRegardingAll(x) & DarknessDestroyedEveryWay(x) & RaisedFrom(x,world,samsara_mire) & TeachesAccordingToReality(x) & BowedTo(speaker,x) & Treatise(kosa) & AnnouncesFutureExposition(speaker,kosa))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
exists x.(DarknessDestroyedRegardingAll(x) & DarknessDestroyedEveryWay(x) & RaisedFrom(x,world,samsara_mire) & TeachesAccordingToReality(x) & BowedTo(speaker,x) & Treatise(kosa) & AnnouncesFutureExposition(speaker,kosa))
```

```nltk-valuation
speaker => author
kosa => work
world => beings
samsara_mire => mire
DarknessDestroyedRegardingAll => {teacher}
DarknessDestroyedEveryWay => {teacher}
RaisedFrom => {(teacher,beings,mire)}
TeachesAccordingToReality => {teacher}
BowedTo => {(author,teacher)}
Treatise => {work}
AnnouncesFutureExposition => {(author,work)}
```

**Bhāṣya determination.** Buddha is the referent; the benefit to others
operates through teaching reality. The finite valuation witnesses the
verse's predication; it does not prove exhaustive knowledge or historical
events. Removing either darkness predicate, or assigning homage and
rescue to different teachers, must make this formula false.

**Organon interpretation.** The movement from obscuration through its
overcoming to instruction orients Dharma-analysis toward liberation.
It is not a source-derived universal rule that only a fully liberated
person may begin studying Abhidharma.

## 9. Interpretive Note

The first verse already sets the chapter's whole orientation. Abhidharma is not mere scholastic inventory. It is grounded in liberation from darkness and in the disclosure of reality.

For the later dhātu analysis, this matters because the Principles will not be treated as dead categories. They are the lawful determinations through which the world of saṃsāra can be understood, judged, cultivated, and transcended.

Organon note:

```text
Buddha
    = one in whom obscuration is destroyed

Abhidharma
    = analysis of Dharma according to reality

Kośa
    = treasury of determinate truth
```

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_01
    a vak:Karika ;
    rdfs:label "VAK 1.01" ;
    vak:hasIAST "yaḥ sarvathāsarvahatāndhakāraḥ saṃsārapaṅkājjagadujjahāra / tasmai namaskṛtya yathārthaśāstre śāstraṃ pravakṣyāmy abhidharmakośam" ;
    vak:hasTopic vak:HomageAndAnnouncement ;
    vak:belongsTo vak:Dhatunirdesa .
```
