# VAK_2.54 — Pervasive Cause and Maturation Cause

## 1. Sanskrit (Devanāgarī)

> सर्वत्रगाख्यः क्लिष्टानां स्वभूमौ पूर्वसर्वगाः ।
>
> विपाकहेतुरशुभाः कुशलाश्चैव सास्रवाः ॥ २.५४ ॥

## 2. Sanskrit (IAST)

> sarvatragākhyaḥ kliṣṭānāṃ svabhūmau pūrvasarvagāḥ /
>
> vipākahetur aśubhāḥ kuśalāś caiva sāsravāḥ // 2.54 //

## 3. Lexical Analysis

| Pada | Force |
|---|---|
| sarvatraga-ākhyaḥ | called pervasive |
| kliṣṭānām | of the afflicted |
| sva-bhūmau | on their own level |
| pūrva-sarvagāḥ | prior pervasive dharmas |
| vipāka-hetuḥ | maturation cause |
| aśubhāḥ | unwholesome |
| kuśalāḥ sāsravāḥ | wholesome with influx |

## 4. Grammar

```text
% start S
S[CAUSE=pervasive] -> Prior[LEVEL=own, TARGET=later-afflicted, CLASS=other-allowed]
S[CAUSE=maturation] -> Unwholesome | WholesomeWithInflux
```

Pervasive is prior, own level, later afflicted, other class allowed.  
Maturation is unwholesome and wholesome with influx.  
Indeterminate weak. Uncontaminated not moistened.

## 5. Translation

### Literal Translation

Called pervasive, of the afflicted, on their own level: the prior pervasive. Maturation cause: the unwholesome, and the wholesome with influx.

### Bhāṣya-informed study translation

> The cause called pervasive is the prior pervasive dharmas of a level, for the afflicted dharmas that follow them on their own level, even of another class. The maturation cause is the unwholesome and the wholesome with influx; indeterminate dharmas are too weak to mature, and uncontaminated ones are not moistened by craving.

## 6. Philosophical Translation

> Pervasive is prior, own level, later afflicted, other class allowed. Maturation is unwholesome and wholesome with influx. Indeterminate weak. Uncontaminated not moistened. Series required. Not settled.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| sarvatraga-hetu | pervasive cause | prior, own level, other class |
| vipāka-hetu | maturation cause | unwholesome, wholesome with influx |
| abhiṣyandita | moistened | by craving |
| santati-pariṇāma | transformation of a continuum | the critical ripening |

## 8. Logical Determination

```text
pervasive
    prior + own level + later afflicted
    class may differ
maturation
    unwholesome or wholesome with influx
    not indeterminate
    not uncontaminated
ripening
    disputed
series
    required
    not simultaneous
    not immediate
```

## 9. Interpretive Note

The latent-tendency list is not this chapter. Non-percipient is withdrawn where the attainment is named. The temporal classification of the six is the next verse.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_54 a vak:Karika ; vak:hasTopic vak:PervasiveCause, vak:MaturationCause .
vak:VipakaMeaning vak:settled false .
```
