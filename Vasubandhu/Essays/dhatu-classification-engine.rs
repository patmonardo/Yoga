//! Dhātu as a classification engine
//! =================================
//!
//! Research Rust for `dharma-skandha.md`. A readable model, not a crate,
//! and not a claim that the Kośa was written as a program.
//!
//! Replaces the earlier sketch that generated eighteen domains as
//! `6 × (support, object, cognition)`. That product is true for the five
//! senses. It is false for the sixth, and it made the cross-map invisible.
//!
//! SOURCE RULE (VAK 1.14–1.17): five skandhas, twelve āyatanas, and
//! eighteen dhātus classify overlapping content under different relations.
//! The fifteen sensory positions are a real product. The last three are not
//! another row of that product:
//!
//! ```text
//! 5 × (support, object, cognition) = 15
//! manodhātu     = a past cognition in the support role, not a sixth organ
//! dharmadhātu   = three conceptual skandhas + avijñapti + unconditioned
//! mano-vijñāna  = the present mental cognition
//!                                  = 18
//! ```
//!
//! The Nāma-skandha view groups the four non-Rūpa members of `Gathered` as
//! Jñāna-skandha : Vijñāna-skandha. Jñāna-skandha is the ordinary-knowledge
//! overlay on Vedanā, Saṃjñā, and Saṃskāra; Vijñāna remains the separate,
//! special Cognition member. The Dharma-dhātu keeps its source paths visible.
//!
//! The project-level Form root is fivefold. VAK 1.09 elaborates the Form
//! Base as five faculties, five fields, and avijñapti; VAK 1.16 excludes
//! avijñapti from the ten Rūpa slots while cross-classifying it under Dharma.
//! Do not turn that expanded crosswalk into a tenfold Base.
//!
//! A top-level Dharma view may wrap Dharma-āyatana and Dharma-dhātu together,
//! but the core matrix retains separate Essence and Principle slots.
//!
//! `classify` is a projection, not a partition and not a bijection.
//! Many contents share one Essence and one Domain. If it were injective,
//! avijñapti could not be rūpa and dharmāyatana at once.
//!
//! ORGANON, fenced, not a translation: Skandha is the gathered answer,
//! Āyatana is the capacity/field Essence (not Concept), and only
//! the support–object–cognition closure is Concept-grade. `Position` is
//! not "the Concept enum." The Concept is the closure, not the list.

#![allow(dead_code)] // research sketch: the functions are the text

// 1. Positions. The sixth row cannot be built by the product that builds
// the fifteen.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Sense {
    Eye,
    Ear,
    Nose,
    Tongue,
    Touch,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum SenseRole {
    Support,
    Object,
    Cognition,
}

/// Eighteen slots. Not eighteen substances.
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Position {
    Sense { channel: Sense, role: SenseRole },
    ManoDhatu,
    DharmaDhatu,
    ManoVijnana,
}

const SENSES: [Sense; 5] = [
    Sense::Eye,
    Sense::Ear,
    Sense::Nose,
    Sense::Tongue,
    Sense::Touch,
];

const SENSE_ROLES: [SenseRole; 3] = [
    SenseRole::Support,
    SenseRole::Object,
    SenseRole::Cognition,
];

fn sensory_positions() -> impl Iterator<Item = Position> {
    SENSES.into_iter().flat_map(|channel| {
        SENSE_ROLES.into_iter().map(move |role| Position::Sense { channel, role })
    })
}

fn eighteen_positions() -> impl Iterator<Item = Position> {
    sensory_positions().chain([
        Position::ManoDhatu,
        Position::DharmaDhatu,
        Position::ManoVijnana,
    ])
}

// 2. Essences. Twelve, not eighteen. Six cognitions share mana-āyatana.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Essence {
    Faculty(Sense),
    Field(Sense),
    Mind,
    Dharma,
}

fn twelve_essences() -> impl Iterator<Item = Essence> {
    SENSES
        .into_iter()
        .map(Essence::Faculty)
        .chain(SENSES.into_iter().map(Essence::Field))
        .chain([Essence::Mind, Essence::Dharma])
}

// 3. Gathered kind. `None` is the unconditioned's datum, not a missing field.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Gathered {
    Rupa,
    Vedana,
    Samjna,
    Samskara,
    Vijnana,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum SkandhaFamily {
    Rupa,
    Nama,
}

