# VAK_2.31

## 1. Sanskrit (Devanāgarī)

> कौकृत्यमिद्धाकुशलान्याद्ये ध्याने न सन्त्यतः ।
>
> ध्यानान्तरे वितर्कश्च विचारश्चाप्यतः परम् ॥ २.३१ ॥

## 2. Sanskrit (IAST)

> kaukṛtyamiddhākuśalāny ādye dhyāne na santy ataḥ /
>
> dhyānāntare vitarkaś ca vicāraś cāpy ataḥ param // 2.31 //

## 3. Padaccheda

```text
kaukṛtyamiddhākuśalāny
                    → kaukṛtya-middha-akuśalāni
ādye                → ādye
dhyāne              → dhyāne
na santy            → na santi
ataḥ                → ataḥ
dhyānāntare         → dhyāna-antare
vitarkaś ca         → vitarkaḥ ca
vicāraś cāpy        → vicāraḥ ca api
ataḥ param          → ataḥ param
```

| Form | Morphology | Lexical force here |
|---|---|---|
| kaukṛtya | compound member | remorse |
| middha | compound member | sleepiness / torpor |
| akuśalāni | nominative neuter plural | unwholesome factors |
| ādye dhyāne | locative singular phrase | in the first dhyāna |
| na santi | third-person plural present with negation | are not present |
| ataḥ | indeclinable | from this / from the previously stated distribution |
| dhyāna-antare | locative singular compound | in the intermediate dhyāna |
| vitarkaḥ | nominative masculine singular | `vitarka` |
| vicāraḥ | nominative masculine singular | `vicāra` |
| api | additive particle | also; expanded by the Bhāṣya beyond the bare factor-list |
| ataḥ param | indeclinable phrase | beyond this |

`Dhyānāntara` is not merely “another dhyāna.” The Bhāṣya fixes it as the
intermediate level between the first and second dhyānas.

## 4. Grammar

The first exclusion rule is:

```text
ādye dhyāne
    → in the first dhyāna

kaukṛtya-middha-akuśalāni na santi
    → remorse, torpor, and unwholesome factors are absent
```

The Bhāṣya qualifies the last member carefully. No factor operates there in
an unwholesome determination. Yet crookedness, intoxication, and deception
are exceptions among the named affliction factors in that they may still
occur on the first-dhyāna level under the relevant non-unwholesome
classification.

The second rule is cumulative:

```text
dhyāna-antare
    → in the intermediate dhyāna

[the preceding exclusions] + vitarkaḥ na asti
    → vitarka is additionally absent
```

The third carries the exclusions higher:

```text
ataḥ param
    → beyond the intermediate dhyāna,
      in the second and subsequent dhyānas and the formless attainments

[the preceding exclusions] + vicāraḥ na asti
    → vicāra is additionally absent
```

The Bhāṣya reads `api` as also excluding deception and crookedness beyond the
intermediate level.

## 5. Translation

### Close syntactic construe

> Remorse, torpor, and unwholesome factors are not present in the first dhyāna. In the intermediate dhyāna, `vitarka` also [is absent]; beyond this, `vicāra` too.

### Bhāṣya-informed translation

> The first dhyāna excludes remorse, torpor, and factors operating as unwholesome, while retaining `vitarka` and `vicāra`. The intermediate dhyāna inherits those exclusions and additionally excludes `vitarka`, while `vicāra` remains. From the second dhyāna upward, including the formless attainments, `vicāra` is also absent; deception and crookedness no longer occur there either.

The first-dhyāna statement does not entail that every factor elsewhere named
an affliction is absent in every mode. The Bhāṣya preserves the limited
occurrence of crookedness, intoxication, and deception at that level.

## 6. Philosophical Translation

> A contemplative ground is defined partly by what can no longer occur within it. The movement upward is cumulative exclusion: remorse, torpor, and unwholesome operation fall away; then initiating engagement ceases while sustained examination remains; then sustained examination also ceases. Higher organization is not an additive inventory but a progressively constrained event-form.

Restrained Organon rendering:

> The bhūmi acts as a stage-indexed schema. Each transition inherits prior incompatibilities and adds new exclusions. State refinement is therefore monotonic with respect to forbidden factors, while the remaining factor-set must still be computed at each stage.

“Stage-indexed schema” and “monotonic” are project renderings. The textual
doctrine gives cumulative caitta exclusions across dhyāna levels.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination in this unit |
|---|---|---|
| ādya-dhyāna | first dhyāna | retains `vitarka` and `vicāra`; excludes remorse, torpor, and unwholesome operation |
| dhyānāntara | intermediate dhyāna | level between first and second dhyāna where `vitarka` has ceased but `vicāra` remains |
| ataḥ param | beyond this | second and subsequent dhyānas together with formless attainments in this rule |
| yathā-pratiṣiddham | according to what was previously excluded | Bhāṣya procedure carrying exclusions upward |
| vitarka | initiating engagement | function present in first dhyāna and absent in the intermediate dhyāna |
| vicāra | sustained examination | survives the intermediate level and ceases above it |
| śāṭhya | crookedness | limited through the Brahmā level; excluded higher |
| māyā | deception / false display | likewise explicitly excluded above the intermediate level |
| parṣat-sambandha | connection with an assembly | social condition used to explain the restricted range of crookedness |
| kṣepa | evasion / deflecting display | Brahmā's response when unable to answer Aśvajit's question |
| bhūmi | operative level | determines which consciousness-factor configurations remain possible |

