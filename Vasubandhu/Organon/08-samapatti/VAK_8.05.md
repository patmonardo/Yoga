# VAK_8.05 — Eight Fundamental Attainments and Their Admissible Modes

## 1. Sanskrit (Devanāgarī)

```sanskrit
इति मौलं समापत्तिद्रव्यमष्टविधं त्रिधा ।
सप्त आस्वादनवच्छुद्धानास्रवाणि अष्टमं द्विधा ॥ ८.०५ ॥
```

## 2. Sanskrit (IAST)

```text
iti maulaṃ samāpattidravyam aṣṭavidhaṃ tridhā |
sapta āsvādanavacchuddhānāsravāṇi aṣṭamaṃ dvidhā || 8.05 ||
```

The Sanskrit follows the local kārikā witness. The
Devanāgarī renders that reading. The running source has
`āsvādanāvacchūddhānāsravāṇi`; the explicit prose list
controls the three categories despite these vowel-length
differences.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `iti` | summarizing particle | thus; gathering the preceding series |
| `maulam` | nominative singular neuter adjective | fundamental or principal |
| `samāpatti-dravyam` | nominative singular neuter compound | the substantive inventory of attainments |
| `aṣṭa-vidham` | nominative singular neuter adjective | eightfold |
| `tridhā` | adverb | threefold in the classification that follows |
| `sapta` | numeral | seven [principal attainments] |
| `āsvādana-vat-śuddha-anāsravāṇi` | neuter plural coordinated expression; `vat + śuddha` → `vacchuddha`, `śuddha + anāsrava` → `śuddhānāsrava` | three alternatives, expanded by the prose as `āsvādanāsaṃprayuktāni`, `śuddhakāni`, `anāsravāṇi`: associated with savoring, pure, uncontaminated |
| `aṣṭamam` | nominative singular neuter ordinal | the eighth [attainment] |
| `dvidhā` | adverb | twofold |

## 4. Grammar

The verse first gathers eight principal attainments, then distributes the three modes over seven and two modes over the eighth. The Bhāṣya identifies the eighth as bhavāgra and excludes an uncontaminated instance.

```nltk-fcfg
% start S
# tokens: iti maulaṃ samāpattidravyam aṣṭavidhaṃ tridhā sapta āsvādanavacchuddhānāsravāṇi aṣṭamaṃ dvidhā ∅-bhavāgram
S -> CL[K=inventory] CL[K=seven_modes] CL[K=eighth_modes]
CL[K=inventory] -> PTCL[SUMMARY=yes] ADJ[CASE=nom,NUM=sg,GEN=n,PRINCIPAL=yes] N[CASE=nom,NUM=sg,GEN=n] ADJ[CASE=nom,NUM=sg,GEN=n,COUNT=eight]
CL[K=seven_modes] -> ADV[COUNT=three] NUM[CASE=nom,NUM=pl,GEN=n] ADJ[CASE=nom,NUM=pl,GEN=n,MODES=three]
CL[K=eighth_modes] -> NUM[CASE=nom,NUM=sg,GEN=n,REF=eighth] ADV[COUNT=two] N[CASE=nom,NUM=sg,GEN=n,SUPPLIED=prose,REF=eighth]
PTCL[SUMMARY=yes] -> 'iti'
ADJ[CASE=nom,NUM=sg,GEN=n,PRINCIPAL=yes] -> 'maulaṃ'
N[CASE=nom,NUM=sg,GEN=n] -> 'samāpattidravyam'
ADJ[CASE=nom,NUM=sg,GEN=n,COUNT=eight] -> 'aṣṭavidhaṃ'
ADV[COUNT=three] -> 'tridhā'
NUM[CASE=nom,NUM=pl,GEN=n] -> 'sapta'
ADJ[CASE=nom,NUM=pl,GEN=n,MODES=three] -> 'āsvādanavacchuddhānāsravāṇi'
NUM[CASE=nom,NUM=sg,GEN=n,REF=eighth] -> 'aṣṭamaṃ'
ADV[COUNT=two] -> 'dvidhā'
N[CASE=nom,NUM=sg,GEN=n,SUPPLIED=prose,REF=eighth] -> '∅-bhavāgram'
```

```nltk-dep
'samāpattidravyam' -> 'iti' | 'maulaṃ' | 'aṣṭavidhaṃ'
'sapta' -> 'tridhā' | 'āsvādanavacchuddhānāsravāṇi'
'∅-bhavāgram' -> 'aṣṭamaṃ' | 'dvidhā'
```

