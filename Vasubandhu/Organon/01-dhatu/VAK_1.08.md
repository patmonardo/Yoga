# VAK_1.08 — The Impure Division of the Bases

## 1. Sanskrit (Devanāgarī)

```sanskrit
ये सास्रवा उपादानस्कन्धास्ते सरणा अपि ।
दुःखं समुदयो लोको दृष्टिस्थानं भवश्च ते ॥ १.०८ ॥
```

## 2. Sanskrit (IAST)

```text
ye sāsravā upādānaskandhās te saraṇā api /
duḥkhaṃ samudayo loko dṛṣṭisthānaṃ bhavaś ca te // 1.08 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| ye | nominative masculine plural | those which. Restricts the five Bases of 1.07 |
| sāsravāḥ | sa-āsrava; nominative masculine plural | Impure. The summary division |
| upādānaskandhāḥ | upādāna-skandha; nominative masculine plural | Bases of appropriation. Not every Base |
| te | nominative masculine plural | they. Same field |
| saraṇāḥ | sa-raṇa; nominative masculine plural | with conflict. Coextensive with the Impure field |
| api | particle | also. Not a second inventory |
| duḥkham | nominative neuter singular | suffering |
| samudayaḥ | nominative masculine singular | origin |
| lokaḥ | nominative masculine singular | world. Here, what dissolves |
| dṛṣṭisthānam | dṛṣṭi-sthāna; nominative neuter singular | station of views. Not the station of prajñā |
| bhavaḥ | nominative masculine singular | becoming |
| ca | particle | and. The five names are one field |
| te | nominative masculine plural | they, resumed |

**Grammar tokens.** Verse-order IAST with sandhi opened. Both occurrences
of *te* remain; each resumes the Impure restriction, not every Base.
The compound *upādāna-skandhāḥ* remains one leaf. No covert token is needed.

```text
# tokens: ye sāsravāḥ upādāna-skandhāḥ te saraṇāḥ api duḥkham samudayaḥ lokaḥ dṛṣṭisthānam bhavaḥ ca te
```

## 4. Grammar

The relative *ye* restricts the conditioned field resumed from 1.07.
Plural *sāsravāḥ*, *upādāna-skandhāḥ*, and *saraṇāḥ* share agreement.
The five final predicate nouns vary in gender but do not introduce five
new subjects. Both *te* resumptions preserve the same restriction.

```nltk-fcfg
% start S
# tokens: ye sāsravāḥ upādāna-skandhāḥ te saraṇāḥ api duḥkham samudayaḥ lokaḥ dṛṣṭisthānam bhavaḥ ca te
S[SEM=<(?a & ?c & ?names)>] -> APPROPRIATION[SEM=?a] CONFLICT[SEM=?c] NAMES[SEM=?names]
APPROPRIATION[SEM=<?rel(?impure)(?base)>] -> REL[CASE=nom,NUM=?n,GEN=?g,SEM=?rel] IMPURE[CASE=nom,NUM=?n,GEN=?g,SEM=?impure] BASE[CASE=nom,NUM=?n,GEN=?g,SEM=?base]
CONFLICT[SEM=<?scope(?conflict)>] -> CORR[CASE=nom,NUM=?n,GEN=?g,SEM=?scope] CONFLICTHEAD[CASE=nom,NUM=?n,GEN=?g,SEM=?conflict] ALSO
NAMES[SEM=<?scope(\x.(?suffering(x) & ?origin(x) & ?world(x) & ?views(x) & ?becoming(x)))>] -> SUFFERING[CASE=nom,SEM=?suffering] ORIGIN[CASE=nom,SEM=?origin] WORLD[CASE=nom,SEM=?world] VIEWS[CASE=nom,SEM=?views] BECOMING[CASE=nom,SEM=?becoming] AND CORR[CASE=nom,NUM=pl,GEN=m,SEM=?scope]
REL[CASE=nom,NUM=pl,GEN=m,SEM=<\P.\Q.all x.((Dharma(x) & Conditioned(x)) -> (P(x) <-> Q(x)))>] -> 'ye'
IMPURE[CASE=nom,NUM=pl,GEN=m,SEM=<\x.Impure(x)>] -> 'sāsravāḥ'
BASE[CASE=nom,NUM=pl,GEN=m,SEM=<\x.AppropriationBaseMember(x)>] -> 'upādāna-skandhāḥ'
CORR[CASE=nom,NUM=pl,GEN=m,SEM=<\P.all x.((Dharma(x) & Conditioned(x) & Impure(x)) -> P(x))>] -> 'te'
CONFLICTHEAD[CASE=nom,NUM=pl,GEN=m,SEM=<\x.WithConflict(x)>] -> 'saraṇāḥ'
ALSO -> 'api'
SUFFERING[CASE=nom,NUM=sg,GEN=n,SEM=<\x.Suffering(x)>] -> 'duḥkham'
ORIGIN[CASE=nom,NUM=sg,GEN=m,SEM=<\x.Origin(x)>] -> 'samudayaḥ'
WORLD[CASE=nom,NUM=sg,GEN=m,SEM=<\x.DissolvingWorld(x)>] -> 'lokaḥ'
VIEWS[CASE=nom,NUM=sg,GEN=n,SEM=<\x.StationOfViews(x)>] -> 'dṛṣṭisthānam'
BECOMING[CASE=nom,NUM=sg,GEN=m,SEM=<\x.Becoming(x)>] -> 'bhavaḥ'
AND -> 'ca'
```

```nltk-dep
'upādāna-skandhāḥ' -> 'ye' | 'sāsravāḥ'
'saraṇāḥ' -> 'te' | 'api'
'duḥkham' -> 'samudayaḥ' | 'lokaḥ' | 'dṛṣṭisthānam' | 'bhavaḥ' | 'te'
'bhavaḥ' -> 'ca'
```

**Close construe.** Those which are Impure are Bases of appropriation;
they are also with conflict. Those same are suffering, origin, world,
station of views, and becoming.

`AppropriationBaseMember` classifies a Dharma under a Base of appropriation;
it does not identify an individual Dharma with an entire Base. The first
clause is read as a class specification, as the Bhāṣya confirms. The
remaining clauses predicate their names of that restricted field without
deriving their explanatory mechanisms or asserting unrestricted converse
rules. The conditioned Pure Path lies outside the restriction.

The commentary distinguishes three readings of appropriation: the Bases
arise from afflictions, are governed by them, or give rise to them. These
are different directed relations, not a single automatic transition.
Its working *lujyata* explanation of *loka* remains marked in the paired
study; the grammar does not resolve that textual question.

## 5. Translation

### Literal Translation

> Those which are Impure are the Bases of appropriation. They are also with
> conflict. They are suffering, origin, world, the station of views, and
> becoming.

### Bhāṣya-informed study translation

> Those conditioned dharmas that are with outflows are Bases of
> appropriation; they too are with conflict. These same dharmas are
> suffering, origin, the world, the station of views, and becoming.

## 6. Philosophical Translation

The five Bases are divided. The Impure are the Bases of appropriation, and they are also the field of conflict. That same field is suffering, origin, world, the station of views, and becoming.

```text
Five Bases       the gathered field of 1.07

