# VAK_7.12 — Fourteen and Sixteen Aspects

## Sanskrit

### Devanāgarī

```text
शेषे चतुर्दशाकारे शून्यानात्मविवर्जिते ।
नामलः षोडशभ्योऽन्य आकारोऽन्येऽस्ति शास्त्रतः ॥ ७.१२ ॥
```

### IAST

```text
śeṣe caturdaśākāre śūnyānātmavivarjite /
nāmalaḥ ṣoḍaśabhyo 'nya ākāro 'nye 'sti śāstrataḥ // VAK_7.12 //
```

## Source Caution

The verse is compressed and contains an explicit doctrinal disagreement. The first half assigns fourteen aspects to the remaining knowledges by excluding the aspects of emptiness and non-self. The second half states the principal position that no pure aspect exists beyond the sixteen truth-aspects, while noting that others admit an additional aspect on scriptural authority.

The exact scope of `śeṣe` should be read together with VAK 7.10–7.11 and the bhāṣya. This first pass therefore preserves “the remaining knowledges” without forcing a narrower allocation prematurely.

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| śeṣe | locative singular used distributively or substantively | in the remaining case; among the remaining knowledges |
| caturdaśa-ākāre | locative singular | having fourteen aspects |
| śūnya-anātma-vivarjite | locative singular | excluding emptiness and non-self |
| na | indeclinable negation, contracted in `nāmalaḥ` | not |
| amalaḥ | nominative singular masculine | pure; undefiled |
| ṣoḍaśabhyaḥ | ablative plural | beyond or other than the sixteen |
| anyaḥ ākāraḥ | nominative singular masculine | another aspect |
| anye | nominative plural masculine | others |
| asti | third-person singular present | there is |
| śāstrataḥ | ablative adverbial expression | on scriptural authority; according to scripture |

## Grammar

The first half gives a numerical restriction:

```text
fourteen aspects
    because two are excluded

excluded:
    emptiness
    non-self
```

The second half states a thesis and an opposing view:

```text
principal thesis:
    no pure aspect exists beyond the sixteen

alternative thesis:
    another exists
    according to scriptural authority
```

`nāmalaḥ` is read as `na amalaḥ`: “for the pure, there is no other aspect.” The construction `ṣoḍaśabhyo 'nya ākāraḥ` means an aspect other than or beyond the sixteen.

## Literal Translation

Among the remaining knowledges there are fourteen aspects, with emptiness and non-self excluded. For the pure there is no aspect other than the sixteen; others hold that there is one, on scriptural authority.

## Philosophical Translation

The remaining forms of knowledge operate through fourteen truth-aspects because they do not assume the aspects of emptiness and non-self. Pure knowledge, according to the principal position, admits no mode of apprehension beyond the established sixteen truth-aspects, although another school accepts an additional pure aspect on scriptural grounds.

## Technical Vocabulary

### caturdaśākāra

```text
caturdaśākāra
    = fourteen-aspected
    = the sixteen truth-aspects
      minus emptiness and non-self
```

The number fourteen is grounded by exclusion, not merely asserted.

### śūnya

```text
śūnya
    = empty
    = an aspect under which conditioned reality is apprehended
```

Here it is one of the two excluded aspects.

### anātman

```text
anātman
    = non-self
    = absence of an enduring self in the apprehended field
```

It is excluded together with emptiness in the fourteenfold range.

### amala

```text
amala
    = pure
    = undefiled cognition
```

The principal thesis restricts pure cognition to the established sixteen truth-aspects.

### śāstrataḥ

```text
śāstrataḥ
    = according to scripture
    = on textual authority
```

The verse records an alternative doctrinal claim without yet adjudicating it fully.

## Doctrinal Determination

VAK 7.12 continues the distribution of the grounds announced in VAK 7.08. The relevant ground remains `ākāra`, the mode under which knowledge apprehends its object.

The verse gives two determinations.

### Fourteenfold range

```text
sixteen truth-aspects
    minus emptiness
    minus non-self
    = fourteen aspects
```

The restriction is exact: these knowledges are not simply described as “limited.” Their limit is numerically grounded by the absence of two determinate modes.

### Pure range

```text
principal position:
    pure knowledge
        sixteen aspects only

alternative position:
    an additional pure aspect
        admitted from scripture
```

Thus the verse preserves both systematic restriction and scholastic disagreement.

## Logical Determination

This is another grounded division, now by subtraction and boundary.

```text
complete aspect-system
    sixteen

restricted aspect-system
    sixteen minus two
    fourteen
```

The second half then marks the boundary of the pure system:

```text
inside the system
    sixteen established aspects

possible beyond
    denied by the principal position
    affirmed by others through testimony
```

The important point is methodological. A numerical classification is justified by naming what is excluded, while a disputed extension is explicitly marked by its source of authority.

## Organon Light

VAK 7.12 remains within disciplined Reflection. It does not derive the sixteen genetically; it specifies the limits of their distribution.

```text
Reflection
    identifies the aspect-range

Ground
    states the excluded determinations

Doctrinal dispute
    asks whether the established boundary is complete
```

The verse therefore shows two different forms of justification:

```text
systematic ground
    fourteen follows from sixteen minus two

scriptural ground
    an additional aspect is claimed by others
```

That distinction is useful for the Organon Dataset. A proposition should record not only what is asserted, but the kind of warrant under which it is asserted:

```text
structural derivation
    versus
textual authority
```

No larger transcendental mapping is imposed in this first pass.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_7_12
    a vak:Karika ;
    rdfs:label "VAK 7.12" ;
    vak:determines jna:FourteenAspectRange,
                   jna:SixteenPureAspects,
                   jna:EmptinessAspect,
                   jna:NonSelfAspect,
                   jna:ScripturalAlternative .

jna:FourteenAspectRange
    a jna:AspectRange ;
    jna:excludes jna:EmptinessAspect,
                 jna:NonSelfAspect .

jna:SixteenPureAspects
    a jna:AspectRange ;
    jna:appliesTo jna:PureKnowledge .

jna:ScripturalAlternative
    a jna:DoctrinalPosition ;
    jna:isGroundedBy jna:ScripturalAuthority .
```

## Commit History

```text
2026-07-23 — Initial kārikā-pass analysis.
```