The singular inventory is collective, not a permanent substance; access attainments are not added. The modes are alternatives, not simultaneous qualities; `sapta` excludes bhavāgra, which has no uncontaminated form.


**Close construe.** Thus the principal attainment inventory
is eightfold. Seven are threefold—as savoring-associated,
pure, and uncontaminated—while the eighth is twofold.

## 5. Translation

### Literal Translation

> Thus the fundamental attainment inventory is eightfold.
> Seven are threefold: savoring-associated, pure, and
> uncontaminated. The eighth is twofold.

### Bhāṣya-informed study translation

> The four dhyānas and four formless attainments constitute
> the fundamental attainment inventory, which is thus eightfold.
> Seven of them are threefold: associated with savoring, pure,
> and uncontaminated. The eighth, the summit of existence, is
> twofold: savoring-associated and pure.

## 6. Philosophical Translation

> Position in the attainment series and the mode in
> which an attainment occurs are different determinations.
> The highest member of the series does not admit every
> mode available below it. Its position alone therefore
> cannot establish uncontaminated status.

The classification is neither a single ascending ladder
of liberative value nor a completely unrestricted pairing
of levels and modes. The eighth member supplies an
explicit constraint on their combinations.

## 7. Technical Vocabulary

**`Maula`.** Principal or fundamental. This distinguishes
the eight main attainments from access states without
denying the latter's role in the broader exposition.

**`Samāpattidravya`.** The actual attainment or substantive
attainment inventory under classification. “Substance”
would be misleading if taken to imply permanence or
an independent metaphysical bearer. The prose explicitly
enumerates the four dhyānas and four formless states.

**`Āsvādanavat / āsvādanāsaṃprayukta`.** With savoring,
or associated with relish. The second is the prose's
expansion. The technical explanation involving craving
belongs to the next verse; the present passage identifies
its place in the classification.

**`Śuddha / śuddhaka`.** Pure. It is a separate category
from `anāsrava`, so “pure” must not be silently rendered
as “uncontaminated” and collapse the threefold list.
The next verse supplies its positive definition.

**`Anāsrava`.** Without influxes or uncontaminated.
Its exclusion from the eighth principal attainment
is explicit. It does not mean an unconditioned entity
merely because the translated word suggests purity.

**`Bhavāgra`.** Summit of existence. Here it identifies
the eighth attainment, neither-perception-nor-non-perception.
It is not a ninth state above the four formless attainments
and not a synonym for final liberation.

## 8. Logical Determination

The matrix is data; the exception is a rule checked against it. Provenance
tags: `[verse]`, `[prose]`. Constants are ASCII and longer than one letter
(NLTK reads `d1` as a variable).

**Signature.** `Principal(x)` (one of the eight), `Mode(m)`, `Admits(x,m)`
(the classification admits mode `m` for attainment `x`), `Summit(x)`
(bhavāgra), `Attenuated(x)` (the 8.04 attenuation of perception).

**Facts (the attainment-mode matrix).** One row per admitted pair; the
extension of `Admits` is a two-column frame. `Admits` has 23 rows: seven
attainments with three modes, and bhavāgra with two. This count is read from
the data, not derived by the logic, and it is an editorial count, not a
replacement for the source's eight principal kinds.

```nltk-valuation
first => first
second => second
third => third
fourth => fourth
space => space
consciousness => consciousness
nothingness => nothingness
bhavagra => bhavagra
savor => savor
pure => pure
unc => unc
Principal => {first, second, third, fourth, space, consciousness, nothingness, bhavagra}
Mode => {savor, pure, unc}
Summit => {bhavagra}
Admits => {(first,savor),(first,pure),(first,unc),(second,savor),(second,pure),(second,unc),(third,savor),(third,pure),(third,unc),(fourth,savor),(fourth,pure),(fourth,unc),(space,savor),(space,pure),(space,unc),(consciousness,savor),(consciousness,pure),(consciousness,unc),(nothingness,savor),(nothingness,pure),(nothingness,unc),(bhavagra,savor),(bhavagra,pure)}
```

**Rules (verse and prose).**

```nltk-fol
# THEORY shared
# [verse] sapta ... tridhā: the seven admit all three modes
all x.((Principal(x) & -Summit(x)) -> (Admits(x,savor) & Admits(x,pure) & Admits(x,unc)))
# [verse] aṣṭamaṃ dvidhā; [prose] ∅-bhavāgram: the eighth admits two, not the third
Principal(bhavagra)
Summit(bhavagra)
Admits(bhavagra,savor)
Admits(bhavagra,pure)
-Admits(bhavagra,unc)
# [prose] the one exception: only the summit lacks the uncontaminated mode
all x.((Principal(x) & -Admits(x,unc)) -> Summit(x))
```

