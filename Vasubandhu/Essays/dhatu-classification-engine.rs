//! Dhātu as a classification engine
//! =================================
//!
//! Research Rust for `dharma-skandha.md`. This is a readable model, not a
//! crate or a claim that the Kośa itself was written as a program.
//!
//! SOURCE RULE (VAK 1.14–1.17): five skandhas, twelve āyatanas, and eighteen
//! dhātus classify overlapping content under different relations. The
//! eighteen are six supports (āśraya), six objects (ālambana), and six
//! cognitions (āśrita). Manodhātu names one of the six cognitions when it is
//! immediately past and functions as support for the sixth cognition.
//!
//! ORGANON PROPOSAL: Skandha : Āyatana : Dhātu may be read as gathered
//! content : relational sphere : articulated system. The Hegelian
//! Being–Essence–Concept comparison belongs to this proposal; it is not a
//! translation of Vasubandhu's three Sanskrit terms.
//!
//! A classification is a judgment about a dharma in a specified respect.
//! It is never a new dharma manufactured by a list.

// 1. The three questions asked of one occurrence.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Skandha { Rupa, Vedana, Samjna, Samskara, Vijnana }

// The Kośa's order is Eye → Ear → Nose → Tongue → Touch → Mind (VAK 1.23).
// The proposed Sāṃkhya–Yoga station order below is a separate project
// ordering of indriya channels, not a list of tanmātras.
// `Touch` names a functional channel; its two poles remain distinct:
// kāya is the faculty/support, spraṣṭavya the tangible field/object.
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Sense { Eye, Ear, Nose, Tongue, Touch }

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Channel { Eye, Ear, Nose, Tongue, Touch, Mind }

impl From<Sense> for Channel {
    fn from(sense: Sense) -> Self {
        match sense {
            Sense::Eye => Self::Eye, Sense::Ear => Self::Ear,
            Sense::Nose => Self::Nose, Sense::Tongue => Self::Tongue,
            Sense::Touch => Self::Touch,
        }
    }
}

// Twelve bases: five sensory capacities, five sensory fields, mind, dharma.
// The last two are not another material organ and another material object.
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Ayatana { Faculty(Sense), Field(Sense), Mind, Dharma }

// Eighteen domains: six of each *role*. Cognition(Mind) and Support(Mind)
// may involve the same stream without collapsing into one position.
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Dhatu { Support(Channel), Object(Channel), Cognition(Channel) }

const KOSA_CHANNEL_ORDER: [Channel; 6] = [
    Channel::Eye, Channel::Ear, Channel::Nose,
    Channel::Tongue, Channel::Touch, Channel::Mind,
];

const STATION_SENSE_ORDER: [Sense; 5] = [
    Sense::Ear, Sense::Touch, Sense::Eye, Sense::Tongue, Sense::Nose,
];

fn eighteen_positions() -> impl Iterator<Item = Dhatu> {
    KOSA_CHANNEL_ORDER.into_iter().flat_map(|channel| [
        Dhatu::Support(channel), Dhatu::Object(channel),
        Dhatu::Cognition(channel),
    ])
}

// 6 × (support + object + cognition) = 18 positions, not disjoint substances.

