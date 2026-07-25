# VAK_2.34 — Citta, Manas, Vijñāna, and Fivefold Association

## 1. Sanskrit — Devanāgarī

```text
चित्तं मनोऽथ विज्ञानमेकार्थं चित्तचैतसाः ।
साश्रयालम्बनाकाराः संप्रयुक्ताश्च पञ्चधा ॥ VAkK_2.34 ॥
```

## 2. Sanskrit — IAST

```text
cittaṃ mano 'tha vijñānam ekārthaṃ cittacaitasāḥ /
sāśrayālambanākārāḥ saṃprayuktāś ca pañcadhā // VAkK_2.34 //
```

Source form:

```text
cittaṃ mano 'tha vijñānamekārthaṃ cittacaitasāḥ /
sāśrayā lambanākārāḥ saṃprayuktāśca pañcadhā // VAkK_2.34 //
```

## 3. Padaccheda and Grammar

| Sanskrit | Padaccheda | Grammar | Working Sense |
|---|---|---|---|
| cittaṃ | cittaṃ | neuter nominative/accusative singular | citta / mental field |
| manaḥ | manaḥ | neuter nominative singular | manas / mind |
| atha | atha | particle | and now / furthermore |
| vijñānam | vijñānam | neuter nominative singular | knowledge-event |
| eka-artham | eka-artham | neuter nominative singular | having one meaning / same referent |
| citta-caitasāḥ | citta-caitasāḥ | masculine nominative plural compound | citta and caittas |
| sa-āśraya | sāśraya | compound | with support |
| ālambana | ālambana | compound member | object-support |
| ākāra | ākāra | compound member | mode / aspect |
| saṃprayuktāḥ | saṃprayuktāḥ | masculine nominative plural | associated / conjoined |
| ca | ca | indeclinable | and |
| pañcadhā | pañcadhā | adverb | fivefold |

## 4. Literal Translation

```text
Citta, manas, and vijñāna have one meaning.
Citta and caittas are associated fivefold: with support, object-support, and mode.
```

## 5. Philosophical Translation

```text
Citta, manas, and vijñāna are treated here as functionally equivalent names for the mental occurrence.

Citta and caittas are not merely adjacent. They are associated by a fivefold rule involving support, object-support, mode or aspect, and their conjunction.
```

## 6. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| citta | mental field | Appearance-side field of mental occurrence |
| manas | mind | Inner coordinator; here grouped with citta and vijñāna |
| vijñāna | knowledge-event | Never translated as consciousness in this project |
| ekārtha | one meaning / same referent | Functional equivalence in this context, not crude identity of all uses |
| citta-caitasa | citta and caittas | Field and associated feature-functions |
| āśraya | support | Basis on which occurrence depends |
| ālambana | object-support | Object-bearing support or intentional object-field |
| ākāra | mode / aspect | Way the object-support is taken or appears |
| saṃprayukta | associated / conjoined | Technical relation of citta and caittas |
| pañcadhā | fivefold | Fivefold association rule |

## 7. Logical Determination

VAK_2.34 is the mature association rule for the citta-caitta system.

First, it gives functional equivalence:

```text
citta
manas
vijñāna
    = ekārtha
```

This means that, in this context, the same mental occurrence may be described from three angles:

```text
citta
    = field-side

manas
    = coordinating-side

vijñāna
    = knowledge-event side
```

Second, it gives Conjunction as association:

```text
citta + caitta
    = saṃprayukta
```

Their association is fivefold:

```text
support
object-support
mode / aspect
association
fivefold relation
```

The verse therefore gives the rule by which citta and caittas belong to one event.

## 8. Relation to Indriya

This verse clarifies the relation between the truth-side and appearance-side structures.

```text
Dhātu-Indriya
    = truth-side principle of experience

Citta-Caitta
    = appearance-side law of mental operation
```

But now the appearance-side has an association protocol:

```text
Citta-Caitta event
    requires shared support,
    shared object-support,
    shared mode,
    and lawful association.
```

This is how indriya-givenness becomes a determinate knowledge-event.

```text
Indriya
    gives operative access.

Citta
    receives the occurrence as field.

Caitta
    configures the occurrence as feature-function.

Vijñāna
    is the knowledge-event of that appearance.
```

## 9. Organon Interpretation

Organon reading:

```text
CittaManasVijnana
    = one event, three names:
        field
        coordinator
        knowledge-event
```

Association schema:

```text
CittaCaittaAssociation:
    hasSupport
    hasObjectSupport
    hasAspect
    hasAssociationRelation
    hasEventUnity
```

Agent architecture:

```text
Agent FactStore / KnowledgeStore
    requires event-unity rules.

A feature is not attached arbitrarily.
It belongs to an event only through support,
object-support,
aspect,
and lawful association.
```

This is a direct bridge to semantic dataset design.

## 10. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:CittaManasVijnanaEquivalence a rdfs:Class ;
    rdfs:label "Citta-Manas-Vijñāna Functional Equivalence" ;
    rdfs:comment "The treatment of citta, manas, and vijñāna as one meaning in this context." .

vak:CittaCaittaAssociation a rdfs:Class ;
    rdfs:label "Citta-Caitta Association" ;
    rdfs:comment "Fivefold association rule binding citta and caittas into one event." .

vak:hasSupport a rdf:Property ;
    rdfs:label "has support" .

vak:hasObjectSupport a rdf:Property ;
    rdfs:label "has object-support" .

vak:hasAspect a rdf:Property ;
    rdfs:label "has aspect" .

vak:hasAssociationRelation a rdf:Property ;
    rdfs:label "has association relation" .

vak:hasEventUnity a rdf:Property ;
    rdfs:label "has event unity" .

vak:CittaCaittaEvent a vak:CittaCaittaAssociation ;
    vak:hasSupport vak:Ashraya ;
    vak:hasObjectSupport vak:Alambana ;
    vak:hasAspect vak:Akara ;
    vak:hasAssociationRelation vak:Samprayoga .
```

## 11. Commit History

```text
VAK_2.34 opened.
Method: kārikā-first speculative seed.
Theme: citta, manas, and vijñāna functional equivalence; fivefold citta-caitta association.
Logical protocols recorded: functional equivalence and conjunctive association rule.
Relation to indriya tracked: association protocol explains how indriya-givenness becomes knowledge-event appearance.
Zero-padded file naming maintained: VAK_2.34.
```
