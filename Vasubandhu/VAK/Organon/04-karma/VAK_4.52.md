# VAK_4.52

## 1. Sanskrit (Devanāgarī)

```sanskrit
यद्विरक्तः स्थिरो बालस्तत्र नोत्पद्यवेद्यकृत् ।
नान्यवेद्यकृदप्यार्यः कामेऽग्रे वास्थिरोऽपि न ॥ ४.५२ ॥
```

## 2. Sanskrit (IAST)

```iast
yadviraktaḥ sthiro bālas tatra notpadyavedyakṛt /
nānyavedyakṛd apy āryaḥ kāme 'gre vāsthiro 'pi na // 4.52 //
```

Padapāṭha-style separation:

```iast
yat-viraktaḥ sthiraḥ bālaḥ tatra na utpadya-vedya-kṛt /
na anya-vedya-kṛt api āryaḥ kāme agre vā asthiraḥ api na //
```

The source's `vāsthiraḥ` resolves as `vā asthiraḥ`, “or even unstable.” The
first-pass separation as `vā sthiraḥ` conflicts with both the source sandhi and
the Bhāṣya's explicit explanation of an Ārya liable to fall back.

## 3. Lexical Analysis

```text
yat-viraktaḥ
sthiraḥ
bālaḥ

tatra
na
utpadya-vedya-kṛt

na
anya-vedya-kṛt
api
āryaḥ

kāme
agre
vā
asthiraḥ
api
na
```

| Form | Morphology | Lexical value here |
|---|---|---|
| `yadviraktaḥ` | nominative masculine singular compound | detached from whichever level |
| `sthiraḥ` | nominative masculine singular | stable; not liable to fall back |
| `bālaḥ` | nominative masculine singular | ordinary, non-noble person |
| `tatra` | locative adverb | there; with respect to that level |
| `utpadyavedyakṛt` | nominative masculine singular compound | producer of karma to be experienced in the next rebirth |
| `anyavedyakṛt` | nominative masculine singular compound | producer of the other future-result karma |
| `āryaḥ` | nominative masculine singular | noble person |
| `kāme` | locative masculine singular | in or with respect to the desire domain |
| `agre` | locative neuter singular | at the summit of existence |
| `asthiraḥ` | nominative masculine singular | unstable; liable to fall back |
| `api na` | particles | not even; nevertheless does not |

**`sthira`**

The Bhāṣya glosses stability as `aparihāṇadharmatā`, not being of a nature
liable to fall back from the attained detachment.

**`anya-vedya`**

The “other” future-result karma is fixed by the Bhāṣya as
`aparaparyāyavedanīya`, karma to be experienced in a later life, in addition
to next-birth-result karma.

**`bhavāgra`**

The “summit” is the highest conditioned level, the upper boundary of
saṃsāric existence.

## 4. Grammar

**Stable ordinary person**

```text
yat [bhūmeḥ] viraktaḥ
sthiraḥ bālaḥ
tatra
na utpadya-vedya-kṛt [bhavati]
```

> A stable ordinary person detached from a given level does not produce karma
> to be experienced there in the next rebirth.

The relative `yat` is completed contextually by the correlative `tatra`.

**Stable noble person**

```text
sthiraḥ [iti vartate]
āryaḥ api
na anya-vedya-kṛt [bhavati]
```

> A stable noble person does not produce the other later-life karma either.

The Bhāṣya explicitly states that `sthiraḥ` continues into this clause. It then
includes both next-birth and later-life karma in the prohibition.

**Unstable noble person at the boundaries**

```text
kāme agre vā
asthiraḥ api [āryaḥ]
na [tad-karma-kṛt]
```

> Even an unstable noble person does not produce those future karmas with
> respect to the desire domain or the summit of existence.

The sandhi `vāsthiraḥ` must be resolved as `vā asthiraḥ` for this syntax.

## 5. Translation

### Literal Translation

> A stable ordinary person detached from a given level does not produce karma
> to be experienced there in the next rebirth. A stable noble person does not
> produce the other future-result karma either; with respect to the desire
> domain or the summit, even an unstable noble person does not.

### Bhāṣya-informed study translation

> An ordinary person who is stably detached from a level produces no karma
> leading to immediate rebirth in that level. A stable noble person produces
> neither immediate-next-birth nor later-life karma for a level from which that
> person is detached, because return to the lower level is no longer possible.
> Even a noble person liable to fall back cannot produce those future karmas
> with respect to the desire domain or the summit of existence.

The continuation of `sthira`, the scope of the two future karmas, the
impossibility of return, and the special rule for an unstable noble person are
supplied by the Bhāṣya.

## 6. Philosophical Translation

> The Path changes the modal range of karmic production. Stable detachment does
> not merely make a future rebirth unlikely; it removes the capacity to produce
> the karma whose fruition would require return to the abandoned level. The
> transformation of the continuum therefore contracts its field of possible
> actions and, through them, its field of possible future worlds.

This restriction concerns newly producible karma. It does not by itself state
that every previously accumulated karmic determination has been destroyed.

## 7. Technical Vocabulary

**Stable ordinary person**

```text
ordinary person
    + stable detachment from level X
    → cannot produce next-birth karma for X
```

The restriction does not yet exclude every more remote karmic relation to X.

