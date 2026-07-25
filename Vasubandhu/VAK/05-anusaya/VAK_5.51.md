# VAK 5.51

## Sanskrit

दृष्ट्यामर्शात् प्रदाशस्तु शाठ्यं दृष्टिसमुत्थितम् ।
तत्राह्रीक्यानपत्राप्यस्त्यानमिद्धोद्धवा द्विधा ॥ ५.५१ ॥

## IAST

dṛṣṭyāmarśāt pradāśas tu śāṭhyaṃ dṛṣṭi-samutthitam /
tatrāhrīkyānapatrāpyastyānamiddhoddhavā dvidhā // 5.51 //

## Padaccheda

dṛṣṭi-āmarśāt | pradāśaḥ | tu | śāṭhyam | dṛṣṭi-samutthitam | tatra | āhrīkyam | anapatrāpyam | styānam | middham | uddhavaḥ | dvidhā

## Grammar

- **dṛṣṭi-āmarśāt** — ablative singular compound, “from grasping at a view,” or “from appropriative insistence upon a view.”
- **pradāśaḥ** — nominative singular masculine, “contentious indignation,” “hostile insistence,” or “consuming resentment.”
- **tu** — indeclinable, “but,” marking a contrast with the derivations given in the preceding verse.
- **śāṭhyam** — nominative singular neuter, “crookedness,” “fraudulent concealment of intention.”
- **dṛṣṭi-samutthitam** — nominative singular neuter, “arisen from view,” “generated from a doctrinal or evaluative standpoint.”
- **tatra** — indeclinable, “among these,” referring to the derivative afflictions under discussion.
- **āhrīkyam** — nominative singular neuter, absence of inward moral restraint.
- **anapatrāpyam** — nominative singular neuter, absence of concern before others or before consequences.
- **styānam** — nominative singular neuter, mental rigidity or torpor.
- **middham** — nominative singular neuter, sleepiness or oppressive heaviness.
- **uddhavaḥ** — nominative singular masculine, agitation or restlessness; the transmitted form corresponds to **auddhatya** in the doctrinal list.
- **dvidhā** — indeclinable, “twofold,” referring to two modes of abandonment: through seeing and through cultivation.

## Literal Translation

Contentious indignation arises from grasping at a view, while crookedness arises from view. Among these, shamelessness, disregard, rigidity, torpor, and agitation are twofold.

## Philosophical Translation

Pradāśa is generated when a view is not merely held but appropriatively seized and defended; śāṭhya arises from view as a crooked practical presentation of that standpoint. Among the derivative afflictions, five—absence of inward restraint, absence of concern, mental rigidity, torpor, and agitation—belong to both modes of removal: they may be abandoned through seeing or through cultivation.

## Structural Analysis

VAK 5.48–5.50 mapped derivative afflictions back to the roots of attachment, hostility, ignorance, and doubt. VAK 5.51 adds a specifically cognitive source:

```text
view
    ↓
appropriative insistence upon view
    ↓
contentious indignation
```

and:

```text
view
    ↓
crooked practical presentation
    ↓
śāṭhya
```

The verse then changes the classificatory standpoint. It no longer asks only:

```text
From which root does this affliction arise?
```

It asks:

```text
By which path-operation is it abandoned?
```

This introduces the distinction between:

```text
darśana-heya
    abandoned through seeing

bhāvanā-heya
    abandoned through cultivation
```

The five listed derivative afflictions are **dvidhā** because they may participate in both fields.

## Technical Vocabulary

### Dṛṣṭi-āmarśa

A view becomes afflictively intensified when it is seized as one’s own position and defended through appropriative insistence.

```text
dṛṣṭi
    standpoint

āmarśa
    appropriative grasping
```

The compound therefore expresses more than false cognition. It expresses identification with cognition.

### Pradāśa

The exact semantic range should be checked against the Bhāṣya, but the structural sense is clear: a view is defended through consuming opposition, hostile insistence, or contentious resentment.

Working translation:

```text
pradāśa
    =
contentious indignation
```

### Śāṭhya

Crookedness in the presentation of intention. It is not merely factual deception but the practical bending of appearance so that one’s real motive remains concealed.

```text
held view
    ↓
strategic self-presentation
    ↓
śāṭhya
```

### Dvidhā

“Twofold” concerns the path by which the determination is abandoned.

