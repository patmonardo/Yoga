# VAK_2.73_bhasya — Acquisition Rules and Closure of the Pratyaya Analysis

## Kārikā

```text
kliṣṭe traidhātuke lābhaḥ ṣaṇṇāṃ ṣaṇṇāṃ dvayoḥ /
śubhe trayāṇāṃ rūpaje śaikṣe caturṇāṃ tasya śeṣite // VAkK_2.73 //
```

## Working Translation

When an afflicted citta of the three realms becomes manifest, there is acquisition of six, six, and two cittas respectively. In a wholesome Form-Realm citta, there is acquisition of three; in a trainee citta, of four. In the remaining cases, acquisition is of that citta itself.

## Bhāṣya — Continuous Translation

**Voice: Vasubandhu**

Of the twelve cittas previously stated, when each kind of citta becomes manifest, how many cittas are newly acquired?

When an afflicted Desire-Realm citta becomes manifest, six cittas are acquired. One acquires the Desire-Realm wholesome citta, either through the restoration of a wholesome root after doubt or through return to that realm; the Desire-Realm unwholesome and obscured-indeterminate cittas, and the afflicted Form-Realm citta, through return to the realm or through falling away; and the afflicted Formless-Realm citta and the trainee citta through falling away.

When an afflicted Form-Realm citta becomes manifest, six cittas are likewise acquired: the three Form-Realm cittas; the Desire-Realm unobscured-indeterminate citta through return to that realm; and the afflicted Formless-Realm citta and trainee citta through falling away.

When an afflicted Formless-Realm citta becomes manifest, however, only two cittas are acquired: that afflicted Formless-Realm citta itself and trainee citta, through falling away.

When a wholesome Form-Realm citta becomes manifest, three cittas are acquired: that same wholesome Form-Realm citta and the unobscured-indeterminate cittas of the Desire and Form Realms.

When trainee citta becomes manifest, four cittas are acquired: trainee citta itself, the unobscured-indeterminate cittas of the Desire and Form Realms, and wholesome Formless-Realm citta. This occurs through the noble path in connection with dispassion from the Desire and Form Realms.

As for the remainder: what is left over is called the remainder. Wherever acquisition has not been specifically explained for a citta, one should understand that there is acquisition of that citta itself and not of another.

**Voice: other teachers**

Others state the matter without making these distinctions:

> In an afflicted citta, the wise say that nine are acquired; in a wholesome citta, six; in an indeterminate citta, only that citta itself.

**Voice: Vasubandhu**

But in the case of wholesome citta, one should say seven rather than six. Desire-Realm wholesome citta is acquired through restoration of the wholesome roots by right view; the unobscured-indeterminate cittas of the Desire and Form Realms are acquired through dispassion; the wholesome cittas of the Form and Formless Realms through acquisition of the corresponding concentrations; and trainee and beyond-training cittas through entry into the fixed course and attainment of arhatship. The remainder is to be determined from the explanations already given.

A summary verse states:

> Through rebirth, meditative attainment, dispassion, falling away, and restoration of wholesome roots, citta is acquired by one who did not previously possess it.

Thus ends the discussion occasioned by the conditions (*pratyaya*).

Thus ends the second Kośa chapter, called the Exposition of the Faculties (*Indriyanirdeśa*), in the *Abhidharmakośabhāṣya*.

## New Technical Terms

- **lābha** — acquisition / obtaining of a citta not previously possessed.
  - **status:** related to earlier `prāpti`, but here used as the operative acquisition relation in the citta matrix.
  - **function:** state-update relation: manifestation of one citta may coincide with newly obtaining one or more other citta-types.
- **dhātu-pratyāgamana** — return to a realm.
  - **status:** Bhāṣya-level transition context.
  - **function:** explains acquisition of realm-specific cittas when returning to a lower realm.
- **parihāṇi** — falling away / loss from an attainment.
  - **status:** previously doctrinally familiar; functionally explicit here.
  - **function:** transition condition under which afflicted or trainee cittas may be reacquired.
- **kuśalamūla-pratisaṃdhāna** — restoration/reconnection of wholesome roots.
  - **status:** Bhāṣya-specific acquisition context here.
  - **function:** explains renewed acquisition of Desire-Realm wholesome citta.
- **vairāgya** — dispassion.
  - **status:** major path term; used here as an acquisition event.
  - **function:** causes acquisition of certain unobscured-indeterminate cittas as the practitioner becomes detached from a realm.
