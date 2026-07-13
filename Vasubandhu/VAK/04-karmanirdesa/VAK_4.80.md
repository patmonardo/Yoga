# VAK_4.80

## 1. Sanskrit — Devanāgarī

छिनत्ति स्त्री पुमान् दृष्टिचरितः सोऽसमन्वयः ।  
संधिः काङ्क्षास्तिदृष्टिभ्यां नेहानन्तर्यकारिणः ॥ ४.८० ॥

## 2. Sanskrit — IAST

**chinatti strī pumān dṛṣṭi-caritaḥ so ’samanvayaḥ |**  
**saṃdhiḥ kāṅkṣāsti-dṛṣṭibhyāṃ nehānantarya-kāriṇaḥ || 4.80 ||**

Local source:

```text
chinatti strī pumān dṛṣṭicaritaḥ so 'samanvayaḥ /
saṃdhiḥ kāṅkṣāstidṛṣṭibhyāṃ nehānantaryakāriṇaḥ // VAkK_4.80 //
```

The verse continues the account of severing and reconnecting the roots of the wholesome.

## 3. Padaccheda

```text
chinatti
strī
pumān
dṛṣṭi-caritaḥ
saḥ
asamanvayaḥ
saṃdhiḥ
kāṅkṣā
asti-dṛṣṭibhyām
na
iha
ānantarya-kāriṇaḥ
```

Expanded sense:

> A woman or a man whose conduct is governed by view severs the wholesome roots; that person becomes non-endowed with them. Their reconnection occurs through doubt or through the view that they exist. For one who has committed an immediate-retribution action, however, it does not occur in this life.

## 4. Grammar

- **chinatti** — third-person singular present of √chid, “cuts, severs”; understood object: *kuśala-mūlāni*.
- **strī / pumān** — woman / man; either may sever the roots.
- **dṛṣṭi-caritaḥ** — one whose conduct is governed by view; not a passing opinion but a dominant practical orientation.
- **asamanvayaḥ** — non-endowment, non-possession; the continuum is no longer operatively endowed with the wholesome roots.
- **saṃdhiḥ** — junction, reconnection, restoration of continuity.
- **kāṅkṣā** — doubt or uncertainty.
- **asti-dṛṣṭi** — the view that karmic ground and result exist.
- **-bhyām** — instrumental dual: through either doubt or affirmative view.
- **na iha** — not here, not in this present life.
- **ānantarya-kāriṇaḥ** — of one who has committed an immediate-retribution action.

## 5. Literal Translation

> A woman or a man whose conduct is governed by view severs them; that person is non-endowed with them. Reconnection occurs through doubt or through the view that they exist, but not here for one who has committed an immediate-retribution action.

## 6. Philosophical Translation

> The severance of wholesome practical capacity is possible in any human continuum, female or male, when conduct becomes governed by a false principial standpoint. Severance means that the continuum is no longer endowed with the generative bases of wholesome activity. Reconnection begins when the closed certainty of denial is broken—either by doubt or by renewed affirmation that practical ground and consequence are real. Yet where radical false view has issued in an immediate-retribution action, the consequences of that completed activity prevent restoration within the present existence.

## 7. Technical Vocabulary

### dṛṣṭi-carita

Conduct governed by view. An isolated error is not enough; the view must function as the governing principle of the practical continuum.

### samanvaya / asamanvaya

`Samanvaya` is operative endowment within a continuum. `Asamanvaya` is non-endowment. Root-severance is therefore relational rather than substantial: the continuum ceases to possess the wholesome roots as active capacities.

### saṃdhi

Reconnection or restored continuity. The roots are not recreated from nothing; operative possession is re-established.

### kāṅkṣā

Doubt is negative relative to knowledge but positive relative to dogmatic false certainty. It breaks the closure of nihilistic denial.

### asti-dṛṣṭi

Affirmative view: karmic ground exists, karmic result exists, and the distinction between wholesome and unwholesome activity is valid.

### ānantarya-kārin

One who has completed an action whose result follows without an intervening birth. Such a completed act blocks reconnection in the present life.

## 8. Doctrinal Determination

