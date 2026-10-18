# VAK_1.02 — Abhidharma as Attained Knowing, Path, and Treasury

## 1. Sanskrit (Devanāgarī)

```sanskrit
प्रज्ञामला सानुचराभिधर्मः तत्प्राप्तये यापि च यच्च शास्त्रम् ।
तस्यार्थतोऽस्मिन् समनुप्रवेशात् स चाश्रयोऽस्येत्यभिधर्मकोशम् ॥ १.०२ ॥
```

## 2. Sanskrit (IAST)

```text
prajñāmalā sānucarābhidharmaḥ tatprāptaye yāpi ca yacca śāstram /
tasyārthato 'smin samanupraveśāt sa cāśrayo 'syety abhidharmakośam // 1.02 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| prajñā | noun; feminine; nominative singular | discriminative comprehension; subject of the first definition |
| amalā | adjective; feminine; nominative singular (lemma: amala) | stainless in Literal and Bhāṣya-informed |
| sānucarā | adjective; feminine; nominative singular (lemma: sa-anucara) | qualifies `prajñā`: with attendants |
| abhidharmaḥ | noun; masculine; nominative singular (lemma: abhidharma) | predicate nominative |
| tatprāptaye | compound noun; feminine; dative singular (lemma: tad-prāpti) | purpose: for attainment of that |
| yā | relative pronoun; feminine; nominative singular (lemma: yad) | supplies a second `prajñā` by ellipsis |
| api | indeclinable | inclusion: also |
| ca | indeclinable | coordination |
| yat | relative pronoun; neuter; nominative singular (lemma: yad) | qualifies `śāstram` |
| ca | indeclinable | coordination |
| śāstram | noun; neuter; nominative singular (lemma: śāstra) | treatise included in the definition |
| tasya | pronoun; masculine/neuter; genitive singular (lemma: tad) | of that Abhidharma |
| arthataḥ | indeclinable ablatival adverb (lemma: artha) | by meaning; in respect of meaning |
| asmin | pronoun; masculine/neuter; locative singular (lemma: idam) | in this treatise |
| samanupraveśāt | action noun; masculine; ablative singular (lemma: sam-anu-praveśa) | causal: because of comprehensive entry |
| saḥ | pronoun; masculine; nominative singular (lemma: tad) | that Abhidharma |
| ca | indeclinable | introduces the further derivation |
| āśrayaḥ | noun; masculine; nominative singular (lemma: āśraya) | predicate: supporting basis |
| asya | pronoun; masculine/neuter; genitive singular (lemma: idam) | of this treatise |
| iti | indeclinable | closes the title derivation |
| abhidharmakośam | compound noun; neuter; accusative singular (lemma: abhidharma-kośa) | the title predicated of the treatise |

Sandhi to retain: *sānucarā* = *sa-anucarā*; *tasyārthato 'smin* =
*tasya arthataḥ asmin*; *sa cāśrayo 'syety* =
*saḥ ca āśrayaḥ asya iti*.

**Grammar tokens.** Normalized IAST in verse order. `∅-prajñā` supplies
the noun qualified by *yā*; `∅-tatprāptaye` repeats the purpose for the
treatise; `∅-abhidharmaḥ` repeats the predicate for both conventional
members. These are Bhāṣya-resolved ellipses, not witness words.

```text
# tokens: prajñā amalā sānucarā abhidharmaḥ tatprāptaye yā ∅-prajñā api ca yat ca śāstram ∅-tatprāptaye ∅-abhidharmaḥ tasya arthataḥ asmin samanupraveśāt saḥ ca āśrayaḥ asya iti abhidharmakośam
```

## 4. Grammar

Feminine *amalā* and *sānucarā* agree with *prajñā*, not the masculine
predicate noun *abhidharmaḥ*. The dative purpose governs both conventional
members. The last clauses distinguish entry by meaning from supporting
source and then name the work.

```nltk-fcfg
% start S
# tokens: prajñā amalā sānucarā abhidharmaḥ tatprāptaye yā ∅-prajñā api ca yat ca śāstram ∅-tatprāptaye ∅-abhidharmaḥ tasya arthataḥ asmin samanupraveśāt saḥ ca āśrayaḥ asya iti abhidharmakośam
S[SEM=<(?u & ?c & ?t)>] -> ULTIMATE[SEM=?u] CONVENTIONAL[SEM=?c] TITLECLAUSE[SEM=?t]
ULTIMATE[SEM=<all x.(?retinue(?pure(?prajna))(x) -> ?pred(x))>] -> N[K=prajna,CASE=nom,NUM=?n,GEN=?g,SEM=?prajna] ADJ[K=stainless,CASE=nom,NUM=?n,GEN=?g,SEM=?pure] ADJ[K=retinue,CASE=nom,NUM=?n,GEN=?g,SEM=?retinue] PRED[CASE=nom,NUM=?n,SEM=?pred]
CONVENTIONAL[SEM=<(?q(?p)(?purpose)(?pred) & ?qt(?t)(?purpose2)(?pred))>] -> PURPOSE[CASE=dat,SEM=?purpose] REL[CASE=nom,NUM=?n,GEN=?g,SEM=?q] COVERT[K=prajna,CASE=nom,NUM=?n,GEN=?g,SUPPLIED=prose,SEM=?p] PTCL[K=also] PTCL[K=and] REL[CASE=nom,NUM=?nt,GEN=?gt,SEM=?qt] PTCL[K=and] N[K=treatise,CASE=nom,NUM=?nt,GEN=?gt,SEM=?t] COVERT[K=purpose,CASE=dat,SUPPLIED=prose,SEM=?purpose2] COVERT[K=predicate,CASE=nom,SUPPLIED=prose,SEM=?pred]
TITLECLAUSE[SEM=<(?entry & ?support & ?name)>] -> ENTRY[SEM=?entry] SUPPORT[SEM=?support] PTCL[K=iti] NAME[CASE=acc,SEM=?name]
ENTRY[SEM=<?entry(?mode)(?source)(?work)>] -> PRON[K=that,CASE=gen,SEM=?source] ADV[SEM=?mode] PRON[K=this,CASE=loc,SEM=?work] ENTRYHEAD[CASE=abl,SEM=?entry]
SUPPORT[SEM=<?support(?source)(?work)>] -> PRON[K=that,CASE=nom,NUM=?n,GEN=?g,SEM=?source] PTCL[K=and] SUPPORTHEAD[CASE=nom,NUM=?n,GEN=?g,SEM=?support] PRON[K=this,CASE=gen,SEM=?work]
N[K=prajna,CASE=nom,NUM=sg,GEN=f,SEM=<\x.Prajna(x)>] -> 'prajñā'
ADJ[K=stainless,CASE=nom,NUM=sg,GEN=f,SEM=<\P.\x.(P(x) & Stainless(x))>] -> 'amalā'
ADJ[K=retinue,CASE=nom,NUM=sg,GEN=f,SEM=<\P.\x.(P(x) & WithRetinue(x))>] -> 'sānucarā'
PRED[CASE=nom,NUM=sg,GEN=m,SEM=<\x.Abhidharma(x)>] -> 'abhidharmaḥ'
PURPOSE[CASE=dat,SEM=<\x.ForAttainmentOf(x,stainless_prajna)>] -> 'tatprāptaye'
REL[CASE=nom,NUM=sg,GEN=f,SEM=<\P.\Q.\R.all x.((P(x) & Q(x)) -> R(x))>] -> 'yā'
COVERT[K=prajna,CASE=nom,NUM=sg,GEN=f,SUPPLIED=prose,SEM=<\x.Prajna(x)>] -> '∅-prajñā'
PTCL[K=also] -> 'api'
PTCL[K=and] -> 'ca'
REL[CASE=nom,NUM=sg,GEN=n,SEM=<\P.\Q.\R.all x.((P(x) & Q(x)) -> R(x))>] -> 'yat'
N[K=treatise,CASE=nom,NUM=sg,GEN=n,SEM=<\x.Treatise(x)>] -> 'śāstram'
COVERT[K=purpose,CASE=dat,SUPPLIED=prose,SEM=<\x.ForAttainmentOf(x,stainless_prajna)>] -> '∅-tatprāptaye'
COVERT[K=predicate,CASE=nom,SUPPLIED=prose,SEM=<\x.Abhidharma(x)>] -> '∅-abhidharmaḥ'
PRON[K=that,CASE=gen,SEM=<abhidharma_source>] -> 'tasya'
ADV[SEM=<principal_meaning>] -> 'arthataḥ'
PRON[K=this,CASE=loc,SEM=<kosa>] -> 'asmin'
ENTRYHEAD[CASE=abl,SEM=<\m.\s.\w.ContainsByMeaning(w,s,m)>] -> 'samanupraveśāt'
PRON[K=that,CASE=nom,NUM=sg,GEN=m,SEM=<abhidharma_source>] -> 'saḥ'
SUPPORTHEAD[CASE=nom,NUM=sg,GEN=m,SEM=<\s.\w.SourceFor(s,w)>] -> 'āśrayaḥ'
PRON[K=this,CASE=gen,SEM=<kosa>] -> 'asya'
PTCL[K=iti] -> 'iti'
NAME[CASE=acc,SEM=<Named(kosa,kosa_title)>] -> 'abhidharmakośam'
```

```nltk-dep
'abhidharmaḥ' -> 'prajñā' | '∅-abhidharmaḥ' | 'abhidharmakośam'
'prajñā' -> 'amalā' | 'sānucarā'
'∅-abhidharmaḥ' -> '∅-prajñā' | 'śāstram'
'∅-prajñā' -> 'tatprāptaye' | 'yā' | 'api' | 'ca'
'śāstram' -> 'yat' | 'ca' | '∅-tatprāptaye'
'abhidharmakośam' -> 'samanupraveśāt' | 'āśrayaḥ' | 'iti'
'samanupraveśāt' -> 'tasya' | 'arthataḥ' | 'asmin'
'āśrayaḥ' -> 'saḥ' | 'ca' | 'asya'
```

**Close construe.** Stainless prajñā with attendants is Abhidharma; so
also are prajñā and the treatise directed to its attainment. Because
Abhidharma enters this work by meaning and is its supporting source,
the work is called Abhidharmakośa.

The Bhāṣya calls the first an *anāsrava* five-Base complex and the second
prajñā *sāsrava*, constituted through hearing, reflection, cultivation,
or birth-acquisition. These are commentary determinations, not extra
witness words. The title has two derivations: this work is treasury-like
by containment; Abhidharma is the treasury-source from which the work
is drawn. The formula records their different directions, not a general
equation between āśraya and other conditioning relations.

## 5. Translation

### Literal Translation

> Stainless prajñā, with its attendants, is Abhidharma; so also is whatever
> [prajñā] is for the attainment of that, and whatever treatise [is for its
> attainment]. Because that enters into this by meaning—and because that is
> the supporting basis of this—[this treatise is called] the
> *Abhidharmakośa*.

### Bhāṣya-informed study translation

> Stainless discriminative comprehension with its attendants is Abhidharma.
> Also included are what serves to attain it and the treatise. The meaning
> of that Abhidharma enters this treatise, and Abhidharma is its source;
> hence this is called the *Abhidharmakośa*.

## 6. Philosophical Translation

> Abhidharma is first the Discriminator: stainless discriminative comprehension of dharmas, occurring with its full accompanying complex. By designation, the name also extends to prajñā still on the way, and to the treatise that functions as equipment for attaining it. The Kośa mediates between these orders: it gathers Abhidharma's principal meaning, yet is itself drawn from Abhidharma as its source.

Organon rendering:

> The book is not the first meaning of Abhidharma. Abhidharma is the Dharma of a Buddha. Discriminative comprehension here is a science, not a mood of wisdom. Kant's expression is therefore Pure Prajñā. Hearing, reflection, cultivation, birth-acquired prajñā, and the śāstra belong to it by their directedness toward that attainment. The Kośa is both a containment of Abhidharma in meaning and an extraction from Abhidharma as source.

> Pure is Always First. The path-prajñā presupposes that attainment as its before. It is not a moral grade. Stainless remains the verse word.

## 7. Technical Vocabulary

### Kārikā terms

| Sanskrit | Project rendering | Determination |
|---|---|---|
| prajñā | discriminative comprehension | Bhāṣya: `dharmapravicaya`, discrimination of dharmas. A science |
| amala | stainless | Literal and Bhāṣya-informed. Organon: Pure Prajñā. Not outflow-free |
| sānucara | with attendants | Prajñā together with its retinue; the attendants are not enumerated here |
| tatprāpti | attainment of that | Attainment of stainless prajñā with attendants |
| śāstra | treatise | Conventionally Abhidharma because it is equipment for that attainment |
| arthataḥ | by meaning | The mode in which Abhidharma is included in this work |
| samanupraveśa | comprehensive entry | Inclusion of the principal meaning of śāstric Abhidharma |
| āśraya | supporting basis | Abhidharma as the source from which the treatise is drawn |
| kośa | treasury | Either this work as container or Abhidharma as source-treasury |

### Bhāṣya determinations

| Sanskrit | Project rendering | Function here |
|---|---|---|
| pāramārthika | in the ultimate sense | Classifies stainless prajñā with attendants |
| sāṃketika | conventional / designated | Classifies path-prajñā and the treatise |
| anāsrava | Pure | Organon name of the Bhāṣya gloss of `amala`. Always First. Not the verse English |
| sāsrava | with outflows | Conventional. Organon: Impure. Presupposes a before |
| pañcaskandhaka | consisting of five Bases | Concrete complex of ultimate Abhidharma |
| saṃbhāra | equipment | Why the treatise is conventionally Abhidharma |
| dharmapravicaya | discrimination of dharmas | Operational definition of prajñā |
| dharma | dharma | `svalakṣaṇa-dhāraṇāt`: because it bears its own mark |
| dhāraṇa | bearing | The holding. Root `dhṛ`. Not dropped from the definition |
| svalakṣaṇa | own mark | What a dharma bears |
| pratyabhimukha | facing toward | The prefix `abhi-`. Two facings, both kept |
| paramārtha-dharma | ultimate dharma | Identified here with nirvāṇa. First facing |
| dharma-lakṣaṇa | mark of a dharma | Second facing. The Sāṃkhya hinge. Not dropped |

## 8. Logical Determination

**Kārikā, derived.** The first predication is an implication, not a
biconditional excluding conventional Abhidharma. The purpose qualification
is repeated for both conventional members. The title's two grounds retain
their different directions; the causal force of the naming is stated in
the construe, not expanded into a general causal law.

```nltk-sem
# derived by the section 4 parse
((all x.(((Prajna(x) & Stainless(x)) & WithRetinue(x)) -> Abhidharma(x))) & ((all x.((Prajna(x) & ForAttainmentOf(x,stainless_prajna)) -> Abhidharma(x))) & (all x.((Treatise(x) & ForAttainmentOf(x,stainless_prajna)) -> Abhidharma(x)))) & (ContainsByMeaning(kosa,abhidharma_source,principal_meaning) & SourceFor(abhidharma_source,kosa) & Named(kosa,kosa_title)))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((all x.(((Prajna(x) & Stainless(x)) & WithRetinue(x)) -> Abhidharma(x))) & ((all x.((Prajna(x) & ForAttainmentOf(x,stainless_prajna)) -> Abhidharma(x))) & (all x.((Treatise(x) & ForAttainmentOf(x,stainless_prajna)) -> Abhidharma(x)))) & (ContainsByMeaning(kosa,abhidharma_source,principal_meaning) & SourceFor(abhidharma_source,kosa) & Named(kosa,kosa_title)))
```

```nltk-valuation
stainless_prajna => pure
abhidharma_source => source
principal_meaning => meaning
kosa => work
kosa_title => title
Prajna => {pure,path}
Stainless => {pure}
WithRetinue => {pure,path}
Treatise => {work}
ForAttainmentOf => {(path,pure),(work,pure)}
Abhidharma => {pure,path,work}
ContainsByMeaning => {(work,source,meaning)}
SourceFor => {(source,work)}
Named => {(work,title)}
```

**Model checks.** All three Abhidharma classifications have witnesses;
the implications do not pass merely by empty antecedents. Removing a
conventional member from Abhidharma or reversing `SourceFor` must fail.
The valuation also refutes the overstatement that every Abhidharma member
is stainless. A finite model tests this specification, not metaphysical
truth.

**Bhāṣya determinations.** The following expands the verse's compact
predications; it is not additional output derived from its overt tokens.

```text
ABHIDHARMA
│
├── ultimate (pāramārthika)
│   └── stainless prajñā with attendants
│       └── discrimination of dharmas
│       └── an anāsrava five-Base complex
│
└── conventional (sāṃketika)
    ├── sāsrava prajñā directed toward the ultimate
    │   ├── hearing-constituted
    │   ├── reflection-constituted
    │   ├── cultivation-constituted
    │   └── birth-acquired
    └── śāstra serving as equipment for attainment

