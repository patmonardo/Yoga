# VAK_8.11 — The Fourth Dhyāna's Immovability

## 1. Sanskrit (Devanāgarī)

```sanskrit
अष्टापक्षालमुक्तत्वादानिञ्जं तु चतुर्थकम् ।
वितर्कचारौ श्वासौ च सुखादि च चतुष्टयम् ॥ ८.११ ॥
```

## 2. Sanskrit (IAST)

```text
aṣṭāpakṣālamuktatvād āniñjaṃ tu caturthakam |
vitarkacārau śvāsau ca sukhādi ca catuṣṭayam || 8.11 ||
```

The Sanskrit follows the local kārikā witness. The
prose expands the compressed pairs and the fourfold
feeling group. Its related form `āneñjya` is retained
in discussion without replacing the verse's `āniñja`.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `aṣṭa-apakṣāla-muktatvāt` | ablative singular of abstract `mukta-tva` with compound members `aṣṭa` (eight) and `apakṣāla` (disturbance or fault); `aṣṭa + apakṣāla` → `aṣṭāpakṣāla`; `muktatvāt + āniñjam` → `muktatvād āniñjam` | because of freedom from eight disturbances |
| `āniñjam` | nominative singular neuter | immovable; unshaken |
| `tu` | contrast particle | but; marks the fourth against the first three |
| `caturthakam` | nominative singular neuter ordinal | the fourth [dhyāna] |
| `vitarka-cārau` | nominative dual | vitarka and vicāra, as expanded in prose |
| `śvāsau` | nominative dual | the two breaths, śvāsa and praśvāsa |
| `ca` | conjunction | and |
| `sukha-ādi` | nominative singular neuter adjective | beginning with pleasure |
| `ca` | conjunction | and |
| `catuṣṭayam` | nominative singular neuter collective noun | a group of four |

## 4. Grammar

The causal ablative predicates immovability of the fourth dhyāna. The Bhāṣya expands the compressed duals and the open `sukhādi` list; an alternative explanation is not substituted for this eight-member account.

```nltk-fcfg
% start S
# tokens: aṣṭāpakṣālamuktatvāt āniñjam tu caturthakam vitarkacārau śvāsau ca sukhādi ca catuṣṭayam
S -> CL[K=predicate] CL[K=disturbances]
CL[K=predicate] -> ABL[CASE=abl,NUM=sg,GEN=n,CAUSE=freedom] ADJ[CASE=nom,NUM=sg,GEN=n,STATE=immovable] PTCL[CONTRAST=yes] N[CASE=nom,NUM=sg,GEN=n,REF=fourth]
CL[K=disturbances] -> N[CASE=nom,NUM=du,GEN=m,COUNT=two] N[CASE=nom,NUM=du,GEN=m,COUNT=two] CONJ[COORD=yes] ADJ[COUNT=four] CONJ[COORD=yes] N[CASE=nom,NUM=sg,GEN=n,COUNT=four]
ABL[CASE=abl,NUM=sg,GEN=n,CAUSE=freedom] -> 'aṣṭāpakṣālamuktatvāt'
ADJ[CASE=nom,NUM=sg,GEN=n,STATE=immovable] -> 'āniñjam'
PTCL[CONTRAST=yes] -> 'tu'
N[CASE=nom,NUM=sg,GEN=n,REF=fourth] -> 'caturthakam'
N[CASE=nom,NUM=du,GEN=m,COUNT=two] -> 'vitarkacārau'
N[CASE=nom,NUM=du,GEN=m,COUNT=two] -> 'śvāsau'
CONJ[COORD=yes] -> 'ca'
ADJ[COUNT=four] -> 'sukhādi'
CONJ[COORD=yes] -> 'ca'
N[CASE=nom,NUM=sg,GEN=n,COUNT=four] -> 'catuṣṭayam'
```

```nltk-dep
'āniñjam' -> 'aṣṭāpakṣālamuktatvāt' | 'tu' | 'caturthakam'
'catuṣṭayam' -> 'vitarkacārau' | 'śvāsau' | 'ca' | 'sukhādi' | 'ca'
```

