# VAK_2.26 — Afflicted and Unwholesome Caitta Factors

## 1. Sanskrit — Devanāgarī

```text
मोहः प्रमादः कौशीद्यमाश्रद्धयं स्त्यानमुद्धवः ।
क्लिष्टे सदैव अकुशले त्वाह्रीक्यमनपत्रपा ॥ VAkK_2.26 ॥
```

## 2. Sanskrit — IAST

```text
mohaḥ pramādaḥ kauśīdyam āśraddhayaṃ styānam uddhavaḥ /
kliṣṭe sadaiva akuśale tv āhrīkyam anapatrapā // VAkK_2.26 //
```

Source form:

```text
mohaḥ pramādaḥ kauśīdyamāśraddhayaṃ styānamuddhavaḥ /
kliṣṭe sadaiva akuśale tvāhrīkyamanapatrapā // VAkK_2.26 //
```

Textual caution:

```text
The source form `āśraddhayaṃ` and `uddhavaḥ` should be checked later against the Bhāṣya and printed editions.
The present file preserves the source form while giving a kārikā-first analysis.
```

## 3. Padaccheda and Grammar

| Sanskrit | Padaccheda | Grammar | Working Sense |
|---|---|---|---|
| mohaḥ | mohaḥ | masculine nominative singular | delusion |
| pramādaḥ | pramādaḥ | masculine nominative singular | negligence / carelessness |
| kauśīdyam | kauśīdyam | neuter nominative singular | laziness / torpor of effort |
| āśraddhayam | āśraddhayam | neuter nominative singular, source form | lack of confidence / non-confidence |
| styānam | styānam | neuter nominative singular | mental sluggishness / rigidity |
| uddhavaḥ | uddhavaḥ | masculine nominative singular, source form | agitation / excitation; source form to verify |
| kliṣṭe | kliṣṭe | locative singular | in the afflicted |
| sadā eva | sadā eva | indeclinable phrase | always indeed |
| akuśale | akuśale | locative singular | in the unwholesome |
| tu | tu | particle | but / however |
| āhrīkyam | āhrīkyam | neuter nominative singular | lack of hrī; shamelessness |
| anapatrapā | an-apatrapā | feminine nominative singular | lack of moral regard |

## 4. Literal Translation

```text
Delusion, negligence, laziness, lack of confidence, sluggishness, and agitation
are always in the afflicted.

But in the unwholesome there are shamelessness and lack of moral regard.
```

## 5. Philosophical Translation

```text
Afflicted citta has its own necessary feature-set.
It is marked by delusion, negligence, weakness of effort, loss of confidence,
sluggishness, and disturbance.

When the citta is specifically unwholesome, the ethical restraints of hrī and apatrapā are absent.
```

## 6. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| moha | delusion | Basic obscuration |
| pramāda | negligence | Opposite of apramāda in VAK_2.25 |
| kauśīdya | laziness | Failure of energetic cultivation |
| āśraddhya / āśraddhaya | lack of confidence | Opposite of śraddhā |
| styāna | sluggishness | Mental rigidity or stagnation |
| uddhava / auddhatya? | agitation / excitation | Source form to be checked |
| kliṣṭa | afflicted | Defiled or disturbed by kleśa |
| akuśala | unwholesome | Ethically unskillful or harmful |
| āhrīkya | shamelessness | Absence of hrī |
| anapatrapā | lack of moral regard | Absence of apatrapā |

## 7. Logical Determination

VAK_2.26 gives the afflicted and unwholesome caitta classes.

The dominant protocol is Hypothetical Necessity:

```text
if citta is kliṣṭa,
then delusion and the afflicted feature-set are present.

if citta is akuśala,
then āhrīkya and anapatrapā are present.
```

The verse also establishes a contrast with VAK_2.25:

```text
kuśala citta
    = śraddhā + apramāda + hrī + apatrapā + vīrya ...

kliṣṭa / akuśala citta
    = moha + pramāda + āśraddhya + āhrīkya + anapatrapā ...
```

Thus the caitta taxonomy is not a flat list. It is a disjunctive ethical feature-model.

```text
wholesome
    vs
afflicted
    vs
unwholesome
```

## 8. Relation to Indriya

Indriyas govern the availability of experience. Caittas determine the functional quality of the citta-field receiving and organizing that availability.

```text
Indriya
    = faculty-givenness

Caitta
    = qualitative feature-function of the mental field
```

Afflicted caittas show how the instrument becomes distorted:

```text
indriya-givenness
    may be taken up by citta
    through delusion, negligence, sluggishness, or agitation.
```

So the caitta model is necessary for learning because it explains not only correct functioning, but malfunction.

## 9. Organon Interpretation

Organon reading:

```text
AfflictedCaittaFeatureSet
    = distortion model of Agent-side operation
```

Dataset schema:

```text
KliṣṭaCitta:
    hasDelusion
    hasNegligence
    hasLaziness
    hasNonConfidence
    hasSluggishness
    hasAgitation

AkuśalaCitta:
    hasShamelessness
    hasLackOfMoralRegard
```

Learning implication:

```text
Learning requires a diagnostic model of distortion.

The Agent must know not only what features support knowledge,
but what features deform the field of knowledge.
```

## 10. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:AfflictedCaitta a rdfs:Class ;
    rdfs:subClassOf vak:Caitta ;
    rdfs:label "afflicted caitta" ;
    rdfs:comment "A caitta always present in afflicted citta." .

vak:UnwholesomeCaitta a rdfs:Class ;
    rdfs:subClassOf vak:Caitta ;
    rdfs:label "unwholesome caitta" ;
    rdfs:comment "A caitta present in unwholesome citta." .

vak:Moha a vak:AfflictedCaitta .
vak:Pramāda a vak:AfflictedCaitta .
vak:Kauśīdya a vak:AfflictedCaitta .
vak:Āśraddhya a vak:AfflictedCaitta .
vak:Styāna a vak:AfflictedCaitta .
vak:Uddhava a vak:AfflictedCaitta .
vak:Āhrīkya a vak:UnwholesomeCaitta .
vak:Anapatrapā a vak:UnwholesomeCaitta .
```

## 11. Commit History

```text
VAK_2.26 opened.
Method: kārikā-first speculative seed.
Theme: afflicted and unwholesome caittas.
Logical protocols recorded: hypothetical necessity and disjunctive ethical feature-model.
Textual caution recorded for source forms āśraddhayaṃ and uddhavaḥ.
Relation to indriya tracked: caittas as distortion or modulation of faculty-givenness in citta.
Zero-padded file naming maintained: VAK_2.26.
```
