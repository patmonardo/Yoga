# VAK_3.50 — Bhājanaloka: Meru in the Water, Meru Above the Water

## 1. Sanskrit — Devanāgarī

```sanskrit
चतूरत्नमयो मेरुः जलेऽशीतिसहस्रके ।
मग्नः ऊर्ध्वं जलात् मेरुर्भूयोऽशीतिसहस्रकः ॥ VAkK_3.50 ॥
```

## 2. Sanskrit — IAST

```iast
catūratnamayo meruḥ jale 'śītisahasrake /
magnāḥ ūrdhva jalāt merur bhūyo 'śītisahasrakaḥ // VAkK_3.50 //
```

## 3. Source Caution

The source reading is:

```iast
catūratnamayo meruḥ jale 'śītisahasrake /
magnāḥ ūrdhva jalāt merurbhūyo 'śītisahasrakaḥ // VAkK_3.50 //
```

The source has `magnāḥ`, while the sense appears to require `magnaḥ`, “submerged.” This should be checked against Pradhan and the bhāṣya in Pass 2. First-pass analysis preserves the source reading while translating the expected syntactic sense.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| catūratnamayo | catuḥ-ratna-mayaḥ | made of four jewels / four precious substances |
| meruḥ | meruḥ | Meru, the central mountain |
| jale | jale | in water |
| 'śītisahasrake | aśīti-sahasrake | in eighty thousand; locative measure |
| magnāḥ | magnaḥ | submerged; source has plural-looking form, verify |
| ūrdhva | ūrdhvam | upward, above |
| jalāt | jalāt | from the water, above the water |
| meruḥ | meruḥ | Meru |
| bhūyaḥ | bhūyaḥ | again, further, moreover |
| 'śītisahasrakaḥ | aśīti-sahasrakaḥ | eighty thousand |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| catuḥ-ratna-mayaḥ | nominative singular masculine compound | qualifies `meruḥ`: “made of four jewels” |
| meruḥ | nominative singular masculine | subject |
| jale | locative singular neuter | location: “in water” |
| aśīti-sahasrake | locative singular compound | measured depth: “in eighty thousand” |
| magnaḥ | nominative singular masculine participle | predicate: “submerged” |
| ūrdhvam jalāt | adverbial phrase | “above the water” |
| meruḥ | nominative singular masculine | repeated subject |
| bhūyaḥ aśīti-sahasrakaḥ | numerical predicate | “again eighty thousand” |

## 6. Literal Translation

Meru, made of four jewels, is submerged in the water for eighty thousand. Above the water, Meru is again eighty thousand.

## 7. Philosophical Translation

Meru is determined as a four-jewel mountain whose structure is divided by the water-line: eighty thousand below the water and eighty thousand above it. The central axis of the world is therefore both immersed in the support-field and manifest above it.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| Meru | Meru | central axial mountain of the container-world |
| catuḥ-ratna-maya | made of four jewels | material constitution of Meru |
| jala | water | support-field in which Meru is partly submerged |
| magna | submerged | relation of Meru to the water-support |
| ūrdhvam | above / upward | vertical emergence above the waterline |
| aśīti-sahasra | eighty thousand | standard cosmological measure for Meru below and above water |

## 9. Doctrinal Determination

VAkK_3.50 determines Meru itself after the surrounding mountain-ring sequence of 3.48–3.49. Meru is not merely named; it is measured and materially qualified.

The verse gives three determinations:

```text
Meru is made of four jewels.
Meru is submerged eighty thousand in the water.
Meru rises eighty thousand above the water.
```

Thus Meru is the central axis joining the hidden support-field and the manifest cosmological field.

## 10. Logical Determination

```text
support-field
    → central mountain
        → submerged depth
            → manifest height
```

The central mountain is not simply placed on the support. It penetrates the water-field and rises out of it. This gives Meru a mediating function between support and appearance:

```text
below water
    ↔ waterline
        ↔ above water
```

Meru is the first vertical axis of the articulated container-world.

## 11. Interpretive Note

For first-pass purposes, the most important point is the vertical duplication: eighty thousand below and eighty thousand above. The world-axis has a concealed depth equal to its manifest height.

This is structurally powerful but should not yet be over-interpreted. Pass 1 records the determinate cosmographic logic. Pass 2 will check the bhāṣya for the exact reading of `magnāḥ/magnaḥ` and for the four-jewel explanation. Pass 3 may later draw out the Organon significance of an axis that is equally submerged and manifest.

## 12. OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

vak:VAK_3_50 a vak:Karika ;
    rdfs:label "VAK 3.50" ;
    vak:sourceSiglum "VAkK_3.50" ;
    vak:belongsToChapter vak:Lokanirdesa ;
    vak:belongsToBlock vak:VAK_3c ;
    vak:continuesFrom vak:VAK_3_49 ;
    vak:hasTopic loka:Meru ;
    vak:describes loka:MeruMaterialConstitution , loka:MeruSubmergedMeasure , loka:MeruEmergentMeasure .

loka:Meru a loka:CosmologicalMountain ;
    rdfs:label "Meru" ;
    rdfs:comment "The central axial mountain of the container-world." .

loka:MeruMaterialConstitution a owl:Class ;
    rdfs:label "Meru material constitution" ;
    rdfs:comment "Meru as made of four jewels." .

loka:hasSubmergedExtent a owl:DatatypeProperty ;
    rdfs:label "has submerged extent" ;
    rdfs:range xsd:string .

loka:hasEmergentExtent a owl:DatatypeProperty ;
    rdfs:label "has emergent extent" ;
    rdfs:range xsd:string .

loka:hasMaterialConstitution a owl:DatatypeProperty ;
    rdfs:label "has material constitution" ;
    rdfs:range xsd:string .

loka:Meru loka:hasMaterialConstitution "catuḥ-ratna-maya" ;
    loka:hasSubmergedExtent "eighty thousand" ;
    loka:hasEmergentExtent "eighty thousand" .
```

## 13. Commit Note

```text
Add VAK_3.50 first-pass analysis.

Continues the VAK_3c container-world block.
Determines Meru as four-jewel, submerged eighty thousand in water, and rising eighty thousand above water.
Uses VAK filename convention while preserving VAkK as source siglum.
Marks magnāḥ/magnaḥ for Pass 2 verification.
```
