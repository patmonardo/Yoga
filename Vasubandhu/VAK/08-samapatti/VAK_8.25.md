# VAK_8.25

## Sanskrit

शुद्धामलाः निर्मलास्तु ते विमोक्षमुखत्रयम् ।
शून्यताशून्यताद्याख्यास्त्रयोऽपरसमाधयः ॥

## IAST

śuddhāmalāḥ nirmalās tu te vimokṣamukhatrayam /
śūnyatāśūnyatādyākhyās trayo 'parasamādhayaḥ //

## Padaccheda

śuddha-amalāḥ | nirmalāḥ | tu | te | vimokṣa-mukha-trayam |
śūnyatā-śūnyatā-ādi-ākhyāḥ | trayaḥ | apare | samādhayaḥ

## Literal Translation

Those are pure or immaculate; the immaculate ones are the three gates of liberation. There are three further Recognitions, called Emptiness-of-Emptiness and so forth.

## Philosophical Translation

The three Recognitions may belong either to purified conditioned cognition or to immaculate knowing. Only as immaculate Recognition do they constitute the three gates of liberation. Beyond them stand three reflexive Recognitions, beginning with Recognition of emptiness in Emptiness Recognition.

## Technical Vocabulary

- **samādhi** — Recognition.
- **śuddha** — cultivated purity, not necessarily beyond outflow.
- **amala / nirmala** — immaculate, stainless, anāsrava.
- **vimokṣa-mukha** — gate or opening of liberation.
- **apara** — further, subsequent.

## Doctrinal Determination

The three samādhis of VAK_8.24 may occur in pure worldly or immaculate supramundane form. Only their immaculate forms are the three gates of liberation.

The second half introduces three further Recognitions:

- Recognition of emptiness in Emptiness Recognition;
- Recognition of signlessness in Signless Recognition;
- Recognition of non-direction in Non-directed Recognition.

These should not be treated as exotic “double absorptions.” They are analytical acts in which Recognition takes attained Recognition as object.

## Logical Determination

Correct truth-content does not by itself constitute liberation. Pure Recognition concerns cultivated form; immaculate Recognition concerns the freedom of the knowing act itself.

Recognition of emptiness in Emptiness Recognition prevents the universal from hardening into a fixed model or feature-set. Pure Reason speaks for itself; it does not speak for models and features.

The yogin’s analytic form is full of objective determinations. In Samādhi their independent analytic standing is sublated. Samādhi is terminally the determinate Concept, not another determination.

## Yoga Contact

Yoga Sūtra III.3 defines Samādhi:

`tad evārthamātra-nirbhāsaṃ svarūpa-śūnyam iva samādhiḥ`

- **svarūpa-śūnyam iva** — the yogin’s analytic form no longer stands independently;
- **nirbhāsa** — positive manifestation;
- **artha-mātra** — meaning alone, the determinate Principle speaking for itself.

## Organon Interpretation

- `śuddha-samādhi` — adequately cultivated Recognition.
- `amala-samādhi` — Recognition free from contamination.
- `vimokṣa-mukha` — Recognition as an opening into liberation.
- `śūnyatā-śūnyatā` — Recognition of emptiness in Emptiness Recognition, without reifying the universal.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix samadhi: <http://127.0.0.1:3000/samadhi#> .

vak:VAK_8_25 a vak:Karika ;
    vak:determines samadhi:LiberationGateTriad ;
    vak:introduces samadhi:ReflexiveRecognitionTriad .

samadhi:RecognitionOfEmptinessInEmptinessRecognition
    rdfs:subClassOf samadhi:ReflexiveRecognition ;
    samadhi:preventsReificationOf samadhi:EmptinessRecognition .
```

## Commit History

`VAK_8.25 — distinguish pure immaculate and reflexive Recognition`
