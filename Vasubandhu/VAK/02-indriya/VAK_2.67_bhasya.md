# VAK_2.67_bhasya — Desire-Realm Citta Transition Matrix I

## Kārikā

```text
kāme nava śubhāc cittāc cittāni aṣṭābhya eva tat /
daśabhyo 'kuśalaṃ tasmāc catvāri nivṛtaṃ tathā // VAkK_2.67 //
```

## Working Translation

```text
In the desire realm, nine cittas arise immediately after a wholesome citta;
that wholesome citta itself arises immediately after eight.
An unwholesome citta arises after ten, and from it four arise;
an obscured-neutral citta is likewise [ten before it, four after it].
```

## Bhāṣya — Continuous Translation

A wholesome citta belonging to the desire realm is immediately followed by nine cittas.

These are the four cittas of its own realm; two belonging to the form realm; an obscured citta belonging to the formless realm at the time of rebirth-linking; and the trainee and beyond-training cittas.

Within the form realm, the wholesome citta arises after the desire-realm wholesome citta when one enters meditative attainment; the obscured citta arises at rebirth-linking. In the formless realm only the obscured citta follows at rebirth-linking, not a wholesome citta, because the formless realm is too remote from the desire realm. The formless attainments are remote from the desire realm in four respects: support, mode, object, and antidote.

Conversely, a wholesome desire-realm citta arises immediately after eight cittas: the four cittas of its own realm; two belonging to the form realm; and the trainee and beyond-training cittas.

It arises after a wholesome form-realm citta when one emerges from attainment. It can arise after an obscured form-realm citta when a person oppressed by a defiled attainment resorts to the wholesome level serving as support. It also arises after trainee and beyond-training cittas when one emerges from those states.

An unwholesome desire-realm citta arises immediately after ten cittas. Excluding trainee and beyond-training cognition, it can arise at rebirth-linking after all cittas belonging to the form and formless realms.

From an unwholesome citta, only the four cittas of the desire realm arise immediately.

The obscured-neutral citta of the desire realm is the same in this respect: it arises immediately after ten, and only the four desire-realm cittas arise immediately after it.

## Voice

**Voice:** Vasubandhu presenting the Abhidharma transition scheme.

The verse is classificatory, but the prose explanations supply the operative reasons for exceptional transitions: meditative entry and emergence, rebirth-linking, and the relative remoteness of realms.

## New Technical Terms

- **pratisaṃdhi / pratisaṃdhikāla** — rebirth-linking / the moment of rebirth-linking
  - **status:** previously encountered doctrinally, newly important here as a transition operator
  - **function:** explains cross-realm citta succession at the beginning of a new existence

- **vyutthāna / vyutthānakāla** — emergence from attainment
  - **status:** rare in the Kārikā analysis
  - **function:** explains transition from higher or pure cognition back to desire-realm wholesome citta

- **samāpatti** — meditative attainment
  - **status:** previously encountered
  - **function:** here not treated as a static state but as a transition-context permitting ascent to a higher-realm wholesome citta

- **kliṣṭa-samāpatti** — defiled attainment
  - **status:** Bhāṣya-specific in this local passage
  - **function:** explains why one can fall back upon a wholesome support-level after being afflicted by a defiled meditative state

- **ādhāra-kuśala-bhūmi** — wholesome supporting level
  - **status:** Bhāṣya-specific expression
  - **function:** names the wholesome base resorted to after pressure from a defiled attainment

- **dūratā** — remoteness
  - **status:** newly technical here
  - **function:** restricts possible immediate transitions between realms

- **āśraya-dūratā** — remoteness of support
  - **status:** Bhāṣya-only technical distinction in this passage
  - **function:** one of four reasons why desire and formless realms do not connect through a direct wholesome transition

- **ākāra-dūratā** — remoteness of cognitive mode/aspect
  - **status:** Bhāṣya-only technical distinction in this passage
  - **function:** restricts cross-realm transition

- **ālambana-dūratā** — remoteness of object
  - **status:** Bhāṣya-only technical distinction in this passage
  - **function:** restricts cross-realm transition

- **pratipakṣa-dūratā** — remoteness of antidote
  - **status:** Bhāṣya-only technical distinction in this passage
  - **function:** restricts cross-realm transition by difference of counteractive function

## Transition Table

```text
Kāma wholesome -> 9
    4 kāma cittas
    2 rūpa cittas
    1 ārūpya obscured citta at rebirth-linking
    śaikṣa
    aśaikṣa

Kāma wholesome <- 8
    4 kāma cittas
    2 rūpa cittas
    śaikṣa
    aśaikṣa

Kāma unwholesome <- 10
    all relevant realm-bound cittas except śaikṣa/aśaikṣa

Kāma unwholesome -> 4
    only the four kāma cittas

Kāma obscured-neutral <- 10
    same count-profile as unwholesome

Kāma obscured-neutral -> 4
    only the four kāma cittas
```

## Doctrinal Determination

The verse converts `samanantara-pratyaya` from a general relation into a typed transition system.

A previous citta does not merely precede the next. Its realm, ethical status, meditative context, and path-status constrain what can arise immediately afterward.

The Bhāṣya therefore distinguishes several kinds of transition-context:

```text
ordinary within-realm succession
samāpatti-entry
samāpatti-emergence
rebirth-linking
return from pure/path cognition
```

The cross-realm rules are not arbitrary. The impossibility of a direct wholesome transition from desire to formless cognition is explained through four kinds of remoteness: support, cognitive mode, object, and antidote.

## Translation Consequences

`Samanantara` should not be weakened to mere temporal adjacency. Here it functions as a rule-governed immediate succession relation.

Likewise, the numerical counts in the Kārikā are not bare scholastic bookkeeping. The Bhāṣya supplies the transition semantics behind the numbers.

A useful working translation for the relation is therefore:

```text
immediately antecedent condition
= the prior citta insofar as it licenses a determinate next citta
```

## Limited Organon Interpretation

This passage gives a genuine finite-state transition architecture for citta.

```text
CittaState:
    realm
    ethical/status class
    obscuration status
    path status
    meditative context

Transition:
    source state
    target state
    admissibility condition
```

The rational content lies not in the numerical count by itself, but in the determination of admissible succession.

In the comparative framework developed in this project, this strengthens the interpretation of `pratyaya` as rationally articulated subjectivity: cognition is not a sequence of private states but a lawful transition-field in which some determinations can follow others and some cannot.

This should remain a comparative reconstruction, not an attribution of Kantian or Organon terminology to Vasubandhu.

## Relation to VAK 2.66

VAK 2.66 supplied the twelve citta classes.

VAK 2.67 begins the transition function over that class-space:

```text
2.66 = state-types
2.67ff = permitted immediate transitions
```

This is the first detailed operationalization of `samanantara-pratyaya` after its general definition in VAK 2.62.
