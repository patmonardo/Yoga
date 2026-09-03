# VAK_5.50

## 1. Sanskrit (Devanāgarī)

```sanskrit
प्रदाश उपनाहश्च विहिंसा चेति रागजौ ।
मायामदौ प्रतिघजे उपनाहविहिंसने ॥ ५.५० ॥
```

## 2. Sanskrit (IAST)

```text
pradāśa upanāhaś ca vihiṃsā ceti rāgajau |
māyā-madau pratighaje upanāha-vihiṃsane || 5.50 ||
```

VAK 5.50 completes the six stains of affliction begun in VAK 5.49 and assigns
four of them to two afflictive sources. The remaining sources of `pradāśa` and
`śāṭhya` are stated in VAK 5.51.

## 3. Padaccheda and Lexical Analysis

```text
pradāśaḥ | upanāhaḥ | ca | vihiṃsā | ca | iti |
rāga-jau | māyā-madau | pratigha-je | upanāha-vihiṃsane
```

| Form | Morphology | Contextual sense |
|---|---|---|
| `pradāśaḥ` | nominative singular masculine | obstinate fault-clinging or resistance to correction |
| `upanāhaḥ` | nominative singular masculine | sustained resentment or rancor |
| `vihiṃsā` | nominative singular feminine | harmfulness or injuriousness |
| `ca iti` | conjunction with quotative closure | and thus, completing the list |
| `rāga-jau` | nominative dual masculine | the two born from attachment |
| `māyā-madau` | nominative dual masculine | deceit and intoxication |
| `pratigha-je` | nominative dual feminine | the two born from hostility |
| `upanāha-vihiṃsane` | nominative dual feminine | sustained resentment and harmfulness |

The two paired constructions are syntactically exact:

```text
rāga-jau māyā-madau
pratigha-je upanāha-vihiṃsane
```

Each source adjective agrees with its dual pair.

## 4. Grammar

**Completion of the six-member list**

```text
pradāśaḥ
upanāhaḥ ca
vihiṃsā ca
    iti
```

`Iti` closes the enumeration begun with deceit, crookedness, and intoxication
in VAK 5.49. It does not close the subsequent genetic analysis.

**Attachment-born pair**

```text
māyā-madau
    rāga-jau
```

The dual compound joins deceit and intoxication; `rāgajau` predicates their
common origin in attachment.

**Hostility-born pair**

```text
upanāha-vihiṃsane
    pratigha-je
```

The dual joins sustained resentment and harmfulness; `pratighaje` predicates
their origin in hostility. The sources of the other two stains are deliberately
left to the next verse.

## 5. Translation

### Literal Translation

> Obstinate fault-clinging, sustained resentment, and harmfulness—thus [the six
> stains are completed]. Deceit and intoxication are the two born from
> attachment; sustained resentment and harmfulness are the two born from
> hostility.

### Bhāṣya-informed study translation

> The six stains are deceit, crookedness, intoxication, obstinate adherence to
> a blameworthy matter, sustained resentment, and harmfulness. Deceit is the
> deceiving of another; crookedness prevents straightforward disclosure;
> `pradāśa` firmly clings to a blameworthy position and rejects proper
> admonition; `upanāha` repeatedly intensifies a basis of resentment; and
> `vihiṃsā` injures others through striking, harshness, and similar acts. Of
> these six, deceit and intoxication are born from attachment, while sustained
> resentment and harmfulness are born from hostility. The origins of
> `pradāśa` and crookedness remain for VAK 5.51.

The definitions and controlled four-member genealogy are supplied by the
Bhāṣya.

## 6. Philosophical Translation

> One class can contain members with different origins and different
> operations. Deceit and intoxication share attachment as their stated source;
> sustained resentment and harmfulness share hostility. Yet class-membership
> does not reduce either pair to one act: deception alters another's
> apprehension, intoxication is a distinct self-affective condition, resentment
> reiterates an injury-basis, and harmfulness performs injury. The text therefore
> determines each stain along separate axes—what it is called, what it does,
> and from which affliction it arises—while leaving two genetic relations open
> for the next step.

The verse states genealogies but does not itself provide speculative mechanisms
explaining why each source necessarily produces its assigned pair.

## 7. Technical Vocabulary

**`Kleśa-mala` — stain of affliction**

The stable six-member class introduced in VAK 5.49 and completed here. Its
members do not share a single source, so class-membership and genealogy must
remain distinct.

**`Pradāśa` — obstinate fault-clinging**

Defined as firm grasping of a blameworthy matter
(`sāvadyavastu-dṛḍhagrāhitā`) through which one refuses proper or reasoned
admonition (`nyāya-saṃjñapti`). The Bhāṣya does not define it primarily as
exposing or attacking another's fault.

**`Upanāha` — sustained resentment or rancor**

Defined as repeated enlargement of a basis of resentment or injury
(`āghātavastu-vahulīkāra`). Reiteration and intensification distinguish it
from a merely initial hostile event.

**`Vihiṃsā` — harmfulness**

Defined as injuring others (`viheṭhana`) through striking, harshness, and the
like.

