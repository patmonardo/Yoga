# VAK_2.37 — The Acquisition Matrix

## 1. Sanskrit (Devanāgarī)

```sanskrit
त्रैयध्विकानां त्रिविधा शुभादीनां शुभादिका ।
स्वधातुका तदाप्तानामनाप्तानां चतुर्विधा ॥ २.३७ ॥
```

## 2. Sanskrit (IAST)

```text
traiyadhvikānāṃ trividhā śubhādīnāṃ śubhādikā /
svadhātukā tadāptānām anāptānāṃ caturvidhā // 2.37 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| traiyadhvikānām | gen. pl. m.; adjective | of dharmas of the three times |
| trividhā | nom. sg. f. | threefold |
| śubhādīnām | gen. pl. m.; compound | of wholesome and the rest |
| śubhādikā | nom. sg. f.; compound | correspondingly wholesome and so forth |
| svadhātukā | nom. sg. f.; adjective | of the same realm |
| tadāptānām | gen. pl. m.; compound | of those included in that realm |
| anāptānām | gen. pl. m.; past passive participle | of those not included in a realm |
| caturvidhā | nom. sg. f. | fourfold |

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

> For dharmas of the three times, acquisition is threefold. For wholesome
> and the rest, it has the corresponding ethical status. Of those included
> in a realm, it belongs to that same realm; of those not included, it is
> fourfold.
### Bhāṣya-informed study translation

> For dharmas of the three times, acquisition is threefold; of wholesome,
> unwholesome, or indeterminate dharmas, it has that status. Acquisition of
> a realm-included dharma belongs to that realm; of one not included in a
> realm, it is fourfold.
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

**Translation note.** The commentary specifies the four cases for what is not realm-included: desire, form, or formless realm, and uncontaminated. The last is not a fourth realm. It further classifies acquisition by path and abandonment, details supplied by the commentary rather than this verse.

The matrix is what a bare possesses leaves out. When, of what quality, in which realm, and, in the commentary, by what path and what abandonment. The fourfold rule is not arbitrary. It is the union of the eligible cases. Not an implementation.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_37 a vak:Karika ; vak:hasTopic vak:AcquisitionMatrix .
vak:DharmaTime vak:independentOf vak:AcquisitionTime .
```
