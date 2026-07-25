# VAK_4.99

## 1. Sanskrit — Devanāgarī

तदवद्यं मृषावादस्तेन भेत्ता समन्वितः ।
अवीचौ पच्यते कल्पमधिकैरधिका रुजः ॥ ४.९९ ॥

## 2. Sanskrit — IAST

**tadavadyaṃ mṛṣāvādas tena bhettā samanvitaḥ |**  
**avīcau pacyate kalpam adhikair adhikā rujaḥ || 4.99 ||**

## 3. Padaccheda

`tad | avadyam | mṛṣā-vādaḥ | tena | bhettā | samanvitaḥ | avīcau | pacyate | kalpam | adhikaiḥ | adhikāḥ | rujaḥ`

Expanded first half:

`tasya saṃghabhedasya avadyaṃ mṛṣāvādaḥ; tena mṛṣāvādena bhettā samanvitaḥ.`

## 4. Grammar

- **tad-avadyam** — the culpable activity associated with that division.
- **mṛṣāvādaḥ** — false speech.
- **tena** — by or with that.
- **bhettā** — the divider, from √bhid.
- **samanvitaḥ** — endowed or connected with.
- **avīcau** — in Avīci.
- **pacyate** — is cooked, tormented, or undergoes karmic maturation.
- **kalpam** — for one kalpa.
- **adhikair adhikā rujaḥ** — with additional aggravating factors, the pains are greater.

## 5. Literal Translation

> The culpable act associated with that is false speech, and the divider is endowed with it. He is tormented in Avīci for a kalpa; with additional factors, the pains are greater.

## 6. Philosophical Translation

> The morally culpable karma that produces Saṃgha-division is false speech; it is this karma that belongs to the divider. Its maturation is suffering in Avīci for a kalpa, with the intensity of suffering increasing according to the aggravation of the divisive act.

## 7. Technical Vocabulary

- **avadya** — blameworthy or culpable activity.
- **mṛṣāvāda** — false speech.
- **bhettā** — the causal agent who divides.
- **Avīci** — the hell of uninterrupted suffering.
- **pacyate** — undergoes maturation or torment.
- **kalpa** — the specified duration of the maturation.
- **ruj** — pain or torment.

## 8. Doctrinal Determination

VAK_4.98 and VAK_4.99 distinguish the objective state of division from the karma that produces it.

- the Saṃgha is connected with the objective state of non-concord;
- the divider is connected with afflicted false speech;
- the false speech is unwholesome karma;
- the produced collective state is non-afflicted and indeterminate;
- the karma matures in Avīci for one kalpa.

Thus an unwholesome communicative act produces an ethically indeterminate collective determination.

## 9. Logical Determination

The complete circuit is:

```text
false representation
    → divisive speech-karma
    → collective non-concord
    → Avīci maturation
```

The speech-act is borne by the divider; the division is borne by the Saṃgha; the resultant suffering is borne by the divider’s later continuum.

## 10. Light Organon Interpretation

False speech here does not merely misdescribe an already given social reality. By reorganizing adherence around a false representation of teacher, Dharma, and Path, it produces a real communal rupture.

This distinguishes semantic validity from causal efficacy: a false proposition may be logically invalid while remaining karmically and socially powerful.

## 11. OWL++ Seed

```ttl
vak:VAK_4_99 a vak:Karika ;
    rdfs:label "VAK 4.99" ;
    vak:continues vak:VAK_4_98 ;
    vak:hasTopic vak:DivisiveFalseSpeech, vak:AviciMaturation .

vak:DivisiveFalseSpeech
    rdfs:subClassOf vak:FalseSpeech, vak:UnwholesomeKarma ;
    vak:produces vak:SanghaDivision .

vak:SanghaDivider vak:isBearerOf vak:DivisiveFalseSpeech .
vak:Sangha vak:isBearerOf vak:SanghaDivision .
vak:DivisiveFalseSpeech vak:hasMaturation vak:AviciMaturation .
```

## 12. Commit Note

- identify false speech as the culpable karma producing division;
- assign the false speech to the divider;
- preserve the distinction between unwholesome cause and indeterminate collective state;
- identify Avīci maturation for one kalpa;
- retain proportional increase of suffering under aggravating conditions;
- model false representation as causally productive of real communal rupture.