**Stable noble person**

```text
noble person
    + stable detachment from level X
    → cannot produce next-birth karma for X
    → cannot produce later-life karma for X
```

The ground is structural: return to the lower level is no longer possible.

**Remaining karmic possibilities**

The Bhāṣya allows:

```text
aniyata karma
    because its fruition is not necessary

dṛṣṭadharmavedanīya karma
    if the person is presently born in that level
```

**Unstable noble person**

`Parihāṇadharmā` means liable to fall back. Even such a noble person is subject
to the special restriction at the desire domain and `bhavāgra`.

**Reason for the boundary restriction**

The Bhāṣya says the person falls from the fruit and anticipates a later
doctrine: one who has fallen from the fruit does not die while remaining in
that fallen condition. The temporal opening required for the prohibited
future maturation therefore does not arise.

## 8. Logical Determination

**Possible karma depends on possible future**

```text
RETURN(agent, level X) = impossible
    → PRODUCE(next-birth-karma-for-X) = impossible
    → PRODUCE(later-life-karma-for-X) = impossible
```

This is a modal restriction on production, not merely an empirical absence of
the relevant action.

**Agent-relative karmic capacity**

```text
PRODUCIBLE_KARMA
    = function(
        path status,
        level of detachment,
        stability of attainment
      )
```

The same karmic class may remain possible for one continuum and become
impossible for another.

**Ordinary and noble restrictions differ**

```text
stable ordinary
    excludes immediate-next-birth karma

stable noble
    excludes immediate-next-birth
    and later-life karma
```

The stronger restriction follows the stronger impossibility of future return.

**Past accumulation and present capacity**

```text
cannot newly produce karma K
    does not entail
every previously accumulated K is absent
```

Genesis and continued possession remain different questions.

## 9. Interpretive Note

**The Path transforms practical possibility**

Attainment is not an ornamental status added to an unchanged agent. It changes
what the continuum can still do:

```text
detachment
    → impossibility of return
    → impossibility of corresponding karmic production
    → contraction of future rebirth-space
```

This gives the Path a direct function within Karma theory.

**Discipline becomes irreversible determination**

At the stable level, discipline is no longer only repeated resistance to an
available possibility. The relevant karmic future has ceased to be
projectible. Stability therefore marks a transformation in the field of
possibility itself.

**The boundary levels**

Kāmadhātu and `bhavāgra` are the lower and upper limits singled out in the
special rule for the unstable noble person. The restriction depends on the
technical doctrine of falling from a fruit and must not be generalized without
that context.

**Textual correction matters conceptually**

Reading `vā sthiraḥ` would merely repeat the stable case. Reading the source
correctly as `vā asthiraḥ` introduces the required third case and makes the
Bhāṣya's entire final explanation intelligible.

This is the Organon contact. The practitioner distinctions, impossibility of
return, and fall-from-fruit explanation belong to the Bhāṣya.

## 10. OWL++ Seed

```text
Class: Person
Class: OrdinaryPerson
Class: NoblePerson
Class: StablePerson
Class: UnstablePerson
Class: Detachment
Class: Level
Class: DesireDomain
Class: SummitOfExistence
Class: Karma
Class: PresentLifeResultKarma
Class: FutureResultKarma
Class: NextBirthResultKarma
Class: LaterLifeResultKarma
Class: IndeterminateKarma
Class: PossibleFuture

ObjectProperty: detachedFrom
ObjectProperty: stableIn
ObjectProperty: liableToFallFrom
ObjectProperty: canReturnTo
ObjectProperty: cannotReturnTo
ObjectProperty: canProduce
ObjectProperty: cannotProduce
ObjectProperty: maturesIn

OrdinaryPerson SubClassOf Person
NoblePerson SubClassOf Person
StablePerson SubClassOf Person
UnstablePerson SubClassOf Person
PresentLifeResultKarma SubClassOf Karma
FutureResultKarma SubClassOf Karma
NextBirthResultKarma SubClassOf FutureResultKarma
LaterLifeResultKarma SubClassOf FutureResultKarma
IndeterminateKarma SubClassOf Karma

Rule: StableOrdinaryCannotProduceNextBirthKarmaForDetachedLevel
    OrdinaryPerson(?p)
    and StablePerson(?p)
    and detachedFrom(?p, ?x)
    and NextBirthResultKarma(?k)
    and maturesIn(?k, ?x)
    -> cannotProduce(?p, ?k)

Rule: StableNobleCannotProduceFutureKarmaForDetachedLevel
    NoblePerson(?p)
    and StablePerson(?p)
    and detachedFrom(?p, ?x)
    and FutureResultKarma(?k)
    and maturesIn(?k, ?x)
    -> cannotProduce(?p, ?k)

Constraint: ImpossibleReturnContractsKarmicCapacity
    cannotReturnTo(?p, ?x)
    entails inability to produce determinate future karma for ?x

Constraint: ProductionAndPriorAccumulationRemainDistinct
    cannotProduce(?p, ?k)
    does not entail absence of every previously accumulated ?k

Constraint: AsthiraReadingRequired
    vasthirah in the sandhied verse
    resolves as va asthirah
    in agreement with the Bhāṣya
```

The seed represents path-status and stability as conditions changing the range
of karmas a continuum can still produce.
