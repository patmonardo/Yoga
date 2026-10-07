# VAK_2.15

## 1. Sanskrit (Devanāgarī)

> निरोधयत्युपरमान्नारूप्ये जीवितं मनः ।
>
> उपेक्षां चैव रूपेऽष्टौ कामे दश नवाष्टौ वा ॥ २.१५ ॥

## 2. Sanskrit (IAST)

> nirodhayaty uparamān nārūpye jīvitaṃ manaḥ /
>
> upekṣāṃ caiva rūpe 'ṣṭau kāme daśa navāṣṭau vā // 2.15 //

The transmitted sequence `uparamān nārūpye` is morphologically compressed
and uncertain in isolation. The Bhāṣya unambiguously construes the clause as
the faculties ceased by one dying in the formless realm; that construction
governs the translations below.

## 3. Lexical Analysis

```text
nirodhayaty        → nirodhayati
uparamān nārūpye  → transmitted phrase; Bhāṣya: at death in the formless realm
jīvitaṃ            → jīvitam
manaḥ              → manaḥ
upekṣāṃ caiva      → upekṣām ca eva
rūpe 'ṣṭau         → rūpe aṣṭau
kāme               → kāme
daśa               → daśa
navāṣṭau vā        → nava aṣṭau vā
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| nirodhayati | third-person singular causative present | causes to cease / brings to cessation |
| uparamān nārūpye | transmitted sequence | construed by the Bhāṣya with death in the formless realm |
| jīvitam | accusative neuter singular | life-faculty |
| manaḥ | accusative neuter singular | mind-faculty |
| upekṣām | accusative feminine singular | neutral-feeling faculty |
| ca eva | conjunction plus emphatic particle | and indeed / and also |
| rūpe | locative neuter singular | in the form realm |
| aṣṭau | accusative plural numeral | eight faculties |
| kāme | locative masculine singular | in the desire realm |
| daśa | accusative plural numeral | ten faculties |
| nava | accusative plural numeral | nine faculties |
| vā | alternative particle | or |

Here `nirodha` is terminal cessation of possessed faculties at death. It is
not, without further qualification, the liberative cessation discussed in
other contexts.

## 4. Grammar

The Bhāṣya supplies the governing question:

```text
kasmindhātau mriyamāṇaḥ katīndriyāṇi nirodhayati
    → dying in which realm, how many faculties does one cause to cease?
```

It resolves the first line as:

```text
formless realm:
    jīvitam
    manaḥ
    upekṣām
        → life, mind, and neutral feeling cease
```

The second line gives two further realm counts:

```text
rūpe aṣṭau
    → eight in the form realm

kāme daśa nava aṣṭau vā
    → in the desire realm, ten, nine, or eight
```

The alternatives depend upon sexual configuration:

```text
both sexual faculties present
    → 10

one present
    → 9

neither present
    → 8
```

The Bhāṣya explicitly limits these Kārikā counts to `sakṛn-maraṇa`, death in
which the relevant faculties cease all at once. It introduces gradual death
only with the next Kārikā, so that separate count is not imported here.

## 5. Scientific English Rendering

### Kārikā

> At death in the formless realm [according to the Bhāṣya's construal], one causes life, mind, and neutral feeling to cease; in the form realm, eight; in the desire realm, ten, nine, or eight.

### Bhāṣya-informed rendering

> At death in the formless realm, the faculties of life, mind, and neutral feeling cease. At death in the form realm, those three and the five sensory faculties cease, making eight. At simultaneous death in the desire realm, eight, nine, or ten cease according to whether neither, one, or both sexual faculties are present.

The realm profiles are:

```text
formless:
    life + mind + neutral feeling = 3

form:
    life + mind + neutral feeling
    + five sensory faculties = 8

desire:
    base eight
    + no sexual faculty = 8
    + one sexual faculty = 9
    + both sexual faculties = 10
```

## 6. Interpretation

The Bhāṣya explicitly limits the realm counts to death occurring all
at once. It then distinguishes gradual death, whose fourfold cessation
is continued in the opening of VAK 2.16, and adds five Faculties when
the terminal mind is wholesome. Realm, sexual configuration, death-mode,
and ethical condition therefore delimit the relevant counts. The
transmitted phrase *uparamān nārūpye* remains uncertain in isolation;
the Bhāṣya's construal governs the translation.

In the Kant-informed Techne, cessation at death and initial acquisition
as maturation-result are distinct predicates. The Dhātu crosswalk locates
Faculty-status within the Base–Essence–Principle architecture; this
passage applies cessation to the Faculties possessed in the stated
terminal context. This is a project-level interpretation, not terminology
supplied by the Bhāṣya.

The Kośa's governing synthesis: Vijñāna is Discriminative Cognition joining
and governing Perception and Conception. Their unity is Inconceivable as a
homogeneous operation; its Idea is disclosed in the Cognition Base. Vijñāna
governs Mind and guides the reading of Dharma Base. *Avijñapti* is the
bridge, one Dharma classified in both Form Base and Dharma Base; Vijñāna
bears a *prati* relation to it.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| tyāga | loss / relinquishment | Bhāṣya heading for the inverse topic after acquisition |
| nirodhayati | causes to cease | cessation of possessed faculties at death |
| uparama | stopping / death | terminal context indicated by the Kārikā's compressed phrase |
| maraṇa | death | Bhāṣya's explicit determination of the context |
| ārūpya | formless realm | three-faculty terminal profile |
| rūpa | Form Realm | eight-faculty terminal profile |
| kāma | desire realm | eight-, nine-, or ten-faculty terminal profile |
| sakṛn-maraṇa | death occurring all at once | mode presupposed by the Kārikā's realm counts |
| samagra-indriya | possessing complete faculties | condition of spontaneously born form-realm beings at arising and death |
| vyañjana | sexual characteristic | determines the desire-realm variation from eight to ten |

The next Bhāṣya unit contrasts gradual death, but its count and inseparable
terminal cluster belong to VAK 2.16 and are not advanced here.

## 8. Logical Determination

Terminal configuration is parameterized by realm and embodiment:

```text
TerminalFacultySet
    = f(Realm, SexualConfiguration, DeathMode)