dharma
    = bears its own mark

Abhidharma
    = this dharma facing nirvāṇa
      or facing the mark of a dharma
```

Organon names, not the verse lines: `anāsrava` = Pure Prajñā; `sāsrava` = Impure.

The title then expresses reciprocal dependence:

```text
Abhidharma ──principal meaning enters──▶ Kośa
Kośa ──is drawn from──────────────▶ Abhidharma

first relation:  Kośa is treasury-like for Abhidharma
second relation: Abhidharma is the treasury-source of the Kośa
```

The two relations must not be reduced to a single generic notion of “support.” They reverse the direction of containment and dependence. The two facings must not be reduced to one.

## 9. Interpretive Note

**Translation note.** The Bhāṣya specifies the conventional members as outflow-bearing discriminative comprehension and the treatise directed toward stainless comprehension. It also develops the two senses of the title: the treatise contains Abhidharma's meaning, and Abhidharma is the source from which the treatise is drawn.

VAK 1.02 determines the relation between realized discrimination, the path that produces it, and the textual equipment that serves that path.

```text
sāsrava prajñā and textual equipment
    are directed toward
stainless prajñā with attendants
```

The Kośa is neither a merely external description nor the ultimate Abhidharma itself.

Organon note:

```text
ultimate Abhidharma
    = the Dharma of a Buddha
    = the Discriminator
    = Pure Prajñā, because prajñā is a science

