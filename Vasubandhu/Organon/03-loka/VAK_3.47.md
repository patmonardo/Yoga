# VAK_3.47

## 1. Sanskrit (Devanāgarī)

> तिर्यक् त्रीणि सहस्राणि सार्धं शतचतुष्टयम् ।
>
> लक्षद्वादशकं चैव जलकाञ्चनमण्डलम् ॥ ३.४७ ॥

## 2. Sanskrit (IAST)

> tiryak trīṇi sahasrāṇi sārdhaṃ śatacatuṣṭayam /
>
> lakṣadvādaśakaṃ caiva jalakāñcanamaṇḍalam // 3.47 //

## 3. Lexical Analysis

```text
tiryak                       → tiryak
trīṇi                        → trīṇi
sahasrāṇi                    → sahasrāṇi
sa-ardham                    → sārdham
śata-catuṣṭayam              → śatacatuṣṭayam
lakṣa-dvādaśakam             → lakṣadvādaśakam
ca eva                       → caiva
jala-kāñcana-maṇḍalam        → jalakāñcanamaṇḍalam
```

| Form | Morphology | Lexical force here |
|---|---|---|
| tiryak | indeclinable | transversely, laterally, across |
| trīṇi sahasrāṇi | neuter plural numerical phrase | three thousand |
| sārdham | indeclinable numerical qualifier | with a half; here a half-hundred |
| śatacatuṣṭayam | neuter singular numerical expression | a group of four hundreds |
| lakṣadvādaśakam | neuter singular numerical compound | twelve hundred-thousands |
| ca eva | conjunction plus emphatic particle | and indeed; and precisely |
| jalakāñcanamaṇḍalam | neuter singular compound | the water-and-gold maṇḍala system |

`Sārdhaṃ śatacatuṣṭayam` denotes four hundred plus half of a hundred, or 450.
The complete transverse measure is therefore 1,203,450 yojanas.

## 4. Grammar

The measured subject is `jalakāñcanamaṇḍalam`; its copula and unit are supplied
from context:

```text
jalakāñcanamaṇḍalam
    tiryak
    lakṣa-dvādaśakam
    trīṇi sahasrāṇi
    sārdhaṃ śata-catuṣṭayam ca eva
    [yojanānām asti]

the water-and-gold maṇḍala
    transversely
    [measures] twelve lakṣas,
    three thousand,
    and precisely four hundred and fifty
    [yojanas]
```

The Bhāṣya states that `ubhayam`, both the water and gold domains, are equal in
`vistāra`, breadth. Thus the compound does not designate a third substance; it
collects two vertically differentiated domains under one shared transverse
measure.

## 5. Translation

### Close syntactic construe

> The water-and-gold maṇḍala extends transversely twelve hundred-thousands,
> three thousand, and four hundred and fifty [yojanas].

### Bhāṣya-informed study translation

> The water-maṇḍala and golden-earth maṇḍala have the same horizontal extent:
> each measures 1,203,450 yojanas across.

Their equality in breadth, the supplied yojana unit, and the distributive
application of the one measure to both domains are Bhāṣya determinations.

## 6. Philosophical Translation

> The two support-domains distinguished vertically in 3.46 are now unified
> horizontally. Water remains below and golden earth above, yet both occupy one
> transverse world-field. Difference of function and depth therefore coexists
> with equality of breadth. The Physical World acquires determinate extension
> through coordinated measures rather than through an undifferentiated notion
> of vastness.

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this unit |
|---|---|---|
| tiryak | transversely / laterally | axis of measure distinguished from vertical depth |
| vistāra | breadth / extent | Bhāṣya gloss for the transverse measure |
| jala-maṇḍala | water-maṇḍala | lower domain retaining 320,000 yojanas of depth |
| kāñcana-maṇḍala | golden-earth maṇḍala | upper transformed domain 800,000 yojanas deep |
| jala-kāñcana-maṇḍala | water-and-gold maṇḍala system | the two domains considered under their equal breadth |
| lakṣa | hundred-thousand | largest unit in the stated transverse measure |
| sahasra | thousand | intermediate unit in the stated measure |
| śata | hundred | smallest unit explicitly grouped in the measure |
| sārdha | with a half | adds half a hundred to four hundreds |
| parikṣepa | circumference / encircling measure | Bhāṣya term explaining the opening of 3.48, not wording of 3.47 |

