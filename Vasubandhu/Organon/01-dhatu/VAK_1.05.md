# VAK_1.05 — The Pure, and Space

## 1. Sanskrit (Devanāgarī)

```sanskrit
अनास्रवा मार्गसत्यं त्रिविधं चाप्यसंस्कृतम् ।
आकाशं द्वौ निरोधौ च तत्राकाशमनावृतिः ॥ १.०५ ॥
```

## 2. Sanskrit (IAST)

```text
anāsravā mārgasatyaṃ trividhaṃ cāpy asaṃskṛtam /
ākāśaṃ dvau nirodhau ca tatrākāśam anāvṛtiḥ // 1.05 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| anāsravāḥ | adjective; nominative plural | pure; the subject supplied from 1.04 |
| mārgasatyam | mārga-satyam; nominative neuter singular | the Truth of the Path |
| trividham | nominative neuter singular | threefold |
| ca api | particles | and also |
| asaṃskṛtam | nominative neuter singular | the unconditioned |
| ākāśam | nominative neuter singular | space |
| dvau nirodhau | masculine dual nominative | the two cessations |
| tatra | indeclinable | among these |
| anāvṛtiḥ | an-āvṛtiḥ; nominative feminine singular | non-obstruction; the predicate of space |

**Grammar tokens.** Verse-order IAST with sandhi opened; *ca api* and
*dvau nirodhau* become separate leaves. Space occurs twice. The Pure
Dharmas are recovered from 1.04 semantically, without a covert noun leaf.
The Bhāṣya names the two cessations; the verse supplies their dual count.

```text
# tokens: anāsravāḥ mārgasatyam trividham ca api asaṃskṛtam ākāśam dvau nirodhau ca tatra ākāśam anāvṛtiḥ
```

## 4. Grammar

The plural Pure classification encompasses the Path Truth and the
threefold unconditioned. *Trividham* agrees with neuter *asaṃskṛtam*;
*dvau* agrees with masculine dual *nirodhau*. The definition of space
is cross-gender nominal predication, not adjective agreement.

```nltk-fcfg
% start S
# tokens: anāsravāḥ mārgasatyam trividham ca api asaṃskṛtam ākāśam dvau nirodhau ca tatra ākāśam anāvṛtiḥ
S[SEM=<(?p(?path)(?u) & ?roster & ?space)>] -> PURE[SEM=?p] PATH[SEM=?path] UNCONDITIONED[SEM=?u] ROSTER[SEM=?roster] SPACEDEF[SEM=?space]
UNCONDITIONED[SEM=<?three(?u)>] -> THREE[CASE=nom,NUM=?n,GEN=?g,SEM=?three] AND ALSO UNCOND[CASE=nom,NUM=?n,GEN=?g,SEM=?u]
ROSTER[SEM=<all x.(Unconditioned(x) <-> (x=?space | ?cessations(x)))>] -> SPACE[CASE=nom,SEM=?space] TWO[CASE=nom,NUM=?n,GEN=?g] CESSATIONS[CASE=nom,NUM=?n,GEN=?g,SEM=?cessations] AND
SPACEDEF[SEM=<?pred(?space)>] -> AMONG SPACE[CASE=nom,NUM=?n,SEM=?space] NONOBSTRUCTION[CASE=nom,NUM=?n,SEM=?pred]
PURE[CASE=nom,NUM=pl,SEM=<\P.\Q.all x.(Dharma(x) -> (Pure(x) <-> (P(x) | Q(x))))>] -> 'anāsravāḥ'
PATH[CASE=nom,NUM=sg,GEN=n,SEM=<\x.PathTruth(x)>] -> 'mārgasatyam'
THREE[CASE=nom,NUM=sg,GEN=n,SEM=<\P.\x.P(x)>] -> 'trividham'
AND -> 'ca'
ALSO -> 'api'
UNCOND[CASE=nom,NUM=sg,GEN=n,SEM=<\x.Unconditioned(x)>] -> 'asaṃskṛtam'
SPACE[CASE=nom,NUM=sg,GEN=n,SEM=<space>] -> 'ākāśam'
TWO[CASE=nom,NUM=dual,GEN=m] -> 'dvau'
CESSATIONS[CASE=nom,NUM=dual,GEN=m,SEM=<\x.(x=discriminative_cessation | x=nondiscriminative_cessation)>] -> 'nirodhau'
AMONG -> 'tatra'
NONOBSTRUCTION[CASE=nom,NUM=sg,GEN=f,SEM=<\x.NonObstruction(x)>] -> 'anāvṛtiḥ'
```

```nltk-dep
'anāsravāḥ' -> 'mārgasatyam' | 'asaṃskṛtam'
'asaṃskṛtam' -> 'trividham' | 'ca' | 'api' | 'ākāśam' | 'nirodhau'
'nirodhau' -> 'dvau' | 'ca'
'anāvṛtiḥ' -> 'tatra' | 'ākāśam'
```

**Close construe.** The Pure are the Path Truth and the threefold
unconditioned: space and two cessations. Among them space is non-obstruction.

The scope of Pure comes from the division in 1.04. The roster names the
cessations using the Bhāṣya's referents, without inserting those names into
the witness. Distinctness and the resulting count of three are checked
in the valuation, not derived by arithmetic from *trividham*. The
Bhāṣya's “where Form can move” explains non-obstruction; it does not
classify space as a conditioned container or as a bodily support.

## 5. Translation

### Literal Translation

> The pure are the Truth of the Path and also the threefold unconditioned:
> space and the two cessations. Among these, space is non-obstruction.

### Bhāṣya-informed study translation

> The Path Truth is Pure, and the unconditioned is also threefold: space
> and the two cessations, cessation through discrimination and cessation
> not through discrimination. Among these, space is non-obstruction, where
> Form can move.

## 6. Philosophical Translation

The pure member named in the previous verse is enumerated here. It is not the unconditioned as such.

The Truth of the Path is conditioned, and pure. Space and the two cessations are unconditioned, and pure. The reason is the same failure: the *āsravas* do not persist in them. Persistence was the test of the impure. Its absence is the test of the pure.

Space is defined. The two cessations are named. Their definitions are the next verse.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| anāsrava | pure | the *āsravas* do not persist |
| mārga-satya | Truth of the Path | conditioned and pure |
| asaṃskṛta | unconditioned | space and the two cessations |
| ākāśa | space | non-obstruction |
| anāvṛti | non-obstruction | where Form can move |
| pratisaṃkhyā-nirodha | cessation through discrimination | named here; defined in 1.06 |
| apratisaṃkhyā-nirodha | cessation not through discrimination | named here; defined in 1.06 |
| anuśerate | persist | the verb that fails in the pure |

## 8. Logical Determination

**Kārikā, derived with resolved referents.** Pure does not mean
unconditioned: the Path is included without being one of the three.

```nltk-sem
# derived by the section 4 parse
((all x.(Dharma(x) -> (Pure(x) <-> (PathTruth(x) | Unconditioned(x))))) & (all x.(Unconditioned(x) <-> (x=space | (x=discriminative_cessation | x=nondiscriminative_cessation)))) & NonObstruction(space))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((all x.(Dharma(x) -> (Pure(x) <-> (PathTruth(x) | Unconditioned(x))))) & (all x.(Unconditioned(x) <-> (x=space | (x=discriminative_cessation | x=nondiscriminative_cessation)))) & NonObstruction(space))
# THEORY prose
# EXPECT prose T
all x.(PathTruth(x) -> (Dharma(x) & Conditioned(x)))
all x.(Unconditioned(x) -> (Dharma(x) & -Conditioned(x)))
# THEORY rejected_pure_means_unconditioned
# EXPECT rejected_pure_means_unconditioned F
all x.(Pure(x) -> Unconditioned(x))
```

```nltk-valuation
space => space_case
discriminative_cessation => discriminative
nondiscriminative_cessation => nondiscriminative
Dharma => {path,ordinary,space_case,discriminative,nondiscriminative}
Pure => {path,space_case,discriminative,nondiscriminative}
PathTruth => {path}
Unconditioned => {space_case,discriminative,nondiscriminative}
Conditioned => {path,ordinary}
NonObstruction => {space_case}
```

**Model checks.** The three unconditioned representatives must be distinct;
an extra unconditioned member falsifies the roster. The conditioned Path
refutes the rejected equation between Pure and unconditioned. Removing
space's non-obstruction falsifies its definition.

**Bhāṣya determination.** The following preserves the earlier overview.
Form's possible movement is explanatory prose, not an extra derived
predicate in this pilot.

```text
pure
    = Truth of the Path
    + threefold unconditioned
        = space
        + cessation through discrimination
        + cessation not through discrimination

conditioned does not entail impure
pure does not entail unconditioned

space
    = non-obstruction
    = where Form can move
```

| Dharma class | Conditioned? | Pure? |
|---|---:|---:|
| conditioned, other than the Path | yes | no |
| Truth of the Path | yes | yes |
| space and the two cessations | no | yes |

## 9. Interpretive Note

**Translation note.** The Bhāṣya explains that the Path Truth and the three unconditioned dharmas are Pure because the outflows do not persist through them; it identifies the two cessations and defines space as non-obstruction.

The verse completes the division opened in 1.04. Four dharmas are pure. One of them is conditioned. Space receives its definition. The two cessations do not.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_05 a vak:Karika ;
    vak:hasTopic vak:PureDharmas ;
    vak:belongsTo vak:Dhatunirdesa .

vak:PathTruth a vak:ConditionedDharma, vak:PureDharma .
vak:Akasha a vak:UnconditionedDharma, vak:PureDharma ;
    vak:definedAs vak:NonObstruction .
vak:PratisamkhyaNirodha a vak:UnconditionedDharma, vak:PureDharma .
vak:ApratisamkhyaNirodha a vak:UnconditionedDharma, vak:PureDharma .
```
