# VAK_2.31

## 1. Sanskrit (Devanāgarī)

> कौकृत्यमिद्धाकुशलान्याद्ये ध्याने न सन्त्यतः ।
>
> ध्यानान्तरे वितर्कश्च विचारश्चाप्यतः परम् ॥ २.३१ ॥

## 2. Sanskrit (IAST)

> kaukṛtyamiddhākuśalāny ādye dhyāne na santy ataḥ /
>
> dhyānāntare vitarkaś ca vicāraś cāpy ataḥ param // 2.31 //

## 3. Lexical Analysis

```text
kaukṛtyamiddhākuśalāny → kaukṛtya-middha-akuśalāni
ādye                   → ādye
dhyāne                 → dhyāne
na santy               → na santi
ataḥ                   → ataḥ
dhyānāntare            → dhyāna-antare
vitarkaś ca            → vitarkaḥ ca
vicāraś cāpy           → vicāraḥ ca api
ataḥ param             → ataḥ param
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| kaukṛtya | compound member | remorse |
| middha | compound member | torpor |
| akuśalāni | nominative neuter plural | unwholesome factors |
| ādye dhyāne | locative singular phrase | in the first dhyāna |
| na santi | third-person plural present with negation | are absent |
| ataḥ | indeclinable | from the foregoing distribution |
| dhyāna-antare | locative singular compound | in the intermediate dhyāna |
| vitarkaḥ | nominative masculine singular | *vitarka* |
| vicāraḥ | nominative masculine singular | *vicāra* |
| api | additive particle | also |
| ataḥ param | indeclinable phrase | beyond this level |

*Dhyānāntara* is the intermediate level between the first and second
dhyānas, as specified by the Bhāṣya.

## 4. Grammar

The first clause identifies factors absent at the first level:

```text
ādye dhyāne
    → in the first dhyāna

kaukṛtya-middha-akuśalāni na santi
    → remorse, torpor, and factors in unwholesome mode are absent
```

The Bhāṣya qualifies the last member. Crookedness, intoxication, and
deception are exceptions among the named affliction factors at the
first-dhyāna/Brahmā level.

The exclusions are cumulative:

```text
intermediate dhyāna:
    previous exclusions + vitarka

second dhyāna and above, including formless attainments:
    previous exclusions + vicāra
    and, by the Bhāṣya's reading of api, deception and crookedness
```

The later exclusion does not include intoxication.

## 5. Scientific English Rendering

### Kārikā

> Remorse, torpor, and unwholesome factors are absent in the first
> dhyāna. In the intermediate dhyāna, *vitarka* is absent as well;
> beyond this, *vicāra* also.

### Bhāṣya-informed rendering

> Of the factors described, remorse and torpor are entirely absent in the
> first dhyāna, as are factors operating in an unwholesome mode: hostility,
> the factors beginning with anger except crookedness, intoxication, and
> deception, and shamelessness and absence of moral caution. Everything
> else remains as before. Those absent in the first dhyāna are also absent
> in the intermediate dhyāna, together with *vitarka*. The remainder is
> as before. Beyond the intermediate dhyāna, in the second and subsequent
> dhyānas and in the Formless levels, *vicāra* is also absent, along with
> deception and crookedness. The remainder is as before.

The Bhāṣya explains that crookedness is recounted only as far as Brahmā,
because it is connected with an assembly. Aśvajit questions Brahmā about
where the four Great Principles cease without remainder. Not knowing,
Brahmā evades the question by declaring, “I am Brahmā, Lord, Maker,
Fashioner, Creator, Producer, Father of beings.” The transmitted title
sequence is imperfect; the English rendering is provisional.

## 6. Interpretation

The verse turns the previous count profiles into level-specific exclusions.
The first dhyāna excludes remorse, torpor, and unwholesome operation, but
the Bhāṣya preserves exceptions for crookedness, intoxication, and
deception. At the intermediate level, *vitarka* is additionally absent;
above it, *vicāra* is absent as well, and the Bhāṣya reads *api* to add
deception and crookedness. Intoxication is not included in that later
exclusion.

The Brahmā episode illustrates the specific assembly-related range of
crookedness: a display of authority evades a question the speaker cannot
answer. Its argument is local; status alone does not establish knowledge.
The commentary's conclusion is a level-indexed count of mental factors,
not a claim that every consciousness at a level is identical.

The Kośa's governing synthesis: Vijñāna is Discriminative Cognition joining
and governing Perception and Conception. Their unity is Inconceivable as a
homogeneous operation; its Idea is disclosed in the Cognition Base. Vijñāna
governs Mind and guides the reading of Dharma Base. Form Base and Dharma
Base both include the same *avijñapti* in distinct classifications, and
Vijñāna bears a *prati* relation to *avijñapti*. This architecture remains
distinct from the local level-indexed factor exclusions.

## 7. Logical Determination

```text
FirstDhyana:
    Excludes(Remorse, Torpor, UnwholesomeMode)
    Retains(Vitarka, Vicara)
    ExceptionsAmongNamedAfflictions = {Crookedness, Intoxication, Deception}

IntermediateDhyana:
    Inherits(FirstDhyanaExclusions)
    Excludes(Vitarka)
    Retains(Vicara)

SecondAndHigherDhyanaOrFormless:
    Inherits(IntermediateDhyanaExclusions)
    Excludes(Vicara, Deception, Crookedness)
```

The first-dhyāna statement excludes factors in an unwholesome mode; it
does not erase every factor elsewhere classified as an affliction in
every mode.

## 8. Interpretive Note

The levels form a cumulative exclusion rule, but not a complete account
of every mental-factor possibility at each level. “The remainder is as
before” carries forward unchanged classifications. The exceptions and
the specific scope of *api* must be retained to avoid overextending the
exclusion.

The Bhāṣya distinguishes *middha*, torpor, from *styāna*, sluggishness,
and *mada*, intoxication, from *māna*, conceit. These lexical distinctions
matter to the count and exclusions.

## 9. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_31
    a vak:Karika ;
    rdfs:label "VAK 2.31" ;
    vak:hasTopic vak:DhyanaLevelFactorExclusions ;
    vak:belongsTo vak:Indriyanirdesa .

vak:FirstDhyanaProfile
    vak:excludes vak:Remorse,
        vak:Torpor,
        vak:UnwholesomeOperation ;
    vak:retains vak:Vitarka,
        vak:Vicara ;
    vak:hasExceptions vak:Crookedness,
        vak:Intoxication,
        vak:Deception .

vak:IntermediateDhyanaProfile
    vak:inheritsExclusionsFrom vak:FirstDhyanaProfile ;
    vak:excludes vak:Vitarka ;
    vak:retains vak:Vicara .

vak:HigherDhyanaAndFormlessProfile
    vak:inheritsExclusionsFrom vak:IntermediateDhyanaProfile ;
    vak:excludes vak:Vicara,
        vak:Deception,
        vak:Crookedness .
```