```text
seeing
    removes the determination
    insofar as it depends upon false discernment

cultivation
    removes the determination
    insofar as it persists as habituated formation
```

## Doctrinal Determination

The verse distinguishes two kinds of relation to view.

First:

```text
view
    + appropriative grasping
    = pradāśa
```

Here the view becomes a center of conflict. Opposition to the view is experienced as opposition to the one who has appropriated it.

Second:

```text
view
    + crooked practical expression
    = śāṭhya
```

Here the cognitive position deforms outward conduct and presentation.

The five twofold afflictions are:

```text
āhrīkya
anapatrāpya
styāna
middha
auddhatya
```

They cannot be assigned exclusively either to error destroyed by seeing or to habit destroyed by cultivation. Their manifestations may be linked to both.

This gives the Path a more exact rationale:

```text
not every manifest affliction
is removed by one and the same operation
```

The practitioner must discriminate whether a state is sustained by:

```text
false seeing
habitual formation
or both
```

## Logical Determination

VAK 5.51 introduces a second axis of classification.

The first axis is genetic:

```text
root
    → derivative manifestation
```

The second axis is soteriological:

```text
determination
    → mode of abandonment
```

A single derivative affliction may therefore have:

```text
one causal origin
    and
more than one path-location
```

This prevents a flat taxonomy. The same determination can be classified by:

```text
what generates it
how it functions
where it appears
how it is removed
```

The verse therefore begins to transform the afflictive taxonomy into a logic of the Path.

## Organon Note

This verse suggests a rule for speculative modeling:

```text
A determination is not fully specified
until both its ground
and its mode of sublation are known.
```

For the Platform:

```text
AfflictiveDetermination
    hasGround RootAffliction
    hasManifestation DerivativeAffliction
    hasRemovalMode Seeing | Cultivation
```

The dvidhā cases require a non-exclusive relation:

```text
hasRemovalMode some Seeing
hasRemovalMode some Cultivation
```

This is important because the Path is not a single operation applied uniformly. It is a differentiated sequence of rational acts, each corresponding to a distinct structure of error or persistence.

## OWL++ Seed

```ttl
vak:RemovalMode a owl:Class .
vak:SeeingRemoval a owl:Class ;
  rdfs:subClassOf vak:RemovalMode .
vak:CultivationRemoval a owl:Class ;
  rdfs:subClassOf vak:RemovalMode .

vak:hasRemovalMode a owl:ObjectProperty .
vak:arisesFromView a owl:ObjectProperty .
vak:arisesFromViewGrasping a owl:ObjectProperty .

vak:Pradasa a owl:Class ;
  rdfs:subClassOf vak:KlesaStain ;
  rdfs:subClassOf [
    a owl:Restriction ;
    owl:onProperty vak:arisesFromViewGrasping ;
    owl:someValuesFrom vak:ViewGrasping
  ] .

vak:Shathya a owl:Class ;
  rdfs:subClassOf vak:KlesaStain ;
  rdfs:subClassOf [
    a owl:Restriction ;
    owl:onProperty vak:arisesFromView ;
    owl:someValuesFrom vak:AfflictedView
  ] .
```

Possible shape for the twofold group:

```ttl
vak:TwofoldRemovalShape a sh:NodeShape ;
  sh:targetClass vak:TwofoldDerivativeAffliction ;
  sh:property [
    sh:path vak:hasRemovalMode ;
    sh:qualifiedValueShape [ sh:class vak:SeeingRemoval ] ;
    sh:qualifiedMinCount 1
  ] ;
  sh:property [
    sh:path vak:hasRemovalMode ;
    sh:qualifiedValueShape [ sh:class vak:CultivationRemoval ] ;
    sh:qualifiedMinCount 1
  ] .
```

## Bhāṣya Questions

1. How precisely does the Bhāṣya define **pradāśa**?
2. Does **dṛṣṭyāmarśa** indicate grasping at any afflicted view, or especially attachment to one’s own doctrinal position?
3. Why is **śāṭhya** said to arise from view rather than directly from attachment or ignorance?
4. Does **dvidhā** unambiguously mean both **darśana-heya** and **bhāvanā-heya**?
5. Why are exactly āhrīkya, anapatrāpya, styāna, middha, and auddhatya included in the twofold group?
6. How does VAK 5.52 distribute the remaining derivative afflictions between cultivation-abandonment and independent occurrence?
