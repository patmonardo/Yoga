# VAK_2.70_bhasya — Outflow-Free and Path Citta Transition Counts

## Kārikā

```text
nava cittāni tat ṣaṇṇāṃ nivṛtāt sapta tat tathā /
caturbhyaḥ śaikṣam asmāt tu pañca aśaikṣaṃ tu pañcakāt // VAkK_2.70 //
```

## Bhāṣya — Continuous Translation

From wholesome citta of the formless realm, nine cittas arise. This wholesome formless citta itself arises from six: the three cittas of its own realm, wholesome citta of the form realm, and the trainee and beyond-training cittas.

From obscured citta of the formless realm, seven cittas arise: the three cittas of its own realm, wholesome and obscured citta of the form realm, and the two afflicted cittas of the desire realm. That obscured formless citta itself likewise arises from seven, excluding the afflicted cittas of the desire and form realms and the trainee and beyond-training cittas.

The trainee citta arises from four: the wholesome cittas of the three realms and trainee citta itself.

From this trainee citta arise five: those same four and beyond-training citta.

Beyond-training citta arises from five, namely the very five just mentioned.

From beyond-training citta, four cittas arise immediately afterward: the wholesome cittas of the three realms and beyond-training citta itself.

Thus the twelve cittas are completed.

## Voices

- **Voice: Vasubandhu / expository Abhidharma voice** — states and explains the transition counts.
- **Voice: Vaibhāṣika framework** — the twelvefold citta-classification and samanantara transition system presuppose the Abhidharma causal scheme used throughout this section.

## New Technical Terms

- **śaikṣa** — trainee citta; outflow-free cognition belonging to one still in training.
  - **status** — previously encountered in the Kārikā analysis.
  - **function** — path-status feature in the citta transition grammar.
- **aśaikṣa** — beyond-training citta; outflow-free cognition of one for whom training is complete.
  - **status** — previously encountered.
  - **function** — terminal path-status feature in the citta transition grammar.
- **samanantara** — immediately antecedent relation.
  - **status** — previously encountered.
  - **function** — production/transition relation licensing the next citta.

## Translation Consequences

The verse closes the twelve-state citta transition matrix. The crucial point is not the arithmetic itself but the fact that path-status is built into the transition system. A trainee citta can produce beyond-training citta, but beyond-training citta does not revert to trainee citta. Thus the grammar of succession is not symmetric.

## Doctrinal / Logical Determination

The twelve citta-types now form a typed state-space with directed transition rules.

```text
CittaState:
    realm
    ethicalStatus
    obscurationStatus
    outflowStatus
    pathStatus

TransitionRule:
    sourceState
    permittedSuccessorSet
```

The path distinction is structurally decisive:

```text
śaikṣa
    -> śaikṣa
    -> aśaikṣa

but

aśaikṣa
    -> aśaikṣa
    not -> śaikṣa
```

This is a directional liberation grammar rather than mere empirical succession.

## Organon Interpretation

In the Workbook reading, VAK 2.70 gives a clean example of a Feature Grammar production constrained by path-status. `śaikṣa` and `aśaikṣa` are not merely labels attached to citta; they alter which productions are licensed.

```text
Citta[pathStatus=trainee]
    -> {realm-wholesome cittas, trainee, beyond-training}

Citta[pathStatus=beyond-training]
    -> {realm-wholesome cittas, beyond-training}
```

The asymmetry is philosophically important. Completion is represented formally as restriction of backward transition. The state-space itself therefore encodes a practical direction: cognition can cross from training to completed training, but the completed state is not defined by regression to the trainee state.

For Organon Dataset purposes this is an exemplary solution pattern:

```text
Feature structure
+ transition relation
+ asymmetry constraint
= rational production rule
```

## Summary

VAK 2.70 completes the twelvefold citta matrix and brings the pratyaya analysis directly into the Path. The immediately antecedent condition is therefore not a neutral temporal relation: it is a typed rule of lawful cognitive succession, including the irreversible transition from training to beyond-training.
