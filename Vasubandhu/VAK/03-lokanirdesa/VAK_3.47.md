# VAkK_3.47 — Bhājanaloka: Lateral Measure of the Water-Gold Maṇḍala

## 1. Sanskrit — Devanāgarī

```sanskrit
तिर्यक् त्रीणि सहस्राणि सार्धं शतचतुष्टयम् ।
लक्षद्वादशकं चैव जलकाञ्चनमण्डलम् ॥ VAkK_3.47 ॥
```

## 2. Sanskrit — IAST

```iast
tiryak trīṇi sahasrāṇi sārdhaṃ śatacatuṣṭayam /
lakṣadvādaśakaṃ caiva jalakāñcanamaṇḍalam // VAkK_3.47 //
```

## 3. Source Caution

The source reading is:

```iast
tiryak trīṇi sahasrāṇi sārdhaṃ śatacatuṣṭayam /
lakṣadvādaśakaṃ caiva jalakāñcanamaṇḍalam // VAkK_3.47 //
```

This verse gives the lateral measure, `tiryak`, of the water-gold maṇḍala. The numerical expression is treated in first pass as:

```text
12 lakṣas + 3,000 + 450
```

The exact arithmetic and inherited commentarial handling should be verified in Pass 2 against Pradhan and the bhāṣya.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| tiryak | tiryak | across, laterally, horizontally |
| trīṇi | trīṇi | three |
| sahasrāṇi | sahasrāṇi | thousands |
| sārdhaṃ | sa-ardham | with a half; plus half |
| śatacatuṣṭayam | śata-catuṣṭayam | a set of four hundreds; four hundred, with `sārdhaṃ` likely yielding four hundred and fifty |
| lakṣadvādaśakam | lakṣa-dvādaśakam | twelve lakṣas |
| ca | ca | and |
| eva | eva | indeed, just, precisely |
| jalakāñcanamaṇḍalam | jala-kāñcana-maṇḍalam | the water-gold maṇḍala |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| tiryak | indeclinable | marks the measure as lateral or transverse |
| trīṇi sahasrāṇi | nominative/accusative neuter plural phrase | numerical measure: three thousand |
| sārdhaṃ śatacatuṣṭayam | numerical compound phrase | four hundred with a half-hundred; provisionally four hundred and fifty |
| lakṣa-dvādaśakam | nominative/accusative singular neuter | numerical measure: twelve lakṣas |
| ca eva | particles | conjunction and emphasis |
| jala-kāñcana-maṇḍalam | nominative/accusative singular neuter | measured subject: the water-gold maṇḍala |

## 6. Literal Translation

Laterally, the water-gold maṇḍala is twelve lakṣas, and also three thousand and four hundred with a half.

## 7. Philosophical Translation

The water-gold support-field is now determined not only vertically but laterally. Its horizontal extension is measured as twelve lakṣas plus three thousand and four hundred-and-a-half hundreds. The container-world gains transverse extension after its layered support has been established.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| tiryak | lateral / transverse / across | horizontal extension of the world-support |
| jala | water | fluid support-field from VAkK_3.46 |
| kāñcana | gold / golden support | stabilized support-field from VAkK_3.46 |
| maṇḍala | disk / field / support-plane | bounded cosmological support-field |
| lakṣa | hundred-thousand | large-scale cosmological unit |
| sahasra | thousand | numerical measure |
| śata | hundred | numerical measure |
| sārdha | with half | fractional augmentation of a numerical measure |

## 9. Doctrinal Determination

VAkK_3.47 completes the immediate measure of the water-gold foundation introduced in VAkK_3.46. The prior verse gave vertical determination: water and the golden remainder. This verse gives lateral determination: the transverse extent of the combined `jala-kāñcana-maṇḍala`.

The sequence is therefore:

```text
VAkK_3.45
    foundational wind-support

VAkK_3.46
    vertical water-support and golden remainder

VAkK_3.47
    lateral measure of the water-gold maṇḍala
```

This confirms that the container-world is being built by determinate measures, not by narrative description alone.

## 10. Logical Determination

```text
support-field
    → vertical determination
        → lateral determination
```

The verse adds transverse extension to the previous vertical structure. Cosmological existence is being generated through measurable dimensionality:

```text
below
    thickness / elevation
        breadth / lateral extension
```

The logical importance lies in the transition from support as mere foundation to support as extended field. The water-gold maṇḍala is no longer only what lies beneath; it is now a determinate expanse.

## 11. Interpretive Note

This verse is compact, but structurally important. The Kośa is not yet discussing mountains, continents, or inhabited regions. It is still constructing the dimensional support of the world-container. The field must first be measurable before it can be articulated into places.

For Organon purposes, the verse marks the emergence of breadth:

```text
foundation
    → measured expanse
        → possible placement
```

This prepares VAkK_3.48–3.52, where Meru, the surrounding mountains, and the inner and outer seas appear within this measured support-field.

## 12. OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

vak:VAkK_3_47 a vak:Karika ;
    rdfs:label "VAkK 3.47" ;
    vak:belongsToChapter vak:Lokanirdesa ;
    vak:belongsToBlock vak:VAK_3c ;
    vak:continuesFrom vak:VAkK_3_46 ;
    vak:hasTopic loka:JalaKancanaMandala ;
    vak:describes loka:LateralMeasure .

loka:JalaKancanaMandala a owl:Class ;
    rdfs:label "jala-kāñcana-maṇḍala" ;
    rdfs:comment "The combined water-gold support-field of the container-world." .

loka:LateralMeasure a owl:Class ;
    rdfs:label "tiryak-pramāṇa" ;
    rdfs:comment "The transverse or lateral measure of a cosmological support-field." .

loka:hasLateralExtent a owl:DatatypeProperty ;
    rdfs:label "has lateral extent" ;
    rdfs:domain loka:JalaKancanaMandala ;
    rdfs:range xsd:string .

loka:hasMeasureComponent a owl:DatatypeProperty ;
    rdfs:label "has measure component" ;
    rdfs:range xsd:string .

loka:JalaKancanaMandala rdfs:subClassOf loka:SupportLayer ;
    vak:canonicalTranslation "water-gold maṇḍala" ;
    loka:hasLateralExtent "twelve lakṣas plus three thousand plus four hundred and fifty, to be verified in Pass 2" ;
    loka:hasMeasureComponent "lakṣa-dvādaśakam" ;
    loka:hasMeasureComponent "trīṇi sahasrāṇi" ;
    loka:hasMeasureComponent "sārdhaṃ śatacatuṣṭayam" .
```

## 13. Commit Note

```text
Add VAkK_3.47 first-pass analysis.

Continues VAK_3c container-world foundations.
Adds lateral measure of the water-gold maṇḍala after the vertical water/gold support of VAkK_3.46.
Marks compound numerical expression for Pass 2 verification.
```
