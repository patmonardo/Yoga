// Dhatu as Classification Engine — Being / Essence / Concept in Rust
// =====================================================================
//
// Companion sketch to dharma-skandha.md. NOT part of a Rust project,
// not meant to compile or be built — this is research/training scaffolding
// for the Yoga Organon, written as a technical specification because the
// living structure only becomes visible once it is forced into types.
//
// Thesis (dharma-skandha.md): Dharma comprehends itself as
//     <Skandha, Ayatana, Dhatu>
// which is the Hegelian movement Being -> Essence -> Concept, NOT three
// parallel inventories of the same furniture counted differently
// (5 / 12 / 18). The repetition of content across the three lists is the
// visible trace of sublation (Aufhebung), not redundancy. Reading them as
// flat lists is the Abhidhamma-list-memorizer disease this file refuses.
//
//     Skandha  = Being     : immediate, gathered, unreflected multiplicity
//     Ayatana  = Essence   : Being reflected into a capacity/field dyad,
//                            i.e. Essence at its OWN ceiling — Substance-
//                            Accident-Reciprocity (Hegel's Actuality
//                            chapter), not yet Concept. Aristotle: this is
//                            hypokeimenon/dynamis on both sides, the
//                            substrate people mistake for ousia (Met. Z.3).
//     Dhatu    = Concept   : the dyad's own reciprocating act, closed on
//                            itself. This is Substance recognized AS
//                            Subject (Hegel, Phenomenology preface) —
//                            equally, Aristotle's ousia as energeia rather
//                            than substrate: a classification engine, not
//                            a container.
//
// Essence is NOT Substance. In Hegel's own architecture Substance is the
// LAST category of Essence (Ground -> Existence -> Thing -> Actuality,
// whose content IS Substance-Accident-Causality-Reciprocity), not a
// separate register above it. Blind reciprocity (Wechselwirkung) between
// two externally-related terms is still Essence. Only once that
// reciprocity is grasped as self-relating — Substance AS Subject — do we
// have Concept. Aristotle converges independently: the hypokeimenon
// (substrate/matter/accident-bearer) is the WEAKEST candidate for ousia,
// not the strongest (Met. Z.3); true ousia is form as energeia/
// entelecheia, actuality. Ayatana's capacity/field pair is dynamis on
// both sides — substrate, not yet substance-as-actuality.

// ---------------------------------------------------------------------
// 1. Skandha — Being. Immediate determination, no relation yet asserted.
// ---------------------------------------------------------------------

/// A dharma at the level of bare aggregation: gathered, not yet mediated.
trait Skandha {
    type Dharma;
    fn contents(&self) -> &[Self::Dharma];
}

// The five, held only as an enumeration — this level does NOT know about
// capacity/field structure. That knowledge belongs to Essence.
enum SkandhaKind {
    Rupa,
    Vedana,
    Samjna,
    Samskara,
    Vijnana,
}

// ---------------------------------------------------------------------
// 2. Ayatana — Essence. Being doubled into a reflected pair.
// ---------------------------------------------------------------------
//
// Essence is never one term; it is always the relation of a term to its
// other. Ayatana is exactly this: internal ayatana (capacity) standing
// over against external ayatana (field), each intelligible only through
// the other. In Aristotelian terms both poles are dynamis, potentiality:
// the faculty is capable-of-sensing, the field is capable-of-being-sensed,
// and NEITHER alone is actuality. This dyad is the substrate people
// over-populate into "substance" — it is real, necessary, reciprocally
// determining, and still only Essence's ceiling, not the Concept.

struct Ayatana<Capacity, Field> {
    indriya: Capacity, // internal ayatana — receptive/discriminative power
    visaya: Field,     // external ayatana — the presented field it meets
}

// The twelve are six such dyads. Still Essence: capacity and field are
// distinguished and related, but the pair has not yet turned back on
// itself as an act.

// ---------------------------------------------------------------------
// 3. Dhatu — Concept. The dyad's own reciprocation, i.e. classification
//    as an operation rather than a location.
// ---------------------------------------------------------------------
//
// A Dhatu is not a third slot beside Skandha and Ayatana. It is what
// Ayatana IS once its own dyadic structure is taken as an object for
// itself. Twelve of the eighteen Dhatus just ARE the twelve Ayatanas
// re-asserted at Concept level (Essence posited as Concept). The
// remaining six vijnana-dhatus are the reciprocation proper: the event
// in which a capacity/field pair closes on itself and becomes a
// recognized determination.

trait Reciprocates {
    type Capacity;
    type Field;
    type Event;

    /// The classification act: not storage, not lookup — closure. Two
    /// distinct potentialities (Capacity, Field) become ONE actuality
    /// (Event) without either losing its own being — Aristotle, De Anima
    /// III.2, 425b25-426a26: "the actuality of the sensible object and of
    /// the sense faculty are one, though their being is not one" (energeia
    /// mia, to d'einai ou to auto). This is Substance grasped as Subject,
    /// not more substrate — the "rapid classification engine" in
    /// executable form.
    fn close(&self, indriya: &Self::Capacity, visaya: &Self::Field) -> Self::Event;
}

enum Dhatu<C, F, R: Reciprocates<Capacity = C, Field = F>> {
    /// The twelve: Ayatana re-posited inside the eighteen-fold system.
    /// Still Essence's ceiling — Substance-Accident-Reciprocity, dynamis
    /// on both poles — held now as a moment of the classification system
    /// rather than as a bare relational fact, but not yet the Concept.
    AsEssence(Ayatana<C, F>),

