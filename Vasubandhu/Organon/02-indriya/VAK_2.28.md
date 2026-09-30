# VAK_2.28

## 1. Sanskrit (Devanāgarī)

> सवितर्कविचारत्वात् कुशले कामचेतसि ।
>
> द्वाविंशतिश्चैतसिकाः कौकृत्यमधिकं क्वचित् ॥ २.२८ ॥

## 2. Sanskrit (IAST)

> savitarkavicāratvāt kuśale kāmacetasi /
>
> dvāviṃśatiś caitasikāḥ kaukṛtyam adhikaṃ kvacit // 2.28 //

The research source-form line gives `dvāṃviṃśatiḥ`; the regular numeral
`dvāviṃśatiḥ`, “twenty-two,” is adopted here. The research witness remains
unchanged.

## 3. Padaccheda

```text
savitarkavicāratvāt → sa-vitarka-vicāratvāt
kuśale             → kuśale
kāmacetasi         → kāma-cetasi
dvāviṃśatiś        → dvāviṃśatiḥ
caitasikāḥ         → caitasikāḥ
kaukṛtyam          → kaukṛtyam
adhikaṃ            → adhikam
kvacit             → kvacit
```

| Form | Morphology | Lexical force here |
|---|---|---|
| sa-vitarka-vicāratvāt | ablative singular abstract compound | because of being accompanied by `vitarka` and `vicāra` |
| kuśale | locative neuter singular | in wholesome [consciousness] |
| kāma-cetasi | locative neuter singular compound | in a desire-realm consciousness-event |
| dvāviṃśatiḥ | nominative feminine singular numeral | twenty-two |
| caitasikāḥ | nominative masculine plural | mental factors |
| kaukṛtyam | nominative neuter singular | remorse / troubled reconsideration |
| adhikam | nominative neuter singular | additional |
| kvacit | indeclinable | sometimes / in some cases |

The ablative `-tvāt` gives the reason for the base count. `Kvacit` restricts
the addition of remorse and prevents it from being assimilated to the factors
universally present in wholesome consciousness.

## 4. Grammar

The base rule is:

```text
kuśale kāma-cetasi
    → in a wholesome desire-realm consciousness-event

sa-vitarka-vicāratvāt
    → because it is accompanied by vitarka and vicāra

dvāviṃśatiḥ caitasikāḥ
    → there are 22 mental factors
```

The Bhāṣya expands the count:

```text
10 universal great-ground factors
+ 10 wholesome great-ground factors
+ vitarka
+ vicāra
= 22
```

The second clause gives a conditional extension:

```text
kaukṛtyam adhikam kvacit
    → in some cases remorse is an additional factor
```

Therefore `kaukṛtya` produces twenty-three only when actually associated
with the wholesome event. It is not a member of the wholesome great-ground
class.

## 5. Translation

### Close syntactic construe

> Because wholesome desire-realm consciousness is accompanied by `vitarka` and `vicāra`, there are twenty-two mental factors; in some cases remorse is additional.

### Bhāṣya-informed translation

> A wholesome desire-realm consciousness-event necessarily contains the ten universal factors, the ten wholesome great-ground factors, `vitarka`, and `vicāra`, making twenty-two. When wholesome remorse is also present, it is a conditional twenty-third factor.

The Bhāṣya defines wholesome remorse as regret over having performed what is
unwholesome or having failed to perform what is wholesome. Painful or
self-critical affect by itself does not make remorse wholesome.

## 6. Philosophical Translation

> The five ground-classes now become an actual event calculation. Realm and ethical determination select two required factor-sets, while the discursive constitution of desire-realm consciousness supplies `vitarka` and `vicāra`. Remorse does not belong to this invariant base: it arises only when consciousness retrospectively judges an action or omission as badly done.

Restrained Organon rendering:

> A mental profile is assembled from inherited ground requirements, realm requirements, and conditional factors. Optional does not mean untyped: remorse must be validated by its evaluative direction, because the same remembered action can support wholesome or unwholesome regret.

The profile language is project-level. The textual doctrine gives the exact
twenty-two/ twenty-three counts and the ethical determination of remorse.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Bhāṣya determination |
|---|---|---|
| kāma-cetas | desire-realm consciousness | necessarily accompanied here by `vitarka` and `vicāra` |
| vitarka | `vitarka` / initial application | semi-technical factor counted in every desire-realm consciousness-event |
| vicāra | `vicāra` / sustained examination | semi-technical factor counted with `vitarka` here |
| caitasika | mental factor | associated determination of consciousness |
| kaukṛtya | remorse / regret | conditional mental factor directed toward an action or omission judged badly done |
| vipratisāra | troubled reconsideration / remorse | Bhāṣya definition of the mental factor called `kaukṛtya` |
| kukṛta | badly done | action or omission serving as the cognitive basis for remorse |
| sthāna / sthānin | locus / occupant | analogy for transfer of a basis-name to what occurs in relation to it |
| hetūpacāra | causal transfer of designation | semantic explanation in which a related cause or result supplies the name |
| ubhayādhiṣṭhāna | based on either kind | wholesome and unwholesome remorse can each concern wholesome or unwholesome conduct |
| kvacit | sometimes | marks genuine conditional association rather than ground-wide necessity |

