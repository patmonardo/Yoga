# VAK_1.45

## 1. Sanskrit (Devanāgarī)

> तद्विकारविकारित्वादाश्रयाश्चक्षुरादयः ।
>
> अतोऽसाधारणत्वाद्धि विज्ञानं तैर्निरुच्यते ॥ १.४५ ॥

## 2. Sanskrit (IAST)

> tadvikāravikāritvād āśrayāś cakṣurādayaḥ /
>
> ato 'sādhāraṇatvād dhi vijñānaṃ tair nirucyate // VAkK_1.45 //

Source saṃhitā form:

> tadvikāravikāritvādāśrayāścakṣurādayaḥ /
>
> ato 'sādhāraṇatvāddhi vijñānaṃ tairnirucyate // VAkK_1.45 //

## 3. Padaccheda

| Form | Padaccheda | Meaning |
|---|---|---|
| tad-vikāra-vikāritvāt | tad-vikāra-vikāritvāt | because it is altered by their alteration |
| āśrayāḥ | āśrayāḥ | supports, bases |
| cakṣur-ādayaḥ | cakṣus-ādayaḥ | eye and the others |
| ataḥ | ataḥ | therefore |
| asādhāraṇatvāt | a-sādhāraṇa-tvāt | because of being non-common / specific |
| hi | hi | indeed |
| vijñānam | vijñānam | knowledge |
| taiḥ | taiḥ | by them |
| nirucyate | nirucyate | is designated, explained, named |

## 4. Grammar

Eye and the other faculties are called **āśraya**, supports, because the knowledge is modified when they are modified.

```text
tad-vikāra-vikāritva
    = being altered by their alteration
```

If the eye changes, eye-knowledge changes. If the ear changes, auditory knowledge changes. Thus the support is not an external label but a determining condition.

The second half gives the naming principle:

```text
asādhāraṇatvāt
    because the supports are specific / non-common

vijñānaṃ taiḥ nirucyate
    knowledge is designated by them
```

Thus we say eye-knowledge, ear-knowledge, and so on because each knowledge is determined by its specific non-common support.

## 5. Literal Translation

> Eye and the others are supports because [knowledge] is altered by their alteration. Therefore, because they are non-common, knowledge is designated by them.

## 6. Philosophical Translation

> The eye and other faculties are supports because the corresponding knowledge changes when they change. Knowledge is therefore named from these supports because each support is specific and non-common to its own knowledge-domain.

Organon rendering:

> Knowledge is named by its determining support. The faculty is not an accidental instrument; its modification modifies the knowledge. Because each support is specific, each knowledge-domain receives its determination from that support.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| vikāra | alteration / modification | change in support reflected in knowledge |
| vikāritva | being altered | susceptibility to modification |
| āśraya | support / basis | determining support of knowledge |
| cakṣurādi | eye and the others | the six faculty supports |
| asādhāraṇa | non-common / specific | not shared across all knowledges |
| nirucyate | is designated | named/explained from its support |
| vijñāna | knowledge | never consciousness in this project layer |

## 8. Logical Determination

VAK_1.44 established support-time. VAK_1.45 establishes support-determination.

```text
support changes
    ↓
knowledge changes
```

Therefore:

```text
knowledge-domain
    is named from its specific support
```

The structure is:

```text
cakṣus altered
    → cakṣurvijñāna altered

śrotra altered
    → śrotravijñāna altered

support-specificity
    → knowledge-designation
```

## 9. Interpretive Note

This verse makes the support relation ontologically serious. A support is not merely an occasion. It is a determining basis whose alteration is reflected in the knowledge it supports.

The knowledge-domain is therefore neither independent subjectivity nor passive reflection. It is a supported disclosure whose character is shaped by a specific faculty-domain.

Organon sequence:

```text
1.44 temporal support
1.45 determining support
```

Kant-Fichte-Hegel note:

```text
faculty
    is not a container

faculty
    is a determining condition

knowledge
    takes its determinate name
    from the support that conditions it
```

This is very close to a principle of form-determination: the support is the form through which the disclosure is determined.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_45
    a vak:Karika ;
    rdfs:label "VAK 1.45" ;
    vak:hasIAST "tadvikāravikāritvād āśrayāś cakṣurādayaḥ / ato 'sādhāraṇatvād dhi vijñānaṃ tair nirucyate" ;
    vak:hasTopic vak:SupportDeterminesKnowledge ;
    vak:belongsTo vak:Dhatunirdesa .

vak:SupportDeterminesKnowledge
    a vak:LogicalDetermination ;
    rdfs:label "support determines knowledge" ;
    vak:hasRule vak:SupportAlterationAltersKnowledge .

vak:SupportAlterationAltersKnowledge
    a vak:Rule ;
    rdfs:label "knowledge is altered by alteration of support" .

vak:KnowledgeDesignationBySupport
    a vak:NamingPrinciple ;
    rdfs:label "knowledge is named from its specific support" ;
    vak:groundedIn vak:Asadharanatva .
```

## 11. Commit History

- Added Organon analysis for VAK_1.45.
- Establishes the faculties as supports because knowledge changes when they change.
- Explains why knowledge-domains are named from their specific supports.
- Adds support-determination to the chapter sequence after temporal support.