fn skandha_family(gathered: Option<Gathered>) -> Option<SkandhaFamily> {
    match gathered {
        Some(Gathered::Rupa) => Some(SkandhaFamily::Rupa),
        Some(Gathered::Vedana | Gathered::Samjna | Gathered::Samskara | Gathered::Vijnana) => {
            Some(SkandhaFamily::Nama)
        }
        None => None,
    }
}

/// A project overlay on the five Skandhas, not another Skandha enumeration.
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum SkandhaView {
    FormEmpirical,
    JnanaSkandha,
    VijnanaSkandha,
}

fn skandha_view(gathered: Option<Gathered>) -> Option<SkandhaView> {
    match gathered {
        Some(Gathered::Rupa) => Some(SkandhaView::FormEmpirical),
        Some(Gathered::Vedana | Gathered::Samjna | Gathered::Samskara) => {
            Some(SkandhaView::JnanaSkandha)
        }
        Some(Gathered::Vijnana) => Some(SkandhaView::VijnanaSkandha),
        None => None,
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Channel {
    Sense(Sense),
    Mind,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Cognition {
    channel: Channel,
    occurrence: u64,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Content {
    Faculty(Sense),
    Field(Sense),
    Avijnapti,
    Feeling,
    Recognition,
    Formation,
    Cognition(Cognition),
    Unconditioned,
}

/// Distinct routes into the Dharma column of the matrix.
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum DharmaColumnPath {
    JnanaSkandha(Gathered),
    AvijnaptiFromRupa,
    Unconditioned,
}

fn dharma_column_path(content: Content) -> Option<DharmaColumnPath> {
    match content {
        Content::Feeling => Some(DharmaColumnPath::JnanaSkandha(Gathered::Vedana)),
        Content::Recognition => Some(DharmaColumnPath::JnanaSkandha(Gathered::Samjna)),
        Content::Formation => Some(DharmaColumnPath::JnanaSkandha(Gathered::Samskara)),
        Content::Avijnapti => Some(DharmaColumnPath::AvijnaptiFromRupa),
        Content::Unconditioned => Some(DharmaColumnPath::Unconditioned),
        Content::Faculty(_) | Content::Field(_) | Content::Cognition(_) => None,
    }
}

/// Content is kept. The cross-map has to survive the projection.
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Classified {
    content: Content,
    gathered: Option<Gathered>,
    essence: Essence,
    position: Position,
}

fn classify(content: Content) -> Classified {
    use Content::*;
    match content {
        Faculty(s) => Classified {
            content,
            gathered: Some(Gathered::Rupa),
            essence: Essence::Faculty(s),
            position: Position::Sense {
                channel: s,
                role: SenseRole::Support,
            },
        },
        Field(s) => Classified {
            content,
            gathered: Some(Gathered::Rupa),
            essence: Essence::Field(s),
            position: Position::Sense {
                channel: s,
                role: SenseRole::Object,
            },
        },
        // Rūpa that is not an Essence.
        Avijnapti => Classified {
            content,
            gathered: Some(Gathered::Rupa),
            essence: Essence::Dharma,
            position: Position::DharmaDhatu,
        },
        Feeling => mental_object(content, Gathered::Vedana),
        Recognition => mental_object(content, Gathered::Samjna),
        Formation => mental_object(content, Gathered::Samskara),
        Cognition(c) => Classified {
            content,
            gathered: Some(Gathered::Vijnana),
            // Six vijñānas, one mana-āyatana. The split returns only as Domain.
            essence: Essence::Mind,
            position: match c.channel {
                Channel::Sense(s) => Position::Sense {
                    channel: s,
                    role: SenseRole::Cognition,
                },
                Channel::Mind => Position::ManoVijnana,
            },
        },
        Unconditioned => Classified {
            content,
            gathered: None,
            essence: Essence::Dharma,
            position: Position::DharmaDhatu,
        },
    }
}

fn mental_object(content: Content, gathered: Gathered) -> Classified {
    Classified {
        content,
        gathered: Some(gathered),
        essence: Essence::Dharma,
        position: Position::DharmaDhatu,
    }
}

// Feeling, recognition, formations, avijñapti, and the unconditioned share
// DharmaDhatu through distinct paths. The shared slot does not erase their
// different Base origins or the unconditioned's lack of a Skandha.

// 4. Encounter. Precedence is a witness, not a bool.
//
// VAK 1.17: manodhātu is the citta immediately past, functioning as support.
// An arhat's final citta remains manas though no successor arises — another
// cause can be absent. Do not fabricate that successor, and do not require
// `last().unwrap()`.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum ManasStatus {
    /// This citta immediately precedes a present cognition.
    Precedes { next: u64 },
    /// No further cause. Still manas. Not a made-up next event.
    NoFurtherCause,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Support {
    Faculty(Sense),
    PastCitta { which: Cognition, status: ManasStatus },
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Presented {
    Field(Sense),
    Dharma,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Encounter {
    support: Support,
    object: Presented,
    cognition: Cognition,
    positions: [Position; 3],
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum ClassError {
    NeedFaculty,
    NeedField,
    BrokenPair,
    ManasIsARole,
    NeedDharmaObject,
}

fn encounter(
    support: Support,
    object: Presented,
    cognition: Cognition,
) -> Result<Encounter, ClassError> {
    let positions = match cognition.channel {
        Channel::Sense(s) => {
            let Support::Faculty(faculty) = support else {
                return Err(ClassError::NeedFaculty);
            };
            let Presented::Field(field) = object else {
                return Err(ClassError::NeedField);
            };
            if faculty != s || field != s {
                return Err(ClassError::BrokenPair);
            }
            [
                Position::Sense {
                    channel: s,
                    role: SenseRole::Support,
                },
                Position::Sense {
                    channel: s,
                    role: SenseRole::Object,
                },
                Position::Sense {
                    channel: s,
                    role: SenseRole::Cognition,
                },
            ]
        }
        Channel::Mind => {
            let Support::PastCitta { .. } = support else {
                return Err(ClassError::ManasIsARole);
            };
            if object != Presented::Dharma {
                return Err(ClassError::NeedDharmaObject);
            }
            [
                Position::ManoDhatu,
                Position::DharmaDhatu,
                Position::ManoVijnana,
            ]
        }
    };
    Ok(Encounter {
        support,
        object,
        cognition,
        positions,
    })
}

/// Role-change. The same citta was a cognition; it is now support.
/// It does not become the object, and it does not fill dharmadhātu.
fn as_manas(previous: Cognition, status: ManasStatus) -> Support {
    Support::PastCitta {
        which: previous,
        status,
    }
}

fn eye_example() -> Result<Encounter, ClassError> {
    let visible = classify(Content::Field(Sense::Eye));
    assert_eq!(visible.gathered, Some(Gathered::Rupa));
    assert_eq!(visible.essence, Essence::Field(Sense::Eye));
    assert_eq!(
        visible.position,
        Position::Sense {
            channel: Sense::Eye,
            role: SenseRole::Object,
        }
    );

    let seeing = Cognition {
        channel: Channel::Sense(Sense::Eye),
        occurrence: 42,
    };
    let met = encounter(
        Support::Faculty(Sense::Eye),
        Presented::Field(Sense::Eye),
        seeing,
    )?;
    assert_eq!(
        met.positions,
        [
            Position::Sense {
                channel: Sense::Eye,
                role: SenseRole::Support,
            },
            Position::Sense {
                channel: Sense::Eye,
                role: SenseRole::Object,
            },
            Position::Sense {
                channel: Sense::Eye,
                role: SenseRole::Cognition,
            },
        ]
    );
    Ok(met)
}

fn cross_map_example() {
    let avijnapti = classify(Content::Avijnapti);
    let unconditioned = classify(Content::Unconditioned);
    let feeling = classify(Content::Feeling);

    assert_eq!(avijnapti.position, Position::DharmaDhatu);
    assert_eq!(unconditioned.position, Position::DharmaDhatu);
    assert_eq!(feeling.position, Position::DharmaDhatu);

    assert_eq!(avijnapti.gathered, Some(Gathered::Rupa));
    assert_eq!(unconditioned.gathered, None);
    assert_eq!(feeling.gathered, Some(Gathered::Vedana));

    let seeing = classify(Content::Cognition(Cognition {
        channel: Channel::Sense(Sense::Eye),
        occurrence: 42,
    }));
    assert_eq!(seeing.essence, Essence::Mind);
    assert_eq!(
        seeing.position,
        Position::Sense {
            channel: Sense::Eye,
            role: SenseRole::Cognition,
        }
    );
}

fn mental_example() -> Result<Encounter, ClassError> {
    let earlier = Cognition {
        channel: Channel::Sense(Sense::Eye),
        occurrence: 42,
    };
    let present = Cognition {
        channel: Channel::Mind,
        occurrence: 43,
    };
    // The eye-citta changes role. It is not "recent history," and it is
    // not the dharma-object.
    encounter(
        as_manas(earlier, ManasStatus::Precedes { next: 43 }),
        Presented::Dharma,
        present,
    )
}

fn final_citta_is_still_manas() -> Support {
    let last = Cognition {
        channel: Channel::Mind,
        occurrence: 99,
    };
    as_manas(last, ManasStatus::NoFurtherCause)
}

// Viṣaya names the sensory field's role. Comprehension of vastu is a
// further Organon problem, not a return value of `encounter`.

// 5. Counts are schemas, not ontologies.
//
// VAK 1.01 (sarvathā / sarvatra) is another theorem. Eighteen positions
// are not eighteen knowing-tasks. A finite audit of this file cannot
// establish exhaustive knowing. That conjecture does not live here.
// Station order of the indriyas does not live here either.

fn schema_counts() {
    assert_eq!(sensory_positions().count(), 15);
    assert_eq!(eighteen_positions().count(), 18);
    assert_eq!(twelve_essences().count(), 12);
}

// 6. Architectural wager.
//
// Skandha asks: under what gathered kind is this content considered?
// Āyatana asks: in what capacity/field Essence is it available?
// Dhātu asks: which position does it occupy — and, for manas, in which role?
//
// Overlap is the datum. Avijñapti stays rūpa while sitting in dharmāyatana
// and dharmadhātu. The unconditioned sits in those same two and in no skandha.
// Six cognitions are one skandha and one Essence, then six cognition-domains.
//
// If a source distinction defeats this, revise the types. Do not restore
// a flat 5/12/18 mnemonic and call it a movement.

#[cfg(test)]
mod checks {
    use super::*;

    #[test]
    fn jnana_skandha_view_groups_three_existing_skandhas_only() {
        assert_eq!(
            skandha_view(Some(Gathered::Vedana)),
            Some(SkandhaView::JnanaSkandha)
        );
        assert_eq!(
            skandha_view(Some(Gathered::Samjna)),
            Some(SkandhaView::JnanaSkandha)
        );
        assert_eq!(
            skandha_view(Some(Gathered::Samskara)),
            Some(SkandhaView::JnanaSkandha)
        );
        assert_eq!(
            skandha_view(Some(Gathered::Rupa)),
            Some(SkandhaView::FormEmpirical)
        );
        assert_eq!(
            skandha_view(Some(Gathered::Vijnana)),
            Some(SkandhaView::VijnanaSkandha)
        );
        assert_eq!(skandha_view(None), None);
    }

    #[test]
    fn nama_skandha_view_groups_the_four_non_rupa_skandhas() {
        for skandha in [
            Gathered::Vedana,
            Gathered::Samjna,
            Gathered::Samskara,
            Gathered::Vijnana,
        ] {
            assert_eq!(skandha_family(Some(skandha)), Some(SkandhaFamily::Nama));
        }
        assert_eq!(
            skandha_family(Some(Gathered::Rupa)),
            Some(SkandhaFamily::Rupa)
        );
        assert_eq!(skandha_family(None), None);
    }

    #[test]
    fn dharma_column_keeps_its_distinct_source_paths() {
        assert_eq!(
            dharma_column_path(Content::Feeling),
            Some(DharmaColumnPath::JnanaSkandha(Gathered::Vedana))
        );
        assert_eq!(
            dharma_column_path(Content::Recognition),
            Some(DharmaColumnPath::JnanaSkandha(Gathered::Samjna))
        );
        assert_eq!(
            dharma_column_path(Content::Formation),
            Some(DharmaColumnPath::JnanaSkandha(Gathered::Samskara))
        );
        assert_eq!(
            dharma_column_path(Content::Avijnapti),
            Some(DharmaColumnPath::AvijnaptiFromRupa)
        );
        assert_eq!(
            dharma_column_path(Content::Unconditioned),
            Some(DharmaColumnPath::Unconditioned)
        );
        assert_eq!(
            dharma_column_path(Content::Cognition(Cognition {
                channel: Channel::Mind,
                occurrence: 1,
            })),
            None
        );
    }

    #[test]
    fn the_schema_holds() {
        schema_counts();
        cross_map_example();
        eye_example().unwrap();
        let met = mental_example().unwrap();
        assert_eq!(
            met.positions,
            [
                Position::ManoDhatu,
                Position::DharmaDhatu,
                Position::ManoVijnana,
            ]
        );
        assert!(matches!(
            final_citta_is_still_manas(),
            Support::PastCitta {
                status: ManasStatus::NoFurtherCause,
                ..
            }
        ));
    }
}
