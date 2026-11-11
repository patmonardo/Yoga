# VAK_8.36 — Ten Totalities and Their Object Fields

## 1. Sanskrit (Devanāgarī)

```sanskrit
दश कृत्स्नानि अलोभाष्टौ ध्यानेऽन्त्ये गोचरः पुनः ।
कामाः द्वे शुद्धकारूप्ये स्वचतुःस्कन्धगोचरे ॥ ८.३६ ॥
```

## 2. Sanskrit (IAST)

```text
daśa kṛtsnāni alobhāṣṭau dhyāne 'ntye gocaraḥ punaḥ |
kāmāḥ dve śuddhākārūpye svacatuḥskandhagocare || 8.36 ||
```

The local scripts are retained. Their śuddha-compound
spellings differ: Devanāgarī gives śuddhakārūpye, while
the local IAST has śuddhākārūpye. The running
verse prints śuddhakārupye, and its explanatory prose
has śuddhakārūpyasvabhāve. The analysis below follows
the prose-supported *śuddhaka-ārūpya* without silently altering
the displayed witnesses. The complete Bhāṣya unit is
[457|13]–[458|09–10]; [457|12] closes 8.35 and
[458|11] opens 8.37.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `daśa` | numeral | ten |
| `kṛtsnāni` | nominative plural neuter | totalities, expanded as totality-Essences in prose |
| `alobhāḥ` | nominative plural masculine predicate | non-greed; having non-greed as nature |
| `aṣṭau` | numeral | eight, the first eight |
| `dhyāne` | locative singular neuter | in dhyāna |
| `antye` | locative singular adjective | in the last, here fourth |
| `gocaraḥ` | nominative singular masculine | range |
| `punaḥ` | indeclinable | again; as for |
| `kāmāḥ` | nominative plural masculine | desire-domain range, with its Support specified in prose |
| `dve` | nominative dual neuter | the two remaining totalities |
| `śuddhakārūpye` | nominative dual neuter, prose-supported analysis | pure formless attainments |
| `svacatuḥskandhagocare` | nominative dual neuter compound adjective | ranging over the four Bases of their own level |

Sandhi: `alobhāḥ + aṣṭau` > `alobhāṣṭau`; `dhyāne + antye` is displayed
with avagraha as `dhyāne 'ntye`.
Sva in the final compound is specified by
the prose's svabhūmika, “belonging to one's own level.”

## 4. Grammar

The tenfold subject is divided into the first eight and the final two; attainment level, range, and Support are separate relations. The Bhāṣya identifies `antye` as the fourth dhyāna and distributes each of the final pair's four-Base Supports to its own level.

