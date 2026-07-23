# VAK_7.04 — Truth-Division and the Terminal Knowledges

## Sanskrit

### Devanāgarī

```text
ते एव सत्यभेदेन चत्वारि एते चतुर्विधे ।
अनुत्पादक्षयज्ञाने ते पुनः प्रथमोदिते ॥ ७.४ ॥
```

### IAST

```text
te eva satyabhedena catvāri ete caturvidhe /
anutpādakṣayajñāne te punaḥ prathamodite // VAK_7.04 //
```

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| te | nominative dual | those two |
| eva | indeclinable | precisely; just |
| satya-bhedena | instrumental singular | by the division of the truths |
| catvāri | nominative plural neuter | four |
| ete | nominative dual | these two |
| caturvidhe | nominative dual neuter | fourfold |
| anutpāda-jñāne | nominative dual neuter | knowledge of non-arising |
| kṣaya-jñāne | nominative dual neuter | knowledge of exhaustion |
| te | nominative dual | those two |
| punaḥ | indeclinable | again; in turn |
| prathama-udite | locative dual / compressed reference | in the two first stated |

## Grammar

The opening `te eva` refers back to the two uncontaminated knowledges named in VAK 7.02 and specified in VAK 7.03:

```text
dharmajñāna
anvayajñāna
```

Through `satyabhedena`, “by the distinction of the truths,” each is articulated according to the four truths:

```text
duḥkha
samudaya
nirodha
mārga
```

The first half therefore states that the two pure knowledges become fourfold through the truth-division.

The second half introduces `kṣayajñāna` and `anutpādajñāna` as themselves fourfold, because they are determined with respect to the same four truths.

The closing phrase `te punaḥ prathamodite` is highly compressed. In this first-pass reading, it indicates that these terminal knowledges are grounded in, or take their place within, the two knowledges first stated: dharma-knowledge and subsequent knowledge.

## Literal Translation

Those same two, through the division of the truths, are four.
These two—knowledge of non-arising and knowledge of exhaustion—are fourfold.
They again belong to the two first stated.

## Philosophical Translation

Dharma-knowledge and subsequent knowledge are each articulated according to the four truths. Knowledge of exhaustion and knowledge of non-arising are likewise fourfold, and their determination remains within the structure first established by those two uncontaminated knowledges.

## Technical Vocabulary

### satyabheda

```text
satya-bheda
    = division according to the truths
```

The four truths do not appear here as an empirical list. They function as the formal differentiating principle by which uncontaminated knowledge receives determinate forms.

### caturvidha

```text
caturvidha
    = fourfold
```

The fourfoldness is not an additional species beside dharma-knowledge and subsequent knowledge. It is the internal articulation of each according to the four truths.

### kṣayajñāna

```text
kṣayajñāna
    = knowledge of exhaustion
```

This is determinate knowledge that the relevant task has been completed and that the contaminants to be exhausted have been exhausted.

### anutpādajñāna

```text
anutpādajñāna
    = knowledge of non-arising
```

This is determinate knowledge that what has been exhausted will not arise again and that the completed work need not be repeated.

### prathamodita

```text
prathama-udita
    = first stated
    = previously announced
```

The phrase points back to the first uncontaminated division:

```text
dharmajñāna / anvayajñāna
```

Its exact syntactic force should remain open for deeper commentary work.

## Doctrinal Determination

VAK 7.04 extends the structure of VAK 7.02–7.03.

### 1. The two uncontaminated knowledges

```text
anāsrava-jñāna
    ├── dharmajñāna
    └── anvayajñāna
```

### 2. Each is divided by the four truths

```text
dharmajñāna
    ├── suffering
    ├── origin
    ├── cessation
    └── path

anvayajñāna
    ├── suffering
    ├── origin
    ├── cessation
    └── path
```

This produces eight truth-determined uncontaminated knowledges.

### 3. The terminal knowledges are also fourfold

```text
kṣayajñāna
    ├── suffering
    ├── origin
    ├── cessation
    └── path

anutpādajñāna
    ├── suffering
    ├── origin
    ├── cessation
    └── path
```

The verse does not introduce these as unstructured final states. Even terminal knowledge remains truth-determined.

## Logical Determination

The important logical operation is not empirical enumeration but cross-classification.

```text
first axis
    dharma / anvaya

second axis
    suffering / origin / cessation / path
```

The result is a structured field:

```text
2 × 4 = 8
```

The two terminal knowledges are then articulated by the same fourfold truth-division:

```text
2 × 4
```

The method is therefore:

```text
establish a dichotomy
    ↓
apply a complete formal division
    ↓
locate later determinations inside the established structure
```

This supports the emerging observation that the chapter prefers exact formal division over empirical proliferation.

## Organon Light

VAK 7.02 established the primary dichotomy of contaminated and uncontaminated knowledge. Within the uncontaminated side, it established the further dichotomy:

```text
dharma / anvaya
```

VAK 7.03 assigned these two to their respective domains.

VAK 7.04 now adds the four-truth determination:

```text
pure knowledge
    = domain-difference
      crossed with
      truth-difference
```

So knowledge becomes determinate through two independent principles:

```text
where the truth is known
what truth is known
```

The terminal knowledges do not abolish this structure. They complete it.

## Interpretive Note

The verse is important for the project because it refuses to identify liberation with an undifferentiated state beyond determination.

```text
exhaustion
non-arising
```

remain articulated through the four truths. Final knowledge is therefore not the disappearance of logical distinction but its completed possession.

This conclusion should remain provisional until the following verses specify the ten knowledges and their mutual relations in greater detail.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_7_04
    a vak:Karika ;
    rdfs:label "VAK 7.04" ;
    vak:determines jna:DharmaKnowledge,
                   jna:SubsequentKnowledge,
                   jna:ExhaustionKnowledge,
                   jna:NonArisingKnowledge,
                   jna:FourTruthDivision .

jna:DharmaKnowledge
    vak:dividedBy jna:FourTruthDivision .

jna:SubsequentKnowledge
    vak:dividedBy jna:FourTruthDivision .

jna:ExhaustionKnowledge
    vak:dividedBy jna:FourTruthDivision .

jna:NonArisingKnowledge
    vak:dividedBy jna:FourTruthDivision .
```

## Commit History

```text
2026-07-23 — Initial kārikā-pass analysis.
```
