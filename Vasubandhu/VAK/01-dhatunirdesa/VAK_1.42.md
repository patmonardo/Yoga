# VAK_1.42

## 1. Sanskrit (Devanāgarī)

> चक्षुः पश्यति रूपाणि सभागं न तदाश्रितम् ।
>
> विज्ञानं दृश्यते रूपं न किलान्तरितं यतः ॥ १.४२ ॥

## 2. Sanskrit (IAST)

> cakṣuḥ paśyati rūpāṇi sabhāgaṃ na tadāśritam /
>
> vijñānaṃ dṛśyate rūpaṃ na kilāntaritaṃ yataḥ // VAkK_1.42 //

Source saṃhitā form:

> cakṣuḥ paśyati rūpāṇi sabhāgaṃ na tadāśritam /
>
> vijñānaṃ dṛśyate rūpaṃ na kilāntaritaṃ yataḥ // VAkK_1.42 //

## 3. Padaccheda

| Form | Padaccheda | Meaning |
|---|---|---|
| cakṣuḥ | cakṣuḥ | eye-domain |
| paśyati | paśyati | sees |
| rūpāṇi | rūpāṇi | visible forms |
| sabhāgam | sabhāgam | functioning member |
| na tadāśritam | na tad-āśritam | not what is dependent on it |
| vijñānam | vijñānam | knowledge |
| dṛśyate | dṛśyate | is seen / is regarded as seeing |
| rūpam | rūpam | visible form |
| na kila | na kila | surely not |
| antaritam | antaritam | obstructed, intervened, screened off |
| yataḥ | yataḥ | because, since |

## 4. Grammar

The first claim is direct:

```text
cakṣuḥ paśyati rūpāṇi
    the eye sees visible forms
```

But this is restricted:

```text
sabhāgam
    the functioning eye-domain

na tadāśritam
    not the knowledge dependent on it
```

Thus the seeing is predicated of the eye-domain as functionally active, not of the dependent eye-knowledge.

The second half gives the reason:

```text
vijñānam ... rūpam na antaritam
```

Knowledge is not the seer in this strict sense because the visible form is not obstructed from the eye. If form is not screened off from the eye, the eye is the seeing-domain.

## 5. Literal Translation

> The eye sees visible forms, the functioning [eye], not what is dependent on it. Knowledge [does not see]; visible form is surely not obstructed, because of this.

## 6. Philosophical Translation

> It is the functioning eye-domain that sees visible form, not the eye-knowledge that depends upon it. Since visible form is not obstructed from the eye, seeing is attributed to the operative faculty-domain rather than to the dependent knowledge-domain.

Organon rendering:

> Seeing is not a disembodied act of knowledge. It belongs to the functioning visual faculty. Knowledge depends upon the faculty, but the unobstructed relation between eye and visible form grounds the act of seeing.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| cakṣus | eye-domain | visual faculty-domain |
| paśyati | sees | operation of the functioning eye |
| rūpa | visible form | object-domain of the eye |
| sabhāga | functioning member | performs its own function |
| tadāśrita | dependent on it | the eye-knowledge dependent on eye |
| vijñāna | knowledge | here not the strict seer |
| antarita | obstructed / screened | visual relation blocked by intervention |

## 8. Logical Determination

VAK_1.41 distinguished seeing from sensory co-born intelligence. VAK_1.42 now asks where seeing is located.

```text
seeing
    belongs to functioning eye-domain

not to:
    dependent eye-knowledge-domain
```

The logical structure is:

```text
faculty-domain
    = functional condition of seeing

knowledge-domain
    = dependent disclosure

visible form
    = unobstructed object-domain
```

Thus:

```text
condition
    is not collapsed into act

act
    is not detached from condition
```

## 9. Interpretive Note

This verse is a precision instrument. It does not deny knowledge; it assigns roles.

The eye sees when it is **sabhāga**, functionally actual. Eye-knowledge depends on that operative eye, but the verse refuses to make knowledge the independent seer.

This matters after VAK_1.38, which distinguished eye-domain and eye-knowledge-domain through acquisition. Now VAK_1.42 gives the functional version of that same distinction:

```text
eye-domain
    = operative condition of seeing

eye-knowledge-domain
    = dependent disclosure
```

Organon sequence:

```text
1.41 seeing requires ascertainment
1.42 seeing is grounded in functional faculty
```

Kant-Fichte-Hegel note:

```text
intuition is not free-floating representation.
It is grounded in a determinate faculty-condition.
But knowledge is not abolished;
it is the dependent disclosure of that condition.
```

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_42
    a vak:Karika ;
    rdfs:label "VAK 1.42" ;
    vak:hasIAST "cakṣuḥ paśyati rūpāṇi sabhāgaṃ na tadāśritam / vijñānaṃ dṛśyate rūpaṃ na kilāntaritaṃ yataḥ" ;
    vak:hasTopic vak:SeeingByFunctionalEye ;
    vak:belongsTo vak:Dhatunirdesa .

vak:FunctionalEyeDomain
    a vak:FacultyDomain ;
    rdfs:label "functioning eye-domain" ;
    vak:hasStatus vak:Sabhaga ;
    vak:performs vak:Seeing .

vak:EyeKnowledgeDomain
    a vak:KnowledgeDomain ;
    rdfs:label "eye-knowledge-domain" ;
    vak:dependsOn vak:FunctionalEyeDomain ;
    vak:notPrimaryAgentOf vak:Seeing .

vak:VisibleForm
    a vak:ObjectDomain ;
    rdfs:label "visible form" ;
    vak:notObstructedFrom vak:FunctionalEyeDomain .
```

## 11. Commit History

- Added Organon analysis for VAK_1.42.
- Establishes the functioning eye-domain as the seer of visible form.
- Distinguishes the eye-domain from the eye-knowledge dependent on it.
- Connects **sabhāga** from VAK_1.39 to the act of seeing.
- Reads unobstructed visible form as grounding the attribution of seeing to the eye.
