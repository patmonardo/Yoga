# VAK_8.27 — Further Samādhi Restrictions and Present-Life Pleasant Abiding

## 1. Sanskrit (Devanāgarī)

```sanskrit
सास्रवाः नृषु अकोप्यस्य सप्तसामन्तवर्जिताः ।
समाधिभावना ध्यानं शुभमाद्यं सुखाय हि ॥ ८.२७ ॥
```

## 2. Sanskrit (IAST)

```text
sāsravāḥ nṛṣu akopyasya saptasāmantavarjitāḥ |
samādhibhāvanā dhyānaṃ śubham ādyaṃ sukhāya hi || 8.27 ||
```

The Sanskrit follows the local kārikā witness, including
its separated opening words. The first half continues
the further-samādhi discussion; the second introduces
the first of four cultivations of samādhi.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `sāsravāḥ` | nominative plural masculine adjective | contaminated, accompanied by outflows |
| `nṛṣu` | locative plural of nṛ | among human beings |
| `akopyasya` | genitive singular masculine | of the unshakeable [arhat] |
| `saptasāmantavarjitāḥ` | nominative plural masculine compound adjective | excluding seven access stages |
| `samādhibhāvanā` | nominative singular feminine compound | cultivation of samādhi |
| `dhyānam` | nominative singular neuter | dhyāna |
| `śubham` | nominative singular neuter adjective | wholesome |
| `ādyam` | nominative singular neuter adjective | first |
| `sukhāya` | dative singular neuter | for happiness or pleasant abiding |
| `hi` | explanatory particle | for; indeed |

`Sa + āsrava` yields `sāsrava`. The compound
saptasāmantavarjita contains the number seven; it does
not exclude every access attainment without exception.

## 4. Grammar

The inherited plural subject is restricted by mode, human location, practitioner, and level exclusion; the second half begins a new cultivation subject. The locative answers where, the genitive whose, and the dative purpose is locally expanded by the Bhāṣya.

```nltk-fcfg
% start S
# tokens: ∅-aparasamādhayaḥ sāsravāḥ nṛṣu akopyasya saptasāmantavarjitāḥ samādhibhāvanā dhyānam śubham ādyaṃ sukhāya hi ∅-dṛṣṭadharmasukhavihārāya
S -> CL[K=restriction] CL[K=cultivation]
CL[K=restriction] -> N[CASE=nom,NUM=?n,GEN=?g,SUPPLIED=prose] ADJ[CASE=nom,NUM=?n,GEN=?g,MODE=only] N[CASE=loc,NUM=pl,GEN=m] N[CASE=gen,NUM=sg,GEN=m] ADJ[CASE=nom,NUM=?n,GEN=?g,PRIV=yes]
CL[K=cultivation] -> N[CASE=nom,NUM=sg,GEN=f] N[CASE=nom,NUM=sg,GEN=n] ADJ[CASE=nom,NUM=sg,GEN=n] ADJ[CASE=nom,NUM=sg,GEN=n] N[CASE=dat,NUM=sg,GEN=n] PTCL[EXPL=yes] N[CASE=dat,NUM=sg,GEN=n,SUPPLIED=prose]
N[CASE=nom,NUM=pl,GEN=m,SUPPLIED=prose] -> '∅-aparasamādhayaḥ'
ADJ[CASE=nom,NUM=pl,GEN=m,MODE=only] -> 'sāsravāḥ'
N[CASE=loc,NUM=pl,GEN=m] -> 'nṛṣu'
N[CASE=gen,NUM=sg,GEN=m] -> 'akopyasya'
ADJ[CASE=nom,NUM=pl,GEN=m,PRIV=yes] -> 'saptasāmantavarjitāḥ'
N[CASE=nom,NUM=sg,GEN=f] -> 'samādhibhāvanā'
N[CASE=nom,NUM=sg,GEN=n] -> 'dhyānam'
ADJ[CASE=nom,NUM=sg,GEN=n] -> 'śubham' | 'ādyaṃ'
N[CASE=dat,NUM=sg,GEN=n] -> 'sukhāya'
PTCL[CASE=none,NUM=none,GEN=none,EXPL=yes] -> 'hi'
N[CASE=dat,NUM=sg,GEN=n,SUPPLIED=prose] -> '∅-dṛṣṭadharmasukhavihārāya'
```

```nltk-dep
'∅-aparasamādhayaḥ' -> 'sāsravāḥ' | 'nṛṣu' | 'akopyasya' | 'saptasāmantavarjitāḥ'
'samādhibhāvanā' -> 'dhyānam' | 'śubham' | 'ādyaṃ' | 'sukhāya' | 'hi' | '∅-dṛṣṭadharmasukhavihārāya'
```

The seven excluded access stages do not include anāgamya, which remains among the eleven
grounds. The second subject is not restricted to the unshakeable arhat; `sukhāya` is
specified as present-life pleasant abiding, not a guaranteed later-life result.


