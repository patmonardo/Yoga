# VAK_8.22 — Eight Access Attainments and the First Access Exception

## 1. Sanskrit (Devanāgarī)

```sanskrit
अष्टौ सामन्तकान्येषां शुद्धादुःखासुखानि हि ।
आर्यं चाद्यं त्रिधा केचिद् अतर्कं ध्यानमन्तरम् ॥ ८.२२ ॥
```

## 2. Sanskrit (IAST)

```text
aṣṭau sāmantakāny eṣāṃ śuddhāduḥkhāsukhāni hi |
āryaṃ cādyaṃ tridhā kecid atarkaṃ dhyānam antaram || 8.22 ||
```

The Sanskrit follows the local kārikā study's grammatical
normalization, with Devanāgarī केचिद् matching its IAST
sandhi before atarkam. The running source's final
clause reads `atarka dhyānamantaram`; the local
study supplies atarkaṃ. The explicit prose identification
supports the meaning “without vitarka.”

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `aṣṭau` | numeral | eight |
| `sāmantakāni` | nominative plural neuter | access or neighboring attainments |
| `eṣām` | genitive plural demonstrative | of these [principal attainments] |
| `śuddhāduḥkhāsukhāni` | nominative plural neuter compound predicate | pure and neither painful nor pleasant |
| `hi` | explanatory particle | for; indeed |
| `āryam` | nominative singular neuter | noble, here uncontaminated |
| `ādyam` | nominative singular neuter | the first [access attainment] |
| `tridhā` | adverb | threefold |
| `kecit` | nominative plural indefinite pronoun | some [authorities] |
| `atarkam` | nominative singular neuter adjective | without vitarka |
| `dhyānam antaram` | nominative singular neuter noun and adjective | intermediate dhyāna |

`Sāmantakāni + eṣām` yields `sāmantakāny eṣām`;
`ca + ādyam` yields `cādyam`; `kecit + atarkam`
yields `kecid atarkam`. The prose separates the
compound predicates into being pure and being associated
with the neutral-feeling faculty.

## 4. Grammar

The verse counts one access attainment per principal attainment, then distinguishes access properties from the first-access exception and the separate intermediate dhyāna.

```nltk-fcfg
% start S
# tokens: aṣṭau sāmantakāny eṣām ∅-ekaikasy ∅-aikaikam śuddhāduḥkhāsukhāni hi āryaṃ cādyaṃ ∅-sāmantakam tridhā kecit atarkam dhyānam antaram
S -> CL[K=count] CL[K=properties] CL[K=first_access] CL[K=reported_view] CL[K=intermediate]
CL[K=count] -> NUM[COUNT=eight] N[CASE=nom,NUM=pl,GEN=n,KIND=access] PRON[CASE=gen,NUM=pl,GEN=n,REF=principal] COV[CASE=gen,NUM=sg,SUPPLIED=prose] COV[ONE=each,SUPPLIED=prose]
CL[K=properties] -> ADJ[CASE=nom,NUM=pl,GEN=n,QUALITY=pure_and_neutral] PTCL[EXPLAIN=yes]
CL[K=first_access] -> ADJ[CASE=nom,NUM=?n,GEN=?g,MODE=uncontaminated] ADJ[CASE=nom,NUM=?n,GEN=?g,ORDER=first] COV[CASE=nom,NUM=?n,GEN=?g,KIND=access,SUPPLIED=prose]
CL[K=reported_view] -> ADV[COUNT=three] N[CASE=nom,NUM=pl,GEN=m,VOICE=reported]
CL[K=intermediate] -> ADJ[CASE=nom,NUM=?n,GEN=?g,PRIV=vitarka] N[CASE=nom,NUM=?n,GEN=?g,KIND=intermediate] ADJ[CASE=nom,NUM=?n,GEN=?g,KIND=intermediate]
NUM[COUNT=eight] -> 'aṣṭau'
N[CASE=nom,NUM=pl,GEN=n,KIND=access] -> 'sāmantakāny'
PRON[CASE=gen,NUM=pl,GEN=n,REF=principal] -> 'eṣām'
COV[CASE=gen,NUM=sg,SUPPLIED=prose] -> '∅-ekaikasy'
COV[ONE=each,SUPPLIED=prose] -> '∅-aikaikam'
ADJ[CASE=nom,NUM=pl,GEN=n,QUALITY=pure_and_neutral] -> 'śuddhāduḥkhāsukhāni'
PTCL[EXPLAIN=yes] -> 'hi'
ADJ[CASE=nom,NUM=sg,GEN=n,MODE=uncontaminated] -> 'āryaṃ'
ADJ[CASE=nom,NUM=sg,GEN=n,ORDER=first] -> 'cādyaṃ'
COV[CASE=nom,NUM=sg,GEN=n,KIND=access,SUPPLIED=prose] -> '∅-sāmantakam'
ADV[COUNT=three] -> 'tridhā'
N[CASE=nom,NUM=pl,GEN=m,VOICE=reported] -> 'kecit'
ADJ[CASE=nom,NUM=sg,GEN=n,PRIV=vitarka] -> 'atarkam'
N[CASE=nom,NUM=sg,GEN=n,KIND=intermediate] -> 'dhyānam'
ADJ[CASE=nom,NUM=sg,GEN=n,KIND=intermediate] -> 'antaram'
```

