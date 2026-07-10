# VAK_4.05 — Material Support and Non-Appropriation

## 1. Sanskrit — Devanāgarī

```sanskrit
स्वानि भूतान्युपादाय कायवाक्कर्म सास्रवम् ।
अनास्रवं यत्र जातोऽविज्ञप्तिरनुपात्तिका ॥
```

## 2. Sanskrit — IAST

```iast
svāni bhūtāny upādāya kāya-vāk-karma sāsravam |
anāsravaṃ yatra jāto ’vijñaptir anupāttikā ||
```

## 3. Source Caution

External source siglum: VAkK_4.5.

The transmitted `jātaḥ` appears masculine, while the most natural referent in the second pāda is neuter `anāsravam [karma]`. A normalized syntactic reading might expect `jātam`, or the commentary may supply a masculine referent.

The secure first-pass doctrinal structure is:

```text
sāsrava bodily and verbal karma
    depends upon its own great material determinations

anāsrava karma
    depends upon the great material determinations
    of the level where it arises

avijñapti
    is non-appropriated
```

The exact grammatical attachment of `yatra jātaḥ` remains open for the Bhāṣya pass.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Working determination |
|---|---|---|
| svāni bhūtāny | svāni bhūtāni | its own great material determinations |
| upādāya | upādāya | taking as basis; depending upon |
| kāya-vāk-karma | kāya-karma + vāk-karma | bodily and verbal karma |
| sāsravam | sa-āsravam | with influx; contaminated |
| anāsravam | an-āsravam | without influx; uncontaminated |
| yatra jātaḥ | yatra jātaḥ | arisen wherever / at whatever level |
| avijñaptiḥ | avijñaptiḥ | non-manifest action |
| anupāttikā | an-upāttikā | non-appropriated |

## 5. Grammar

### `svāni bhūtāny upādāya`

`upādāya` is an absolutive of `upa-ā-√dā`:

```text
taking up
taking as support
depending upon
```

Thus bodily and verbal karma do not arise independently. They arise supported by the great material determinations.

### `kāya-vāk-karma sāsravam`

The singular compound collects two modes:

```text
kāya-karma
vāk-karma
```

`Sāsrava` qualifies them as belonging to the contaminated field.

### `anāsravaṃ yatra jātaḥ`

The syntax is compressed. The intended contrast appears to be:

```text
sāsrava karma
    relies upon its own material determinants

anāsrava karma
    relies upon those of the level
    in which it arises
```

### `avijñaptir anupāttikā`

This is direct:

```text
avijñaptiḥ
    non-manifest action

anupāttikā
    non-appropriated
```

## 6. Literal Translation

Contaminated bodily and verbal karma arises taking its own great material determinations as basis. The uncontaminated [takes as basis those] belonging to wherever it arises. Non-manifest action is non-appropriated.

## 7. Philosophical Translation

Contaminated bodily and verbal action depends upon the great material determinations belonging to its own embodied continuum. Uncontaminated action depends upon the material basis of the level in which it arises. Non-manifest action itself is not appropriated as part of the living body.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| bhūta | great material determination | functional material basis, not merely element |
| upādāya | taking as basis | derivatively supported by |
| sāsrava | contaminated | belonging to the field in which influxes operate |
| anāsrava | uncontaminated | free from influx |
| upātta | appropriated | taken up into the living continuum |
| anupāttika | non-appropriated | not incorporated as living bodily matter |
| avijñapti | non-manifest action | materially grounded but not presently manifest |

## 9. Doctrinal Determination

VAK_4.04 established that avijñapti operates:

```text
kṣaṇād ūrdhvam
    beyond the initiating moment
```

VAK_4.05 now specifies its material relation:

```text
sāsrava bodily/verbal karma
    → depends upon its own great material determinations

anāsrava bodily/verbal karma
    → depends upon the material basis
      of the level where it arises

avijñapti
    → materially conditioned
    → non-appropriated
```

This prevents two reductions:

```text
avijñapti
    is not merely mental

avijñapti
    is not an ordinary part
    of the appropriated living body
```

## 10. Logical Determination

The verse distinguishes:

```text
action and material support
contaminated and uncontaminated action
materiality and appropriation
```

The crucial distinction is:

```text
material determination
    does not necessarily mean
    appropriated bodily matter
```

Thus avijñapti occupies an unusual position:

```text
generated from material conditions
classified with material form
not a perceptible bodily configuration
not appropriated into the sentient organism
```

## 11. Interpretive Note

The safest first-pass formulation is:

```text
avijñapti
    = non-manifest material action-determination
      not appropriated as living bodily matter
```

The paradoxical status should be preserved without forcing a deeper systematic identification.

## 12. Light Organon Interpretation

The text is constructing a mediation between:

```text
purely mental intention
purely observable physical deed
```

Avijñapti is:

```text
causally rooted in volition
materially supported
non-manifest
temporally subsequent
non-appropriated
```

It is therefore best treated at this stage as an effective determination rather than either a private mental state or a visible event.

## 13. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_05
    a vak:Karika ;
    rdfs:label "VAK 4.05" ;
    vak:continues vak:VAK_4_04 ;
    vak:hasTopic vak:MaterialSupport ;
    vak:hasTopic vak:SasravaKarma ;
    vak:hasTopic vak:AnasravaKarma ;
    vak:hasTopic vak:NonAppropriatedAvijnapti .

vak:SasravaBodySpeechKarma
    a vak:BodySpeechKarma ;
    vak:dependsUpon vak:OwnGreatMaterialDeterminations .

vak:AnasravaBodySpeechKarma
    a vak:BodySpeechKarma ;
    vak:dependsUpon vak:MaterialDeterminationsOfArisingLevel .

vak:Avijnapti
    a vak:NonManifestActionMode ;
    vak:hasMaterialStatus vak:DerivedMaterialDetermination ;
    vak:hasAppropriationStatus vak:NonAppropriated .
```

## 14. Verse Summary

```text
VAK_4.05

Contaminated bodily and verbal karma
    depends upon its own great material determinations.

Uncontaminated action
    depends upon the material basis
    of the level where it arises.

Avijñapti is non-appropriated.

Therefore:

non-manifest action is materially grounded
    without being an appropriated part
    of the living body.
```

## 15. Commit Note

Committed VAK_4.05.

Established:
- contaminated bodily and verbal karma depends on its own material basis.
- uncontaminated action depends on the basis of its level of arising.
- avijñapti is materially grounded yet non-appropriated.
- the grammar of `yatra jātaḥ` remains provisional pending the Bhāṣya pass.
