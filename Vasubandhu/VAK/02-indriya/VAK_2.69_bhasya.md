# VAK_2.69_bhasya — Form-Realm Completion and Formless-Realm Transition Rule

## Kārikā

```text
aṣṭābhyo nivṛtaṃ tasmāt ṣaṭ tribhyo 'nivṛtaṃ punaḥ /
tasmāt ṣaṭ evam ārūpye tasya nītiḥ śubhāt punaḥ // VAkK_2.69 //
```

## Working Translation

```text
The obscured [form-realm citta] arises from eight; from it, six [cittas follow].
The unobscured, again, arises from three; from it, six.
Thus also in the formless realm is its rule; again, from the wholesome ...
```

The final phrase `śubhāt punaḥ` is intentionally incomplete within this verse. Its count is supplied by VAK 2.70: `nava cittāni`.

## Bhāṣya — Continuous Translation

**Voice: Vasubandhu**

The obscured-indeterminate citta belonging to the Form Realm arises from eight [cittas], excluding the two afflicted cittas of the Desire Realm and the trainee and beyond-training cittas.

From that obscured-indeterminate Form-Realm citta, six [cittas] arise immediately afterward: the three belonging to its own realm, together with [appropriate cittas of] the Desire Realm, excluding the unobscured-indeterminate [where the transition is not licensed in the stated profile].

The unobscured-indeterminate citta belonging to the Form Realm arises from only three cittas, namely the three belonging to its own realm.

From that unobscured-indeterminate Form-Realm citta, six cittas arise: the three belonging to its own realm, afflicted citta in the Desire Realm, and [the relevant] Formless-Realm citta.

As the rule for unobscured-indeterminate citta has been stated in the Form Realm, so is its rule in the Formless Realm.

Thus the unobscured-indeterminate citta belonging to the Formless Realm also arises only from the three cittas belonging to its own realm; and from it likewise six cittas arise: the three of its own realm and the afflicted cittas belonging to the lower realms.

Again, from the wholesome [Formless-Realm citta] ...

The sentence continues in VAK 2.70, where the successor count is stated.

## Doctrinal Determination

VAK 2.69 completes the Form-Realm obscured/unobscured transition profiles and then explicitly **reuses the same rule-schema in the Formless Realm**.

The significant term is `nīti` — rule, procedure, governing pattern. The text is not merely reporting isolated counts. It states that a previously established transition-pattern can be carried over to a new realm when the relevant feature-structure is preserved.

```text
Rūpadhātu.anivṛtāvyākṛta
    predecessor profile = 3 own-realm cittas
    successor profile = 6 licensed cittas

Ārūpyadhātu.anivṛtāvyākṛta
    inherits the same rule-form
    with realm-relative substitutions
```

This is a genuine rule-schema rather than a flat table.

## Logical Determination

The transition system has now acquired three layers:

```text
1. Feature type
   realm + ethical/obscuration/path status

2. Production rule
   which successor cittas are licensed

3. Rule inheritance
   a transition-pattern established in one realm
   can be reapplied in another under corresponding features
```

That is exactly what a Feature Grammar would call a reusable production schema.

The text's `evam ārūpye tasya nītiḥ` is especially important:

```text
"thus, in the Formless Realm, its rule [is the same]"
```

The Kośa therefore does not merely enumerate states. It abstracts a **rule of generation** from one typed domain and applies it to another.

## Translation Consequences

- `nivṛta` should continue to be read as **obscured-indeterminate**, not simply "bad" or "afflicted," because its role is a precise citta-status within the transition matrix.
- `anivṛta` is **unobscured-indeterminate**, again a technical transition-type rather than ordinary neutrality.
- `nīti` deserves stronger attention than a loose "method." Here it means a governing transition-rule or procedure.
- `samanantara` remains implicit in the entire section: these are admissible immediate-successor relations, not remote causal possibilities.

## New Technical Terms

- **nīti** — governing rule, procedure, transition-pattern  
  **status:** rare / newly important in this passage  
  **function:** abstracts a rule from the Form-Realm transition profile and reapplies it to the Formless Realm.

- **svabhūmika** — belonging to its own level/realm  
  **status:** previously encountered in realm-sensitive causal analysis  
  **function:** constrains predecessor and successor cittas to the relevant realm-level unless a specifically licensed cross-realm transition applies.

- **kliṣṭa** — afflicted  
  **status:** previously encountered  
  **function:** marks the cross-realm citta-types that may appear in the successor profile under rebirth or other specifically licensed contexts.

## Organon / Workbook Interpretation

**Comparative reconstruction, not Vasubandhu's terminology.**

VAK 2.69 is one of the clearest places so far where the Kośa behaves like an executable grammar.

```text
FeatureStructure:
    Citta[
        realm,
        obscurationStatus,
        ethicalStatus,
        pathStatus
    ]

ProductionSchema:
    predecessor-set(CittaType)
    successor-set(CittaType)

InheritanceRule:
    if corresponding feature conditions hold,
    reuse transition-schema across realm domains
```

This is directly useful for the Organon Workbook because it suggests that our dataset records should distinguish:

```text
instance facts
rule schemas
exceptions
cross-domain inheritance
source justification
```

The Organon therefore learns how to become the Organon by extracting from the Kośa not just concepts but **ways of organizing rational production itself**.

## Relation to the Dharma Technical Manual

The permanent value of these Kośa sections is now clear. A Dharma Technical Manual needs more than doctrinal definitions. It needs:

```text
state-types
feature constraints
transition rules
exception conditions
path-sensitive transformations
```

VAK 2.69 supplies all five in compressed form.

The Kārikā gives the production skeleton; the Bhāṣya explains the admissibility conditions and realm-relative application. That makes the pair unusually suitable for a browsable, editable Workbook that can later be promoted into formal Organon Dataset features.