```nltk-dep
'sāmantakāny' -> 'aṣṭau' | 'eṣām' | '∅-ekaikasy' | '∅-aikaikam' | 'śuddhāduḥkhāsukhāni' | 'hi'
'cādyaṃ' -> 'āryaṃ' | '∅-sāmantakam'
'kecit' -> 'tridhā'
'dhyānam' -> 'atarkam' | 'antaram'
```

Āryam resolves to uncontaminated first access, while tridhā kecit is only the reported
first-access alternative. Neutral feeling is not ethical indeterminacy. Atarkam begins a
distinct intermediate-dhyāna account, not an equation of access with intermediate
dhyāna.

**Close construe.** There are eight access attainments
for these principal attainments, pure and accompanied
by neutral feeling. The first is also uncontaminated;
some authorities make it threefold. Intermediate dhyāna
is dhyāna without vitarka.

## 5. Translation

### Literal Translation

> There are eight access attainments for these;
> they are pure and neither painful nor pleasant.
> The first is also noble. Some [say it is]
> threefold. Intermediate dhyāna is without vitarka.

### Bhāṣya-informed study translation

> For these eight principal attainments there are eight access
> attainments, one for each; they are pure and neither painful nor
> pleasant. The first access attainment is also noble. Some say it is
> threefold. The intermediate dhyāna is a dhyāna without vitarka.

## 6. Philosophical Translation

> The access to an attainment has its own classification.
> Its modes and feeling cannot simply be copied
> from the principal attainment it enables one to
> enter. The commentary further distinguishes an access-level
> mind used in rebirth-linking from collected access
> attainment, and distinguishes access from intermediate dhyāna.

The repeated language of proximity or intermediacy
therefore does not establish a single undifferentiated
kind of meditative state.

## 7. Technical Vocabulary

**Source.** Pradhan 447|18–448|11, checked against the local Bhāṣya
study and running source. The Bhāṣya resolves “neither painful nor
pleasant” as association with the faculty of neutral feeling; in the
principal account, access is not savoring-associated, being a path of
dispassion. The first access, anāgamya, is both pure and uncontaminated
(“noble”); “threefold” adds a savoring-associated mode on some
authorities' view. The modes, feeling, and result of intermediate dhyāna
continue in VAK 8.23.

**`Sāmantaka`.** Access or neighboring attainment, one
for each principal attainment. Its dispassion-path
function continues the antidotal account of VAK 8.21.
It is an attainment with its own determination,
not merely a name for an empty interval.

**`Anāgamya`.** The first access attainment. In the
principal account it has pure and uncontaminated
modes. The reported alternative adds savoring association.

