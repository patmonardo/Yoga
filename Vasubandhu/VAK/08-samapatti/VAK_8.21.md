# VAkK 8.21

## Sanskrit

न मौलाः कुशलारूप्याः सास्रवाधरगोचराः ।
अनास्रवेण हीयन्ते क्लेशाः सामन्तकेन च ॥ VAkK_8.21 ॥

## IAST

na maulāḥ kuśalārūpyāḥ sāsravādharagocarāḥ /
anāsraveṇa hīyante kleśāḥ sāmantakena ca // VAkK_8.21 //

## Source Caution

The source text is clear. The compounds require careful doctrinal parsing: `kuśalārūpyāḥ` refers to wholesome formless attainments, `sāsravādharagocarāḥ` to contaminated lower-level objects, and `sāmantakena` to a neighboring or preparatory attainment.

## Padaccheda

- na
- maulāḥ
- kuśala-ārūpyāḥ
- sāsrava-adhara-gocarāḥ
- anāsraveṇa
- hīyante
- kleśāḥ
- sāmantakena
- ca

## Grammar

- **na** — negation, “not.”
- **maulāḥ** — nominative plural masculine, “fundamental” or “root” attainments.
- **kuśalārūpyāḥ** — nominative plural masculine, “wholesome formless attainments.”
- **sāsravādharagocarāḥ** — nominative plural masculine compound, “having contaminated lower levels as their object.”
- **anāsraveṇa** — instrumental singular, “by the uncontaminated [attainment].”
- **hīyante** — 3rd person plural middle/passive, “are abandoned,” “are eliminated.”
- **kleśāḥ** — nominative plural masculine, “defilements.”
- **sāmantakena** — instrumental singular, “by the neighboring or preparatory attainment.”
- **ca** — “and.”

## Literal Translation

The fundamental wholesome formless attainments do not take contaminated lower levels as their object. Defilements are abandoned by the uncontaminated attainment and also by the neighboring attainment.

## Philosophical Translation

The root wholesome formless attainments do not descend intentionally toward contaminated lower-level objects. The actual abandonment of defilements is effected through uncontaminated attainment and through the adjoining preparatory stage that leads into it.

## Technical Vocabulary

- **maula** — fundamental, root, fully established attainment.
- **kuśala** — wholesome.
- **ārūpya** — formless attainment or formless level.
- **sāsrava** — contaminated, subject to outflows.
- **adhara** — lower.
- **gocara** — object-range, field, intentional domain.
- **anāsrava** — uncontaminated.
- **kleśa** — defilement.
- **sāmantaka** — neighboring, access, preparatory attainment immediately adjoining a fundamental attainment.

## Doctrinal Determination

The verse makes two distinctions.

First, it limits the intentional range of the fundamental wholesome formless attainments. They do not take contaminated states belonging to lower levels as objects. Their object-range is therefore determined by the purity and elevation proper to their level.

Second, it identifies the operative grounds of abandonment. Defilements are relinquished through:

1. the uncontaminated attainment itself;
2. the neighboring preparatory attainment that immediately approaches it.

This means that the transition into liberating cognition is not groundless. The adjoining stage has a genuine causal role in the abandonment of defilements.

## Logical Determination

The verse distinguishes:

```text
object-law
    fundamental wholesome formless attainment
        does not descend toward contaminated lower objects

causal law
    uncontaminated attainment
        abandons defilements

    neighboring attainment
        also abandons defilements
```

A system is genetically complete only when the transition is supplied with its ground. Here the higher attainment is not merely placed after the preparatory one. The preparatory stage is shown to participate in the production of the result.

Thus the transition has the form:

```text
neighboring ground
    → abandonment begins
    → uncontaminated attainment
    → abandonment is completed
```

## Organon Light

This verse is especially important for a genetic science of divisions and transitions.

A merely classificatory system says:

```text
preparatory attainment
then
fundamental uncontaminated attainment
```

A genetic system must say why the first passes into the second and what work the first already performs.

The neighboring attainment is therefore not an external corridor between two finished states. It is the determinate ground through which the later state becomes possible. The transition itself belongs to the Concept of the attainment.

This also clarifies why the root wholesome formless attainments do not simply range backward over contaminated lower objects. Their object-range expresses the qualitative determination already achieved.

## OWL++ Seed

```text
Class: FundamentalWholesomeFormlessAttainment
Class: ContaminatedLowerObject
Class: UncontaminatedAttainment
Class: NeighboringAttainment
Class: Defilement

ObjectProperty: hasObject
ObjectProperty: abandons
ObjectProperty: preparesFor

Constraint:
FundamentalWholesomeFormlessAttainment
    not hasObject ContaminatedLowerObject.

Rule:
UncontaminatedAttainment
    abandons Defilement.

Rule:
NeighboringAttainment
    abandons Defilement
    and preparesFor UncontaminatedAttainment.
```

## Commit History

- Initial Sanskrit-first analysis of VAkK 8.21.
