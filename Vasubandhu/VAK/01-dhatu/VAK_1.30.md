# VAK_1.30

## 1. Sanskrit (Devanāgarī)

> त्रिधान्ये कामधात्वाप्ताः सर्वे रूपे चतुर्दश ।
>
> विना गन्धरसघ्राणजिह्वाविज्ञानधातुभिः ॥ १.३० ॥

## 2. Sanskrit (IAST)

> tridhānye kāmadhātvāptāḥ sarve rūpe caturdaśa /
>
> vinā gandharasaghrāṇajihvāvijñānadhātubhiḥ // VAkK_1.30 //

Source label in GRETIL: `VAkK_1.30`. Project-normalized label: `VAkK_1.30`.

## 3. Padaccheda

| Form | Padaccheda | Meaning |
|---|---|---|
| tridhā anye | tridhā anye | the others are threefold |
| kāmadhātu-āptāḥ | kāmadhātu-āptāḥ | belonging to the desire-domain |
| sarve | sarve | all |
| rūpe | rūpe | in the form-domain |
| caturdaśa | caturdaśa | fourteen |
| vinā | vinā | except, without |
| gandha-rasa | gandha-rasa | smell and taste |
| ghrāṇa-jihvā-vijñāna-dhātubhiḥ | ghrāṇa-jihvā-vijñāna-dhātubhiḥ | smell- and tongue-knowledge-domains |

## 4. Grammar

The eighteen domains are now classified by realm.

```text
kāmadhātu
    contains all eighteen domains

rūpadhātu
    contains fourteen domains
    excluding smell, taste,
    smell-knowledge, and taste-knowledge
```

The remaining domains are threefold with respect to realm-inclusion.

## 5. Literal Translation

> The others are threefold. All belong to the desire-domain. In the form-domain there are fourteen, excluding smell, taste, and the smell- and tongue-knowledge domains.

## 6. Philosophical Translation

> All eighteen domains belong to the desire-domain. The form-domain contains fourteen, lacking smell, taste, and their corresponding knowledge-domains.

Organon rendering:

> The domain-system is now mapped onto planes of existence. Kāmadhātu is the full sensory field. Rūpadhātu preserves form and higher sensory structure but excludes the smell/taste complex tied to gross desire embodiment.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| kāmadhātu | desire-domain | full eighteen-domain field |
| rūpadhātu | form-domain | fourteen-domain field |
| gandha | smell | excluded in form-domain |
| rasa | taste | excluded in form-domain |
| ghrāṇavijñāna | smell-knowledge | excluded in form-domain |
| jihvāvijñāna | taste-knowledge | excluded in form-domain |

## 8. Logical Determination

```text
kāmadhātu
    = all eighteen domains

rūpadhātu
    = eighteen minus four
    = fourteen domains
```

## 9. Interpretive Note

This verse shows that realms are not merely places. They are domain-configurations. Kāmadhātu has the full entanglement of sensory object and knowledge. Rūpadhātu is a refined configuration, with smell and taste removed.

Organon note:

```text
realm
    = configuration of active domains
```

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_30 a vak:Karika ;
    vak:hasSourceLabel "VAkK_1.30" ;
    vak:hasProjectLabel "VAkK_1.30" ;
    vak:hasTopic vak:RealmConfigurationOfDomains .
```

## 11. Commit History

- Upgraded VAK_1.30 with expanded Organon analysis.
- Classifies all eighteen domains in kāmadhātu and fourteen in rūpadhātu.
- Reads realm as domain-configuration rather than mere location.
