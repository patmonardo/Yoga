# VAK_4.08 — Originating Conditions and Modes of Goodness

## 1. Sanskrit — Devanāgarī

```sanskrit
कामेऽपि निवृता नास्ति समुत्थानमसद्यतः ।
परमार्थशुभो मोक्षः स्वतो मूलह्य्रपत्रपाः ॥
```

## 2. Sanskrit — IAST

```iast
kāme ’pi nivṛtā nāsti samutthānam asad yataḥ |
paramārthaśubho mokṣaḥ svato mūla-hrī-apatrapāḥ ||
```

## 3. Source Caution

External source siglum: VAkK_4.8.

Provisional separation:

```iast
kāme api nivṛtā na asti |
samutthānam asat yataḥ |
paramārtha-śubhaḥ mokṣaḥ |
svataḥ mūla-hrī-apatrapāḥ ||
```

The first half continues the ethical classification from VAK_4.07. The likely understood subject is `avijñaptiḥ`. Here `nivṛta` most likely abbreviates `nivṛtāvyākṛta`, obscured-indeterminate or defiled-neutral. The second half begins a classification of what is called wholesome. The compound `mūla-hrī-apatrapāḥ` is provisionally read as a list: roots, hrī, and apatrāpya.

## 4. Padaccheda

| Transmitted form | Padaccheda | Working determination |
|---|---|---|
| kāme ’pi | kāme api | even in the desire domain |
| nivṛtā | nivṛtā | obscured; defiled-neutral |
| nāsti | na asti | does not exist |
| samutthānam | samutthānam | originating condition |
| asad | asat | bad; unwholesome |
| yataḥ | yataḥ | because |
| paramārthaśubhaḥ | paramārtha-śubhaḥ | wholesome in the ultimate sense |
| mokṣaḥ | mokṣaḥ | liberation |
| svataḥ | svataḥ | intrinsically |
| mūla | mūla | root |
| hrī | hrī | moral shame / ethical self-respect |
| apatrāpāḥ | apatrāpāḥ | moral circumspection |

## 5. Grammar

### `kāme ’pi nivṛtā nāsti`

The feminine `nivṛtā` most naturally qualifies the understood `avijñaptiḥ`:

> Even in the desire domain, there is no obscured-indeterminate avijñapti.

### `samutthānam asad yataḥ`

> Because its originating condition is unwholesome.

The line links the ethical character of non-manifest action to the character of the condition from which it arises.

### `paramārthaśubho mokṣaḥ`

> Liberation is wholesome in the ultimate sense.

### `svato mūla-hrī-apatrapāḥ`

The understood predicate is `śubhāḥ`:

> The roots, hrī, and apatrāpya are wholesome by their own nature.

## 6. Literal Translation

Even in the desire domain there is no obscured-indeterminate [avijñapti], because its originating condition is bad. Liberation is wholesome in the ultimate sense; the roots, moral shame, and moral circumspection are wholesome by their own nature.

## 7. Philosophical Translation

Non-manifest action is never merely defiled-neutral, not even within the desire domain, because the defiled source capable of generating it is classified as unwholesome. The verse then distinguishes modes of goodness: liberation is good in the ultimate sense, whereas the wholesome roots, moral self-respect, and moral regard are good intrinsically.

## 8. Technical Vocabulary

| Sanskrit | Working translation | Determination |
|---|---|---|
| nivṛta | obscured-indeterminate | defiled but not ethically classified as wholesome or unwholesome |
| samutthāna | originating condition | the activating source from which action proceeds |
| asat | bad / unwholesome | lexical contrary of good |
| paramārtha-śubha | ultimately wholesome | goodness belonging to liberation itself |
| mokṣa | liberation | release |
| hrī | moral shame / ethical self-respect | restraint in relation to oneself |
| apatrāpya | moral circumspection | restraint through regard for others |
| mūla | root | most likely wholesome root |

## 9. Doctrinal Determination

VAK_4.07 established that avijñapti is wholesome or unwholesome and never indeterminate. VAK_4.08 sharpens the exclusion: avijñapti is not obscured-indeterminate, even in kāmadhātu, because the originating condition capable of producing it is unwholesome rather than neutral.

The second half distinguishes:

```text
ultimate goodness
    mokṣa

intrinsic goodness
    roots
    hrī
    apatrāpya
```

## 10. Logical Determination

The first half links ethical status to origin:

```text
samutthāna
    → determines the ethical classification
      of produced action
```

The second half differentiates the predicate “good” according to why it belongs:

```text
liberation
    good in the ultimate sense

roots, hrī, apatrāpya
    good intrinsically
```

## 11. Interpretive Note

The word to watch is `samutthāna`. The verse gives a precise causal relation: an action has an originating condition, and the ethical character of that origin determines the character of the generated action.

## 12. Light Organon Interpretation

The predicate `śubha` is not univocal. It is differentiated according to the relation by which goodness belongs to its subject. This is enough for the first pass; deeper alignment with Ground or Path-Knowledge remains deferred.

## 13. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_08
    a vak:Karika ;
    rdfs:label "VAK 4.08" ;
    vak:continues vak:VAK_4_07 ;
    vak:hasTopic vak:NivrtaAvyakrta ;
    vak:hasTopic vak:Samutthana ;
    vak:hasTopic vak:ModesOfWholesomeness .

vak:Avijnapti
    vak:excludesEthicalQuality vak:ObscuredIndeterminate .

vak:UnwholesomeAvijnapti
    vak:arisesFrom vak:UnwholesomeOriginatingCondition .

vak:Moksa
    vak:hasWholesomeMode vak:UltimateWholesome .

vak:WholesomeRoot
    vak:hasWholesomeMode vak:IntrinsicallyWholesome .

vak:Hri
    vak:hasWholesomeMode vak:IntrinsicallyWholesome .

vak:Apatrapya
    vak:hasWholesomeMode vak:IntrinsicallyWholesome .
```

## 14. Verse Summary

```text
VAK_4.08

Avijñapti is not obscured-indeterminate,
even in the desire domain.

Its originating condition
is unwholesome rather than neutral.

Liberation
    is wholesome in the ultimate sense.

The wholesome roots,
hrī,
and apatrāpya
    are wholesome intrinsically.
```

## 15. Commit Note

Committed VAK_4.08.
