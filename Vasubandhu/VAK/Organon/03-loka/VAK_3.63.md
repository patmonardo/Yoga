# VAK_3.63

## 1. Sanskrit (Devanāgarī)

> परिषण्डाश्चतस्रोऽस्य दशसाहस्रिकान्तराः ।
>
> षोडशाष्टौ सहस्राणि चत्वारि द्वे च निर्गताः ॥ ३.६३ ॥

## 2. Sanskrit (IAST)

> pariṣaṇḍāś catasro 'sya daśasāhasrikāntarāḥ /
>
> ṣoḍaśāṣṭau sahasrāṇi catvāri dve ca nirgatāḥ // 3.63 //

## 3. Lexical Analysis

```text
pariṣaṇḍāḥ                 → pariṣaṇḍāś
catasraḥ                   → catasro
asya                       → 'sya
daśa-sāhasrika-antarāḥ     → daśasāhasrikāntarāḥ
ṣoḍaśa                     → ṣoḍaśa
aṣṭau                      → aṣṭau
sahasrāṇi                  → sahasrāṇi
catvāri                    → catvāri
dve                        → dve
ca                         → ca
nirgatāḥ                   → nirgatāḥ
```

| Form | Morphology | Lexical force here |
|---|---|---|
| pariṣaṇḍāḥ | nominative feminine plural | surrounding terraces or ledges |
| catasraḥ | nominative feminine plural numeral | four |
| asya | genitive masculine singular pronoun | of this, namely Sumeru |
| daśasāhasrikāntarāḥ | nominative feminine plural compound | separated by intervals of ten thousand |
| ṣoḍaśa | numeral | sixteen; with `sahasrāṇi`, sixteen thousand |
| aṣṭau | numeral | eight; with `sahasrāṇi`, eight thousand |
| sahasrāṇi | accusative neuter plural | thousands, measures of extent |
| catvāri | accusative neuter plural numeral | four thousand |
| dve | accusative neuter dual numeral | two thousand |
| nirgatāḥ | nominative feminine plural past participle of `nir-√gam` | gone or projected outward |

The feminine numeral `catasraḥ` and participle `nirgatāḥ` agree with the four
terraces. The unit `yojana` is supplied by the established cosmographical
context and made explicit in the Bhāṣya.

## 4. Grammar

The first half states the number of terraces and their vertical interval:

```text
asya [sumeroḥ]
    pariṣaṇḍāḥ catasraḥ
    daśa-sāhasrika-antarāḥ [santi]
```

> Of this [Sumeru] there are four terraces, each at a ten-thousand interval.

The second half distributes four measures across the terraces in their stated
order:

```text
[tāḥ yathāsaṃkhyam]
    ṣoḍaśa sahasrāṇi,
    aṣṭau sahasrāṇi,
    catvāri [sahasrāṇi],
    dve [sahasre]
    nirgatāḥ
```

The Bhāṣya supplies `yathāsaṃkhyam`, “respectively,” and makes the ellipsis of
the measure explicit. Thus the first terrace projects 16,000 yojanas, the
second 8,000, the third 4,000, and the fourth 2,000.

## 5. Translation

### Close syntactic construe

> This [Sumeru] has four terraces at intervals of ten thousand. They project
> outward sixteen thousand, eight thousand, four thousand, and two thousand
> [yojanas respectively].

### Bhāṣya-informed study translation

> Sumeru has four surrounding terraces. The first is reached after ascending
> 10,000 yojanas, and each succeeding terrace after another 10,000, so that the
> fourth stands at 40,000 yojanas and the four together occupy the lower half
> of Sumeru's 80,000-yojana height above the water. From the mountain they
> project outward respectively 16,000, 8,000, 4,000, and 2,000 yojanas.

The cumulative elevations, the lower-half determination, and the ordered
distribution of the outward measures are Bhāṣya determinations.

## 6. Philosophical Translation

> Sumeru is articulated as a graded domain by two coordinated but different
> laws. Elevation advances through equal additions; outward extent contracts
> by successive halves. The identity of a level is therefore not exhausted by
> one spatial quantity: each terrace has an ordinal position, a vertical
> address, and a determinate breadth. Before the inhabitants of these levels
> are introduced, the World System first establishes the ordered places and
> capacities in which they can be situated.

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this unit |
|---|---|---|
| Sumeru | Sumeru | central mountain whose emerged height is articulated |
| pariṣaṇḍā | surrounding terrace / ledge | one of four projected levels of Sumeru |
| antara | interval | constant vertical separation between successive terraces |
| daśasāhasrika | ten-thousandfold | measure governing each vertical step |
| udgamya | having risen / after ascending | Bhāṣya expression for reaching each level |
| nirgata | projected outward | horizontal extension from Sumeru |
| yathāsaṃkhyam | respectively / according to enumeration | binds each measure to its terrace in sequence |
| ākṣipta | occupied / taken up | Bhāṣya determination of the half-height covered by the terraces |
| ardha | half | 40,000 of Sumeru's 80,000 yojanas above the water |

