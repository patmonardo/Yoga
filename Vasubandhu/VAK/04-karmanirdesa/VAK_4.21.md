# VAK_4.21

## Sanskrit — Devanāgarī

समाहितार्यमार्गस्थौ तौ युक्तौ वर्तमानया ।
मध्यस्थस्यास्ति चेदादौ मध्यया ऊर्ध्वं द्विकालया ॥

## Sanskrit — IAST

samāhītāryamārgasthau tau yuktau vartamānayā |
madhyasthasyāsti ced ādau madhyayā ūrdhvaṃ dvikālayā ||

## Source caution

Source: `VAkK_4.21`.

The source reading `samāhītārya-` is difficult. The intended compound is probably `samāhita-ārya-mārga-sthau`: one established in concentration and one established in the noble Path.

The phrase `madhyasthasya` most naturally refers to one situated in the middle—neither established in restraint nor in non-restraint. This should be confirmed in the Bhāṣya.

## Padaccheda

samāhita | ārya-mārga-sthau | tau | yuktau | vartamānayā |
madhyasthasya | asti | cet | ādau | madhyayā | ūrdhvam | dvi-kālayā ||

## Literal translation

The concentrated person and the one established in the noble Path are both joined with present avijñapti. If one in the middle position possesses it, initially he is joined with the middle temporal mode, and afterward with two temporal modes.

Here “middle temporal mode” means the present, between past and future.

## Philosophical translation

Meditation-born restraint and uncontaminated restraint are present while their corresponding concentrated or noble-path consciousness is actually occurring. For a person established in neither restraint nor non-restraint, an occasional avijñapti is initially possessed only as present; once its first moment has passed, it is possessed as both present and past.

## Technical analysis

`samāhita` means collected or concentrated. The concentrated practitioner possesses present meditation-born restraint.

`ārya-mārga-stha` means one standing in the noble Path. Such a practitioner possesses present uncontaminated restraint.

`tau yuktau vartamānayā` states that these two persons are joined with the corresponding avijñapti as present. This concretizes VAK_4.17, where meditation-born and uncontaminated restraints were called `cittānuvartin`, mind-following.

`madhyastha`, one standing in the middle, most likely means one established in neither `saṃvara` nor `asaṃvara`. This corresponds to the third class of avijñapti from VAK_4.13, `itarā`, neither restraint nor non-restraint.

The conditional `asti cet` indicates that such a person does not necessarily possess avijñapti continuously. If an occasional avijñapti arises, then at its first moment it is present only (`ādau madhyayā`), and afterward it is possessed in two temporal modes (`ūrdhvaṃ dvikālayā`): past and present.

## Doctrinal determination

1. Meditation-born restraint is present while one is concentrated.
2. Uncontaminated restraint is present while one is established in the noble Path.
3. A person in neither restraint nor non-restraint may possess occasional avijñapti.
4. At its first moment that avijñapti is present only.
5. Afterward it is possessed as past and present.

## Light Organon interpretation

A determination may be structurally established or occasionally produced.

The middle person lacks a permanent restraint-system or non-restraint-system, but may still acquire a determinate action-trace. At first there is immediate present determination; afterward the present determination is joined with its accumulated past.

Being outside the two established systems does not mean absence of determination.

## OWL++ seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_21
    a vak:Karika ;
    rdfs:label "VAK 4.21" ;
    vak:continues vak:VAK_4_20 ;
    vak:hasTopic vak:PresentMindFollowingRestraint ;
    vak:hasTopic vak:TemporalPossessionOfOccasionalAvijnapti .

vak:ConcentratedPractitioner
    vak:isEndowedWith vak:PresentDhyanaBornRestraint .

vak:AryaPathPractitioner
    vak:isEndowedWith vak:PresentUncontaminatedRestraint .

vak:MiddlePositionPerson
    vak:mayBeEndowedWith vak:OccasionalAvijnapti .

vak:OccasionalAvijnaptiAtFirstMoment
    vak:hasTemporalMode vak:Present .

vak:OccasionalAvijnaptiAfterFirstMoment
    vak:hasTemporalMode vak:Past ;
    vak:hasTemporalMode vak:Present .
```

## Verse summary

The concentrated practitioner possesses present meditation-born restraint. The practitioner established in the noble Path possesses present uncontaminated restraint. A person established in neither restraint nor non-restraint may nevertheless possess avijñapti: at its first moment, present only; afterward, past and present.