**Close construe.** The further samādhis are contaminated,
occur among humans in the unshakeable arhat, and
exclude seven access stages. Wholesome first dhyāna
is cultivation of samādhi for present-life pleasant abiding.

## 5. Translation

### Literal Translation

> [The further samādhis] are contaminated, [arising] among humans, [for] the
> unshakeable one, excluding seven access stages.
> The [first] cultivation of samādhi is wholesome first dhyāna,
> for happiness.

### Bhāṣya-informed study translation

> The further samādhis are contaminated; they arise among human beings, for the
> unshakeable arhat, excluding the seven access stages. The first cultivation of
> samādhi is wholesome first dhyāna, for pleasant abiding in the present life.

## 6. Philosophical Translation

> The status of a further samādhi is not inherited
> from its uncontaminated object. Its mode, practitioner,
> and supporting level receive their own determinations.
> The exposition then changes question: repeated cultivation
> of samādhi is classified by what it accomplishes,
> beginning with pleasant abiding in the present life.

Contaminated does not mean merely conditioned. Uncontaminated
path knowledge is also conditioned; the present
classification requires the specific reason supplied
by the commentary.

## 7. Technical Vocabulary

**`Āryamārgadveṣitva`.** Opposition or aversion toward
the noble path. This is the prose's reason
for the further samādhis' contaminated status, continuing
the depreciative orientation of VAK 8.26. It
must not be converted into an assertion that
the arhat has reacquired the defilement of hatred.

**`Akopya`.** Unshakeable, the technical arhat type
specified here. “Unshakeable knower” without that
qualification would blur the explicit exclusion of
other arhat types.

**`Saptasāmantavarjita`.** Excluding seven access stages.
Anāgamya remains included. The rule is an exact
level enumeration, not a general preference for
principal over preparatory attainment.

**`Samādhibhāvanā`.** Cultivation of samādhi. The cited
formula speaks of practice, cultivation, and repeated
development leading to a specified result. This
new fourfold list is distinct from both preceding
samādhi triads.

**`Dṛṣṭadharmasukhavihāra`.** Pleasant abiding in the
present life. It states the purpose of the
first cultivation, not merely the presence of a
particular pleasure faculty in every dhyāna.

**`Saṃparāya`.** A later existence. The commentary
distinguishes the present-life purpose from a result
that need not be present in a subsequent existence.

## 8. Logical Determination

The verse closes the further-samādhi restrictions and begins a new fourfold cultivation account. The Bhāṣya fixes the first group as exclusively contaminated, human, for the unshakeable arhat, across eleven grounds; the second clause's first-dhyāna cultivation is for present-life pleasant abiding. `[verse]` with `[prose]` expansions.

**Signature.** `Further(x)`; `Contaminated(x)`; `AmongHumans(x)`; `ForAkopya(x)`; `AllowedGround(g)`; `OnGround(x,g)`; `Cultivation(x)`; `Wholesome(x)`; `FirstDhyana(x)`; `ForPresentAbiding(x)`.

```nltk-valuation
furtherEmpty => furtherEmpty
furtherNonDirected => furtherNonDirected
furtherSignless => furtherSignless
firstCultivation => firstCultivation
desireGround => desireGround
anagamya => anagamya
intermediateDhyana => intermediateDhyana
firstDhyanaGround => firstDhyanaGround
secondDhyanaGround => secondDhyanaGround
thirdDhyanaGround => thirdDhyanaGround
fourthDhyanaGround => fourthDhyanaGround
spaceGround => spaceGround
consciousnessGround => consciousnessGround
nothingnessGround => nothingnessGround
summitGround => summitGround
Further => {furtherEmpty, furtherNonDirected, furtherSignless}
Contaminated => {furtherEmpty, furtherNonDirected, furtherSignless}
AmongHumans => {furtherEmpty, furtherNonDirected, furtherSignless}
ForAkopya => {furtherEmpty, furtherNonDirected, furtherSignless}
AllowedGround => {desireGround, anagamya, intermediateDhyana, firstDhyanaGround, secondDhyanaGround, thirdDhyanaGround, fourthDhyanaGround, spaceGround, consciousnessGround, nothingnessGround, summitGround}
OnGround => {(furtherEmpty,desireGround),(furtherEmpty,anagamya),(furtherEmpty,intermediateDhyana),(furtherEmpty,firstDhyanaGround),(furtherEmpty,secondDhyanaGround),(furtherEmpty,thirdDhyanaGround),(furtherEmpty,fourthDhyanaGround),(furtherEmpty,spaceGround),(furtherEmpty,consciousnessGround),(furtherEmpty,nothingnessGround),(furtherEmpty,summitGround),(furtherNonDirected,desireGround),(furtherNonDirected,anagamya),(furtherNonDirected,intermediateDhyana),(furtherNonDirected,firstDhyanaGround),(furtherNonDirected,secondDhyanaGround),(furtherNonDirected,thirdDhyanaGround),(furtherNonDirected,fourthDhyanaGround),(furtherNonDirected,spaceGround),(furtherNonDirected,consciousnessGround),(furtherNonDirected,nothingnessGround),(furtherNonDirected,summitGround),(furtherSignless,desireGround),(furtherSignless,anagamya),(furtherSignless,intermediateDhyana),(furtherSignless,firstDhyanaGround),(furtherSignless,secondDhyanaGround),(furtherSignless,thirdDhyanaGround),(furtherSignless,fourthDhyanaGround),(furtherSignless,spaceGround),(furtherSignless,consciousnessGround),(furtherSignless,nothingnessGround),(furtherSignless,summitGround)}
Cultivation => {firstCultivation}
Wholesome => {firstCultivation}
FirstDhyana => {firstCultivation}
ForPresentAbiding => {firstCultivation}
```

