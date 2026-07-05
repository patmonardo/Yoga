# VAK_3b — VAkK_3.27

## Sanskrit — Devanāgarī

क्लेशात् क्लेशः क्रिया चैव ततो वस्तु ततः पुनः ।
वस्तु क्लेशाश्च जायन्ते भवाङ्गानामयं नयः ॥ VAkK_3.27 ॥

## Sanskrit — IAST

kleśāt kleśaḥ kriyā caiva tato vastu tataḥ punaḥ /
vastu kleśāś ca jāyante bhavāṅgānām ayaṃ nayaḥ // VAkK_3.27 //

## Padaccheda

| Sandhi form | Padaccheda | Basic meaning |
|---|---|---|
| kleśāt | kleśāt | from affliction |
| kleśaḥ | kleśaḥ | affliction |
| kriyā | kriyā | activity / action |
| ca eva | ca eva | and indeed |
| tataḥ | tataḥ | from that; thereafter |
| vastu | vastu | real thing / factual basis |
| tataḥ punaḥ | tataḥ punaḥ | from that again |
| vastu | vastu | factual basis / concrete existence |
| kleśāḥ | kleśāḥ | afflictions |
| ca | ca | and |
| jāyante | jāyante | are born / arise |
| bhavāṅgānām | bhava-aṅgānām | of the limbs of becoming |
| ayam | ayam | this |
| nayaḥ | nayaḥ | method; principle; way |

## Grammar

```text
kleśāt
    ablative singular
    = from affliction

kleśaḥ kriyā ca eva
    nominative singulars
    = affliction and action indeed

tataḥ vastu
    = from that, vastu

tataḥ punaḥ vastu kleśāḥ ca jāyante
    = from that again, vastu and afflictions arise

bhava-aṅgānām ayam nayaḥ
    = this is the method/principle of the limbs of becoming
```

## Literal Translation

From affliction arise affliction and activity; from that, vastu. From that again, vastu and afflictions are born. This is the principle of the limbs of becoming.

## Philosophical Translation

Affliction gives rise both to further affliction and to action. From action there arises the concrete factual series. From that factual series, again, both further factual existence and afflictions arise. This is the dynamic principle governing the limbs of becoming.

## Technical Vocabulary

| Sanskrit | Working translation | Note |
|---|---|---|
| kleśa | affliction | Defiled motive-condition; includes ignorance, craving, appropriation |
| kriyā | activity / action | Here functionally aligned with karma |
| vastu | real thing / factual basis / concrete existence | The concrete resultant series |
| jāyante | arise / are born | Marks renewed production |
| bhava-aṅga | limb of becoming | Limb within the dependent co-arising process |
| naya | principle / method / way | Governing rule of the sequence |

## Doctrinal Determination

VAkK_3.27 gives the dynamic law behind the compression stated in 3.26.

3.26 grouped the twelve as:

```text
kleśa
karma / kriyā
vastu / phala
```

3.27 now gives the cyclic movement:

```text
kleśa
    ↓
kleśa + kriyā
    ↓
vastu
    ↓
vastu + kleśa
    ↓
renewed becoming
```

This is not a linear chain that simply ends. It is a wheel.

```text
affliction
    produces action

action
    produces concrete existence

concrete existence
    produces further affliction and further concrete existence
```

## Logical Determination

The key logical structure is recurrence.

```text
kleśa → kriyā → vastu → kleśa
```

More fully:

```text
Affliction
    is not merely an origin.
    It reproduces itself through action.

Action
    is not merely motion.
    It produces a concrete resultant basis.

Concrete existence
    is not inert.
    It becomes the field from which further affliction arises.
```

So the logic of dependent co-arising is:

```text
motive-defilement
    ↓
activity / karma
    ↓
concrete existence
    ↓
renewed motive-defilement
```

This confirms the wheel-structure of the whole block.

## Interpretive Note

This verse protects us from reading the twelve limbs as merely chronological. The twelve can be listed sequentially, but their deeper principle is recursive.

The word **vastu** is especially important. Here it should not be made too abstract. It is the concrete factual basis, or concrete existence, produced by affliction and action. From that concrete existence, further affliction arises.

Thus the middle as concrete field becomes the thing: not substance in itself, but the resultant factual basis through which the wheel turns again.

## Organon Interpretation

Speculatively, VAkK_3.27 is a process rule.

```text
kleśa
    = distorted motive / affective-practical fault

kriyā
    = operation / activity

vastu
    = concrete produced field

renewed kleśa
    = recurrence of distortion within the produced field
```

In Organon terms:

```text
faulted principle
    generates operation

operation
    generates concrete field

concrete field
    generates further faulted principle
```

This is close to a self-reproducing loop:

```text
condition
    → operation
        → concrete result
            → renewed condition
```

The speculative mapping should remain subordinate to the Sanskrit and Bhāṣya. But as an architectural hypothesis, this is strong: the wheel is recurrence through concrete existence.

## OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_27
    a vak:Karika ;
    rdfs:label "VAkK 3.27" ;
    vak:continues vak:VAK_3_26 ;
    vak:hasTopic vak:DependentCoArising ;
    vak:statesPrinciple vak:BhavangaNaya ;
    vak:hasCycle vak:KleshaKriyaVastuCycle .

vak:BhavangaNaya
    a logic:ProcessPrinciple ;
    rdfs:label "principle of the limbs of becoming" ;
    vak:hasSanskrit "bhavāṅgānām ayaṃ nayaḥ" .

vak:KleshaKriyaVastuCycle
    a logic:RecursiveCycle ;
    rdfs:label "kleśa-kriyā-vastu cycle" ;
    logic:beginsWith vak:Klesha ;
    logic:mediatedBy vak:Kriya ;
    logic:produces vak:Vastu ;
    logic:recursAs vak:Klesha .

vak:Kriya
    a logic:Activity ;
    rdfs:label "kriyā" ;
    vak:hasCanonicalTranslation "activity" ;
    rdfs:comment "Activity or action arising from affliction and producing vastu." .

vak:Vastu
    a logic:ConcreteExistence ;
    rdfs:label "vastu" ;
    vak:hasCanonicalTranslation "concrete factual basis" .
```

## Commit Note

Committed VAK_3b / VAkK_3.27.

Established:
- from kleśa arise kleśa and kriyā.
- from kriyā arises vastu.
- from vastu again arise vastu and kleśa.
- this is the naya, the governing principle, of the limbs of becoming.

Logical determination:
VAkK_3.27 gives the recursive wheel-dynamic behind the twelvefold sequence. Affliction produces activity, activity produces concrete existence, and concrete existence becomes the field for renewed affliction and further becoming.