**Model check (`Model.satisfy` against the facts).** The three rules above
hold in the matrix. The naive uniform rule
`all x.(Principal(x) -> Admits(x,unc))` is false there, so the exception
determines the rule's scope: threefold classification does not extend
uniformly to the eighth.

**Proof check (NLTK `TableauProver` and `ResolutionProver` agree).** From
the first rule and the summit's missing mode, `Summit(bhavagra)` follows: the
summit is not among the seven. The converse overreach is blocked: that the
summit lacks `unc` does not entail that no lower attainment admits it: given
any non-summit `Principal` (such as `first`),
`exists x.(Principal(x) & Admits(x,unc))` is derivable from the first rule.

**Scope cautions.**
- `Admits` is admissibility in the classification, not simultaneous
  possession of all three modes, and not a guarantee that a practitioner who
  reaches a level has acquired every admitted mode. No rule asserts
  `Has(person,x,m)`.
- No rule links `Attenuated(bhavagra)` to `-Admits(bhavagra,unc)`. VAK 8.04
  explains the attenuation of perception; VAK 8.05 states the missing mode
  without deriving it. The grammar permits no unstated “because”.
- The relation to VAK 8.01 is by mode: ethical and soteriological identity is
  not required of every occurrence of the name. The detailed account of
  savoring and pure modes is VAK 8.06.

## 9. Interpretive Note

**Distinct coordinates, constrained combinations.** The
research analysis calls level and mode independent
classifications. They are distinguishable coordinates,
but not independent in the sense that every combination
is possible: the bhavāgra exclusion is precisely a
constraint relating them. A faithful formal model must
retain both their difference and their connection.

**Source boundary.** The unit ends at Pradhan 437|02.
The next statements explain savoring through craving,
pure attainment as worldly wholesome, and uncontaminated
attainment as supramundane. Those belong to VAK 8.06;
this study does not silently fold their full argument
into the present enumeration.

**Witness cautions.** The running source prints
`āsvādanāvacchūddhānāsravāṇi` where the local kārikā
has `āsvādanavacchuddhānāsravāṇi`. The prose separately
names all three modes and resolves the intended list.
Its final `anāsrava nāsti` is compressed but unambiguous
in denying the uncontaminated mode of bhavāgra. The
underlying witnesses remain unchanged.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates the attainment kinds and the
conditions under which their modal designations apply.
Yoga Technē, its kriyā–karma companion, concerns the
cultivation and exercise of attainments under those
conditions. A position in the series does not by itself
settle the quality of its exercise.

For Organon representation, this gives a precise reason
to record both level and mode. The record must also
encode exclusions, since a two-coordinate description
is insufficient if it permits combinations the source
rejects. The eighth attainment makes the constraint
concrete rather than merely formal.

This is a project use of the classification. It does
not turn the source's attainment hierarchy into a generic
score of capability or imply that maximal refinement
in every system has the same relation to liberation.
The doctrinal result is local and definite: bhavāgra
has no uncontaminated form in this account.

**Review status.** Provisional, Bhāṣya-controlled study.
The eight principal kinds, seven threefold members,
three prose-expanded modes, eighth-member identification,
and explicit uncontaminated exclusion have been checked
against the local extract and running source. Detailed
mode definitions remain the next verse's task.

## 10. OWL++ Seed

```text
Class: PrincipalAttainment
Class: AttainmentMode

ObjectProperty: admitsMode
ObjectProperty: excludesMode

PrincipalAttainments:
    FirstDhyana
    SecondDhyana
    ThirdDhyana
    FourthDhyana
    InfiniteSpace
    InfiniteConsciousness
    Nothingness
    NeitherPerceptionNorNonPerception

FirstSeven:
    admittedModes: SavoringAssociated, Pure, Uncontaminated

Bhavagra:
    attainment: NeitherPerceptionNorNonPerception
    admittedModes: SavoringAssociated, Pure
    excludedMode: Uncontaminated

ProjectConstraint: Principal count excludes access attainments.
ProjectConstraint: Pure and uncontaminated are distinct categories.
ProjectConstraint: Admissible modes need not be simultaneously possessed.
ProjectConstraint: Distinct coordinates do not imply unrestricted combinations.
ProjectConstraint: Do not invent the causal reason for the eighth's exclusion here.
ProjectConstraint: Detailed mode definitions continue in VAK 8.06.
```

This is a declarative project seed, not executable OWL.
VAK 8.06 next defines savoring-associated, pure, and
uncontaminated attainment and the relation of savoring
to its object.
