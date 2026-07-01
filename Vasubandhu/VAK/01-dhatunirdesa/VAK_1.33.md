# VAK_1.33

## 1. Sanskrit (Devanāgarī)

> निर्ऊपणानुस्मरणविकल्पेनाविकल्पकाः ।
>
> तौ प्रज्ञा मानसी व्यग्रा स्मृतिः सर्वैव मानसी ॥

## 2. Sanskrit (IAST)

> nirūpaṇānusmaraṇavikalpenāvikalpakāḥ /
>
> tau prajñā mānasī vyagrā smṛtiḥ sarvaiva mānasī //

## 3. Padaccheda

| Pada        | Form               | Meaning                                                      |
| ----------- | ------------------ | ------------------------------------------------------------ |
| nirūpaṇa    | stem in compound   | determination, specification, ascertainment                  |
| anusmaraṇa  | stem in compound   | recollection, reproductive remembrance                       |
| vikalpena   | instr.sg.n.        | by imaginative differentiation / constructive discrimination |
| avikalpakāḥ | nom.pl.m.          | non-imaginative, non-constructive, without vikalpa           |
| tau         | nom.du.m.          | those two                                                    |
| prajñā      | nom.sg.f.          | principle, discriminative knowing                            |
| mānasī      | nom.sg.f.          | mental, belonging to manas                                   |
| vyagrā      | nom.sg.f.          | occupied, engaged, distracted                                |
| smṛtiḥ      | nom.sg.f.          | recollection, memory                                         |
| sarvā eva   | nom.sg.f. emphatic | entirely, wholly                                             |
| mānasī      | nom.sg.f.          | mental, belonging to manas                                   |

## 4. Literal Translation

> Those two are non-constructive with respect to determination, recollection, and vikalpa. Prajñā is mental; memory, being occupied, is entirely mental.

## 5. Philosophical Translation

> The two immediate knowledge-events are non-constructive: they do not yet operate through determination, reproductive recollection, or imaginative differentiation. Prajñā belongs to the mental domain, and memory, insofar as it is actively occupied with recollection, is wholly mental.

## 6. Technical Vocabulary

| Sanskrit   | Rendering                          | Note                                                  |
| ---------- | ---------------------------------- | ----------------------------------------------------- |
| nirūpaṇa   | determination / specification      | act of ascertaining or specifying                     |
| anusmaraṇa | recollective reproduction          | remembrance as renewed presentation                   |
| vikalpa    | imaginative differentiation        | constructive differentiating power, not final concept |
| avikalpaka | non-constructive                   | prior to vikalpa                                      |
| prajñā     | principle / discriminative knowing | mental discrimination                                 |
| smṛti      | memory / recollection              | mental retention and recall                           |
| mānasī     | mental                             | belonging to manas                                    |

## 7. Logical Determination

Immediate Knowledge
        ↓
Non-Constructive Operation
        ↓
Determination / Recollection / Vikalpa
        ↓
Mental Principle and Memory

## 8. Interpretive Note

This verse distinguishes immediate knowledge-events from the later mental operations of determination, recollection, and vikalpa. The key point is that vikalpa should not be rendered simply as final conceptualization. Here it marks a constructive differentiating power within the mental sequence. Prajñā and smṛti are explicitly assigned to the domain of manas.

## 9. OWL++ Seed

```ttl
vak:VAK_1_33
    rdf:type vak:Karika ;
    vak:defines vak:Avikalpaka ;
    vak:defines vak:Nirupana ;
    vak:defines vak:Anusmarana ;
    vak:defines vak:Vikalpa ;
    vak:defines vak:Prajna ;
    vak:defines vak:Smrti ;
    vak:assignsDomain vak:Manas .

vak:Avikalpaka
    vak:priorTo vak:Nirupana , vak:Anusmarana , vak:Vikalpa .

vak:Prajna
    vak:belongsTo vak:Manas .

vak:Smrti
    vak:belongsTo vak:Manas .
```

## 10. Commit History

- Initial artifact for VAK_1.33.
- Corrects the padaccheda by separating prajñā and mānasī.
- Avoids reducing vikalpa to final conceptualization.
- Assigns prajñā and smṛti to the mental domain.
