# VAK_3b — VAkK_3.42

## Sanskrit — Devanāgarī

छेदसंधानवैराग्यहानिच्युत्युपपत्तयः ।
मनोविज्ञान एवेष्टाः उपेक्षायां च्युतोद्भवौ ॥ VAkK_3.42 ॥

## Sanskrit — IAST

chedasaṃdhāna vairāgyahānicyutyupapattayaḥ /
manovijñāna eveṣṭāḥ upekṣāyāṃ cyutodbhavau // VAkK_3.42 //

## Source Caution

The source reads:

```text
chedasaṃdhāna vairāgyahānicyutyupapattayaḥ /
manovijñāna eveṣṭāḥ upekṣāyāṃ cyutodbhavau // VAkK_3.42 //
```

The compound-list is dense. I preserve the source order and keep exact doctrinal pairings provisional pending Bhāṣya control.

## Padaccheda

| Sandhi form | Padaccheda | Basic meaning |
|---|---|---|
| cheda | cheda | cutting / severance |
| saṃdhāna | saṃdhāna | joining / linking |
| vairāgya | vairāgya | detachment / dispassion |
| hāni | hāni | decline / loss |
| cyuti | cyuti | falling away / death |
| upapatti | upapatti | rebirth / arising into existence |
| manovijñāne | mano-vijñāne | in mental knowledge / mental vijñāna |
| eva | eva | only |
| iṣṭāḥ | iṣṭāḥ | accepted / held |
| upekṣāyām | upekṣāyām | in equanimity / neutral feeling |
| cyutodbhavau | cyuta-udbhavau | death and arising / falling and birth |

## Grammar

```text
cheda-saṃdhāna-vairāgya-hāni-cyuti-upapattayaḥ
    = cutting, linking, detachment, decline, death, and rebirth

mano-vijñāne eva iṣṭāḥ
    = are accepted only in mental vijñāna

upekṣāyām cyuta-udbhavau
    = death and arising occur in equanimity
```

## Literal Translation

Cutting, linking, detachment, decline, death, and rebirth are accepted only in mental vijñāna. Death and arising occur in equanimity.

## Philosophical Translation

The decisive transition-functions of conditioned continuity — severance, reconnection, dispassion, decline, death, and rebirth — are assigned to mental knowledge alone. The moments of falling away and arising occur in the neutral register of equanimity.

## Technical Vocabulary

| Sanskrit | Working translation | Note |
|---|---|---|
| cheda | cutting / severance | Break or interruption |
| saṃdhāna | linking / joining | Connection or continuity-link |
| vairāgya | detachment / dispassion | Dispassion-function |
| hāni | decline / loss | Loss or falling away |
| cyuti | death / falling away | Passing out of a state |
| upapatti | rebirth / arising | Arising into a new state |
| manovijñāna | mental knowledge | Sixth vijñāna; transition-functions assigned here |
| upekṣā | equanimity / neutrality | Feeling-tone of death and arising |
| udbhava | arising / birth | Coming forth into existence |

## Doctrinal Determination

VAkK_3.40 introduced `antarābhava` and named the sustaining nutriments.

VAkK_3.42 now gives the transition-functions of continuity:

```text
cheda        cutting
saṃdhāna     linking
vairāgya     dispassion
a hāni       decline / loss
cyuti        death / falling away
upapatti     rebirth / arising
```

These are assigned to:

```text
manovijñāna eva
    mental knowledge alone
```

The verse then states:

```text
upekṣāyāṃ cyutodbhavau
    death and arising occur in equanimity
```

## Logical Determination

This is a major refinement of the wheel.

The transition from one existence to another is not assigned to the five bodily contacts. It is assigned to mental knowledge.

```text
continuity-transition
    belongs to manovijñāna
```

And the affective tone of the decisive transition is not pleasure or pain, but equanimity:

```text
cyuti / udbhava
    occur in upekṣā
```

The wheel therefore passes through a neutral mental register at the point of death and arising.

## Interpretive Note

This continues the active-modeling analysis of features.

```text
cheda / saṃdhāna
    = transition features

cyuti / upapatti
    = death-birth features

manovijñāna
    = locus of transition

upekṣā
    = affective neutrality of transition
```

This is a subtle doctrine of continuity without a permanent self. The transition is real, but it is carried by conditioned mental knowledge, not by an enduring substance.

## Organon Interpretation

Light contact point:

```text
The wheel continues by transition-functions.
```

These functions are not external to the system. They belong to the mental side of conditioned continuity.

```text
severance
linking
decline
death
rebirth

all pass through manovijñāna
```

This deepens the movement from being to functional essence: transition itself is now a feature.

## OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_42
    a vak:Karika ;
    rdfs:label "VAkK 3.42" ;
    vak:continues vak:VAK_3_41 ;
    vak:hasTopic vak:Manovijnana ;
    vak:hasTopic vak:TransitionFunction ;
    vak:assignsLocus vak:Manovijnana ;
    vak:assignsAffectiveTone vak:Upeksa .

vak:TransitionFunction
    a logic:FunctionalDetermination ;
    rdfs:label "transition-function" .

vak:Upeksa
    a logic:AffectiveTone ;
    rdfs:label "upekṣā" ;
    vak:hasCanonicalTranslation "equanimity" .
```

## Commit Note

Committed VAK_3b / VAkK_3.42.

Established:
- cutting, linking, detachment, decline, death, and rebirth are accepted only in manovijñāna.
- death and arising occur in upekṣā.
- the continuity of the wheel is carried by transition-functions, not by a permanent self.
