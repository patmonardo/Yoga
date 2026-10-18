# VAK_1.19 — One Principle, Two Sites

## 1. Sanskrit (Devanāgarī)

```sanskrit
जातिगोचरविज्ञानसामान्यादेकधातुता ।
द्वित्वेऽपि चक्षुरादीनां शोभार्थं तु द्वयोद्भवः ॥ १.१९ ॥
```

## 2. Sanskrit (IAST)

```text
jātigocaravijñānasāmānyād ekadhātutā /
dvitve 'pi cakṣurādīnāṃ śobhārthaṃ tu dvayodbhavaḥ // 1.19 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| jāti | compound member | kind; the nature of the eye |
| gocara | compound member | range |
| vijñāna | compound member | the cognition |
| sāmānyāt | ablative | because of commonality |
| eka-dhātutā | nominative | the status of one principle |
| dvitve api | locative and particle | even though two |
| cakṣus-ādīnām | genitive plural | of the eye and the rest |
| śobhā-artham | accusative of purpose | for beauty |
| tu | particle | a second question |
| dvaya-udbhavaḥ | nominative | arising as a pair |

The commentary restricts the eye and the rest to eye, ear, and nose. Tongue and body do not raise the count.

**Grammar tokens.** Verse-order IAST with sandhi opened. The first
compound is one leaf, combining the first four lexical rows; *dvitve api*
is separated. *Cakṣus-ādi* is restricted by the Bhāṣya to eye, ear, and
nose. No covert token is needed.

```text
# tokens: jāti-gocara-vijñāna-sāmānyāt eka-dhātutā dvitve api cakṣus-ādīnām śobhā-artham tu dvaya-udbhavaḥ
```

## 4. Grammar

The causal ablative gives three commonalities; the concessive locative
retains duality without doubling the Principle. *Tu* turns from why one
Principle to why two sites. The purpose of beauty is not a fourth
criterion of Principle identity.

```nltk-fcfg
% start S
# tokens: jāti-gocara-vijñāna-sāmānyāt eka-dhātutā dvitve api cakṣus-ādīnām śobhā-artham tu dvaya-udbhavaḥ
S[SEM=<(?identity & ?arising)>] -> IDENTITY[SEM=?identity] ARISING[SEM=?arising]
IDENTITY[SEM=<?scope(?shared)(?single)>] -> COMMON[CASE=abl,SEM=?shared] SINGLE[CASE=nom,NUM=?n,SEM=?single] DUAL[CASE=loc] EVEN SCOPE[CASE=gen,NUM=pl,SEM=?scope]
ARISING[SEM=<?purpose(?arising)>] -> PURPOSE[SEM=?purpose] CONTRAST PAIR[CASE=nom,NUM=sg,SEM=?arising]
COMMON[CASE=abl,SEM=<\x.(CommonKind(x) & CommonRange(x) & CommonCognition(x))>] -> 'jāti-gocara-vijñāna-sāmānyāt'
SINGLE[CASE=nom,NUM=sg,GEN=f,SEM=<\x.OnePrinciple(x)>] -> 'eka-dhātutā'
DUAL[CASE=loc,NUM=sg] -> 'dvitve'
EVEN -> 'api'
SCOPE[CASE=gen,NUM=pl,SEM=<\P.\Q.all x.((PairedEyeEarNose(x) & P(x)) -> Q(x))>] -> 'cakṣus-ādīnām'
PURPOSE[SEM=<\P.all x.(PairedEyeEarNose(x) -> (P(x) & ForBeautyOfSupport(x)))>] -> 'śobhā-artham'
CONTRAST -> 'tu'
PAIR[CASE=nom,NUM=sg,GEN=m,SEM=<\x.ArisesAsPair(x)>] -> 'dvaya-udbhavaḥ'
```

```nltk-dep
'eka-dhātutā' -> 'jāti-gocara-vijñāna-sāmānyāt' | 'dvitve' | 'cakṣus-ādīnām'
'dvitve' -> 'api'
'dvaya-udbhavaḥ' -> 'śobhā-artham' | 'tu'
```

**Close construe.** Despite the duality of eye and the rest, common kind,
range, and Cognition ground one Principle; arising as a pair is for the
beauty of the support.

`x` represents a paired arrangement, not either anatomical site alone.
The compound's *vijñāna* is Cognition, not dhātu. The Bhāṣya explains
the common Cognition through both sites supporting one Eye-Cognition.
The grammar does not identify
two sites numerically, nor infer a Principle merely from bodily beauty.

## 5. Translation

### Literal Translation

> From commonality of kind, range, and Cognition, there is the status of one
> principle, even in the duality of the eye and the rest. But the arising as
> a pair is for the sake of beauty.

### Bhāṣya-informed study translation

> Although the eyes, ears, and nostrils occur in pairs, each pair is one
> Principle through commonality of kind, range, and Cognition. Yet they arise
> in pairs for the beauty of the bodily support.

## 6. Philosophical Translation

Again, two lines. The first answers the count. The second answers the body.

The objection is anatomical. Two eyes, two ears, two nostrils: eighteen plus three, twenty-one. The reply refuses the inference. Two sites are not two principles.

Three commonalities, and all three. Kind: both have the nature of the eye. Range: both take visible form. Cognition: both are supports of one Eye-Cognition. The same is to be applied to ear and nose. Not tongue. Not body. Those do not generate the objection.

*Tu* keeps the second question honest. Why two, if one principle? For the beauty of the support. One eye-site, one ear-site, one nostril-opening, and the commentary says there would be great disfigurement. Beauty is not a fourth ground of the count. It explains the pair.

1.18 said inclusion is by own-nature. Here own-nature is not the count of sites. Kind, range, and Cognition, in common, ground the single Principle. The meanings of base, essence, and principle are the next verse. Not this one.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| jāti | kind | the nature of the eye; not birth |
| gocara | range | both take visible form |
| vijñāna | Cognition | both sites support one Eye-Cognition |
| sāmānya | commonality | the three together |
| eka-dhātutā | status of one principle | the count |
| dvitva | duality | two sites, conceded |
| āśraya | support | the bodily support |
| śobhā | beauty | why the pair; not why the one |
| vairūpya | disfigurement | the commentary's contrast |
| rūpa-viṣaya | visible form as condition | the range |

## 8. Logical Determination

**Kārikā, derived.** The first universal requires all three commonalities
within the eye–ear–nose scope. The second gives paired arising its purpose,
not a further test of Principle identity.

```nltk-sem
# derived by the section 4 parse
((all x.((PairedEyeEarNose(x) & (CommonKind(x) & CommonRange(x) & CommonCognition(x))) -> OnePrinciple(x))) & (all x.(PairedEyeEarNose(x) -> (ArisesAsPair(x) & ForBeautyOfSupport(x)))))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((all x.((PairedEyeEarNose(x) & (CommonKind(x) & CommonRange(x) & CommonCognition(x))) -> OnePrinciple(x))) & (all x.(PairedEyeEarNose(x) -> (ArisesAsPair(x) & ForBeautyOfSupport(x)))))
```

```nltk-valuation
PairedEyeEarNose => {eyes,ears,nostrils}
CommonKind => {eyes,ears,nostrils}
CommonRange => {eyes,ears,nostrils}
CommonCognition => {eyes,ears,nostrils}
OnePrinciple => {eyes,ears,nostrils}
ArisesAsPair => {eyes,ears,nostrils}
ForBeautyOfSupport => {eyes,ears,nostrils}
```

**Model checks.** Denying One Principle to a scoped pair with all three
commonalities must fail. If a commonality is absent, this rule no longer
warrants that conclusion; it does not prove the converse. A beauty-only
case outside the scoped arrangements does not acquire One Principle.
The numeral “one” is represented by a classification predicate, not by
equating the two bodily sites.

**Bhāṣya determination.** The objection and explanatory movement remain
below. The aesthetic rationale is the source's claim, not a modern
anatomical explanation or a universal principle of paired development.

```text
objection
    18 + second eye + second ear + second nostril
    = 21

reply
    two sites ≠ two principles

    kind in common
    range in common
    Cognition in common
        → one Eye Principle despite two sites
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

**Translation note.** The Bhāṣya restricts the paired cases to eye, ear, and
nose: each pair shares its respective kind, range, and supported Cognition.
The pair's purpose is beauty of the bodily support; without paired sites the
commentary says there would be great disfigurement. Tongue and body are not
part of the count-objection.

The hinge is *sāmānyāt*, then *tu*. Interpretation of the two questions is in the Bhāṣya.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_19 a vak:Karika ;
    vak:hasTopic vak:OnePrincipleTwoSites ;
    vak:belongsTo vak:Dhatunirdesa .

vak:TwoEyes vak:constitute vak:OneEyePrinciple .
vak:PairedArising vak:for vak:BeautyOfSupport ;
    vak:isGroundOfCount false .
vak:TwentyOneCount vak:rejected true .
```
