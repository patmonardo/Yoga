//! Dharma-wheel index model
//! ========================
//!
//! A research data model for an eventual Index of Dharmas. It does not turn
//! Dharma into a flat taxonomy or claim that the Kośa was written as software.
//! A record remains available under the three irreducible projections:
//! Skandha (gathered kind), Ayatana (Sphere), and Dhatu (Domain).
//!
//! The wheel is the index's operational form: its hub is the governing
//! determination, its spokes are distinct moments, its rim records how those
//! moments close into one traversable operation. Recognition is accountable to
//! both learned resemblance and an explicit rule witness; neither is treated as
//! sufficient by itself.

#![allow(dead_code)] // research sketch: the types define the proposed index

use std::collections::{BTreeMap, BTreeSet};

const MAX_DHARMAS: usize = 80_000;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct DharmaId(u32);

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Skandha {
    Rupa,
    Vedana,
    Samjna,
    Samskara,
    Vijnana,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Ayatana {
    EyeFaculty,
    VisibleField,
    EarFaculty,
    AudibleField,
    NoseFaculty,
    OdorField,
    TongueFaculty,
    TasteField,
    BodyFaculty,
    TangibleField,
    Mind,
    Dharma,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Dhatu {
    Eye,
    VisibleForm,
    EyeConsciousness,
    Ear,
    Sound,
    EarConsciousness,
    Nose,
    Odor,
    NoseConsciousness,
    Tongue,
    Taste,
    TongueConsciousness,
    Body,
    Tangible,
    BodyConsciousness,
    Mind,
    Dharma,
    MentalConsciousness,
}

/// A dharma's three projections. `skandha` is absent for the unconditioned.
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct DharmaLocation {
    skandha: Option<Skandha>,
    ayatana: Ayatana,
    dhatu: Dhatu,
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct DharmaRecord {
    id: DharmaId,
    canonical_name: String,
    definition: String,
    location: DharmaLocation,
    source_refs: Vec<String>,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum RelationKind {
    Conditions,
    Manifests,
    Corrects,
    Realizes,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct DharmaRelation {
    from: DharmaId,
    to: DharmaId,
    kind: RelationKind,
}

/// An explicit, reviewable basis for a classification.
#[derive(Clone, Debug, Eq, PartialEq)]
struct RuleWitness {
    rule: String,
    source_refs: Vec<String>,
}

/// A first-class act of Abhidharma discrimination.
///
/// The discriminator is itself a Dharma record, so this relation may be
/// reflexive: Abhidharma can make its own discriminating form explicit.
#[derive(Clone, Debug, Eq, PartialEq)]
struct Discrimination {
    discriminator: DharmaId,
    discriminated: DharmaId,
    witness: RuleWitness,
}

/// A learned recognizer may rank candidates, but it does not silently decide.
#[derive(Clone, Copy, Debug, PartialEq)]
struct LearnedMatch {
    candidate: DharmaId,
    similarity: f32,
}

#[derive(Clone, Debug, PartialEq)]
struct Recognition {
    learned: LearnedMatch,
    rule_witness: RuleWitness,
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct DharmaWheel {
    hub: DharmaId,
    spokes: Vec<DharmaId>,
    rim: Vec<DharmaRelation>,
}

#[derive(Clone, Debug, Eq, PartialEq)]
enum IndexError {
    DuplicateId(DharmaId),
    CapacityReached,
    UnknownDharma(DharmaId),
    EmptyCanonicalName,
    MissingRuleWitness,
    InvalidWheelHub,
    InvalidWheelSpoke(DharmaId),
    InvalidRimRelation(DharmaRelation),
}

#[derive(Default)]
struct DharmaIndex {
    records: BTreeMap<DharmaId, DharmaRecord>,
    relations: Vec<DharmaRelation>,
    discriminations: Vec<Discrimination>,
}

impl DharmaIndex {
    fn insert(&mut self, record: DharmaRecord) -> Result<(), IndexError> {
        if record.canonical_name.trim().is_empty() {
            return Err(IndexError::EmptyCanonicalName);
        }
        if self.records.contains_key(&record.id) {
            return Err(IndexError::DuplicateId(record.id));
        }
        if self.records.len() == MAX_DHARMAS {
            return Err(IndexError::CapacityReached);
        }
        self.records.insert(record.id, record);
        Ok(())
    }

    fn relate(&mut self, relation: DharmaRelation) -> Result<(), IndexError> {
        self.require_known(relation.from)?;
        self.require_known(relation.to)?;
        self.relations.push(relation);
        Ok(())
    }

    fn discriminate(&mut self, discrimination: Discrimination) -> Result<(), IndexError> {
        self.require_known(discrimination.discriminator)?;
        self.require_known(discrimination.discriminated)?;
        if discrimination.witness.rule.trim().is_empty() {
            return Err(IndexError::MissingRuleWitness);
        }
        self.discriminations.push(discrimination);
        Ok(())
    }

    fn recognize(&self, recognition: Recognition) -> Result<&DharmaRecord, IndexError> {
        // The score ranks candidates; the named rule keeps the outcome inspectable.
        if recognition.rule_witness.rule.trim().is_empty() {
            return Err(IndexError::MissingRuleWitness);
        }
        self.require_known(recognition.learned.candidate)
    }

    fn validate_wheel(&self, wheel: &DharmaWheel) -> Result<(), IndexError> {
        if !self.records.contains_key(&wheel.hub) {
            return Err(IndexError::InvalidWheelHub);
        }

        let spoke_set: BTreeSet<_> = wheel.spokes.iter().copied().collect();
        for spoke in &spoke_set {
            if *spoke == wheel.hub || !self.records.contains_key(spoke) {
                return Err(IndexError::InvalidWheelSpoke(*spoke));
            }
        }

        for relation in &wheel.rim {
            if !spoke_set.contains(&relation.from) || !spoke_set.contains(&relation.to) {
                return Err(IndexError::InvalidRimRelation(*relation));
            }
        }
        Ok(())
    }

    fn require_known(&self, id: DharmaId) -> Result<&DharmaRecord, IndexError> {
        self.records.get(&id).ok_or(IndexError::UnknownDharma(id))
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn record(id: u32, name: &str, location: DharmaLocation) -> DharmaRecord {
        DharmaRecord {
            id: DharmaId(id),
            canonical_name: name.into(),
            definition: "A determinate Dharma record.".into(),
            location,
            source_refs: vec!["VAK 1.14-1.17".into()],
        }
    }

    #[test]
    fn recognition_returns_a_triangularly_located_record() {
        let feeling = record(
            1,
            "feeling",
            DharmaLocation {
                skandha: Some(Skandha::Vedana),
                ayatana: Ayatana::Dharma,
                dhatu: Dhatu::Dharma,
            },
        );
        let mut index = DharmaIndex::default();
        index.insert(feeling).unwrap();

        let recognized = index
            .recognize(Recognition {
                learned: LearnedMatch {
                    candidate: DharmaId(1),
                    similarity: 0.94,
                },
                rule_witness: RuleWitness {
                    rule: "Affect is considered under feeling and is a Dharma object.".into(),
                    source_refs: vec!["VAK 1.14-1.17".into()],
                },
            })
            .unwrap();

        assert_eq!(recognized.location.skandha, Some(Skandha::Vedana));
        assert_eq!(recognized.location.ayatana, Ayatana::Dharma);
        assert_eq!(recognized.location.dhatu, Dhatu::Dharma);
    }

    #[test]
    fn wheel_requires_known_spokes_and_a_closed_rim() {
        let location = DharmaLocation {
            skandha: Some(Skandha::Samskara),
            ayatana: Ayatana::Dharma,
            dhatu: Dhatu::Dharma,
        };
        let mut index = DharmaIndex::default();
        index.insert(record(1, "path", location)).unwrap();
        index.insert(record(2, "right-view", location)).unwrap();
        index.insert(record(3, "right-intention", location)).unwrap();

        let wheel = DharmaWheel {
            hub: DharmaId(1),
            spokes: vec![DharmaId(2), DharmaId(3)],
            rim: vec![DharmaRelation {
                from: DharmaId(2),
                to: DharmaId(3),
                kind: RelationKind::Conditions,
            }],
        };

        assert_eq!(index.validate_wheel(&wheel), Ok(()));
    }

    #[test]
    fn wheel_rejects_rim_relations_outside_its_spokes() {
        let location = DharmaLocation {
            skandha: Some(Skandha::Samskara),
            ayatana: Ayatana::Dharma,
            dhatu: Dhatu::Dharma,
        };
        let mut index = DharmaIndex::default();
        index.insert(record(1, "path", location)).unwrap();
        index.insert(record(2, "right-view", location)).unwrap();
        index.insert(record(3, "outside", location)).unwrap();

        let wheel = DharmaWheel {
            hub: DharmaId(1),
            spokes: vec![DharmaId(2)],
            rim: vec![DharmaRelation {
                from: DharmaId(2),
                to: DharmaId(3),
                kind: RelationKind::Conditions,
            }],
        };

        assert_eq!(
            index.validate_wheel(&wheel),
            Err(IndexError::InvalidRimRelation(DharmaRelation {
                from: DharmaId(2),
                to: DharmaId(3),
                kind: RelationKind::Conditions,
            }))
        );
    }

    #[test]
    fn discriminator_is_indexed_and_can_discriminate_itself() {
        let abhidharma = record(
            1,
            "abhidharma",
            DharmaLocation {
                skandha: Some(Skandha::Samskara),
                ayatana: Ayatana::Dharma,
                dhatu: Dhatu::Dharma,
            },
        );
        let mut index = DharmaIndex::default();
        index.insert(abhidharma).unwrap();

        let discrimination = Discrimination {
            discriminator: DharmaId(1),
            discriminated: DharmaId(1),
            witness: RuleWitness {
                rule: "Sarvadharma includes the discriminating Dharma itself.".into(),
                source_refs: vec!["Organon reading; not a literal Kośa translation.".into()],
            },
        };
        assert_eq!(index.discriminate(discrimination.clone()), Ok(()));
        assert_eq!(index.discriminations, vec![discrimination]);
    }
}