```nltk-fcfg
% start S
# tokens: daśa kṛtsnāni ∅-kṛtsnāyatanāni alobhāṣṭau ∅-prathamāni dhyāne antye gocaraḥ punaḥ kāmāḥ ∅-rūpāyatanam dve śuddhākārūpye svacatuḥskandhagocare
S -> CL[K=total] CL[K=eight] CL[K=object] CL[K=two]

CL[K=total] -> NUMR[CASE=?c,NUM=?n,GEN=?g] N[CASE=?c,NUM=?n,GEN=?g] N[CASE=?c,NUM=?n,GEN=?g,SUPPLIED=prose]
CL[K=eight] -> ADJ[CASE=?c,NUM=?n,GEN=?g,NATURE=nongreed] N[CASE=?c,NUM=?n,GEN=?g,SUPPLIED=prose] N[CASE=?d,NUM=?m,GEN=?h] ADJ[CASE=?d,NUM=?m,GEN=?h]
CL[K=object] -> N[CASE=?c,NUM=sg,GEN=m,ROLE=field] ADV[CONTRAST=yes] N[CASE=?c,NUM=pl,GEN=m,ROLE=object] N[CASE=?c,NUM=sg,GEN=n,SUPPLIED=prose]
CL[K=two] -> NUMR[CASE=?c,NUM=?n,GEN=?g] ADJ[CASE=?c,NUM=?n,GEN=?g,QUALITY=pure] ADJ[CASE=?c,NUM=?n,GEN=?g,ROLE=ownlevelobject]

NUMR[CASE=nom,NUM=pl,GEN=n] -> 'daśa'
N[CASE=nom,NUM=pl,GEN=n] -> 'kṛtsnāni'
N[CASE=nom,NUM=pl,GEN=n,SUPPLIED=prose] -> '∅-kṛtsnāyatanāni'
ADJ[CASE=nom,NUM=pl,GEN=n,NATURE=nongreed] -> 'alobhāṣṭau'
N[CASE=nom,NUM=pl,GEN=n,SUPPLIED=prose] -> '∅-prathamāni'
N[CASE=loc,NUM=sg,GEN=n] -> 'dhyāne'
ADJ[CASE=loc,NUM=sg,GEN=n] -> 'antye'
N[CASE=nom,NUM=sg,GEN=m,ROLE=field] -> 'gocaraḥ'
ADV[CONTRAST=yes] -> 'punaḥ'
N[CASE=nom,NUM=pl,GEN=m,ROLE=object] -> 'kāmāḥ'
N[CASE=nom,NUM=sg,GEN=n,SUPPLIED=prose] -> '∅-rūpāyatanam'
NUMR[CASE=nom,NUM=du,GEN=n] -> 'dve'
ADJ[CASE=nom,NUM=du,GEN=n,QUALITY=pure] -> 'śuddhākārūpye'
ADJ[CASE=nom,NUM=du,GEN=n,ROLE=ownlevelobject] -> 'svacatuḥskandhagocare'
```

```nltk-dep
'kṛtsnāni' -> 'daśa' | '∅-kṛtsnāyatanāni'
'alobhāṣṭau' -> '∅-prathamāni' | 'dhyāne' | 'antye'
'gocaraḥ' -> 'punaḥ' | 'kāmāḥ' | '∅-rūpāyatanam'
'dve' -> 'śuddhākārūpye' | 'svacatuḥskandhagocare'
```

`Alobhāṣṭau` assigns non-greed as nature, not as an injunction; the desire-domain range is specified in prose as visible Form Support (one attributed view assigns wind a tangible Support).
`Śuddhaka` does not mean *anāsrava*, and neither range is a claim of omniscience.
**Close construe.** There are ten totalities. The
first eight have non-greed as nature and occur
in the last dhyāna; their range is
the desire domain. The remaining two are
pure formless attainments, each ranging over the four
Bases of its own level.

## 5. Translation

### Literal Translation

> There are ten totalities. Eight are non-greed,
> in the last dhyāna; their range, moreover,
> is the desire domain. Two are pure formless
> attainments, ranging over the four Bases of
> their own level.

### Bhāṣya-informed study translation

> There are ten totality-Essences, so named for uninterrupted complete
> pervasion: earth, water, fire, wind, blue, yellow, red, white, infinite
> space, and infinite Cognition. The first eight have non-greed as their
> nature and occur only in the fourth dhyāna. Their range is the desire
> domain, with the visible Form Essence as Support; some assign wind the
> tangible Essence instead. The final two are pure formless attainments,
> each taking the four Bases of its own ground as Support.

## 6. Philosophical Translation

> Totality concerns complete pervasion of a contemplative
> field. Its classification still distinguishes the nature
> of the practice, the level at which it
> occurs, and the Supports it takes. Even
> this developed capacity can occur in an
> ordinary person's continuum; its accomplishment alone
> does not establish noble status.

This formulation draws on the explanatory prose.
“Totality” does not entail that all dharmas
are simultaneously known or that every Thing
falls within each totality's range.

## 7. Technical Vocabulary