**`Māyā` — deceit**

Defined here as deceiving another (`paravañcanā`). The term does not denote a
cosmic principle of appearance in this Abhidharma context.

**`Śāṭhya` — crookedness or duplicity**

Crookedness of mind by which matters are not disclosed as they actually are.
Its genetic affiliation is deferred to VAK 5.51.

**`Mada` — intoxication or infatuation**

Previously defined in the Kośa and here classified as born from attachment.
The Bhāṣya does not repeat its definition in this passage.

**`Rāgaja` — born from attachment**

The genetic predicate of deceit and intoxication. It states origin, not their
complete function.

**`Pratighaja` — born from hostility**

The genetic predicate of sustained resentment and harmfulness.

## 8. Logical Determination

The complete class is:

```text
Extension(KleśaMala)
    = {Māyā, Śāṭhya, Mada, Pradāśa, Upanāha, Vihiṃsā}
```

VAK 5.50 establishes four source-assertions:

```text
BornFrom(Māyā, Rāga)
BornFrom(Mada, Rāga)

BornFrom(Upanāha, Pratigha)
BornFrom(Vihiṃsā, Pratigha)
```

Their operations remain differentiated:

```text
Māyā       → DeceivesAnother
Pradāśa    → RejectsProperAdmonition
Upanāha    → RepeatedlyIntensifiesResentment
Vihiṃsā    → InjuresAnother
```

Therefore:

```text
MemberOf(x, KleśaMala)
    ⇏ SameOrigin(x, everyOtherMember)

SameOrigin(x, y)
    ⇏ SameOperation(x, y)

DefinedOperation(x)
    ⇏ SettledOrigin(x)
```

The last rule accounts for `pradāśa` and `śāṭhya`: both have operational
definitions before their sources are stated.

## 9. Interpretive Note

**Source determination.** The Bhāṣya presents the definitions before assigning
roots. The sequence itself distinguishes three questions:

```text
What factor is being discussed?
What does it do?
From which kleśa is it born?
```

VAK 5.50 answers the third question for four of the six.

**Two sources, four stains.** Deceit and intoxication belong to attachment;
sustained resentment and harmfulness belong to hostility. The text does not
say that all stains arise from one universal “staining” cause, nor that every
factor born from the same root has an interchangeable function.

**Correction of `pradāśa`.** Its direct Bhāṣya definition concerns the agent's
firm adherence to a blameworthy matter and refusal of proper correction. A
rendering centered on malicious exposure of someone else's fault reverses the
relation and should not control the official study.

**Path contact.** The passage gives a basis for differentiated diagnosis but
not yet a catalogue of remedies. One must distinguish a stain's concrete
operation from its source-affiliation before relating either to abandonment.
That soteriological axis becomes explicit in the next verses.

**Organon interpretation.** The Dataset should represent class, source, and
operation independently:

```text
StainAssertion
    hasFactor
    memberOf KleśaMala
    bornFrom RootAffliction
    performs Operation
    supportedBy SourceSpan
```

This allows incomplete-but-controlled knowledge: four sources can be asserted
without inventing the remaining two, while all six operational definitions
remain available.

## 10. OWL++ Seed

```text
Class: AfflictiveFactor
Class: RootAffliction
Class: KlesaMala
    SubClassOf: AfflictiveFactor
Class: FunctionalOperation
Class: SourceAssertion

Class: Deceit
    SubClassOf: KlesaMala
Class: Crookedness
    SubClassOf: KlesaMala
Class: Intoxication
    SubClassOf: KlesaMala
Class: Obstinacy
    SubClassOf: KlesaMala
Class: Resentment
    SubClassOf: KlesaMala
Class: Harmfulness
    SubClassOf: KlesaMala

ObjectProperty: bornFrom
    Domain: KlesaMala
    Range: RootAffliction

ObjectProperty: performsOperation
    Domain: KlesaMala
    Range: FunctionalOperation

ObjectProperty: supportedBySource
    Domain: SourceAssertion

Rule: Deceit(?x)
    OR Intoxication(?x)
    -> bornFrom(?x, Attachment)

Rule: Resentment(?x)
    OR Harmfulness(?x)
    -> bornFrom(?x, Hostility)

Rule: Deceit(?x)
    -> performsOperation(?x, DeceivingAnother)

Rule: Obstinacy(?x)
    -> performsOperation(?x, RejectingProperAdmonition)

Rule: Resentment(?x)
    -> performsOperation(?x, IntensifyingBasisOfInjury)

Rule: Harmfulness(?x)
    -> performsOperation(?x, InjuringAnother)

Constraint: SameClass(?x, ?y, KlesaMala)
    doesNotEntail SameRoot(?x, ?y)

Constraint: SameRoot(?x, ?y)
    doesNotEntail SameOperation(?x, ?y)

View: SixAfflictiveStains
    Preserves: FactorIdentity, OperationalDefinition, RootAffiliation,
               UnresolvedAffiliation, SourceProvenance
```

The seed permits the six-member class to remain complete while its genealogy
is completed incrementally and without conflating common origin with common
operation.
