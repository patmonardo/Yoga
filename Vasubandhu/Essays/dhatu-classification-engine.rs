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
//! dharmadhātu   = a heterogeneous object-bin, not "mind's color"
//! mano-vijñāna  = the present mental cognition
//!                                  = 18
//! ```
//!
//! `classify` is a projection, not a partition and not a bijection.
//! Many contents share one Sphere and one Domain. If it were injective,
//! avijñapti could not be rūpa and dharmāyatana at once.
//!
//! ORGANON, fenced, not a translation: Skandha is the gathered answer,
//! Āyatana is the capacity/field Sphere (Essence, not Concept), and only
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

// 2. Spheres. Twelve, not eighteen. Six cognitions share mana-āyatana.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Sphere {
    Faculty(Sense),
    Field(Sense),
    Mind,
    Dharma,
}

fn twelve_spheres() -> impl Iterator<Item = Sphere> {
    SENSES
        .into_iter()
        .map(Sphere::Faculty)
        .chain(SENSES.into_iter().map(Sphere::Field))
        .chain([Sphere::Mind, Sphere::Dharma])
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

/// Content is kept. The cross-map has to survive the projection.
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Classified {
    content: Content,
    gathered: Option<Gathered>,
    sphere: Sphere,
    position: Position,
}

fn classify(content: Content) -> Classified {
    use Content::*;
    match content {
        Faculty(s) => Classified {
            content,
            gathered: Some(Gathered::Rupa),
            sphere: Sphere::Faculty(s),
            position: Position::Sense {
                channel: s,
                role: SenseRole::Support,
            },
        },
        Field(s) => Classified {
            content,
            gathered: Some(Gathered::Rupa),
            sphere: Sphere::Field(s),
            position: Position::Sense {
                channel: s,
                role: SenseRole::Object,
            },
        },
        // Rūpa that is not a sense-field.
        Avijnapti => Classified {
            content,
            gathered: Some(Gathered::Rupa),
            sphere: Sphere::Dharma,
            position: Position::DharmaDhatu,
        },
        Feeling => mental_object(content, Gathered::Vedana),
        Recognition => mental_object(content, Gathered::Samjna),
        Formation => mental_object(content, Gathered::Samskara),
        Cognition(c) => Classified {
            content,
            gathered: Some(Gathered::Vijnana),
            // Six vijñānas, one mana-āyatana. The split returns only as Domain.
            sphere: Sphere::Mind,
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
            sphere: Sphere::Dharma,
            position: Position::DharmaDhatu,
        },
    }
}

fn mental_object(content: Content, gathered: Gathered) -> Classified {
    Classified {
        content,
        gathered: Some(gathered),
        sphere: Sphere::Dharma,
        position: Position::DharmaDhatu,
    }
}

// Feeling, recognition, formations, avijñapti, and the unconditioned share
// DharmaDhatu. They do not share Gathered. That shared slot plus unshared
// kind is the algebra a 5/12/18 mnemonic cannot say.

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
    assert_eq!(visible.sphere, Sphere::Field(Sense::Eye));
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
    assert_eq!(seeing.sphere, Sphere::Mind);
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
    assert_eq!(twelve_spheres().count(), 12);
}

// 6. Architectural wager.
//
// Skandha asks: under what gathered kind is this content considered?
// Āyatana asks: in what capacity/field sphere is it available?
// Dhātu asks: which position does it occupy — and, for manas, in which role?
//
// Overlap is the datum. Avijñapti stays rūpa while sitting in dharmāyatana
// and dharmadhātu. The unconditioned sits in those same two and in no skandha.
// Six cognitions are one skandha and one Sphere, then six cognition-domains.
//
// If a source distinction defeats this, revise the types. Do not restore
// a flat 5/12/18 mnemonic and call it a movement.

#[cfg(test)]
mod checks {
    use super::*;

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