The verse's duals remain single compound leaves; commentary resolves `vitarkacārau` as vitarka/vicāra and `śvāsau` as both breaths. The four beginning with pleasure are pleasure, pain, pleasant-mindedness, and displeasure—not four agreeable states.


**Close construe.** The fourth dhyāna, however, is
immovable because it is free from eight disturbances:
vitarka and vicāra, the two breaths, and the group of
four beginning with pleasure.

## 5. Translation

### Literal Translation

> Because it is free from eight disturbances, the
> fourth is immovable: vitarka and vicāra, the two
> breaths, and the four beginning with pleasure.

### Bhāṣya-informed study translation

> The fourth dhyāna, however, is immovable because it is free
> from eight disturbances: vitarka and vicāra, the two breaths,
> and the four beginning with pleasure, namely pleasure, pain,
> pleasant-mindedness, and displeasure.

## 6. Philosophical Translation

> Immovability receives a determinate scope: the fourth
> dhyāna is free from each of eight specified disturbances.
> The alternative explanation emphasizes what cannot
> shake it, illustrated by the steadiness of a lamp
> where there is no wind.

This predicate concerns the attainment under discussion.
It does not establish permanence, freedom from every
possible condition, or final liberation. The positive
fourth-dhyāna factors already enumerated remain relevant
to what this attainment is.

## 7. Technical Vocabulary

**`Apakṣāla`.** Disturbance or fault. Its contextual
force comes from the contrast with immovability and
the explicit list. Vitarka and vicāra were counted
as first-dhyāna factors; calling them disturbances
here does not make every occurrence a kleśa or an
unwholesome state.

**`Āniñja / āneñjya`.** Immovable or unshaken. These
related verse and prose forms characterize the fourth
dhyāna in this local comparison. Their meaning should
not be expanded beyond the reasons the passage supplies.

**`Vitarka / vicāra`.** Initial application and sustained
examination, retained as technical terms in translation.
The prose securely resolves the verse's compressed
pair. Their earlier role as factors and their present
exclusion answer different questions.

**`Śvāsa / praśvāsa`.** The two respiratory movements,
rendered together as inhalation and exhalation. The
passage asserts their absence in the fourth attainment;
it provides no physiological mechanism or procedure
for producing that absence.

**`Sukhādi catuṣṭaya`.** Pleasure, pain, pleasant-mindedness,
and displeasure. The distinction between sukha and
saumanasya follows the preceding discussion. In view
of VAK 8.09's debate, the present study does not impose
“bodily pleasure” as an uncontested gloss of every sukha.

**`Akampanīyatva`.** Inability to be shaken. The alternative
account specifies the four factors by which the fourth
dhyāna cannot be shaken.

**`Nirvāta-pradīpa-nidarśana`.** Illustration of a lamp
in a windless place. This supports the reported alternative;
it is not a separate clause of the kārikā.

## 8. Logical Determination

The principal account says the fourth dhyāna is immovable because none of eight specified disturbances occurs there [verse; prose]. A separate `apare` explanation describes inability to be shaken by four factors; the two formulations remain distinct.

**Signature.** `Disturbance(x)`; `AbsentFrom(level,x)`; `Immovable(level)`; `CannotShake(level,x)`.

**Finite data.** The eight exclusions are vitarka, vicāra, two breaths, and four feelings. The alternative states a four-member “cannot shake” relation, not a replacement eight-item inventory.

```nltk-valuation
fourth => fourth
vitarka => vitarka
vicara => vicara
inbreath => inbreath
outbreath => outbreath
sukha => sukha
duhkha => duhkha
saumanasya => saumanasya
daurmanasya => daurmanasya
Disturbance => {vitarka, vicara, inbreath, outbreath, sukha, duhkha, saumanasya, daurmanasya}
AbsentFrom => {(fourth,vitarka),(fourth,vicara),(fourth,inbreath),(fourth,outbreath),(fourth,sukha),(fourth,duhkha),(fourth,saumanasya),(fourth,daurmanasya)}
Immovable => {fourth}
CannotShake => {(fourth,vitarka),(fourth,vicara),(fourth,priti),(fourth,sukha)}
priti => priti
```

