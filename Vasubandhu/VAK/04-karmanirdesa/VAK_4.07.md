# VAK_4.07 — Ethical and Domain Classification of Action

## 1. Sanskrit — Devanāgarī

```sanskrit
नाव्याकृतास्त्यविज्ञप्तिस्त्रिधान्यत्ताशुभं पुनः ।
कामे रूपेऽप्यविज्ञप्तिर्विज्ञप्तिः सविचारयोः ॥
```

## 2. Sanskrit — IAST

```iast
nāvyākṛtāsty avijñaptiḥ tridhānyat aśubhaṃ punaḥ |
kāme rūpe ’py avijñaptiḥ vijñaptiḥ savicārayoḥ ||
```

## 3. Source Caution

External source siglum: VAkK_4.7.

The transmitted `tridhānvyat` is read provisionally as `tridhā anyat`, “the other is threefold,” with `anyat` referring to `vijñapti`. The exact identification of `savicārayoḥ` should wait for the Bhāṣya.

## 4. Padaccheda

| Form | Padaccheda | Working meaning |
|---|---|---|
| nāvyākṛtāsti | na avyākṛtā asti | there is no ethically indeterminate |
| avijñaptiḥ | avijñaptiḥ | non-manifest action |
| tridhānyat | tridhā anyat | the other is threefold |
| aśubham | aśubham | unwholesome |
| kāme | kāme | in the desire domain |
| rūpe api | rūpe api | also in the form domain |
| vijñaptiḥ | vijñaptiḥ | manifest action |
| savicārayoḥ | sa-vicārayoḥ | in the two levels possessing vicāra |

## 5. Grammar

`nāvyākṛtāsty avijñaptiḥ` states directly that avijñapti is never ethically indeterminate. `tridhā anyat` most naturally contrasts vijñapti as threefold: wholesome, unwholesome, and indeterminate. `aśubhaṃ punaḥ kāme` restricts the unwholesome to the desire domain. `rūpe ’py avijñaptiḥ` extends avijñapti into the form domain. `savicārayoḥ` is locative dual; its precise cosmological scope remains provisional.

## 6. Literal Translation

There is no indeterminate non-manifest action; the other is threefold. The unwholesome, however, is in the desire domain. Non-manifest action exists also in the form domain; manifest action exists in the two levels possessing vicāra.

## 7. Philosophical Translation

Non-manifest action is never ethically neutral: it is necessarily wholesome or unwholesome. Manifest action, by contrast, may be wholesome, unwholesome, or indeterminate. Unwholesome non-manifest action is restricted to the desire domain, although non-manifest action also occurs in the form domain. Manifest action occurs only in the two levels in which vicāra remains operative.

## 8. Technical Vocabulary

- `avyākṛta`: ethically indeterminate, neither wholesome nor unwholesome.
- `tridhā`: threefold.
- `aśubha`: unwholesome.
- `savicāra`: accompanied by vicāra; exact level-identification deferred.

## 9. Doctrinal Determination

```text
avijñapti
├── wholesome
└── unwholesome

vijñapti
├── wholesome
├── unwholesome
└── indeterminate
```

Unwholesome avijñapti is restricted to kāmadhātu. Avijñapti also occurs in rūpadhātu. The verse thereby crosses ethical classification with domain-distribution.

## 10. Logical Determination

The non-manifest is not less determined than the manifest. It is more selectively determined:

```text
manifest action
    may be ethically neutral

non-manifest continuation
    cannot be ethically neutral
```

Thus avijñapti is not a hidden duplicate of every visible deed. It belongs only where action has acquired a determinate wholesome or unwholesome efficacy.

## 11. Interpretive Note

The verse blocks an overly broad account of avijñapti as the concealed ground of every action. A safer first-pass formulation is:

```text
avijñapti
    = non-manifest continuation
      of ethically determinate action
```

## 12. Light Organon Interpretation

Two axes are now explicit:

```text
manifest / non-manifest
wholesome / unwholesome / indeterminate
```

But the axes are asymmetrical: vijñapti spans all three ethical values, while avijñapti excludes neutrality. The suppressed dimension is therefore not vague; it is more narrowly constituted.

## 13. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_07
    a vak:Karika ;
    rdfs:label "VAK 4.07" ;
    vak:continues vak:VAK_4_06 ;
    vak:hasTopic vak:EthicalClassificationOfAction ;
    vak:hasTopic vak:DomainDistributionOfAction .

vak:Avijnapti
    vak:hasPossibleEthicalQuality vak:Wholesome ;
    vak:hasPossibleEthicalQuality vak:Unwholesome ;
    vak:excludesEthicalQuality vak:Indeterminate .

vak:Vijnapti
    vak:hasPossibleEthicalQuality vak:Wholesome ;
    vak:hasPossibleEthicalQuality vak:Unwholesome ;
    vak:hasPossibleEthicalQuality vak:Indeterminate .

vak:UnwholesomeAvijnapti
    vak:existsOnlyIn vak:KamaDhatu .
```

## 14. Verse Summary

```text
VAK_4.07

Avijñapti is never ethically neutral.
Vijñapti may be wholesome, unwholesome, or indeterminate.
Unwholesome avijñapti is restricted to the desire domain.
Avijñapti also exists in the form domain.
Manifest action exists only in the two levels accompanied by vicāra.
```

## 15. Commit Note

Committed VAK_4.07. The exact identification of `savicārayoḥ` remains deferred to the Bhāṣya pass.
