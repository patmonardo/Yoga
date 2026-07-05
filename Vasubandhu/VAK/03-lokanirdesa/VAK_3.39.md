# VAK_3b — VAkK_3.39

## Sanskrit — Devanāgarī

कवडीकार आहारः कामे त्र्यायतनात्मकः ।
न रूपायतनं तेन स्वाक्षमुक्ताननुग्रहात् ॥ VAkK_3.39 ॥

## Sanskrit — IAST

kavaḍīkāra āhāraḥ kāme tryāyatanātmakaḥ /
na rūpāyatanaṃ tena svākṣamuktānanugrahāt // VAkK_3.39 //

## Source Caution

The source reads:

```text
kavaḍīkāra āhāraḥ kāme tryāyatanātmakaḥ /
na rūpāyatanaṃ tena svākṣamuktānanugrahāt // VAkK_3.39 //
```

The compound `svākṣamuktānanugrahāt` is compact. I preserve the source form and treat the final causal phrase cautiously until checked against the Bhāṣya.

## Padaccheda

| Sandhi form | Padaccheda | Basic meaning |
|---|---|---|
| kavaḍīkāra | kavaḍīkāra | morsel / mouthful-form |
| āhāraḥ | āhāraḥ | nutriment / food |
| kāme | kāme | in the desire realm |
| tryāyatanātmakaḥ | tri-āyatana-ātmakaḥ | having three spheres as its nature |
| na | na | not |
| rūpāyatanam | rūpa-āyatanam | the visible-form sphere |
| tena | tena | therefore / by that |
| svākṣamuktānanugrahāt | sva-akṣa-mukta-an-anugrahāt | because of not benefiting its own faculty and the liberated; provisional |

## Grammar

```text
kavaḍīkāra āhāraḥ
    = morsel nutriment

kāme tri-āyatana-ātmakaḥ
    = in the desire realm, it has three spheres as its nature

na rūpa-āyatanam
    = not the visible-form sphere

tena ... an-anugrahāt
    = because it does not benefit/support ...
```

## Literal Translation

Morsel nutriment, in the desire realm, has three spheres as its nature. The visible-form sphere is not included, because it does not benefit its own faculty and the liberated. The final reason remains provisional pending Bhāṣya control.

## Philosophical Translation

Material or morsel nutriment in the desire realm is defined through three āyatanas, not through visible form. The visible-form sphere is excluded because mere visible form does not perform the sustaining function required of nutriment.

## Technical Vocabulary

| Sanskrit | Working translation | Note |
|---|---|---|
| āhāra | nutriment / food | Sustaining condition of the world |
| kavaḍīkāra āhāra | morsel nutriment | Material nutriment, taken in mouthful form |
| kāma | desire realm | Realm in which morsel nutriment applies |
| āyatana | sphere | Here the relevant sensory spheres of nutriment |
| tri-āyatana-ātmaka | having three spheres as nature | Usually smell, taste, and tangible/contactable; confirm with Bhāṣya |
| rūpāyatana | visible-form sphere | Explicitly excluded |
| anugraha | benefit / support / sustaining aid | Functional criterion for nutriment |

## Doctrinal Determination

VAkK_3.38 stated:

```text
āhāra-sthitikaṃ jagat
    = the world is sustained by nutriment
```

VAkK_3.39 begins the analysis of nutriment with morsel nutriment:

```text
kavaḍīkāra āhāra
    = morsel / material nutriment
    = in kāma-dhātu
    = tri-āyatana-ātmaka
```

The visible-form sphere is explicitly excluded:

```text
na rūpāyatanam
```

This is important. Nutriment is not defined by mere visibility. It is defined by sustaining function.

## Logical Determination

The active feature is now `āhāra`.

```text
āhāra
    is not merely an object
    but a sustaining condition
```

Thus morsel nutriment is determined functionally:

```text
included:
    what sustains

excluded:
    mere visible form, if it does not sustain in the relevant way
```

So the analysis moves from thinghood to function:

```text
food as visible object
    ≠ nutriment as sustaining feature
```

## Interpretive Note

The Vedānta echo with `annamaya`, the food-sheath, is a useful contact point, but the Abhidharma taxonomy is more precise here.

The verse is not saying simply:

```text
body depends on food
```

It is saying:

```text
world persists through nutriment
and morsel nutriment is defined by sustaining āyatanas,
not by visible form alone.
```

## Organon Interpretation

Light contact point:

```text
A feature is determined by what it does in the system.
```

Here, `āhāra` is a sustaining feature. It is not the object as seen, but the object insofar as it supports persistence.

```text
visible thing
    becomes nutriment
        only through sustaining function
```

## OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_39
    a vak:Karika ;
    rdfs:label "VAkK 3.39" ;
    vak:continues vak:VAK_3_38 ;
    vak:hasTopic vak:Ahara ;
    vak:defines vak:KavadikaraAhara ;
    vak:excludes vak:Rupayatana .

vak:KavadikaraAhara
    a logic:NutrimentType ;
    rdfs:label "kavaḍīkāra āhāra" ;
    vak:hasCanonicalTranslation "morsel nutriment" ;
    logic:inField vak:KamaDhatu ;
    vak:hasSphereCount 3 .

vak:Rupayatana
    a logic:SenseSphere ;
    rdfs:label "rūpāyatana" ;
    vak:hasCanonicalTranslation "visible-form sphere" .
```

## Commit Note

Committed VAK_3b / VAkK_3.39.

Established:
- the analysis of āhāra begins with kavaḍīkāra āhāra.
- morsel nutriment in the desire realm is tri-āyatana-ātmaka.
- rūpāyatana is explicitly excluded.
- nutriment is defined by sustaining function, not by mere visible objecthood.
