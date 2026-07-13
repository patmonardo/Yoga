# VAK_4d — VAkK_4.65

## 1. Sanskrit — Devanāgarī

अशुभं कायाकर्मादि मतं दुश्चरितत्रयम् ।
अकर्मापि त्वभिध्यादि मनोदुश्चरितं त्रिधा ॥ VAkK_4.65 ॥

## 2. Sanskrit — IAST

aśubhaṃ kāyakarmādi mataṃ duścaritatrayam /
akarmāpi tvabhidhyādi manoduścaritaṃ tridhā // VAkK_4.65 //

Source note: segment `kāya-karmādi`; the source joins the compound. The second half is analyzed as `akarma api tu abhidhyā-ādi mano-duścaritam tridhā`.

## 3. Padaccheda

| Sandhi form | Padaccheda | Basic meaning |
|---|---|---|
| aśubham | a-śubham | unwholesome; bad |
| kāyakarmādi | kāya-karma-ādi | bodily karma and the rest |
| matam | matam | considered; held to be |
| duścaritatrayam | duścarita-trayam | threefold bad conduct |
| akarmāpi | akarma api | even though not karma |
| tu | tu | but; however |
| abhidhyādi | abhidhyā-ādi | covetousness and the others |
| manoduścaritam | manaḥ-duścaritam | mental bad conduct |
| tridhā | tridhā | threefold |

Expanded construction:

```text
aśubham kāya-karma
aśubham vāk-karma
aśubham manaḥ-karma
    iti
duścarita-trayam matam

abhidhyā
vyāpāda
mithyādṛṣṭi
    akarma api
    mano-duścaritam tridhā
```

## 4. Grammar

- `aśubham`: neuter nominative singular, distributed over bodily, verbal, and mental karma.
- `kāya-karmādi`: “bodily karma and the rest,” implying verbal and mental karma.
- `matam`: past passive participle of `man`, “considered” or “held.”
- `duścarita-trayam`: the threefold bad conduct.
- `akarma api`: “even though not karma.”
- `tu`: marks the doctrinal qualification.
- `abhidhyā-ādi`: covetousness and the other two, namely ill will and false view.
- `mano-duścaritam`: mental bad conduct.
- `tridhā`: in three forms.

The first statement identifies unwholesome bodily, verbal, and mental karma with the three bad conducts. The second states that covetousness, ill will, and false view are also mental bad conduct even though they are not karma in the strict sense.

## 5. Literal Translation

Unwholesome bodily karma and the rest are considered the threefold bad conduct. But covetousness and the others, though not karma, are the threefold mental bad conduct.

## 6. Philosophical Translation

The unwholesome activity of body, speech, and mind constitutes the threefold course of bad conduct. Mental bad conduct, however, also includes covetousness, ill will, and false view, even though these are not classified as karma in the strict sense.

```text
conduct
    ≠ only karma

mental bad conduct
    is broader than
mental karma
```

## 7. Technical Vocabulary

### aśubha

Unwholesome or ethically bad. It classifies the quality of the act.

### duścarita

`dus-carita`: bad conduct, or a wrongly conducted course of activity.

### akarman

Not karma in the strict doctrinal sense. This does not mean ethically irrelevant or causally inert.

### abhidhyā

Covetous fixation directed toward what belongs to another.

### abhidhyādi

The three mental bad courses:

```text
abhidhyā     covetousness
vyāpāda      ill will
mithyādṛṣṭi  false view
```

### mano-duścarita

Mental bad conduct. Its extension is broader than mental karma because it includes the three non-karmic mental courses.

## 8. Doctrinal Determination

VAK_4.64 identified threefold good conduct and purity. VAK_4.65 supplies the negative counterpart:

```text
body      bodily bad conduct
speech    verbal bad conduct
mind      mental bad conduct
```

The symmetry is not exact. Mental bad conduct includes:

```text
abhidhyā
vyāpāda
mithyādṛṣṭi
```

even though these are not karma strictly speaking.

Thus:

```text
mental karma
    ⊂
mental conduct
```

This prepares the doctrine of the ten karmapathas. A karmapatha is therefore not simply a subtype of karma; it is a determinate route or course through which karma proceeds.

## 9. Logical Determination

The verse distinguishes Activity from the form or course of Activity:

```text
karma
    = determinate intentional activity

carita
    = the manner or course in which activity proceeds
```

The first half gives identity:

```text
unwholesome karma
    =
bad conduct
```

The second half breaks simple identity:

```text
not-karma
    can nevertheless be
mental bad conduct
```

Thus conduct is logically broader than action strictly taken as karma. The inward orientations of appropriation, hostility, and false view can organize the karmic field prior to or apart from completed action.

## 10. Light Organon Interpretation

A useful first-pass architecture is:

```text
mental orientation
    ↓
intention
    ↓
executed action
    ↓
course of conduct
    ↓
result
```

Yet the verse shows that conduct begins before execution. A false view is already practical deformation, not merely a mistaken proposition.

```text
abhidhyā
    corrupt appropriation of the object

vyāpāda
    corrupt negation of the other

mithyādṛṣṭi
    corrupt determination of the whole
```

This supports the broader project principle that avidyā and vidyā determine Path and not-Path practically, not merely theoretically.

## 11. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_65
    a vak:Karika ;
    rdfs:label "VAkK 4.65" ;
    vak:continues vak:VAK_4_64 ;
    vak:hasTopic vak:ThreefoldBadConduct ;
    vak:distinguishes vak:Karma, vak:Conduct .

vak:BadConduct a vak:Conduct .
vak:BodilyBadConduct rdfs:subClassOf vak:BadConduct .
vak:VerbalBadConduct rdfs:subClassOf vak:BadConduct .
vak:MentalBadConduct rdfs:subClassOf vak:BadConduct .

vak:Covetousness
    a vak:MentalDetermination ;
    rdfs:label "abhidhyā" ;
    rdfs:subClassOf vak:MentalBadConduct ;
    vak:isStrictKarma false .

vak:IllWill
    a vak:MentalDetermination ;
    rdfs:label "vyāpāda" ;
    rdfs:subClassOf vak:MentalBadConduct ;
    vak:isStrictKarma false .

vak:FalseView
    a vak:MentalDetermination ;
    rdfs:label "mithyādṛṣṭi" ;
    rdfs:subClassOf vak:MentalBadConduct ;
    vak:isStrictKarma false .
```

## 12. Commit Note

Committed VAK_4d / VAkK_4.65.

Established:
- unwholesome bodily, verbal, and mental karma as threefold bad conduct
- abhidhyā, vyāpāda, and mithyādṛṣṭi as mental bad conduct
- the claim that these three are not strict karma
- the distinction between karma and the broader field of conduct
- preparation for the ten karmapathas

First-pass determination:

```text
duścarita-traya
    = unwholesome conduct of body, speech, and mind

mental bad conduct
    > mental karma

conduct
    is broader than
karma
```