**`Upekṣendriya`.** Faculty of neutral feeling. Here
it resolves neither-painful-nor-pleasant. It must remain
distinct from the separately classified wholesome equanimity
factor. Neutral feeling also does not mean ethically
neutral, since the principal account calls the attainments pure.

**`Vairāgyamārga / vairāgyapatha`.** Path of dispassion.
The prose uses this function in explaining exclusion
of savoring association and in distinguishing access
from intermediate dhyāna.

**`Pratisaṃdhibandha`.** Rebirth-linking. Its defiled character
in the cited access-level mental occurrence is not
transferred to the collected attainment.

**`Samāhita`.** Collected or concentrated. The denial
of defiledness is expressly qualified by this term.
The scope of the denial matters as much as the
level-name of the mind concerned.

**`Dhyānāntara`.** Intermediate dhyāna. The local definition
states absence of vitarka and calls it a particular
variety of dhyāna. Its fuller constitution is developed
in the next study.

## 8. Logical Determination

The verse counts one access attainment for each principal attainment and gives the principal account of its mode and feeling. The Bhāṣya attributes a competing savoring-associated first-access view to `kecit`; keep it separate. Provenance: `[verse]`, `[prose]`, `[kecit]`.

**Signature.** `Access/1(a)`, `Principal/1(p)`—access and principal attainment; `ForAccess/2(a,p)`—a corresponds to p; `Pure/1(a)`, `Uncontaminated/1(a)`, `Savoring/1(a)`—mode; `NeutralFeeling/1(a)`—feeling faculty; `IntermediateDhyana/1(a)`—intermediate dhyāna; `Vitarka/1(a)`—vitarka is present.

**Dataset.** Eight access-to-principal pairs; the listed first access is also uncontaminated. Neutral feeling is not ethical neutrality.

```nltk-valuation
firstAccess => firstAccess
secondAccess => secondAccess
thirdAccess => thirdAccess
fourthAccess => fourthAccess
spaceAccess => spaceAccess
consciousnessAccess => consciousnessAccess
nothingnessAccess => nothingnessAccess
summitAccess => summitAccess
firstPrincipal => firstPrincipal
secondPrincipal => secondPrincipal
thirdPrincipal => thirdPrincipal
fourthPrincipal => fourthPrincipal
spacePrincipal => spacePrincipal
consciousnessPrincipal => consciousnessPrincipal
nothingnessPrincipal => nothingnessPrincipal
summitPrincipal => summitPrincipal
intermediateDhyana => intermediateDhyana
Access => {firstAccess,secondAccess,thirdAccess,fourthAccess,spaceAccess,consciousnessAccess,nothingnessAccess,summitAccess}
Principal => {firstPrincipal,secondPrincipal,thirdPrincipal,fourthPrincipal,spacePrincipal,consciousnessPrincipal,nothingnessPrincipal,summitPrincipal}
ForAccess => {(firstAccess,firstPrincipal),(secondAccess,secondPrincipal),(thirdAccess,thirdPrincipal),(fourthAccess,fourthPrincipal),(spaceAccess,spacePrincipal),(consciousnessAccess,consciousnessPrincipal),(nothingnessAccess,nothingnessPrincipal),(summitAccess,summitPrincipal)}
Pure => {firstAccess,secondAccess,thirdAccess,fourthAccess,spaceAccess,consciousnessAccess,nothingnessAccess,summitAccess}
NeutralFeeling => {firstAccess,secondAccess,thirdAccess,fourthAccess,spaceAccess,consciousnessAccess,nothingnessAccess,summitAccess}
Uncontaminated => {firstAccess}
Savoring => {}
IntermediateDhyana => {intermediateDhyana}
Vitarka => {}
```

