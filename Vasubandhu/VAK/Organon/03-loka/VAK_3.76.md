# VAK_3.76

## 1. Sanskrit (Devanāgarī)

> पादवृद्ध्या तनुर्यावत्सार्धक्रोशो दिवौकसाम् ।
>
> कामिनां रूपिणां त्वादौ योजनार्धं ततः परम् ॥ ३.७६ ॥

## 2. Sanskrit (IAST)

> pādavṛddhyā tanur yāvat sārdhakrośo divaukasām /
>
> kāmināṃ rūpiṇāṃ tv ādau yojanārdhaṃ tataḥ param // 3.76 //

The form `pādavṛddhyā` is adopted here: an increase by one quarter. It is the
reading required by both the construction and the exact series supplied by
the Bhāṣya.

## 3. Lexical Analysis

```text
pāda-vṛddhyā      → pādavṛddhyā
tanuḥ             → tanur (before y-)
yāvat             → yāvat
sa-ardha-krośaḥ   → sārdhakrośaḥ
diva-okasām       → divaukasām
kāminām           → kāmināṃ
rūpiṇām           → rūpiṇāṃ
tu                → tv (before ā-)
ādau              → ādau
yojana-ardham     → yojanārdham
tataḥ             → tataḥ
param             → param
```

| Form | Morphology | Lexical force here |
|---|---|---|
| pādavṛddhyā | instrumental feminine singular compound | by an increase of one quarter of a krośa at each step |
| tanuḥ | nominative feminine singular | body; bodily stature |
| yāvat | indeclinable | up to, as far as |
| sārdhakrośaḥ | nominative masculine singular used predicatively with measure | one and one-half krośas |
| divaukasām | genitive masculine plural compound | of the heaven-dwellers |
| kāminām | genitive masculine plural | belonging to the desire realm; enjoying sense desire |
| rūpiṇām | genitive masculine plural | of those belonging to the form realm |
| tu | particle | but; marks the change of domain and rule |
| ādau | locative masculine singular | at the beginning; in the first station |
| yojanārdham | nominative or accusative neuter singular measure expression | half a yojana |
| tataḥ param | adverbial sequence | beyond that; thereafter |

`pāda` is resolved by the Bhāṣya as one fourth of a krośa. `ādau` is likewise
made exact there: it refers to the Brahmakāyika devas, the first form-realm
station in this measurement series.

## 4. Grammar

The first construction concerns only the desire-realm heaven-dwellers:

```text
kāmināṃ divaukasām
    tanuḥ
    pāda-vṛddhyā
    yāvat sārdha-krośaḥ [bhavati]
```

> The body of the desire-realm heaven-dwellers increases by one quarter at a
> time, up to one and one-half krośas.

The genitives `divaukasām kāminām` belong together. The Bhāṣya distributes
the successive quarter-krośa increments across the six classes of desire-realm
devas.

The second construction changes the domain:

```text
rūpiṇāṃ tu
    ādau
    yojana-ardhaṃ [tanuḥ]
    tataḥ param [vardhate]
```

> But among the form-realm devas, at the beginning the body is half a yojana;
> beyond that, it increases further.

The particle `tu` is structurally decisive. It prevents `yojanārdham` from
being read as another member of the preceding quarter-krośa progression.
`tataḥ param` announces a continuation whose determinate series is supplied
in VAK 3.77.

## 5. Translation

### Close syntactic construe

> Among the desire-realm heaven-dwellers, bodily stature increases by a
> quarter, up to one and one-half krośas. But for the form-realm devas, at the
> beginning it is half a yojana; beyond that, it is greater.

### Bhāṣya-informed study translation

> The bodies of the six classes of desire-realm devas measure successively
> one quarter, one half, three quarters, one, one and one-quarter, and one and
> one-half krośas. At the first form-realm station, that of the Brahmakāyikas,
> the body measures half a yojana; the measures beyond that are taken up next.

The identity of the six classes, their exact distribution, and the
identification of the first form-realm station are Bhāṣya determinations.

## 6. Philosophical Translation

> Celestial embodiment is not left as an indefinite magnificence. Within the
> desire realm it is generated as an exact ordered series: station determines
> bodily measure by a constant increment. At the boundary of the form realm,
> however, the World System changes its measuring schema. A new domain begins
> from a new base value in a new unit, and its further law is explicitly
> deferred. Hierarchical ascent is therefore represented not by one vague
> scale but by domain-indexed rules of embodiment.

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this unit |
|---|---|---|
| tanu | body / bodily stature | the magnitude being measured |
| divaukas | heaven-dweller | celestial inhabitant whose body remains quantitatively determined |
| kāmin | desire-realm being | scopes the six deva classes governed by the quarter-krośa series |
| rūpin | form-realm being | begins a distinct celestial measurement domain |
| pāda | quarter of a krośa | constant increment of the desire-realm series |
| vṛddhi | increase | ordered addition from one deva class to the next |
| krośa | krośa | unit used for the desire-realm deva measures |
| yojana | yojana | unit introduced at the form-realm boundary |
| sārdha | with a half added | fixes the upper desire-realm value at 1½ krośas |
| Brahmakāyika | Brahmakāyika deva | first form-realm station; body of ½ yojana |
| ādau | at the beginning | selects the base case of the form-realm series |
| tataḥ param | beyond that / thereafter | continuation pointer to the subsequent measures |

