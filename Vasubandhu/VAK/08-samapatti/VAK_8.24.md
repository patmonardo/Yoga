# VAK_8.24

## Sanskrit

आनिमित्तः शमाकारैः शून्यतानात्मशून्यतः ।
प्रवर्ततेऽप्रणिहितः सत्याकारैरतः परैः ॥

## IAST

ānimittaḥ śamākāraiḥ śūnyatānātmaśūnyataḥ /
pravartate 'praṇihitaḥ satyākārair ataḥ paraiḥ //

## Source Note

The supplied GRETIL text reads `samākāraiḥ`. The doctrinal syntax supports the provisional reading `śamākāraiḥ`, “through the aspects of peace.”

## Padaccheda

ānimittaḥ | śama-ākāraiḥ | śūnyatā | anātma-śūnyataḥ | pravartate | apraṇihitaḥ | satya-ākāraiḥ | ataḥ | paraiḥ

## Literal Translation

Signless Recognition proceeds through the aspects of peace.

Emptiness Recognition proceeds through emptiness and non-self.

Non-directed Recognition proceeds through the remaining aspects of the truths.

## Philosophical Translation

Signless Recognition flows through the determinations of peace.

Emptiness Recognition flows through the recognition of emptiness and non-self.

Non-directed Recognition flows through the remaining determinations of the truths.

## Technical Vocabulary

- **samādhi** — Recognition, not concentration.
- **dhyāna** — the sustained work of concentration upon determinate content.
- **nimitta** — sign, mark, determinate appearance.
- **apraṇihita** — non-directed Recognition, free from projection toward a conditioned result.
- **ākāra** — cognitive aspect or determinate mode.

Dhyāna works the content. Samādhi is the free flow of conclusive meaning.

## Doctrinal Determination

The verse distributes the aspects of the truths among three Recognitions:

- **Śūnyatā** operates through emptiness and non-self.
- **Ānimitta** operates through the peaceful aspects of cessation.
- **Apraṇihita** operates through the remaining truth-aspects.

Yoga’s `svarūpa-śūnya` does not reduce cognition to powerlessness. The yogin’s analytic form is full of objective determinations; in Samādhi those determinations no longer stand as independently managed characteristics. Their separate standing is sublated in the determinate Concept, so meaning can speak with its own authority.

## Logical Determination

The three Recognitions release cognition from three finite structures:

- **śūnyatā** — no substantial bearer;
- **ānimitta** — no conditioned sign adequate to cessation;
- **apraṇihita** — no projected conditioned end.

The triple is not transcendental. It is the threefold incarnation of liberated Recognition.

## Organon Interpretation

Samādhi is the determinate Concept: not a determination, not a model, and not a feature-set.

- Śūnyatā is Recognition freed from substantial subjectivity.
- Ānimitta is Recognition freed from finite presentation.
- Apraṇihita is Recognition freed from finite purposiveness.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix samadhi: <http://127.0.0.1:3000/samadhi#> .
@prefix truth: <http://127.0.0.1:3000/truth#> .

vak:VAK_8_24
    a vak:Karika ;
    vak:chapter vak:Samapatti ;
    vak:determines samadhi:ThreeRecognitions .

samadhi:EmptinessRecognition
    rdfs:subClassOf samadhi:Recognition ;
    samadhi:operatesThrough truth:EmptinessAspect,
                              truth:NonSelfAspect .

samadhi:SignlessRecognition
    rdfs:subClassOf samadhi:Recognition ;
    samadhi:operatesThrough truth:PeacefulCessationAspects .

samadhi:NonDirectedRecognition
    rdfs:subClassOf samadhi:Recognition ;
    samadhi:operatesThrough truth:RemainingTruthAspects .
```

## Commit History

`VAK_8.24 — analyze three samadhi recognitions`