Impure           Bases of appropriation
                 the summary division

Path             Conditioned and Pure
                 not within this division
```

## 7. Technical Vocabulary

| Sanskrit | Do not use as the reading | Determination |
|---|---|---|
| sāsrava | with outflows; lodging | Impure. Summary division |
| anāsrava | outflow-free | Pure. The Path is Conditioned and Pure |
| upādānaskandha | Base of clinging as a stain-word | Base of appropriation |
| saraṇa | with defilement, unspecified | with conflict |
| loka | a place | here, what dissolves |
| dṛṣṭisthāna | a viewpoint | station of views |
| bhava | existence as a realm-name | becoming |

## 8. Logical Determination

**Kārikā, derived.** All predicates below concern Dharmas in the
conditioned field of 1.07. The two resumptions retain the Impure
restriction. The universal claims have actual witnesses in the valuation.

```nltk-sem
# derived by the section 4 parse
((all x.((Dharma(x) & Conditioned(x)) -> (Impure(x) <-> AppropriationBaseMember(x)))) & (all x.((Dharma(x) & Conditioned(x) & Impure(x)) -> WithConflict(x))) & (all x.((Dharma(x) & Conditioned(x) & Impure(x)) -> (Suffering(x) & Origin(x) & DissolvingWorld(x) & StationOfViews(x) & Becoming(x)))))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((all x.((Dharma(x) & Conditioned(x)) -> (Impure(x) <-> AppropriationBaseMember(x)))) & (all x.((Dharma(x) & Conditioned(x) & Impure(x)) -> WithConflict(x))) & (all x.((Dharma(x) & Conditioned(x) & Impure(x)) -> (Suffering(x) & Origin(x) & DissolvingWorld(x) & StationOfViews(x) & Becoming(x)))))
# THEORY prose
# EXPECT prose T
all x.(AppropriationBaseMember(x) -> FiveBaseMember(x))
exists x.(Dharma(x) & Conditioned(x) & Pure(x) & FiveBaseMember(x) & -AppropriationBaseMember(x))
# THEORY rejected_every_base_is_appropriated
# EXPECT rejected_every_base_is_appropriated F
all x.(FiveBaseMember(x) -> AppropriationBaseMember(x))
```

```nltk-valuation
Dharma => {ordinary,path,space_case}
Conditioned => {ordinary,path}
Impure => {ordinary}
Pure => {path,space_case}
FiveBaseMember => {ordinary,path}
AppropriationBaseMember => {ordinary}
WithConflict => {ordinary}
Suffering => {ordinary}
Origin => {ordinary}
DissolvingWorld => {ordinary}
StationOfViews => {ordinary}
Becoming => {ordinary}
```

**Model checks.** Removing any predication from `ordinary` must fail.
Including the Pure Path among appropriation-Base members must also fail,
but removing a name from the Path cannot violate the verse's restricted
predication. Equal extensions in this small model do not prove synonymy
or unrestricted equivalence of the named determinations.

**Bhāṣya determination.** Conflict names afflictions as injuring oneself
and others. The five names have distinct explanations: opposition to the
Āryas, origination of suffering, dissolution, views persisting, and coming
to be. Their explanations remain prose here rather than invented causal
axioms.

**Organon interpretation.** The earlier schematic summary follows.
Its coextension claims describe this field; they must not be read as
unrestricted equalities among all uses of the predicates.

```text
Impure(x) ↔ AppropriationBase(x)
AppropriationBase(x) → Base(x)
Base(x) ↛ Impure(x)
Path is Conditioned and Pure

saraṇa ↔ Impure
duḥkha, samudaya, loka, dṛṣṭisthāna, bhava
    coextensive
    not synonyms
```

## 9. Interpretive Note

**Translation note.** The Bhāṣya explains the three relations behind the name Base of appropriation: the Bases arise from afflictions, are governed by them, or give rise to them. It also explains that afflictions are called conflicts because they injure oneself and others.

Impure is the top-level division within the five-Base field. Once the division is made, the word can drop. The sheath is later. The first two names are the first two Truths of what persists. The station of views is not the station of prajñā. A Rational Dharma does not Persist.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_08 a vak:Karika ;
    vak:hasTopic vak:ImpureDivision ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Impure vak:summaryDivision true ;
    vak:selects vak:AppropriationBase .
vak:AppropriationBase vak:subsetOf vak:Base .
vak:Path vak:isConditioned true ;
    vak:isPure true ;
    vak:not vak:Impure .
```