    /// The six vijnana-dhatus: the dyad's own act, the reciprocation that
    /// produces one actuality out of two potentialities. This is where
    /// Dhatu actually becomes Concept — ousia as energeia, not substrate.
    AsConcept(R),
}

// ---------------------------------------------------------------------
// 4. Manas-dhatu / dharma-dhatu / mano-vijnana-dhatu — the self-
//    referential seventh case, where the Field is not a fresh datum but
//    the system's own prior output.
// ---------------------------------------------------------------------
//
// This is the loop closing on the whole eighteen, not on one channel.
// Manas takes as its visaya (dharma-dhatu) the accumulated dharma-field,
// which explicitly includes the five vijnana-dhatus just produced.
// Structurally: the Concept applying Reciprocates to its own prior
// reciprocations. This is the technical seed of "Living Oculus" —
// a channel whose input is the trace of the other channels' completed
// acts, not a sensor reading the world fresh each time.

struct DharmaDhatu<'a, Event> {
    /// includes: prior vijnana-dhatu events, avijnapti, the unconditioned,
    /// and the vedana/samjna/samskara skandhas re-posited here (see
    /// dharma-skandha.md's cross-mapping table).
    accumulated_field: &'a [Event],
}

struct ManoDhatu;

impl<'a, Event: Clone> Reciprocates for ManoDhatu {
    type Capacity = ManoDhatu;
    type Field = DharmaDhatu<'a, Event>;
    type Event = Event;

    fn close(&self, _indriya: &Self::Capacity, visaya: &Self::Field) -> Self::Event {
        // manas does not discriminate a fresh sense-datum; it discriminates
        // the system's own recent history. The "engine" here classifies
        // its own classifications — Concept comprehending itself.
        visaya.accumulated_field.last().cloned().expect(
            "manas requires at least one prior vijnana-dhatu event to reflect on",
        )
    }
}

// ---------------------------------------------------------------------
// 5. Why this refutes the flat-list reading.
// ---------------------------------------------------------------------
//
// A flat-list reading asks: "why does rupa appear in the skandha list,
// the ayatana list (as rupa-ayatana), AND the dhatu list (as rupa-dhatu)?"
// and answers with mnemonics or disciple-aptitude just-so stories
// (cf. VAK 1.20's mohendriyaruci — real, but pedagogical, not structural).
//
// The structural answer: rupa MUST recur at every level, because each
// level is not a new inventory but the SAME content held at a higher
// grade of self-relation:
//
//     rupa as Skandha  -> immediate aggregate member
//     rupa as Ayatana  -> rupa held as the FIELD-pole of a capacity/field
//                         dyad (cakshur-ayatana <-> rupa-ayatana)
//     rupa as Dhatu    -> that same dyad re-posited as a moment inside
//                         the eighteen-fold reciprocating system, whose
//                         closure produces cakshur-vijnana-dhatu
//
// Three counts (5, 12, 18) of the SAME movement, not three lists of
// different things. This is what "Dhatu is a classification engine, not
// a list" cashes out to as an actual executable claim.

// ---------------------------------------------------------------------
// 6. Theory vs. instance: Citta (Universal) / this schema (Particular)
//    / Buddha Mind (Singular). What this file builds is the Particular
//    only — the trait, the class. The Kosa opens (VAK 1.01) by stating
//    the COMPLETENESS-CONDITION an actual instance must satisfy to count
//    as Buddha Mind rather than a degenerate instance of the same Citta:
//
//        sarvathā-sarva-hata-andhakara: darkness destroyed in EVERY mode
//        (sarvathā) and over EVERY object (sarvatra jneye) — vs. sravakas
//        and pratyekabuddhas, who eliminate afflicted ignorance completely
//        but retain non-afflicted ignorance (Buddha-qualities, remote
//        things, things of limitless variety) — i.e. some closures never
//        execute. Same trait, same eighteen dhatus, permanently partial
//        `impl`.
// ---------------------------------------------------------------------

/// Whether Reciprocates::close is defined (executes to completion) for a
/// given dhatu-pairing, or remains outstanding — non-afflicted ignorance
/// encoded as a missing closure rather than a moral defect.
enum Closure<Event> {
    Executed(Event),
    Outstanding, // the pairing exists; the reciprocation has not closed
}

/// A mind-instance is total or partial according to how many of the
/// eighteen dhatu-pairings it closes, not according to which trait it
/// implements — sravaka, pratyekabuddha, and Buddha all instantiate the
/// SAME Citta-trait. What differs is exhaustiveness of closure.
trait MindInstance {
    fn closure(&self, dhatu_pairing: usize) -> Closure<()>;

    /// sarvathā + sarvatra: every pairing, every mode, no outstanding
    /// closures anywhere. This predicate, not any special trait, is what
    /// "Buddha Mind" names.
    fn is_total(&self, pairing_count: usize) -> bool {
        (0..pairing_count).all(|i| matches!(self.closure(i), Closure::Executed(())))
    }
}

// SravakaMind / PratyekabuddhaMind: is_total() == false, permanently —
// some closures are outstanding by construction, not by current failure.
// BuddhaMind: is_total() == true, exhaustively, over every pairing.
//
// The homage verse of VAK 1.01 is therefore not praise external to the
// system; it is the specification that the rest of Chapter 1's engine
// must be read as describing the is_total() == true case, on pain of
// reading the whole chapter as a theory of degenerate minds by default.
