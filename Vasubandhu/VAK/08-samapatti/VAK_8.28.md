# VAK_8.28

## Sanskrit

दर्शनायाक्ष्यभिज्ञेष्टा धीभेदाय प्रयोगजाः ।
वज्रोपमोऽन्त्ये यो ध्याने सास्रवक्षयभावना ॥

## IAST

darśanāyākṣyabhijñeṣṭā dhībhedāya prayogajāḥ /
vajropamo 'ntye yo dhyāne sāsravakṣayabhāvanā //

## Padaccheda

darśanāya | akṣi-abhijñā | iṣṭā | dhī-bhedāya | prayoga-jāḥ | vajra-upamaḥ | antye | yaḥ | dhyāne | sa-āsrava-kṣaya-bhāvanā

## Literal Translation

For seeing, the superknowledge of the eye is intended. Those born from application are for the differentiation of understanding. The Vajra-like Recognition in the final Dhyāna is the cultivation for the exhaustion of the outflows.

## Philosophical Translation

The second cultivation of Recognition produces direct vision. The third, arising from deliberate application, differentiates understanding. The fourth is the Vajra-like Recognition grounded in the final Dhyāna, whose work is the exhaustion of the outflows.

## Technical Vocabulary

- **darśana** — seeing; direct vision
- **akṣi-abhijñā** — superknowledge of the eye; the divine-eye cognition
- **dhī-bheda** — differentiation / distinction of understanding
- **prayoga-ja** — born from application or deliberate practice
- **vajropama** — Vajra-like; adamantine and immediately destructive of the final obstruction
- **antya-dhyāna** — the final or fourth Dhyāna
- **āsrava-kṣaya** — exhaustion of the outflows
- **bhāvanā** — cultivation

## Doctrinal Determination

Together with VAK_8.27, this verse completes the four cultivations of Recognition:

1. cultivation for present happiness,
2. cultivation for knowledge and vision,
3. cultivation for differentiation of understanding,
4. cultivation for exhaustion of the outflows.

The divine-eye superknowledge supplies the cultivation for direct vision. Recognitions produced through deliberate application supply the differentiation of understanding. The Vajra-like Recognition in the fourth Dhyāna is the culminating cultivation that destroys the remaining outflows.

## Logical Determination

The four cultivations distinguish four powers of Recognition rather than four merely stronger degrees of concentration:

- abiding freely,
- seeing directly,
- differentiating understanding,
- terminating the conditioned obstruction.

The sequence moves from the present actuality of Recognition, through its objective disclosure and analytic articulation, to its final liberating efficacy.

## Organon Interpretation

The yogin's analytic form remains full of objective determinations at the level of deliberate application. This is the work of **dhī-bheda**: understanding differentiates the articulated field.

The Vajra-like Recognition is not another determination added to that field. It is the terminally determinate Concept whose actuality exhausts the outflows. Its force lies not in accumulating further characteristics, but in bringing the conditioned cognitive field to its conclusion.

Thus the four cultivations may be read provisionally as:

```text
free abiding
    → direct disclosure
    → differentiated understanding
    → conclusive liberation
```

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix samadhi: <http://127.0.0.1:3000/samadhi#> .
@prefix dhyana: <http://127.0.0.1:3000/dhyana#> .
@prefix path: <http://127.0.0.1:3000/path#> .

vak:VAK_8_28
    a vak:Karika ;
    vak:completes samadhi:FourCultivationsOfRecognition .

samadhi:VisionCultivation
    samadhi:uses path:DivineEyeSuperknowledge ;
    samadhi:hasResult path:DirectVision .

samadhi:DiscriminativeCultivation
    samadhi:arisesFrom path:DeliberateApplication ;
    samadhi:hasResult path:DifferentiatedUnderstanding .

samadhi:OutflowExhaustionCultivation
    samadhi:uses samadhi:VajraLikeRecognition ;
    samadhi:groundedIn dhyana:FourthDhyana ;
    samadhi:hasResult path:ExhaustionOfOutflows .
```

## Commit History

First-pass Kārikā analysis committed after discussion.