- **niyāmāvakrānti** — entry into the fixed course / certainty of the noble path.
  - **status:** path technical term.
  - **function:** acquisition condition for trainee citta.
- **arhattva** — arhatship.
  - **status:** established path term.
  - **function:** acquisition condition for beyond-training citta.

## Translation Consequences

1. `lābha` here is not merely possession in a static sense. The Bhāṣya asks which cittas become newly obtained when a given citta is manifest, so the term functions dynamically.
2. The acquisition counts depend on transition context: return to a realm, falling away, dispassion, meditative attainment, restoration of wholesome roots, entry into the noble path, and arhatship.
3. `tasya śeṣite` establishes a default rule: where no special cross-acquisition has been specified, manifestation entails acquisition only of that citta itself.
4. The alternative teachers' compressed rule is explicitly corrected by Vasubandhu in the wholesome case; the Bhāṣya therefore preserves not only a rule but a competing compression and its correction.

## Logical Determination

VAK 2.73 adds an **acquisition/update relation** to the transition grammar developed in 2.66–2.72.

```text
CittaState:
    possessedTypes
    manifestType
    realm
    pathStatus
    attainmentStatus

AcquisitionEvent:
    triggerContext
    newlyAcquiredTypes
```

The relevant trigger contexts are:

```text
upapatti          rebirth / realm-entry
samāpatti         meditative attainment
vairāgya          dispassion
parihāṇi          falling away
kuśala-pratisaṃdhāna
                  restoration of wholesome roots
niyāmāvakrānti    entry into the noble course
arhattva          attainment of arhatship
```

Thus the citta grammar has two distinct relations:

```text
SuccessorRule:
    Citta[A] -> Citta[B]

AcquisitionRule:
    manifestation(Citta[A], context=X)
        -> acquire {Citta[B], Citta[C], ...}
```

These must not be conflated. A citta may be newly acquired without being the immediate successor currently manifest, and immediate succession does not by itself specify acquisition.

## Organon Interpretation

The chapter closes with something remarkably close to a stateful production system.

```text
Feature Structure
    defines the citta-type

Transition Grammar
    defines what may arise next

Acquisition Grammar
    defines what becomes available/possessed
    under a transition context

Default Rule
    if no exceptional acquisition rule applies,
    acquire only the manifest type
```

For a future Organon Workbook or GraphForm, this suggests that a philosophical Dataset record should be able to distinguish at least:

```text
Node / Type
    what the determination is

Edge / Production
    what may follow from it

Context
    under which condition the rule applies

State Update
    what becomes acquired, lost, or available

Justification
    Bhāṣya reason for the rule
```

That is stronger than a static knowledge graph. The Kośa is supplying a graph whose admissible edges and node-availability change with rationally specified conditions.

## Chapter-Level Closing Determination

Indriyanirdeśa began with the faculties and ends with a rule-governed dynamics of conditioned experience.

```text
Indriya
    capacities / governing powers
        ↓
Citta-Caitta
    structured cognitive events
        ↓
Viprayukta-saṃskāra
    structural operators
        ↓
Lakṣaṇa
    arising, duration, aging, impermanence
        ↓
Hetu-Phala
    productive ground and result
        ↓
Pratyaya
    relational conditions
        ↓
Citta Transition Grammar
    permitted immediate succession
        ↓
Citta Acquisition Grammar
    state change under path and realm conditions
```

The chapter therefore does not end with a mere list of faculties. It ends with a compact technical model of how a conditioned cognitive system is typed, generated, constrained, transformed, and acquired.

For the Organon project this is best treated as a **comparative reconstruction**, not as a claim that Vasubandhu intended a modern formal grammar. But the source genuinely supplies the distinctions needed for such a reconstruction: typed states, transition constraints, contextual exceptions, acquisition rules, defaults, and competing rule-compressions.

## Voice Notes

- **Voice: Vasubandhu** — dominant explanatory voice and correction of the alternative compressed rule.
- **Voice: other teachers** — introduced by `anye punar abhedenāhuḥ`; they give a generalized acquisition-count formula.
- **Voice: summary verse** — mnemonic condensation of the principal acquisition contexts.

## Chapter Closure

```text
// samāptaḥ pratyayaprasaṅgaḥ //

abhidharmakośabhāṣye indriyanirdeśo nāma
dvitīyaṃ kośasthānaṃ samāptam
```

The discussion occasioned by the conditions is complete. The second Kośa chapter, the *Indriyanirdeśa*, is complete.
