# VAK_3.21 Bhāṣya — Four State-Designations of the Continuum

## 1. Kārikā Anchor

> pūrvakleśā daśāvidyā saṃskārāḥ pūrvakarmaṇaḥ /
> saṃdhiskandhās tu vijñānaṃ nāmarūpam ataḥ param // 3.21 //

### Bhāṣya-informed study translation

> The state of afflictions in the prior birth is called Ignorance, because
> the other afflictions accompany it and operate under its influence. The
> former birth's meritorious and other karmic state, whose result matures
> here, is called Formations. At the moment of rebirth-linking in the
> mother's womb, the five Bases together are designated Discriminative
> Cognition. Name-and-Form follows that junction; the next verse specifies
> the boundary of this stage.

## 2. Continuous Sanskrit

> atha ka ime 'vidyādayaḥ?
>
> pūrvakleśā daśā 'vidyā /
>
> yā pūrvake janmani kleśāvasthā, seha avidyety ucyate / sāhacaryāt,
> tadvaśena teṣāṃ samudācārāc ca / rājāgamanavacane tadanuyātrikā-
> gamanasiddhavat /
>
> saṃskārāḥ pūrvakarmaṇaḥ /
>
> daśeti vartate / pūrvajanmany eva yā puṇyādikarmāvasthā seha
> saṃskārā ity ucyante, yasya karmaṇa iha vipākaḥ /
>
> saṃdhiskandhās tu vijñānam /
>
> mātuḥ kukṣī pratisaṃdhikṣaṇe pañca skandhā vijñānam /
>
> nāmarūpam ataḥ param // 3.21 //

This verse-unit runs from printed 131.19 through 132.01 in
`Vasubandhu/Sources/kosabhasya.txt`. The next pāda, `prāk
ṣaḍāyatanotpādāt`, begins the boundary definition for Name-and-Form and
belongs to VAK 3.22.

Word division and punctuation are editorial. The e-text reads
`pūrvakleśā daśā 'vidyā`; the Bhāṣya confirms *daśā*, “state,” while the
precise compound division remains provisional. The source reads
`mātuḥ kukṣī`; the translation provisionally construes this as the locative
“in the mother's womb.” The running source remains unchanged.

## 3. Scientific English Rendering

What, then, are these members beginning with Ignorance?

> The state of former afflictions is Ignorance.

The state of afflictions in the former birth is here called Ignorance. This
is because the other afflictions accompany it and because they operate under
its influence. It is like the accepted implication in the statement “the
king comes”: the king's retinue is understood to come with him.

> Formations are of former Karma.

The word “state” continues to be understood. The state of meritorious and
other Karma in the former birth, whose result matures here, is called
Formations.

> The junction Bases, however, are Discriminative Cognition.

At the moment of rebirth-linking in the mother's womb, the five Bases
together are Discriminative Cognition.

> After this comes Name-and-Form.

## 4. Commentary Structure

Vasubandhu asks what the members designate and answers through four stages:

```text
former afflictive state
    → designated Ignorance

former karmic state, whose result matures here
    → designated Formations

five Bases at the rebirth-junction
    → collectively designated Discriminative Cognition

stage after the junction
    → Name-and-Form
```

The royal-retinue comparison explains designation by predominance and
association. Ignorance names the former afflictive state without making all
its accompanying afflictions numerically identical to Ignorance. In the same
way, Discriminative Cognition names the junctional configuration of all five
Bases; it is not an isolated traveler.

The commentary does not yet define the duration or endpoint of
Name-and-Form. VAK 3.22 continues the explanation and marks the boundary at
the arising of the six Essences.

## 5. Interpretation

The placement of Formations beside Discriminative Cognition is structurally
significant, but they are not located in the same birth. Formations names
the former karmic state; Discriminative Cognition names the five-Base
configuration at the present rebirth-junction. Their sequence therefore
shows the transition across births: former Karma matures here, and the
junction is comprehended as a whole configuration rather than as a
transmigrating substance.

Name-and-Form may be a comprehensive twofold summary of the stage following
the junction, but this verse establishes only its succession. The next
verse supplies its endpoint. In the project's root-framework reading,
Dharma Essence integrates the sixfold Essence structure and includes Feeling
and Formations within its wider scope, while the twelve-member analysis
discriminates them into distinct positions. This verse locates Formations
in the prior birth; Feeling receives its own position in the present
sequence.

Horizontally, the verse locates conditions and stages across prior and
present births. Vertically, it reconstructs the mediacy through which the
prior karmic state is intelligible in the present junction. The immediate
appearance is retained while its conditioning is made knowable.

At the level of the Kośa's wider cognitive architecture, Vijñāna is
Discriminative Cognition joining and governing Perception and Conception;
their unity is not a homogeneous operation, and its Idea is disclosed in
the Cognition Base. Vijñāna governs Mind and guides the reading of Dharma
Base. Its relation to Avijñapti, and Avijñapti's distinct classifications
in Form Base and Dharma Base, must likewise remain discriminated. Here the
Bhāṣya names the junctional five Bases as Discriminative Cognition; that
local designation does not make Cognition identical with consciousness or
Mind.

## 6. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .

vak:VAK_3_21
    a vak:Karika ;
    vak:continues vak:VAK_3_20 ;
    vak:definesStage vak:FormerAfflictiveState,
        vak:FormerKarmicState, vak:RebirthJunction, vak:NameAndForm .

vak:FormerAfflictiveState
    a vak:TemporalState ;
    vak:hasDesignation vak:Avidya ;
    vak:hasRelation organon:AssociationAndPredominance .

vak:FormerKarmicState
    a vak:TemporalState ;
    vak:hasDesignation vak:Samskara ;
    vak:maturesAs vak:PresentResult .

vak:RebirthJunction
    a vak:TemporalState ;
    vak:hasBaseCount 5 ;
    vak:hasDesignation vak:Vijnana .

vak:NameAndForm
    a vak:TemporalState ;
    vak:follows vak:RebirthJunction ;
    vak:boundarySpecifiedIn vak:VAK_3_22 .

organon:AssociationAndPredominance
    a organon:ReflectiveDesignation ;
    organon:explains vak:Avidya .
```
