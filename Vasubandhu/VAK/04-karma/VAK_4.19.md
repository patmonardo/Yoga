# VAK_4.19

## Sanskrit — Devanāgarī

```sanskrit
प्रातिमोक्षस्थितो नित्यमत्यागाद्वर्तमानया ।
अविज्ञप्त्यान्वितः पूर्वात् क्षणादूर्ध्वमतीतया ॥
```

## Sanskrit — IAST

```iast
prātimokṣasthito nityam atyāgād vartamānayā |
avijñaptyānvitaḥ pūrvāt kṣaṇād ūrdhvam atītayā ||
```

## Source reference

Source: `VAkK_4.19`.

## Padaccheda

```text
prātimokṣa-sthitaḥ
nityam
atyāgāt
vartamānayā

avijñaptyā
anvitaḥ
pūrvāt
kṣaṇāt
ūrdhvam
atītayā
```

## Literal translation

> One established in prātimokṣa restraint is continually endowed with present avijñapti because it has not been abandoned; after the first moment, he is also endowed with past avijñapti.

## Technical analysis

`prātimokṣasthitaḥ` means one established in prātimokṣa restraint. `atyāga` is non-abandonment or non-relinquishment. Thus continued possession depends upon acquisition of the restraint together with the absence of abandonment.

`nityam` here means continually for as long as the restraint remains un-abandoned, not metaphysical eternity.

The bearer possesses the restraint in two temporal modes:

```text
first moment:
    present avijñapti

subsequent moments:
    present avijñapti
    plus past avijñapti from prior moments
```

The verse therefore applies the Sarvāstivāda temporal classification directly to restraint. Persistence does not require one numerically identical dharma to endure. Rather, each moment supplies a presently occurring avijñapti while earlier moments become past.

## Doctrinal determination

1. Prātimokṣa restraint persists while it is not abandoned.
2. Its bearer continually possesses present avijñapti.
3. After the initial moment, the bearer also possesses past avijñapti.

The verse does not mention future avijñapti here.

## Light Organon interpretation

```text
a determination persists
not because one identical moment endures,

but because:
    each new moment renews it

while:
    prior moments remain determined as past
```

Continuity is thus continuity of form through difference of temporal moments.

## OWL++ seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_19
    a vak:Karika ;
    rdfs:label "VAK 4.19" ;
    vak:continues vak:VAK_4_18 ;
    vak:hasTopic vak:TemporalPossessionOfPratimoksa ;
    vak:hasTopic vak:PresentAndPastAvijnapti .

vak:PratimoksaBearer
    vak:isEndowedWith vak:PresentAvijnapti .

vak:NonAbandonment
    vak:conditions vak:ContinuedPratimoksaPossession .

vak:PratimoksaBearerAfterFirstMoment
    vak:isEndowedWith vak:PresentAvijnapti ;
    vak:isEndowedWith vak:PastAvijnapti .
```

## Verse summary

```text
VAK_4.19

One established in prātimokṣa restraint
continually possesses present avijñapti
so long as the restraint is not abandoned.

At the first moment:
    present avijñapti only

After the first moment:
    present avijñapti
    plus past avijñapti
```
