# VAK_3.22 Bhāṣya — From Name-and-Form to Contact

## 1. Kārikā Anchor

> prāk ṣaḍāyatanotpādāt tatpūrvaṃ trikasaṃgamāt /
> sparśaḥ prāk sukhaduḥkhādikāraṇajñānaśaktitaḥ // 3.22 //

### Bhāṣya-informed study translation

> Name-and-Form names the interval after junction consciousness and before
> the arising of the six Essences. The succeeding interval is called the
> six-Essence stage, even though its boundary could be stated as the arising
> of four Essences, because the full sixfold organization is established
> then. That stage continues until Faculty, Condition, and Discriminative
> Cognition meet. From their conjunction, Contact arises; the Contact-stage
> lasts until the capacity to discriminate the causes of pleasant, painful,
> and neutral Feeling is established.

## 2. Continuous Sanskrit

> prāk ṣaḍāyatanotpādāt /
>
> saṃdhicittāt pareṇa yāvat ṣaḍāyatanaṃ notpadyate sā 'vasthā nāmarūpam /
> tāvat ṣaḍāyatanam ity ucyate / prāk caturāyatanotpādād iti vaktavye
> ṣaḍāyatanavacanaṃ tadā tadvyavasthāpanāt /
>
> tatpūrvaṃ trikasaṃgamāt /
>
> utpanne ṣaḍāyatane sāvasthā tāvat ṣaḍāyatanaṃ ity ucyate yāvad
> indriyaviṣayavijñānatrikasaṃnipātaḥ /
>
> sparśaḥ prāk sukhaduḥkhādikāraṇajñānaśaktitaḥ // 3.22 //
>
> trayāṇāṃ saṃnipātāt sparśo bhavati / sa yāvad
> vedanātrayakāraṇaparicchedena samartho bhavati sā 'vasthā sparśa ity
> ucyate /

This natural unit runs from printed 132.02 through 132.11 in
`Vasubandhu/Sources/kosabhasya.txt`. The next statement at 132.11,
`paricchedasāmarthye sati`, introduces the Feeling-stage and belongs to
VAK 3.23.

Word division and punctuation are editorial. The e-text's
`prakcaturāyatanotpādādini` is provisionally divided as
`prāk caturāyatanotpādād iti`. The source's `sā 'vasthā` is joined by
ordinary word division. The running source remains unchanged.

## 3. Scientific English Rendering

> Before the arising of the six Essences.

The stage after junction consciousness and before the six Essences have
arisen is Name-and-Form. After that it is called the six-Essence stage.
Although it could have been said “before the arising of four Essences,” the
designation “six Essences” is used because the sixfold organization is
established at that time.

> That stage is before the conjunction of the triad.

Once the six Essences have arisen, the stage is called the six-Essence stage
until the conjunction of the triad of Faculty, Condition, and
Discriminative Cognition.

> Contact is before the capacity to discriminate the causes of pleasure,
> pain, and the other Feeling.

Contact arises from the conjunction of the three. The stage in which one
becomes capable of discriminating the causes of the three Feelings is called
Contact.

## 4. Commentary Movement

The Bhāṣya specifies a succession of temporal and cognitive boundaries:

```text
after junction consciousness, before six Essences arise
    → Name-and-Form

sixfold Essence organization established, before triad conjunction
    → six-Essence stage

Faculty + Condition + Discriminative Cognition meet
    → Contact arises

capacity to discriminate causes of three Feelings develops
    → limit of the Contact-stage
```

The four-versus-six question concerns designation. The Bhāṣya acknowledges
that four Essences could mark immediate emergence, but explains that the
six-Essence name applies because the full sixfold organization is
established then. It does not identify which four Essences newly arise.

The source gives the cognitive triad directly: Faculty, Condition, and
Discriminative Cognition. Their conjunction is not itself one of the three
members; Contact is the relation that arises from their conjunction.
Here Condition is *viṣaya*: a specific moment of the Seen and the playground
of the Faculties. Object is the comprehended truth of Vastu, not this
Condition.

## 5. Interpretation

### Essence structure and temporal boundaries

This verse makes the sixfold Essence stage precise as a temporal
organization, not merely a count. The Bhāṣya's four-versus-six distinction
shows how immediate emergence is designated through the full framework it
establishes. In the project's root-framework reading, Dharma Essence takes
up the sixfold Essence structure. Feeling and Formations remain within that
wider framework but retain distinct positions in the twelve-member
sequence.

### Contact as a relation

The horizontal structure is the sixfold range of cognitive access. The
vertical movement is from that organized capacity to the actual conjunction
of Faculty, Condition, and Discriminative Cognition, and then to the
capacity for discriminating the causes of Feeling. Contact is not the
Essence-stage itself or one of the triad's members; it is the relation
arising from their conjunction. The higher discriminative capacity marks a
further phase rather than dissolving the earlier distinctions. The sequence
thus determines Objective Dharmas through their boundaries and relations,
not as a flat inventory.

### Vijñāna in the wider Kośa

At the level of the Kośa's wider cognitive architecture, Vijñāna is
Discriminative Cognition joining and governing Perception and Conception;
their unity is not a homogeneous operation, and its Idea is disclosed in
the Cognition Base. Vijñāna governs Mind and guides the reading of Dharma
Base. Its relation to Avijñapti, and Avijñapti's distinct classifications
in Form Base and Dharma Base, must likewise remain discriminated. Here the
Bhāṣya's triad preserves Faculty, Condition, and Discriminative Cognition
as distinct terms.

## 6. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .

vak:VAK_3_22
    a vak:Karika ;
    vak:continues vak:VAK_3_21 ;
    vak:definesStage vak:NameAndFormStage, vak:SixEssenceStage,
        vak:ContactStage ;
    vak:definesRelation vak:CognitiveTriad .

vak:NameAndFormStage
    a vak:TemporalStage ;
    vak:endsBefore vak:SixEssencesArise .

vak:SixEssenceStage
    a vak:TemporalStage ;
    vak:endsBefore vak:CognitiveTriadConjunction .

vak:CognitiveTriad
    a organon:CognitiveRelation ;
    vak:hasMember vak:Faculty, vak:Condition, vak:Vijnana ;
    vak:conjunctionProduces vak:Contact .

vak:ContactStage
    a vak:TemporalStage ;
    vak:beginsAt vak:CognitiveTriadConjunction ;
    vak:endsBefore vak:CauseDiscriminationCapacity .

vak:CauseDiscriminationCapacity
    a organon:DiscriminativeCapacity ;
    vak:concerns vak:ThreeFeelingsCauses .
```