**Theories (attributed accounts).**

```nltk-fol
# THEORY Vasubandhu — [verse] eight absent; [prose] not one remains
Immovable(fourth)
all x.(Disturbance(x) -> AbsentFrom(fourth,x))

# THEORY apare — [prose] inability to be shaken by the four named factors
CannotShake(fourth,vitarka)
CannotShake(fourth,vicara)
CannotShake(fourth,priti)
CannotShake(fourth,sukha)
```

**Results (NLTK).** The checker confirms both theories in the finite valuation. It checks the stated relations; it does not prove the theories equivalent or that each lower dhyāna contains every listed disturbance.

**Scope cautions.** The eight-item exclusion does not say all eight vanish only upon reaching the fourth. `Prīti` is aligned with saumanasya by the preceding account, but the `apare` list is not explicitly eight items. The claim about breaths is doctrinal, not a breath-control instruction; immovable is not permanent or liberated.

## 9. Interpretive Note

**Stability has a stated basis.** The explanation names
the conditions excluded rather than leaving “immovable”
as an unrestricted epithet. At the same time, an
absence-list is not the complete constitution of the
attainment: neutral feeling, qualified equanimity and
mindfulness, and samādhi have already been enumerated.

**Scope of the bodily claim.** The breaths belong to
the doctrinal list in the source. The local passage
does not establish a modern physiological account,
and it does not instruct deliberate breath retention.
The study preserves the claim at its textual scope.

**Witness cautions.** The running source's `señjitāni`
is retained as a witness reading in the introductory
contrast. “Subject to movement” conveys its contextual
opposition to āniñja without silently reconstructing
the form. The prose uses āneñjya beside the verse's
āniñja and expands cāra to vicāra. None of these
observations changes the research witnesses.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates the relation between the predicate
of stability and its specified conditions. Yoga Technē,
its kriyā–karma companion, concerns the effective
exercise of an attainment so determined. The source's
list supports disciplined specification of what counts
as disturbance within this comparison.

For Organon, preserve the eight-member set, the scope
of the exclusion, the continuing positive factors,
and the attribution of the alternative explanation.
A finite exclusion does not by itself license an
unrestricted claim of invulnerability. This is a
project use of the source's distinctions, not a
claim that Vasubandhu is proposing Organon architecture.

**Review status.** Provisional, Bhāṣya-controlled study.
The eight members, their absence in the fourth dhyāna,
the alternative four-factor explanation and lamp image,
and the transition from attainment feelings to rebirth
feelings have been checked against the local research
and running source.

## 10. OWL++ Seed

```text
Class: DhyanaAttainment
Class: SpecifiedDisturbanceSet
Class: ReportedExplanation
Class: FeelingDetermination

ObjectProperty: freeFromEachMemberOf
ObjectProperty: cannotBeShakenBy
ObjectProperty: illustratedBy
ObjectProperty: hasFeelingDetermination

EightDisturbances:
    members: Vitarka, Vicara, Svasa, Prasvasa,
             Sukha, Duhkha, Saumanasya, Daurmanasya
    count: 8

FourthDhyanaAttainment:
    freeFromEachMemberOf: EightDisturbances
    designation: Aninja
    feelingDetermination: NeutralFeeling

AlternativeExplanation:
    attribution: OtherAuthorities
    subject: FourthDhyanaAttainment
    cannotBeShakenBy: Vitarka, Vicara, Priti, Sukha
    illustratedBy: LampInWindlessPlace

ProjectConstraint: Exclusion concerns the specified eight disturbances.
ProjectConstraint: Do not infer all eight occur in every lower dhyana.
ProjectConstraint: Do not infer all eight first cease at the fourth dhyana.
ProjectConstraint: Neutral feeling and the equanimity factor remain distinct.
ProjectConstraint: Preserve the alternative explanation as attributed.
ProjectConstraint: Do not transfer attainment feelings directly to rebirth.
```

This is a declarative project seed, not executable OWL.
VAK 8.12 next determines the feelings in dhyāna rebirth,
distinguishing them from those of meditative attainment.