**`Kṛtsna / kṛtsnāyatana`.** Totality / totality-Essence.
The prose explains the name by complete pervasion.
The selected determination and the completeness of
its extension must remain distinguishable.

**`Nirantarakṛtsnaspharaṇa`.** Uninterrupted complete pervasion.
This gives the local explanation of the name;
it is more precise than merely describing the
Support as large or calling the practice universal.

**`Alobhasvabhāva`.** Having non-greed as nature.
“Non-appropriation” can develop the project's interpretation,
but non-greed retains the explicit technical predicate.

**`Rūpāyatana / spraṣṭavyāyatana`.** Visible-form Essence /
tangible Essence. The principal account gives the
former as Support for the first eight; unnamed authorities
assign the latter to wind. Earth, water,
fire, and wind in this inventory should not
automatically be substituted by four tangible Supports.

**`Śuddhakārūpya`.** Pure formless attainment. Śuddhaka
retains the chapter's technical pure classification;
it must not be silently translated as anāsrava,
uncontaminated. “Pure” here is not a new
claim that all ten totalities are noble paths.

**`Ākāśānantyāyatana / vijñānānantyāyatana`.** Essence of
infinite space / Essence of infinite Cognition.
These identify the final two totalities. *Vijñāna*
is Cognition in the project vocabulary; it is distinct from
Knowledge (*jñāna*) and Prajñā.

**`Svabhūmikāś catvāraḥ skandhāḥ`.** The four Bases
of the respective level: feeling, recognition, formations,
and Cognition. The formless context excludes the
Form Base from this fourfold Support.

**`Prāveśika / uttarottaraviśiṣṭatva`.** Entry-related /
successive superiority. The first term links the
three practice groups; the second gives the
explicit reason for their graded relation.

**`Pṛthagjanāryasāṃtānika`.** Belonging to the continuities
of ordinary and noble persons. This is a
bearer classification, distinct from an attainment's
level, range, Support, and technical mode.

## 8. Logical Determination

The verse and Bhāṣya classify ten totalities by number, nature, attainment ground, range, and Support. The first eight share non-greed, fourth-dhyāna location, desire-domain range, and, in the principal account, visible Form Support. The final two are pure formless attainments with four own-ground Bases as Support. `[verse]` / `[prose]`.

**Signature.** `Totality(x)`, `FirstEight(x)`, `LastTwo(x)`, `Nongreed(x)`, `FourthDhyana(x)`, `DesireRange(x)`, `VisibleFormSupport(x)`, `PureFormless(x)`, and `OwnLevelFourBaseSupport(x)`.

```nltk-fol
# THEORY shared
# [verse, prose] first-eight nature, level, range, and principal Support
all x.(FirstEight(x) -> (Nongreed(x) & FourthDhyana(x) & DesireRange(x) & VisibleFormSupport(x)))
# [verse] dve śuddhākārūpye; [prose] own-ground four Bases as Support
all x.(LastTwo(x) -> (PureFormless(x) & OwnLevelFourBaseSupport(x)))
all x.(Totality(x) -> (FirstEight(x) | LastTwo(x)))
```

**Finite classification valuation.** The ten named members are data; the universal rules encode only the two class-level descriptions.

```nltk-valuation
earth => earth
water => water
fire => fire
wind => wind
blue => blue
yellow => yellow
red => red
white => white
spacetotality => spacetotality
cognitiontotality => cognitiontotality
Totality => {earth,water,fire,wind,blue,yellow,red,white,spacetotality,cognitiontotality}
FirstEight => {earth,water,fire,wind,blue,yellow,red,white}
LastTwo => {spacetotality,cognitiontotality}
Nongreed => {earth,water,fire,wind,blue,yellow,red,white}
FourthDhyana => {earth,water,fire,wind,blue,yellow,red,white}
DesireRange => {earth,water,fire,wind,blue,yellow,red,white}
VisibleFormSupport => {earth,water,fire,wind,blue,yellow,red,white}
PureFormless => {spacetotality,cognitiontotality}
OwnLevelFourBaseSupport => {spacetotality,cognitiontotality}
```