`Kaukṛtya` literally derives from what is badly done, but technically names
the mental remorse that takes such doing—or a failure to act—as its cognitive
basis. The basis and the factor must remain distinct.

## 8. Logical Determination

The mandatory base is:

```text
WholesomeDesireBase =
      UniversalGreatGroundTen
    ∪ WholesomeGreatGroundTen
    ∪ {Vitarka, Vicāra}

Count(WholesomeDesireBase) = 22
```

The conditional extension is:

```text
Factors(e) = WholesomeDesireBase
    when ¬HasRemorse(e)

Factors(e) = WholesomeDesireBase ∪ {Remorse}
    when HasRemorse(e)

Count = 22 or 23 respectively
```

The ethical direction of remorse is:

```text
WholesomeRemorse(e) iff
       Regrets(e, Commission(UnwholesomeAction))
    or Regrets(e, Omission(WholesomeAction))

UnwholesomeRemorse(e) iff
       Regrets(e, Commission(WholesomeAction))
    or Regrets(e, Omission(UnwholesomeAction))
```

The conduct-type alone does not determine the remorse-type:

```text
EthicalStatus(BasisOfRemorse)
    ⇏ EthicalStatus(Remorse)

EthicalStatus(Remorse)
    = f(ConductType, CommissionOrOmission,
        EvaluativeDirection)
```

The technical name also encodes a semantic relation:

```text
Name(Remorse) derivesFrom Name(BadlyDoneBasis)

NameTransfer(basis, factor)
    ⇏ Identity(basis, factor)
```

## 9. Interpretive Note

VAK 2.28 changes levels from class definition to event composition. The
preceding verses established which factors range through every consciousness
and every wholesome consciousness. A wholesome desire-realm event inherits
both sets. Because desire-realm consciousness is also accompanied by
`vitarka` and `vicāra`, its necessary total is twenty-two.

The calculation is compositional:

```text
universal ground inheritance
    + wholesome ground inheritance
    + realm-specific factors
    + conditional event factors
```

`Kaukṛtya` is the first explicit conditional addition. The word `kvacit`
protects the distinction drawn in VAK 2.27: not every named factor belongs to
a required ground-bundle. Remorse can be wholesome, but it is not present in
every wholesome event.

The Bhāṣya's semantic discussion is as important as the count. The badly done
action is not identical with remorse. Its name is transferred to the mental
factor that retrospectively takes it as a cognitive basis. An omission can
enter the same structure because consciousness can judge “not doing” as what
was badly done.

Ethical classification then depends upon evaluative direction. Regretting an
unwholesome commission or a wholesome omission is wholesome; regretting a
wholesome commission or an unwholesome omission is unwholesome. Both kinds of
remorse can therefore concern either wholesome or unwholesome conduct. The
content alone does not mechanically transmit its ethical status to the act of
evaluation.

For the Kośa Technē, the restrained consequence is:

```text
MentalEventProfile
    = inherited required factors
    + realm-conditioned factors
    + zero or more licensed optional factors

OptionalFactorStatus
    requires relational evaluation
    not name matching or affect matching
```

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_28
    a vak:Karika ;
    rdfs:label "VAK 2.28" ;
    vak:hasTopic vak:WholesomeDesireRealmCaittaProfile ;
    vak:belongsTo vak:Indriyanirdesa .

vak:WholesomeDesireRealmCaittaProfile
    vak:inherits vak:UniversalGreatGroundTen,
        vak:WholesomeGreatGroundTen ;
    vak:requires vak:Vitarka,
        vak:Vicara ;
    vak:hasBaseCount 22 ;
    vak:hasOptionalFactor vak:Remorse ;
    vak:hasExtendedCount 23 .

vak:Remorse
    vak:hasCognitiveBasis vak:ActionOrOmissionJudgedBadlyDone ;
    vak:ethicalStatusDeterminedBy vak:EvaluativeDirection ;
    vak:notUniversallyPresentIn vak:WholesomeCitta .

organon:MentalEventProfile
    a organon:InterpretiveReconstruction ;
    organon:combines organon:InheritedGroundRequirements,
        organon:RealmConditionedFactors,
        organon:LicensedOptionalFactors ;
    organon:inferredFrom vak:WholesomeDesireRealmCaittaProfile .
```
