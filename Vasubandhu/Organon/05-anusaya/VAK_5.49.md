# VAK_5.49

## 1. Sanskrit (Devanāgarī)

```sanskrit
कौकृत्यं विचिकित्सातः क्रोधेर्ष्ये प्रतिघान्वये ।
अन्ये च षट्क्लेशमलाः माया शाठ्यं मदस्तथा ॥ ५.४९ ॥
```

## 2. Sanskrit (IAST)

```text
kaukṛtyaṃ vicikitsātaḥ krodherṣye pratighānvaye |
anye ca ṣaṭ kleśa-malāḥ māyā śāṭhyaṃ madas tathā || 5.49 ||
```

VAK 5.49 completes the genetic account of the ten Vaibhāṣika
`paryavasthānas` and then opens a new sixfold class, the stains of affliction.
The Bhāṣya closes the tenfold derivation and announces the new class; its
remaining members and definitions belong to the distributed 5.50 unit.

**Textual caution.** The working Bhāṣya e-text reads `kodherṣye` where the
kārikā witness has `krodherṣye`. Its explanatory prose `pratighasamutthe`
makes the intended relation unambiguous, but the source variant is not silently
normalized.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `kaukṛtyam` | nominative singular neuter | remorse or regret |
| `vicikitsātaḥ` | ablative singular feminine | from doubt |
| `krodha-īrṣye` | nominative dual | anger and envy |
| `pratigha-anvaye` | nominative dual predicate compound | belonging to the lineage of hostility; glossed as arising from it |
| `anye ca` | nominative plural with conjunction | and other [factors] |
| `ṣaṭ kleśa-malāḥ` | nominative plural masculine | six stains of affliction |
| `māyā` | nominative singular feminine | deceit |
| `śāṭhyam` | nominative singular neuter | crookedness or duplicity |
| `madaḥ` | nominative singular masculine | intoxication or infatuation |
| `tathā` | indeclinable adverb | likewise, with the remaining members following |


The Bhāṣya glosses `pratighānvaye` as `pratighasamutthe`, “arisen from
hostility,” giving the compound a genetic rather than merely taxonomic force.

## 4. Grammar

**Completion of the paryavasthāna genealogy**

```text
kaukṛtyam
    vicikitsātaḥ [utthitam]

krodha-īrṣye
    pratigha-anvaye
```

The ablative supplies doubt as the source of remorse. The dual subject anger
and envy takes the dual predicate `pratighānvaye`; the Bhāṣya's plural-dual
sense is explicit in `pratighasamutthe`.

**Opening of the six stains**

```text
anye ca
    ṣaṭ kleśa-malāḥ

māyā
śāṭhyam
madaḥ
tathā [continuation in 5.50]
```

`Anye` marks a new group of upakleśas rather than further members of the ten
paryavasthānas. This verse names the first three; the remaining three and their
definitions begin with the distributed 5.50 verse.

## 5. Translation

### Literal Translation

> Remorse arises from doubt; anger and envy arise in dependence upon hostility.
> There are also six other stains of affliction: deceit, crookedness,
> intoxication, and likewise [three further stains].

### Bhāṣya-informed study translation

> Remorse arises from doubt; anger and envy arise from hostility. There are
> also six other stains of affliction, beginning with deceit, crookedness, and
> intoxication.

## 6. Philosophical Translation

> The source inquiry into the ten envelopments closes: remorse is assigned to
> doubt, anger and envy to hostility, and the ten are gathered as derivatives
> of affliction. The next determination opens a different sixfold class, the
> stains of affliction. Its first three names are given here; the class is not
> yet fully enumerated or explained.

The verse's transition distinguishes an established derivation from an
announced classification. The meaning of `mala` remains open here.

## 7. Technical Vocabulary

**`Kaukṛtya` — remorse**

Assigned here to doubt (`vicikitsā`). The verse gives its source, not a
psychological account of how doubt produces it.

**`Pratighānvaya` — belonging to hostility's lineage**

The Bhāṣya glosses the compound with `pratighasamutthe`, “arisen from
hostility,” for anger and envy. This establishes their local derivation.

**`Kleśa-niḥṣyanda` — derivative of affliction**

The Bhāṣya gathers the ten envelopments as upakleśas derivative of kleśas.
That collective statement retains the reported disagreement about
concealment's particular source in 5.48.

**`Kleśa-mala` — stain of affliction**

The new sixfold group is named here. The verse names `māyā` (deceit),
`śāṭhya` (crookedness), and `mada` (intoxication); the other three and the
individual definitions begin in 5.50. This unit does not define the general
force of “stain.”

## 8. Logical Determination

```text
NiḥṣyandaOf(Kaukṛtya, Vicikitsā)
ArisesFrom(Krodha, Pratigha)
ArisesFrom(Īrṣyā, Pratigha)

For x in TenVaibhāṣikaParyavasthānas:
    Upakleśa(x) AND KleśaNiḥṣyanda(x)

Count(KleśaMala) = 6
NamedHere(KleśaMala) = {Māyā, Śāṭhya, Mada}
```

The collective derivation does not settle the disputed particular ground of
`mrakṣa`. Nor does the announcement of six stains establish the unlisted
members' definitions or sources in this unit.

## 9. Interpretive Note

**Source determination.** The Bhāṣya gloss `pratighasamutthe` licenses “arise
from hostility” for anger and envy. Its following collective statement closes
the tenfold envelopment account. `Anye ca` then opens another group of six
upakleśas under the name `kleśa-mala`.

**Verse boundary.** Only deceit, crookedness, and intoxication are named at
[313|09–11]. The next three names and their definitions begin at [313|12] in
the distributed 5.50 verse. Their derivations follow later. This study leaves
that work to 5.50.

**Organon determination.** A completed source relation and a newly announced
class are distinct determinations. The latter can be recorded with its stated
count and three attested members before its full inventory is available.

## 10. OWL++ Seed

```text
Class: Paryavasthana
    SubClassOf: Upaklesa
Class: KlesaMala
    SubClassOf: Upaklesa

Rule: Remorse(?x)
    -> isNihsyandaOf(?x, Doubt)
Rule: Anger(?x) OR Envy(?x)
    -> arisesFrom(?x, Hostility)

Assertion: Count(KlesaMala, 6)
Assertion: NamedHere(Maya, KlesaMala)
Assertion: NamedHere(Sathya, KlesaMala)
Assertion: NamedHere(Mada, KlesaMala)

Constraint: CollectiveKlesaDerivation(TenParyavasthanas)
    doesNotSettle ParticularSource(Mraksa)
```

The seed records this verse's closure and the new class without importing the
continuation's names, definitions, or derivations.
