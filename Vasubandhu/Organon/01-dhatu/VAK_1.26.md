# VAK_1.26 — The Measure of a Dharma-Collection

## 1. Sanskrit (Devanāgarī)

```sanskrit
शास्त्रप्रमाण इत्येके स्कन्धादीनां कथैकशः ।
चरितप्रतिपक्षस्तु धर्मस्कन्धोऽनुवर्णितः ॥ १.२६ ॥
```

## 2. Sanskrit (IAST)

```text
śāstrapramāṇa ity eke skandhādīnāṃ kathaikaśaḥ /
caritapratipakṣas tu dharmaskandho 'nuvarṇitaḥ // 1.26 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| śāstra-pramāṇaḥ | śāstra-pramāṇa, bahuvrīhi; nominative masculine singular | having a treatise as its measure; said of the Dharma-collection |
| iti | quotative particle | closes the reported account |
| eke | nominative masculine plural | some; holders of the first account |
| skandha-ādīnām | skandha-ādi; genitive plural | of the Bases and the rest; the topics |
| kathā | nominative feminine singular | exposition; the second measure |
| ekaśaḥ | distributive adverb | each separately |
| carita-pratipakṣaḥ | carita-pratipakṣa; nominative masculine singular | counteragent to a disposition; predicate |
| tu | particle | but; contrasts, does not refute |
| dharma-skandhaḥ | dharma-skandha; nominative masculine singular | a Dharma-collection; subject; not a sixth Base |
| anuvarṇitaḥ | anu-√varṇ, past passive participle; nominative masculine singular | has been described; agrees with the subject |

The research verse has `śāstrapramāṇā`. The running verse and the commentary read `śāstrapramāṇa`. That reading is kept. The long vowel is recorded, not adopted.

**Grammar tokens.** Verse-order IAST with sandhi opened (`kathaikaśaḥ` →
*kathā ekaśaḥ*, `'nuvarṇitaḥ` → *anuvarṇitaḥ*) and compound boundaries
marked. The second account's holders ("others") and the measured
Dharma-collection of the first two accounts are supplied by the Bhāṣya
inside the rules, not as covert leaves.

```text
# tokens: śāstra-pramāṇaḥ iti eke skandha-ādīnām kathā ekaśaḥ carita-pratipakṣaḥ tu dharma-skandhaḥ anuvarṇitaḥ
```

## 4. Grammar

Three accounts in sequence. The first is quoted (*iti*) and attributed
(*eke*). The second is elliptical: a genitive of topics, the nominative
*kathā*, and the distributive *ekaśaḥ*; the Bhāṣya supplies *apare*. The
third is complete: a masculine nominative predicate, *tu*, the masculine
subject, and an agreeing participle.

