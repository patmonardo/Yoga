# VAK_2.37 — The Acquisition Matrix

## 1. Sanskrit (Devanāgarī)

> त्रैयध्विकानां त्रिविधा शुभादीनां शुभादिका ।
>
> स्वधातुका तदाप्तानामनाप्तानां चतुर्विधा ॥ २.३७ ॥

## 2. Sanskrit (IAST)

> traiyadhvikānāṃ trividhā śubhādīnāṃ śubhādikā /
>
> svadhātukā tadāptānām anāptānāṃ caturvidhā // 2.37 //

## 3. Lexical Analysis

| Pada | Force |
|---|---|
| traiyadhvikānām | of dharmas of the three times |
| trividhā | threefold |
| śubhādikā | correspondingly wholesome and so forth |
| svadhātukā | of the same realm |
| tadāptānām | of those included in that realm |
| anāptānām | of those not included in a realm |
| caturvidhā | fourfold |

Realm is the three. Not the eighteen. Not Domain.

## 4. Grammar

```text
% start S
S[INDEX=time] -> Acquisition[TIME=?t] of Dharma[TIME=?t]
S[INDEX=ethical] -> Acquisition[ETHICAL=?e] of Dharma[ETHICAL=?e]
S[INDEX=realm] -> Acquisition[REALM=?r] of Dharma[INCLUDED=?r]
S[INDEX=not-included] -> Acquisition[REALM=desire|form|formless|uncontaminated]
```

Time of the dharma and time of the acquisition are distinct.  
Uncontaminated is not a fourth realm.  
Space remains excluded.

## 5. Translation

### Literal Translation

Of those of the three times, threefold. Of the wholesome and the rest, wholesome and the rest. Of the same realm, of those included in that. Of those not included, fourfold.

### Bhāṣya-informed study translation

> Acquisition of a past, future, or present dharma may itself be past, future, or present. Of a wholesome, unwholesome, or indeterminate dharma, the acquisition has that ethical status. Of a dharma included in a realm, the acquisition belongs to that realm. Of a dharma not included, the acquisition may be of the desire, form, or formless realm, or uncontaminated. Uncontaminated is not a fourth realm.

## 6. Philosophical Translation

> Four indices. Time of the dharma and time of the acquisition are distinct. Uncontaminated is not a fourth realm. Space remains excluded.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| traiyadhvika | of the three times | both indices |
| svadhātuka | of the same realm | not Principle |
| anāpta | not included in a realm | not unacquired |
| anāsrava | uncontaminated | not a realm |

## 8. Logical Determination

```text
dharma-time × acquisition-time
    nine, not three inherited
ethical class of acquisition
    = ethical class of the dharma
realm-bound
    → same realm
not realm-bound
    → desire, form, formless, or uncontaminated
space
    still neither
```

## 9. Interpretive Note

The matrix is what a bare possesses leaves out. When, of what quality, in which realm, and, in the commentary, by what path and what abandonment. The fourfold rule is not arbitrary. It is the union of the eligible cases. Not an implementation.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_37 a vak:Karika ; vak:hasTopic vak:AcquisitionMatrix .
vak:DharmaTime vak:independentOf vak:AcquisitionTime .
```
