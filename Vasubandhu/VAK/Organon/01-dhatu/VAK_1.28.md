# VAK_1.28

## 1. Sanskrit (Devanāgarī)

> छिद्रमाकाशधात्वाख्यम् आलोकतमसी किल ।
>
> विज्ञानधातुर्विज्ञानं सास्रवं जन्मनिश्रयाः ॥ १.२८ ॥

## 2. Sanskrit (IAST)

> chidram ākāśadhātvākhyam ālokatamasī kila /
>
> vijñānadhātur vijñānaṃ sāsravaṃ janmaniśrayāḥ // 1.28 //

## 3. Padaccheda

```text
ākāśadhātvākhyam    → ākāśa-dhātu-ākhyam
ālokatamasī          → āloka-tamasī
vijñānadhātuḥ        → vijñāna-dhātuḥ
sāsravam             → sa-āsravam
janmaniśrayāḥ        → janma-niśrayāḥ
```

| Form | Morphology | Lexical force here |
|---|---|---|
| chidram | nominative neuter singular | aperture, opening, cavity |
| ākāśa-dhātu-ākhyam | nominative neuter singular compound | bearing the name “space-domain” |
| āloka-tamasī | nominative neuter dual compound | light and darkness |
| kila | reportive particle | so it is said; according to the received account |
| vijñāna-dhātuḥ | nominative masculine singular | consciousness-domain |
| vijñānam | nominative neuter singular | consciousness |
| sa-āsravam | nominative neuter singular | accompanied by outflows; contaminated |
| janma-niśrayāḥ | nominative masculine plural compound | supports or bases of birth |

`Dhātu` is rendered **Domain** in the Organon study. “Element” remains useful
when discussing conventional translations of the sūtra's sixfold list, but
it would obscure the inward classificatory work of this chapter if allowed
to govern the primary rendering.

## 4. Grammar

The first statement identifies a named referent:

```text
chidram
    an aperture

ākāśa-dhātu-ākhyam
    is called the space-domain
```

The following dual, `āloka-tamasī`, supplies the received Vaibhāṣika
analysis of that aperture: no separate cavity is perceived apart from the
light or darkness occupying it. `Kila` is reportive and should remain
audible in translation; Vasubandhu is transmitting a school explanation,
not presenting “aperture equals light and darkness” as an unmarked truism.

The second statement restricts the consciousness-domain:

```text
vijñāna-dhātuḥ
    the consciousness-domain

vijñānaṃ sāsravam
    is outflow-bound consciousness
```

The final `janmaniśrayāḥ` is plural. The Bhāṣya makes all six Domains—earth,
water, fire, wind, space, and consciousness—its subject. They are taught
together because they support birth. Consequently, it is grammatically and
doctrinally misleading to attach “support of birth” only to the singular
consciousness-domain.

The Bhāṣya defines the relevant life-continuum as extending from
rebirth-linking consciousness (`pratisandhicitta`) through death-consciousness
(`cyuticitta`). Because outflow-free consciousness does not support such
birth, it is excluded from `vijñānadhātu` in this particular six-domain
teaching.

## 5. Translation

### Close syntactic construe

> An aperture is called the space-domain—light and darkness, according to the received account. The consciousness-domain is outflow-bound consciousness; [the six Domains] are supports of birth.

### Bhāṣya-informed translation

> In the sūtra's teaching of six Domains, “space-domain” denotes a conditioned aperture, analyzed by the Vaibhāṣikas as the light or darkness appearing there. “Consciousness-domain” denotes only consciousness accompanied by outflows. The six are grouped together because they support the continuum of birth.

The clarifying phrases in the second rendering derive from the Bhāṣya. They
must not be silently read into every occurrence of `ākāśa` or `vijñāna`.

## 6. Philosophical Translation

> The same name can operate at different levels of determination. Here “space” is not unconditioned non-obstruction but a conditioned opening within visible appearance. Here “consciousness” is not consciousness without qualification but the outflow-bound consciousness implicated in birth. Their place is determined by the function of the particular teaching in which they occur.

Organon rendering:

> The Discriminator prevents universal terms from floating free of their determinate use. Space as absolute non-obstruction must be distinguished from the aperture through which appearance is articulated as light and darkness. Consciousness as such must be distinguished from the conditioned consciousness sustaining the course of birth. The Domain is not an outward element; it is the precisely bounded range within which a determination has validity.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| ṣaḍ-dhātu | six Domains | earth, water, fire, wind, space, and consciousness in this sūtra teaching |
| chidra | aperture / opening | conditioned referent of `ākāśadhātu` here |
| ākāśa | unconditioned space / non-obstruction | asaṃskṛta established earlier; not the present aperture |
| ākāśadhātu | space-domain | conditioned aperture included within visible form |
| āloka | light | one perceptible determination of the aperture |
| tamas | darkness | the other perceptible determination of the aperture |
| kila | according to the received account | marks the Vaibhāṣika explanation |
| aghasāmantaka-rūpa | aperture-bordering form | technical and etymologically disputed designation for the conditioned space-domain |
| vijñānadhātu | consciousness-domain | here restricted to outflow-bound consciousness |
| sāsrava | accompanied by outflows / contaminated | implicated in conditioned existence and birth |
| anāsrava | outflow-free | excluded from this six-domain consciousness classification |
| janmaniśraya | support of birth | shared functional reason for grouping the six Domains |
| pratisandhicitta | rebirth-linking consciousness | opening consciousness of a new life-continuum |
| cyuticitta | death-consciousness | terminal consciousness of that continuum |