conventional Abhidharma
    = the operations and equipment ordered toward its attainment

Kośa
    = a meaning-container drawn from Abhidharma as source
```

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_02
    a vak:Karika ;
    rdfs:label "VAK 1.02" ;
    vak:hasIAST "prajñāmalā sānucarābhidharmaḥ tatprāptaye yāpi ca yacca śāstram / tasyārthato 'smin samanupraveśāt sa cāśrayo 'syety abhidharmakośam" ;
    vak:hasTopic vak:DefinitionOfAbhidharma ;
    vak:belongsTo vak:Dhatunirdesa .

vak:ParamarthikaAbhidharma
    a vak:AbhidharmaSense ;
    rdfs:label "Abhidharma in the ultimate sense" ;
    vak:definedAs vak:StainlessPrajnaWithAttendants ;
    vak:organonName vak:PurePrajna .

vak:SamketikaAbhidharma
    a vak:AbhidharmaSense ;
    rdfs:label "Abhidharma in the conventional sense" ;
    vak:includes vak:PathPrajna, vak:AttainmentTreatise ;
    vak:directedToward vak:StainlessPrajnaWithAttendants .

vak:Dharma
    vak:definedAs vak:BearsOwnMark .

vak:Abhidharma
    vak:faces vak:Nirvana, vak:DharmaLaksana .

vak:Abhidharmakosa
    a vak:Treatise ;
    vak:containsByPrincipalMeaning vak:ScholasticAbhidharma ;
    vak:drawnFrom vak:Abhidharma .
```