// 2. The cross-map. One content, several answers.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Cognition { channel: Channel, occurrence: u64 }

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Dharma {
    SensoryFaculty(Sense), SensoryField(Sense), Avijnapti,
    Feeling, Recognition, Formation, Cognition(Cognition), Unconditioned,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Classification {
    // The unconditioned belongs to dharmāyatana/dharmadhātu but to no
    // conditioned aggregate. Option therefore has doctrinal force.
    skandha: Option<Skandha>,
    ayatana: Ayatana,
    dhatu: Dhatu,
}

fn classify(dharma: Dharma) -> Classification {
    use Dharma::*;
    match dharma {
        SensoryFaculty(s) => Classification {
            skandha: Some(Skandha::Rupa),
            ayatana: Ayatana::Faculty(s),
            dhatu: Dhatu::Support(s.into()),
        },
        SensoryField(s) => Classification {
            skandha: Some(Skandha::Rupa),
            ayatana: Ayatana::Field(s),
            dhatu: Dhatu::Object(s.into()),
        },
        Avijnapti => Classification {
            skandha: Some(Skandha::Rupa),
            ayatana: Ayatana::Dharma,
            dhatu: Dhatu::Object(Channel::Mind),
        },
        Feeling => mental_object(Skandha::Vedana),
        Recognition => mental_object(Skandha::Samjna),
        Formation => mental_object(Skandha::Samskara),
        Cognition(c) => Classification {
            skandha: Some(Skandha::Vijnana),
            ayatana: Ayatana::Mind,
            dhatu: Dhatu::Cognition(c.channel),
        },
        Unconditioned => Classification {
            skandha: None,
            ayatana: Ayatana::Dharma,
            dhatu: Dhatu::Object(Channel::Mind),
        },
    }
}

fn mental_object(skandha: Skandha) -> Classification {
    Classification {
        skandha: Some(skandha),
        ayatana: Ayatana::Dharma,
        dhatu: Dhatu::Object(Channel::Mind),
    }
}

// classify(Avijnapti) = (Rūpa, dharmāyatana, dharmadhātu).
// classify(Unconditioned) = (no skandha, dharmāyatana, dharmadhātu).
// The same word `dharma` in Dharma and Ayatana::Dharma does not mean
// every dharma is automatically in the dharma-object base.

// 3. A cognitive occurrence has distinct support, object, and cognition.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Support {
    Sensory(Sense),
    // Not a seventh cognition or an accumulated memory bank: VAK 1.17.
    ImmediatelyPast(Cognition),
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Presented { Sensory(Sense), DharmaObject }

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Encounter { support: Support, object: Presented, cognition: Cognition }

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum ClassificationError {
    WrongSensoryPair, WrongCognitionChannel,
    MentalSupportRequired, MentalObjectRequired,
    ImmediatePrecedenceRequired,
}

impl Encounter {
    /// Check the *classification* of a supplied occurrence. Constructing
    /// this value does not pretend to cause perception.
    fn classify(
        support: Support,
        object: Presented,
        cognition: Cognition,
        immediately_precedes: bool,
    ) -> Result<Self, ClassificationError> {
        match cognition.channel {
            Channel::Mind => {
                if !matches!(support, Support::ImmediatelyPast(_)) {
                    return Err(ClassificationError::MentalSupportRequired);
                }
                if object != Presented::DharmaObject {
                    return Err(ClassificationError::MentalObjectRequired);
                }
                if !immediately_precedes {
                    return Err(ClassificationError::ImmediatePrecedenceRequired);
                }
            }
            sensory_channel => {
                let Support::Sensory(support_sense) = support else {
                    return Err(ClassificationError::WrongCognitionChannel);
                };
                let Presented::Sensory(object_sense) = object else {
                    return Err(ClassificationError::WrongSensoryPair);
                };
                if Channel::from(support_sense) != sensory_channel
                    || support_sense != object_sense {
                    return Err(ClassificationError::WrongSensoryPair);
                }
            }
        }
        Ok(Self { support, object, cognition })
    }

    fn dhatu_positions(&self) -> [Dhatu; 3] {
        let channel = self.cognition.channel;
        [Dhatu::Support(channel), Dhatu::Object(channel),
         Dhatu::Cognition(channel)]
    }
}

// A real temporal model would witness immediate precedence rather than
// accept a caller-supplied bool. The parameter keeps that dependency
// visible in this research sketch instead of hiding it in `close()`.
// A past cognition can occupy manodhātu's support position without losing
// its earlier cognition classification. Nor must a successor arise for an
// arhat's final citta to retain manas status: VAK 1.17 says another cause
// can be absent. Therefore no `last().unwrap()` or fabricated event.
fn as_manas(previous: Cognition) -> Support {
    Support::ImmediatelyPast(previous)
}

// Dharmadhātu is the object position of mental cognition. Its range
// includes feeling, recognition, formations, avijñapti, and unconditioned
// factors (VAK 1.15–1.16). It is not just prior cognition. Support and
// object cannot both be modeled as “the system's recent history.”

// 4. A visible form moves through three classifications without changing
// into three separate things.

fn eye_example() -> Result<Encounter, ClassificationError> {
    let eye = Sense::Eye;
    let visible = classify(Dharma::SensoryField(eye));
    assert_eq!(visible.skandha, Some(Skandha::Rupa));
    assert_eq!(visible.ayatana, Ayatana::Field(eye));
    assert_eq!(visible.dhatu, Dhatu::Object(Channel::Eye));

    let seeing = Cognition { channel: Channel::Eye, occurrence: 42 };
    let encounter = Encounter::classify(
        Support::Sensory(eye), Presented::Sensory(eye), seeing, false,
    )?;
    assert_eq!(encounter.dhatu_positions(), [
        Dhatu::Support(Channel::Eye),
        Dhatu::Object(Channel::Eye),
        Dhatu::Cognition(Channel::Eye),
    ]);
    Ok(encounter)
}

fn mental_example() -> Result<Encounter, ClassificationError> {
    // The eye cognition can next be considered in the support role.
    // Its prior result does not exhaust the dharma-object field.
    let earlier = Cognition { channel: Channel::Eye, occurrence: 42 };
    let present = Cognition { channel: Channel::Mind, occurrence: 43 };
    Encounter::classify(
        as_manas(earlier), Presented::DharmaObject, present, true,
    )
}

// The sensory field is not yet a finished Object of knowledge. `Viṣaya`
// names its role here; comprehension of `vastu` is a further Organon
// problem, not a return value of Encounter::classify.

// 5. Completeness is a separate, explicitly scoped research conjecture.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Verdict { Determined, Outstanding, Unexamined }

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct KnowingTask<Object, Mode> { object: Object, mode: Mode }

trait Knower<Object, Mode> {
    fn assess(&self, task: KnowingTask<Object, Mode>) -> Verdict;
}

fn complete_on<K, Object, Mode>(
    knower: &K,
    tasks: impl IntoIterator<Item = KnowingTask<Object, Mode>>,
) -> bool
where K: Knower<Object, Mode> {
    let mut tasks = tasks.into_iter().peekable();
    // The empty audit has no warrant to call any mind complete.
    tasks.peek().is_some()
        && tasks.all(|task| knower.assess(task) == Verdict::Determined)
}

// This proves completeness only relative to the supplied scope. VAK
// 1.01's sarvathā / sarvatra makes an unrestricted claim about modes and
// knowables. Eighteen dhātu positions are *not* eighteen knowing tasks;
// a finite audit cannot establish the Buddha's exhaustive knowledge.

// 6. The architectural wager.
//
// Skandha asks: under what gathered kind is this occurrence considered?
// Āyatana asks: in what capacity/field sphere does it become available?
// Dhātu asks: which support/object/cognition position does it occupy?
//
// Their overlap is the important datum. Avijñapti remains rūpa as
// aggregate while entering dharmāyatana and dharmadhātu in the other
// arrangements. A 5/12/18 mnemonic does not express that movement.
//
// The Organon's Being–Essence–Concept reading must answer to the exact
// cross-mappings and to manas as a change of role within one stream.
// If a source distinction defeats the analogy, revise the analogy.
