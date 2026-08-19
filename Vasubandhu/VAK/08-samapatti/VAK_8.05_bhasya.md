# VAK_8.05 — Bhāṣya

## Kārikā

> iti maulaṃ samāpattidravyam aṣṭavidhaṃ tridhā /
> sapta āsvādanavacchuddhānāsravāṇi aṣṭamaṃ dvidhā // VAK_8.05 //

**Best current translation:**  
Thus the fundamental body of meditative attainment is eightfold and classified threefold. Seven occur as savoring-associated, pure, and uncontaminated; the eighth occurs only in two modes.

**Kārikā analysis:** [`VAK_8.05.md`](./VAK_8.05.md)

## Bhāṣya Source

Pradhan 436|12–437|02.

```text
[436|12]
iti maulaṃ samāpattidravyamaṣṭavidhaṃ

[436|13-436|14]
ityetānyaṣṭau maulāni samāpattidravyāṇi yaduta catvāri dhyānāni catvāra ārupyā iti /

[436|14]
teṣāṃ punaḥ

[436|15]
tridhā /

[436|16]
sapta

[436|17]
bhavāgrādanyāni sapta trividhāni /

[436|18]
āsvādanāvacchūddhānāsravāṇi

[436|19]
āsvādanāsaṃprayuktāni śuddhakānyanāsravāṇi ca /

[437|01]
aṣṭamaṃ dvidhā // VAK_8.5 //

[437|02]
bhavāgramāsvādanāsaṃprayuktaṃ śuddhakaṃ ca /
anāsrava nāsti /
```

## Source Caution

The working e-text is based principally on Pradhan with corrections from Shastri and is not a critical edition. The transmitted spelling `āsvādanāvacchūddhānāsravāṇi` should be read through Vasubandhu's explicit prose unpacking as three distinct modes: `āsvādanāsaṃprayukta`, `śuddhaka`, and `anāsrava`.

The natural argument of VAK 8.05 ends at 437|02. The following prose begins the explanation of VAK 8.06 and should not be folded backward into this verse except where it clarifies terminology already named here.

## Natural Argument

**Voice: Vasubandhu**

The preceding verses have established the eight principal meditative attainments. Vasubandhu now gathers them explicitly as eight `maula samāpattidravyāṇi`: the four dhyānas and the four formless attainments.

This eightfold vertical classification is then crossed by a second, modal classification. Seven of the eight principal attainments can each occur in three ways:

```text
āsvādanāsaṃprayukta
    associated with savoring

śuddhaka
    pure

anāsrava
    uncontaminated
```

The exception is the eighth principal attainment, `bhavāgra`, the summit of existence. It is only twofold: it may be savoring-associated or pure, but no uncontaminated form of it exists.

The Bhāṣya therefore resolves the compressed `aṣṭamaṃ dvidhā` of the Kārikā directly:

```text
bhavāgra
    āsvādanāsaṃprayukta
    śuddhaka
    not anāsrava
```

## Argument Reconstruction

```text
principal samāpatti field
    four dhyānas
    + four ārūpyas
        = eight maula attainments

↓ modal cross-classification

first seven
    āsvādanāsaṃprayukta
    śuddhaka
    anāsrava

eighth = bhavāgra
    āsvādanāsaṃprayukta
    śuddhaka
    × anāsrava
```

The chapter therefore no longer presents a merely ascending series. Each level must now be determined both by its place in the attainment hierarchy and by the mode in which it occurs.

## New Technical Terms

- **bhavāgra** — the summit or peak of conditioned existence; here the eighth principal attainment, neither-perception-nor-non-perception
  - **status:** previously encountered in the Kārikās
  - **function:** identifies the exceptional member of the eightfold series

- **āsvādanāsaṃprayukta** — associated or conjoined with savoring/relish
  - **status:** prose expansion of the compressed Kārikā expression
  - **function:** first modal classification of samāpatti

- **śuddhaka** — pure attainment
  - **status:** prose technical form corresponding to Kārikā `śuddha`
  - **function:** second modal classification of samāpatti

## Doctrinal Determination

VAK 8.05 introduces an important distinction between **attainment-level** and **attainment-mode**.

```text
attainment-level
    answers: which samāpatti?

attainment-mode
    answers: in what qualitative/path condition does it occur?
```

The same principal meditative level can therefore be doctrinally different depending on whether it is joined with savoring, merely pure, or uncontaminated.

The exception of `bhavāgra` is decisive. The highest conditioned meditative attainment is not therefore the highest liberative attainment. Its very height within conditioned existence does not convert it into an uncontaminated state.

This blocks a simple equation:

```text
higher meditative level
    ≠ necessarily more liberative
```

The top of the conditioned hierarchy remains within the conditioned hierarchy.

## Translation Consequences

The first-pass translation of `aṣṭamaṃ dvidhā` can now be made explicit:

> The eighth, the summit of existence, is only twofold: savoring-associated and pure; it has no uncontaminated form.

`samāpattidravya` should continue to mean the determinate body or set of actual attainment-types, not a permanent substance.

The threefold classification should be rendered consistently as:

```text
āsvādanāsaṃprayukta
    savoring-associated

śuddhaka
    pure

anāsrava
    uncontaminated
```

## Logical Determination

The verse introduces a second classificatory axis across the already established eightfold field.

```text
Vertical determination
    level in the hierarchy

Modal determination
    manner in which that level is instantiated
```

This creates a matrix rather than a ladder.

The most important logical result is the non-equivalence of **maximal level** and **maximal path-status**:

```text
bhavāgra
    highest conditioned attainment

but

bhavāgra
    cannot be anāsrava
```

Thus quantitative or hierarchical superiority does not determine liberative quality.

A state can be maximally refined within one ordering while remaining excluded from another ordering altogether.

## Light Organon Contact

The immediate systems contact should remain restrained. VAK 8.05 shows that a state cannot be typed by one coordinate alone.

```text
SamapattiInstance {
    level
    mode
}
```

with a real constraint:

```text
if level == bhavāgra:
    mode ∈ {āsvādanāsaṃprayukta, śuddhaka}
    mode ≠ anāsrava
```

The conceptual lesson is doctrinally important before it is computationally interesting: **position in a hierarchy and path-value are independent determinations.**

This is especially important in a chapter on meditative attainment, because otherwise the vertical ascent could be mistaken for liberation itself.

## Commit History

```text
2026-08-19 — Initial Bhāṣya-pass analysis and stabilization of the threefold modal classification.
```