**Results (NLTK).** The checker reports every shared rule true in the finite ten-member model. This is a model check, not a proof that no other totalities are possible.

**Scope cautions.** The prose's *eke* assignment of a tangible Support to wind is an attributed alternative, not included in the shared classification. “Pure” does not silently mean without influx; the four own-ground Bases are Supports, not an assertion of omniscience.

## 9. Interpretive Note

**Source voice.** The principal exposition assigns
visible Form Support to the first eight. The wind
exception is attributed to unnamed authorities. These
are kept distinct in the translation and table;
no school identity is supplied beyond the witness.

**Witness cautions.** The śuddha-compound discrepancy
between scripts and running text is disclosed
above. The prose also prints anyor in the
four-Base sentence, where the context supplies the
reference to the final two. The study follows
that clear dual reference without editing the source.
The directional force of the entry compounds
remains open for philological review.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā distinguishes selected determination, complete
pervasion, technical nature, attainment ground, range, Support,
and bearer status. Yoga Technē, its kriyā–karma
companion, concerns the effective cultivation of a
field pervaded by the selected determination.

The research's “universality at the level of
appearance” is useful project language for this
operation. Its scope remains the contemplative field.
Neither pervasion nor non-greed by itself establishes
an unrestricted constitutive Principle of Knowledge.
The source's ordinary/noble bearer distinction helps
keep practical accomplishment and liberative status separate.

**Review status.** Source-collated, Bhāṣya-controlled study.
The complete unit [457|13]–[458|09–10], preceding [457|12], and
following [458|11] boundaries were checked against the running source.
The tenfold inventory, wind alternative, final-two four-Base Supports,
entry-related compounds, and cessation exception are covered.
The *prāveśika* direction and irregular `anyorālambanam` remain open.

## 10. OWL++ Seed

```text
Class: TotalityEssence
Class: AttainmentLevel
Class: Range
Class: Support
Class: BearerStatus

ObjectProperty: hasNature
ObjectProperty: occursAtLevel
ObjectProperty: hasRange
ObjectProperty: takesAsSupport
ObjectProperty: attributedTo

TenTotalities:
    memberCount: 10
    namingReason: UninterruptedCompletePervasion

FirstEightTotalities:
    members: Earth, Water, Fire, Wind, Blue, Yellow, Red, White
    nature: NonGreed
    exclusiveLevel: FourthDhyana
    range: DesireDomain
    principalSupport: DesireDomainVisibleFormEssence

WindAlternativeSupportAccount:
    support: TangibleEssence
    attributedTo: UnnamedAuthorities

InfiniteSpaceTotality:
    mode: PureFormless
    level: InfiniteSpace
    supports: FourBasesOfOwnLevel

InfiniteCognitionTotality:
    mode: PureFormless
    level: InfiniteCognition
    supports: FourBasesOfOwnLevel

ReleaseMasteryTotalityRelation:
    gradedOrder: Release, MasteryBase, TotalityEssence
    statedReason: SuccessiveSuperiority
    entryCompoundDirection: RequiresPhilologicalReview

PracticesBeginningWithReleases:
    possibleBearers: OrdinaryPersons, NoblePersons
    exceptionToSharedBearerRange: CessationRelease

ProjectConstraint: Wind alternative does not add an eleventh member.
ProjectConstraint: Pure is not silently identified with uncontaminated.
ProjectConstraint: Keep attainment ground, range, and Support separate.
ProjectConstraint: Complete pervasion does not assert omniscience.
ProjectConstraint: Graded order does not alone establish mandatory acquisition order.
ProjectConstraint: Cessation-release is not one of the ten totalities.
```

This is a declarative project seed, not executable OWL.
VAK 8.37 next addresses acquisition and the Bases
of these practices.
