# VAK_1.19 — One Principle, Two Sites

## 1. Sanskrit (Devanāgarī)

> जातिगोचरविज्ञानसामान्यादेकधातुता ।
>
> द्वित्वेऽपि चक्षुरादीनां शोभार्थं तु द्वयोद्भवः ॥ १.१९ ॥॥

## 2. Sanskrit (IAST)

> jātigocaravijñānasāmānyād ekadhātutā /
>
> dvitve 'pi cakṣurādīnāṃ śobhārthaṃ tu dvayodbhavaḥ // 1.19 //

## 3. Lexical Analysis

```text
jātigocaravijñānasāmānyāt → jāti-gocara-vijñāna-sāmānyāt
ekadhātutā                 → eka-dhātutā
dvitve 'pi                 → dvitve + api
śobhārtham                 → śobhā-artham
dvayodbhavaḥ               → dvaya-udbhavaḥ
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| jāti | compound member | kind; here, the nature of the eye |
| gocara | compound member | range |
| vijñāna | compound member | the principle |
| sāmānyāt | ablative | because of commonality |
| eka-dhātutā | nominative feminine | the status of one principle |
| dvitve | locative | in duality; even though two |
| api | particle | even |
| cakṣus-ādīnām | genitive plural | of the eye and the rest |
| śobhā-artham | accusative of purpose | for the sake of beauty |
| tu | particle | but; a second question |
| dvaya-udbhavaḥ | nominative | arising as a pair |

The Bhāṣya restricts *cakṣurādīnām* to eye, ear, and nose. Tongue and
body do not raise the count.

## 4. Grammar

```text
jāti-gocara-vijñāna-sāmānyāt
    → eka-dhātutā
    dvitve api

tu
    śobhā-artham dvaya-udbhavaḥ
```

The first clause is an ablative of cause. Commonality of kind, of range,
and of principle is why there is one principle, even in duality.

*Tu* turns the question. The pair is not the ground of the count. The pair
is for beauty.

## 5. Translation

### Literal Translation

From commonality of kind, range, and principle, there is the status of one
principle, even in the duality of the eye and the rest. But the arising as
a pair is for the sake of beauty.

### Bhāṣya-informed study translation

There are not twenty-one principles. The two eyes are one eye-principle,
because both have the nature of the eye, both take visible form, and both
are supports of one eye-principle. The same holds for ear and nose. That
they arise as a pair is for the beauty of the support. Otherwise there
would be great disfigurement.

## 6. Philosophical Translation

Again, two lines. The first answers the count. The second answers the body.

The objection is anatomical. Two eyes, two ears, two nostrils: eighteen
plus three, twenty-one. The reply refuses the inference. Two sites are not
two principles.

Three commonalities, and all three. Kind: both have the nature of the eye.
Range: both take visible form. Principle: both are supports of one
eye-principle. The same is to be applied to ear and nose. Not tongue. Not
body. Those do not generate the objection.

*Tu* keeps the second question honest. Why two, if one principle? For the
beauty of the support. One eye-site, one ear-site, one nostril-opening,
and the commentary says there would be great disfigurement. Beauty is not
a fourth ground of the count. It is why the support is paired.

This is the transition. 1.18 said inclusion is by own-nature. Here
own-nature is not the count of sites. Kind, range, and principle, in
common, are the nature that includes. The meanings of base, essence, and
principle are the next verse. Not this one.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| jāti | kind | both have the nature of the eye; not birth, not caste |
| gocara | range | glossed as taking visible form |
| vijñāna | principle | one eye-principle; not a second substance |
| sāmānya | commonality | the three together |
| eka-dhātutā | status of one principle | the count |
| dvitva | duality | two sites, conceded |
| āśraya | support | the bodily support; not the base |
| śobhā | beauty | why the pair; not why the one |
| vairūpya | disfigurement | the commentary's contrast |
| rūpa-viṣaya | visible form as condition | the range; not a finished object |

## 8. Logical Determination

```text
objection
    18 + second eye + second ear + second nostril
    = 21

reply
    two sites ≠ two principles

    kind in common
    range in common
    principle in common
        → one eye-principle
        likewise ear, nose

why one?
    the three commonalities
why two?
    beauty of the support
    otherwise, disfigurement

not tongue, not body
1.20 not opened
```

## 9. Interpretive Note

The hinge is *sāmānyāt*, then *tu*. Interpretation of the two questions
is in the Bhāṣya.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_19 a vak:Karika ;
    vak:hasTopic vak:OnePrincipleDespiteTwoSites ;
    vak:belongsTo vak:Dhatunirdesa ;
    vak:transitionsTo vak:VAK_1_20 .

vak:OnePrincipleStatus vak:groundedIn vak:CommonKind, vak:CommonRange,
    vak:CommonPrinciple ;
    vak:compatibleWith vak:TwoSites .

vak:TwoEyes vak:constitute vak:OneEyePrinciple .
vak:TwoEars vak:constitute vak:OneEarPrinciple .
vak:TwoNostrils vak:constitute vak:OneNosePrinciple .

vak:TwentyOneCount vak:rejected true .

vak:PairedArising vak:for vak:BeautyOfSupport ;
    vak:isGroundOfCount false .
```
