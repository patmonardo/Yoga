//! Runnable Organon sketch: Corpora–LM–Logic as applied BEP, then BEC.
//!
//! Run: rustc Vasubandhu/Essays/applied-bep-bec.rs -o /tmp/applied-bep-bec && /tmp/applied-bep-bec
//! The source witness is VAK 2.02. The mappings are project determinations.

#[derive(Debug)]
struct CorpusWitness {
    reference: &'static str,
    text: &'static str,
}

#[derive(Debug, PartialEq)]
struct Marks {
    own_meaning: bool,
    apprehension: bool,
    governance: bool,
    mind_range: bool,
}

trait MarkModel {
    fn mark(&self, text: &str, marks: &mut Marks);
}

struct LexicalModel;
impl MarkModel for LexicalModel {
    fn mark(&self, text: &str, marks: &mut Marks) {
        marks.own_meaning = text.contains("svārth");
        marks.apprehension = text.contains("palabdhi") || text.contains("palabdhy");
        marks.governance = text.contains("ādhipaty");
    }
}

struct ScopeModel;
impl MarkModel for ScopeModel {
    fn mark(&self, text: &str, marks: &mut Marks) {
        marks.mind_range = text.contains("sarvasya ca");
    }
}

/// LM is a gateway of marks composed from models, not a single classifier.
struct LanguageModule {
    models: Vec<Box<dyn MarkModel>>,
}

impl LanguageModule {
    fn new() -> Self {
        Self { models: vec![Box::new(LexicalModel), Box::new(ScopeModel)] }
    }

    fn read(&self, witness: &CorpusWitness) -> Marks {
        let mut marks = Marks {
            own_meaning: false,
            apprehension: false,
            governance: false,
            mind_range: false,
        };
        for model in &self.models {
            model.mark(witness.text, &mut marks);
        }
        marks
    }
}

#[derive(Debug)]
struct RuleWitness {
    rule: &'static str,
    source: &'static str,
}

#[derive(Debug)]
struct BecApplication {
    being: &'static str,
    essence: &'static str,
    concept: &'static str,
    warrant: RuleWitness,
}

/// Logic applies a situated rule to source-linked marks. Missing marks block the claim.
fn apply_principle(witness: &CorpusWitness, marks: &Marks) -> Result<BecApplication, &'static str> {
    if !(marks.own_meaning && marks.apprehension && marks.governance && marks.mind_range) {
        return Err("required source marks are missing");
    }
    Ok(BecApplication {
        being: "six faculties are presented in VAK 2.02",
        essence: "five govern apprehension of their respective meanings; mind ranges across meanings",
        concept: "faculty is determined by its governing role in a situated apprehension",
        warrant: RuleWitness {
            rule: "svārtha-upalabdhi-ādhipatya determines the five; sarvasya ca extends the range for mind",
            source: witness.reference,
        },
    })
}

fn main() {
    let corpus = CorpusWitness {
        reference: "VAK 2.02; Organon 02-indriya/VAK_2.02.md",
        text: "svārthopalabdhyādhipatyāt sarvasya ca ṣaḍindriyam",
    };
    let marks = LanguageModule::new().read(&corpus);
    let result = apply_principle(&corpus, &marks).expect("the witness supports the rule");
    println!("BEP / Corpora-Base: {}", corpus.reference);
    println!("BEP / LM-Essence marks: {marks:?}");
    println!("BEP / Logic-Principle: {}", result.warrant.rule);
    println!("BEC / Being: {}", result.being);
    println!("BEC / Essence: {}", result.essence);
    println!("BEC / Concept: {}", result.concept);
    println!("Warrant: {}", result.warrant.source);
}
