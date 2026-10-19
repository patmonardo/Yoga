# VAK_2.33 — Coarse and Subtle

## 1. Sanskrit (Devanāgarī)

```sanskrit
वितर्कचारावौदार्यसूक्ष्मते मान उन्नतिः ।
मदः स्वधर्मे रक्तस्य पर्यादानं तु चेतसः ॥ २.३३ ॥
```

## 2. Sanskrit (IAST)

```text
vitarkacārāv audāryasūkṣmate māna unnatiḥ /
madaḥ svadharme raktasya paryādānaṃ tu cetasaḥ // 2.33 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| vitarka-cārau | nom. dual m.; coordinated compound | initial and sustained examination |
| audārya-sūkṣmate | nom. dual n.; coordinated abstract nouns | coarseness and subtlety, paired respectively |
| mānaḥ | nom. sg. m. | conceit |
| unnatiḥ | nom. sg. f. | elevation |
| madaḥ | nom. sg. m. | intoxication |
| sva-dharme raktasya | loc. sg. n. + gen. sg. m. participle | of one attached to one's own qualities |
| paryādānam | nom. sg. n. | taking-over |
| cetasaḥ | gen. sg. n. | of consciousness |
| tu | contrastive particle | distinguishes intoxication from conceit |

The prose explicitly carries the later of consciousness into the
examination definition, and supplies it again for conceit. The verse
opens three definition units. Sandhi is opened for parsing.

```text
# tokens: vitarkacārau audāryasūkṣmate mānaḥ unnatiḥ madaḥ svadharme raktasya paryādānam tu cetasaḥ
```

## 4. Grammar

The dual pairs initial examination with coarseness and sustained
examination with subtlety; it does not assert their simultaneous
occurrence. The final genitive supplies the locus of taking-over,
not its object as one's own qualities: the latter are what the
person is attached to.

```nltk-fcfg
% start S
# tokens: vitarkacārau audāryasūkṣmate mānaḥ unnatiḥ madaḥ svadharme raktasya paryādānam tu cetasaḥ
S[SEM=<(?examination & ?conceit & ?intoxication)>] -> EXAMINATION[SEM=?examination] CONCEITCLAUSE[SEM=?conceit] INTOXICATIONCLAUSE[SEM=?intoxication]
EXAMINATION[SEM=<(DefinedAs(initial,coarseness) & DefinedAs(sustained,subtlety))>] -> EXAMPAIR[NUM=du] STATEPAIR[NUM=du,ORDER=respective]
CONCEITCLAUSE[SEM=<DefinedAs(conceit,elevation)>] -> CONCEIT[CASE=nom] ELEVATION[CASE=nom]
INTOXICATIONCLAUSE[SEM=<(DefinedAs(intoxication,taking_over) & AttachmentTo(intoxication,own_qualities) & Locus(intoxication,consciousness))>] -> INTOXICATION[CASE=nom] OWN[CASE=loc] ATTACHED[CASE=gen] TAKEOVER[CASE=nom] BUT CONSCIOUSNESS[CASE=gen]
EXAMPAIR[NUM=du] -> 'vitarkacārau'
STATEPAIR[NUM=du,ORDER=respective] -> 'audāryasūkṣmate'
CONCEIT[CASE=nom] -> 'mānaḥ'
ELEVATION[CASE=nom] -> 'unnatiḥ'
INTOXICATION[CASE=nom] -> 'madaḥ'
OWN[CASE=loc] -> 'svadharme'
ATTACHED[CASE=gen] -> 'raktasya'
TAKEOVER[CASE=nom] -> 'paryādānam'
BUT -> 'tu'
CONSCIOUSNESS[CASE=gen] -> 'cetasaḥ'
```

```nltk-dep
'vitarkacārau' -> 'audāryasūkṣmate'
'mānaḥ' -> 'unnatiḥ'
'madaḥ' -> 'paryādānam' | 'tu'
'paryādānam' -> 'raktasya' | 'cetasaḥ'
'raktasya' -> 'svadharme'
```

| Span | Constituent | Result |
|---|---|---|
| [0, 2) | `EXAMINATION` | respective dual definitions |
| [2, 4) | `CONCEITCLAUSE` | elevation |
| [4, 10) | `INTOXICATIONCLAUSE` | taking-over of consciousness, attachment to own qualities |

## 5. Translation

### Literal Translation

> Vitarka and vicāra are coarseness and subtlety. Conceit is elevation.
> Intoxication is the taking-over of the consciousness of one attached to
> one's own qualities.
### Bhāṣya-informed study translation

> Initial and sustained examination are, respectively, coarseness and
> subtlety of consciousness. Conceit is elevation of consciousness through
> a constructed distinction relative to another. Intoxication, however,
> is the taking-over of consciousness in one attached to one's own qualities.
## 6. Philosophical Translation

> Coarseness and subtlety do not by themselves settle co-presence. Conceit compares. Intoxication takes over one's own. Level-attribution is not moment-co-presence.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| vitarka | initial examination | coarseness definition examined in the dispute |
| vicāra | sustained examination | subtlety definition examined in the dispute |
| vāk-saṃskāra | formation of speech | the sūtra account |
| jāti-bheda | difference of kind | demanded, not stated |
| bhūmitaḥ | by level | the five-factor attribution |
| kṣaṇataḥ | by moment | not thereby co-present |
| māna | conceit | elevation by comparison |
| mada | intoxication | taking-over; not conceit |
| saṃpraharṣaṇa | exhilaration | others |

## 8. Logical Determination

**Kārikā, derived.** DefinedAs records the formulas being examined,
not a proof that the disputed definitions withstand every objection.
The Bhāṣya's positions are indexed separately: the model does not
assert both co-presence and its denial as one theory.

```nltk-sem
definition : \a.\b.DefinedAs(b,a)
locus : \x.Locus(x,consciousness)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((DefinedAs(initial,coarseness) & DefinedAs(sustained,subtlety)) & DefinedAs(conceit,elevation) & (DefinedAs(intoxication,taking_over) & AttachmentTo(intoxication,own_qualities) & Locus(intoxication,consciousness)))