```nltk-fcfg
% start S
# tokens: śāstra-pramāṇaḥ iti eke skandha-ādīnām kathā ekaśaḥ carita-pratipakṣaḥ tu dharma-skandhaḥ anuvarṇitaḥ
S[SEM=<(?first & ?second & ?third)>] -> FIRST[SEM=?first] SECOND[SUPPLIED=prose,SEM=?second] THIRD[SEM=?third]
FIRST[SEM=<?holder(?measure)>] -> MEASURE[CASE=nom,NUM=sg,GEN=m,SEM=?measure] QUOTE HOLDER[CASE=nom,NUM=pl,SEM=?holder]
SECOND[SUPPLIED=prose,SEM=<(Holds(other_teachers,?exp) & MeasureOf(?exp,dharma_collection) & ?topics(?exp) & ?each(?exp))>] -> TOPICS[CASE=gen,NUM=pl,SEM=?topics] EXPOSITION[CASE=nom,NUM=sg,GEN=f,SEM=?exp] EACH[SEM=?each]
THIRD[SEM=<(?described(?coll)(?pred) & ?contrast(?pred))>] -> PRED[CASE=nom,NUM=?n,GEN=?g,SEM=?pred] TU[SEM=?contrast] COLL[CASE=nom,NUM=?n,GEN=?g,SEM=?coll] DESCRIBED[CASE=nom,NUM=?n,GEN=?g,SEM=?described]
MEASURE[CASE=nom,NUM=sg,GEN=m,SEM=<treatise_measure>] -> 'śāstra-pramāṇaḥ'
QUOTE -> 'iti'
HOLDER[CASE=nom,NUM=pl,GEN=m,SEM=<\m.(Holds(some_teachers,m) & MeasureOf(m,dharma_collection))>] -> 'eke'
TOPICS[CASE=gen,NUM=pl,SEM=<\m.ConcernsTopics(m,bases_and_rest)>] -> 'skandha-ādīnām'
EXPOSITION[CASE=nom,NUM=sg,GEN=f,SEM=<exposition_measure>] -> 'kathā'
EACH[SEM=<\m.Distributive(m)>] -> 'ekaśaḥ'
PRED[CASE=nom,NUM=sg,GEN=m,SEM=<counteragent_measure>] -> 'carita-pratipakṣaḥ'
TU[SEM=<\m.(ContrastsWith(m,treatise_measure) & ContrastsWith(m,exposition_measure))>] -> 'tu'
COLL[CASE=nom,NUM=sg,GEN=m,SEM=<dharma_collection>] -> 'dharma-skandhaḥ'
DESCRIBED[CASE=nom,NUM=sg,GEN=m,SEM=<\c m.(DescribedAs(c,m) & MeasureOf(m,c))>] -> 'anuvarṇitaḥ'
```

```nltk-dep
'eke' -> 'śāstra-pramāṇaḥ' | 'iti'
'kathā' -> 'skandha-ādīnām' | 'ekaśaḥ'
'anuvarṇitaḥ' -> 'dharma-skandhaḥ' | 'carita-pratipakṣaḥ' | 'tu'
```

**Close construe.** "Having a treatise as its measure," some say; [others:]
an exposition of the Bases and the rest, each separately. But a
Dharma-collection is described as a counteragent to a disposition.

`Holds` keeps attribution; no account is asserted as the author's own
except by *anuvarṇitaḥ*'s report. `ContrastsWith` projects *tu* as contrast,
not refutation: the parse never derives `Refuted`. `Distributive` makes
each exposition one collection, not one exposition of all topics.
`MeasureOf` is extent, not *pramāṇa* as a means of knowledge.

The commentary supplies the Dharma-collection as what is measured in the first account and "others" in the second. `Tu` contrasts. It does not say the first two are false.

## 5. Translation

### Literal Translation

> Some say the measure is a treatise; an exposition of each of the Bases and
> the rest. But a Dharma-collection is described as a counteragent to a
> disposition.

### Bhāṣya-informed study translation

> Some say a treatise is the measure of a Dharma-collection; others, an
> exposition of each of the Bases and the rest. But a Dharma-collection is
> described as a counteragent to a disposition.

## 6. Philosophical Translation

Three measures. The verse does not choose by erasing.

Some measure the collection by a treatise. The treatise named Dharmaskandha is six thousand. The unit is not given.

Others measure it by exposition. Each topic, separately. The Bases and the rest are the topics. A topic is not a further Base.

But the collection that is described is a counteragent to a disposition. Eighty thousand dispositions. Eighty thousand collections. The count is the correspondence. The pairings are not listed.

The word is a teaching-collection. It is not a member of the five Bases. It does not reopen the Essence called Form, or the Essence called Dharma.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| dharmaskandha | Dharma-collection | a teaching-unit; not a sixth Base |
| pramāṇa | measure | extent; not a means of knowledge |
| śāstra | treatise | the work named Dharmaskandha |
| ṣaṭsahasrāṇi | six thousand | unit unstated |
| kathā | exposition | the second measure |
| ekaśaḥ | each separately | not one collective topic |
| skandha | Base | in the topic list; the five |
| āyatana | Essence | in the topic list; the twelve |
| dhātu | Principle | in the topic list; the eighteen |
| carita | disposition | attachment, hatred, delusion, pride, and the rest |
| pratipakṣa | counteragent | the third measure |
| aśītisahasra | eighty thousand | dispositions, and collections |