## 8. Logical Determination

The ambiguity tested by the verse is:

```text
Named(x, AkashaDhatu)
    → UnconditionedSpace(x)?

Named(y, VijnanaDhatu)
    → EveryKindOfConsciousness(y)?
```

Both unrestricted inferences are denied:

```text
AkashaDhatuInSixDomainTeaching
    = ConditionedAperture
    = LightOrDarknessForm
    → IncludedIn(RupaDhatu)

VijnanaDhatuInSixDomainTeaching
    = SasravaConsciousness
    → IncludedIn(SevenConsciousnessDhatus)
```

The remaining four are reintegrated as follows:

```text
Earth | Water | Fire | Wind
    → IncludedIn(SprastavyaDhatu)
```

The governing functional restriction is:

```text
MemberOf(x, SixDomainTeaching)
    → Supports(x, BirthContinuum)

AnasravaConsciousness(x)
    → DoesNotSupport(x, BirthContinuum)
    → ExcludedFrom(x, VijnanaDhatuInThisTeaching)
```

Thus the six-domain list is fully assignable within the established eighteen
Domains:

```text
four material supports → tangible-domain
conditioned aperture  → visible-form domain
conditioned awareness → seven consciousness-domains
```

## 9. Interpretive Note

VAK 1.28 is the worked proof of the method stated in 1.27. The sūtra gives a
six-domain teaching whose names initially appear to cross the boundaries of
the eighteen-domain system. Vasubandhu does not reject the sūtra and does not
multiply the fundamental classes. He asks what `ākāśadhātu` and
`vijñānadhātu` denote in this precise instructional context.

The result is a decisive distinction between two spaces:

```text
unconditioned ākāśa
    = non-obstruction
    = not produced

conditioned ākāśadhātu here
    = aperture apprehended through light or darkness
    = visible-form domain
```

Our earlier poetic contact between unconditioned space and Brahman belongs
entirely to the Organon comparison. The present verse neither retracts the
unconditioned status of `ākāśa` nor applies that status to every expression
containing the word. It shows why conceptual discipline is necessary: the
shared word does not abolish the difference of Domains.

The restriction of consciousness is equally powerful. `Vijñāna` here is
not pure Buddha Mind and not liberating cognition. It is precisely the
conditioned consciousness that participates in the span from rebirth-linking
to death. The six Domains constitute a genetic support-system of embodied
birth, but they do not thereby become six new primitives outside the
eighteen Domains.

This completes the present sequence of classificatory problems:

```text
1.24  distinguish technical names from universal class-words
1.25  reintegrate inherited Dharma-collections by their nature
1.26  state what can individuate one teaching-unit
1.27  formulate classification by referent, scope, and own-characteristic
1.28  demonstrate the method on the six-domain teaching
```

The lesson for the Organon is exact and restrained: a Domain is not a lump
of outward matter. It is a determination whose extension depends upon the
specified referent, scope, and function. The classifier becomes rational by
refusing both verbal equivalence and external enumeration.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_28
    a vak:Karika ;
    rdfs:label "VAK 1.28" ;
    vak:hasTopic vak:ReintegrationOfSixDomains ;
    vak:belongsTo vak:Dhatunirdesa .

vak:UnconditionedSpace
    a vak:AsamskrtaDharma ;
    vak:hasCharacteristic vak:NonObstruction ;
    vak:distinctFrom vak:ConditionedSpaceDomain .

vak:ConditionedSpaceDomain
    a vak:ConditionedAperture,
        vak:VisibleForm ;
    vak:manifestAs vak:Light,
        vak:Darkness ;
    vak:includedIn vak:RupaDhatu .

vak:ConsciousnessDomainInSixDomainTeaching
    a vak:SasravaConsciousness ;
    vak:supports vak:BirthContinuum ;
    vak:includedIn vak:SevenConsciousnessDhatus ;
    vak:excludes vak:AnasravaConsciousness .

vak:SixDomainTeaching
    a vak:SpecializedScripturalClassification ;
    vak:hasFunction vak:SupportOfBirth ;
    vak:reintegratedWithin vak:EighteenDhatus .
```