## 8. Logical Determination

### Terrace coordinate table

Let `n` be the terrace ordinal, counted upward from the water-level base of
Sumeru:

| `n` | Elevation `H(n)` | Outward projection `P(n)` |
|---:|---:|---:|
| 1 | 10,000 yojanas | 16,000 yojanas |
| 2 | 20,000 yojanas | 8,000 yojanas |
| 3 | 30,000 yojanas | 4,000 yojanas |
| 4 | 40,000 yojanas | 2,000 yojanas |

### Two update laws

```text
vertical progression:
    H(n) = 10,000 × n
    H(n + 1) − H(n) = 10,000

horizontal progression:
    P(n) = 16,000 / 2^(n − 1)
    P(n + 1) = P(n) / 2
```

One axis is additive; the other is multiplicative. A single ordinal succession
therefore coordinates two non-identical transformations.

### Boundary determination

```text
emerged height of Sumeru = 80,000
elevation of fourth terrace = 40,000

40,000 / 80,000 = 1/2
```

The four-level terrace system articulates the lower half of the emerged
mountain. This is a bounded subsystem within Sumeru, not a complete division
of its height.

### Ordinal binding

```text
ordered terraces:
    T₁, T₂, T₃, T₄

ordered projections:
    16,000, 8,000, 4,000, 2,000

yathāsaṃkhyam:
    T₁ ↦ 16,000
    T₂ ↦ 8,000
    T₃ ↦ 4,000
    T₄ ↦ 2,000
```

The mapping depends upon sequence. Removing ordinal position would destroy
the information needed to assign the measures correctly.

## 9. Interpretive Note

VAK 3.63 changes scale without abandoning the method of the preceding
cosmography. The verse does not merely say that Sumeru has ledges. It provides
a compact generative specification:

```text
level count
    + constant vertical interval
    + ordered initial projection
    + recurrent halving
        → complete terrace geometry
```

The useful abstraction is an axis-coupled hierarchy. Successive levels share
one ordinal series, but that series controls elevation and breadth through
different rules. Consequently, “higher” does not mean “greater” in every
respect. Elevation increases while outward projection decreases. This is a
formal feature of the produced Loka described here, not a general judgment
about spiritual rank.

The verse also separates topology from population. VAK 3.63 defines the
available levels; the following verse assigns inhabitants to them. In the
Organon vocabulary, domain construction logically precedes Agent binding:

```text
graded places and capacities
    → possible locations for inhabitants
    → differentiated occupancy
```

This gives the Physical World an Agential relevance without reducing its
geometry to agency. A system must first provide discriminable positions and
constraints before an Agent can be located, related, or given a role within
it.

```ts
interface MeruTerrace {
  ordinal: 1 | 2 | 3 | 4;
  elevationYojanas: 10000 | 20000 | 30000 | 40000;
  outwardProjectionYojanas: 16000 | 8000 | 4000 | 2000;
}

const elevation = (ordinal: number) => 10_000 * ordinal;
const projection = (ordinal: number) => 16_000 / 2 ** (ordinal - 1);
```

This is explanatory project notation, not Vasubandhu's vocabulary. Its point
is to retain the distinction between a terrace's identity, its vertical
address, and its outward extent. VAK 3.64 can then add inhabitants without
rewriting the spatial schema.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .

vak:VAK_3_63
    a vak:Karika ;
    vak:describes loka:MeruTerraceSystem .

loka:MeruTerraceSystem
    loka:hasMember loka:Terrace1,
        loka:Terrace2,
        loka:Terrace3,
        loka:Terrace4 ;
    loka:hasVerticalIntervalYojanas 10000 ;
    loka:occupiesFractionOfEmergedMeru "1/2" .

loka:Terrace1
    loka:hasOrdinal 1 ;
    loka:hasElevationYojanas 10000 ;
    loka:hasOutwardProjectionYojanas 16000 .

loka:Terrace2
    loka:hasOrdinal 2 ;
    loka:hasElevationYojanas 20000 ;
    loka:hasOutwardProjectionYojanas 8000 .

loka:Terrace3
    loka:hasOrdinal 3 ;
    loka:hasElevationYojanas 30000 ;
    loka:hasOutwardProjectionYojanas 4000 .

loka:Terrace4
    loka:hasOrdinal 4 ;
    loka:hasElevationYojanas 40000 ;
    loka:hasOutwardProjectionYojanas 2000 .

organon:AxisCoupledHierarchy
    a organon:ProjectInterpretation ;
    organon:hasVerticalRule organon:ConstantAdditiveIncrease ;
    organon:hasHorizontalRule organon:SuccessiveHalving ;
    organon:preserves organon:OrdinalBinding .

organon:PreallocatedHabitationSchema
    a organon:ProjectInterpretation ;
    organon:requires organon:DomainConstruction ;
    organon:precedes organon:AgentBinding .
```