```nltk-fol
# THEORY shared
# [prose] sāsrava ekāntena; the eleven grounds are represented as a finite set
all x.(Further(x) -> (Contaminated(x) & AmongHumans(x) & ForAkopya(x)))
all x.(Further(x) -> exists g.(AllowedGround(g) & OnGround(x,g)))
# [verse, prose] first wholesome cultivation is first dhyāna, for present-life abiding
all x.(Cultivation(x) -> (Wholesome(x) & FirstDhyana(x) & ForPresentAbiding(x)))
```

**Results (NLTK).** The checker reports `shared: T` in the finite model.

**Scope cautions.** Humans are the practitioner class, not the attainment level. Seven excluded access stages do not include anāgamya. The prose says the series continues beyond first dhyāna and denies a necessary later-life result; this model does not encode a universal guarantee or a rebirth claim.

## 9. Interpretive Note

**Corrections to earlier readings.** “Conditioned”
is insufficient for sāsrava, and “completed rather
than preliminary ground” misses the express inclusion
of anāgamya. The present study retains contaminated
mode, its stated rationale, and the exact eleven-level
inventory. It also preserves the prose extension
beyond the initially named first dhyāna.

**Witness cautions.** The running source prints
`vahulīkṛtā` in the cultivation formula and the
compressed `aparihiṇordhvopapannaparinirvṛtānāṃ` in the
later-life qualification. “Repeatedly developed” reflects
the intelligible formula; the last sentence is
not silently rewritten into a critically established
reading. Original witnesses remain untouched.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
The project's Recognition vocabulary can distinguish
an object's status from that of the further
act taking it as object. Yoga Vidyā articulates
mode, practitioner, support level, and purpose;
Yoga Technē, its kriyā–karma companion, concerns
the repeated cultivation that realizes the specified function.

The research comparison with Pure Reason and
Yoga samādhi remains a separate project interpretation.
The Kośa's reason for contaminated status is its
own explicit path-relative explanation. For Organon
representation, keep that reason, the practitioner
restrictions, and the new cultivation subject separate,
rather than deriving them from a general ranking
of reflective and non-reflective knowing.

**Review status.** Provisional, Bhāṣya-controlled study.
The mode rationale, human/akopya restrictions, eleven
levels, first cultivation, two wholesome modes,
extension to other dhyānas, and present/later-life
distinction have been checked against the local
research and running source. The compressed final
counterexample remains textually qualified.

## 10. OWL++ Seed

```text
Class: FurtherSamadhi
Class: PractitionerType
Class: AttainmentLevel
Class: SamadhiCultivation

ObjectProperty: hasMode
ObjectProperty: requiresPractitioner
ObjectProperty: occursAmong
ObjectProperty: availableAtLevel
ObjectProperty: cultivatedFor

FurtherTriad:
    mode: ContaminatedOnly
    sourceReason: OppositionToNoblePath
    occurrence: HumansOnly
    practitioner: AkopyaArhat
    levels: DesireDomain, Anagamya, IntermediateDhyana,
            FourDhyanas, FourFormlessLevels
    levelCount: 11
    excludedLevels: SevenOtherAccessStages

FirstSamadhiCultivation:
    namedBasis: WholesomeFirstDhyana
    allowedModes: Pure, Uncontaminated
    proseExtension: OtherDhyanasAlsoUnderstood
    purpose: PresentLifePleasantAbiding
    necessarySameLaterLifeResult: NotAsserted

ProjectConstraint: Contaminated is not synonymous with conditioned.
ProjectConstraint: Path opposition is not an assertion of renewed arhat hatred.
ProjectConstraint: Human occurrence and attainment level are distinct axes.
ProjectConstraint: Anagamya remains included despite seven access exclusions.
ProjectConstraint: Further-triad restrictions do not transfer to the new cultivation.
ProjectConstraint: Present pleasant abiding is not one uniform feeling faculty.
ProjectConstraint: The remaining three cultivations continue in VAK 8.28.
```

This is a declarative project seed, not executable OWL.
VAK 8.28 next completes the four cultivations of samādhi.
