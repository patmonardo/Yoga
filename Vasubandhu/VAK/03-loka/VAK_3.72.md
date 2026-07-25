# VAK_3.72 — Deva-World Ascent: Visibility Limits Between Worlds

## 1. Sanskrit — Devanāgarī

```sanskrit
स्थानात् स्थानादधो यावत्तावदूर्ध्वं ततस्ततः ।
नोर्ध्वदर्शनमस्त्येषामन्यत्रर्द्धिपराश्रयात् ॥ VAkK_3.72 ॥
```

## 2. Sanskrit — IAST

```iast
sthānāt sthānād adho yāvat tāvad ūrdhvaṃ tatas tataḥ /
nordhva-darśanam asty eṣām anyatrarddhi-parāśrayāt // VAkK_3.72 //
```

## 3. Source Caution

The source reading is:

```iast
sthānāt sthānadadho yāvattāvadūrdhvaṃ tatastataḥ /
nordhva darśanamastyeṣāmanyatrarddhiparāśrayāt // VAkK_3.72 //
```

Sandhi has been lightly separated:

```iast
sthānāt sthānāt adhaḥ yāvat tāvat ūrdhvam tataḥ tataḥ /
na ūrdhva-darśanam asti eṣām anyatra ṛddhi-para-āśrayāt //
```

The source has `ṛddhi` in sandhi as `rddhi`. The compound `ṛddhi-para-āśraya` is provisionally read as “through supernormal power or reliance on another.” This should be checked against the bhāṣya.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| sthānāt sthānāt | sthānāt sthānāt | from each station / level |
| adhaḥ | adhaḥ | downward, below |
| yāvat | yāvat | as far as |
| tāvat | tāvat | so far, to that extent |
| ūrdhvam | ūrdhvam | upward, above |
| tataḥ tataḥ | tataḥ tataḥ | from each corresponding point; from there and there |
| na | na | not |
| ūrdhva-darśanam | ūrdhva-darśanam | seeing upward, upward vision |
| asti | asti | there is |
| eṣām | eṣām | for these beings |
| anyatra | anyatra | except, apart from |
| ṛddhi | ṛddhi | supernormal power, accomplishment |
| para-āśrayāt | para-āśrayāt | through reliance on another |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| sthānāt sthānāt | ablative singular repeated | from each station or level |
| adhaḥ yāvat | adverbial phrase | as far downward as |
| tāvat ūrdhvam | correlative phrase | so far upward |
| tataḥ tataḥ | repeated ablative/adverbial | from each level in turn |
| na ūrdhva-darśanam asti | negative existential clause | there is no seeing upward |
| eṣām | genitive plural | for these beings |
| anyatra | indeclinable | except, apart from |
| ṛddhi-para-āśrayāt | ablative compound | from/through supernormal power or reliance on another |

## 6. Literal Translation

From each station, as far downward as there is vision, so far upward from each lower station there is not vision for these beings, except through ṛddhi or reliance on another.

## 7. Philosophical Translation

Each world-level has a limited range of vision. Beings may see downward within the range proper to their station, but they do not see upward into higher stations except by supernormal power or by depending on another.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| sthāna | station / level | determinate world-position or existential level |
| adhaḥ | downward | lower range of visibility |
| ūrdhva | upward | higher range of visibility |
| darśana | seeing / vision | perceptual access to a world-level |
| ūrdhva-darśana | upward vision | seeing into higher levels |
| eṣām | of these beings | beings located within these world-levels |
| ṛddhi | supernormal power / accomplishment | exceptional capacity extending visibility |
| para-āśraya | reliance on another | dependent access mediated by another being |

## 9. Doctrinal Determination

VAkK_3.71 classified birth as arising into determinate experiential territories: kāma-upapatti and sukha-upapatti. VAkK_3.72 now gives the visibility-rule of those territories.

```text
world-station
    → downward visibility
    → no upward visibility
    → exception: ṛddhi or reliance on another
```

This is a crucial rule for the devic Dhyāna Path: higher territories are not automatically visible from lower ones.

## 10. Logical Determination

This verse introduces the asymmetry of standpoint.

```text
higher station
    can see downward

lower station
    cannot see upward
        except by exceptional mediation
```

A territory is therefore not merely a place of birth. It determines the range of what can appear to the observer.

## 11. Interpretive Note

This verse strongly supports the `draṣṭṛ / madhya / territory` control.

```text
draṣṭṛ
    observes from a station

sthāna
    determines the observable territory

madhya
    mediates observer and field

Discriminator
    determines whether the visible territory is Path or not-Path
```

The absence of upward vision is especially important. A being may inhabit a refined territory and still lack access to what is higher. This prevents the mistake of identifying one’s present field of refinement with final truth.

## 12. Organon Interpretation

Light contact point:

```text
Every standpoint has a visibility horizon.
```

The deva-world and dhyāna-world classifications now become epistemological as well as cosmological. Birth into a field determines not only what one enjoys, but what one can see. Upward access requires mediation: ṛddhi or dependence on another.

This is why the Path-Discriminator is essential. It is not enough to occupy a refined world-field. One must discriminate the limit of the standpoint itself.

## 13. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_72
    a vak:Karika ;
    rdfs:label "VAK 3.72" ;
    vak:sourceReference "VAkK_3.72" ;
    vak:continues vak:VAK_3_71 ;
    vak:hasTopic vak:VisibilityHorizon ;
    vak:hasTopic vak:UpwardVisionLimit ;
    vak:belongsTo vak:DevaWorldAscentBlock .

vak:VisibilityHorizon
    a logic:StandpointLimit ;
    rdfs:label "visibility horizon of a world-station" ;
    vak:determinedBy vak:Sthana ;
    vak:permits vak:DownwardVision ;
    vak:limits vak:UpwardVision .

vak:UpwardVisionLimit
    a logic:EpistemicLimit ;
    rdfs:label "absence of upward vision except by mediation" ;
    vak:hasException vak:Rddhi ;
    vak:hasException vak:ParaAshraya .

vak:PathDiscriminator
    a logic:EvaluativeMiddle ;
    rdfs:label "Path-Discriminator" ;
    vak:evaluates vak:VisibilityHorizon ;
    vak:distinguishes vak:PathFromNotPath .
```

## 14. Commit Note

Committed VAK_3.72 / VAkK_3.72.

Established:
- each world-station has a visibility horizon.
- downward vision is allowed according to station; upward vision is blocked.
- upward vision requires ṛddhi or reliance on another.
- this verse grounds the observer-territory rule and strengthens the role of the Path-Discriminator.