```

For the Kārikā's simultaneous-death mode:

```text
Realm = Formless
∧ DeathMode = Simultaneous
    → TerminalFacultySet = {Life, Mind, NeutralFeeling}
    → Count = 3
```

```text
Realm = Form
∧ DeathMode = Simultaneous
    → TerminalFacultySet = {Life,
                            Mind,
                            NeutralFeeling,
                            FiveSensoryFaculties}
    → Count = 8
```

```text
Realm = Desire
∧ DeathMode = Simultaneous
    → BaseTerminalSet = {Life,
                         Mind,
                         NeutralFeeling,
                         FiveSensoryFaculties}

SexualConfiguration = None
    → Count = 8

SexualConfiguration = One
    → Count = 9

SexualConfiguration = Both
    → Count = 10
```

Initialization and termination are asymmetric:

```text
InitialVipakaSet(context)
    ≠ TerminalFacultySet(context)
```

For example:

```text
FormlessInitialVipakaSet = {Life}

FormlessTerminalFacultySet
    = {Life, Mind, NeutralFeeling}
```

The difference follows from classification scope:

```text
InitialVipakaSet
    → only faculties first acquired as maturation-result

TerminalFacultySet
    → relevant faculties possessed when the continuum ends
```

## 9. Interpretive Note

VAK 2.15 answers the inverse question to VAK 2.14, but it does not simply
reverse the preceding lists. Initial acquisition asked which faculties are
first obtained as `vipāka`. Terminal cessation asks which possessed faculties
cease at death. These are different relations over different temporal states.

The formless case makes the difference undeniable. Only life was initially
counted as maturation-result in VAK 2.14; Mind and neutral feeling were
nonetheless present at relinking, though their afflicted instances were not
counted as *vipāka*. At death, all three—Life, Mind, and neutral feeling—are
included in the terminal cessation count.

The form-realm case has the same structure. Its sixfold initial *vipāka*
count consisted of the five sensory Faculties and Life; it did not claim that
Mind and neutral feeling were absent at relinking. At death, all eight are
counted. Desire-realm terminal variation is then determined by the presence
of neither, one, or both sexual Faculties.

**Reciprocal return to Dhātu.** VAK 1.48 maps Faculty-status within
the Base–Essence–Principle architecture. VAK 2.15 applies a distinct
predicate—cessation at death—to Faculties possessed in the stated
realm-profile. The formless count excludes sensory Faculties from
this terminal set without denying their Dhātu relations.

The Bhāṣya limits these counts to death occurring all at once.
Gradual death and the five-Faculty addition with a wholesome terminal
mind are taken up at the opening of VAK 2.16. The counts therefore
should not be generalized to every mode of dying.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_15
    a vak:Karika ;
    rdfs:label "VAK 2.15" ;
    vak:hasTopic vak:TerminalFacultyCessation ;
    vak:belongsTo vak:Indriyanirdesa .

vak:FormlessTerminalProfile
    vak:ceases vak:LifeFaculty,
        vak:MindFaculty,
        vak:NeutralFeelingFaculty ;
    vak:hasCount 3 .

vak:FormTerminalProfile
    vak:ceases vak:LifeFaculty,
        vak:MindFaculty,
        vak:NeutralFeelingFaculty,
        vak:FiveSensoryFaculties ;
    vak:hasCount 8 .

vak:DesireTerminalProfile
    vak:hasBaseSet vak:FormTerminalProfile ;
    vak:variesBy vak:SexualConfiguration ;
    vak:hasPossibleCount 8,
        9,
        10 .

vak:TerminalFacultyCessation
    vak:presupposes vak:SimultaneousDeath .

organon:RealmSensitiveTermination
    a organon:InterpretiveReconstruction ;
    organon:operatesOn vak:PossessedFacultySet ;
    organon:variesBy vak:Realm,
        vak:SexualConfiguration,
        vak:DeathMode ;
    organon:inferredFrom vak:TerminalFacultyCessation .
```
