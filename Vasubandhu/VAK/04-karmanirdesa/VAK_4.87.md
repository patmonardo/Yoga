# VAK_4.87

## 1. Sanskrit — Devanāgarī

प्रहाणमार्गे समले सफलं कर्म पञ्चभिः ।  
चतुर्भिरमलेऽन्यच्च सास्रवं यच्छुभाशुभम् ॥ ४.८७ ॥

## 2. Sanskrit — IAST

**prahāṇa-mārge samale sa-phalaṃ karma pañcabhiḥ |**  
**caturbhir amale ’nyac ca sāsravaṃ yac chubhāśubham || 4.87 ||**

Local source:

```text
prahāṇamārge samale saphalaṃ karma pañcabhiḥ /
caturbhiramale anyacca sāsravaṃ yacchubhāśubham // VAkK_4.87 //
```

The verse begins a systematic classification of karma according to the number of results with which each class is connected.

## 3. Padaccheda

```text
prahāṇa-mārge
samale
sa-phalam
karma
pañcabhiḥ
caturbhiḥ
amale
anyat
ca
sa-āsravam
yat
śubha-aśubham
```

Expanded syntax:

```text
samale prahāṇa-mārge karma
    pañcabhiḥ phalaiḥ sa-phalam

amale prahāṇa-mārge karma
    caturbhiḥ phalaiḥ sa-phalam

anyat ca yat sāsravaṃ śubham aśubhaṃ vā
    caturbhiḥ phalaiḥ sa-phalam
```

## 4. Grammar

### prahāṇa-mārge

Locative singular compound:

```text
prahāṇa
    abandoning
    relinquishment
    removal

mārga
    path
```

Thus `prahāṇa-mārga` is the path of abandoning.

### samale

Locative singular of `samala`:

```text
sa-
    with

mala
    stain
    contamination
```

Thus: contaminated.

### sa-phalam

Neuter nominative singular agreeing with `karma`:

```text
sa-
    possessing

phala
    result
```

Thus: possessing results.

### pañcabhiḥ / caturbhiḥ

Instrumental plurals:

```text
pañcabhiḥ
    with five

caturbhiḥ
    with four
```

The understood noun is `phalaiḥ`, results.

### amale

Locative singular:

```text
a-mala
    without stain
    uncontaminated
```

The understood phrase is `amale prahāṇa-mārge`.

### sāsravam

Neuter nominative singular:

```text
sa-āsrava
    accompanied by outflows
    contaminated
```

### śubhāśubham

Distributive compound:

```text
śubham
    wholesome

aśubham
    unwholesome
```

## 5. Literal Translation

> Karma in the contaminated path of abandoning possesses five results. In the uncontaminated path it possesses four; so also does any other contaminated karma that is wholesome or unwholesome.

## 6. Philosophical Translation

> The number of results attributable to an activity depends upon the causal and doctrinal field in which that activity occurs. Activity within a contaminated path of abandoning enters into all five result-relations. Activity within an uncontaminated path lacks one of those relations and therefore possesses four. Other contaminated wholesome and unwholesome activity likewise possesses four.

The verse asks not which single result follows from an act, but with how many distinct result-types a class of karma can stand in relation.

## 7. Technical Vocabulary

### The five results

The verse presupposes the fivefold Abhidharma result-system:

```text
1. vipāka-phala
       maturation result

2. niṣyanda-phala
       outflow-result

3. visaṃyoga-phala
       disconnection-result

4. puruṣakāra-phala
       activity-produced result

5. adhipati-phala
       dominant result
```

VAK_4.85 mentioned `adhipati`, `niṣyanda`, and `vipāka`; this verse invokes the complete fivefold taxonomy.

### samala / amala

```text
samala
    contaminated

amala
    uncontaminated
```

### sāsrava

```text
sāsrava
    accompanied by outflows
    belonging to the contaminated field
```

### śubha and aśubha

```text
śubha
    wholesome

aśubha
    unwholesome
```

