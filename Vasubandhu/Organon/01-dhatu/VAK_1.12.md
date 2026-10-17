# VAK_1.12 — The Four Great Elements

## 1. Sanskrit (Devanāgarī)

```sanskrit
भूतानि पृथिवीधातुरप्तेजोवायुधातवः ।
धृत्यादिकर्मसंसिद्धाः खरस्नेहोष्णतेरणाः ॥ १.१२ ॥
```

## 2. Sanskrit (IAST)

```text
bhūtāni pṛthivīdhātur aptejovāyudhātavaḥ /
dhṛtyādikarmasaṃsiddhāḥ kharasnehoṣṇateraṇāḥ // 1.12 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| bhūtāni | nominative neuter plural | the four Elements |
| pṛthivī-dhātuḥ | nominative | the Earth Principle |
| ap-tejo-vāyu-dhātavaḥ | nominative plural | Water, Fire, Wind Principles |
| karma-saṃsiddhāḥ | nominative plural | established in the functions |
| dhṛti-ādi | compound member | beginning with support |
| khara | compound member | hardness |
| sneha | compound member | cohesion |
| uṣṇatā | compound member | heat |
| īraṇā | compound member | impulsion |

*Dhātu* is the chapter word for Principle; *bhūta* names an Element. The four
Elements are identified as Earth, Water, Fire, and Wind Principles. In the
commentary’s mass-sentence, *skandha* means a mass, not a technical Base.

## 4. Grammar

```text
bhūtāni
    = pṛthivī-dhātuḥ
    + ap-tejo-vāyu-dhātavaḥ

those four
    = dhṛti-ādi-karma-saṃsiddhāḥ
    = khara-sneha-uṣṇatā-īraṇāḥ
```

The first line names them. The second gives function, then own-character.
The commentary pairs the lists in order.

## 5. Translation

### Literal Translation

> The Elements are the Earth Principle and the Water, Fire, and Wind Principles.
> They are established in functions beginning with support: hardness,
> cohesion, heat, and impulsion.

### Bhāṣya-informed study translation

> The four Great Elements are the Earth, Water, Fire, and Wind Principles,
> each sustaining its own-character and derived Form. In that order, their
> functions are support, gathering, ripening, and spreading (growth and
> extension), while their own-characters are hardness, cohesion, heat, and
> impulsion.

## 6. Philosophical Translation

Again, two lines. The first names the four. The second is function, then
own-character.

1.11 said depending on the Great Elements. This verse says which. Earth,
Water, Fire, and Wind Principles. Each holds its own-character and derived
Form. Each is a Principle, not a Base or Essence.

They hold their own-character and derived Form. That is why each is a Principle.
Greatness is two readings, both kept. Magnitude, as support of all other
Form. Or a great gathering in the masses, where that Principle operates
prominently. *Skandha* in that sentence is the mass. Not one of the five.

The functions are support, gathering, ripening, and spreading. Spreading is
increase and extension. The own-characters are hardness, cohesion, heat, and
impulsion. Impulsion is that by which the stream of Great Elements is driven to
arise in another place, as a lamp-flame moves.

The treatises say the Wind Principle is lightness of movement. That lightness
is also said to be derived Form. Therefore Wind is the Dharma whose
own-character is impulsion. The function makes the character evident. Not
the reverse, and not a fifth Element.

The next question distinguishes worldly Form from the Principle itself. Not
this verse.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| bhūta | Element | the four |
| mahābhūta | Great Element | magnitude, or gathering in masses |
| dhātu | Principle | here it names the principled determination |
| dhṛti | support | earth |
| saṃgraha | gathering | water |
| pakti | ripening | fire |
| vyūhana | spreading | wind; increase and extension |
| khara | hardness | own-character of earth |
| sneha | cohesion | own-character of water |
| uṣṇatā | heat | own-character of fire |
| īraṇā | impulsion | own-character of wind |
| svabhāva | own-character | the second list |
| laghutva | lightness | derived Form; not the Wind Principle |
| skandha | mass | in the commentary’s heap-sentence; not a technical Base |

## 8. Logical Determination

```text
1.11  depending on the Great Elements
1.12  which: four Great Elements, as Principles

Earth    support      hardness
Water    gathering    cohesion
Fire     ripening     heat
Wind     spreading    impulsion

Principle → holds own-character and derived Form
great     → support of all other Form
          or gathering in the masses

lightness → derived Form
Wind      → impulsion
function makes own-character evident

1.13 not opened
```

## 9. Interpretive Note

The hinge is *dhātu*, then the two lists. Interpretation of the function is
in the Bhāṣya.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_12 a vak:Karika ;
    vak:hasTopic vak:FourGreatElements ;
    vak:belongsTo vak:Dhatunirdesa .

vak:PrincipledEarth vak:function vak:Support ;
    vak:ownCharacter vak:Hardness .
vak:WaterPrinciple vak:function vak:Gathering ;
    vak:ownCharacter vak:Cohesion .
vak:FirePrinciple vak:function vak:Ripening ;
    vak:ownCharacter vak:Heat .
vak:WindPrinciple vak:function vak:Spreading ;
    vak:ownCharacter vak:Impulsion ;
    vak:not vak:Lightness .
vak:Lightness vak:is vak:DerivedForm .
```