## 8. Logical Determination

**Kārikā, derived.** Three attributed measures of one Dharma-collection;
the described measure contrasts with the other two without refuting them.

```nltk-sem
# derived by the section 4 parse
(Holds(some_teachers,treatise_measure) & MeasureOf(treatise_measure,dharma_collection) & Holds(other_teachers,exposition_measure) & MeasureOf(exposition_measure,dharma_collection) & ConcernsTopics(exposition_measure,bases_and_rest) & Distributive(exposition_measure) & DescribedAs(dharma_collection,counteragent_measure) & MeasureOf(counteragent_measure,dharma_collection) & ContrastsWith(counteragent_measure,treatise_measure) & ContrastsWith(counteragent_measure,exposition_measure))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(Holds(some_teachers,treatise_measure) & MeasureOf(treatise_measure,dharma_collection) & Holds(other_teachers,exposition_measure) & MeasureOf(exposition_measure,dharma_collection) & ConcernsTopics(exposition_measure,bases_and_rest) & Distributive(exposition_measure) & DescribedAs(dharma_collection,counteragent_measure) & MeasureOf(counteragent_measure,dharma_collection) & ContrastsWith(counteragent_measure,treatise_measure) & ContrastsWith(counteragent_measure,exposition_measure))
# THEORY prose
# EXPECT prose T
exists t.(t = dharmaskandha_treatise & NamedDharmaskandha(t) & Abhidharma(t) & HasCount(t,six_thousand))
exists n.(n = six_thousand & -UnitStated(n))
Topic(bases_topic) & Topic(essences_topic) & Topic(principles_topic)
all t.(Topic(t) -> exists x.(ExpositionOf(x,t) & DharmaCollection(x)))
all x t u.((ExpositionOf(x,t) & ExpositionOf(x,u)) -> (t = u))
all d.(Disposition(d) -> exists c.(Counteragent(c,d) & DharmaCollection(c) & Taught(blessed_one,c)))
all c d f.((Counteragent(c,d) & Counteragent(c,f)) -> (d = f))
all d.(Disposition(d) -> exists k.(DifferentiatedBy(d,k) & DispositionKind(k)))
DispositionKind(attachment) & DispositionKind(hatred) & DispositionKind(delusion) & DispositionKind(pride)
all m.-Refuted(m)
all c.(DharmaCollection(c) -> -Base(c))
# THEORY rejected_tu_refutes
# EXPECT rejected_tu_refutes F
exists m.(MeasureOf(m,dharma_collection) & Refuted(m))
# THEORY rejected_collection_is_base
# EXPECT rejected_collection_is_base F
exists c.(DharmaCollection(c) & Base(c))
# THEORY rejected_one_exposition_of_all_topics
# EXPECT rejected_one_exposition_of_all_topics F
exists x.all t.(Topic(t) -> ExpositionOf(x,t))
# THEORY rejected_unit_stated
# EXPECT rejected_unit_stated F
exists n.(n = six_thousand & UnitStated(n))
# THEORY rejected_pramana_as_means_of_knowledge
# EXPECT rejected_pramana_as_means_of_knowledge F
exists m.(MeasureOf(m,dharma_collection) & MeansOfKnowledge(m))
# THEORY rejected_one_counteragent_for_many
# EXPECT rejected_one_counteragent_for_many F
exists c d f.(Counteragent(c,d) & Counteragent(c,f) & -(d = f))
```

