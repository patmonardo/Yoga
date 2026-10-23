# VAK_2.35 — Dissociated Formations

## 1. Sanskrit (Devanāgarī)

```sanskrit
विप्रयुक्तास्तु संस्काराः प्राप्त्यप्राप्ती सभागता ।
आसंज्ञिकं समापत्ती जीवितं लक्षणानि च ॥ २.३५ ॥
```

## 2. Sanskrit (IAST)

```text
viprayuktās tu saṃskārāḥ prāptyaprāptī sabhāgatā /
āsaṃjñikaṃ samāpattī jīvitaṃ lakṣaṇāni ca // 2.35 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| viprayuktāḥ | nom. pl. m.; past passive participle | dissociated; the Bhāṣya specifies dissociation from *citta* |
| tu | particle | the new class |
| saṃskārāḥ | nom. pl. m. | formations |
| prāpti-aprāptī | nom. dual f. | acquisition and non-acquisition |
| sabhāgatā | nom. sg. f. | commonality |
| āsaṃjñikam | nom. sg. n. | listed; English not locked |
| samāpattī | nom. dual f. | two attainments |
| jīvitam | nom. sg. n. | life |
| lakṣaṇāni | nom. pl. n. | the marks |
| ca | conjunction | and; the enumeration continues into the next verse |

The verse introduces a class of formations after 2.34 has specified the fivefold association of *citta* and *caittas*. The Bhāṣya calls these *citta-viprayukta*: they do not enter that form of association. The term does not by itself deny other relations to an episode or a continuum.

The grammar opens external sandhi and retains the acquisition pair. The next verse's groups of names and so forth is not an extra token in this verse's parse.

```text
# tokens: viprayuktāḥ tu saṃskārāḥ prāptyaprāptī sabhāgatā āsaṃjñikam samāpattī jīvitam lakṣaṇāni ca
```

## 4. Grammar

The opening class-name governs the following enumeration. Two duals remain pairs; the marks remain plural. Their later definitions and any complete numerical inventory are not supplied by this introductory verse. The final conjunction leaves the list open for *nāmakāyādayaś ca* at the start of 2.36. Grammar records the class and its members; it does not explain their causal functions.

```nltk-fcfg
% start S
# tokens: viprayuktāḥ tu saṃskārāḥ prāptyaprāptī sabhāgatā āsaṃjñikam samāpattī jīvitam lakṣaṇāni ca
S[SEM=<DissociatedEntry(acquisition) & DissociatedEntry(nonacquisition) & DissociatedEntry(commonality) & DissociatedEntry(asamjnika) & DissociatedEntry(attainment_one) & DissociatedEntry(attainment_two) & DissociatedEntry(life) & DissociatedEntry(marks)>] -> CLASS MEMBERS
CLASS -> DISSOCIATED CONTRAST FORMATIONS
DISSOCIATED -> 'viprayuktāḥ'
CONTRAST -> 'tu'
FORMATIONS -> 'saṃskārāḥ'
MEMBERS -> ACQUISITIONPAIR COMMONALITY ASAMJNIKA ATTAINMENTS LIFE MARKS AND
ACQUISITIONPAIR -> 'prāptyaprāptī'
COMMONALITY -> 'sabhāgatā'
ASAMJNIKA -> 'āsaṃjñikam'
ATTAINMENTS -> 'samāpattī'
LIFE -> 'jīvitam'
MARKS -> 'lakṣaṇāni'
AND -> 'ca'
```

```nltk-dep
'saṃskārāḥ' -> 'viprayuktāḥ' | 'tu' | 'prāptyaprāptī' | 'sabhāgatā' | 'āsaṃjñikam' | 'samāpattī' | 'jīvitam' | 'lakṣaṇāni'
'lakṣaṇāni' -> 'ca'
```

| Span | Constituent | Result |
|---|---|---|
| [0, 3) | `CLASS` | formations outside the preceding citta–caitta association, as the Bhāṣya specifies |
| [3, 10) | `MEMBERS` | named entries, two pairs, plural marks, open continuation |
| [0, 10) | `S` | classification, not definitions or proof of distinct reality |

## 5. Translation

### Literal Translation

> The dissociated formations are acquisition and non-acquisition, commonality, āsaṃjñika, the two attainments, life, and the marks.

### Bhāṣya-informed study translation

> Formations dissociated from the association of consciousness and its mental factors include acquisition and non-acquisition, commonality, āsaṃjñika, the two attainments, life, and the marks; the list continues with groups of names and related groups at the start of 2.36.

## 6. Philosophical Translation

> After specifying how consciousness and mental factors operate together, the text introduces conditioned formations that do not take part in that fivefold conjunction and are not Form by nature. Their place in a process is the question opened by the list, not answered by the class-name.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| citta-viprayukta-saṃskāra | formation dissociated from consciousness | outside the fivefold citta–caitta association; not Form by nature; still conditioned |
| prāpti | acquisition | listed; defined next |
| aprāpti | non-acquisition | the pair |
| sabhāgatā | commonality | listed |
| āsaṃjñika | āsaṃjñika | English not locked |
| samāpatti | attainment | two; not identified here |
| jīvita | life | listed |
| lakṣaṇa | mark | plural |
| nāma-kāya | groups of names | continuation of this list in 2.36; not the whole *nāma* side of *nāma-rūpa* |

## 8. Logical Determination

**Kārikā, derived.** Entry constants represent listed headings. Marks is a plural heading, not one mark; the two attainment slots are distinguished without importing their later names. Entry membership does not establish a count of distinct real dharmas.

```nltk-sem
classification : DissociatedEntry(acquisition)
acquisition_pair : DissociatedEntry(acquisition) & DissociatedEntry(nonacquisition)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(DissociatedEntry(acquisition) & DissociatedEntry(nonacquisition) & DissociatedEntry(commonality) & DissociatedEntry(asamjnika) & DissociatedEntry(attainment_one) & DissociatedEntry(attainment_two) & DissociatedEntry(life) & DissociatedEntry(marks))

