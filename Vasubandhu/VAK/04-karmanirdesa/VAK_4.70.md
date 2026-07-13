# VAK_4d — VAkK_4.70

## 1. Sanskrit — Devanāgarī

वधव्यापादपारुष्यनिष्ठा द्वेषेण लोभतः ।
परस्त्रीगमनाभिध्यादत्तादानसमापनम् ॥ VAkK_4.70 ॥

## 2. Sanskrit — IAST

vadha-vyāpāda-pāruṣya-niṣṭhā dveṣeṇa lobhataḥ /
para-strī-gamanābhidhyādattādāna-samāpanam // VAkK_4.70 //

## 3. Padaccheda

| Sandhi form | Padaccheda | Basic meaning |
|---|---|---|
| vadha | vadha | killing |
| vyāpāda | vyāpāda | ill will |
| pāruṣya | pāruṣya | harsh speech |
| niṣṭhā | niṣṭhā | completion / culmination |
| dveṣeṇa | dveṣeṇa | through hatred |
| lobhataḥ | lobhataḥ | through greed |
| para-strī-gamana | para-strī-gamana | sexual misconduct |
| abhidhyā | abhidhyā | covetousness |
| adatta-ādāna | adatta-ādāna | taking what is not given |
| samāpanam | samāpanam | completion |

Expanded construction:

```text
killing
ill will
harsh speech
    completed through hatred

sexual misconduct
covetousness
taking what is not given
    completed through greed
```

## 4. Grammar

`vadha-vyāpāda-pāruṣya-niṣṭhā` is a distributive compound: the completion of killing, ill will, and harsh speech. `dveṣeṇa` is instrumental singular, expressing the completing root. `lobhataḥ` is ablative singular, “from / through greed.” `samāpanam` applies distributively to sexual misconduct, covetousness, and taking what is not given.

The two completion terms, `niṣṭhā` and `samāpana`, function in parallel here, though their exact nuance remains for the Bhāṣya pass.

## 5. Literal Translation

The completion of killing, ill will, and harsh speech is through hatred. From greed comes the completion of sexual misconduct, covetousness, and taking what is not given.

## 6. Philosophical Translation

Although the broader preparation of an unwholesome course may involve several afflictive roots, its decisive completion has a characteristic ground. Killing, harmful intent, and harsh speech culminate through hatred; sexual misconduct, covetousness, and theft culminate through greed.

## 7. Technical Vocabulary

### vadha

Killing or destruction of life. The fuller karmapatha term is `prāṇātipāta`.

### vyāpāda

Ill will, harmful intent, or the directed wish for another’s injury.

### pāruṣya

Harshness or injurious speech; an abbreviation of `pāruṣya-vāc`.

### dveṣa

Hatred, aversion, or hostile negation. It completes courses whose defining movement is destructive or injurious.

### para-strī-gamana

Literally, “going to another’s wife.” In the broader doctrine it belongs under sexual misconduct, `kāma-mithyācāra`.

### abhidhyā

Covetousness: appropriative fixation upon another’s possession.

### adattādāna

Taking what is not given; theft.

### lobha

Greed, attachment, or appropriative desire. It completes courses whose defining movement is acquisition or possession.

### niṣṭhā / samāpana

Completion or culmination: the threshold at which preparation becomes a completed karmapatha.

## 8. Doctrinal Determination

VAK_4.68–4.69 established that preparation may arise from greed, hatred, or delusion. VAK_4.70 now classifies the characteristic root at completion.

```text
Completed through hatred:
    killing
    ill will
    harsh speech

Completed through greed:
    sexual misconduct
    covetousness
    taking what is not given
```

The historical motive-complex may be plural, while the formal completion-root is determinate. Theft may be prepared from hatred or delusion, but as the completed course of taking what is not given its defining root is greed. Killing may be prepared for profit, yet its completed destructive form is classified through hatred.

## 9. Logical Determination

The verse distinguishes genetic ground from formal ground of completion.

```text
Why did the process begin?
    genetic root or mixture of roots

What makes the completed act this kind of act?
    characteristic completion-root
```

Hatred is the universal pattern of hostile negation instantiated in killing, ill will, and harsh speech. Greed is the universal pattern of improper appropriation instantiated in sexual misconduct, covetousness, and theft.

## 10. Light Organon Interpretation

A moral processor should retain both motivational history and completion classification.

```text
MoralProcess
    hasMotivationalHistory
    hasCompletionRoot
```

These need not coincide. Killing for profit may have greed in its motivational history while hatred remains its formal completion-root. Theft undertaken to humiliate an enemy may involve hatred while greed remains the constitutive root of the completed course.

The verse therefore yields two general failure operators:

```text
Dveṣa
    destructive negation of another

Lobha
    improper appropriation of another or another’s object
```

## 11. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_70
    a vak:Karika ;
    rdfs:label "VAkK 4.70" ;
    vak:continues vak:VAK_4_69 ;
    vak:hasTopic vak:CompletionRoots .

vak:Killing vak:hasCompletionRoot vak:Hatred .
vak:IllWill vak:hasCompletionRoot vak:Hatred .
vak:HarshSpeech vak:hasCompletionRoot vak:Hatred .

vak:SexualMisconduct vak:hasCompletionRoot vak:Greed .
vak:Covetousness vak:hasCompletionRoot vak:Greed .
vak:TakingWhatIsNotGiven vak:hasCompletionRoot vak:Greed .

vak:Hatred
    a vak:CompletionRoot ;
    vak:hasFormalPattern vak:HostileNegation .

vak:Greed
    a vak:CompletionRoot ;
    vak:hasFormalPattern vak:ImproperAppropriation .
```

Constraint:

```text
hasPreparatoryRoot(?x, ?root)
does not imply
hasCompletionRoot(?x, ?root)
```

## 12. Commit Note

Committed VAK_4d / VAkK_4.70.

Established:
- causal preparation differs from formal completion
- killing, ill will, and harsh speech complete through hatred
- sexual misconduct, covetousness, and taking what is not given complete through greed
- hatred formalizes hostile negation
- greed formalizes improper appropriation
- VAK_4.71 will complete the root classification

First-pass determination:

```text
preparatory roots
    may be plural

completion root
    is formally determinate
```