## 8. Logical Determination

### Desire-realm additive series

Let `n` be the ordinal position of a desire-realm deva class, from 1 through
6. The Bhāṣya makes the rule exact:

```text
KāmaDevaMeasure(n) = n × ¼ krośa
```

| n | Deva class | Body measure |
|---:|---|---:|
| 1 | Cāturmahārājakāyika | ¼ krośa |
| 2 | Trāyastriṃśa | ½ krośa |
| 3 | Yāma | ¾ krośa |
| 4 | Tuṣita | 1 krośa |
| 5 | Nirmāṇarati | 1¼ krośas |
| 6 | Paranirmitavaśavartin | 1½ krośas |

This is addition by a constant difference, not multiplication by a constant
ratio:

```text
Mₙ₊₁ = Mₙ + ¼ krośa
```

### Domain transition

```text
desire realm:
    unit       = krośa
    base       = ¼ krośa
    update     = add ¼ krośa
    members    = six deva classes

form realm:
    first      = Brahmakāyika
    unit       = yojana
    base       = ½ yojana
    update     = deferred to VAK 3.77
```

The verse changes both domain and unit. It does not itself state a conversion
between krośa and yojana, so no numerical ratio between the final desire-realm
measure and the first form-realm measure should be inferred here.

### Rule boundary

The syntax encodes a disciplined handoff:

```text
pādavṛddhyā ... kāminām
    → closes one complete recurrence

rūpiṇāṃ tu ādau yojanārdham
    → declares a new base case

tataḥ param
    → points forward without yet supplying the new recurrence
```

Thus the verse gives a complete rule for one domain and only the initialization
of the next.

## 9. Interpretive Note

VAK 3.76 continues the contraction of scale begun in 3.75. After measuring
human bodies by continent, the analysis measures celestial bodies by station.
The methodological continuity is more important than the spectacle of a
procession of gods:

```text
domain classification
    → ordered station
        → applicable measurement schema
            → determinate embodiment
```

The useful abstraction is **class-conditioned bodily magnitude**. A body is
not assigned an arbitrary celestial size; its measure follows from its place
in an ordered domain. Yet the World System does not impose one universal
formula. Crossing from desire to form changes the base, the unit, and—pending
3.77—the recurrence.

The semantic–syntactic discrimination matters at exactly this boundary.
Syntactically, the verse is compact enough to look like one uninterrupted
increase. Semantically, `kāminām` closes the first scope and `rūpiṇāṃ tu`
opens another. The copular force of the omitted `is` accordingly relates two
different kinds of subjects to two different measurement schemas. The same
predicate—bodily measure—does not entail the same rule of determination.

```ts
type KamaDevaOrdinal = 1 | 2 | 3 | 4 | 5 | 6;

interface KamaDevaBodyMeasure {
  classOrdinal: KamaDevaOrdinal;
  unit: "QuarterKrosa";
  magnitude: KamaDevaOrdinal;
}

interface RupaDevaBodyMeasureBase {
  station: "Brahmakayika";
  unit: "Yojana";
  magnitude: 0.5;
  continuation: "VAK_3_77";
}
```

This is explanatory project notation, not Vasubandhu's terminology. Its value
is that it forbids a consumer from applying the completed desire-realm update
rule to the newly initialized form-realm domain.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .

vak:VAK_3_76
    a vak:Karika ;
    vak:continues vak:VAK_3_75 ;
    vak:describes loka:KamaDevaBodyMeasureSeries,
                  loka:RupaDevaBodyMeasureBase ;
    vak:continuedBy vak:VAK_3_77 .

loka:KamaDevaBodyMeasureSeries
    a organon:AdditiveSeries ;
    organon:hasDomain loka:DesireRealmDevas ;
    organon:hasUnit loka:QuarterKrosa ;
    organon:hasInitialMagnitude 1 ;
    organon:hasIncrement 1 ;
    organon:hasTerminalMagnitude 6 .

loka:CaturmaharajakayikaBody
    organon:hasMagnitudeInQuarterKrosas 1 .

loka:TrayastrmsaBody
    organon:hasMagnitudeInQuarterKrosas 2 .

loka:YamaBody
    organon:hasMagnitudeInQuarterKrosas 3 .

loka:TusitaBody
    organon:hasMagnitudeInQuarterKrosas 4 .

loka:NirmanaratiBody
    organon:hasMagnitudeInQuarterKrosas 5 .

loka:ParanirmitavasavartinBody
    organon:hasMagnitudeInQuarterKrosas 6 .

loka:RupaDevaBodyMeasureBase
    a organon:SeriesInitialization ;
    organon:hasDomain loka:FormRealmDevas ;
    organon:hasFirstStation loka:Brahmakayika ;
    organon:hasUnit loka:Yojana ;
    organon:hasInitialMagnitude 0.5 ;
    organon:hasDeferredRule vak:VAK_3_77 .

loka:DesireToFormMeasurementTransition
    a organon:DomainTransition ;
    organon:fromSchema loka:KamaDevaBodyMeasureSeries ;
    organon:toSchema loka:RupaDevaBodyMeasureBase ;
    organon:changesUnit true ;
    organon:doesNotAssertUnitConversion true .
```