# THEORY prose_classification
# EXPECT prose_classification T
all x.(DissociatedEntry(x) -> (FormationEntry(x) & ConditionedEntry(x) & -FivefoldCittaCaittaAssociated(x) & -FormNature(x)))
DissociatedEntry(name_groups) & ContinuationEntry(name_groups)

# THEORY rejected_dissociated_means_unconditioned
# EXPECT rejected_dissociated_means_unconditioned F
all x.(DissociatedEntry(x) -> -ConditionedEntry(x))

# THEORY rejected_asamjnika_is_one_of_attainment_pair
# EXPECT rejected_asamjnika_is_one_of_attainment_pair F
asamjnika = attainment_one | asamjnika = attainment_two

# THEORY rejected_every_listed_entry_is_single
# EXPECT rejected_every_listed_entry_is_single F
all x.(DissociatedEntry(x) -> SingleEntry(x))
```

```nltk-valuation
acquisition => acquisition_entry
nonacquisition => nonacquisition_entry
commonality => commonality_entry
asamjnika => asamjnika_entry
attainment_one => attainment_slot_one
attainment_two => attainment_slot_two
life => life_entry
marks => marks_heading
name_groups => name_groups_heading
DissociatedEntry => {acquisition_entry,nonacquisition_entry,commonality_entry,asamjnika_entry,attainment_slot_one,attainment_slot_two,life_entry,marks_heading,name_groups_heading}
FormationEntry => {acquisition_entry,nonacquisition_entry,commonality_entry,asamjnika_entry,attainment_slot_one,attainment_slot_two,life_entry,marks_heading,name_groups_heading}
ConditionedEntry => {acquisition_entry,nonacquisition_entry,commonality_entry,asamjnika_entry,attainment_slot_one,attainment_slot_two,life_entry,marks_heading,name_groups_heading}
FivefoldCittaCaittaAssociated => {}
FormNature => {}
ContinuationEntry => {name_groups_heading}
SingleEntry => {acquisition_entry,nonacquisition_entry,commonality_entry,asamjnika_entry,attainment_slot_one,attainment_slot_two,life_entry}
```

The qualified association predicate refers only to the five equalities explained at 2.34. The prose-classification theory follows the class-name and contextual English against the running witness's conflicting double negation; it is not a parse or repair of that defective sentence. The continuation is modeled separately, not attributed to the numbered verse. No converse or exhaustive-list axiom is asserted. In particular, the model does not deny causal relations to consciousness or determine distinct real existence.

## 9. Interpretive Note

**Translation note.** The commentary adds groups of names and related groups, and contrasts these formations with both citta–caitta association and Form nature. Its transmitted double negative makes the first contrast textually uncertain at the level of that sentence; the class-name and the 2.34 account support the contextual construal. It does not define the listed attainments, life, or marks here.

The class opens after the close of consciousness and the mental factors. No objection. No school. The members follow separately.

Āsaṃjñika is not one of the two attainments. Their definitions are not imported. Life is not defined. The marks are not enumerated.

The double negation stays in the source. The English follows the class-name and must remain marked as contextual. The groups of names and so forth continue the list at the opening of 2.36; that continuation belongs to this enumeration, not the acquisition definition.

**Organon question.** If Mind is understood as a result within a cognitive process, what work do these formations perform without being *caittas* in the fivefold conjunction? This verse does not answer. It also does not turn *saṃjñā* into *vijñāna*: their co-occurrence in the preceding account does not erase their different roles. The individual entries must be examined before assigning such process functions to them.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_35
    a vak:Karika ;
    rdfs:label "VAK 2.35" ;
    vak:hasTopic vak:DissociatedFormations ;
    vak:belongsTo vak:Indriyanirdesa .

vak:DissociatedFormations vak:notForm true .
vak:DissociatedFormations vak:outsideFivefoldCittaCaittaAssociation true .
vak:Prapti vak:definedHere false .

organon:VAK_2_35_Interpretation
    organon:distinguishes vak:EnumeratedEntry, vak:Association,
        vak:ConditionedStatus, vak:DistinctReality .
```
