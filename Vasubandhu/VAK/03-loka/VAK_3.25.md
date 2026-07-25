# VAK_3b — VAkK_3.25

## Sanskrit — Devanāgarī

आवस्थिकः किलेष्टोऽयं प्राधान्यात्त्वङ्गकीर्तनम् ।
पूर्वापरान्तमध्येषु संमोहविनिवृत्तये ॥ VAkK_3.25 ॥

## Sanskrit — IAST

āvasthikaḥ kileṣṭo 'yaṃ prādhānyā ttvaṅgakīrtanam /
pūrvāparāntamadhyeṣu saṃmohavinivṛttaye // VAkK_3.25 //

## Source Resolution

The source sandhi is compact:

```text
āvasthikaḥ kileṣṭo 'yaṃ prādhānyā ttvaṅgakīrtanam
```

Resolved cautiously:

```text
āvasthikaḥ kila iṣṭaḥ ayam prādhānyāt tu aṅga-kīrtanam
```

## Padaccheda

| Sandhi form | Padaccheda | Basic meaning |
|---|---|---|
| āvasthikaḥ | āvasthikaḥ | pertaining to stages / states |
| kila | kila | indeed; it is said; traditionally accepted |
| iṣṭaḥ | iṣṭaḥ | accepted; intended; held |
| ayam | ayam | this |
| prādhānyāt | prādhānyāt | because of predominance |
| tu | tu | but; however |
| aṅgakīrtanam | aṅga-kīrtanam | naming / mention of the limbs |
| pūrvāparāntamadhyeṣu | pūrva-apara-anta-madhyeṣu | in the prior, later, and middle sections |
| saṃmohavinivṛttaye | saṃmoha-vinivṛttaye | for the removal of confusion |

## Grammar

```text
āvasthikaḥ
    nominative singular masculine
    = stage-based; state-based

kila iṣṭaḥ ayam
    = this is indeed accepted / intended

prādhānyāt tu
    ablative of cause
    = but because of predominance

aṅga-kīrtanam
    nominative singular neuter
    = the naming or mention of a limb

pūrva-apara-anta-madhyeṣu
    locative plural compound
    = in the prior limit, later limit, and middle

saṃmoha-vinivṛttaye
    dative singular
    = for the removal of confusion
```

## Literal Translation

This is indeed accepted as stage-based. But the naming of the limbs is due to predominance, for the removal of confusion concerning the prior limit, later limit, and middle.

## Philosophical Translation

This twelvefold dependent co-arising is to be understood as a sequence of stages or conditions. The individual limbs are named according to what is predominant in each stage, in order to remove confusion about the past, future, and middle sections of the process.

## Technical Vocabulary

| Sanskrit | Working translation | Note |
|---|---|---|
| āvasthika | stage-based / state-based | The limbs are phases or conditions, not isolated substances |
| avasthā | state / stage | Developmental condition or phase |
| iṣṭa | accepted / intended | Marks doctrinal acceptance |
| prādhānya | predominance | A limb is named by what predominates in that phase |
| aṅga | limb / member | Functional member of dependent co-arising |
| kīrtana | naming / mention | Doctrinal naming rather than ontological isolation |
| pūrvānta | prior limit | Past section |
| aparānta | later limit | Future section |
| madhya | middle | Present section |
| saṃmoha | confusion / delusion | Confusion about the three temporal sections |
| vinivṛtti | removal / cessation | Removal of confusion |

## Doctrinal Determination

VAkK_3.25 interprets the enumeration of 3.20–3.24.

The twelve limbs are not twelve isolated entities. They are **āvasthika**: stage-based determinations.

```text
Dependent co-arising
    = a stage-based sequence

Each limb-name
    = named by predominance

Purpose
    = removal of confusion about prior, middle, and later sections
```

This is crucial. Vasubandhu is not merely listing things. He is explaining why the series is named the way it is.

```text
Avidyā is named because ignorance predominates.
Saṃskāra is named because formations predominate.
Vijñāna is named because knowledge predominates.
And so on through the series.
```

The limb-name is therefore a dominant marker of a stage.

## Logical Determination

The verse gives the rule of denomination.

```text
stage
    has many factors

one factor predominates
    therefore the stage is named by that factor
```

So the logic is:

```text
Multiplicity of conditions
    ↓
Predominant determination
    ↓
Named limb
```

This prevents the mistaken view that each limb is a separate substantial thing.

```text
aṅga
    = predominant function within a stage

not:
    isolated substance
```

This also explains why the twelvefold chain can be both sequential and composite. Each stage contains multiple factors, but one factor gives the name.

## Interpretive Note

This verse is a major methodological correction. It tells us how to read the whole preceding enumeration.

The twelve limbs are not atoms in a causal chain. They are stages named by predominance.

This supports a cautious reading of 3.22 and 3.23: `nāmarūpa`, `ṣaḍāyatana`, `sparśa`, `vittiḥ`, `tṛṣṇā`, and `upādāna` are not isolated mental objects. They are dominant determinations within a developmental phase.

## Organon Interpretation

Speculatively, VAkK_3.25 gives the rule for modeling dependent co-arising as a structured process.

```text
Stage
    = complex state of the system

Predominance
    = dominant feature / marker

Limb-name
    = semantic label of the dominant feature
```

In Organon terms:

```text
Process-state
    contains many factors

Dominant factor
    becomes the named mark

Named mark
    organizes the stage in the doctrinal model
```

This is very close to feature-dominance in a semantic dataset. But that remains interpretive. The primary doctrinal point is simpler and stronger: the limbs are stage-names by predominance, intended to remove confusion about past, present, and future.

## OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_25
    a vak:Karika ;
    rdfs:label "VAkK 3.25" ;
    vak:continues vak:VAK_3_24 ;
    vak:hasTopic vak:DependentCoArising ;
    vak:statesMethod vak:StageBasedDenomination ;
    vak:statesPurpose vak:RemovalOfConfusion .

vak:StageBasedDenomination
    a logic:Method ;
    rdfs:label "stage-based denomination" ;
    vak:hasSanskrit "āvasthika" ;
    rdfs:comment "The limbs are understood as stages named according to the factor that predominates in each stage." .

vak:Predominance
    a logic:DeterminingFunction ;
    rdfs:label "predominance" ;
    vak:hasSanskrit "prādhānya" .

vak:LimbNaming
    a logic:Denomination ;
    rdfs:label "aṅga-kīrtana" ;
    logic:dependsOn vak:Predominance .

vak:RemovalOfConfusion
    a logic:Purpose ;
    rdfs:label "removal of confusion" ;
    vak:hasSanskrit "saṃmoha-vinivṛtti" ;
    vak:concerns vak:PurvantaSection ;
    vak:concerns vak:MadhyaSection ;
    vak:concerns vak:AparantaSection .
```

## Commit Note

Committed VAK_3b / VAkK_3.25.

Established:
- the twelve limbs are āvasthika, stage-based.
- the naming of a limb is due to prādhānya, predominance.
- aṅga-kīrtana is denomination by dominant function, not isolation of a substance.
- the purpose is the removal of confusion about prior limit, middle, and later limit.

Logical determination:
VAkK_3.25 gives the method for reading the twelvefold chain. Each limb is a stage-name based on the factor predominant in that stage. This prevents a substance-like reading of the twelve limbs and prepares the structural analysis in 3.26–3.27.
