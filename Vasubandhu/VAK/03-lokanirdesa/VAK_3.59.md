# VAK_3.59 — Bhājanaloka: Cold Narakas and the Sun–Moon Measure

## 1. Sanskrit — Devanāgarī

```sanskrit
अन्येऽष्टशीतनरका अर्बुदादयः ।
सूर्याचन्द्रमसोर्मध्यं पञ्चाशदेकं योजनम् ॥ VAkK_3.59 ॥
```

## 2. Sanskrit — IAST

```iast
anye 'ṣṭaśītanarakā arvudādayaḥ /
sūryācandramasor madhyaṃ pañcāśad ekaṃ yojanam // VAkK_3.59 //
```

## 3. Source Caution

The source reading is:

```iast
anye 'ṣṭaśītanarakāḥ arvudādayaḥ /
sūryācandramasormadhyaṃ pañcāśat ekaṃ yojanam // VAkK_3.59 //
```

Sandhi has been lightly separated:

```iast
anye aṣṭa-śīta-narakāḥ arvuda-ādayaḥ /
sūrya-candramasoḥ madhyam pañcāśat ekam yojanam //
```

The source has `arvuda`, though the standard cold-naraka list often gives `arbuda`. First-pass work preserves the source form and marks it for Pass 2 verification against Pradhan and the bhāṣya.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| anye | anye | others, further ones |
| 'ṣṭaśītanarakāḥ | aṣṭa-śīta-narakāḥ | eight cold narakas |
| arvudādayaḥ | arvuda-ādayaḥ | beginning with Arvuda/Arbuda; source form preserved |
| sūryācandramasoḥ | sūrya-candramasoḥ | of the sun and moon |
| madhyam | madhyam | middle, interval, intervening space |
| pañcāśat | pañcāśat | fifty |
| ekam | ekam | one |
| yojanam | yojanam | yojana, unit of distance |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| anye | nominative plural masculine | subject qualifier: “others” |
| aṣṭa-śīta-narakāḥ | nominative plural masculine compound | subject: the eight cold narakas |
| arvuda-ādayaḥ | nominative plural masculine compound | “beginning with Arvuda/Arbuda” |
| sūrya-candramasoḥ | genitive dual masculine | “of the sun and moon” |
| madhyam | nominative/accusative singular neuter | interval or middle between them |
| pañcāśat ekam yojanam | numerical phrase | fifty-one yojanas |

## 6. Literal Translation

There are other lower-world regions: the eight cold narakas, beginning with Arvuda. The interval between the sun and moon is fifty-one yojanas.

## 7. Philosophical Translation

After the eight hot narakas and their subsidiary regions, the text adds another lower-world series: the eight cold narakas beginning with Arvuda/Arbuda. It then gives a cosmological measure for the interval between the sun and the moon: fifty-one yojanas.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| anya | other | marks a further class beyond the previously listed hot narakas |
| śīta-naraka | cold naraka | painful lower region determined by cold rather than heat |
| aṣṭa | eight | count of the cold narakas |
| Arvuda / Arbuda | Arvuda / Arbuda | first cold naraka in the list; source form to verify |
| sūrya | sun | celestial body in the cosmological measure |
| candramas | moon | celestial body in the cosmological measure |
| madhya | interval / middle | space between sun and moon |
| pañcāśad-eka | fifty-one | numerical distance measure |
| yojana | yojana | unit of cosmological distance |

## 9. Doctrinal Determination

VAkK_3.59 closes this thread’s container-world sequence by adding two final determinations:

```text
eight cold narakas
    beginning with Arvuda/Arbuda

sun–moon interval
    fifty-one yojanas
```

The lower-world series is now double:

```text
hot narakas
    → eight principal regions
    → sixteen utsadas each

cold narakas
    → eight, beginning with Arvuda/Arbuda
```

The verse then turns upward again to a celestial measure: the distance between sun and moon.

## 10. Logical Determination

```text
lower-world differentiation
    → hot narakas
        → cold narakas
            → celestial interval measure
```

The verse creates a strong closure for the block. After descending into the lower-world sequence, it returns to the sky by measuring the sun–moon interval. The container-world is therefore articulated both downward and upward.

The logical movement of VAkK_3.45–3.59 can now be summarized:

```text
support-field
    → mountains and seas
        → continents and intermediate islands
            → regional mountains and lake
                → lower-world regions
                    → celestial measure
```

## 11. Interpretive Note

VAkK_3.59 is a natural stopping point for this thread. It completes the lower-world extension by adding the cold narakas and then gives a first celestial interval. The block has moved from the foundations of the container-world to its lower and upper determinations.

For Pass 2, two points should be checked:

```text
arvuda / arbuda
    exact source form and standard list of cold narakas

sūrya-candramasoḥ madhyam
    exact interpretation of the fifty-one yojana interval
```

For Organon purposes, this closes the first large container-world arc:

```text
field
    → form
        → region
            → depth
                → sky-measure
```

## 12. OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_59 a vak:Karika ;
    rdfs:label "VAK 3.59" ;
    vak:sourceSiglum "VAkK_3.59" ;
    vak:belongsToChapter vak:Lokanirdesa ;
    vak:endsBlock vak:VAK_3c ;
    vak:continuesFrom vak:VAK_3_58 ;
    vak:hasTopic loka:ColdNarakasAndSunMoonMeasure ;
    vak:describes loka:ColdNarakaSeries , loka:SunMoonInterval .

loka:ColdNarakaSeries a owl:Class ;
    rdfs:label "eight cold narakas" ;
    rdfs:comment "The eight cold narakas beginning with Arvuda/Arbuda." .

loka:ColdNaraka a owl:Class ;
    rdfs:label "śīta-naraka" ;
    rdfs:comment "Cold lower-world region, distinct from the hot naraka series." .

loka:SunMoonInterval a owl:Class ;
    rdfs:label "sun–moon interval" ;
    rdfs:comment "The interval between sun and moon, given as fifty-one yojanas." .

loka:hasCount a owl:DatatypeProperty ;
    rdfs:label "has count" .

loka:beginsWith a owl:DatatypeProperty ;
    rdfs:label "begins with" .

loka:hasDistanceMeasure a owl:DatatypeProperty ;
    rdfs:label "has distance measure" .

loka:ColdNarakaSeries loka:hasCount "aṣṭa" ;
    loka:beginsWith "arvuda / arbuda; verify in Pass 2" .

loka:SunMoonInterval loka:hasDistanceMeasure "pañcāśad ekaṃ yojanam" .
```

## 13. Commit Note

```text
Add VAK_3.59 first-pass analysis.

Completes the VAK_3c thread target through verse 59.
Adds the eight cold narakas beginning with Arvuda/Arbuda and the sun-moon interval of fifty-one yojanas.
Marks arvuda/arbuda and the sun-moon interval for Pass 2 verification.
Ends the expanded VAK_3c container-world block.
```