Wholesome does not by itself mean uncontaminated.

## 8. Doctrinal Determination

### Contaminated path of abandoning: five results

Karma in the contaminated path of abandoning possesses all five result-relations.

### Uncontaminated path: four results

Karma in the uncontaminated path possesses four. The precise omitted result should be fixed from the Bhāṣya rather than guessed in the kārikā pass.

### Other contaminated wholesome and unwholesome karma: four results

Other contaminated karma, whether wholesome or unwholesome, also possesses four results.

This establishes at least two independent axes:

```text
ethical quality:
    wholesome / unwholesome

contamination status:
    contaminated / uncontaminated
```

These must not be collapsed.

## 9. Logical Determination

Let `Results(K)` be the set of result-types applicable to karma `K`.

```text
ContaminatedAbandoningPathKarma(K)
    → |Results(K)| = 5
```

```text
UncontaminatedPathKarma(K)
    → |Results(K)| = 4
```

```text
OtherContaminatedWholesomeOrUnwholesomeKarma(K)
    → |Results(K)| = 4
```

Equal cardinality does not imply identical membership:

```text
|Results(K1)| = |Results(K2)|
    does not imply
Results(K1) = Results(K2)
```

The kārikā gives cardinality; the Bhāṣya must determine the exact members of each result-set.

## 10. Light Organon Interpretation

At the Kernel level, the verse requires a multidimensional classification:

```text
KarmaClassification {
    ethicalQuality
    contaminationStatus
    pathType
    applicableResults[]
    resultCount
}
```

A single label such as `Wholesome` does not determine contamination status, and a result count does not determine result-set membership.

The safe structural lesson is:

```text
class membership
independent dimensions
set cardinality
exact set membership
```

must remain distinct.

## 11. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_87
    a vak:Karika ;
    rdfs:label "VAkK 4.87" ;
    vak:continues vak:VAK_4_86 ;
    vak:hasTopic vak:KarmicResultCardinality .

vak:FiveResults
    vak:includes
        vak:MaturationResult,
        vak:OutflowResult,
        vak:DisconnectionResult,
        vak:ActivityProducedResult,
        vak:DominantResult ;
    vak:hasCardinality 5 .

vak:ContaminatedAbandoningPathKarma
    rdfs:subClassOf vak:Karma ;
    vak:hasContaminationStatus vak:Contaminated ;
    vak:hasPathType vak:AbandoningPath ;
    vak:hasResultCardinality 5 .

vak:UncontaminatedPathKarma
    rdfs:subClassOf vak:Karma ;
    vak:hasContaminationStatus vak:Uncontaminated ;
    vak:hasResultCardinality 4 .

vak:OtherContaminatedWholesomeKarma
    rdfs:subClassOf vak:WholesomeKarma ;
    vak:hasContaminationStatus vak:Contaminated ;
    vak:hasResultCardinality 4 .

vak:OtherContaminatedUnwholesomeKarma
    rdfs:subClassOf vak:UnwholesomeKarma ;
    vak:hasContaminationStatus vak:Contaminated ;
    vak:hasResultCardinality 4 .
```

## 12. Commit Note

```text
VAK_4.87 — Classify karma by the number of its results

- introduce the complete five-result taxonomy
- assign five results to karma in the contaminated path of abandoning
- assign four results to karma in the uncontaminated path
- assign four results to other contaminated wholesome or unwholesome karma
- distinguish ethical quality from contamination status
- preserve result cardinality separately from exact result-set membership
- defer identification of excluded results to the Bhāṣya pass
- keep the Organon interpretation at the Kernel classification level
```

### First-pass determination

```text
contaminated path of abandoning:
    five results

uncontaminated path:
    four results

other contaminated wholesome or unwholesome karma:
    four results
```

The structural point is that the causal range of karma depends not only upon whether it is wholesome or unwholesome, but also upon whether it is contaminated and what path-class it belongs to.
