# VAkK 8.20

## Sanskrit

आर्याकिञ्चन्यसांमुख्याद् भवाग्रे त्वास्रवक्षयः ।
सतृष्णाः स्वभवालम्बाः ध्यानं षड्विषयं शुभम् ॥ VAkK_8.20 ॥

## IAST

āryākiṃcanyasāṃmukhyād bhavāgre tv āsravakṣayaḥ /
satṛṣṇāḥ svabhavālambāḥ dhyānaṃ ṣaḍviṣayaṃ śubham // VAkK_8.20 //

## Source Caution

The source file reads `sadviṣayaṃ`; this is normalized here to `ṣaḍviṣayaṃ`, “having six objects,” which is required by the doctrine and syntax.

## Padaccheda

- ārya-ākiṃcanya-sāṃmukhyāt
- bhava-agre
- tu
- āsrava-kṣayaḥ
- sa-tṛṣṇāḥ
- sva-bhava-ālambāḥ
- dhyānam
- ṣaṭ-viṣayam
- śubham

## Grammar

- **āryākiṃcanyasāṃmukhyāt** — ablative singular compound, “from the direct presence of the noble [attainment] of nothingness.”
- **bhavāgre** — locative singular, “at the summit of existence,” i.e. the sphere of neither-perception-nor-non-perception.
- **āsravakṣayaḥ** — nominative singular, “destruction of the outflows.”
- **satṛṣṇāḥ** — nominative plural, “those accompanied by craving.”
- **svabhavālambāḥ** — nominative plural, “taking their own existence as object.”
- **dhyānam** — nominative singular neuter, “dhyāna.”
- **ṣaḍviṣayam** — nominative singular neuter, “having six object-fields.”
- **śubham** — nominative singular neuter, “wholesome.”

## Literal Translation

At the summit of existence, the destruction of the outflows occurs through the direct presence of the noble attainment of nothingness. Attainments accompanied by craving take their own existence as object; wholesome dhyāna has six object-fields.

## Philosophical Translation

The highest conditioned station does not itself supply the decisive liberating cognition. At the summit of existence, the outflows are destroyed through the noble attainment of nothingness brought directly to bear. Craving-associated attainments remain reflexively enclosed within their own mode of existence, whereas wholesome dhyāna can range across all six classes of objects.

## Technical Vocabulary

- **ārya** — noble; here, supramundane.
- **ākiṃcanya** — nothingness; the third formless attainment.
- **sāṃmukhya** — direct presence, immediate confrontation, bringing into direct application.
- **bhavāgra** — summit of existence; the highest conditioned sphere.
- **āsravakṣaya** — destruction of the outflows.
- **satṛṣṇa** — accompanied by craving.
- **svabhavālambana** — taking one’s own existence or own level as object.
- **ṣaḍviṣaya** — having six classes of objects.

## Doctrinal Determination

This verse makes three determinations.

1. The summit of existence is not by itself liberating. The destruction of the outflows there depends on the noble attainment of nothingness being made directly present.
2. Craving-associated attainments are self-enclosed: they take the existence to which they belong as their object.
3. Wholesome dhyāna has a broader cognitive range and may take six kinds of objects.

The highest conditioned level therefore still depends on a lower but noble attainment for liberation. Cosmological height and liberating efficacy are not identical.

## Logical Determination

The verse distinguishes rank from function.

```text
highest conditioned level
    does not by itself destroy the outflows

noble nothingness-attainment
    supplies the decisive liberating confrontation
```

It also distinguishes two object-relations:

```text
craving-associated attainment
    → reflexively bound to its own existence

wholesome dhyāna
    → cognitively ranges across six object-fields
```

Thus, an attainment is determined not only by its level and purity, but by the range and direction of its intentional field.

## Organon Light

This is a precise instance of qualitative mastery over hierarchy.

The supreme conditioned station is not automatically the supreme cognitive power. A lower determination may possess the function required to liberate the higher one. The system therefore cannot be read as a simple ladder in which every higher level contains every lower capacity in a superior form.

The craving-associated state is closed within its own given existence. Wholesome dhyāna, by contrast, has the freedom to range across a wider field. The distinction is between self-enclosed being and cognitively mobile apprehension.

## OWL++ Seed

```text
Class: SummitOfExistence
Class: NobleNothingnessAttainment
Class: CravingAssociatedAttainment
Class: WholesomeDhyana
Class: OutflowDestruction

ObjectProperty: directlySupports
ObjectProperty: takesAsObject
ObjectProperty: hasObjectRange

Rule:
NobleNothingnessAttainment
    directlySupports OutflowDestruction
    at SummitOfExistence.

Rule:
CravingAssociatedAttainment
    takesAsObject its own existence.

Rule:
WholesomeDhyana
    hasObjectRange six object-fields.
```

## Commit History

- Initial Sanskrit-first analysis of VAkK 8.20.