```nltk-fol
# THEORY principal
# [verse, prose] eight accesses, each corresponding to a principal attainment
all a.(Access(a) -> exists p.(Principal(p) & ForAccess(a,p)))
# [verse, prose] principal account: pure and associated with neutral feeling
all a.(Access(a) -> (Pure(a) & NeutralFeeling(a) & -Savoring(a)))
# [verse, prose] first access is also uncontaminated; intermediate dhyāna lacks vitarka
Uncontaminated(firstAccess)
all a.(IntermediateDhyana(a) -> -Vitarka(a))

# THEORY kecit
# [prose, kecit] some authorities add savoring at anāgamya
Savoring(firstAccess)
```

**Results (NLTK).** The principal theory satisfies the displayed finite model; the `kecit` claim satisfies a separate finite model with `Savoring(firstAccess)` added. `ResolutionProver` proves the union contradictory when `Access(firstAccess)` is included.

**Scope cautions.** “Threefold” is the reported alternative for first access, not the three modes of intermediate dhyāna in 8.23. The intermediate-dhyāna statement opens a distinct topic. Neutral feeling does not imply ethical indeterminacy, and rebirth-linking mind is not modeled as the collected access attainment.

## 9. Interpretive Note

**Correction of the research first pass.** Its source
caution treats tridhā as beginning a classification
completed in the next verse. The Bhāṣya instead
makes tridhā kecit a report of disagreement concerning
anāgamya. This study follows that explicit explanation.
The chapter has substantial material remaining; the
verse does not close the Samāpatti chapter.

**Witness cautions.** The running text inspected here
already has `āryaṃ cādyaṃ`, although the research
kārikā reports an uninflected source form. The final
`atarka` is regularized in the local study and
explained by vitarkāsaṃprayukta in prose. The uncertain
`yantabāhyatvāt` is left unresolved. Original files
and the running witness remain untouched.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates level, mode, feeling, and
function without treating their classifications as interchangeable.
Yoga Technē, its kriyā–karma companion, concerns the
entry and antidotal work assigned to access attainment.
The first-access exception and reported alternative
must remain visible in any representation of that work.

For Organon, distinguish an access attainment from
an intermediate dhyāna, and collected operation from
rebirth-linking. Store attributed alternatives separately
from the principal classification. This is project
reconstruction, not an additional doctrine attributed
to the Bhāṣya.

**Review status.** Provisional, Bhāṣya-controlled study.
The eightfold count, neutral feeling, first-access
exception, alternative threefold account, rebirth-linking
qualification, and access/intermediate distinction have
been checked against the local research and running
source. The damaged causal expression remains unresolved.

## 10. OWL++ Seed

```text
Class: AccessAttainment
Class: PrincipalAttainment
Class: IntermediateDhyana
Class: ReportedAccount
Class: MentalOccurrenceFunction

ObjectProperty: enablesEntryInto
ObjectProperty: hasAvailableMode
ObjectProperty: hasFeelingFaculty
ObjectProperty: classifiedUnderAccount

AccessAttainmentInventory:
    count: 8
    correspondence: OneAccessForEachPrincipalAttainment
    feelingFaculty: NeutralFeeling

PrincipalAccessAccount:
    generalMode: Pure
    firstAccessAdditionalMode: Uncontaminated
    collectedSavoringMode: excluded

AlternativeFirstAccessAccount:
    attribution: SomeAuthorities
    availableModes: SavoringAssociated, Pure, Uncontaminated

AccessLevelRebirthLinking:
    mayBeDefiled: true
    function: RebirthLinking

IntermediateDhyana:
    localDefinition: DhyanaWithoutVitarka
    notSynonymousWith: AccessAttainment

ProjectConstraint: Neutral feeling is not ethical neutrality.
ProjectConstraint: First access admits alternative modes, not simultaneous modes.
ProjectConstraint: Do not generalize the alternative account to all access levels.
ProjectConstraint: Defiled rebirth-linking does not establish defiled collected access.
ProjectConstraint: Tridha kecit concerns first access, not the later samadhi triad.
ProjectConstraint: Preserve the unresolved causal witness expression.
```

This is a declarative project seed, not executable OWL.
VAK 8.23 next determines intermediate dhyāna's modes,
feeling, and result, and continues the samādhi classification.
