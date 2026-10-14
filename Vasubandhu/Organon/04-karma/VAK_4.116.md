# VAK 4.116 — The Distinction of the Gift-Object

## 1. Sanskrit (Devanāgarī)

```sanskrit
वर्णादिसम्पदा वस्तु सुरूपत्वं यशस्वि वा ।
प्रियता सुकुमारर्तुसुखस्पर्शाङ्गता ततः ॥ ४.११६ ॥
```

## 2. Sanskrit (IAST)

```iast
varṇādisampadā vastu surūpatvaṃ yaśasvi vā /
priyatā sukumārartusukhasparśāṅgatā tataḥ // 4.116 //
```

The source witness reads `surūptvaṃ` where the repository kārikā has
`surūpatvaṃ`; the latter is retained here. The transmitted `yaśasvi vā` is
also retained, while the Bhāṣya explains the result as `yaśasvī bhavati`.

## 3. Lexical Analysis

```text
varṇa-ādi-sampadā | vastu | su-rūpatvam | yaśasvi | vā |
priyatā | su-kumāra-ṛtu-sukha-sparśa-aṅgatā | tataḥ
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| `varṇādisampadā` | instrumental singular feminine compound | through excellence of color and the other qualities |
| `vastu` | nominative singular neuter | the thing given; the gift-object |
| `surūpatvam` | nominative singular neuter abstract noun | beauty of form |
| `yaśasvi` | transmitted neuter form; prose construes `yaśasvī` | renowned; possessing renown |
| `vā` | indeclinable | or; retained in the transmitted verse wording |
| `priyatā` | nominative singular feminine abstract noun | being beloved or agreeable |
| `sukumārartusukhasparśāṅgatā` | nominative singular feminine compound | having delicate limbs pleasant to touch according to the season |
| `tataḥ` | ablatival adverb | from that; consequently |

The Bhāṣya specifies `varṇādi` as color, smell, taste, and touch, and says
excellence in any one of these can distinguish the thing given. Its
`yathākramam` governs the correspondence with the stated results.

## 4. Grammar

The prose carries forward `viśiṣṭam`:

```text
vastu
    varṇādi-sampadā
    viśiṣṭam [bhavati]
```

> The thing given is distinguished through excellence of color and the
> other qualities.

The results follow in the Bhāṣya's explicit order:

```text
color      → beauty
smell      → renown
taste      → belovedness
touch      → delicacy of limbs and seasonally pleasant touch
```

The last compound gathers two related bodily results under touch; it does
not add a fifth quality of the gift-object.

## 5. Translation

### Scientific English Rendering

> The gift-object is distinguished by excellence of color and the other
> qualities. From giving such an object arise beauty, renown, belovedness,
> delicacy of limbs, and limbs pleasant to touch according to the seasons.

### Bhāṣya-informed study translation

> The gift-object is distinguished by excellence of color and the other
> qualities. From giving such an object arise beauty, renown, belovedness,
> delicacy of limbs, and limbs pleasant to touch according to the seasons.
> The Bhāṣya specifies color, smell, taste, and touch: giving something
> excellent in color yields beauty; something fragrant yields renown;
> something excellent in taste yields belovedness; and something excellent
> in touch yields delicate limbs and limbs pleasant to touch according to
> the seasons.

The four qualities and their ordered correspondence are explicit in the
Bhāṣya, not separately enumerated in the compact kārikā.

## 6. Philosophical Translation

> Giving does not become determinate through intention alone: the thing
> given has its own qualities and makes a particular form of benefit
> available. The Bhāṣya reads maturation as corresponding to those
> qualities, including two bodily outcomes from touch. This extends the
> giver-side analysis of 4.115 without collapsing the giver, the gift-object,
> or its results into one undifferentiated event.

## 7. Technical Vocabulary

- **`Vastu-viśeṣa`** — distinction of the thing given, the second
  determinant named in 4.114.
- **`Varṇādisampad`** — excellence of color and the other qualities; the
  Bhāṣya expands these as smell, taste, and touch.
- **`Surūpatva`** — beauty of form, paired with a gift excellent in color.
- **`Yaśas`** — renown, paired with a fragrant gift; the Bhāṣya compares
  fame spreading through the directions to fragrance.
- **`Priyatā`** — being beloved or agreeable, paired with excellence of
  taste.
- **`Sukumārāṅgatā`** — delicacy of limbs, one of the outcomes paired with
  excellence of touch.
- **`Ṛtusukhasparśāṅgatā`** — limbs pleasant to touch according to the
  seasons, the other outcome paired with excellence of touch.
- **`Yathākramam`** — “in order,” the Bhāṣya's instruction for matching
  the four qualities with the results.

## 8. Logical Determination

```text
Quality of the gift-object              Result stated by the Bhāṣya
---------------------------              ---------------------------
excellence of color                     beauty
excellence of smell                     renown
excellence of taste                     belovedness
excellence of touch                     delicate limbs
                                        seasonally pleasant touch
```

Any one of the four qualities can distinguish the thing given. Touch has
two stated results, so the correspondence is four qualities to five
outcomes—not five independent qualities or one undifferentiated reward.
The analogies between fragrance and spreading fame, and between taste and
agreeableness, belong to the Bhāṣya's explanation.

## 9. Interpretive Note

VAK 4.115 considered the giver and manner of giving; 4.116 considers the
thing given. The giving-event thus has distinct relational determinations:
volition is not the gift-object, and neither the object nor the recipient
is Mind itself. In the project's terms, Bases articulate content and frames;
they are not Mind. Here the material and sensible qualities of the object
make the deed's recipient-facing content specific, while the Bhāṣya traces
those distinctions into its account of maturation.

This passage does not itself name `cetanā`; the volitional dimension is
carried forward from the chapter's broader analysis of giving, not inserted
as a term in this kārikā. The source span is `[269|20]–[270|03]`. At
`[269|22–23]`, the witness's `dadvarṇa...` is separated and repaired as
`tad varṇa...`; at `[269|24–25]`, it reads `surūptvaṃ`, while the
repository kārikā gives `surūpatvaṃ`. The next recipient-field question
begins at `[270|04]`.

## 10. OWL++ Seed

```text
Class: DistinguishedGiftObject
Class: ExcellentColor
Class: ExcellentSmell
Class: ExcellentTaste
Class: ExcellentTouch
Class: BeautyOfForm
Class: Renown
Class: Belovedness
Class: DelicateLimbs
Class: SeasonallyPleasantTouch

Rule: GiftObjectQualityResults
  ExcellentColor -> BeautyOfForm
  ExcellentSmell -> Renown
  ExcellentTaste -> Belovedness
  ExcellentTouch -> DelicateLimbs
  ExcellentTouch -> SeasonallyPleasantTouch

Attribution: GiftObjectQualityResults
  source = Bhāṣya
```
