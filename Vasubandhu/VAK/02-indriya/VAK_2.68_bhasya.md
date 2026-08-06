# VAK_2.68_bhasya — Desire-Realm Unobscured and Form-Realm Wholesome Citta Transitions

## Kārikā

```text
pañcabhyo 'nivṛtaṃ tasmāt sapta cittāny anantaram /
rūpe daśaikaṃ ca śubhāt navabhyas tadanantaram // VAkK_2.68 //
```

## Working Translation

```text
In the desire realm, the unobscured citta arises immediately after five;
from it, seven cittas arise immediately afterward.

In the form realm, eleven cittas arise immediately after a wholesome citta;
and that wholesome citta itself arises immediately after nine.
```

## Bhāṣya — Continuous Translation

**Voice: Vasubandhu**

The qualification “in the desire realm” continues to apply. An unobscured-indeterminate citta arises immediately after five cittas: after the four cittas of its own realm, and after a wholesome citta of the form realm, in the case of a constructive (`nirmāṇa`) citta.

Immediately after an unobscured-indeterminate desire-realm citta, seven cittas can arise: the four cittas of its own realm; two belonging to the form realm; and one afflicted citta belonging to the formless realm.

The form-realm wholesome citta follows a constructive citta immediately. The afflicted form-realm citta arises at the time of rebirth-linking (`pratisaṃdhi`). The afflicted formless-realm citta likewise arises only at the time of rebirth-linking.

In the form realm, eleven cittas can arise immediately after a wholesome citta: all except the unobscured-indeterminate citta of the formless realm.

Conversely, a wholesome form-realm citta can arise immediately after nine cittas: all except the two afflicted cittas of the desire realm and the unobscured-indeterminate citta of the formless realm.

## Transition Matrix

### Desire-Realm Unobscured-Indeterminate Citta

```text
PREDECESSORS = 5

4 desire-realm cittas
+ 1 form-realm wholesome citta
  [when the transition is through nirmāṇa-citta]
```

```text
SUCCESSORS = 7

4 desire-realm cittas
+ 2 form-realm cittas
+ 1 afflicted formless-realm citta
```

The cross-realm transitions are not free transitions. They are licensed by specific functions:

```text
form wholesome → desire unobscured
    through constructive / nirmāṇa cognition

form afflicted transition
    at rebirth-linking

formless afflicted transition
    at rebirth-linking
```

### Form-Realm Wholesome Citta

```text
SUCCESSORS = 11
    all twelve citta-types
    except formless unobscured-indeterminate
```

```text
PREDECESSORS = 9
    all twelve citta-types
    except:
        2 afflicted desire-realm cittas
        1 formless unobscured-indeterminate citta
```

## Doctrinal Determination

VAK 2.68 shows that `samanantara-pratyaya` is not merely chronological adjacency. The twelvefold citta classification functions as a constrained transition-space. A citta-type has a determinate predecessor-set and successor-set, and exceptional cross-realm transitions require a specified doctrinal mechanism.

The important distinction is therefore:

```text
mere sequence:
    A happens before B

samanantara-pratyaya:
    A is an admissible immediately antecedent condition for B
```

The Bhāṣya supplies the reasons licensing some exceptional transitions. `Nirmāṇa-citta` explains a cross-realm constructive transition; `pratisaṃdhi` explains otherwise exceptional afflicted transitions at rebirth.

## Feature Grammar Reconstruction

The passage can be represented provisionally as a typed production system:

```text
Citta[
    realm,
    ethicalStatus,
    obscurationStatus,
    pathStatus,
    functionalContext
]
```

with transition productions of the form:

```text
Citta[A] -> Citta[B]
    iff transition(A,B) is licensed
```

and context-sensitive constraints such as:

```text
functionalContext = nirmāṇa
    licenses selected cross-realm transition

functionalContext = pratisaṃdhi
    licenses selected afflicted rebirth transition
```

Thus the numerical lists in the Kārikā are compressed grammar productions rather than bare enumerations.

## Organon Interpretation

In the Organon reconstruction, this gives us a useful distinction between a Feature and a Production:

```text
Feature Structure
    determines what kind of citta this is

Production Rule
    determines what kind of citta may arise next

Context Constraint
    determines when an otherwise exceptional transition is licensed
```

This is especially valuable for a future Organon Dataset because the Bhāṣya does not merely provide labels. It supplies rational explanations for transition permissions and exclusions.

The philosophical gain is therefore not that the Kośa secretly contains a modern NLP grammar, but that its own doctrinal structure is naturally representable as a typed, constrained transition grammar without loss of the underlying Abhidharma distinctions.

## New Technical Terms

- **nirmāṇa-citta** — constructive or magically productive cognition; here the specific context permitting a form-realm wholesome citta to be immediately followed by desire-realm unobscured-indeterminate citta.
  - **status:** rare / not prominent in the Kārikā analysis so far
  - **function:** explains an exceptional cross-realm transition

- **pratisaṃdhi** — rebirth-linking; the transition at the beginning of a new existence.
  - **status:** previously encountered doctrinally, but important here as a transition constraint
  - **function:** licenses specified afflicted cross-realm successor relations

- **samanantaram utpadyate** — arises immediately after.
  - **status:** central in the present pratyaya section
  - **function:** expresses admissible immediately antecedent conditioning rather than mere chronology

## Translation Consequence

The verse's numerical compression should not be translated as though it were an arbitrary mnemonic table. The Bhāṣya shows that the numbers summarize a structured transition grammar whose permissions depend on realm, status, and sometimes special functional context.

## Method Note

Kārikā = compressed transition counts.
Bhāṣya = explanation of the permitted and excluded transitions.
Organon comment = provisional Feature Grammar reconstruction, explicitly secondary to the Abhidharma account.
