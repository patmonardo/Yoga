# VAK_1.11

## 1. Sanskrit (Devanāgarī)

> विक्षिप्तचित्तकस्यापि योऽनुबन्धः शुभाशुभः ।
>
> महाभूतान्युपादाय स ह्यविज्ञप्तिरुच्यते ॥ १.११ ॥

## 2. Sanskrit (IAST)

> vikṣiptācittakasyāpi yo 'nubandhaḥ śubhāśubhaḥ /
>
> mahābhūtāny upādāya sa hy avijñaptir ucyate // VAkK_1.11 //

Source label in GRETIL: `VAkK_1.11`. Project-normalized label: `VAkK_1.11`.

## 3. Padaccheda

| Form | Padaccheda | Meaning |
|---|---|---|
| vikṣipta-acittakasya api | vikṣipta-acittakasya api | even of one distracted or without mind |
| yaḥ | yaḥ | that which |
| anubandhaḥ | anubandhaḥ | continuity, binding trace |
| śubha-aśubhaḥ | śubha-aśubhaḥ | wholesome or unwholesome |
| mahābhūtāni | mahābhūtāni | great elements |
| upādāya | upādāya | taking as basis, depending upon |
| saḥ hi | saḥ hi | that indeed |
| avijñaptiḥ | avijñaptiḥ | non-disclosive form |
| ucyate | ucyate | is called |

## 4. Grammar

The subject is **yo 'nubandhaḥ**, a continuing trace or bond. It may remain even when the mind is distracted or absent. It is wholesome or unwholesome and depends on the great elements.

That continuing, ethically marked, element-dependent trace is called **avijñapti**.

## 5. Literal Translation

> That wholesome or unwholesome continuity which belongs even to one distracted or without mind, depending upon the great elements, is called avijñapti.

## 6. Philosophical Translation

> Avijñapti is a subtle form: an ethically marked continuity that persists even when explicit mental disclosure is not occurring, grounded in the great elements.

Organon rendering:

> Avijñapti is the non-manifest trace of action. It is not visible expression, yet it has form-status because it depends on the elemental basis. It preserves the ethical continuity of action beyond immediate mental presentation.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| avijñapti | non-disclosive form | subtle form, not ordinary manifestation |
| anubandha | continuing trace / bond | persists beyond explicit attention |
| śubha / aśubha | wholesome / unwholesome | ethical polarity |
| vikṣipta | distracted | mind not gathered |
| acittaka | without mind | no active mental disclosure |
| mahābhūta | great element | elemental basis of form |
| upādāya | depending upon | derivative grounding |

## 8. Logical Determination

```text
avijñapti
    = ethical continuity
    + non-disclosure
    + elemental dependence
```

It is form, but not ordinary visible form. It is action-trace in a subtle material mode.

## 9. Interpretive Note

This verse is the first major breakthrough after the definition of rūpa. Rūpa includes not only faculties and objects but also a subtle continuity of action. The body of karma has a form-side even when it is not explicitly manifest.

Organon note:

```text
vijñapti
    = disclosure

avijñapti
    = non-disclosive continuity

karma
    leaves a lawful trace
    grounded in the elemental field
```

This will matter later for karma, discipline, vow, and ethical form.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_11
    a vak:Karika ;
    rdfs:label "VAK 1.11" ;
    vak:hasSourceLabel "VAkK_1.11" ;
    vak:hasProjectLabel "VAkK_1.11" ;
    vak:hasTopic vak:Avijnapti ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Avijnapti
    rdfs:label "non-disclosive form" ;
    vak:dependsOn vak:Mahabhuta ;
    vak:hasEthicalPolarity vak:Wholesome , vak:Unwholesome .
```

## 11. Commit History

- Added expanded Organon analysis for VAK_1.11.
- Establishes avijñapti as ethically marked non-disclosive continuity.
- Connects avijñapti to mahābhūta-dependence and karmic trace.