```nltk-valuation
treatise_measure => treatise_account
exposition_measure => exposition_account
counteragent_measure => counteragent_account
dharma_collection => dharma_collection_kind
some_teachers => eke_holders
other_teachers => apare_holders
bases_and_rest => topic_list
dharmaskandha_treatise => dharmaskandha_sastra
six_thousand => six_thousand_count
bases_topic => skandha_topic
essences_topic => ayatana_topic
principles_topic => dhatu_topic
blessed_one => bhagavat
attachment => raga
hatred => dvesa
delusion => moha
pride => mana
Holds => {(eke_holders,treatise_account),(apare_holders,exposition_account)}
MeasureOf => {(treatise_account,dharma_collection_kind),(exposition_account,dharma_collection_kind),(counteragent_account,dharma_collection_kind)}
ConcernsTopics => {(exposition_account,topic_list)}
Distributive => {exposition_account}
ContrastsWith => {(counteragent_account,treatise_account),(counteragent_account,exposition_account)}
DescribedAs => {(dharma_collection_kind,counteragent_account)}
NamedDharmaskandha => {dharmaskandha_sastra}
Abhidharma => {dharmaskandha_sastra}
HasCount => {(dharmaskandha_sastra,six_thousand_count)}
UnitStated => {}
Topic => {skandha_topic,ayatana_topic,dhatu_topic}
ExpositionOf => {(skandha_exposition,skandha_topic),(ayatana_exposition,ayatana_topic),(dhatu_exposition,dhatu_topic)}
DharmaCollection => {skandha_exposition,ayatana_exposition,dhatu_exposition,counter_a,counter_b}
Disposition => {disposition_a,disposition_b}
Counteragent => {(counter_a,disposition_a),(counter_b,disposition_b)}
Taught => {(bhagavat,counter_a),(bhagavat,counter_b)}
DifferentiatedBy => {(disposition_a,raga),(disposition_b,dvesa)}
DispositionKind => {raga,dvesa,moha,mana}
Refuted => {}
Base => {rupa_skandha,vedana_skandha}
MeansOfKnowledge => {}
```

**Model checks.** Three expositions of three distinct topics give three
collections; one exposition of all topics is rejected. Two representative
dispositions receive two distinct counteragent collections; the eighty
thousand is the count of the correspondence, and the model does not list
the pairings. Removing either attribution, the distributive reading, or
either contrast falsifies the derived formula. Nothing is refuted; no
collection is a Base.

**Bhāṣya determination.** The first measure is the Abhidharma treatise
named Dharmaskandha, six thousand with the unit unstated. The second
supplies *apare* and lists the topics from the Bases, Essences, and
Principles through knowledge through resolve and freedom from conflict.
The third explains the eighty thousand: dispositions differentiated by
attachment, hatred, delusion, pride, and the rest, each with its
counteragent taught by the Blessed One.

**Organon interpretation.** The classification engine now measures its
own teaching-units. Three measures run in parallel: by text, by topic, and
by function. The described one is functional: a collection is individuated
by the disposition it counters, so the teaching is indexed to the
practitioner, not to the page. None of the three adds a Base. The
assignment of other names (1.27) is not opened. The earlier schematic
follows.

```text
what is the measure of one Dharma-collection

some
    treatise
    the work named Dharmaskandha
    six thousand
    unit unstated

others
    exposition of each topic
    Bases, Essences, Principles, and the rest
    each exposition is one collection

but, described
    counteragent to a disposition
    eighty thousand dispositions
    eighty thousand collections
    correspondence, not a listing

tu
    contrasts
    does not refute the first two

not a Base
not the Essence called Form
not the Essence called Dharma

1.27 not opened
```

## 9. Interpretive Note

**Translation note.** The Bhāṣya distinguishes three measures: some take the
Abhidharma treatise named Dharmaskandha (six thousand, with the unit
unstated); others take each exposition of a topic separately; the final
account treats collections as counteragents to eighty thousand dispositions,
differentiated by attachment, hatred, delusion, pride, and others. The
contrastive tu does not refute the first two accounts.

The hinge is `tu`. The classification has already named its positions. This verse meets the word that looks like a further Base. The word is a collection of teaching, and the collection that is described is the counteragent. Assignment of other scriptural names is the next verse.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_26 a vak:Karika ;
    vak:hasTopic vak:DharmaCollectionMeasure ;
    vak:belongsTo vak:Dhatunirdesa .

vak:DharmaCollection vak:notA vak:Base ;
    vak:measuredBy vak:Treatise, vak:Exposition, vak:Counteragent .

vak:Counteragent vak:correspondsTo vak:Disposition ;
    vak:count 80000 .
vak:DharmaskandhaTreatise vak:count 6000 ;
    vak:unitUnstated true .
```
