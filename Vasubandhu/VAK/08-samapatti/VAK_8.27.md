# VAK_8.27

## Sanskrit

सास्रवाः नृषु अकोप्यस्य सप्तसामन्तवर्जिताः ।
समाधिभावना ध्यानं शुभमाद्यं सुखाय हि ॥

## IAST

sāsravāḥ nṛṣu akopyasya saptasāmantavarjitāḥ /
samādhibhāvanā dhyānaṃ śubham ādyaṃ sukhāya hi //

## Padaccheda

sa-āsravāḥ | nṛṣu | akopyasya | sapta-sāmanta-varjitāḥ | samādhi-bhāvanā | dhyānam | śubham | ādyam | sukhāya | hi

## Literal Translation

They are accompanied by outflows, occur among human beings, belong to the Unshakeable one, and are excluded from the seven preliminary attainments. The first wholesome Dhyāna is indeed the cultivation of Recognition for happiness.

## Philosophical Translation

The reflexive Recognitions remain conditioned acts. They arise in human existence, belong to the Unshakeable knower, and require completed rather than merely preliminary cognitive ground. The first wholesome Dhyāna cultivates Recognition as a present dwelling in happiness.

## Technical Vocabulary

- **sāsrava** — accompanied by outflows; conditioned
- **nṛṣu** — among human beings
- **akopya** — the Unshakeable one
- **sāmanta** — preliminary / neighboring attainment
- **samādhi-bhāvanā** — cultivation of Recognition
- **dhyāna** — the concentrated work upon determinate content
- **śubha** — wholesome / purified
- **sukha** — happiness; ease of abiding

## Doctrinal Determination

The three reflexive Recognitions are not immaculate. They still take attained Recognition as object and therefore remain conditioned. Their occurrence is restricted to the stable ground of the Unshakeable Arhat and not to merely transitional attainments.

The verse then begins the four cultivations of Recognition. The first is cultivation for present happiness.

## Logical Determination

Reflection upon completed Recognition is not yet Pure Reason speaking immediately for itself.

Dhyāna performs the concentrated analytic work. Samādhi is the released authority of conclusive meaning. Sukha is the free coherence in which Recognition can presently dwell.

## Organon Interpretation

The yogin's analytic form is full of objective determinations. Samādhi does not erase this content. It sublates the determinations as independently managed determinations into the determinate Concept.

Thus Yoga Samādhi is characteristic-free in the same sense that Hegel's Logic is characteristic-free: it does not characterize this tree or that animal. It is universal and determinate without being an empirical determination.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix samadhi: <http://127.0.0.1:3000/samadhi#> .
@prefix dhyana: <http://127.0.0.1:3000/dhyana#> .
@prefix path: <http://127.0.0.1:3000/path#> .

vak:VAK_8_27
    a vak:Karika ;
    vak:limits samadhi:ReflexiveRecognitionTriad ;
    vak:introduces samadhi:FourCultivationsOfRecognition .

samadhi:ReflexiveRecognitionTriad
    samadhi:hasStatus path:Conditioned ;
    samadhi:arisesAmong path:HumanBeings ;
    samadhi:belongsTo path:UnshakeableArhat .

samadhi:PresentHappinessCultivation
    samadhi:uses dhyana:FirstWholesomeDhyana ;
    samadhi:hasResult path:PresentHappyDwelling .
```

## Commit History

First-pass Kārikā analysis committed after discussion.