The dimensional matrix across 3.46–3.47 is:

```text
                       vertical depth       transverse extent
water-maṇḍala            320,000               1,203,450
golden-earth maṇḍala     800,000               1,203,450
```

## 8. Logical Determination

### Vertical difference and horizontal equality

```text
water-domain ≠ gold-domain
    with respect to substance, genesis, position, and depth

water-domain = gold-domain
    with respect to transverse extent
```

Equality is indexed to a dimension. It does not erase the determinations by
which the two domains differ.

### From generated layer to measured field

```text
formation and transformation in 3.46
    → vertically differentiated supports
        → one equal horizontal extent in 3.47
```

The result is an articulated field capable of receiving further placements.
Measure here is constitutive of the cosmological model: it specifies the
relations within which mountains, seas, and inhabited regions will be located.

### Arithmetic determination

```text
12 × 100,000
    + 3 × 1,000
    + 4 × 100
    + 1/2 × 100
        = 1,203,450 yojanas
```

The compound numerical expression is additive, not a set of alternative
measurements.

### Boundary with 3.48

The Bhāṣya immediately explains the next words, `samantatas tu triguṇam`, as a
circumference three times the transverse measure. Those words belong to 3.48.
For 3.47 the warranted result is only the equal breadth of the two maṇḍalas;
the circumferential operation is a forward link, not part of this Kārikā.

## 9. Interpretive Note

VAK 3.47 is austere but methodologically revealing. Once the Kośa has generated
the water and golden-earth domains, it does not rush immediately to populated
geography. It first fixes their shared extension. The container must become a
measured field before determinate locations can be distributed within it.

The most useful abstraction is not merely “breadth follows height.” It is that
one structured whole can sustain different relations along different axes:

```text
vertical axis
    → difference, layering, support

horizontal axis
    → equality, coextension, common field
```

This is a genuine semantic discrimination. Saying that water and gold are
“equal” without supplying the axis would be false; saying only that they are
“different” would miss their common spatial domain. The proposition becomes
true through the relation under which its terms are compared.

For the Organon projection:

```ts
interface DimensionedSupportDomain {
  domain: "water" | "golden-earth";
  verticalDepthYojanas: number;
  transverseExtentYojanas: 1_203_450;
}
```

This is explanatory notation, not Vasubandhu's terminology. It preserves the
important fact that a single entity may participate in several measures and
that comparison requires an explicitly selected dimension.

The verse therefore contributes a modest but durable World-System principle:
configuration becomes intelligible when heterogeneous domains are related by
shared coordinates without having their differences flattened.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .

vak:VAK_3_47
    a vak:Karika ;
    vak:continues vak:ContainerWorldAccount ;
    vak:measures loka:WaterMandala,
        loka:GoldenEarth ;
    vak:hasMeasurementAxis loka:TransverseAxis .

loka:WaterMandala
    loka:hasVerticalDepthYojanas 320000 ;
    loka:hasTransverseExtentYojanas 1203450 .

loka:GoldenEarth
    loka:hasVerticalDepthYojanas 800000 ;
    loka:hasTransverseExtentYojanas 1203450 .

loka:WaterMandala
    loka:isCoextensiveWith loka:GoldenEarth .

organon:DimensionIndexedComparison
    a organon:ProjectInterpretation ;
    organon:preserves organon:VerticalDifference,
        organon:HorizontalEquality ;
    organon:requires organon:ExplicitComparisonRelation .
```
