# VAK_1.16

## 1. Sanskrit (Devanāgarī)

> विज्ञानं प्रतिविज्ञप्तिः मन आयतनं च तत् ।
>
> धातवः सप्त च मताः षड्विज्ञानान्यथो मनः ॥ १.१६ ॥

## 2. Sanskrit (IAST)

> vijñānaṃ prativijñaptiḥ mana āyatanaṃ ca tat /
>
> dhātavaḥ sapta ca matāḥ ṣaḍvijñānāny atho manaḥ // VAkK_1.16 //

Source label in GRETIL: `VAkK_1.16`. Project-normalized label: `VAkK_1.16`.

## 3. Padaccheda

| Form | Padaccheda | Meaning |
|---|---|---|
| vijñānam | vijñānam | knowledge |
| prativijñaptiḥ | prativijñaptiḥ | counter-disclosure / discriminative disclosure |
| manaḥ | manaḥ | mind |
| āyatanam ca tat | āyatanam ca tat | and that is a sphere |
| dhātavaḥ sapta | dhātavaḥ sapta | seven domains |
| ca matāḥ | ca matāḥ | are accepted |
| ṣaṭ vijñānāni | ṣaṭ vijñānāni | six knowledges |
| atho manaḥ | atho manaḥ | and also mind |

## 4. Grammar

The first definition is direct:

```text
vijñāna
    = prativijñapti
```

Knowledge is discriminative disclosure: it knows by differentiating object-domain and mode of disclosure.

The verse then states that **manas** is an āyatana and that there are seven domains here:

```text
six vijñānas
+ manas
    = seven domains
```

## 5. Literal Translation

> Knowledge is prativijñapti. Mind is also that sphere. And seven domains are accepted: the six knowledges and also mind.

## 6. Philosophical Translation

> Vijñāna is discriminative disclosure. Manas is the mental sphere, and together the six knowledge-domains and mind make seven domains.

Organon rendering:

> Knowledge is not vague awareness. It is prativijñapti: disclosure through distinction. Manas is the internal sphere that coordinates the six knowledges and becomes the seventh domain in the cognitive architecture.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| vijñāna | knowledge | never consciousness in this project layer |
| prativijñapti | discriminative disclosure | knowing as differential disclosure |
| manas | mind | mental sphere/domain |
| āyatana | sphere | relational field |
| dhātu | domain | lawful domain of analysis |
| ṣaḍvijñāna | six knowledges | five sensory plus mental knowledge |

## 8. Logical Determination

```text
vijñāna
    = prativijñapti
```

and:

```text
six knowledges
+ manas
    = seven domains
```

The verse sets up the distinction between the six knowledge-events and the mind-domain that supports their serial continuity.

## 9. Interpretive Note

This is a central project verse. Translating **vijñāna** as consciousness would flatten the logic. The verse defines it as **prativijñapti**, a discriminative disclosure. Knowledge is structured by difference.

Organon note:

```text
vijñāna
    = knowledge as differential disclosure

manas
    = inner sphere/domain of coordination
```

This prepares VAK_1.17, where the immediately past sixfold knowledge is identified as manas.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_16
    a vak:Karika ;
    rdfs:label "VAK 1.16" ;
    vak:hasSourceLabel "VAkK_1.16" ;
    vak:hasProjectLabel "VAkK_1.16" ;
    vak:hasTopic vak:VijnanaAndManas ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Vijnana vak:definedAs vak:Prativijnapti .
vak:SevenCognitiveDomains vak:includes vak:SixVijnanas , vak:Manas .
```

## 11. Commit History

- Upgraded VAK_1.16 with expanded Organon analysis.
- Preserves **vijñāna = knowledge** and defines it through **prativijñapti**.
- Establishes six knowledges plus manas as seven domains.
