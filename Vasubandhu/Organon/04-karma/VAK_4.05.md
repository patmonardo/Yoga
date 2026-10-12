# VAK_4.05 — Karma and Its Great-Element Support

## 1. Sanskrit (Devanāgarī)

> स्वानि भूतान्युपादाय कायवाक्कर्म सास्रवम् ।
>
> अनास्रवं यत्र जातोऽविज्ञप्तिरनुपात्तिका ॥ ४.५ ॥

## 2. Sanskrit (IAST)

> svāni bhūtāny upādāya kāyavākkarma sāsravam /
>
> anāsravaṃ yatra jāto 'vijñaptir anupāttikā // 4.5 //

VAK 4.04 distinguished the past producing basis from the present sustaining
support of desire-domain `avijñapti`. VAK 4.05 now asks which Great Elements
support bodily and verbal karma at each level. It crosses two
independent classifications:

```text
karmic status
    sāsrava / anāsrava

level of support
    desire-realm or dhyāna-level Great Elements
```

The Bhāṣya resolves the compressed `yatra jātaḥ`: it refers to the practitioner
who, born in a given level, produces uncontaminated bodily or verbal karma.

## 3. Lexical Analysis

```text
sva-āni bhūta-āni up-ādāya kāya-vāk-karma sa-āsravam /
an-āsravam yatra jātaḥ avijñaptiḥ an-upāttikā
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| svāni bhūtāni | accusative neuter plural | its own Great Elements; the Bhāṣya specifies those of the same level |
| upādāya | absolutive of `upa-ā-√dā` | depending upon; taking as basis |
| kāyavākkarma | nominative neuter singular compound | bodily and verbal karma |
| sāsravam | nominative neuter singular adjective | with influx; contaminated |
| anāsravam | nominative neuter singular adjective | without influx; uncontaminated |
| yatra jātaḥ | relative adverb and nominative masculine participle | where the producer is born, as specified by the Bhāṣya |
| avijñaptiḥ | nominative feminine singular | non-disclosing continuity |
| anupāttikā | nominative feminine singular adjective | non-appropriated |

## 4. Grammar

The first pāda predicates `sāsravam` of `kāya-vāk-karma`; `svāni bhūtāni upādāya` is its dependent absolutive phrase. The second pāda gives `anāsravam` as a further nominal subject, followed by the relative phrase `yatra jātaḥ`. It closes with the nominal predication `avijñaptiḥ anupāttikā`.

## 5. Translation

### Literal Translation

> Contaminated bodily and verbal karma depends upon its own Great Elements.
> Uncontaminated [karma depends upon the Great Elements of the level] where
> [its producer] is born. Non-disclosing continuity is non-appropriated.

The bracketed terms are syntactically supplied from the Bhāṣya.

### Bhāṣya-informed study translation

> Contaminated bodily and verbal karma depends upon the Great Elements of
> its own level. Uncontaminated bodily and verbal karma has no separate
> uncontaminated Great-Element support; it depends upon the Great Elements
> of the level where its producer is born and arises through their force.
> The Bhāṣya identifies `avijñapti` as non-disclosing continuity and states
> that it is non-appropriated.

The same-level series through the fourth dhyāna, the absence of
uncontaminated Great Elements, and the explicit referent of `jātaḥ` are
Bhāṣya determinations.

## 6. Philosophical Translation

### Interpretation

For contaminated bodily and verbal karma, the Bhāṣya matches the karma's level
with the Great Elements supporting it. Uncontaminated karma has no separate
uncontaminated Great Elements; it is produced through the Great Elements
of the level in which its producer is born. The passage distinguishes the
status of the karma from the level of its support. It then states that
`avijñapti`—non-disclosing continuity—is non-appropriated, without explaining
that classification further here.

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this unit |
|---|---|---|
| mahābhūta | Great Element | basis supporting bodily and verbal karma |
| svāni bhūtāni | its own Great Elements | same-level support of contaminated bodily/verbal karma |
| upādāya | depending upon; taking as basis | dependence upon a basis, not identity with it |
| kāya-karma | bodily karma | may be in the mode of manifestation or non-disclosing continuity |
| vāk-karma | verbal karma | may be in the mode of manifestation or non-disclosing continuity |
| sāsrava | with influx; contaminated | karma associated with the contaminated classification |
| anāsrava | without influx; uncontaminated | karma distinct from the contaminated classification |
| bhūmi | level | locus whose Great Elements support the karma produced there |
| tadbhūmika | belonging to that level | Bhāṣya term specifying the level correspondence |
| dhātu-apratitatva | not included within a Principle-classification | reason uncontaminated Dharmas have no corresponding classification |
| anāsrava-bhūta-abhāva | absence of uncontaminated Great Elements | no separate uncontaminated Great-Element basis exists |
| tadbalena utpatti | arising through their force | karma arises through the Great Elements of that level |
| vijñapti | manifestation; disclosure | bodily or verbal karma in its disclosive mode |
| avijñapti | non-disclosing continuity | non-disclosing mode of karma; classified as Form in the Vaibhāṣika account |
| upātta | appropriated | taken into the living bodily support |
| anupāttika | non-appropriated | not appropriated as a living bodily constituent |

The decisive distinctions are:

```text
anāsrava
    ≠ belonging to a separate uncontaminated Great-Element level

supported by Great Elements
    ≠ identical with those supporting Principles

Form-classified
    ≠ necessarily appropriated bodily support
```

## 8. Logical Determination


Contaminated bodily and verbal action → its own Elements; the second pāda qualifies uncontaminated action by its level of arising and names non-disclosing continuity as non-appropriated.

## 9. Interpretive Note

The Bhāṣya distinguishes the level of the karma from the level of the Great
Principles that support it. It then states that `avijñapti` is
non-appropriated, without explaining this property further in the present
unit.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix karma: <http://127.0.0.1:3000/karma#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_05
    a vak:Karika ;
    rdfs:label "VAK 4.05" ;
    vak:continues vak:VAK_4_04 ;
    vak:belongsTo karma:AbhidharmaKarmaSection ;
    vak:hasTopic karma:LevelSpecificGreatPrincipleSupport,
        karma:UncontaminatedAction,
        karma:NonAppropriatedAvijnapti .

karma:ContaminatedBodySpeechKarma
    logic:hasMaterialBasis karma:GreatPrinciplesOfSameLevel .

karma:UncontaminatedBodySpeechKarma
    logic:hasSoteriologicalStatus karma:WithoutOutflows ;
    logic:hasMaterialBasis karma:GreatPrinciplesOfPractitionerLevel ;
    logic:doesNotRequire karma:UncontaminatedGreatPrinciples .

karma:Avijnapti
    a karma:DerivedFormDetermination ;
    logic:hasAppropriationStatus karma:NonAppropriated .
```