The provisional functional renderings of `vitarka` and `vicāra` follow their
graded presence here. Their explicit definitional dispute belongs to later
verses and is not anticipated as settled.

## 8. Logical Determination

Let the first-stage exclusions be:

```text
E1 = {
    Remorse,
    Torpor,
    FactorsInUnwholesomeMode
}
```

Then:

```text
Stage = FirstDhyana
    → Excluded(Stage) ⊇ E1
    → Present(Vitarka)
    → Present(Vicara)
```

The intermediate stage inherits and extends:

```text
Stage = IntermediateDhyana
    → Excluded(Stage)
        = Excluded(FirstDhyana) ∪ {Vitarka}
    → Present(Vicara)
```

The higher stages inherit and extend again:

```text
Stage ∈ {SecondDhyanaAndAbove, FormlessAttainment}
    → Excluded(Stage)
        = Excluded(IntermediateDhyana)
          ∪ {Vicara, Deception, Crookedness}
```

The transition is monotonic in exclusions:

```text
Excluded(FirstDhyana)
    ⊂ Excluded(IntermediateDhyana)
    ⊂ Excluded(SecondDhyanaAndAbove)
```

The first-dhyāna qualification requires mode-aware membership:

```text
NamedAfflictionFactor(f)
    ⇏ AbsentAtFirstDhyana(f)

OperatesInUnwholesomeMode(f, FirstDhyana)
    → Absent(f, FirstDhyana)
```

Crookedness, intoxication, and deception are the Bhāṣya's exceptions to a
name-based exclusion of every factor elsewhere classified among afflictions.

## 9. Interpretive Note

VAK 2.31 converts the preceding event counts into a vertical bhūmi calculus.
The desire-realm profiles allowed various ethical types and optional factors.
The first dhyāna introduces exclusions; the intermediate dhyāna inherits them
and removes `vitarka`; the second and higher levels inherit those exclusions
and remove `vicāra` as well.

This is a strict temporal and stage schema:

```text
earlier configuration
    → inherited exclusions
    → additional incompatibility
    → later configuration
```

Yet the Bhāṣya refuses a simplistic ascent from “bad” to “good.” Crookedness,
intoxication, and deception can occur at the first-dhyāna/Brahmā level even
though unwholesome factors as such are excluded. Classification depends upon
mode, realm, and range, not upon carrying a name unchanged from the desire
realm.

The Brahmā narrative makes the point concrete. Aśvajit asks where the four
great elements cease without remainder. Brahmā does not know, but before his
assembly he evades the question by proclaiming himself Lord, Maker, Creator,
Fashioner, and Father of beings. Exalted rank and concentrated existence do
not entail knowledge. Public authority can become the condition for
crookedness precisely when ignorance is concealed by display.

The separation of `vitarka` and `vicāra` is equally exact. They cannot be
synonyms because one ceases at the intermediate level while the other
remains. Their different transition points prove functional discrimination
even before their later definitions are debated.

The Bhāṣya closes the inquiry with three indexed variables:

```text
on which bhūmi
in which citta
how many caittas
```

For the Kośa Technē, the restrained schema is:

```text
CaittaProfile<bhumi, citta, time>
    = inherited requirements
    − stage exclusions
    + event-local compatible factors
```

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_31
    a vak:Karika ;
    rdfs:label "VAK 2.31" ;
    vak:hasTopic vak:DhyanaStageCaittaExclusions ;
    vak:belongsTo vak:Indriyanirdesa .

vak:FirstDhyanaProfile
    vak:excludes vak:Remorse,
        vak:Torpor,
        vak:UnwholesomeOperation ;
    vak:retains vak:Vitarka,
        vak:Vicara .

vak:IntermediateDhyanaProfile
    vak:inheritsExclusionsFrom vak:FirstDhyanaProfile ;
    vak:excludes vak:Vitarka ;
    vak:retains vak:Vicara .

vak:HigherDhyanaProfile
    vak:inheritsExclusionsFrom vak:IntermediateDhyanaProfile ;
    vak:excludes vak:Vicara,
        vak:Deception,
        vak:Crookedness .

organon:StageIndexedCaittaSchema
    a organon:InterpretiveReconstruction ;
    organon:requires organon:InheritedExclusions,
        organon:StageSpecificExclusions,
        organon:ModeAwareMembership ;
    organon:inferredFrom vak:DhyanaStageCaittaExclusions .
```
