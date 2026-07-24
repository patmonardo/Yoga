# VAK_7.38 — The Cognitive Nature of the Four Discriminating Knowledges

## Sanskrit

### IAST

`tīsro nāmārthavāgjñānam avivartyaṃ yathākramam /`
`caturthī yuktamuktābhilāpamārgavaśitvayoḥ // VAK_7.38 //`

## Padaccheda

`tīsraḥ / nāma-artha-vāk-jñānam / avivartyam / yathā-kramam / caturthī / yukta-mukta-abhilāpa / mārga-vaśitvayoḥ`

## Literal Translation

The first three are, respectively, irreversible knowledge of name, meaning, and speech. The fourth is mastery concerning appropriate and fluent expression and concerning the Path.

## Philosophical Translation

The first three discriminating knowledges are unfailing mastery of designation, meaning, and verbal expression respectively. The fourth is the power to speak coherently and without obstruction, together with mastery of the liberating Path that such speech communicates.

## Technical Determination

The four pratisaṃvids are specified as follows:

1. **Dharma-pratisaṃvid** — unfailing knowledge of names and doctrinal designations.
2. **Artha-pratisaṃvid** — unfailing knowledge of the meanings or things designated.
3. **Nirukti-pratisaṃvid** — unfailing knowledge of speech and verbal realization.
4. **Pratibhāna-pratisaṃvid** — mastery of coherent, fluent discourse together with mastery of the Path.

The first three command distinguishable elements of teaching:

`name → meaning → speech`

The fourth commands their living unity in the activity of teaching.

## Avivartya

`avivartya` indicates knowledge that is not turned back, obstructed, or made uncertain. The relations among designation, meaning, and expression have become stable and immediately available.

The name is encountered and its meaning is known; the meaning is intended and its expression is available.

## The Fourth: Pratibhāna

`yukta-abhilāpa` is connected, appropriate, and coherent expression.

`mukta-abhilāpa` is free, fluent, and unobstructed expression.

Pratibhāna therefore overcomes two defects:

- fluency without relevance or coherence;
- correctness without freedom of expression.

It unites truthful connection with unobstructed articulation.

## Mastery of the Path

The fourth knowledge also includes `mārga-vaśitva`, mastery of the Path.

Eloquence without the Path is rhetoric. Knowledge of the Path without expression remains incommunicable. Pratibhāna is mastery of the Path becoming unobstructed teaching.

## Logical Determination

The first three form a determinate triad:

- name — universal sign;
- meaning — determinate content;
- speech — actual expression.

The fourth is not merely another item beside them. It is the synthetic practical mastery that coordinates the three in one act of teaching.

Thus the structure is:

`three determinate cognitive powers + one synthetic practical mastery`

## Organon Interpretation

A science must command four moments:

- **Term** — what is it called?
- **Meaning** — what does it signify?
- **Expression** — how is it stated?
- **Method** — how does its expression lead along the Path?

The fourth is the philosophical meaning of Yoga as integration. Names, meanings, speech, and Path are yoked into one living operation.

All philosophy supplies determinations; Yoga integrates them into the Path.

The Kośa has moved beyond merely classifying kinds of knowledge. It is describing how knowledge becomes free philosophical discourse governed by realization.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix lang: <http://127.0.0.1:3000/language#> .
@prefix path: <http://127.0.0.1:3000/path#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_7_38
    a vak:Karika ;
    rdfs:label "VAK 7.38" ;
    vak:determines jna:FourDiscriminatingKnowledges .

jna:DharmaPratisamvid
    jna:hasObject lang:Name ;
    jna:hasQuality jna:UnobstructedKnowledge .

jna:ArthaPratisamvid
    jna:hasObject jna:Meaning ;
    jna:hasQuality jna:UnobstructedKnowledge .

jna:NiruktiPratisamvid
    jna:hasObject lang:Speech ;
    jna:hasQuality jna:UnobstructedKnowledge .

jna:PratibhanaPratisamvid
    jna:hasFunction lang:CoherentExpression,
                    lang:FluentExpression ;
    jna:includesMastery path:PathMastery .
```

## Kārikā-Pass Determination

The first three discriminating knowledges master name, meaning, and speech. The fourth masters their free and coherent use as discourse governed by the Path.

This is the point at which knowledge becomes not merely possessed, but freely deployable as Yoga.