VAK_4.79 restricted severance to humans in the desire domain. VAK_4.80 adds that either a woman or a man may sever the roots; the determining condition is view-governed conduct.

The result is `asamanvaya`: the continuum is no longer endowed with the wholesome roots.

Reconnection occurs through:

1. **Doubt** — the settled denial of karmic ground and result becomes uncertain.
2. **Affirmative view** — the existence of ground, result, and practical distinction is positively recognized.

Doubt is not complete wisdom. It is the transitional negation of radical error. The verse also distinguishes radical false view from radical false view completed in an immediate-retribution action: the latter prevents present-life reconnection.

## 9. Logical Determination

```text
EndowedWithWholesomeRoots(agent)
    ↓ established radical false view
NotEndowedWithWholesomeRoots(agent)
```

Reconnection begins when:

```text
¬P
    becomes
not-settled(¬P)
```

where `P` is the proposition that karmic ground and result exist.

The sequence is:

```text
nihilistic certainty
    → doubt
    → affirmative recognition
```

Doubt reopens possibility; affirmative view restores the principle. Neither by itself is identical with complete cultivation.

## 10. Light Organon Interpretation

The verse provides a model of system recoverability.

A corrupted system need not immediately possess a perfect replacement model. Recovery begins when it ceases treating its corrupt model as unquestionably final.

```text
CurrentSchemaMayBeWrong = true
```

That transition restores openness to correction.

`Samanvaya` can be treated as capability endowment; severance removes operative access to wholesome generative capacities, while reconnection rebinds them into the active context.

The immediate-action exception also distinguishes principial recovery from consequence reversibility:

```text
policy repair
    does not automatically rollback
all committed mutations
```

A corrected view may restore future capability while completed high-gravity actions continue toward their determinate result.

## 11. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_80
    a vak:Karika ;
    rdfs:label "VAkK 4.80" ;
    vak:continues vak:VAK_4_79 ;
    vak:hasTopic vak:SeveranceOfWholesomeRoots,
                 vak:ReconnectionOfWholesomeRoots .

vak:ViewGovernedPerson
    rdfs:label "dṛṣṭi-carita" ;
    vak:mayHaveSex vak:Female, vak:Male ;
    vak:mayPerform vak:SeveranceOfWholesomeRoots .

vak:NonEndowmentWithWholesomeRoots
    a logic:CapabilityNonPossession ;
    rdfs:label "asamanvaya" ;
    vak:resultsFrom vak:SeveranceOfWholesomeRoots .

vak:ReconnectionOfWholesomeRoots
    a logic:CapabilityRestoration ;
    rdfs:label "saṃdhi" ;
    vak:mayBeConditionedBy vak:DoubtConcerningKarmicGroundAndResult,
                           vak:AffirmativeViewOfKarmicGroundAndResult .

vak:ImmediateRetributionActor
    rdfs:label "ānantarya-kārin" ;
    vak:cannotUndergo vak:PresentLifeReconnectionOfWholesomeRoots .
```

Rule seed:

```text
DogmaticDenial(?system, ?principle)
and OpensDoubt(?system, ?principle)
    →
BecomesRepairable(?system)
```

Constraint:

```text
BecomesRepairable(?system)
    does not imply
AllCommittedConsequencesReversed(?system)
```

## 12. Commit Note

```text
VAK_4.80 — Define non-endowment and reconnection of wholesome roots

- specify that either a woman or a man may sever wholesome roots
- identify view-governed conduct as the determining character
- define severance as non-endowment with wholesome roots
- define reconnection through doubt or affirmative view
- interpret doubt as the reopening of practical possibility
- distinguish principial recovery from complete right knowledge
- exclude present-life reconnection for one who has committed
  an immediate-retribution action
- model recovery as restoration of operative capability
  without automatic reversal of committed consequences
```

### First-pass determination

```text
who severs:
    woman or man

determining character:
    conduct governed by view

result:
    non-endowment with wholesome roots

reconnection:
    doubt or affirmative view

exception:
    no reconnection in the present life
    for an immediate-retribution actor
```

The central Rational Agent result is:

```text
a corrupted system does not need
complete knowledge before recovery can begin

it first needs the capacity to say:

    perhaps my governing denial is false
```