# THEORY attributed_positions
# EXPECT attributed_positions T
AllowsCoPresence(balancing) & AllowsCoPresence(speech_account) & DeniesCoPresence(separate_account)
LevelFive(separate_account) & -MomentFive(separate_account)
ComparisonWith(conceit,another) & Locus(conceit,consciousness)

# THEORY rejected_every_account_allows_copresence
# EXPECT rejected_every_account_allows_copresence F
all p.(Position(p) -> AllowsCoPresence(p))

# THEORY rejected_level_five_entails_moment_five
# EXPECT rejected_level_five_entails_moment_five F
all p.(LevelFive(p) -> MomentFive(p))

# THEORY rejected_taking_over_qualities_not_consciousness
# EXPECT rejected_taking_over_qualities_not_consciousness F
Locus(intoxication,own_qualities) & AttachmentTo(intoxication,own_qualities)
```

```nltk-valuation
initial => initial_examination
sustained => sustained_examination
coarseness => coarseness_definition
subtlety => subtlety_definition
conceit => conceit_factor
elevation => elevation_definition
intoxication => intoxication_factor
taking_over => takeover_definition
own_qualities => own_qualities_condition
consciousness => consciousness_locus
another => comparison_other
balancing => balancing_position
speech_account => speech_position
separate_account => separation_position
DefinedAs => {(initial_examination,coarseness_definition),(sustained_examination,subtlety_definition),(conceit_factor,elevation_definition),(intoxication_factor,takeover_definition)}
AttachmentTo => {(intoxication_factor,own_qualities_condition)}
Locus => {(intoxication_factor,consciousness_locus),(conceit_factor,consciousness_locus)}
ComparisonWith => {(conceit_factor,comparison_other)}
Position => {balancing_position,speech_position,separation_position}
AllowsCoPresence => {balancing_position,speech_position}
DeniesCoPresence => {separation_position}
LevelFive => {separation_position}
MomentFive => {}
```

The balancing and speech accounts defend co-presence in different
ways and face different objections. The separation account's
level/moment reply stays attributed, not substituted for the prior
co-arising rules. The model checks these distinctions; it does not
decide the debate or reduce difference of kind to intensity.

## 9. Interpretive Note

**Translation note.** The commentary supplies consciousness as the locus and says conceit involves constructed distinction relative to another. It presents three positions on the relation of vitarka and vicāra—balancing, speech-formation, or denial of co-presence—without harmonizing them. The butter example and a quoted reply are damaged; the summit objection concerns the exclusions of 2.31.

Three positions: balancing, speech-formation, denial of co-presence. No harmonization is appended. The butter example is damaged. Cast into water follows the reply's water and heat. Not a restored reading. The speech quotation is damaged. Its sense is kept.

The summit objection uses the exclusions of 2.31. A satisfactory account would name the factors and keep that range.

In the Organon reading, Cognition governs Perception and Conception
without collapsing into consciousness or Mind. The present dispute
concerns factors and determinations of consciousness, not definitions
of that governing Cognition. Condition versus nature, kind versus
degree, and level versus moment remain distinct tests.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_33
    a vak:Karika ;
    rdfs:label "VAK 2.33" ;
    vak:hasTopic vak:VitarkaVicara ;
    vak:belongsTo vak:Indriyanirdesa .

vak:VitarkaVicara vak:disputeOpen true .
vak:Conceit vak:comparesWithAnother true .
vak:Intoxication vak:takesOver vak:Consciousness ;
    vak:involvesAttachmentTo vak:OwnQualities .

organon:VAK_2_33_Interpretation
    organon:distinguishes vak:Condition, vak:FactorNature,
        vak:Intensity, vak:Kind, vak:Level, vak:Moment .
```
