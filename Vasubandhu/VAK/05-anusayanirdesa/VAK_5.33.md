# VAK 5.33

## Sanskrit

ततोऽन्तग्रहणं तस्माच्छीलामर्शस्ततो दृशः ।
रागः स्वदृष्टौ मानश्च द्वेषोऽन्यत्रेत्यनुक्रमः ॥ ५.३३ ॥

## IAST

*tato ’ntagrahaṇaṃ tasmāc chīlāmarśas tato dṛśaḥ |*
*rāgaḥ svadṛṣṭau mānaś ca dveṣo ’nyatra ity anukramaḥ || 5.33 ||*

## Padaccheda

*tataḥ | antagrahaṇam | tasmāt | śīlāmarśaḥ | tataḥ | dṛśaḥ | rāgaḥ | sva-dṛṣṭau | mānaḥ | ca | dveṣaḥ | anyatra | iti | anukramaḥ*

## Grammar

- **tataḥ / tasmāt** — ablatival adverbs: “from that,” marking causal or genetic succession.
- **antagrahaṇam** — nominative singular neuter: “grasping an extreme,” i.e. the extreme view.
- **śīlāmarśaḥ** — nominative singular masculine; abbreviated expression for attachment to discipline and observance as intrinsically salvific.
- **dṛśaḥ** — genitive singular of *dṛś* / *dṛṣṭi*: “of the view” or “from the view,” understood within the compressed sequence.
- **sva-dṛṣṭau** — locative singular: “with respect to one’s own view.”
- **rāgaḥ, mānaḥ, dveṣaḥ** — nominative singular masculine subjects.
- **anyatra** — “elsewhere,” here: toward another or a different view.
- **iti anukramaḥ** — “such is the sequence.”

## Literal Translation

From that comes grasping an extreme; from that, attachment to discipline; then, regarding the view, attachment and pride in one’s own view, and hatred toward another—such is the sequence.

## Philosophical Translation

From constructed selfhood arises fixation upon an extreme. From extreme fixation arises absolutization of a prescribed practice. One then becomes attached to and proud of one’s own view, while becoming hostile toward what stands outside it. This is the ordered genesis of dogmatic conflict.

## Analysis

VAK 5.32 began the sequence:

```text
moha
  → uncertainty
    → false view
      → personality-view
```

VAK 5.33 completes it:

```text
personality-view
  → extreme view
    → absolutized discipline or observance
      → attachment to one’s own view
        → pride in that view
          → hostility toward another
```

The verse is therefore not merely enumerating afflictions. It presents a **genetic order** in which one distorted determination prepares the next.

### 1. From self-construction to extreme determination

Once a constructed aggregate is taken as self, thought is driven toward an extreme:

```text
self is permanent
or
self is annihilated
```

The false center demands an absolute temporal determination.

### 2. From extreme view to ritual absolutization

A fixed metaphysical stance then seeks a fixed practical guarantee. Discipline, observance, or ritual is no longer treated as a conditioned means but grasped as intrinsically and universally sufficient.

Thus:

```text
false ontology
  → absolutized practice
```

### 3. From doctrine to affective investment

The view is no longer merely entertained. It becomes an object of:

- **rāga** — attachment,
- **māna** — pride,
- **dveṣa** — hostility toward alternatives.

The system therefore distinguishes:

```text
holding a proposition
  ≠
being affectively bound to it
```

A cognition becomes practically dangerous when its content is joined to possessive attachment and comparative self-elevation.

### 4. The production of the enemy

The phrase **dveṣo ’nyatra** marks the final externalization. Once one’s own view has become a support of identity and pride, another view appears not simply as false but as threatening.

The sequence therefore generates polarization:

```text
undetermined cognition
  → false determination
    → identity investment
      → in-group elevation
        → out-group hostility
```

## Technical Vocabulary

| Term | Determination |
|---|---|
| *antagrahaṇa* | grasping one of two extremes |
| *śīlāmarśa* | absolutizing discipline or observance |
| *sva-dṛṣṭi* | one’s own adopted view |
| *rāga* | possessive attachment |
| *māna* | comparative self-elevation or pride |
| *dveṣa* | aversion or hostility |
| *anukrama* | ordered succession or genetic sequence |

## Doctrinal Determination

The afflictions form a conditioned series. A doctrinal error becomes practically operative by acquiring affective force.

The verse thus links three layers:

```text
cognitive error
  → normative fixation
    → affective conflict
```

Wrong view is not isolated intellectual content. It can organize conduct, identity, and opposition.

## Logical Determination

The sequence may be represented as a directed dependency structure:

```text
moha
  causes uncertainty
uncertainty
  conditions false judgment
false judgment
  stabilizes a false subject
false subject
  demands an extreme predicate
extreme predicate
  absolutizes a practice
absolutized practice
  becomes identity-bearing doctrine
doctrinal identity
  generates attachment, pride, and hostility
```

The key logical distinction is:

```text
isBelieved
  ≠
isIdentityBearing
```

and:

```text
isIdentityBearing
  → mayGenerateAffectiveForce
```

## Organon Note

For the Dialectical Copula, a proposition must not be represented only as a subject–predicate assertion. The system also needs to record the practical powers attached to the assertion:

```text
Agent
  holds View
Agent
  identifiesWith View
Agent
  derivesStatusFrom View
Agent
  opposes AlternativeView
```

These are distinct relations.

A practical reasoning system should therefore detect the transition:

```text
claim
  → commitment
    → identity
      → pride
        → antagonism
```

This is especially relevant to LLM reasoning. A model may begin with uncertainty, prematurely settle on an unsupported conclusion, preserve it through self-consistency, and then reject contrary evidence because the earlier conclusion has become structurally privileged.

The corrective intervention is not merely “supply the right fact.” It may require undoing the entire dependency chain.

## OWL++ Seed

```text
Class: AfflictiveSequence
Class: View
Class: ExtremeView
Class: AbsolutizedPractice
Class: AffectiveInvestment

ObjectProperty: arisesFrom
ObjectProperty: identifiesWith
ObjectProperty: isAttachedTo
ObjectProperty: isProudOf
ObjectProperty: isHostileToward
ObjectProperty: conditions

ExtremeView
  arisesFrom some PersonalityView

AbsolutizedPractice
  arisesFrom some ExtremeView

AffectiveInvestment
  isAttachedTo some View
  or isProudOf some View
  or isHostileToward some AlternativeView
```

Possible rule:

```text
identifiesWith(?agent, ?view)
∧ isProudOf(?agent, ?view)
∧ contradicts(?otherView, ?view)
→ riskOfHostilityToward(?agent, ?otherView)
```

This must remain a risk inference, not a deterministic identification.

## Bhāṣya Questions

1. How precisely does the Bhāṣya construe **tato dṛśaḥ** in the compressed syntax?
2. Is **śīlāmarśa** treated here specifically as *śīlavrataparāmarśa*, and which causal link is emphasized?
3. Does Vasubandhu understand attachment and pride as arising simultaneously with respect to one’s own view?
4. Is **dveṣo ’nyatra** directed toward rival doctrines, rival practitioners, or any object opposed to the adopted view?
5. How strongly does the Bhāṣya treat this as a strict causal sequence rather than a typical order of manifestation?
