# VAK_2.46 — Secondary Marks, and the Restriction

## 1. Sanskrit (Devanāgarī)

> जातिजात्यादयस्तेषां तेऽष्टधर्मैकवृत्तयः ।
>
> जन्यस्य जनिका जातिर्न हेतुप्रत्ययैर्विना ॥ २.४६ ॥

## 2. Sanskrit (IAST)

> jātijātyādayas teṣāṃ te 'ṣṭadharmaikavṛttayaḥ /
>
> janyasya janikā jātir na hetupratyayair vinā // 2.46 //

## 3. Lexical Analysis

| Pada | Force |
|---|---|
| jāti-jāti-ādayaḥ | arising-of-arising and the rest |
| teṣām | of those primary marks |
| aṣṭa-dharma-eka-vṛttayaḥ | operating on eight, and on one |
| janyasya | of what is to be generated |
| janikā | the generator |
| na vinā | not without |
| hetu-pratyayaiḥ | causes and conditions |

Operation is activity, efficacy. Not a third synonym for the mark.

## 4. Grammar

```text
% start S
S[MARK=primary] -> OperatesOn[COUNT=8]
S[MARK=secondary] -> OperatesOn[COUNT=1]
S[GENERATE=true] -> Arising[WITH=causes-and-conditions]
```

Primary operate on eight, secondary on one. No regress.  
Arising generates only with causes and conditions.  
The power seen is the conjunction, on the critical account.

## 5. Translation

### Literal Translation

Arising-of-arising and the rest, of those. They operate on eight dharmas, and on one. Arising is the generator of what is to be generated, not without causes and conditions.

### Bhāṣya-informed study translation

> The primary marks, being conditioned, have secondary marks. Primary operate on eight, secondary on one. No regress. Arising generates only with causes and conditions. The power seen is the conjunction, on the critical account. The genitive does not prove a second entity. The marks are maintained as real. Not settled.

## 6. Philosophical Translation

> Primary operate on eight, secondary on one. The stipulation stops the regress; it does not show the entities. Arising generates only with causes and conditions. The power seen is the conjunction. Arising is the transition, not a producer beside it. The marks are maintained as real. Not settled.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| anulakṣaṇa | secondary mark | of the primary |
| vṛtti | operation | efficacy |
| janikā | generator | the claimed role |
| hetu-pratyaya | causes and conditions | the restriction |
| abhūtvā-bhāva | existing after not existing | the critical definition |
| prajñapti | designation | not imaginary |

## 8. Logical Determination

```text
nine
    dharma + four primary + four secondary
primary
    → eight, not itself
secondary
    → one
generates
    → conjunction complete
conjunction complete
    → arises
conjunction absent
    → does not arise
arising-entity
    no further difference
    redundant, on the critical account
unconditioned
    does not arise
reply
    doctrine kept
    not settled
```

## 9. Interpretive Note

The first half belongs with the marks of 2.45. The second half is the objection the restriction invites. Grammar is not ontology. The close is that the marks have been explained, with the dispute recorded.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_46 a vak:Karika ; vak:hasTopic vak:ArisingRestriction .
vak:MarkEntity vak:settled false .
```
