# VAK_8.32

## Sanskrit

अष्टौ विमोक्षाः प्रथमावशुभा ध्यानयोर्द्वयोः ।
तृतीयोऽन्त्ये स चालोभः शुभारूप्याः समाहिताः ॥

## IAST

aṣṭau vimokṣāḥ prathamāv aśubhā dhyānayor dvayoḥ /
tṛtīyo 'ntye sa cālobhaḥ śubhārūpyāḥ samāhitāḥ //

## Padaccheda

aṣṭau | vimokṣāḥ | prathamau | aśubhau | dhyānayoḥ | dvayoḥ | tṛtīyaḥ | antye | saḥ | ca | alobhaḥ | śubha | ārūpyāḥ | samāhitāḥ

## Literal Translation

There are eight Deliverances. The first two are impurity-practices in the first two Dhyānas. The third is in the final Dhyāna, and it is non-greed. The pure and the formless are concentrated attainments.

## Philosophical Translation

Eight Deliverances are distinguished. The first two work through the perception of the unattractive and belong to the first two Dhyānas. The third, the Deliverance through the pure, belongs to the final Dhyāna and is constituted by non-greed. The pure and the formless Deliverances are stabilized meditative practices.

## Technical Vocabulary

- **vimokṣa** — Deliverance; a practiced release from domination by a given field of appearance
- **aśubha** — the unattractive or impure; the contemplative counter-aspect to attachment to form
- **dhyāna** — determinate meditative analysis
- **antya-dhyāna** — the final, fourth Dhyāna
- **alobha** — non-greed or non-appropriation
- **śubha-vimokṣa** — the Deliverance through the pure or beautiful
- **ārūpya** — the formless attainments
- **samāhita** — collected, stabilized, or mediately composed in practice

## Doctrinal Determination

This verse begins the classification of the eight Deliverances.

1. The first two are associated with aśubha practice and the first two Dhyānas.
2. The third is the pure Deliverance, situated in the fourth Dhyāna and constituted by non-greed.
3. The formless Deliverances are included among the stabilized meditative attainments.
4. The eighth Deliverance, the attainment of cessation, is specified in the next verse.

The verse classifies practices and their meditative bases. It does not yet authorize a global identification of every Deliverance with Samāpatti or every stabilized practice with Samādhi. Those relations must be determined case by case from the wording of the following verses.

## Logical Determination

The Deliverances are ordered by progressive freedom from domination by the presented field.

- In the first two, the practitioner changes the governing aspect of visible form through the unattractive.
- In the third, the same field is no longer appropriated through craving; the pure can be seen without possession.
- In the formless states, release proceeds beyond dependence on gross visible form.

Thus vimokṣa is first of all a practical power of release. It names neither a theory nor an abstract Concept, but a disciplined transformation in how a field can appear and bind.

## Organon Interpretation

The first three Deliverances show that freedom is not simple withdrawal from appearance.

The unattractive practices break the immediate authority of sensuous charm. The pure Deliverance then demonstrates a more difficult freedom: the practitioner can encounter the pure or beautiful without greed. This is stronger than merely replacing beauty with ugliness, because the field no longer needs to be negated in order for attachment to cease.

Accordingly:

```text
aśubha-practice
    freedom by counter-aspect

śubha-vimokṣa
    freedom within positive appearance
```

The verse therefore belongs to practical meditative technology. Its determinations should not be prematurely converted into a fixed Samāpatti/Samādhi schema. The text is showing how release is cultivated across distinct bases.

## OWL++ Seed

```turtle
@prefix vak: <https://example.org/vak/> .
@prefix yoga: <https://example.org/yoga/> .

vak:VAK_8_32 a vak:Karika ;
    vak:enumerates vak:EightDeliverances ;
    vak:beginsClassificationOf vak:VimoksaComplex .

vak:FirstDeliverance a vak:Vimoksa ;
    vak:usesPractice vak:Asubha ;
    vak:hasBasis yoga:FirstDhyana .

vak:SecondDeliverance a vak:Vimoksa ;
    vak:usesPractice vak:Asubha ;
    vak:hasBasis yoga:SecondDhyana .

vak:ThirdDeliverance a vak:SubhaVimoksa ;
    vak:hasBasis yoga:FourthDhyana ;
    vak:hasConstitutiveFactor vak:Alobha .

vak:FormlessDeliverance a vak:Vimoksa ;
    vak:belongsTo vak:StabilizedMeditativePractice .
```

## Commit History

- First-pass kārikā analysis committed after identifying the opening structure of the eight Deliverances.
- Samāpatti and Samādhi classifications intentionally left unforced pending the next verses and later bhāṣya pass.
